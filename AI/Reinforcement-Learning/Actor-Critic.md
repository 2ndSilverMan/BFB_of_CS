# Actor-Critic

- Level: Advanced
- Prerequisites: [Policy-Gradient.md](Policy-Gradient.md), [Value-Functions.md](Value-Functions.md), [Function-Approximation.md](Function-Approximation.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

Actor-Critic은 정책을 직접 학습하는 actor와 가치 함수를 추정하는 critic을 함께 사용하는 강화학습 구조다. Actor는 어떤 행동을 할지 결정하고, critic은 그 행동이 기대보다 좋았는지 평가해 actor 업데이트를 돕는다.

## 직관 (Intuition)

배우(actor)는 무대에서 행동하고, 평론가(critic)는 그 행동이 얼마나 좋았는지 피드백한다. 배우 혼자 보상만 보고 배우면 분산이 크고, 평론가의 기준이 있으면 더 안정적인 방향으로 개선할 수 있다.

## 이론 (Theory)

Policy gradient는 다음 형태를 갖는다.

$$
\nabla_\theta J(\theta)=E[\nabla_\theta\log\pi_\theta(a\mid s) A^\pi(s,a)]
$$

Actor-Critic에서 critic은 $V_\phi(s)$ 또는 $Q_\phi(s,a)$를 학습해 advantage $A(s,a)$를 추정한다. 흔한 추정은 TD error를 advantage처럼 쓰는 것이다.

$$
\delta_t=r_t+\gamma V_\phi(s_{t+1})-V_\phi(s_t)
$$

Actor는 $\delta_t\nabla_\theta\log\pi_\theta(a_t\mid s_t)$ 방향으로 업데이트된다.

### Actor와 critic의 결합

Actor는 정책 분포를 바꾸고, critic은 그 정책 아래의 가치를 추정한다. Actor가 바뀌면 critic의 target도 바뀌고, critic이 틀리면 actor가 잘못된 방향으로 업데이트될 수 있다. 이 상호 의존성이 actor-critic 튜닝을 어렵게 만든다.

실무에서는 actor learning rate와 critic learning rate, value loss coefficient, entropy coefficient, rollout length를 함께 조정한다.

### Advantage 추정

TD error는 한 step advantage 추정으로 볼 수 있다. 더 긴 horizon 정보를 섞고 싶으면 n-step return이나 GAE를 사용한다. GAE는 $\lambda$로 bias-variance 균형을 조절한다.

$$
\hat A_t^{GAE}=\sum_{l=0}^{\infty}(\gamma\lambda)^l\delta_{t+l}
$$

$\lambda$가 0에 가까우면 TD(0)에 가깝고, 1에 가까우면 Monte Carlo return에 가까워진다.

### Entropy regularization

Actor가 너무 빨리 결정적 정책으로 수렴하면 탐험이 줄어 local optimum에 갇힐 수 있다. Entropy bonus는 정책 분포가 너무 좁아지는 것을 막는다. 하지만 entropy coefficient가 너무 크면 학습된 좋은 행동도 충분히 exploit하지 못한다.

### Shared encoder의 장단점

Actor와 critic이 같은 feature extractor를 공유하면 계산이 줄고 representation을 함께 배울 수 있다. 반대로 actor와 critic의 목표가 달라 gradient 간섭이 생길 수 있다. 복잡한 환경에서는 shared trunk와 separate head를 쓰되, loss scale을 신중히 맞춘다.

## 구현 (Implementation)

TD error를 advantage로 쓰는 업데이트 신호는 다음처럼 계산된다.

```python
def td_advantage(reward, value, next_value, gamma, done):
    target = reward if done else reward + gamma * next_value
    return target - value


print(td_advantage(1.0, value=0.4, next_value=0.7, gamma=0.99, done=False))
```

실제 알고리즘은 actor loss, critic loss, entropy bonus를 함께 최적화하는 경우가 많다.

```python
def actor_critic_losses(log_prob, advantage, value, target, entropy, entropy_coef=0.01):
    actor_loss = -log_prob * advantage
    critic_loss = (value - target) ** 2
    entropy_bonus = -entropy_coef * entropy
    return actor_loss, critic_loss, entropy_bonus
```

Actor loss는 정책 개선, critic loss는 평가 정확도, entropy 항은 탐험을 각각 담당한다.

## 복잡도 (Complexity)

Actor와 critic 두 모델을 학습하므로 단순 value-based 방법보다 계산과 튜닝이 복잡할 수 있다. 하지만 연속 행동 공간과 stochastic policy에 자연스럽게 적용된다.

## 응용 (Applications)

- 연속 제어
- A2C, A3C, PPO, SAC의 기반 구조
- policy optimization 안정화
- advantage estimation

## 흔한 오해 (Common Misunderstandings)

- Critic이 완벽해야 actor가 학습하는 것은 아니다. 근사 피드백으로도 개선된다.
- Actor-Critic이 항상 DQN보다 안정적인 것은 아니다. 하이퍼파라미터에 민감하다.
- Value estimate bias가 actor 업데이트에 영향을 줄 수 있다.
- Actor와 critic이 같은 feature extractor를 공유할 수도 있고 분리할 수도 있다.

## TMI

- A3C는 여러 actor worker가 비동기적으로 경험을 수집해 학습한다.
- GAE는 advantage 추정의 bias-variance trade-off를 조절하는 기법이다.
- Entropy bonus는 정책이 너무 빨리 결정적으로 되는 것을 막아 탐험을 돕는다.

## 연습 / 확인 문제 (Exercises)

- Actor와 critic의 역할을 구분해 설명하라.
- TD error가 advantage 추정으로 쓰일 수 있는 이유를 말하라.
- Actor-Critic이 연속 행동 공간에 잘 맞는 이유를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [Policy Gradient](Policy-Gradient.md)
- 다음: [PPO](PPO.md), [SAC](SAC.md)

## 참조 (References)

- [Policy-Gradient.md](Policy-Gradient.md)
- [Value-Functions.md](Value-Functions.md)
- [Function-Approximation.md](Function-Approximation.md)
- [Reference/Books.md](../../Reference/Books.md)
