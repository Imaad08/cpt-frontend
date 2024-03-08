---
title: Gallery
---

<html lang="en">

<head>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Sixtyfour&display=swap" rel="stylesheet">
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Image Gallery</title>
    <style>    
        body {
            font-family: 'Sixtyfour', sans-serif;
            background: #cbf6fc; /* Light blue gradient background */
            margin: 0;
            padding: 20px;
        }
        .gallery {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); /* Larger minimum width for each image */
            gap: 20px;
        }
        .gallery-item-container {
            position: relative;
            overflow: hidden;
            animation: glow 2s infinite alternate; /* Animation for the faint, flashing gold glow */
        }
        @keyframes glow {
            0% {
                box-shadow: 0 0 10px gold;
            }
            100% {
                box-shadow: 0 0 20px gold;
            }
        }
        .gallery-item {
            position: relative;
        }
        .gallery-item img {
            width: 100%;
            height: auto;
            transition: transform 0.3s;
            cursor: pointer;
        }
        .gallery-item button {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%);
            padding: 5px 10px;
            background-color: rgba(0, 0, 0, 0.7);
            color: white;
            border: none;
            border-radius: 3px;
            font-size: 12px;
            cursor: pointer;
            opacity: 0;
            transition: opacity 0.3s;
            z-index: 1;
        }
        .gallery-item:hover img {
            transform: scale(1.1);
        }
        .gallery-item:hover button {
            opacity: 1;
        }
        /* Modal styles */
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
        .modal img {
            max-width: 100%;
            max-height: 100%;
            cursor: pointer;
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

<body>
    <div class="gallery">
        <!-- Images will be dynamically added here -->
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
        function downloadImage(imageData, imageName) {
            const link = document.createElement('a');
            link.href = 'data:image/jpeg;base64,' + imageData; // Update the MIME type if needed
            link.download = imageName;
            link.click();
        }
        function displayImages(images) {
            const gallery = document.querySelector('.gallery');
            gallery.innerHTML = '';
            images.forEach((image, index) => {
                const galleryItemContainer = document.createElement('div');
                galleryItemContainer.className = 'gallery-item-container';
                const galleryItem = document.createElement('div');
                galleryItem.className = 'gallery-item';
                const img = document.createElement('img');
                img.src = 'data:image/jpeg;base64,' + image.image;
                img.alt = image.name;
                img.addEventListener('click', () => {
                    openModal(image.image);
                });
                const button = document.createElement('button');
                button.textContent = 'Download';
                button.addEventListener('click', () => {
                    downloadImage(image.image, image.name);
                });
                galleryItem.appendChild(img);
                galleryItem.appendChild(button);
                galleryItemContainer.appendChild(galleryItem);
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

</html>
