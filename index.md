---
layout: base
title: Student Home 
description: Home Page
hide: true
---

This is hanlun's 2024-2025 blog!!! Yippie!

<button onclick="toggleImage()">Click to see my honest reaction to CSA</button>

<div id="imageContainer"></div>

<script>
function toggleImage() {
    const imageContainer = document.getElementById("imageContainer");
    if (imageContainer.innerHTML === "") {
        const imageUrl = "{{site.baseurl}}/images/101939893-Monkey-selfie.jpg";
        const img = document.createElement("img");
        img.src = imageUrl;
        img.alt = "i love csa";
        img.style.maxWidth = "100%"; 
        imageContainer.appendChild(img);
    } else {
        imageContainer.innerHTML = "";
    }
}
</script>
