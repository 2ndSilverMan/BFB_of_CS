# 몬테카를로 방법 (Monte Carlo Methods)

- Level: Advanced
- Prerequisites: [MDP.md](MDP.md), [Value-Functions.md](Value-Functions.md), [Math/Probability-Statistics/Expectation.md](../../Math/Probability-Statistics/Expectation.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

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

### First-visit과 every-visit

First-visit MC는 한 episode에서 상태 $s$가 처음 등장한 시점의 return만 평균에 넣는다. Every-visit MC는 등장할 때마다 return을 모두 넣는다. 충분한 조건에서는 둘 다 같은 기댓값으로 수렴하지만, finite sample에서는 분산과 상관 구조가 다를 수 있다.

상태가 episode 안에서 자주 반복되는 문제라면 every-visit은 더 많은 샘플을 쓰는 것처럼 보이지만, 같은 episode 안 샘플들이 독립은 아니다.

### Exploring starts와 $\epsilon$-soft policy

MC control이 모든 행동의 가치를 학습하려면 충분한 탐험이 필요하다. 고전적 방법인 exploring starts는 모든 상태-행동 쌍에서 시작할 가능성을 가정하지만, 실제 환경에서는 비현실적일 수 있다. 그래서 $\epsilon$-greedy처럼 모든 행동에 작은 확률을 주는 정책을 쓴다.

탐험이 사라지면 현재 좋아 보이는 행동만 평가하고, 아직 시도하지 않은 좋은 행동을 발견하지 못한다.

### Off-policy와 importance sampling

Off-policy MC는 behavior policy $b$가 만든 episode로 target policy $\pi$를 평가한다. 이때 trajectory 확률 비율인 importance sampling weight를 사용한다.

$$
\rho = \prod_t \frac{\pi(A_t\mid S_t)}{b(A_t\mid S_t)}
$$

이 방식은 원리는 깔끔하지만 분산이 매우 커질 수 있다. 특히 긴 horizon에서 작은 확률 비율들이 곱해지면 추정량이 불안정해진다.

### MC와 TD의 bias-variance

MC target은 실제 return이므로 bootstrapping bias가 없다. 대신 episode 전체의 randomness가 들어가 분산이 크다. TD target은 편향이 있을 수 있지만 한 step마다 학습하고 분산이 작다. 이 대비가 TD($\lambda$), advantage estimation, policy gradient variance reduction으로 이어진다.

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

```python
def returns_from_episode(rewards, gamma):
    returns = []
    g = 0.0
    for reward in reversed(rewards):
        g = reward + gamma * g
        returns.append(g)
    return list(reversed(returns))
```

MC 업데이트는 이 return을 상태나 상태-행동 방문 시점에 맞춰 평균내는 방식으로 이뤄진다.

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
