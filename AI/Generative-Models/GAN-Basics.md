# GAN 기초와 학습 안정성 (GAN Basics)

- Level: Advanced
- Prerequisites: [AI/Deep-Learning/Backpropagation.md](../Deep-Learning/Backpropagation.md), [Math/Optimization/SGD.md](../../Math/Optimization/SGD.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

GAN은 generator가 가짜 샘플을 만들고 discriminator가 real과 fake를 구분하는 adversarial game으로 데이터분포를 학습한다.

## 직관 (Intuition)

위조범과 감별사가 경쟁하며 함께 실력이 오른다. 감별사는 진짜와 가짜를 구별하고, 생성자는 감별사를 속일 만큼 그럴듯한 샘플을 만든다.

## 이론 (Theory)

원래 minimax 목적은

$$\min_G\max_D E_{x\sim p_{data}}\log D(x)+E_{z\sim p(z)}\log(1-D(G(z)))$$

다. 실제 generator에는 gradient가 더 강한 non-saturating loss를 자주 쓴다. 두 모델의 동적 균형 때문에 mode collapse, oscillation, vanishing gradient가 생길 수 있다. normalization, architecture, learning-rate 균형과 Wasserstein 계열 목적이 안정화를 돕는다.

## 구현 (Implementation)

```python
def training_step(real_batch, noise, generator, discriminator, optim_d, optim_g):
    fake = generator(noise)
    loss_d = discriminator.loss(real_batch, fake.detach())
    optim_d.step(loss_d)
    loss_g = generator.loss(discriminator(fake))
    optim_g.step(loss_g)
```

이는 학습 순서를 보여 주는 pseudocode다.

## 복잡도 (Complexity)

한 반복은 generator와 discriminator의 forward/backward를 모두 수행한다. 비용과 메모리는 두 network 크기와 update 비율에 좌우된다.

## 응용 (Applications)

- image·audio synthesis
- super-resolution과 image translation
- data augmentation 연구
- domain adaptation

## 흔한 오해 (Common Misunderstandings)

- discriminator accuracy가 높을수록 전체 학습이 항상 좋은 것은 아니다.
- loss 값만으로 sample quality와 diversity를 판단하기 어렵다.
- mode collapse는 일부 종류만 반복 생성하는 실패다.
- 생성 데이터 사용은 privacy·bias·license 검토가 필요하다.

## TMI

- Nash equilibrium 관점이지만 실제 nonconvex training은 이상적 균형에 쉽게 도달하지 않는다.
- FID는 feature 분포를 비교하지만 표본 수와 domain에 민감하다.
- conditional GAN은 label·text 같은 조건을 양쪽 모델에 제공한다.

## 연습 / 확인 문제 (Exercises)

- discriminator가 너무 강할 때 generator gradient를 설명하라.
- mode collapse를 탐지할 평가를 설계하라.
- minimax와 non-saturating generator loss를 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [VAE](VAE.md)
- 다음: [DCGAN](DCGAN.md), [Conditional GAN](Conditional-GAN.md), [DDPM](DDPM.md)

## 참조 (References)

- [Math/Optimization/SGD.md](../../Math/Optimization/SGD.md)
- [Reference/Papers.md](../../Reference/Papers.md)
- [Reference/Books.md](../../Reference/Books.md)
