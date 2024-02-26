---
comments: True
layout: post
toc: false
title: Admin Login
permalink: /login
description: Login
type: hacks
courses: { "compsci": { "week": 2 } }
---

<head>
<link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Sixtyfour&display=swap" rel="stylesheet">
<style>
  body {
            font-family: 'Sixtyfour', sans-serif;
            background: #cbf6fc; /* Light blue gradient background */
            margin: 0;
            padding: 20px;
        }
 #login {
    margin-top: 10px;
    padding-top: 0.75rem;
    padding-bottom: 0.75rem;
    padding-left: 1rem;
    padding-right: 1rem;
    text-align: center;
    width:100%;
}
.login-container {
  border: 3px solid #888888;
  background-color: transparent;
}

input[type=text], input[type=password] {
width: 100%;
padding: 12px 20px;
margin: 8px 0;
display: inline-block;
border: 1px solid black;
box-sizing: border-box;
background-color: transparent;
}

button {
padding: 14px 20px;
margin: 8px 0;
border: none;
cursor: pointer;
width: 50%;
margin-left: 200px;
}
button {
background-color: #6466F1;
color: white;
padding: 14px 20px;
margin: 8px 0;
border: none;
cursor: pointer;
width: 50%;
margin-left: 170px;
}
button:hover {
opacity: 0.8;
}

.imgcontainer {
text-align: center;
margin: 24px 0 12px 0;
}

img.avatar {
width: 40%;
border-radius: 50%;
}

.container {
padding: 16px;
}

span.psw {
display: flex;
justify-items: center;
text-align: center;
margin-left: 250px;
padding-top: 16px;
}
span.psw2 {
display: flex;
justify-items:center
text-align: center;
margin-left: 225px;
}

@media screen and (max-width: 300px) {
span.psw {
display: block;
float: none;
}
.cancelbtn {
width: 100%;
}
}

</style>
</head>
<div class="login-container">

<form action="javascript:login_user()">
    <label for="uid"><b>Username</b></label>
    <input type="text" id="uid" placeholder="Enter Username" name="uid" required>
    <label for="password"><b>Password</b></label>
    <input type="password" id="password" placeholder="Enter Password" name="password" required>
    <button class='button'>Log in</button>
    <div>
    <span class="psw">Need an account? <a href="{{site.baseurl}}/signup"> Sign Up</a></span>
    <span class="psw2">Want to delete an account? <a href="{{site.baseurl}}/delete"> Delete</a></span>
    </div>
    <div>
    <!-- <span class="psw">Want to delete? <a href="{{site.baseurl}}/delete"> Delete</a></span> -->
    </div>

</form>
<script type="module">
    import { uri, options } from '{{site.baseurl}}/assets/js/api/config.js';
    function login_user(){
        const url = uri + '/api/users/authenticate';
        const body = {
            uid: document.getElementById("uid").value,
            password: document.getElementById("password").value,
        };
        const authOptions = {
            ...options, 
            method: 'POST', 
            cache: 'no-cache', 
            body: JSON.stringify(body)
        };
        fetch(url, authOptions)
        .then(response => {
          if (response.status === 400) {
        window.location.href = '{{site.baseurl}}/400';
        return;
      }
            if (!response.ok) {
                const errorMsg = 'Login error: ' + response.status;
                console.log(errorMsg);
                return;
            }
            window.location.href = "{{site.baseurl}}/data/database";
        })
        .catch(err => {
            console.error(err);
        });
    }
    window.login_user = login_user;

</script>
