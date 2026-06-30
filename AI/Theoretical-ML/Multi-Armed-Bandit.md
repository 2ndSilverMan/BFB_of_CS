# 멀티암드 밴딧 (Multi-Armed Bandit)

- Level: Advanced
- Prerequisites: [Regret-Minimization.md](Regret-Minimization.md), [Expert-Algorithms.md](Expert-Algorithms.md), [Math/Probability-Statistics/Distributions.md](../../Math/Probability-Statistics/Distributions.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

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

### Feedback 구조

Bandit은 선택한 arm의 보상만 관측한다. 선택하지 않은 arm이 그 라운드에 어떤 보상을 줬을지는 모른다. 이 partial feedback이 full-information 전문가 문제보다 어렵게 만든다.

따라서 bandit 알고리즘은 좋은 arm을 찾기 위한 exploration과, 현재 좋아 보이는 arm을 선택하는 exploitation을 동시에 설계해야 한다.

### UCB의 optimism

UCB는 불확실한 arm을 낙관적으로 평가한다. 경험 평균이 낮아도 시도 횟수가 적으면 confidence bonus가 크므로 다시 선택될 수 있다. 시간이 지나며 $N_i(t)$가 늘면 bonus가 줄어들어 평균 추정이 안정된다.

이 전략은 "불확실하면 시도해 볼 가치가 있다"는 원리를 수식화한다.

### Thompson sampling

Thompson sampling은 각 arm의 보상 평균에 대한 posterior를 유지하고, posterior sample에서 가장 좋아 보이는 arm을 선택한다. 불확실성이 큰 arm은 sample에서 높게 뽑힐 가능성이 있어 자연스럽게 탐험된다.

Bayesian 구현이 직관적이지만, frequentist regret 관점에서도 분석된다.

### Contextual과 offline 평가

Contextual bandit은 사용자나 상황 feature를 보고 arm을 고른다. 이때 단순 arm 평균이 아니라 policy class와 supervised learning이 결합된다. Offline log로 새 bandit policy를 평가하려면 logging policy의 propensity가 필요하고, support가 없으면 평가가 불가능하다.

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

```python
def update_running_mean(old_mean, count, reward):
    count += 1
    new_mean = old_mean + (reward - old_mean) / count
    return new_mean, count
```

Bandit 학습은 선택한 arm의 통계만 업데이트된다는 점이 full-information online learning과 다르다.

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
