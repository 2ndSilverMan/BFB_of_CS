# 인과적 머신러닝 (Causal Machine Learning)

- Level: Advanced
- Prerequisites: [AI/Causal-Inference/Intervention.md](Intervention.md), [AI/Machine-Learning/Cross-Validation.md](../Machine-Learning/Cross-Validation.md), [AI/Machine-Learning/Regularization.md](../Machine-Learning/Regularization.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

인과적 머신러닝은 ML을 사용해 nuisance function, heterogeneous treatment effect, policy value를 추정하면서도 인과 estimand와 식별 가정을 명확히 유지하는 접근이다.

## 직관 (Intuition)

ML은 복잡한 패턴 예측에 강하다. 하지만 인과 추론에서는 "잘 예측했다"보다 "목표 효과를 편향 없이 추정했는가"가 중요하다. 그래서 예측 모델을 인과 추정의 부품으로 조심스럽게 사용한다.

## 이론 (Theory)

대표 아이디어는 outcome model, propensity model, doubly robust estimation, orthogonalization, cross-fitting이다. CATE는 $E[Y(1)-Y(0)\mid X=x]$로 subgroup별 효과를 추정한다.

Double machine learning은 nuisance estimation error가 target parameter에 1차로 영향을 덜 주도록 orthogonal score를 구성한다. Causal forest, meta-learner(S/T/X/R-learner)는 heterogeneous effect를 모델링한다.

## 구현 (Implementation)

```python
pipeline = [
    "estimate propensity e(x)",
    "estimate outcome m(x)",
    "construct orthogonal score",
    "cross-fit to reduce overfitting bias",
]
```

예측 검증과 인과 추정 검증은 분리해야 한다.

## 복잡도 (Complexity)

ML 모델 비용에 더해 cross-fitting fold 수만큼 학습이 반복된다. 고차원 confounder에서는 variance, overlap, regularization 선택이 중요하다.

## 응용 (Applications)

- 개인화 처치 효과 추정
- uplift modeling
- 정책 학습과 off-policy evaluation
- 고차원 관측 연구 보정

## 흔한 오해 (Common Misunderstandings)

- ML을 쓰면 unobserved confounding이 사라지는 것은 아니다.
- 높은 outcome prediction 성능이 좋은 treatment effect 추정을 보장하지 않는다.
- CATE 추정은 subgroup 탐색의 multiple testing 위험을 가진다.
- Propensity가 0이나 1에 가까우면 ML도 positivity 문제를 해결하지 못한다.

## TMI

- Orthogonal score는 nuisance model 오차에 둔감한 추정 방정식이다.
- Uplift modeling은 treatment를 줄 대상과 말 대상을 나누는 제품 의사결정에 자주 쓰인다.
- Off-policy evaluation은 추천·RL과 인과 추론이 만나는 지점이다.

## 연습 / 확인 문제 (Exercises)

- Outcome model과 propensity model의 역할을 비교하라.
- Cross-fitting이 overfitting bias를 줄이는 이유를 설명하라.
- CATE 결과를 제품 정책으로 바꿀 때 필요한 guardrail을 설계하라.

## 이어서 읽기 (Reading Path)

- 이전: [개입과 ATE](Intervention.md), [RDD](RDD.md)
- 다음: [인과적 표현 학습](Causal-Representation.md)

## 참조 (References)

- [AI/Machine-Learning/Cross-Validation.md](../Machine-Learning/Cross-Validation.md)
- [Reference/Papers.md](../../Reference/Papers.md)
