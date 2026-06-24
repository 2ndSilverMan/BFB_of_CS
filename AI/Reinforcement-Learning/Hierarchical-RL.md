# 계층적 강화학습 (Hierarchical Reinforcement Learning)

- Level: Advanced
- Prerequisites: [MDP.md](MDP.md), [Policy.md](Policy.md), [Value-Functions.md](Value-Functions.md)
- Status: Draft
- Reviewed-by: -

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
