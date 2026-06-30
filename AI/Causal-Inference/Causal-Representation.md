# 인과적 표현 학습 (Causal Representation Learning)

- Level: Advanced
- Prerequisites: [AI/Causal-Inference/SCM.md](SCM.md), [AI/Deep-Learning/Self-Supervised.md](../Deep-Learning/Self-Supervised.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

인과적 표현 학습은 관측 데이터에서 underlying causal variables나 mechanism을 반영하는 representation을 배우려는 분야다. 목표는 분포 변화, 개입, 반사실에 더 강한 표현을 얻는 것이다.

## 직관 (Intuition)

일반 representation은 사진 속 배경과 물체를 함께 묶어 잘 예측할 수 있다. 인과적 표현은 배경이 바뀌어도 물체라는 원인 구조를 더 잘 붙잡으려 한다.

## 이론 (Theory)

핵심 난점은 관측분포만으로 causal factor를 식별하기 어렵다는 것이다. 개입 데이터, 여러 환경, temporal structure, sparsity, independence of mechanisms 같은 추가 가정이 필요하다.

Invariant risk minimization, domain generalization, disentanglement, object-centric learning은 관련 아이디어다. 하지만 invariant feature가 항상 causal feature는 아니며, shortcut이 invariant하게 보일 수도 있다.

### 식별 가능성의 벽

관측 데이터 하나만으로는 latent causal factor를 고유하게 복원하기 어렵다. 같은 joint distribution을 설명하는 서로 다른 latent variableization이 존재할 수 있기 때문이다. 그래서 causal representation learning은 보통 추가 정보를 요구한다.

- 명시적 intervention이나 weak supervision
- 여러 environment에서 바뀌는 distribution
- 시간 순서와 독립 noise 가정
- sparse mechanism 또는 modularity
- object-level inductive bias

이 추가 정보가 무엇인지 밝히지 않으면 representation을 "인과적"이라고 부르는 주장이 약해진다.

### Invariant mechanism

인과 변수의 장점은 환경이 바뀌어도 일부 메커니즘이 안정적으로 남는다는 데 있다. 예를 들어 물체의 모양이 label의 원인이고 배경은 dataset shortcut이라면, 배경 분포가 바뀌어도 모양 기반 예측은 더 안정적일 수 있다.

하지만 invariance는 필요 조건에 가까울 뿐 충분조건은 아니다. 어떤 shortcut도 모든 training environment에서 우연히 안정적이면 invariant feature처럼 보인다. 따라서 환경 선택, stress test, intervention validation이 중요하다.

### Disentanglement와 causal factor의 차이

Disentanglement는 latent dimension을 해석 가능한 축으로 분리하려는 목표다. Causal factor는 개입했을 때 downstream variable을 바꾸는 구조적 변수다. 축이 예쁘게 분리되어도 개입 의미가 없으면 causal representation이 아니다.

반대로 causal factor는 반드시 독립 latent dimension 하나에 대응하지 않을 수 있다. 여러 factor가 조합되어 mechanism을 만들거나, 관측 방식 때문에 factor가 얽혀 보일 수 있다.

### 평가 기준

좋은 causal representation 주장은 prediction accuracy만으로 평가하기 어렵다. 다음 질문을 함께 봐야 한다.

- 새로운 environment에서 성능이 유지되는가?
- 알려진 intervention을 가했을 때 representation이 예상한 방향으로 변하는가?
- Counterfactual query에 대해 구조적으로 일관된 답을 내는가?
- Shortcut을 제거하거나 바꾼 stress test에서도 안정적인가?

## 구현 (Implementation)

```python
def invariant_penalty(environment_losses):
    mean_loss = sum(environment_losses) / len(environment_losses)
    return sum((loss - mean_loss) ** 2 for loss in environment_losses)
```

이 예시는 환경별 loss가 크게 달라지는 representation에 penalty를 주는 직관이다. 실제 IRM·domain generalization 목적함수는 모델 구조와 gradient constraint를 더 엄격하게 정의한다.

## 복잡도 (Complexity)

계산 비용은 deep representation learning과 비슷하지만, 여러 environment·augmentation·intervention setting을 다루면 학습과 평가 비용이 커진다. 식별 가능성은 계산보다 가정의 문제다.

## 응용 (Applications)

- OOD generalization
- robust perception
- controllable generation
- scientific discovery와 mechanism learning

## 흔한 오해 (Common Misunderstandings)

- Disentangled representation이 곧 causal representation은 아니다.
- 여러 domain에서 안정적이면 항상 원인 feature라는 뜻은 아니다.
- Self-supervised feature가 자동으로 개입에 강한 것은 아니다.
- Causal discovery와 representation learning은 모두 강한 가정을 필요로 한다.

## TMI

- Independent causal mechanisms 가정은 각 원인 메커니즘이 독립적으로 변할 수 있다는 직관을 담는다.
- Object-centric representation은 장면을 개체 단위로 분해해 causal modeling에 유리할 수 있다.
- Interventional data가 조금만 있어도 식별성이 크게 좋아질 수 있다.

## 연습 / 확인 문제 (Exercises)

- Shortcut feature와 causal feature의 차이를 예로 설명하라.
- 여러 환경 데이터가 representation 학습에 주는 정보를 정리하라.
- 개입 데이터 없이 causal factor를 식별하기 어려운 이유를 말하라.

## 이어서 읽기 (Reading Path)

- 이전: [SCM](SCM.md), [인과적 머신러닝](Causal-ML.md)
- 다음: [AI Safety](../AI-Safety/Alignment-Overview.md)

## 참조 (References)

- [AI/Causal-Inference/SCM.md](SCM.md)
- [AI/Deep-Learning/Self-Supervised.md](../Deep-Learning/Self-Supervised.md)
- [Reference/Papers.md](../../Reference/Papers.md)
