# 인과적 머신러닝 (Causal Machine Learning)

- Level: Advanced
- Prerequisites: [AI/Causal-Inference/Intervention.md](Intervention.md), [AI/Machine-Learning/Cross-Validation.md](../Machine-Learning/Cross-Validation.md), [AI/Machine-Learning/Regularization.md](../Machine-Learning/Regularization.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

인과적 머신러닝은 ML을 사용해 nuisance function, heterogeneous treatment effect, policy value를 추정하면서도 인과 estimand와 식별 가정을 명확히 유지하는 접근이다.

## 직관 (Intuition)

ML은 복잡한 패턴 예측에 강하다. 하지만 인과 추론에서는 "잘 예측했다"보다 "목표 효과를 편향 없이 추정했는가"가 중요하다. 그래서 예측 모델을 인과 추정의 부품으로 조심스럽게 사용한다.

## 이론 (Theory)

대표 아이디어는 outcome model, propensity model, doubly robust estimation, orthogonalization, cross-fitting이다. CATE는 $E[Y(1)-Y(0)\mid X=x]$로 subgroup별 효과를 추정한다.

Double machine learning은 nuisance estimation error가 target parameter에 1차로 영향을 덜 주도록 orthogonal score를 구성한다. Causal forest, meta-learner(S/T/X/R-learner)는 heterogeneous effect를 모델링한다.

### 예측 문제와 인과 문제의 분리

인과적 ML에서 ML 모델은 보통 target이 아니라 부품이다. Outcome model $m(x)=E[Y\mid X=x]$, propensity model $e(x)=P(D=1\mid X=x)$, treatment effect model $\tau(x)$를 학습하더라도 최종 질문은 "어떤 estimand가 어떤 가정 아래 식별되는가"다.

따라서 validation metric도 둘로 나뉜다. 예측 성능은 nuisance model의 품질을 보는 데 필요하지만, treatment effect 추정의 편향·분산·overlap·민감도까지 대신 보장하지는 않는다.

### Orthogonalization과 Double ML

부분 선형 모형의 대표 형태는 다음과 같다.

$$
Y = \theta D + g(X) + \epsilon,\qquad D = m(X) + v
$$

Double ML은 먼저 $Y$와 $D$에서 covariate로 설명되는 부분을 제거한 residual을 만들고, residualized treatment로 residualized outcome을 설명한다. Cross-fitting을 사용하면 같은 데이터로 nuisance model을 학습하고 target score를 평가하는 overfitting bias를 줄일 수 있다.

핵심은 orthogonal score다. Nuisance model이 조금 틀려도 target parameter $\theta$에 미치는 1차 영향이 작아지도록 score를 설계한다.

### CATE와 정책 학습

CATE는 $E[Y(1)-Y(0)\mid X=x]$다. CATE가 양수인 사람에게 treatment를 주는 정책을 만들 수 있지만, 실제 정책은 비용, capacity, fairness, uncertainty를 함께 고려해야 한다. 작은 subgroup에서 큰 효과처럼 보이는 결과는 탐색적 분석과 multiple testing 문제일 수 있다.

정책 학습에서는 value를 직접 평가해야 한다. Randomized experiment가 있으면 inverse propensity weighting이나 doubly robust estimator를 쓸 수 있고, 관측 데이터에서는 unconfoundedness와 overlap 가정이 여전히 필요하다.

### Overlap과 trimming

Propensity가 0이나 1에 가까우면 한쪽 treatment 상태를 거의 관측하지 못한다. 이 구간의 CATE는 모델 extrapolation에 크게 의존한다. Propensity 분포를 보고 trimming, overlap weighting, 정책 적용 범위 제한을 검토해야 한다.

## 구현 (Implementation)

```python
def aipw_score(y, d, mu0, mu1, propensity):
    eps = 1e-6
    e = propensity.clip(eps, 1 - eps)
    treated = d * (y - mu1) / e
    control = (1 - d) * (y - mu0) / (1 - e)
    return (mu1 - mu0) + treated - control
```

`mu0`, `mu1`, `propensity`는 holdout fold에서 평가된 nuisance prediction이어야 한다. 이 score의 평균은 unconfoundedness와 overlap 아래 ATE의 doubly robust 추정량이 된다.

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
