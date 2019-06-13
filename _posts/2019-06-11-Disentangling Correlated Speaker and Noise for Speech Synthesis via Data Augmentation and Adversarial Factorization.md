---
layout: post
title: "Disentangling Correlated Speaker and Noise for Speech Synthesis via Data Augmentation and Adversarial Factorization"
subtitle: Wei-Ning Hsu, Yu Zhang, Ron J. Weiss2, et al. MIT and Google. ICASSP 2019.
tags: [TTS, disentangle, multi-speaker, noise]
---
[paper](https://openreview.net/pdf?id=Bkg9ZeBB37)

### Abstract
crowed source data를 사용할때에 보통 speaker와 background noise가 correlated 되어 있는 경우가 많다. 본 논문에서는 아래 3가지 방법을 통해서 이를 해결하고자 하였다.
1. formulating a conditional generative model with factorized latent variables.
2. data augmentation을 사용해서 speaker에 correlated 되어 있지 않은 noise를 합성함, 이 데이터에 대해서는 traning 단계에서 labeling 정보가 주어질 것임.
3. using adversarial factorization to improve disentanglement.

### Introduction
crowed source data를 사용하고자 할때 나타나는 문제점.
1. background noise는 labeling 하기 힘듦. (e.g. type, level of background noise and reverberation, etc.) Labeling 된다고 하더라고, speaker labeling과 비슷하게 one-hot으로 될 수 밖에 없음.
2. Speaker들이 보통 녹음할 때 비슷한 환경에서 녹음하기 때문에 speaker와 noise 사이에는 correlatino이 생길 수 밖에 없음.

### Method
![0613](https://user-images.githubusercontent.com/27397032/59400982-267fbe80-8dd4-11e9-82c6-8c793d2c4717.PNG)

### Experiment
Baseline model: Multi Speaker Tacotron2, with phoneme
Speech synthesis: VCTK dataset.  
Noise-Speaker correlated dataset: CHiME-4 challenge dataset.

### Comment
