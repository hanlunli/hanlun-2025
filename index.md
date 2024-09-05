---
layout: default
title: Student Home 
description: Home Page
hide: true
comments: true
---

<style>
 p{font-family: sans-serif;}
  hr{background-color: #7e92d6;}
  .color{color:#7e92d6;}
  body {
    padding: 25px;
    background-color: #282b30;
    color: #7e92d6;
    transition-duration: 0.2s;
  }
  hr{background-color: #7e92d6;}
  .board {
      display: grid;
      grid-template-columns: repeat(3, 100px);
      grid-gap: 2px;
    }
         .cell {
      width: 100px;
      height: 100px;
      border: 1px solid #7e92d6;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 24px;
      cursor: pointer;
         }
  .notebooks {
      display: none;
      margin-top: 10px;
    }
    .notebooks a {
      display: block;
      margin: 10px 0;
      text-decoration: none;
      color: blue;
    }
    .category {
        border: 1px solid #5f73b8;
        background: #424549;
        color: white;
        width: 270px;
        padding: 15px 20px;
        font-weight: bold;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 15px;
        transition-duration: 0.1s;
        cursor: pointer;
        font-family: serif;
    }
    .category:hover {
      background-color: #7e92d6;
    }
    .submenu {
      display: none;
      padding-left: 20px;
      margin-top: 10px;
    }
    .submenu a {
      display: block;
      margin: 5px 0;
      text-decoration: none;
      color: green;
    }

</style>


<script>
function myFunction() {
  var element = document.body;
  element.classList.toggle("dark-mode");
  var elem = document.querySelectorAll("#border");
  elem.forEach(function(border) {
    border.classList.toggle("border-dark");
    });
  var bars = document.querySelectorAll("#bar");
  bars.forEach(function(bar) {
    bar.classList.toggle("bar-dark");
    });
  var cellz = document.querySelectorAll("#cells");
  cellz.forEach(function(cells) {
    cells.classList.toggle("cell");
    cells.classList.toggle("cells-dark");
    });
}
</script>


<p style="font-size:40px;font-weight:bold;"> Hanlun's Blog </p>


<iframe width="560" height="315" src="https://www.youtube.com/embed/tdCN5ZP8Kfs?si=9odSQ-QoAPcgwqNl" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
<br />
This is hanlun's 2024-2025 blog!

can't wait for another year of code code coding

<button onclick="toggleImage()">Monkey Picture Cycler</button>

<div id="imageContainer"></div>



<div id="notebooks-container" class="category">Open Notebooks</div>

<div id="notebooks" class="notebooks">
  <button onclick="window.location.href='{{site.baseurl}}/planning'" class="category">Planning</button>
  <button onclick="window.location.href='{{site.baseurl}}/javascript'" class="category">Javascript</button>
  <button onclick="window.location.href='{{site.baseurl}}/about_pages'" 
  class="category">About Pages</button>

</div>

<script>
    const categoryDiv = document.getElementById('notebooks-container');
    const notebooksDiv = document.getElementById('notebooks');
    const submenuDiv = document.getElementById('submenu');

    categoryDiv.addEventListener('click', function() {
      if (notebooksDiv.style.display === 'none' || notebooksDiv.style.display === '') {
        notebooksDiv.style.display = 'block';
      } else {
        notebooksDiv.style.display = 'none';
        submenuDiv.style.display = 'none';
      }
    });
    const categoryItems = notebooksDiv.querySelectorAll('.category');
    categoryItems.forEach(item => {
      item.addEventListener('click', function() {
        submenuDiv.style.display = 'block';
      });
    });
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
