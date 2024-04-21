<head>
    <link rel="stylesheet" href="https://pyscript.net/releases/2024.1.1/core.css" />
    <script type="module" src="https://pyscript.net/releases/2024.1.1/core.js"></script>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Sixtyfour&display=swap" rel="stylesheet">
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Gallery</title>
    <style>
        body {
            font-family: sans-serif;
            background: #cbf6fc;
            margin: 0;
            padding: 20px;
        }
        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 20px;
        }
        .gallery-item {
            position: relative;
            overflow: hidden;
        }
        .gallery-item img {
            width: 100%;
            height: auto;
            border: 2px solid gold;
            transition: transform 0.3s;
            cursor: pointer;
        }
        .gallery-item:hover img {
            transform: scale(1.1);
        }
        .modal {
            display: none;
            position: fixed;
            z-index: 1000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            overflow: auto;
            background-color: rgba(0, 0, 0, 0.8);
        }
        .modal-content {
            margin: 20px auto;
            display: block;
            max-width: 80%;
            max-height: 80%;
        }
        .close {
            color: white;
            position: absolute;
            top: 10px;
            right: 15px;
            font-size: 30px;
            font-weight: bold;
            cursor: pointer;
        }
        .close:hover {
            color: #999;
        }
    </style>
</head>

<h1>The Gallery:</h1>

<body>
    <div class="gallery">
    </div>
    <div id="modal" class="modal">
        <span class="close">&times;</span>
        <img class="modal-content" id="modal-image">
    </div>
    <script>
        const apiUrl = "http://localhost:8762/api/memeforge/get_database";
        let images = [];
        function fetchDatabase() {
            fetch(apiUrl)
                .then(response => response.json())
                .then(response => {
                    if (response.status === 401) {
                        window.location.href = '{{site.baseurl}}/login';
                        return;
                    }
                    if (response.status === 403) {
                        window.location.href = '{{site.baseurl}}/403';
                        return;
                    }
                    images = JSON.parse(response).reverse();
                    displayImages(images);
                });
        }
        function displayImages(images) {
            const gallery = document.querySelector('.gallery');
            gallery.innerHTML = '';
            images.forEach((image, index) => {
                const galleryItemContainer = document.createElement('div');
                galleryItemContainer.className = 'gallery-item';
                const img = document.createElement('img');
                img.src = 'data:image/jpeg;base64,' + image.image;
                img.alt = image.name;
                img.addEventListener('click', () => {
                    openModal(image.image);
                });
                galleryItemContainer.appendChild(img);
                gallery.appendChild(galleryItemContainer);
            });
        }
        function openModal(imageData) {
            const modal = document.getElementById('modal');
            const modalImg = document.getElementById('modal-image');
            modal.style.display = 'block';
            modalImg.src = 'data:image/jpeg;base64,' + imageData;
            const close = document.getElementsByClassName('close')[0];
            close.onclick = function () {
                modal.style.display = 'none';
            };
        }
        fetchDatabase();
    </script>
</body>