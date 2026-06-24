# DQN (Deep Q-Network)

- Level: Advanced
- Prerequisites: [TD-Learning.md](TD-Learning.md), [Function-Approximation.md](Function-Approximation.md), [AI/Deep-Learning/MLP.md](../Deep-Learning/MLP.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

DQN은 Q-learning에 신경망 함수 근사를 결합한 딥 강화학습 알고리즘이다. 상태를 입력받아 각 행동의 Q값을 출력하고, replay buffer와 target network로 학습을 안정화한다.

## 직관 (Intuition)

테이블에 모든 상태-행동 가치를 저장할 수 없는 게임에서는 화면이나 feature를 보고 “각 행동을 하면 장기적으로 얼마나 좋을지”를 신경망이 예측하게 한다. 단, 같은 네트워크가 계속 움직이는 목표를 쫓으면 불안정하므로 완충 장치가 필요하다.

## 이론 (Theory)

DQN의 목표값은 보통 다음과 같다.

$$
y=r+\gamma\max_{a'}Q_{\theta^-}(s',a')
$$

여기서 $\theta^-$는 target network 파라미터다. 학습 네트워크 $Q_\theta$는

$$
(y-Q_\theta(s,a))^2
$$

를 줄인다. Replay buffer는 연속 샘플의 상관을 줄이고, target network는 bootstrapping target의 급격한 변화를 줄인다.

## 구현 (Implementation)

핵심 TD target 계산은 다음처럼 표현할 수 있다.

```python
def dqn_target(reward, done, next_q_values, gamma):
    if done:
        return reward
    return reward + gamma * max(next_q_values)


print(dqn_target(1.0, False, [0.2, 0.7, 0.4], 0.99))
```

실제 구현에는 replay sampling, epsilon-greedy exploration, target network sync, gradient clipping 등이 포함된다.

## 복잡도 (Complexity)

각 업데이트 비용은 신경망 forward/backward 비용과 batch size에 비례한다. Replay buffer는 많은 transition을 저장하므로 메모리 비용이 크다. Atari 같은 입력에서는 CNN 계산도 중요하다.

## 응용 (Applications)

- 이산 행동 공간 제어
- 게임 플레이
- 시뮬레이터 기반 의사결정
- 딥 RL 안정화 기법 학습

## 흔한 오해 (Common Misunderstandings)

- DQN은 기본적으로 이산 행동 공간에 적합하다.
- Replay buffer가 있으면 모든 off-policy 문제가 해결되는 것은 아니다.
- Target network는 성능 향상 장치라기보다 안정화 장치에 가깝다.
- Q값이 과대평가될 수 있어 Double DQN 같은 개선이 등장했다.

## TMI

- Dueling DQN은 상태 가치와 advantage를 분리해 Q값을 구성한다.
- Prioritized replay는 TD error가 큰 샘플을 더 자주 학습한다.
- Rainbow DQN은 여러 DQN 개선을 결합한 대표 알고리즘이다.

## 연습 / 확인 문제 (Exercises)

- DQN의 target network가 필요한 이유를 설명하라.
- Replay buffer가 샘플 상관을 줄이는 이유를 말하라.
- DQN이 연속 행동 문제에 직접 쓰기 어려운 이유를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [함수 근사](Function-Approximation.md)
- 다음: [Policy Gradient](Policy-Gradient.md), [Actor-Critic](Actor-Critic.md)

## 참조 (References)

- [TD-Learning.md](TD-Learning.md)
- [Function-Approximation.md](Function-Approximation.md)
- [AI/Deep-Learning/MLP.md](../Deep-Learning/MLP.md)
- [Reference/Books.md](../../Reference/Books.md)
