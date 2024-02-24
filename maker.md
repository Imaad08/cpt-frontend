---
layout: post
permalink: /editor
---

<head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Sixtyfour&display=swap" rel="stylesheet">
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Meme Maker</title>
    <style>
        body {
            font-family: 'Sixtyfour', sans-serif;
            background-color: #cbf6fc;
            margin: 0;
            padding: 0;
        }

        h1 {
            text-align: center;
            color: #333;
        }

        div {
            margin-bottom: 15px;
        }

        label {
            display: block;
            margin-bottom: 5px;
            color: #555;
        }

        input[type="file"],
        input[type="text"] {
            width: 100%;
            padding: 8px;
            box-sizing: border-box;
            border: 1px solid #ccc;
            border-radius: 4px;
        }

        input[type="checkbox"] {
            margin-right: 5px;
        }

        button {
            background-color: #4CAF50;
            color: #fff;
            padding: 10px;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }


        .container {
            text-align: center;
            margin-top: 20px;
        }

        .bottom-half {
            padding: 20px;
            border-radius: 4px;
            display: inline-block;
        }

        #uploadedImage {
            max-width: 100%;
            display: none;
            margin-top: 10px;
        }

        #downloadButton {
            margin-top: 10px;
        }
    </style>

</head>
<body>

<h1>Meme Maker</h1>

<div>
    <label for="imageInput">Choose Image File:</label>
    <input type="file" id="imageInput" accept="image/*">
</div>

<div>
    <label for="topText">Top Text:</label>
    <input type="text" id="topText" placeholder="Enter top text">
</div>

<div>
    <label for="bottomText">Bottom Text:</label>
    <input type="text" id="bottomText" placeholder="Enter bottom text">
</div>
            <input type="checkbox" id="addToDatabase" name="addToDatabase">
            <label for="addToDatabase">Add to Database</label>
<br>
<button class='button' onclick="makeMeme()">Generate Meme</button>

<div id="result"></div>
<div class="container">
    <div class="bottom-half">
        <h1 class="p1"><strong>Meme Result</strong></h1>
        <img id="uploadedImage" src="" alt="Uploaded Image" style="max-width: 100%; display: none;">
        <br>
        <button id="downloadButton" class="button">Download Meme</button>
        <br>
    </div>
</div>

<script>
    uploadedImageName = "";

    const options = {
        method: 'GET',
        mode: 'cors',
        cache: 'default',
        credentials: 'omit',
        headers: {
            'Content-Type': 'application/json',
        },
    };
    
    const post_options = {
        method: 'POST',
        mode: 'cors',
        cache: 'default',
        credentials: 'omit',
        headers: {
            'Content-Type': 'application/json',
        },
    };
    
    const url = "http://localhost:8762/api/memeforge/maker/";
    
    function error(message) {
        console.error(message);
    }
    
    function makeMeme() {
        const imageInput = document.getElementById('imageInput');
        const topText = document.getElementById('topText').value;
        const bottomText = document.getElementById('bottomText').value;
        const uploadedImage = document.getElementById('uploadedImage');
        const addToDatabaseCheckbox = document.getElementById('addToDatabase');

        const file = imageInput.files[0];
        if (file) {
            const reader = new FileReader();
            reader.readAsDataURL(file);
    
            reader.onload = function (e) {
                const base64data = e.target.result.split(',')[1];
                const filename = file.name;
                const fileExtension = filename.split('.').pop();
                const addToDatabase = addToDatabaseCheckbox.checked;
                uploadedImageName = file.name;
                const data = {
                    base64data: base64data,
                    top_text: topText,
                    bottom_text: bottomText,
                    addToHistory: addToDatabase,
                    filename: filename,
                };
    
                const image_options = {
                    method: 'POST',
                    mode: 'cors',
                    cache: 'default',
                    credentials: 'omit',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(data)
                };
    
                fetch(url, image_options)
                    .then(response => {
                        if (response.status !== 200) {
                            error('Api error: ' + response.status);
                            return;
                        }
                        response.json().then(data => {
                            const memeImage = new Image();
                            memeImage.src = 'data:image/' + fileExtension + ';base64,' + data['base64image'];
    
                            memeImage.style.maxHeight = '100%';
    
                            uploadedImage.src = memeImage.src;
                            uploadedImage.style.display = 'block';
    
                            memeImage.onload = function () {
                                const parent = document.querySelector('.bottom-half');
                                const ratio = parent.clientWidth / memeImage.width;
    
                                if (ratio < 1) {
                                    const maxHeight = ratio * memeImage.height;
                                    parent.style.height = (maxHeight + 175) + 'px';
                                } else {
                                    parent.style.height = (memeImage.height + 175) + 'px';
                                }
                            };
                        });
                    });
            };
        }
    }
    function handleDownloadClick() {
        const uploadedImage = document.getElementById('uploadedImage');
        const memeImage = new Image();
        memeImage.src = uploadedImage.src;

        if (uploadedImage.width == 0) {
            alert('Please upload an image before trying to download');
            return;
        }
        const downloadLink = document.createElement('a');
        downloadLink.href = memeImage.src;
        downloadLink.download = uploadedImageName.split('.')[0] + "_meme." + uploadedImageName.split('.')[1];
        downloadLink.style.display = 'none';

        document.body.appendChild(downloadLink);
        downloadLink.click();

        document.body.removeChild(downloadLink);

    }
    const downloadButton = document.getElementById('downloadButton');
    downloadButton.addEventListener('click', handleDownloadClick);
</script>

</body>
