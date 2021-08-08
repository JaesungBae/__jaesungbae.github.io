---
layout: single
title:  "Jekyll Notes"
date:   2021-04-27 21:14:06 +0900
categories: coding
---

## Jekyll local post
start wsl
```
$ bundle exec jekyll serve
```

Using math equation in github.io: [https://mkkim85.github.io/blog-apply-mathjax-to-jekyll-and-github-pages/](https://mkkim85.github.io/blog-apply-mathjax-to-jekyll-and-github-pages/)

## Image
### Centering
```css
/* 새 css class */
.center {
  display: block;
  margin: auto;
}
```
```markdown
![title](/img/myImg.png){: width="300" height="300"){: .center}
```
### Resizing
```markdown
![title](/img/myImg.png){: width="100" height="100"}
```
전체 페이지 크기를 100으로 보는 듯하다.
```markdown
![title](/img/myImg.png){: width="100%" height="100%"}
```