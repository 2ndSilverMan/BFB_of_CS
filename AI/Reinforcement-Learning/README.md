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
| MDP (마르코프 결정 과정) | MDP.md | Planned |
| 가치 함수와 벨만 방정식 | Value-Functions.md | Planned |
| 정책 (Policy)과 최적 정책 | Policy.md | Planned |

### 모델 기반 방법

| 주제 | 파일 | Status |
|---|---|---|
| 동적 프로그래밍 (가치 반복, 정책 반복) | Dynamic-Programming.md | Planned |

### 모델 프리 방법

| 주제 | 파일 | Status |
|---|---|---|
| 몬테카를로 방법 | Monte-Carlo.md | Planned |
| 시간 차분 학습 (TD, SARSA, Q-Learning) | TD-Learning.md | Planned |
| 함수 근사 (Linear, Neural) | Function-Approximation.md | Planned |

### 딥 강화학습

| 주제 | 파일 | Status |
|---|---|---|
| DQN (Deep Q-Network) | DQN.md | Planned |
| Policy Gradient (REINFORCE) | Policy-Gradient.md | Planned |
| Actor-Critic (A2C, A3C) | Actor-Critic.md | Planned |
| PPO (Proximal Policy Optimization) | PPO.md | Planned |
| SAC (Soft Actor-Critic) | SAC.md | Planned |

### 심화

| 주제 | 파일 | Status |
|---|---|---|
| 모델 기반 딥 RL (Dreamer, MuZero) | Model-Based-DRL.md | Planned |
| 다중 에이전트 RL | Multi-Agent-RL.md | Planned |
| 계층적 RL | Hierarchical-RL.md | Planned |
| 오프라인 RL | Offline-RL.md | Planned |

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
