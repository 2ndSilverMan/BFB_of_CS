# 교란 변수 (Confounding)

- Level: Intermediate
- Prerequisites: [AI/Causal-Inference/Correlation-vs-Causation.md](Correlation-vs-Causation.md), [AI/PGMs/d-Separation.md](../PGMs/d-Separation.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

교란(confounding)은 treatment와 outcome에 모두 영향을 주는 요인 때문에 관측 비교가 인과 효과와 달라지는 현상이다. 교란을 통제하지 않으면 효과를 과대·과소 추정하거나 방향을 잘못 볼 수 있다.

## 직관 (Intuition)

운동을 많이 하는 사람이 더 건강하다고 해서 운동 효과만 본 것은 아니다. 원래 건강한 사람이 운동을 더 잘 지속했을 수도 있고, 소득·시간·식습관이 함께 작동했을 수도 있다.

## 이론 (Theory)

그래프에서 confounder $Z$는 보통 $Z\to X$와 $Z\to Y$ 경로를 만든다. 이때 backdoor path $X\leftarrow Z\to Y$가 열려 있으면 $P(Y\mid X)$는 인과 효과와 다르다.

Backdoor criterion을 만족하는 조정 집합 $Z$가 있으면 다음처럼 조정할 수 있다.

$$P(Y\mid do(X=x))=\sum_z P(Y\mid X=x,Z=z)P(Z=z)$$

중요한 점은 mediator나 collider를 함부로 조정하면 오히려 bias가 생길 수 있다는 것이다.

## 구현 (Implementation)

```python
def adjusted_mean(p_z, mean_y_xz, x):
    return sum(p_z[z] * mean_y_xz[(x, z)] for z in p_z)
```

조정 변수는 데이터에 있는 모든 column이 아니라 인과 그래프와 연구 질문으로 선택한다.

## 복잡도 (Complexity)

조정 변수 수가 늘면 strata가 희소해지고 positivity 문제가 생긴다. 연속 변수와 고차원 변수에서는 회귀, matching, weighting, ML 기반 nuisance estimation이 필요할 수 있다.

## 응용 (Applications)

- 관측 의료 데이터 처치 효과 추정
- 광고 노출 효과 분석
- 교육 프로그램 평가
- 정책 대상자 selection bias 보정

## 흔한 오해 (Common Misunderstandings)

- 교란 변수는 outcome의 원인이기만 하면 되는 것이 아니라 treatment와도 관련 있어야 한다.
- treatment 이후 변수는 대개 confounder가 아니다.
- 모든 변수를 회귀에 넣으면 bias가 줄어든다는 보장은 없다.
- 조정 후에도 unobserved confounding은 남을 수 있다.

## TMI

- Collider를 조정하면 원래 닫힌 경로가 열릴 수 있다.
- Propensity score는 treatment 배정을 요약하지만 hidden confounder를 없애지는 못한다.
- Negative control은 잔여 교란을 진단하는 데 쓰인다.

## 연습 / 확인 문제 (Exercises)

- Confounder, mediator, collider를 각각 그래프로 그려라.
- Backdoor path를 막는 조정 집합을 찾아라.
- 관측되지 않은 교란이 있을 때 가능한 민감도 분석을 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [상관 vs 인과](Correlation-vs-Causation.md)
- 다음: [인과 DAG](Causal-DAG.md), [개입과 ATE](Intervention.md)

## 참조 (References)

- [AI/PGMs/d-Separation.md](../PGMs/d-Separation.md)
- [Reference/Books.md](../../Reference/Books.md)
