---
layout: post
title: Ubuntu Error 모음
tags: [memo]
---
---
##### librosa.load error
```
raise NoBackendError() 
audioread.NoBackendError
```
solved by installing ffmpeg:
```
conda install ffmpeg -c conda-forge
```
