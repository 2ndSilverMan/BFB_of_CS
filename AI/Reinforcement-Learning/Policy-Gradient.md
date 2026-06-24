# 정책 경사 (Policy Gradient: REINFORCE)

- Level: Advanced
- Prerequisites: [AI/Reinforcement-Learning/Policy.md](Policy.md), [Math/Optimization/SGD.md](../../Math/Optimization/SGD.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

policy gradient는 정책을 파라미터 $\theta$로 직접 표현하고($\pi_\theta(a\mid s)$), 기대 누적 보상을 경사상승으로 최적화하는 방법이다. REINFORCE는 그 기본형으로, 가치 함수 없이 표본 return으로 경사를 추정한다.

## 직관 (Intuition)

가치 기반 방법은 $Q$를 배운 뒤 거기서 행동을 고르지만, 연속 행동이나 확률적 정책이 필요한 문제에서는 다루기 어렵다. policy gradient는 "좋은 결과를 낸 행동의 확률은 올리고, 나쁜 결과를 낸 행동의 확률은 내린다"는 단순한 원리를 경사로 구현한다. 정책을 직접 만지므로 연속 행동·확률적 정책을 자연스럽게 다룬다.

## 이론 (Theory)

목표 $J(\theta)=\mathbb{E}_{\tau\sim\pi_\theta}[R(\tau)]$의 경사는 **정책 경사 정리**로 주어진다.

$$\nabla_\theta J(\theta)=\mathbb{E}_{\pi_\theta}\!\left[\sum_t \nabla_\theta \log \pi_\theta(a_t\mid s_t)\,G_t\right]$$

직관적으로 $\log\pi$의 경사에 return을 가중한 것이다. 분산을 줄이려 baseline $b(s)$를 빼도 기댓값은 그대로다.

$$\nabla_\theta J=\mathbb{E}\!\left[\sum_t \nabla_\theta\log\pi_\theta(a_t\mid s_t)\,(G_t-b(s_t))\right]$$

baseline으로 $V(s)$를 쓰면 $G_t-V(s_t)$는 advantage 추정이 되고, 이를 학습된 가치와 결합한 것이 actor-critic이다. REINFORCE는 episode가 끝난 뒤 실제 return으로 갱신하는 Monte Carlo 방식이라 불편향이지만 분산이 크다.

## 구현 (Implementation)

```python
def reinforce_update(trajectory, policy, optim, gamma):
    returns, G = [], 0
    for (_, _, r) in reversed(trajectory):
        G = r + gamma * G                     # 뒤에서부터 return 누적
        returns.insert(0, G)
    baseline = mean(returns)                  # 간단한 baseline
    loss = 0
    for (s, a, _), G in zip(trajectory, returns):
        loss = loss - log(policy(a, s)) * (G - baseline)  # 경사상승 → 손실 부호 반전
    optim.minimize(loss)
```

## 복잡도 (Complexity)

업데이트 비용은 trajectory 길이와 정책망 크기에 비례한다. 핵심 비용은 계산량보다 **표본 효율과 분산**이다. Monte Carlo return은 분산이 커 수렴이 느리고 불안정하며, baseline·advantage·여러 trajectory 평균으로 분산을 줄인다. on-policy라 갱신 후 과거 데이터를 재사용하기 어렵다.

## 응용 (Applications)

- 연속 제어(로봇 팔, 보행) 등 연속 행동 문제
- actor-critic, A2C/A3C, PPO 등 현대 알고리즘의 토대
- LLM의 RLHF에서 정책 최적화(보통 PPO)
- 게임·추천의 확률적 정책 학습

## 흔한 오해 (Common Misunderstandings)

- baseline을 빼면 편향이 생길 것 같지만, 상태에만 의존하면 기댓값은 변하지 않고 분산만 준다.
- policy gradient는 높은 분산 때문에 그대로 쓰면 불안정하다. 실전에서는 advantage·clipping이 거의 필수다.
- on-policy 특성상 표본 효율이 낮아, off-policy 가치 기반보다 데이터를 많이 쓴다.
- REINFORCE가 곧 actor-critic은 아니다. critic(학습된 가치)을 더한 것이 actor-critic이다.

## TMI

- REINFORCE라는 이름은 1992년 Williams의 알고리즘에서 왔다.
- log-derivative trick($\nabla_\theta p = p\,\nabla_\theta \log p$)은 정책 경사 유도의 핵심 수학 도구이며, score function estimator라고도 불린다.
- PPO는 정책이 한 번에 너무 크게 변하지 않도록 비율을 clip해, RLHF 등에서 사실상 표준이 됐다.

## 연습 / 확인 문제 (Exercises)

- log-derivative trick으로 정책 경사 정리를 직접 유도하라.
- 상태 의존 baseline이 경사 추정의 기댓값을 바꾸지 않음을 보여라.
- REINFORCE의 분산이 큰 이유와 actor-critic이 이를 줄이는 방식을 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [정책 (Policy)](Policy.md), [시간 차분 학습](TD-Learning.md)
- 다음: [Actor-Critic](Actor-Critic.md), [PPO](PPO.md)

## 참조 (References)

- [AI/Reinforcement-Learning/Policy.md](Policy.md)
- [AI/Reinforcement-Learning/Value-Functions.md](Value-Functions.md)
- [Reference/Books.md](../../Reference/Books.md)
