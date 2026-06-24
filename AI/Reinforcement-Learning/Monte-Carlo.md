# 몬테카를로 방법 (Monte Carlo Methods)

- Level: Advanced
- Prerequisites: [MDP.md](MDP.md), [Value-Functions.md](Value-Functions.md), [Math/Probability-Statistics/Expectation.md](../../Math/Probability-Statistics/Expectation.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

강화학습의 몬테카를로 방법은 완전한 에피소드에서 얻은 실제 return 평균으로 가치 함수를 추정하는 샘플 기반 방법이다. 환경 모델을 몰라도 경험한 episode만으로 정책 평가와 제어를 할 수 있다.

## 직관 (Intuition)

어떤 전략이 좋은지 알고 싶다면 게임을 여러 판 끝까지 해보고, 각 상태에서 시작했을 때 실제로 받은 총 보상을 평균내면 된다. 몬테카를로 방법은 이 “끝까지 해보고 평균내기”를 체계화한다.

## 이론 (Theory)

시점 $t$의 return은 보통 다음처럼 정의한다.

$$
G_t=R_{t+1}+\gamma R_{t+2}+\gamma^2R_{t+3}+\cdots
$$

몬테카를로 policy evaluation은 같은 상태 또는 상태-행동 쌍에서 관측된 $G_t$들의 평균으로 $V^\pi(s)$나 $Q^\pi(s,a)$를 추정한다.

First-visit MC는 한 episode에서 상태가 처음 방문된 시점만 사용하고, every-visit MC는 방문될 때마다 샘플을 사용한다. 제어 문제에서는 $\epsilon$-greedy 정책 개선을 함께 사용해 탐험을 유지한다.

## 구현 (Implementation)

Incremental mean으로 return 평균을 갱신할 수 있다.

```python
def update_mean(old_mean, count, new_value):
    count += 1
    old_mean += (new_value - old_mean) / count
    return old_mean, count


value, n = 0.0, 0
for g in [3.0, 5.0, 4.0]:
    value, n = update_mean(value, n, g)

print(value)
```

실제 MC control은 episode 생성, return 역방향 계산, 방문 여부 추적, 정책 개선을 포함한다.

## 복잡도 (Complexity)

한 업데이트는 episode 길이에 선형이다. 에피소드가 끝나야 학습할 수 있으므로 continuing task나 긴 horizon에서는 TD 방법보다 비효율적일 수 있다. 분산은 크지만 bias는 작다.

## 응용 (Applications)

- 에피소드형 게임 정책 평가
- 모델 없는 정책 평가
- MC control과 exploring starts
- TD 학습과 bias-variance 비교의 기준

## 흔한 오해 (Common Misunderstandings)

- 몬테카를로 방법은 환경 모델이 필요 없다.
- 에피소드가 끝나기 전에는 return을 확정할 수 없다.
- 표본 평균은 충분히 많은 episode에서 수렴하지만 분산이 클 수 있다.
- 탐험이 부족하면 좋은 행동을 발견하지 못한다.

## TMI

- Off-policy MC는 importance sampling으로 다른 정책에서 생성한 데이터를 평가할 수 있지만 분산 문제가 크다.
- MC는 bootstrapping을 하지 않는다는 점에서 TD와 구분된다.
- 많은 policy gradient 방법도 episode return 추정이라는 MC 성격을 가진다.

## 연습 / 확인 문제 (Exercises)

- First-visit MC와 every-visit MC의 차이를 설명하라.
- MC와 TD의 업데이트 시점 차이를 말하라.
- 긴 에피소드에서 MC의 분산이 커지는 이유를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [동적 프로그래밍](Dynamic-Programming.md)
- 다음: [TD 학습](TD-Learning.md)

## 참조 (References)

- [MDP.md](MDP.md)
- [Value-Functions.md](Value-Functions.md)
- [Math/Probability-Statistics/Expectation.md](../../Math/Probability-Statistics/Expectation.md)
- [Reference/Books.md](../../Reference/Books.md)
