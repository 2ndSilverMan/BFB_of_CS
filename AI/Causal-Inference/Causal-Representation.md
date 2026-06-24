# 인과적 표현 학습 (Causal Representation Learning)

- Level: Advanced
- Prerequisites: [AI/Causal-Inference/SCM.md](SCM.md), [AI/Deep-Learning/Self-Supervised.md](../Deep-Learning/Self-Supervised.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

인과적 표현 학습은 관측 데이터에서 underlying causal variables나 mechanism을 반영하는 representation을 배우려는 분야다. 목표는 분포 변화, 개입, 반사실에 더 강한 표현을 얻는 것이다.

## 직관 (Intuition)

일반 representation은 사진 속 배경과 물체를 함께 묶어 잘 예측할 수 있다. 인과적 표현은 배경이 바뀌어도 물체라는 원인 구조를 더 잘 붙잡으려 한다.

## 이론 (Theory)

핵심 난점은 관측분포만으로 causal factor를 식별하기 어렵다는 것이다. 개입 데이터, 여러 환경, temporal structure, sparsity, independence of mechanisms 같은 추가 가정이 필요하다.

Invariant risk minimization, domain generalization, disentanglement, object-centric learning은 관련 아이디어다. 하지만 invariant feature가 항상 causal feature는 아니며, shortcut이 invariant하게 보일 수도 있다.

## 구현 (Implementation)

```python
objective = {
    "predictive": "fit labels",
    "invariance": "stable across environments",
    "disentanglement": "separate latent factors",
}
```

환경 정의와 개입 정보가 약하면 representation 해석에 특히 주의해야 한다.

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
