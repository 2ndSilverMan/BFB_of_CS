# 계층적 강화학습 (Hierarchical Reinforcement Learning)

- Level: Advanced
- Prerequisites: [MDP.md](MDP.md), [Policy.md](Policy.md), [Value-Functions.md](Value-Functions.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

계층적 강화학습은 긴 작업을 여러 하위 목표나 option, skill로 나누어 학습하는 방법이다. 상위 정책은 어떤 하위 정책을 실행할지 선택하고, 하위 정책은 일정 기간 구체 행동을 수행한다.

## 직관 (Intuition)

“집에서 회사까지 가라”는 목표를 매 순간 근육 움직임으로 직접 계획하면 어렵다. 대신 “엘리베이터 타기 → 지하철역 가기 → 환승하기 → 사무실 가기” 같은 하위 행동 단위로 나누면 훨씬 다루기 쉽다.

## 이론 (Theory)

Options framework에서 option은 세 요소로 정의된다.

- Initiation set: option을 시작할 수 있는 상태
- Intra-option policy: option 실행 중 따르는 정책
- Termination condition: option이 끝나는 조건

계층 구조는 temporal abstraction을 제공한다. 상위 정책은 primitive action보다 긴 시간 단위로 의사결정할 수 있어 긴 horizon 문제를 줄일 수 있다.

### Temporal abstraction

Option은 여러 primitive action을 묶어 더 긴 시간 단위의 행동처럼 만든다. 상위 정책은 매 step 행동을 고르는 대신 option이 끝날 때 다음 option을 고른다. 이렇게 하면 effective horizon이 줄고, sparse reward 문제에서 탐색이 쉬워질 수 있다.

하지만 option이 너무 길면 환경 변화에 둔감해지고, 너무 짧으면 계층의 장점이 사라진다. 종료 조건은 option의 품질을 좌우한다.

### Option value

Option을 행동처럼 보면 상위 정책은 semi-MDP를 푼다. Option 실행 시간이 variable duration이므로, option 동안 받은 누적 보상과 종료 후 상태 가치를 함께 고려해야 한다.

$$
Q(s,o)=E\left[\sum_{k=0}^{\tau-1}\gamma^kR_{t+k+1}+\gamma^\tau V(S_{t+\tau})\right]
$$

여기서 $\tau$는 option duration이다.

### Option discovery

Option은 사람이 설계할 수도 있고 데이터에서 발견할 수도 있다. 자주 지나는 bottleneck state, 다양성을 만드는 skill, goal-conditioned policy, mutual information objective가 option discovery에 쓰인다.

사람에게 의미 있는 subtask가 에이전트에게 좋은 option일 필요는 없다. 좋은 option은 학습과 planning을 실제로 단순화해야 한다.

### 계층적 credit assignment

실패가 났을 때 상위 정책이 나쁜 option을 골랐는지, 하위 policy가 option을 잘못 실행했는지 구분해야 한다. 계층적 RL에서는 reward를 상위와 하위에 어떻게 배분할지, intrinsic reward가 최종 목표와 어긋나지 않는지 조심해야 한다.

## 구현 (Implementation)

상위 정책이 option을 고르고, option이 종료될 때까지 하위 정책을 실행한다.

```python
def run_option(env, option, state):
    total_reward = 0
    while not option.should_terminate(state):
        action = option.policy(state)
        state, reward, done, _ = env.step(action)
        total_reward += reward
        if done:
            break
    return state, total_reward
```

실제 과제는 좋은 option을 사람이 설계할지, 데이터에서 자동 발견할지다.

```python
def option_return(rewards, gamma, next_value, duration):
    total = 0.0
    for k, reward in enumerate(rewards):
        total += (gamma ** k) * reward
    return total + (gamma ** duration) * next_value
```

Option의 가치는 실행 중 보상과 종료 후 상태 가치를 함께 포함한다.

## 복잡도 (Complexity)

계층 구조는 탐색 공간을 줄일 수 있지만, option 학습과 상위/하위 정책의 동시 최적화가 추가된다. 잘못된 하위 목표는 오히려 학습을 방해할 수 있다.

## 응용 (Applications)

- 긴 horizon 로봇 작업
- 게임의 macro action
- 내비게이션과 subgoal discovery
- skill library 학습

## 흔한 오해 (Common Misunderstandings)

- 계층을 넣으면 자동으로 학습이 쉬워지는 것은 아니다.
- 하위 목표가 최종 보상과 어긋나면 성능이 나빠질 수 있다.
- Option의 종료 조건은 정책만큼 중요하다.
- 사람에게 자연스러운 subtask가 에이전트에게 최적 subtask라는 보장은 없다.

## TMI

- Feudal RL은 manager-worker 구조로 계층을 설명한 초기 방향 중 하나다.
- Skill discovery는 보상 없이도 다양한 행동 option을 찾으려는 연구와 연결된다.
- LLM 기반 에이전트의 고수준 planning도 넓게 보면 계층적 의사결정과 닮았다.

## 연습 / 확인 문제 (Exercises)

- Option의 세 구성요소를 설명하라.
- Temporal abstraction이 긴 horizon 문제에 도움이 되는 이유를 말하라.
- 잘못 설계된 subgoal이 policy learning을 방해하는 예를 들어라.

## 이어서 읽기 (Reading Path)

- 이전: [다중 에이전트 RL](Multi-Agent-RL.md)
- 다음: [오프라인 RL](Offline-RL.md)

## 참조 (References)

- [MDP.md](MDP.md)
- [Policy.md](Policy.md)
- [Value-Functions.md](Value-Functions.md)
- [Reference/Books.md](../../Reference/Books.md)
