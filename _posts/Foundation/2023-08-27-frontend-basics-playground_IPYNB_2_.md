---
layout: post
title: Frontend Development
description: An introduction to HTML, CSS, and JavaScript.
categories: ['Javascript']
permalink: /frontend/basics/playground
type: ccc
courses: {'csse': {'week': 2}, 'csp': {'week': 2}, 'csa': {'week': 0}}
menu: nav/frontend_basics.html
comments: True
---

## How does HTML work?
Similar function to Markdown, syntax defines how stuff should be displayed
- HTML is based on beginning and closing tags `<tagname>content</tagname>`
  - Note the "/" on the ending or closing tag of the pair

## Compare markdown to html below
This below example shows comparison of a [heading](https://www.w3schools.com/html/html_headings.asp) and [paragraph](https://www.w3schools.com/html/html_paragraphs.asp).  Click on links to see many more HTML examples.


```python
%%markdown

### Markdown: This is a Heading

This is a paragraph

```



### Markdown: This is a Heading

This is a paragraph




```python
%%html

<h3>HTML: This is a Heading</h3>
<p>This is a paragraph.</p>
```



<h3>HTML: This is a Heading</h3>
<p>This is a paragraph.</p>



## Attributes
- Learn about [attributes](https://www.w3schools.com/html/html_attributes.asp) 
- Tags can have additional info in the form of attributes
- Attributes usually come in name/value pairs like: name="value"

```html
<tagname attribute_name="attribute_value" another_attribute="another_value">inner html text</tagname>
```

- href example with attribute for web link and inner html to describe link

```html
<a href="https://www.w3schools.com/html/default.asp">Visit W3Schools HTML Page</a>
```

## Sample Markdown vs HTML Tags
Image Tag - Markdown

```md
![describe image](link to image)
```

Image Tag - HTML

```html
<!-- no content so no end tag, width/height is optional (in pixels) -->
<img alt="describe image" src="link to image" width="100" height="200">
```

Link Tag - Markdown

```md
[link text](link)
```

Link Tag - HTML

```html
<a href="link">link text</a>
```

Bolded Text - Markdown

```md
**Bolded Text**
```

Bolded Text - HTML

```md
<strong>Bolded Text</strong>
```

Italic Text - Markdown

```md
*Italic Text*
```

Italic Text - HTML

```md
<i>Italic Text</i>
```

## More tags (not really in markdown)
P tag (just represeants a paragraph/normal text)

```html
<p>This is a paragraph</p>
```

Button

```html
<button>some button text</button>
```

Div (groups together related content)

```html
<!-- first information -->
<div>
    <!-- notice how tags can be put INSIDE eachother -->
    <p>This is the first paragarph of section 1</p>
    <p>This is the second paragraph of section 1</p>
</div>

<!-- second information -->
<div>
    <!-- notice how tags can be put INSIDE eachother -->
    <p>This is the first paragarph of section 2</p>
    <p>This is the second paragraph of section 2</p>
</div>
```



## Resources
- https://www.w3schools.com/html/default.asp

## HTML Hacks
- Below is a wireframe for an HTML element you will create. A wireframe is a rough visual representation of HTML elements on a page and isn't necessarily to scale or have the exact styling that the final HTML will have. 
- Using the syntax above, try to create an HTML cell that corresponds to the below wireframe.
- The "a tags" contain links to other content
- Pick any topic but try to match the plan



```python
%%html
<div>
    <p>i love monkeys</p>
    <button onclick="window.location.href='https://www.cnet.com/a/img/resize/a2a8684fbdcbf2d0b2b2ca48a64f8898437a5c00/hub/2014/08/06/472688a7-9be4-4a05-8c79-10199989c847/wikimonkey-cropped.jpg?auto=webp&fit=crop&height=675&width=1200'">this is a button that makes monkeys</button>
    <br>
</div>
<div>
    <a href = "https://www.cnet.com/a/img/resize/a2a8684fbdcbf2d0b2b2ca48a64f8898437a5c00/hub/2014/08/06/472688a7-9be4-4a05-8c79-10199989c847/wikimonkey-cropped.jpg?auto=webp&fit=crop&height=675&width=1200">monkey1</a>
    <br>
    <a href = "https://www.cnet.com/a/img/resize/a2a8684fbdcbf2d0b2b2ca48a64f8898437a5c00/hub/2014/08/06/472688a7-9be4-4a05-8c79-10199989c847/wikimonkey-cropped.jpg?auto=webp&fit=crop&height=675&width=1200">monkey2</a>
    <p>monkeyyys</p>
</div>
<!-- put your HTML code in this cell, Make sure to press the Run button to see your results below -->
```


<div>
    <p>i love monkeys</p>
    <button onclick="window.location.href='https://www.cnet.com/a/img/resize/a2a8684fbdcbf2d0b2b2ca48a64f8898437a5c00/hub/2014/08/06/472688a7-9be4-4a05-8c79-10199989c847/wikimonkey-cropped.jpg?auto=webp&fit=crop&height=675&width=1200'">this is a button that makes monkeys</button>
    <br>
</div>
<div>
    <a href = "https://www.cnet.com/a/img/resize/a2a8684fbdcbf2d0b2b2ca48a64f8898437a5c00/hub/2014/08/06/472688a7-9be4-4a05-8c79-10199989c847/wikimonkey-cropped.jpg?auto=webp&fit=crop&height=675&width=1200">monkey1</a>
    <br>
    <a href = "https://www.cnet.com/a/img/resize/a2a8684fbdcbf2d0b2b2ca48a64f8898437a5c00/hub/2014/08/06/472688a7-9be4-4a05-8c79-10199989c847/wikimonkey-cropped.jpg?auto=webp&fit=crop&height=675&width=1200">monkey2</a>
    <p>monkeyyys</p>
</div>
<!-- put your HTML code in this cell, Make sure to press the Run button to see your results below -->


