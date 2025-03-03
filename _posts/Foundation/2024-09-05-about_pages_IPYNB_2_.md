---
layout: post
title: About Pages
description: About My Pages or smth
permalink: /about_pages
comments: True
---

## About me:
- Current student at Del Norte High School
- Current classes
    - APUSH
    - APEL
    - AP Stats
    - AP CSA
    - AP Physics E&M
- Aspiring CS major (im not getting into college)


## I love coding:
- leetcode yum
- USACO Gold

## Project ideas:
- Monkey text replacer (replace monkey words with monkey emoji)
- Monkey clicker game (cookie clicker ripoff)


<h1>Currently Solved Leetcode Questions:</h1>
<div id="responseText">Waiting for response...</div>

<script>
        // Function to make a GET request
    function updateText() {
        const url = 'https://alfa-leetcode-api.onrender.com/HanlunLi/solved';
        fetch(url)
            .then(response => response.json())
            .then(data => {
                document.getElementById('responseText').innerText = JSON.stringify(data);
            })
            .catch(error => {
                document.getElementById('responseText').innerText = 'Error: ' + error;
            });
    }

    // Call the function to update the text when the page loads
    window.onload = updateText;
</script>
