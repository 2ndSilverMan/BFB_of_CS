# 다중 에이전트 강화학습 (Multi-Agent RL)

- Level: Advanced
- Prerequisites: [MDP.md](MDP.md), [Policy.md](Policy.md), [AI/Theoretical-ML/Regret-Minimization.md](../Theoretical-ML/Regret-Minimization.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

다중 에이전트 강화학습은 여러 에이전트가 같은 환경에서 상호작용하며 학습하는 문제다. 에이전트들은 협력, 경쟁, 혼합 관계를 가질 수 있고, 한 에이전트의 행동이 다른 에이전트의 관측과 보상에 영향을 준다.

## 직관 (Intuition)

혼자 게임을 배울 때는 환경이 비교적 고정되어 있다. 여러 플레이어가 동시에 배우면 상대도 계속 변한다. 내가 어제 배운 최적 전략이 오늘은 상대의 새 전략 때문에 더 이상 좋지 않을 수 있다.

## 이론 (Theory)

단일 에이전트 MDP와 달리 multi-agent setting은 다른 에이전트 정책이 환경 동역학의 일부처럼 작동한다. 이 때문에 학습 중 환경이 non-stationary해진다.

대표 문제 유형은 다음과 같다.

- Cooperative: 모든 에이전트가 공동 보상을 최대화한다.
- Competitive: zero-sum game처럼 상대 보상을 낮춘다.
- Mixed: 협력과 경쟁이 섞인다.

중요한 설계 축은 centralized training with decentralized execution(CTDE), communication, credit assignment, equilibrium, opponent modeling이다.

### Non-stationarity

단일 에이전트 RL에서는 환경 전이가 고정되어 있다고 가정한다. MARL에서는 다른 에이전트의 정책이 계속 변하므로, 한 에이전트 입장에서는 환경이 학습 중 바뀐다. Replay buffer에 저장된 과거 transition도 "예전 상대 정책"에서 나온 데이터가 된다.

이를 완화하려면 opponent policy version을 기록하거나, centralized critic으로 joint state/action을 보거나, self-play population을 유지한다.

### CTDE

Centralized training with decentralized execution은 학습 중에는 전체 상태나 다른 에이전트 행동을 critic이 볼 수 있게 하고, 배포 시에는 각 에이전트가 자기 관측만으로 행동하게 하는 방식이다. 협력 과제에서 credit assignment와 안정성을 개선할 수 있다.

하지만 실행 시 사용할 수 없는 정보를 actor가 직접 의존하면 안 된다. Training과 execution 정보 경계를 명확히 해야 한다.

### Credit assignment

공동 보상 환경에서는 어떤 에이전트의 어떤 행동이 성공에 기여했는지 알기 어렵다. Difference reward, counterfactual baseline, value decomposition은 공동 보상을 agent별 학습 신호로 나누려는 접근이다.

Credit assignment가 나쁘면 모든 에이전트가 같은 보상을 받지만 누가 무엇을 고쳐야 하는지 모른다.

### 경쟁과 equilibrium

경쟁 환경에서는 "최적 정책"이 상대 집합에 의존한다. 특정 상대에게 강한 정책이 다른 상대에게 취약할 수 있다. Self-play, population-based training, exploitability evaluation은 이런 문제를 다룬다.

## 구현 (Implementation)

공동 보상 환경에서는 여러 에이전트 행동을 모아 한 step을 진행한다.

```python
def joint_step(env, policies, observations):
    actions = {
        agent_id: policy(observations[agent_id])
        for agent_id, policy in policies.items()
    }
    return env.step(actions)
```

실제 구현은 agent별 replay, shared policy, parameter sharing, centralized critic 여부를 결정해야 한다.

```python
def joint_action_space_size(action_counts):
    total = 1
    for count in action_counts:
        total *= count
    return total
```

에이전트가 늘수록 joint action space가 빠르게 커지므로, factorization과 parameter sharing이 중요해진다.

## 복잡도 (Complexity)

에이전트 수가 늘면 joint action space가 곱으로 커진다. 다른 에이전트의 학습 때문에 데이터 분포가 계속 바뀌어 안정적 학습이 어렵다. 통신과 coordination 비용도 커진다.

## 응용 (Applications)

- 멀티플레이어 게임 AI
- 로봇 군집 제어
- 교통 신호 제어
- 시장·경매·자원 배분 시뮬레이션

## 흔한 오해 (Common Misunderstandings)

- 단일 에이전트 알고리즘을 그대로 여러 개 돌리면 항상 잘 되는 것은 아니다.
- 공동 보상이 있어도 credit assignment는 어렵다.
- 경쟁 환경의 좋은 정책은 상대 집합에 따라 달라질 수 있다.
- 더 많은 통신이 항상 좋은 협력을 만드는 것은 아니다.

## TMI

- Self-play는 경쟁 게임에서 강력한 학습 방식이다.
- Mean-field MARL은 많은 에이전트의 효과를 평균장으로 근사하려는 접근이다.
- Emergent communication은 에이전트들이 학습 중 자체 통신 규약을 만드는 현상을 다룬다.

## 연습 / 확인 문제 (Exercises)

- 다중 에이전트 RL이 non-stationary해지는 이유를 설명하라.
- CTDE의 장점을 예로 설명하라.
- cooperative setting에서 credit assignment가 어려운 이유를 말하라.

## 이어서 읽기 (Reading Path)

- 이전: [모델 기반 딥 RL](Model-Based-DRL.md)
- 다음: [계층적 RL](Hierarchical-RL.md)

## 참조 (References)

- [MDP.md](MDP.md)
- [Policy.md](Policy.md)
- [AI/Theoretical-ML/Regret-Minimization.md](../Theoretical-ML/Regret-Minimization.md)
- [Reference/Books.md](../../Reference/Books.md)
