---
layout: post
title: "Effective Use of Variational Embedding Capacity in Expressive End-to-End Speech Synthesis"
subtitle: Eric Battenberg, Soroosh Mariooryad, Daisy Stanton, et al. Google Research. arXiv 2019.
tags: [TTS, prosody, multi-speaker]
---
[paper](https://arxiv.org/abs/1906.03402)

### Abstract

### Introduction
TTS 기술이 발전했지만, 전통적인 TTS 모델들 보다 해석(interpretalbe)이 어렵고 컨트롤이 어렵다고 종종 보여진다.  
TTS는 underdetermined problem이다. => 즉 하나의 텍스트에 대해서 무한정한 스피치가 생성될 수 있다.  
Speaker, channel chracteristics 외에 **prosody (intonation, stress and rhythm)** 가 중요 요소이다.  
Prosody는 lexical representation 너머에 존재하는 linguistic, semantic, and emotional meaning을 전달하는 요소이다.  

Reference 기반 -> GST 기반 -> Variational approach

### Measuring reference embedding capacity
#### Learning a reference embedding space
Heuristic (non-variational) end-to-end approaches: Reference Encoder, 혹은 GST 모델 등등이 모두 여기에 속한다. 이들은 teacher-forced reconstruction loss로 시작해서 학습된 뒤에, deterministic reference encdoer $$g_c(X)$$,에 의해 augmented 되곤 한다. 이때 reconstruction loss로 보통 $$l_1$$이 사용되기 때문에, liklihood는 $$f_\theta()$$에 의해 제공되는 평균과 fixed diagonal covariance를 가지는 Laplace random vector가 되게 된다. Transfer는 합성 단계에서 reference encoder에 의해 계산된 embedding을 다른 텍스트 혹은 화자와 pairing 하면서 진행됩니다.

이러한 heuristic 모델에서 reference encoder의 구조는 모델의 transfer 특징을 결정하게 됩니다. 예를들어, prosody transfer precision은 (1) embedding dimensionality (2) non-linearity의 선택 (tanh vs. softmax) (3) attention-based acrchitectural bottleneck 등에 의해 컨트롤 됩니다.
