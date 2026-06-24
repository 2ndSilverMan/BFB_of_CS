# 강화학습 (Reinforcement Learning)

> 환경과의 상호작용을 통해 보상을 최대화하는 에이전트를 학습시키는 방법.

**선수지식**: [AI/Machine-Learning/](../Machine-Learning/), [Math/Probability-Statistics/](../../Math/Probability-Statistics/), [Math/Optimization/](../../Math/Optimization/)

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

### 기초

| 주제 | 파일 | Status |
|---|---|---|
| MDP (마르코프 결정 과정) | [MDP.md](MDP.md) | Draft |
| 가치 함수와 벨만 방정식 | [Value-Functions.md](Value-Functions.md) | Draft |
| 정책 (Policy)과 최적 정책 | [Policy.md](Policy.md) | Draft |

### 모델 기반 방법

| 주제 | 파일 | Status |
|---|---|---|
| 동적 프로그래밍 (가치 반복, 정책 반복) | [Dynamic-Programming.md](Dynamic-Programming.md) | Draft |

### 모델 프리 방법

| 주제 | 파일 | Status |
|---|---|---|
| 몬테카를로 방법 | [Monte-Carlo.md](Monte-Carlo.md) | Draft |
| 시간 차분 학습 (TD, SARSA, Q-Learning) | [TD-Learning.md](TD-Learning.md) | Draft |
| 함수 근사 (Linear, Neural) | [Function-Approximation.md](Function-Approximation.md) | Draft |

### 딥 강화학습

| 주제 | 파일 | Status |
|---|---|---|
| DQN (Deep Q-Network) | [DQN.md](DQN.md) | Draft |
| Policy Gradient (REINFORCE) | [Policy-Gradient.md](Policy-Gradient.md) | Draft |
| Actor-Critic (A2C, A3C) | [Actor-Critic.md](Actor-Critic.md) | Draft |
| PPO (Proximal Policy Optimization) | [PPO.md](PPO.md) | Draft |
| SAC (Soft Actor-Critic) | [SAC.md](SAC.md) | Draft |

### 심화

| 주제 | 파일 | Status |
|---|---|---|
| 모델 기반 딥 RL (Dreamer, MuZero) | [Model-Based-DRL.md](Model-Based-DRL.md) | Draft |
| 다중 에이전트 RL | [Multi-Agent-RL.md](Multi-Agent-RL.md) | Draft |
| 계층적 RL | [Hierarchical-RL.md](Hierarchical-RL.md) | Draft |
| 오프라인 RL | [Offline-RL.md](Offline-RL.md) | Draft |

---

## 학습 순서

```text
MDP → Value-Functions → Policy
      ↓
Dynamic-Programming → Monte-Carlo → TD-Learning
      ↓
Function-Approximation → DQN
      ↓
Policy-Gradient → Actor-Critic → PPO / SAC
      ↓
Model-Based-DRL / Multi-Agent-RL / Hierarchical-RL / Offline-RL
```

---

## 연관 섹션

- [AI/Machine-Learning/](../Machine-Learning/) — 선수지식
- [AI/Deep-Learning/](../Deep-Learning/) — 딥 RL의 신경망 기반
- [AI/LLMs/](../LLMs/) — RLHF에서 RL 활용
