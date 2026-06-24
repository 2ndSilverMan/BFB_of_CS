# Conditional GAN

- Level: Advanced
- Prerequisites: [AI/Generative-Models/GAN-Basics.md](GAN-Basics.md), [AI/NLP/Word-Embeddings.md](../NLP/Word-Embeddings.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

Conditional GAN은 generator와 discriminator에 label, text, mask, image 같은 조건을 함께 제공해 원하는 조건의 샘플을 생성하는 GAN이다.

## 직관 (Intuition)

그냥 "그림을 그려라"가 아니라 "숫자 7을 그려라", "말을 얼룩말처럼 바꿔라"처럼 조건을 붙이는 방식이다. 조건을 잘 쓰면 생성 결과를 제어할 수 있다.

## 이론 (Theory)

Generator는 $G(z, c)$로 noise와 condition을 함께 입력받는다. Discriminator는 $(x, c)$가 진짜 pair인지 판별한다. Class label은 embedding, spatial mask는 channel concat, text는 encoder embedding이나 cross-attention으로 넣을 수 있다.

조건을 무시하는 collapse가 생길 수 있으므로 auxiliary classifier, projection discriminator, reconstruction/consistency loss를 함께 쓰기도 한다.

## 구현 (Implementation)

```python
def conditional_input(noise, label_embedding):
    return noise + label_embedding
```

실제 구조에서는 noise와 condition의 scale, injection 위치, discriminator conditioning 방식을 실험한다.

## 복잡도 (Complexity)

조건 encoder와 fusion module이 추가된다. Class 조건은 상대적으로 싸지만 text·image·mask 조건은 encoder 비용과 alignment 문제가 커진다.

## 응용 (Applications)

- class-conditional image generation
- image-to-image translation
- super-resolution
- segmentation mask 기반 합성

## 흔한 오해 (Common Misunderstandings)

- 조건을 넣었다고 generator가 반드시 조건을 따른다는 뜻은 아니다.
- 조건 label이 noisy하면 생성 결과도 흔들린다.
- Discriminator가 조건을 보지 않으면 조건부 학습이 약해진다.
- Diversity와 condition fidelity는 tradeoff가 생길 수 있다.

## TMI

- Projection discriminator는 class embedding과 feature의 inner product로 조건 일치를 평가한다.
- Text conditioning은 단어 의미와 spatial layout 사이의 grounding이 어렵다.
- Conditional generation은 데이터 증강에서 class leakage를 특히 조심해야 한다.

## 연습 / 확인 문제 (Exercises)

- Class label 조건과 segmentation mask 조건의 입력 방식을 비교하라.
- Generator가 조건을 무시하는지 평가하는 방법을 설계하라.
- 조건부 생성에서 diversity를 측정하는 기준을 정하라.

## 이어서 읽기 (Reading Path)

- 이전: [GAN 기초](GAN-Basics.md), [DCGAN](DCGAN.md)
- 다음: [CycleGAN](CycleGAN.md), [StyleGAN](StyleGAN.md)

## 참조 (References)

- [AI/Generative-Models/GAN-Basics.md](GAN-Basics.md)
- [Reference/Papers.md](../../Reference/Papers.md)
