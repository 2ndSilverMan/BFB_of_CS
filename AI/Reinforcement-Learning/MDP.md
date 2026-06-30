# 마르코프 결정 과정 (Markov Decision Process)

- Level: Intermediate
- Prerequisites: [Math/Probability-Statistics/Expectation.md](../../Math/Probability-Statistics/Expectation.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

MDP는 상태, 행동, 전이확률, 보상, 할인율로 순차적 의사결정을 모델링한다. 에이전트는 상태에서 행동을 선택하고 환경의 다음 상태·보상을 관측하며 누적 보상을 최대화한다.

## 직관 (Intuition)

미로의 현재 위치가 상태, 이동이 행동, 벽과 미끄러짐이 전이, 목표 도착이 보상이다. 지금의 보상뿐 아니라 행동이 만든 미래 상태의 가치까지 고려한다.

## 이론 (Theory)

MDP는 $(\mathcal S,\mathcal A,P,R,\gamma)$로 쓴다. Markov property는 미래가 과거 전체가 아니라 현재 상태·행동에 조건부로 의존한다는 뜻이다.

$$P(S_{t+1}\mid S_t,A_t,S_{t-1},\dots)=P(S_{t+1}\mid S_t,A_t)$$

return은 $G_t=\sum_{k=0}^{\infty}\gamma^kR_{t+k+1}$이며 $\gamma<1$은 먼 미래를 할인하고 무한합을 안정화한다.

### 상태 충분성과 Markov property

MDP의 핵심은 "상태가 미래 예측에 충분한 정보인가"다. 관측값이 같아도 숨은 변수 때문에 미래가 달라지면 Markov state가 아니다. 예를 들어 카드 게임에서 현재 손패만 보고 덱에 남은 카드를 모르면, 같은 손패라도 과거에 어떤 카드가 나왔는지에 따라 미래 확률이 달라진다.

상태 설계가 부족하면 알고리즘이 아무리 좋아도 잘못된 문제를 풀게 된다. 이 경우에는 history를 상태에 포함하거나, belief state를 쓰거나, POMDP로 모델링한다.

### Episodic과 continuing task

Episodic task는 게임 한 판처럼 terminal state가 있다. Continuing task는 서버 운영, 추천, 재고 관리처럼 명확한 끝이 없을 수 있다. Episodic task에서는 terminal 이후 가치를 0으로 두고, continuing task에서는 할인율이나 average reward formulation으로 장기 보상을 정의한다.

Discount factor $\gamma$는 단순한 수치 안정화 장치가 아니라 문제 정의의 일부다. $\gamma$가 작으면 가까운 보상을 중시하고, $\gamma$가 1에 가까우면 장기 결과가 정책 선택에 크게 반영된다.

### Reward 설계와 specification

Reward는 학습 알고리즘이 보는 목표다. 실제 목표가 안전, 비용, 품질, 사용자 만족처럼 여러 요소를 포함한다면 reward에 무엇을 넣고 무엇을 constraint로 분리할지 결정해야 한다. 잘못된 reward는 최적 정책을 잘못된 행동으로 몰 수 있다.

안전한 문제 정의에서는 reward, constraint, terminal condition, action limit, observation delay를 따로 문서화한다.

## 구현 (Implementation)

```python
def discounted_return(rewards, gamma):
    total = 0.0
    for reward in reversed(rewards):
        total = reward + gamma * total
    return total


print(discounted_return([0, 0, 1], 0.9))
```

```python
mdp_spec = {
    "states": "S",
    "actions": "A",
    "transition": "P(s_next | s, a)",
    "reward": "R(s, a, s_next)",
    "discount": 0.99,
    "terminal_states": {"goal", "failure"},
}
```

명시적 MDP 명세는 알고리즘 구현보다 먼저 문제의 경계를 고정하는 역할을 한다.

## 복잡도 (Complexity)

명시적 tabular MDP는 전이 저장에 최대 `O(|S|^2|A|)` 공간이 필요하다. 실제 큰 문제는 sample interaction과 function approximation을 사용한다.

## 응용 (Applications)

- control·robotics·game
- recommendation과 resource allocation
- operations research
- RL 알고리즘의 공통 수학 모델

## 흔한 오해 (Common Misunderstandings)

- Markov property는 상태 설계에 대한 가정이지 관측이 자동으로 충분하다는 뜻이 아니다.
- reward와 실제 목표가 어긋나면 reward hacking이 생긴다.
- discount는 단순히 성급함만 표현하지 않는다.
- environment model을 모른다고 MDP가 아닌 것은 아니다.

## TMI

- 부분관측 문제는 POMDP로 확장한다.
- terminal state는 이후 보상이 없는 absorbing state로 모델링할 수 있다.
- state representation이 충분하지 않으면 같은 관측에서 다른 미래가 나타난다.

## 연습 / 확인 문제 (Exercises)

- 작은 gridworld의 S,A,P,R을 정의하라.
- gamma를 바꾸며 return을 비교하라.
- Markov state가 아닌 관측 예를 들어라.

## 이어서 읽기 (Reading Path)

- 이전: [기댓값](../../Math/Probability-Statistics/Expectation.md)
- 다음: [가치 함수](Value-Functions.md), [TD 학습](TD-Learning.md)

## 참조 (References)

- [Math/Probability-Statistics/Expectation.md](../../Math/Probability-Statistics/Expectation.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
