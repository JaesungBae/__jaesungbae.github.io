---
layout: post
title: "[paper review] Disentangling Correlated Speaker and Noise for Speech Synthesis via Data Augmentation and Adversarial Factorization"
subtitle: Wei-Ning Hsu, Yu Zhang, Ron J. Weiss2, et al. MIT and Google. ICASSP 2019.
tags: [TTS, disentangle, multi-speaker, noise]
---
[paper](https://openreview.net/pdf?id=Bkg9ZeBB37)

### Abstract
crowed source data를 사용할때에 보통 speaker와 background noise가 correlated 되어 있는 경우가 많다. 본 논문에서는 아래 3가지 방법을 통해서 이를 해결하고자 하였다.
1. formulating a conditional generative model with factorized latent variables.
2. data augmentation을 사용해서 speaker에 correlated 되어 있지 않은 noise를 합성함, 이 데이터에 대해서는 traning 단계에서 labeling 정보가 주어질 것임.
3. using adversarial factorization to improve disentanglement.
