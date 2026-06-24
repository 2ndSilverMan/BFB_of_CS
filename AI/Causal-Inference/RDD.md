# 회귀 불연속 설계 (Regression Discontinuity Design)

- Level: Advanced
- Prerequisites: [AI/Causal-Inference/Intervention.md](Intervention.md), [AI/Machine-Learning/Linear-Regression.md](../Machine-Learning/Linear-Regression.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

회귀 불연속 설계(RDD)는 cutoff를 기준으로 treatment가 배정되는 상황에서 cutoff 바로 주변의 outcome jump를 인과 효과로 해석하는 방법이다.

## 직관 (Intuition)

시험 점수 80점 이상만 장학금을 받는다면, 79.9점과 80.1점 학생은 거의 비슷하지만 treatment 여부만 달라졌다고 볼 수 있다. cutoff 근처의 작은 차이를 이용한다.

## 이론 (Theory)

Running variable $R$와 cutoff $c$가 있고, treatment가 $R\ge c$에서 바뀐다. Sharp RDD는 cutoff가 treatment를 완전히 결정하고, fuzzy RDD는 treatment 확률만 불연속적으로 바뀐다.

핵심 가정은 cutoff 근처에서 잠재 결과가 연속이라는 것이다. Manipulation이나 sorting이 있으면 cutoff 주변 비교가 깨진다. Bandwidth, polynomial order, kernel 선택이 추정에 영향을 준다.

## 구현 (Implementation)

```python
near_cutoff = abs(score - cutoff) <= bandwidth
effect = mean(outcome[near_cutoff & (score >= cutoff)]) - mean(outcome[near_cutoff & (score < cutoff)])
```

실제 분석은 cutoff 양쪽 local regression과 robust confidence interval을 사용한다.

## 복잡도 (Complexity)

계산 자체는 local regression이지만 bandwidth 선택이 bias-variance tradeoff를 결정한다. Fuzzy RDD는 IV와 비슷한 ratio estimand를 사용한다.

## 응용 (Applications)

- 점수 기준 장학금·입학 정책 평가
- 소득 기준 복지 정책 효과
- 위험 점수 threshold 기반 의료 개입
- ranking cutoff 기반 노출 효과

## 흔한 오해 (Common Misunderstandings)

- RDD 효과는 cutoff 주변 local effect이지 전체 ATE가 아니다.
- Cutoff 주변에서 조작이 가능하면 설계가 약해진다.
- 높은 차수 polynomial은 경계에서 불안정할 수 있다.
- Running variable 이외의 covariate도 cutoff에서 jump하면 의심해야 한다.

## TMI

- McCrary density test는 cutoff 주변 조작 가능성을 진단하는 데 쓰인다.
- Donut RDD는 cutoff 바로 근처의 의심스러운 관측치를 제외한다.
- 여러 cutoff가 있으면 일반화 가능성을 더 살펴볼 수 있다.

## 연습 / 확인 문제 (Exercises)

- Sharp와 fuzzy RDD의 차이를 설명하라.
- Bandwidth를 넓히거나 좁힐 때 bias와 variance가 어떻게 변하는지 말하라.
- Cutoff manipulation을 탐지하는 진단을 설계하라.

## 이어서 읽기 (Reading Path)

- 이전: [이중 차분법](DiD.md), [도구 변수](Instrumental-Variables.md)
- 다음: [인과적 머신러닝](Causal-ML.md)

## 참조 (References)

- [AI/Machine-Learning/Linear-Regression.md](../Machine-Learning/Linear-Regression.md)
- [Reference/Books.md](../../Reference/Books.md)
