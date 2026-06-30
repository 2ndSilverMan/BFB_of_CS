# 정책 경사 (Policy Gradient: REINFORCE)

- Level: Advanced
- Prerequisites: [AI/Reinforcement-Learning/Policy.md](Policy.md), [Math/Optimization/SGD.md](../../Math/Optimization/SGD.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

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

### Log-derivative trick

Policy gradient는 trajectory 확률을 직접 미분하기 어렵기 때문에 다음 항등식을 사용한다.

$$
\nabla_\theta p_\theta(x)=p_\theta(x)\nabla_\theta\log p_\theta(x)
$$

이를 score function estimator라고도 한다. 핵심 장점은 환경 전이확률을 몰라도 정책 로그확률의 경사만으로 policy parameter를 업데이트할 수 있다는 점이다.

### Baseline이 편향을 만들지 않는 이유

상태에만 의존하는 baseline $b(s)$는 행동 선택과 독립이므로 다음 기댓값이 0이 된다.

$$
E_{a\sim\pi}[\nabla_\theta \log \pi_\theta(a\mid s)b(s)]=0
$$

따라서 baseline은 기대 경사를 바꾸지 않고 분산만 줄인다. 좋은 baseline은 return의 공통 부분을 제거해 "이 행동이 평균보다 얼마나 좋았는가"에 집중하게 한다.

### Advantage와 credit assignment

Return $G_t$는 episode 전체의 결과를 한 행동에 나눠 주는 거친 신호다. Advantage $A(s,a)=Q(s,a)-V(s)$는 같은 상태에서 평균 행동보다 해당 행동이 얼마나 나은지 본다. 이 차이가 policy update의 credit assignment를 더 날카롭게 만든다.

실전에서는 Monte Carlo advantage, TD error, GAE처럼 여러 추정량이 쓰이며, 모두 bias-variance tradeoff가 다르다.

### On-policy 제약

기본 policy gradient는 현재 정책에서 나온 샘플의 로그확률을 사용한다. 정책이 업데이트되면 이전 trajectory는 더 이상 같은 분포에서 온 데이터가 아니다. Importance sampling으로 보정할 수 있지만 분산이 커져, PPO처럼 정책 변화 폭을 제한하는 방법이 등장했다.

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

```python
def normalize_advantages(advantages):
    mean_value = sum(advantages) / len(advantages)
    variance = sum((a - mean_value) ** 2 for a in advantages) / len(advantages)
    scale = variance ** 0.5 + 1e-8
    return [(a - mean_value) / scale for a in advantages]
```

Advantage normalization은 구현 세부사항처럼 보이지만 policy gradient 안정성에 큰 영향을 준다.

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
