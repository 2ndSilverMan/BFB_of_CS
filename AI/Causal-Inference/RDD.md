# 회귀 불연속 설계 (Regression Discontinuity Design)

- Level: Advanced
- Prerequisites: [AI/Causal-Inference/Intervention.md](Intervention.md), [AI/Machine-Learning/Linear-Regression.md](../Machine-Learning/Linear-Regression.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

회귀 불연속 설계(RDD)는 cutoff를 기준으로 treatment가 배정되는 상황에서 cutoff 바로 주변의 outcome jump를 인과 효과로 해석하는 방법이다.

## 직관 (Intuition)

시험 점수 80점 이상만 장학금을 받는다면, 79.9점과 80.1점 학생은 거의 비슷하지만 treatment 여부만 달라졌다고 볼 수 있다. cutoff 근처의 작은 차이를 이용한다.

## 이론 (Theory)

Running variable $R$와 cutoff $c$가 있고, treatment가 $R\ge c$에서 바뀐다. Sharp RDD는 cutoff가 treatment를 완전히 결정하고, fuzzy RDD는 treatment 확률만 불연속적으로 바뀐다.

핵심 가정은 cutoff 근처에서 잠재 결과가 연속이라는 것이다. Manipulation이나 sorting이 있으면 cutoff 주변 비교가 깨진다. Bandwidth, polynomial order, kernel 선택이 추정에 영향을 준다.

### Sharp RDD의 추정 대상

Sharp RDD에서 treatment는 $D=\mathbf{1}(R\ge c)$처럼 cutoff가 완전히 결정한다. 추정 대상은 cutoff 바로 오른쪽과 왼쪽의 조건부 평균 차이다.

$$
\tau_{SRD}
= \lim_{r\downarrow c} E[Y\mid R=r]
- \lim_{r\uparrow c} E[Y\mid R=r]
$$

이 값은 전체 population ATE가 아니라 cutoff 주변 unit에 대한 local treatment effect다. 따라서 "80점 이상 장학금" 사례에서 95점 학생에게도 같은 효과가 있다고 바로 일반화하면 안 된다.

### Fuzzy RDD와 first stage

Fuzzy RDD에서는 cutoff가 treatment 확률을 바꿀 뿐 treatment를 완전히 결정하지 않는다. 이때 outcome jump를 treatment probability jump로 나누는 Wald/IV 형태의 estimand를 사용한다.

$$
\tau_{FRD}
=
\frac{
\lim_{r\downarrow c} E[Y\mid R=r]
- \lim_{r\uparrow c} E[Y\mid R=r]
}{
\lim_{r\downarrow c} E[D\mid R=r]
- \lim_{r\uparrow c} E[D\mid R=r]
}
$$

분모가 작으면 weak first stage 문제가 생긴다. 또한 해석은 cutoff 때문에 treatment 상태가 바뀐 complier 근처의 local effect에 가깝다.

### Bandwidth, kernel, local linear

Bandwidth는 cutoff 주변을 얼마나 좁게 볼지 정한다. 좁히면 설계가 더 국소적이어서 bias가 줄 수 있지만 표본 수가 줄어 variance가 커진다. 넓히면 variance는 줄 수 있지만 cutoff에서 멀리 떨어진 관측치가 들어와 함수 형태 가정에 더 의존한다.

실무에서는 양쪽에서 local linear regression을 자주 사용한다. 경계점 근처에서는 높은 차수 polynomial보다 local linear가 안정적인 경우가 많고, triangular kernel처럼 cutoff에 가까운 관측치에 더 큰 가중치를 주는 방식이 널리 쓰인다.

### 진단과 위협

RDD의 핵심 질문은 "cutoff 바로 주변 unit이 treatment만 다르고 다른 면에서는 연속적인가"다. 이를 위해 다음을 점검한다.

- Running variable density가 cutoff에서 튀지 않는지 확인한다.
- Treatment 이전 covariate가 cutoff에서 jump하지 않는지 본다.
- 다른 가짜 cutoff(placebo cutoff)에서도 jump가 생기는지 검사한다.
- Cutoff 바로 근처 조작 가능성이 있으면 donut RDD로 민감도를 본다.

## 구현 (Implementation)

```python
def simple_rdd(outcome, running, cutoff, bandwidth):
    centered = running - cutoff
    near = abs(centered) <= bandwidth
    right = near & (centered >= 0)
    left = near & (centered < 0)
    return outcome[right].mean() - outcome[left].mean()
```

이 코드는 직관용 차이 계산이다. 실제 분석은 cutoff 양쪽에서 centered running variable을 사용한 local regression을 적합하고, bandwidth 민감도와 robust confidence interval을 함께 보고한다.

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
