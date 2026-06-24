# 이중 차분법 (Difference-in-Differences)

- Level: Advanced
- Prerequisites: [AI/Causal-Inference/Intervention.md](Intervention.md), [Math/Probability-Statistics/Hypothesis-Testing.md](../../Math/Probability-Statistics/Hypothesis-Testing.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

이중 차분법(DiD)은 treatment group과 control group의 전후 변화 차이를 비교해 정책이나 개입 효과를 추정하는 방법이다. 핵심 가정은 treatment가 없었다면 두 집단의 추세가 평행했을 것이라는 parallel trends다.

## 직관 (Intuition)

처치 후 treated 지역의 매출이 올랐더라도 전체 경기 호황 때문일 수 있다. 그래서 control 지역의 같은 기간 변화도 빼고, 남는 추가 변화만 처치 효과로 본다.

## 이론 (Theory)

기본 DiD estimand는 다음과 같다.

$$(\bar Y_{treated,post}-\bar Y_{treated,pre})-(\bar Y_{control,post}-\bar Y_{control,pre})$$

Parallel trends는 관측 불가능한 counterfactual trend에 대한 가정이다. Pre-trend 확인, event study, placebo test가 가정 점검에 도움을 준다. Staggered adoption에서는 treatment timing과 heterogeneous effect 때문에 더 주의해야 한다.

## 구현 (Implementation)

```python
did = (treated_post - treated_pre) - (control_post - control_pre)
```

회귀에서는 group fixed effect와 time fixed effect를 포함해 표현하는 경우가 많다.

## 복잡도 (Complexity)

기본 계산은 간단하지만 panel data, cluster correlation, staggered rollout, dynamic effect를 다루면 추정량과 표준오차가 복잡해진다.

## 응용 (Applications)

- 지역별 정책 도입 효과
- 가격 정책 변경 전후 분석
- 규제 변화 영향 분석
- phased rollout 제품 분석

## 흔한 오해 (Common Misunderstandings)

- 전후 비교만으로는 DiD가 아니다. Control group의 변화가 필요하다.
- Pre-trend가 비슷해 보여도 parallel trends가 증명되는 것은 아니다.
- Treatment 직전 행동 변화 anticipation이 있으면 bias가 생긴다.
- Staggered DiD를 단순 TWFE로 처리하면 해석이 꼬일 수 있다.

## TMI

- Event study plot은 treatment 전후의 동적 효과와 pre-trend를 동시에 보여 준다.
- Synthetic control은 좋은 control group을 가중 조합으로 만드는 관련 방법이다.
- Clustered standard error는 집단 내 시간 상관을 다룰 때 중요하다.

## 연습 / 확인 문제 (Exercises)

- 2×2 DiD 표에서 효과를 계산하라.
- Parallel trends를 위협하는 상황 3가지를 들어라.
- Event study 그래프를 해석하는 기준을 정리하라.

## 이어서 읽기 (Reading Path)

- 이전: [RCT](RCT.md), [도구 변수](Instrumental-Variables.md)
- 다음: [RDD](RDD.md)

## 참조 (References)

- [Math/Probability-Statistics/Hypothesis-Testing.md](../../Math/Probability-Statistics/Hypothesis-Testing.md)
- [Reference/Books.md](../../Reference/Books.md)
