# 멀티암드 밴딧 (Multi-Armed Bandit)

- Level: Advanced
- Prerequisites: [Regret-Minimization.md](Regret-Minimization.md), [Expert-Algorithms.md](Expert-Algorithms.md), [Math/Probability-Statistics/Distributions.md](../../Math/Probability-Statistics/Distributions.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

멀티암드 밴딧은 여러 행동 중 하나를 반복적으로 선택하며 보상을 관찰하는 순차 의사결정 문제다. 선택한 행동의 보상만 볼 수 있으므로 exploration과 exploitation의 균형이 핵심이다.

## 직관 (Intuition)

여러 슬롯머신이 있고 각 머신의 평균 보상을 모른다고 하자. 지금까지 좋아 보인 머신만 계속 당기면 더 좋은 머신을 놓칠 수 있고, 탐험만 하면 보상을 잃는다. 밴딧 알고리즘은 이 균형을 regret 기준으로 제어한다.

## 이론 (Theory)

$K$개 arm의 평균 보상을 $\mu_i$, 최적 평균을 $\mu^\*$라고 하자. 알고리즘의 regret은

$$
Regret_T=T\mu^\*-\sum_{t=1}^{T}E[\mu_{a_t}]
$$

로 쓴다. UCB 알고리즘은 각 arm의 경험 평균에 불확실성 bonus를 더해 선택한다.

$$
UCB_i(t)=\hat\mu_i(t)+\sqrt{\frac{2\log t}{N_i(t)}}
$$

Thompson sampling은 각 arm의 posterior에서 샘플을 뽑고 가장 좋아 보이는 arm을 선택한다. stochastic bandit에서는 gap-dependent logarithmic regret 경계가 가능하고, adversarial bandit에서는 EXP3 같은 알고리즘이 쓰인다.

## 구현 (Implementation)

UCB 선택 규칙의 핵심은 적게 시도한 arm에 보너스를 주는 것이다.

```python
import math


def choose_ucb(counts, values, t):
    for i, c in enumerate(counts):
        if c == 0:
            return i
    scores = [
        v + math.sqrt(2 * math.log(t) / c)
        for v, c in zip(values, counts)
    ]
    return max(range(len(scores)), key=lambda i: scores[i])


print(choose_ucb([10, 3, 0], [0.4, 0.6, 0.0], t=14))
```

실제 업데이트에서는 선택한 arm의 표본 평균과 count만 갱신한다.

## 복잡도 (Complexity)

기본 UCB는 라운드마다 $K$개 score를 계산하면 $O(K)$ 시간, $O(K)$ 메모리가 든다. contextual bandit이나 large action space에서는 모델 학습과 탐색 전략 비용이 추가된다.

## 응용 (Applications)

- 추천과 광고의 온라인 실험
- A/B/n 테스트의 adaptive allocation
- 하이퍼파라미터 탐색
- 강화학습의 exploration 기초

## 흔한 오해 (Common Misunderstandings)

- 밴딧은 전체 상태 전이를 다루는 일반 MDP보다 단순한 문제다.
- greedy 전략은 초기에 운 나쁘게 낮은 보상을 본 좋은 arm을 영원히 버릴 수 있다.
- regret이 낮다는 말은 모든 사용자에게 공정한 노출을 보장한다는 뜻이 아니다.
- offline log로 bandit 정책을 평가하려면 logging policy와 propensity가 중요하다.

## TMI

- contextual bandit은 사용자나 상황 feature를 보고 arm을 고른다.
- Thompson sampling은 Bayesian 직관이 강하지만 frequentist regret 분석도 연구되어 있다.
- 실제 제품 실험에서는 통계적 효율과 사용자 경험, 정책 제약을 함께 고려한다.

## 연습 / 확인 문제 (Exercises)

- exploration과 exploitation의 trade-off를 예로 설명하라.
- UCB bonus가 시도 횟수 $N_i$가 늘수록 줄어드는 이유를 말하라.
- bandit과 full-information 전문가 문제의 피드백 차이를 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [전문가 알고리즘](Expert-Algorithms.md)
- 다음: [MDL](MDL.md)

## 참조 (References)

- [Regret-Minimization.md](Regret-Minimization.md)
- [Expert-Algorithms.md](Expert-Algorithms.md)
- [Math/Probability-Statistics/Distributions.md](../../Math/Probability-Statistics/Distributions.md)
- [Reference/Books.md](../../Reference/Books.md)
