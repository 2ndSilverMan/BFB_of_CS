# 동적 프로그래밍: 가치 반복과 정책 반복 (Dynamic Programming for RL)

- Level: Advanced
- Prerequisites: [MDP.md](MDP.md), [Value-Functions.md](Value-Functions.md), [Policy.md](Policy.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

강화학습에서 동적 프로그래밍은 MDP의 전이확률과 보상 함수를 알고 있을 때 최적 가치 함수와 최적 정책을 계산하는 방법이다. 대표 알고리즘은 policy evaluation, policy iteration, value iteration이다.

## 직관 (Intuition)

미로의 모든 칸에서 어느 방향으로 가면 어디로 이동하고 보상이 얼마인지 이미 알고 있다고 하자. 그러면 직접 수없이 시행착오를 하지 않아도, “다음 칸의 가치”를 거꾸로 전파하며 각 칸의 최선 행동을 계산할 수 있다.

## 이론 (Theory)

정책 $\pi$의 상태 가치 함수는 Bellman expectation equation을 만족한다.

$$
V^\pi(s)=\sum_a\pi(a\mid s)\sum_{s'}P(s'\mid s,a)\left[R(s,a,s')+\gamma V^\pi(s')\right]
$$

최적 가치 함수는 Bellman optimality equation을 만족한다.

$$
V^\*(s)=\max_a\sum_{s'}P(s'\mid s,a)\left[R(s,a,s')+\gamma V^\*(s')\right]
$$

Policy iteration은 현재 정책을 평가한 뒤 그 가치에 대해 탐욕적으로 정책을 개선한다. Value iteration은 평가와 개선을 한 업데이트에 섞어 최적 Bellman backup을 반복한다.

### Policy evaluation

정책 평가(policy evaluation)는 고정된 정책 $\pi$의 가치 $V^\pi$를 구한다. 정확히 풀려면 선형 방정식을 풀 수 있고, 반복식으로는 다음 업데이트를 수렴할 때까지 적용한다.

$$
V_{k+1}(s)\leftarrow \sum_a\pi(a\mid s)\sum_{s'}P(s'\mid s,a)[R(s,a,s')+\gamma V_k(s')]
$$

평가는 control이 아니라 prediction 문제다. "이 정책을 따르면 얼마나 좋은가"를 묻는다.

### Policy improvement

정책 개선은 현재 가치에 대해 greedy 행동을 선택한다.

$$
\pi_{new}(s)=\arg\max_a\sum_{s'}P(s'\mid s,a)[R(s,a,s')+\gamma V^\pi(s')]
$$

정책 개선 정리에 의해 새 정책은 기존 정책보다 나쁘지 않다. Policy iteration은 evaluation과 improvement를 번갈아 수행한다.

### Value iteration과 truncated evaluation

Value iteration은 완전한 정책 평가를 기다리지 않고 최적 backup을 반복한다. 이는 policy evaluation을 한두 step만 하고 곧바로 improvement를 섞는 것으로 볼 수 있다. 이 때문에 반복당 비용은 낮지만, 수렴 전의 greedy policy는 불안정할 수 있다.

### Generalized policy iteration

대부분의 RL 알고리즘은 generalized policy iteration(GPI)의 변형이다. Critic은 정책을 평가하고, actor 또는 greedy step은 정책을 개선한다. 두 과정이 완전히 끝나지 않아도 서로 밀고 당기며 좋은 정책으로 이동한다.

## 구현 (Implementation)

Value iteration의 핵심 업데이트는 다음과 같다.

```python
def value_iteration_step(states, actions, transition, reward, v, gamma):
    new_v = {}
    for s in states:
        q_values = []
        for a in actions:
            q = sum(
                p * (reward(s, a, sp) + gamma * v[sp])
                for sp, p in transition(s, a)
            )
            q_values.append(q)
        new_v[s] = max(q_values)
    return new_v
```

전이확률을 모르는 실제 환경에서는 Monte Carlo나 TD 학습처럼 샘플 기반 방법을 사용한다.

```python
def greedy_policy_from_value(states, actions, transition, reward, v, gamma):
    policy = {}
    for s in states:
        policy[s] = max(
            actions,
            key=lambda a: sum(
                p * (reward(s, a, sp) + gamma * v[sp])
                for sp, p in transition(s, a)
            ),
        )
    return policy
```

DP에서는 환경 모델을 통해 모든 가능한 다음 상태를 합산한다는 점이 샘플 기반 RL과 다르다.

## 복잡도 (Complexity)

상태 수 $|S|$, 행동 수 $|A|$일 때 한 번의 full Bellman backup은 전이 구조에 따라 대략 $O(|S|^2|A|)$까지 든다. 상태 공간이 크면 tabular DP는 불가능해지고 근사 방법이 필요하다.

## 응용 (Applications)

- 작은 MDP의 최적 정책 계산
- 강화학습 알고리즘의 이론적 기준점
- planning과 model-based RL
- value function과 Bellman backup 이해

## 흔한 오해 (Common Misunderstandings)

- DP는 환경 모델을 알고 있어야 한다.
- Value iteration의 중간 정책이 항상 좋은 것은 아니다. 수렴 후 정책을 추출한다.
- Discount factor가 1에 가까울수록 먼 미래를 보지만 수렴은 느려질 수 있다.
- 큰 연속 상태 공간에서는 그대로 적용하기 어렵다.

## TMI

- Bellman operator는 적절한 조건에서 contraction이라 반복 적용하면 고정점으로 수렴한다.
- Policy iteration은 반복 수가 적을 수 있지만 각 정책 평가가 비쌀 수 있다.
- Generalized policy iteration은 평가와 개선이 상호작용한다는 많은 RL 알고리즘의 공통 틀이다.

## 연습 / 확인 문제 (Exercises)

- policy evaluation과 value iteration의 업데이트 차이를 쓰라.
- Bellman optimality equation에서 max가 들어가는 이유를 설명하라.
- 전이확률을 모르는 환경에서 DP를 그대로 쓸 수 없는 이유를 말하라.

## 이어서 읽기 (Reading Path)

- 이전: [정책과 최적 정책](Policy.md)
- 다음: [몬테카를로 방법](Monte-Carlo.md)

## 참조 (References)

- [MDP.md](MDP.md)
- [Value-Functions.md](Value-Functions.md)
- [Policy.md](Policy.md)
- [Reference/Books.md](../../Reference/Books.md)
