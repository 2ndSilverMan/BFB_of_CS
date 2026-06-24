# 마르코프 결정 과정 (Markov Decision Process)

- Level: Intermediate
- Prerequisites: [Math/Probability-Statistics/Expectation.md](../../Math/Probability-Statistics/Expectation.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

MDP는 상태, 행동, 전이확률, 보상, 할인율로 순차적 의사결정을 모델링한다. 에이전트는 상태에서 행동을 선택하고 환경의 다음 상태·보상을 관측하며 누적 보상을 최대화한다.

## 직관 (Intuition)

미로의 현재 위치가 상태, 이동이 행동, 벽과 미끄러짐이 전이, 목표 도착이 보상이다. 지금의 보상뿐 아니라 행동이 만든 미래 상태의 가치까지 고려한다.

## 이론 (Theory)

MDP는 $(\mathcal S,\mathcal A,P,R,\gamma)$로 쓴다. Markov property는 미래가 과거 전체가 아니라 현재 상태·행동에 조건부로 의존한다는 뜻이다.

$$P(S_{t+1}\mid S_t,A_t,S_{t-1},\dots)=P(S_{t+1}\mid S_t,A_t)$$

return은 $G_t=\sum_{k=0}^{\infty}\gamma^kR_{t+k+1}$이며 $\gamma<1$은 먼 미래를 할인하고 무한합을 안정화한다.

## 구현 (Implementation)

```python
def discounted_return(rewards, gamma):
    total = 0.0
    for reward in reversed(rewards):
        total = reward + gamma * total
    return total


print(discounted_return([0, 0, 1], 0.9))
```

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
