---
layout: single
title:  "[PR] AdaSpeech 2: Adaptive Text-to-Speech With Untranscribed Data"
date:   2021-04-27 21:14:06 +0900
categories: paper-review icassp2021 tts:model
use_math: true
toc: true
---

*Yuzi Yan, Xu Tan, Bohan Li, et al.* \
Department of Electronic Engineering, Tsinghua University, Beijing, China & Microsoft Research Asia & Microsoft Azure Speech \
Arxiv: [https://arxiv.org/pdf/2104.09715.pdf](https://arxiv.org/pdf/2104.09715.pdf)

## Abstract
* Well-trained source TTS model is fine-tuned with few paired adaptation data 하는 방식으로 personal voice 생성에 많이 활용되고 있음. **그러나 untranscribed data만 주어지는 경우도 많음.**
* AdaSpeech2: adaptive TTS system that only leverages untranscribed speech data for adaptation
    1. 잘 학습된 TTS model에 mel-spectrogram encoder를 도입해서 speech reconstruction 수행하도록 함.
    1. 동시에 mel-spectrogram encoder의 output sequence가 원래 phoneme encoder의 output sequence와 가깝도록 함.
    1. Adaptation 단계에서, untranscribed data를 speech reconstruction에 이용해서 TTS decoder만을 fine-tune시킴.
* AdaSpeech2 장점
    1. Pluggable: 기존에 존재하는 TTS model에 손쉽게 적용이 가능함.
    1. Effective:  transcribed data로 TTS adaptation 수행하는 것과 동일한 성능을 보였으며, 기존의 untranscribed adaptation method 보다 나은 성능을 보여줌.

## 1. Introduction
* Task: TTS adaptation => untranscribed dataset
    * fine-tunes a well-trained multi-speaker TTS model with few adaptation data
    * paired speech data: untranscribed dataset 보다 얻기 힘들다.
* 기존 Approach
    1. Basic Method: ASR로 untranscribed data -> transcribe 하기 
        * 문제점1. This additional ASR system may not be available in some scenarios
        * 문제점2. Recognition accuracy is not high enough which will generate incorrect transcripts and affect the adaptation. 
    2. Joint training Method
        * Joint training of TTS pipeline and the modules used for adaptation. 
        * 문제점1. Not pluggable and restricts their method to be extended to other common TTS models.
* AdaSpeech2
    * Leverages untranscribed speech data for adaptation.
    * AdaSpeech를 basic structure로써 사용. (Phoneme encoder + mel-decoder)

    1. Training
        * a) Introduce a mel-encoder into the well-trained source TTS model for speech reconstruction together with the mel decoder
        * b) Output sequence of the mel-encoder to be close to that of the phoneme encoder (L2 loss)
    2. Adaptation
        * Untranscribed speech data를 speech reconstruction을 위해 사용하고, mel-decoder만 fine-tuning 함.
    3. Inference
        * Fine-tuned mel decoder + phoneme encoder => synthesize custom voice for target speaker
    
    * Two advantages
        1. **Pluggable:** 핵심은 additional encoder를 이미 학습된 TTS에 추가하는 것! 그러므로 이미 존재하는 TTS에 손쉽게 적용 가능함
        2. **Effective:** It achieves on-par voice quality with the transcribed TTS adaptation, with the same amount of untranscribed data. 

## 2. Method
![f2](/images/2021-05-11-PR_Adaspeech2/f2.PNG){: width="50%" height="50%" .center}

* Two main modules:
    1. TTS Model pipeline: phoneme encoder + mel-decoder
    2. Mel-Encoder
* Steps
    1. Source model training
    2. Mel-encoder aligning
        * Alignment loss를 사용해서 mel encoder의 output space가 phoneme encoder와 가까워지도록 함.
    3. Untranscribed speech adaptation
        * Mel-decoder가 mel-encoder의 도움을 받아 target speaker에 대해서 adaptation 됨.
    4. Inference
        * phoneme-encoder와 mel-decoder 이용해서 음성 생성

### 2.1. Source Model Training
![f1](/images/2021-05-11-PR_Adaspeech2/f1.PNG){: width="50%" height="50%" .center}

* AdaSpeech 구조 따름
    * specifically designed acoustic condition modeling + conditional layer normalization
    * Phoneme-encoder
        * 4개의 FFT block
        * GT duration 사용해서 upsampling
        * GT duration extraction에 MFA 사용됨
    * Mel-decoder
        * 4개의 FFT Block
        * Adds more variance information including pitch & more phoneme-level acoustic condition info. (AdaSpeech)

### 2.2. Mel-spectrogram encoder aligning
* Mel-decoder의 입장에서 phoneme encoder와 mel-encoder의 output들이 동일한 space에 존재할 것이라고 기대할 것임.
* 그래야 untranscribed speech data로 adaptation한 것이 inference시에 smooth하게 switching이 가능할 것임.
* TTS Model 잘 training 한 뒤에 source transcribed speech dataset 이용하여 eml-encoder가 phoneme-encoder와 가까워지도록 학습함. (L2 loss)
    * Source TTS model (phoneme encoder, mel decoder)는 freeze해서 학습시킴.
    * 이를 통해서 pluggable한 모델이 될 수 있음.

### 2.3. Untranscribed speech adaptation
* Only adapt the parameters related to the conditional layer normalization (AdaSpeech)
    * small amount of parameter만 adapt 해도 됨.

### 2.4. Inference
pass

## 3. Experiments and results
### 3.1. Datasets and Experimental Setup
* Data
    * Source: Libri TTS (586 h & 2456 speakers)
    * Adapt: VCTK (44 h & 1 speaker), LJSpeech (single & 24 h)
    * 실제 발화 상황과 유사한 internal dataset
* Preprocessing
    * 16KHz down sampling
    * 12.5 ms hop size & 50 ms window size
    * G2p를 통한 phoneme 변환
* Setup
    * Hidden dimension = 256 (including the embedding size, the hidden in self-attention, and the input and output of feed-forward network)
    * Attention head = 2 & feed-forward filter size = 1024 & kernel size = 9
* Training
    * 100k steps to optimize the TTS pipeline
    * 10k step to train mel-encoder
    * 2k step for adaptation (mel-decoder)
    * Adam optimizer is used with β1 = 0.9, β2 = 0.98,  = 10−9

### 3.2.  The Quality of Adaptation Voice
* 비교모델
    1. GT
    1. GT mel + Vocoder (MelGAN)
    1. a joint training method
        * Trains the mel-encoder and the phoneme encoder at the same time
            * Similar to some previous adaptable TTS systems using untranscribed data [12]. 
        * 제안한 orderly training strategy가 효과적으로 mel-encoder가 encoder의 output space로 부터 멀어지는 것을 방지하여주고, 성능도 높아지는 것을 증명하기 위한 ***baseline 모델***로 사용.
    1. a PPG-based method
        * Mel-encoder 대신에 PPG-encoder 사용함. (structure는 같음, input만 다름)
        * Uses PPGs (phonetic posteriorgrams) [22, 23] extracted from the untranscribed speech to fine-tune the TTS model. 
            * 내부 ASR 모델을 이용하여 512차원의 PPG extraction  (mel과 길이는 같음)
            * Dense layer 이용해서 256 dim으로 줄인다음 PPG encoder의 input으로 사용됨.
        * PPG-based method를 ***upper bound***로 설정함. 
            * 추가적인 ASR을 이용하여 text/phoneme과 유사한 정보인 PPG를 뽑아내기 때문에
    1. AdaSpeech [8].
        * Previous TTS adaptation system using **paired text and speech (transcribed speech) data.**
        * We take its performance as another ***upper bound.***

![t1](/images/2021-05-11-PR_Adaspeech2/t1.PNG){: width="50%" height="50%" .center}
* Evaluation (MOS & SMOS)
    * Twenty native English speakers are asked to make quality judgments in terms of naturalness and similarity
* 결과
    1. GT recording & 2개의 upper bound 모델들 (AdaSpeech & the PPG-based method)에 동등한 성능 보임. Joint-training 보다는 월등히 뛰어난 성능 보임.
    2. SMOS에 대해서는 upper bound model 보다 약간 안좋은 (0.1점) 성능 보임. 그러나 여전히 Joint-training 보다는 월등히 좋음
    3. Transcribed가 있는 경우 (AdaSpeech) 와 없는 경우 (AdaSpeech2)에 대해서 CMOS 비교도 수행함. 
        * Internal spontaneous speech data에 대해서 실험 수행
        * 비슷한 성능 보임 (AdaSpeech가 0.012 CMOS socre 보임)

### <span style="color:red">3.3. Analyses on Adaptation Strategy (2가지 실험)</span>
![t2](/images/2021-05-11-PR_Adaspeech2/t2.PNG){: width="50%" height="50%" .center}
* 실험 1. W/o L2 loss constraint
    * L2 loss를 통해서 mel-encoder phoneme encoder 가깝게 하는 것의 효과를 관찰하기 위한 ablation study.
* 실험 2. Fine-tune mel encoder & decoder
    * Mel-decoder 뿐만아니라 mel-encoder도 함께 fine-tuning 했을 때의 성능 관찰
    * Voice Qaulity 저하
    * (그러므로) encoder를 변하지 않도록 하는것이 adaptation performance에 긍정적인 영향을 미친다

### <span style="color:red">3.4. Varying Adaptation Data</span>
![f3](/images/2021-05-11-PR_Adaspeech2/f3.PNG){: width="30%" height="30%" .center}

* 샘플 개수에 따른 CMOS evaluation
* 20개 이하일 때 sample 개수가 증가할수록 MOS 점수가 급격하게 증가하는 것을 관찰할 수 있음
* 그러나 이후에는 그렇게 증가가 크지 않음을 관찰할 수 있음

## 4. Conclusion and Comments
* AdaSpeech2
    * pluggable & effective
    * **<span style="color:red">Untranscribed speech data로 adaptation 수행하는 TTS 모델</span>**
    * Upper bound system과 유사한 성능의 MOS와 SMOS 점수 획득
* Future work 
    * We will explore different adaptation methods to improve voice quality and similarity and further extend our method to more challenging scenarios such as spontaneous speech.

***Comments***
* Untranscribed speech dataset을 이용하여 speaker adaptation 수행할 수 있다는 점에서 task 선택 good
* 그리고 뭔가 아이디어 자체가 엄청 특별하지 않지만 신선함. good










<!-- **<span style="color:red">하나의 blank symbol이 모든 2개의 token사이의 transition을 표현할 수 있는가?</span>** -->
<!-- ![1](/images/2021-05-04-PR_talknet2/1.PNG){: .center} -->