# Sparse Autoencoder를 이용한 특성 분해 (Sparse Autoencoders for Feature Decomposition)

- Level: Advanced
- Prerequisites: [Mechanistic-Interpretability.md](Mechanistic-Interpretability.md), [AI/Deep-Learning/Activation-Functions.md](../Deep-Learning/Activation-Functions.md), [Math/Linear-Algebra/Vectors.md](../../Math/Linear-Algebra/Vectors.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

Sparse autoencoder(SAE)는 신경망 activation을 더 많은 잠재 feature의 희소 조합으로 복원하도록 학습하는 모델이다. 해석 가능성에서는 superposition된 내부 표현을 분해해 사람이 이해할 수 있는 feature 후보를 찾는 데 사용한다.

## 직관 (Intuition)

모델의 한 activation 차원이 여러 의미를 겹쳐 담고 있다면, 원래 좌표만 봐서는 해석하기 어렵다. SAE는 더 넓은 사전(dictionary)을 만들고, 각 입력마다 그중 소수 feature만 켜지게 하여 “이 activation은 어떤 feature들의 조합인가”를 보려 한다.

## 이론 (Theory)

기본 autoencoder는 encoder $z=f_\theta(a)$와 decoder $\hat a=g_\phi(z)$로 activation $a$를 복원한다. Sparse autoencoder는 여기에 희소성 penalty를 추가한다.

$$
L = \|a-\hat a\|_2^2 + \lambda \|z\|_1
$$

또는 top-k 활성화처럼 각 입력에서 켜지는 feature 수를 직접 제한한다. 해석 가능성에서 중요한 것은 낮은 복원 오차와 높은 sparsity 사이의 균형이다. feature가 너무 많이 켜지면 해석이 어렵고, 너무 적게 켜지면 중요한 정보를 잃는다.

### Overcomplete dictionary

SAE는 원래 activation 차원보다 더 많은 latent feature를 둘 수 있다. 이를 overcomplete dictionary라고 한다. 목적은 하나의 좌표에 겹쳐 들어간 feature를 더 많은 축으로 펼쳐, 각 입력에서 소수 feature만 활성화되게 만드는 것이다.

하지만 latent 수를 늘리면 feature 후보가 많아지고, 비슷한 feature가 중복되거나 dead feature가 늘 수 있다. 따라서 reconstruction loss, sparsity, feature activation frequency를 함께 본다.

### Feature 해석 절차

SAE feature를 해석할 때는 보통 다음 단계를 따른다.

1. Feature가 강하게 켜지는 top activating examples를 모은다.
2. 공통 token, 문맥, task pattern을 사람이 또는 보조 모델로 요약한다.
3. Feature activation과 downstream metric의 상관을 확인한다.
4. Feature를 ablation하거나 steering해 출력이 예상대로 바뀌는지 본다.
5. 반례와 negative example을 찾아 feature 이름을 수정한다.

Feature label은 발견이 아니라 가설이다. 이름을 붙인 뒤 개입으로 검증해야 한다.

### Monosemanticity와 polysemanticity

Monosemantic feature는 한 가지 해석 가능한 개념에 주로 대응하는 feature다. Polysemantic feature는 여러 unrelated concept에 반응한다. SAE는 monosemantic feature를 늘리려는 도구지만, 모든 feature가 깨끗하게 분리되지는 않는다.

안전 분석에서는 "독성", "거절", "권한 요청", "비밀 정보" 같은 feature 후보를 찾더라도, 실제 정책 결정에 쓰기 전에 domain별 false positive와 false negative를 측정해야 한다.

### Causal intervention과 연결

SAE feature가 어떤 행동과 관련 있어 보이면, 해당 feature를 줄이거나 키워 출력 변화를 본다. 이때 feature steering은 distribution shift를 만들 수 있으므로, 작은 개입 크기와 control feature 비교가 필요하다.

## 구현 (Implementation)

아래는 학습 루프의 핵심 손실 형태를 단순화한 예다.

```python
def sae_loss(activation, reconstruction, latent, l1_weight):
    recon_error = sum((a - r) ** 2 for a, r in zip(activation, reconstruction))
    sparsity = sum(abs(z) for z in latent)
    return recon_error + l1_weight * sparsity


activation = [0.2, -0.5, 1.1]
reconstruction = [0.1, -0.4, 1.0]
latent = [0.0, 1.3, 0.0, 0.2]

print(round(sae_loss(activation, reconstruction, latent, 0.05), 3))
```

실제 분석에서는 학습된 feature가 언제 켜지는지, 어떤 토큰/문맥에서 활성화되는지, 개입하면 출력이 바뀌는지까지 확인한다.

```python
def feature_sparsity(latents):
    active = sum(1 for value in latents if abs(value) > 1e-6)
    return active / len(latents)
```

Sparsity는 낮을수록 해석이 쉬울 수 있지만, 너무 낮으면 복원에 필요한 정보를 잃는다.

## 복잡도 (Complexity)

SAE 학습 비용은 수집한 activation 수, 원래 차원, latent feature 수에 비례한다. 대형 모델의 여러 layer에 대해 SAE를 학습하면 저장 공간과 계산량이 크게 증가한다. feature 해석에는 자동 통계와 사람 검토가 모두 필요하다.

## 응용 (Applications)

- transformer activation feature 분해
- 안전 관련 feature 후보 탐색
- 모델 내부 지식과 거부 행동 분석
- activation steering과 causal intervention 연구의 기반

## 흔한 오해 (Common Misunderstandings)

- SAE feature가 자동으로 사람 개념과 1:1 대응하는 것은 아니다.
- reconstruction이 좋다고 해석 가능성이 보장되는 것은 아니다.
- 희소성이 높을수록 항상 좋은 것은 아니다. 정보 손실이 커질 수 있다.
- feature 이름 붙이기는 가설이며, 별도 검증이 필요하다.

## TMI

- overcomplete dictionary는 원래 activation 차원보다 더 많은 feature를 두어 superposition을 풀려는 전략이다.
- dead feature는 거의 켜지지 않는 feature로, 학습 설정을 조정해야 할 신호일 수 있다.
- SAE 분석은 feature 발견, feature 설명, feature 개입이라는 세 단계를 나눠 보는 것이 안전하다.

## 연습 / 확인 문제 (Exercises)

- L1 penalty가 latent를 sparse하게 만드는 이유를 설명하라.
- 낮은 복원 오차와 높은 해석 가능성이 충돌할 수 있는 예를 들어라.
- 어떤 feature가 “거절 행동”과 관련 있다고 주장하려면 어떤 추가 실험이 필요한가?

## 이어서 읽기 (Reading Path)

- 이전: [기계적 해석 가능성](Mechanistic-Interpretability.md)
- 다음: [적대적 예제](Adversarial-Examples.md)

## 참조 (References)

- [Mechanistic-Interpretability.md](Mechanistic-Interpretability.md)
- [AI/Deep-Learning/Activation-Functions.md](../Deep-Learning/Activation-Functions.md)
- [Math/Linear-Algebra/Vectors.md](../../Math/Linear-Algebra/Vectors.md)
- [Reference/Books.md](../../Reference/Books.md)
