# 무작위 실험 (Randomized Controlled Trial)

- Level: Intermediate
- Prerequisites: [AI/Causal-Inference/Intervention.md](Intervention.md), [Math/Probability-Statistics/Hypothesis-Testing.md](../../Math/Probability-Statistics/Hypothesis-Testing.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

무작위 실험(RCT)은 treatment 배정을 무작위로 정해 confounding을 평균적으로 제거하는 연구 설계다. 잘 설계된 RCT는 인과 효과 추정의 강력한 기준점이다.

## 직관 (Intuition)

동전 던지기로 treatment를 정하면 원래 건강한 사람, 적극적인 사용자, 소득이 높은 사람이 한쪽에만 몰릴 이유가 줄어든다. 그래서 두 집단의 평균 차이를 treatment 효과로 해석하기 쉬워진다.

## 이론 (Theory)

무작위 배정은 treatment $T$가 잠재 결과 $(Y(1),Y(0))$와 독립이 되게 한다. 따라서 단순 평균 차이가 ATE의 unbiased estimator가 될 수 있다.

실험 설계에서는 unit of randomization, sample size, power, blocking/stratification, interference, noncompliance, attrition을 고려한다. Online experiment에서는 metric 정의, guardrail, sequential monitoring도 중요하다.

## 구현 (Implementation)

```python
def assign(user_id, p=0.5):
    return hash(user_id) % 10000 < int(p * 10000)
```

실제 시스템에서는 stable assignment, exposure logging, sample ratio mismatch 점검이 필요하다.

## 복잡도 (Complexity)

분석 계산은 단순할 수 있지만, 충분한 power를 얻으려면 표본 수와 기간이 필요하다. Cluster randomization과 interference가 있으면 표준오차 추정이 복잡해진다.

## 응용 (Applications)

- 제품 A/B 테스트
- 의료 임상시험
- 교육 프로그램 평가
- 정책 pilot 실험

## 흔한 오해 (Common Misunderstandings)

- 무작위 배정만 하면 측정 오류와 attrition 문제가 사라지는 것은 아니다.
- P-value가 작아도 효과 크기가 실무적으로 의미 없을 수 있다.
- 실험 참여자가 서로 영향을 주면 독립성 가정이 깨진다.
- 중간 결과를 계속 보고 멈추면 오류율이 달라진다.

## TMI

- Blocking은 중요한 공변량별로 균형을 맞춰 variance를 줄인다.
- Intent-to-treat 분석은 배정 기준 효과를 본다.
- Sample ratio mismatch는 실험 플랫폼 버그의 초기 신호일 수 있다.

## 연습 / 확인 문제 (Exercises)

- Unit of randomization을 사용자/세션/클러스터 중 선택하는 기준을 설명하라.
- Guardrail metric을 설계하라.
- Noncompliance가 있는 실험에서 ITT와 treatment-on-treated를 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [개입과 ATE](Intervention.md)
- 다음: [도구 변수](Instrumental-Variables.md), [이중 차분법](DiD.md)

## 참조 (References)

- [Math/Probability-Statistics/Hypothesis-Testing.md](../../Math/Probability-Statistics/Hypothesis-Testing.md)
- [Reference/Books.md](../../Reference/Books.md)
