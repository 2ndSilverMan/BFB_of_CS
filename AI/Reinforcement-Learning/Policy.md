# 정책과 최적 정책 (Policy and Optimal Policy)

- Level: Intermediate
- Prerequisites: [AI/Reinforcement-Learning/MDP.md](MDP.md), [AI/Reinforcement-Learning/Value-Functions.md](Value-Functions.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

policy는 상태에서 행동을 고르는 규칙이다. 결정적(deterministic) $a=\pi(s)$이거나 확률적(stochastic) $\pi(a\mid s)$일 수 있다. 최적 정책은 모든 상태에서 기대 누적 보상을 최대화하는 정책이다.

## 직관 (Intuition)

가치 함수가 "각 상황이 얼마나 좋은가"를 말한다면, 정책은 "그래서 무엇을 할 것인가"를 정한다. 강화학습의 최종 산출물은 결국 좋은 정책이다. 가치를 알면 그것을 보고 행동을 고를 수 있고(가치 기반), 정책을 직접 학습할 수도 있다(정책 기반). 두 관점이 강화학습 방법론을 가른다.

## 이론 (Theory)

정책의 좋음은 가치로 정의된다. $\pi \ge \pi'$는 모든 상태에서 $V^\pi(s)\ge V^{\pi'}(s)$를 뜻한다. 유한 MDP에는 항상 최적 정책 $\pi^\*$가 존재하며, 최적 가치 $V^\*,Q^\*$를 공유한다.

최적 가치에서 정책을 끌어내는 것이 **greedy 정책**이다.

$$\pi^\*(s)=\arg\max_a Q^\*(s,a)$$

**정책 개선 정리**: 어떤 정책의 가치에 대해 greedy를 취하면 그 정책보다 나쁘지 않다. 이를 정책 평가와 번갈아 반복하는 것이 **policy iteration**이다.

탐험을 위해 결정적 greedy 대신 $\epsilon$-greedy나 softmax 정책을 쓴다. 정책이 미분 가능한 파라미터 $\theta$로 주어지면($\pi_\theta$) 가치를 직접 경사상승으로 올릴 수 있는데, 이는 policy gradient의 출발점이다.

## 구현 (Implementation)

```python
def policy_iteration(states, actions, P, R, gamma):
    pi = {s: actions[0] for s in states}     # 임의 초기 정책
    while True:
        V = policy_evaluation(pi, states, P, R, gamma)   # 평가
        stable = True
        for s in states:
            old = pi[s]
            pi[s] = max(actions, key=lambda a:
                sum(P[s][a][s2] * (R[s][a][s2] + gamma * V[s2]) for s2 in states))
            if pi[s] != old:                 # 개선
                stable = False
        if stable:
            return pi                        # 더 못 바꾸면 최적
```

## 복잡도 (Complexity)

policy iteration은 보통 적은 반복으로 수렴하지만, 각 반복마다 정책 평가(선형 시스템 또는 반복법)가 필요해 sweep당 `O(|S|^2|A|)` 수준이다. 실제로는 value iteration보다 반복 수는 적되 반복당 비용이 크다. 상태 공간이 크면 함수 근사 기반 정책이 필요하다.

## 응용 (Applications)

- 동적 프로그래밍 기반 최적 제어
- 가치 기반 RL의 행동 선택($\epsilon$-greedy)
- 정책 기반·actor-critic 알고리즘의 학습 대상
- 로봇·게임·추천의 의사결정 규칙

## 흔한 오해 (Common Misunderstandings)

- 최적 정책은 유일하지 않을 수 있다(같은 최적 가치를 주는 여러 정책 가능).
- 확률적 정책이 항상 나쁜 것은 아니다. 부분 관측·탐험·게임 이론적 상황에서 필요하다.
- greedy가 항상 최선은 아니다. 학습 중에는 탐험을 위해 일부러 비greedy하게 행동한다.
- 정책을 직접 학습하는 것과 가치를 학습해 행동을 고르는 것은 다른 접근이다.

## TMI

- "탐험 vs 활용(exploration-exploitation)" 딜레마는 정책 설계의 근본 긴장으로, multi-armed bandit에서 깊게 연구됐다.
- policy iteration이 value iteration보다 적은 반복으로 수렴하는 경우가 많다는 것은 고전적 관찰이다.
- 결정적 최적 정책의 존재는 유한 MDP의 중요한 이론적 보장이다.

## 연습 / 확인 문제 (Exercises)

- $\epsilon$-greedy 정책에서 $\epsilon$이 탐험·활용 균형에 어떤 영향을 주는지 설명하라.
- 정책 개선 정리를 2상태 예제에 적용해 정책이 나빠지지 않음을 확인하라.
- 확률적 정책이 결정적 정책보다 유리한 상황을 한 가지 제시하라.

## 이어서 읽기 (Reading Path)

- 이전: [가치 함수와 벨만 방정식](Value-Functions.md)
- 다음: [시간 차분 학습](TD-Learning.md), [Policy Gradient](Policy-Gradient.md)
- 관련: [동적 프로그래밍: 가치 반복과 정책 반복](Dynamic-Programming.md)

## 참조 (References)

- [AI/Reinforcement-Learning/Value-Functions.md](Value-Functions.md)
- [AI/Reinforcement-Learning/Policy-Gradient.md](Policy-Gradient.md)
- [Reference/Books.md](../../Reference/Books.md)
