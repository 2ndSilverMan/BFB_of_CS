# SAC (Soft Actor-Critic)

- Level: Advanced
- Prerequisites: [Actor-Critic.md](Actor-Critic.md), [Math/Probability-Statistics/Distributions.md](../../Math/Probability-Statistics/Distributions.md), [AI/Deep-Learning/MLP.md](../Deep-Learning/MLP.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

SAC는 최대 엔트로피 강화학습 기반의 off-policy actor-critic 알고리즘이다. 보상뿐 아니라 정책 엔트로피도 최대화해 탐험을 장려하고, 연속 제어 문제에서 안정적이고 샘플 효율적인 성능을 보이는 편이다.

## 직관 (Intuition)

단지 높은 보상을 얻는 행동만 고집하면 너무 빨리 한 전략에 갇힐 수 있다. SAC는 좋은 보상을 얻으면서도 정책이 충분히 무작위성을 유지하도록 보너스를 준다. “잘하면서도 너무 성급히 확신하지 않는” 에이전트를 만드는 셈이다.

## 이론 (Theory)

SAC의 목표는 기대 return에 entropy 항을 더한 soft objective다.

$$
E\left[\sum_t r(s_t,a_t)+\alpha H(\pi(\cdot\mid s_t))\right]
$$

$\alpha$는 entropy temperature로, 보상과 탐험 사이 균형을 조절한다. SAC는 보통 stochastic actor, 두 개의 Q critic, target network, replay buffer를 사용한다. Double Q 구조는 Q값 과대평가를 줄이는 데 도움을 준다.

### Soft Bellman backup

SAC는 일반 Q값 대신 entropy가 포함된 soft value를 사용한다. 다음 상태에서 단순히 큰 Q를 고르는 것이 아니라, 정책의 로그확률 항을 빼서 entropy 보너스를 반영한다.

$$
y=r+\gamma\left(\min_i Q_{\phi_i^-}(s',a')-\alpha\log\pi_\theta(a'\mid s')\right)
$$

여기서 $a'$는 현재 actor에서 샘플링하고, 두 critic 중 작은 값을 써 과대평가를 줄인다.

### Reparameterization trick

연속 행동에서 policy gradient를 낮은 분산으로 학습하려면 stochastic action sampling을 미분 가능하게 표현한다. Gaussian policy에서

$$
a = \tanh(\mu_\theta(s)+\sigma_\theta(s)\epsilon),\quad \epsilon\sim\mathcal N(0,I)
$$

처럼 noise를 외부로 분리하면 action에 대한 Q값 경사를 actor parameter로 전달할 수 있다. Tanh squashing을 쓰면 행동 범위를 제한할 수 있지만 log-probability 보정이 필요하다.

### Temperature tuning

$\alpha$가 크면 entropy를 강하게 보상해 더 무작위적인 정책이 된다. 작으면 보상 최적화에 더 집중한다. Automatic entropy tuning은 target entropy와 실제 entropy 차이를 줄이도록 $\alpha$를 학습한다.

Target entropy는 행동 차원과 환경 특성에 따라 정하며, 너무 높은 target은 계속 불필요한 탐험을 유도할 수 있다.

### Off-policy의 장단점

SAC는 replay buffer를 사용해 같은 데이터를 여러 번 학습할 수 있어 sample efficiency가 좋다. 그러나 replay data가 너무 오래되거나 정책 분포와 크게 어긋나면 critic target이 불안정해질 수 있다. Buffer 관리, target network update, reward scale이 중요하다.

## 구현 (Implementation)

soft target에는 entropy 보정 항이 들어간다.

```python
def sac_target(reward, done, next_q, next_log_prob, gamma, alpha):
    if done:
        return reward
    return reward + gamma * (next_q - alpha * next_log_prob)


print(sac_target(1.0, False, next_q=2.0, next_log_prob=-0.7, gamma=0.99, alpha=0.2))
```

실제 구현은 reparameterized Gaussian policy와 squashing 함수, log-probability 보정을 포함한다.

```python
def clipped_double_q(q1, q2):
    return min(q1, q2)
```

두 critic 중 작은 값을 사용하는 것은 positive bias를 줄이는 간단하지만 강력한 안정화 장치다.

## 복잡도 (Complexity)

SAC는 actor와 보통 두 critic을 학습하므로 업데이트 비용이 크다. Off-policy replay를 사용해 샘플 효율은 좋을 수 있지만, 하이퍼파라미터와 reward scale에 민감할 수 있다.

## 응용 (Applications)

- 연속 제어
- 로봇 시뮬레이션
- 샘플 효율이 중요한 환경
- stochastic policy 기반 탐험

## 흔한 오해 (Common Misunderstandings)

- SAC의 entropy는 단순 노이즈가 아니라 목적 함수의 일부다.
- Off-policy라고 해서 오래된 데이터를 무제한 안전하게 써도 되는 것은 아니다.
- 연속 행동에 특히 잘 맞지만 모든 문제에서 PPO보다 낫다는 뜻은 아니다.
- Temperature tuning이 성능과 탐험에 큰 영향을 준다.

## TMI

- Automatic entropy tuning은 target entropy에 맞춰 $\alpha$를 조정한다.
- SAC는 maximum entropy RL의 대표적 실용 알고리즘이다.
- Squashed Gaussian policy는 행동 범위를 제한하면서 미분 가능한 샘플링을 가능하게 한다.

## 연습 / 확인 문제 (Exercises)

- 최대 엔트로피 목적이 탐험을 돕는 이유를 설명하라.
- SAC가 두 개의 Q critic을 쓰는 이유를 말하라.
- PPO와 SAC를 on-policy/off-policy 관점에서 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [PPO](PPO.md)
- 다음: [모델 기반 딥 RL](Model-Based-DRL.md)

## 참조 (References)

- [Actor-Critic.md](Actor-Critic.md)
- [Math/Probability-Statistics/Distributions.md](../../Math/Probability-Statistics/Distributions.md)
- [AI/Deep-Learning/MLP.md](../Deep-Learning/MLP.md)
- [Reference/Books.md](../../Reference/Books.md)
