# 모델 기반 딥 RL (Model-Based Deep RL)

- Level: Advanced
- Prerequisites: [Dynamic-Programming.md](Dynamic-Programming.md), [Function-Approximation.md](Function-Approximation.md), [AI/Deep-Learning/Transformer.md](../Deep-Learning/Transformer.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

모델 기반 딥 RL은 환경의 동역학이나 보상 모델을 신경망으로 학습하고, 그 모델을 이용해 planning이나 policy learning을 수행하는 방법이다. Dreamer, MuZero 같은 계열이 대표적이다.

## 직관 (Intuition)

현실에서 직접 시도하는 것은 비싸거나 위험할 수 있다. 대신 머릿속 시뮬레이터를 만들고 “이 행동을 하면 다음에 어떻게 될까?”를 상상해 계획한다. 모델 기반 RL은 이 시뮬레이터를 데이터에서 학습한다.

## 이론 (Theory)

모델 기반 RL은 보통 다음 구성요소를 갖는다.

- Dynamics model: $p_\theta(s_{t+1}\mid s_t,a_t)$ 또는 latent transition
- Reward model: $r_\theta(s_t,a_t)$
- Planner or policy optimizer: 모델 안에서 rollout을 수행해 행동을 개선

MuZero는 명시적 관측 공간 dynamics 대신 latent state, reward, value, policy를 학습하고 tree search와 결합한다. Dreamer는 latent world model 안에서 imagined rollout을 통해 actor-critic을 학습한다.

모델 오류가 rollout에서 누적되는 compounding error가 핵심 위험이다.

### 모델의 종류

모델 기반 RL에서 "모델"은 여러 형태를 가질 수 있다.

- Forward dynamics: 현재 상태와 행동에서 다음 상태를 예측한다.
- Reward model: 상태-행동의 보상을 예측한다.
- Termination model: episode 종료 여부를 예측한다.
- Latent world model: 관측 대신 latent state에서 transition을 예측한다.
- Value-equivalent model: 관측 예측보다 planning에 필요한 value/policy 정보를 잘 맞춘다.

제어에 좋은 모델은 픽셀 단위 예측이 가장 좋은 모델과 다를 수 있다. 중요한 것은 policy improvement에 필요한 정보가 정확한가다.

### Compounding model error

한 step 예측 오류가 작아도 rollout을 길게 하면 오류가 누적된다. 정책은 모델이 잘못 예측하는 영역을 찾아 이용할 수 있고, 이를 model exploitation이라고 부른다. 모델 안에서는 좋아 보이는 정책이 실제 환경에서는 실패할 수 있다.

완화 방법은 짧은 horizon planning, uncertainty penalty, ensemble dynamics, real data와 imagined data 혼합, model predictive control처럼 자주 재계획하는 방식이다.

### Planning과 learning의 결합

모델을 배운 뒤 사용할 수 있는 방식은 다양하다. Dyna는 모델이 만든 imagined transition으로 value function을 추가 학습한다. MPC는 매 step 짧은 horizon 계획을 세우고 첫 행동만 실행한다. MuZero류는 learned model과 tree search를 결합한다. Dreamer류는 latent imagination 안에서 actor-critic을 학습한다.

이 선택은 환경 샘플 비용, 계산 비용, 모델 정확도, action space에 따라 달라진다.

### 불확실성

모델이 모르는 영역에서는 보수적으로 행동해야 한다. Ensemble disagreement, probabilistic dynamics, epistemic uncertainty는 모델이 데이터 밖으로 나가는지 감지하는 데 도움을 준다. 안전한 모델 기반 RL에서는 높은 uncertainty rollout에 penalty를 주거나 실제 데이터 수집을 우선한다.

## 구현 (Implementation)

모델 기반 업데이트의 개념 흐름은 다음과 같다.

```python
def imagined_rollout(model, policy, latent, horizon):
    trajectory = []
    for _ in range(horizon):
        action = policy(latent)
        latent, reward = model.step(latent, action)
        trajectory.append((latent, action, reward))
    return trajectory
```

실제 구현에서는 불확실성 추정, 짧은 rollout, real data와 imagined data의 혼합이 중요하다.

```python
def uncertainty_penalized_reward(predicted_reward, model_disagreement, penalty):
    return predicted_reward - penalty * model_disagreement
```

모델 기반 planning은 높은 보상을 찾는 동시에 모델이 확신하지 못하는 영역을 조심해야 한다.

## 복잡도 (Complexity)

환경 샘플은 절약할 수 있지만 모델 학습과 planning 비용이 추가된다. Tree search나 imagined rollout horizon이 길면 계산량이 커지고, 모델 오류 누적도 커진다.

## 응용 (Applications)

- 샘플 비용이 큰 로봇 제어
- 게임 planning
- latent world model 학습
- 안전한 시뮬레이션 기반 정책 개선

## 흔한 오해 (Common Misunderstandings)

- 모델 기반 RL은 항상 모델 프리보다 낫지 않다. 모델 오류가 정책을 망칠 수 있다.
- 예측 정확도가 높은 모델이 제어에 항상 좋은 모델은 아니다.
- 긴 rollout이 항상 더 좋은 계획을 주는 것은 아니다.
- 실제 환경 분포 밖에서 모델을 굴리면 hallucinated dynamics가 생길 수 있다.

## TMI

- Dyna는 실제 경험과 모델 생성 경험을 함께 쓰는 고전적 틀이다.
- Model predictive control은 매 시점 짧은 horizon 계획을 다시 세우는 방식이다.
- World model은 representation learning과 planning을 연결하는 매력적인 연구 축이다.

## 연습 / 확인 문제 (Exercises)

- 모델 기반 RL에서 dynamics model과 policy의 역할을 구분하라.
- Compounding model error가 생기는 이유를 설명하라.
- Dreamer류 latent rollout이 관측 공간 rollout보다 유리할 수 있는 이유를 말하라.

## 이어서 읽기 (Reading Path)

- 이전: [SAC](SAC.md)
- 다음: [다중 에이전트 RL](Multi-Agent-RL.md)

## 참조 (References)

- [Dynamic-Programming.md](Dynamic-Programming.md)
- [Function-Approximation.md](Function-Approximation.md)
- [AI/Deep-Learning/Transformer.md](../Deep-Learning/Transformer.md)
- [Reference/Books.md](../../Reference/Books.md)
