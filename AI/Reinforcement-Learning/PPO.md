# PPO (Proximal Policy Optimization)

- Level: Advanced
- Prerequisites: [Actor-Critic.md](Actor-Critic.md), [Policy-Gradient.md](Policy-Gradient.md), [Math/Optimization/SGD.md](../../Math/Optimization/SGD.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

PPO는 정책을 너무 급격히 바꾸지 않도록 제한하면서 policy gradient를 최적화하는 actor-critic 계열 알고리즘이다. 구현이 비교적 단순하고 안정적이라 딥 강화학습의 기본 baseline으로 널리 쓰인다.

## 직관 (Intuition)

좋은 행동을 더 자주 하도록 정책을 바꾸고 싶지만, 한 번에 너무 크게 바꾸면 지금까지 모은 데이터와 정책이 달라져 학습이 망가질 수 있다. PPO는 “조금씩 가까운 범위에서” 정책을 개선하게 만든다.

## 이론 (Theory)

PPO의 clipped objective는 정책 확률비

$$
r_t(\theta)=\frac{\pi_\theta(a_t\mid s_t)}{\pi_{\theta_{old}}(a_t\mid s_t)}
$$

를 사용한다.

$$
L^{CLIP}(\theta)=E[\min(r_t(\theta)A_t,\operatorname{clip}(r_t(\theta),1-\epsilon,1+\epsilon)A_t)]
$$

확률비가 너무 커지거나 작아지는 업데이트를 잘라 정책 변화 폭을 제한한다. 보통 value loss와 entropy bonus를 함께 더해 학습한다.

## 구현 (Implementation)

clipped surrogate의 한 샘플 값은 다음처럼 계산할 수 있다.

```python
def ppo_clip_loss_ratio(ratio, advantage, eps=0.2):
    clipped = min(max(ratio, 1 - eps), 1 + eps)
    return min(ratio * advantage, clipped * advantage)


print(ppo_clip_loss_ratio(1.4, advantage=2.0))
```

실제 구현은 이 값을 maximize하므로 프레임워크 loss에서는 부호를 반대로 둔다.

## 복잡도 (Complexity)

PPO는 수집한 rollout batch에 대해 여러 epoch SGD를 수행한다. 샘플 효율은 off-policy 방법보다 낮을 수 있지만, 안정성과 구현 난도가 좋아 널리 사용된다.

## 응용 (Applications)

- 연속 제어 benchmark
- 로봇 시뮬레이션
- 게임 AI
- RLHF류 policy optimization의 역사적 기반

## 흔한 오해 (Common Misunderstandings)

- PPO가 모든 환경에서 최고 성능을 보장하는 것은 아니다.
- clip만으로 정책 변화가 완전히 통제되는 것은 아니며 KL 모니터링도 중요하다.
- Advantage normalization과 reward scaling 같은 세부 구현이 성능에 큰 영향을 준다.
- On-policy 특성 때문에 데이터 재사용이 제한적이다.

## TMI

- PPO는 TRPO의 trust region 아이디어를 더 단순한 목적 함수로 구현하려는 방향에서 나왔다.
- 구현 차이가 성능 차이를 크게 만들기 때문에 “PPO details matter”라는 말이 자주 나온다.
- Entropy coefficient는 탐험과 수렴 속도의 균형에 영향을 준다.

## 연습 / 확인 문제 (Exercises)

- PPO에서 probability ratio가 의미하는 바를 설명하라.
- Advantage가 양수일 때 ratio가 너무 커지는 것을 clip하는 이유를 말하라.
- PPO가 on-policy 알고리즘이라는 점이 데이터 효율에 미치는 영향을 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [Actor-Critic](Actor-Critic.md)
- 다음: [SAC](SAC.md)

## 참조 (References)

- [Actor-Critic.md](Actor-Critic.md)
- [Policy-Gradient.md](Policy-Gradient.md)
- [Math/Optimization/SGD.md](../../Math/Optimization/SGD.md)
- [Reference/Books.md](../../Reference/Books.md)
