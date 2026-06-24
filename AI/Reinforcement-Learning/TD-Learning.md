# 시간 차분 학습 (Temporal-Difference Learning)

- Level: Intermediate
- Prerequisites: [AI/Reinforcement-Learning/MDP.md](MDP.md)
- Status: Draft
- Reviewed-by: -

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

## 구현 (Implementation)

```python
def td_update(values, state, reward, next_state, alpha=0.1, gamma=0.99):
    target = reward + gamma * values.get(next_state, 0.0)
    error = target - values.get(state, 0.0)
    values[state] = values.get(state, 0.0) + alpha * error
    return error
```

terminal transition에서는 다음 상태 가치를 0으로 둔다.

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
