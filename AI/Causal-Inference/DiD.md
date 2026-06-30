# 이중 차분법 (Difference-in-Differences)

- Level: Advanced
- Prerequisites: [AI/Causal-Inference/Intervention.md](Intervention.md), [Math/Probability-Statistics/Hypothesis-Testing.md](../../Math/Probability-Statistics/Hypothesis-Testing.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

이중 차분법(DiD)은 treatment group과 control group의 전후 변화 차이를 비교해 정책이나 개입 효과를 추정하는 방법이다. 핵심 가정은 treatment가 없었다면 두 집단의 추세가 평행했을 것이라는 parallel trends다.

## 직관 (Intuition)

처치 후 treated 지역의 매출이 올랐더라도 전체 경기 호황 때문일 수 있다. 그래서 control 지역의 같은 기간 변화도 빼고, 남는 추가 변화만 처치 효과로 본다.

## 이론 (Theory)

기본 DiD estimand는 다음과 같다.

$$(\bar Y_{treated,post}-\bar Y_{treated,pre})-(\bar Y_{control,post}-\bar Y_{control,pre})$$

Parallel trends는 관측 불가능한 counterfactual trend에 대한 가정이다. Pre-trend 확인, event study, placebo test가 가정 점검에 도움을 준다. Staggered adoption에서는 treatment timing과 heterogeneous effect 때문에 더 주의해야 한다.

### 2x2 DiD와 회귀 표현

가장 단순한 2집단 2기간 설정에서는 다음 회귀의 상호작용 계수가 DiD 추정량이다.

$$
Y_{it} = \alpha + \gamma Treat_i + \lambda Post_t + \tau(Treat_i\times Post_t) + \epsilon_{it}
$$

$\tau$는 treated group이 post period에 추가로 경험한 변화다. 이 값은 "treated group의 관측된 post 결과"와 "parallel trends가 맞다면 treatment 없이 보였을 counterfactual 결과"의 차이로 해석된다.

### Parallel trends를 읽는 법

Parallel trends는 treatment 이전 수준(level)이 같다는 뜻이 아니라 trend가 같다는 뜻이다. treated group이 원래 더 높은 매출을 갖고 있어도, treatment가 없었다면 control group과 같은 방향과 속도로 움직였을 것이라고 믿을 수 있으면 DiD가 가능하다.

Pre-trend가 비슷하다는 것은 필요한 sanity check지만 충분조건은 아니다. 정책 도입 직전에 treated group이 이미 다르게 움직이기 시작했거나, treatment를 예상한 행동 변화가 있었다면 DiD는 편향될 수 있다.

### Event study와 동적 효과

Event study는 treatment 시점을 기준으로 여러 lead/lag 계수를 추정한다. Treatment 이전 lead 계수가 0에 가까우면 parallel trends 주장에 힘을 보태고, treatment 이후 lag 계수는 효과가 즉시 나타나는지, 지연되는지, 사라지는지를 보여 준다.

단, lead 계수가 유의하지 않다고 해서 가정이 증명되는 것은 아니다. 표본이 작거나 noise가 크면 위반을 발견하지 못할 수 있다.

### Staggered adoption의 함정

집단마다 treatment 도입 시점이 다르면 단순 two-way fixed effects(TWFE)는 이미 treatment를 받은 집단을 아직 받지 않은 집단의 control처럼 사용하는 문제가 생길 수 있다. 효과가 시간이나 cohort별로 다르면 가중치가 직관과 다르게 작동하고, 심하면 음의 가중치가 생겨 해석이 흐려진다.

이런 경우에는 cohort-time ATT, not-yet-treated control, interaction-weighted event study처럼 treatment timing을 명시적으로 다루는 추정량을 검토한다.

## 구현 (Implementation)

```python
def did_estimate(treated_pre, treated_post, control_pre, control_post):
    treated_change = treated_post - treated_pre
    control_change = control_post - control_pre
    return treated_change - control_change
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
