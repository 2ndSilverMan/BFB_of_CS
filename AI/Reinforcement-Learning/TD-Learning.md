# 시간 차분 학습 (Temporal-Difference Learning)

- Level: Intermediate
- Prerequisites: [AI/Reinforcement-Learning/MDP.md](MDP.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

TD 학습은 episode가 끝나기 전에 현재 추정치와 다음 상태 추정치를 이용해 가치함수를 갱신한다. Monte Carlo의 sampling과 dynamic programming의 bootstrapping을 결합한다.

## 직관 (Intuition)

최종 결과를 기다리지 않고 "현재 보상 + 다음 상태 예상 가치"를 임시 정답으로 삼아 한 걸음마다 예측을 수정한다.

## 이론 (Theory)

TD(0)의 update는

$$\delta_t=R_{t+1}+\gamma V(S_{t+1})-V(S_t),\qquad
V(S_t)\leftarrow V(S_t)+\alpha\delta_t$$

다. SARSA는 실제 다음 행동의 $Q(S',A')$를 쓰는 on-policy, Q-learning은 $\max_{a'}Q(S',a')$를 쓰는 off-policy control이다. exploration과 function approximation에서는 수렴 조건이 더 복잡하다.

### TD target과 TD error

TD target은 $R_{t+1}+\gamma V(S_{t+1})$다. TD error $\delta_t$는 현재 예측이 이 target과 얼마나 다른지 나타낸다. 이 error는 value update뿐 아니라 actor-critic에서 policy update의 advantage 신호로도 쓰인다.

TD target은 실제 return이 아니라 추정치를 포함한다. 그래서 학습이 빠르지만, 잘못된 추정이 다른 상태로 전파될 수 있다.

### SARSA와 Q-learning

SARSA target은 실제로 선택한 다음 행동을 쓴다.

$$
R_{t+1}+\gamma Q(S_{t+1},A_{t+1})
$$

Q-learning target은 다음 상태에서 가장 큰 Q값을 쓴다.

$$
R_{t+1}+\gamma \max_a Q(S_{t+1},a)
$$

따라서 SARSA는 on-policy로 탐험 행동의 위험까지 반영하고, Q-learning은 behavior policy와 별개로 greedy target을 학습한다. 위험한 cliff-walking 예제에서는 이 차이가 정책 성향을 크게 바꾼다.

### n-step TD와 eligibility trace

TD(0)는 한 step 뒤를 보고, MC는 episode 끝까지 본다. n-step TD는 그 중간이다.

$$
G_t^{(n)}=R_{t+1}+\gamma R_{t+2}+\cdots+\gamma^{n-1}R_{t+n}+\gamma^n V(S_{t+n})
$$

TD($\lambda$)는 여러 n-step return을 가중 평균해 short-term bootstrapping과 long-term return을 섞는다.

### Deadly triad

Function approximation, bootstrapping, off-policy learning이 함께 있으면 학습이 발산할 수 있다. 이를 deadly triad라고 한다. DQN이 target network와 replay buffer를 쓰는 이유도 이런 불안정성을 줄이기 위해서다.

## 구현 (Implementation)

```python
def td_update(values, state, reward, next_state, alpha=0.1, gamma=0.99):
    target = reward + gamma * values.get(next_state, 0.0)
    error = target - values.get(state, 0.0)
    values[state] = values.get(state, 0.0) + alpha * error
    return error
```

terminal transition에서는 다음 상태 가치를 0으로 둔다.

```python
def q_learning_update(q, s, a, r, sp, actions, alpha=0.1, gamma=0.99):
    best_next = max(q.get((sp, ap), 0.0) for ap in actions)
    target = r + gamma * best_next
    old = q.get((s, a), 0.0)
    q[(s, a)] = old + alpha * (target - old)
```

행동을 어떻게 선택했는지와 target을 어떻게 계산했는지를 분리해 이해해야 한다.

## 복잡도 (Complexity)

tabular TD 한 transition update는 `O(1)`, 가치표는 `O(|S|)`다. Q-learning 표는 `O(|S||A|)`이며 neural approximation은 model forward/backward 비용을 따른다.

## 응용 (Applications)

- online value prediction
- SARSA·Q-learning
- actor-critic의 critic update
- continuing task와 긴 episode

## 흔한 오해 (Common Misunderstandings)

- bootstrapping target은 실제 정답이 아니라 현재 추정에 의존한다.
- off-policy가 exploration 없이도 된다는 뜻은 아니다.
- Q-learning update와 행동 선택 정책을 구분해야 한다.
- function approximation·off-policy·bootstrapping 조합은 불안정할 수 있다.

## TMI

- eligibility trace의 TD($\lambda$)는 여러 시간 규모의 credit assignment를 섞는다.
- deadly triad는 function approximation, bootstrapping, off-policy의 불안정 조합을 가리킨다.
- TD error는 actor-critic에서 advantage 신호로도 쓰인다.

## 연습 / 확인 문제 (Exercises)

- 한 transition의 TD error와 update를 손으로 계산하라.
- SARSA와 Q-learning target을 비교하라.
- terminal state 처리를 빠뜨리면 생길 오류를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [MDP](MDP.md)
- 다음: [함수 근사](Function-Approximation.md)

## 참조 (References)

- [AI/Reinforcement-Learning/MDP.md](MDP.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
