# 전문가 알고리즘 (Expert Algorithms)

- Level: Advanced
- Prerequisites: [Regret-Minimization.md](Regret-Minimization.md), [Math/Probability-Statistics/Expectation.md](../../Math/Probability-Statistics/Expectation.md), [Convex-Learning.md](Convex-Learning.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

전문가 알고리즘은 여러 전문가 또는 전략의 예측을 순차적으로 관찰하며, 시간이 지날수록 가장 좋은 전문가와 비슷한 성능을 내도록 가중치를 조정하는 온라인 학습 방법이다. 대표 예는 Weighted Majority와 Hedge다.

## 직관 (Intuition)

처음에는 어떤 전문가가 좋은지 모른다. 매 라운드 예측을 보고 틀린 전문가의 가중치를 줄이고, 잘 맞힌 전문가를 더 믿는다. 중요한 점은 처음부터 최고 전문가를 몰랐더라도 전체 손실이 크게 뒤처지지 않게 만드는 것이다.

## 이론 (Theory)

$K$명의 전문가가 있고, 라운드 $t$에서 전문가 $i$의 손실이 $\ell_{t,i}\in[0,1]$이라고 하자. Hedge는 가중치

$$
w_{t+1,i}=w_{t,i}\exp(-\eta \ell_{t,i})
$$

를 사용하고, 확률 $p_{t,i}=w_{t,i}/\sum_j w_{t,j}$로 전문가를 섞는다. 적절한 $\eta$를 고르면 regret은

$$
O(\sqrt{T\log K})
$$

가 된다. 즉 평균 후회는 0으로 간다.

### Potential function 관점

Hedge 분석은 전체 weight 합을 potential로 놓고, 한편으로는 알고리즘 손실을 상계하고 다른 한편으로는 최고 전문가의 weight를 하계한다. Multiplicative update는 손실이 큰 전문가의 weight를 지수적으로 줄여 potential 성장을 통제한다.

이 분석은 boosting, mirror descent, exponential family 업데이트와 깊게 연결된다.

### 학습률 $\eta$

$\eta$가 크면 최근 손실에 빠르게 반응하지만 noise에 민감해진다. $\eta$가 작으면 안정적이지만 좋은 전문가로 이동하는 속도가 느리다. 고전적 regret bound는 $T$와 $K$를 알고 $\eta\approx\sqrt{\log K/T}$로 잡는 형태가 많다.

실전에서는 doubling trick이나 adaptive learning rate를 사용해 horizon을 미리 몰라도 작동하게 만든다.

### Full-information과 bandit feedback

전문가 문제에서는 모든 전문가의 손실 벡터를 관측한다고 가정한다. Bandit setting에서는 내가 선택한 전문가의 손실만 본다. 이 차이 때문에 bandit 알고리즘은 관측되지 않은 손실을 추정해야 하고 exploration이 필수다.

### 전문가 집합의 품질

Hedge는 최고 전문가와의 상대 성능을 보장한다. 전문가들이 모두 나쁘면 절대 성능도 나쁘다. 따라서 좋은 expert pool 구성, 다양성, 중복 제거, sleeping expert처럼 상황별 사용 가능성을 다루는 확장이 중요하다.

## 구현 (Implementation)

손실 벡터를 모두 관측할 수 있는 full-information 설정의 Hedge는 간단하다.

```python
import math


def hedge_weights(loss_rows, eta):
    k = len(loss_rows[0])
    weights = [1.0] * k
    history = []
    for losses in loss_rows:
        total = sum(weights)
        probs = [w / total for w in weights]
        history.append(probs)
        weights = [w * math.exp(-eta * loss) for w, loss in zip(weights, losses)]
    return history
```

선택한 행동의 손실만 관측하는 bandit 설정에서는 중요도 가중 추정이 필요하다.

```python
def normalize(weights):
    total = sum(weights)
    return [w / total for w in weights]
```

전문가 알고리즘의 핵심 state는 expert별 weight이며, 확률 분포로 정규화해 행동 선택에 사용한다.

## 복잡도 (Complexity)

각 라운드마다 $K$개 전문가의 가중치를 갱신하면 $O(K)$ 시간이 든다. 전체 $T$라운드에서는 $O(TK)$ 시간과 $O(K)$ 메모리를 사용한다.

## 응용 (Applications)

- 온라인 예측과 모델 앙상블
- boosting 알고리즘의 이론적 관점
- adaptive routing과 portfolio selection
- no-regret learning 기반 게임 동역학

## 흔한 오해 (Common Misunderstandings)

- 전문가 알고리즘은 최고 전문가보다 항상 잘한다는 보장이 아니다. 최고 고정 전문가에 크게 뒤처지지 않는다는 보장이다.
- 전문가 손실을 모두 관측할 수 있는 설정과 bandit 설정은 다르다.
- $\eta$가 크면 빠르게 적응하지만 불안정해질 수 있다.
- 전문가 자체가 나쁘면 알고리즘도 좋은 절대 성능을 보장하지 않는다.

## TMI

- Multiplicative weights update는 최적화, 게임 이론, 부스팅, 이론 컴퓨터 과학 전반에 반복해서 등장한다.
- Hedge는 exponential weights family의 대표적인 알고리즘이다.
- 전문가를 “모델”로 보면 온라인 앙상블 학습으로 해석할 수 있다.

## 연습 / 확인 문제 (Exercises)

- Weighted Majority에서 틀린 전문가의 가중치를 절반으로 줄이는 직관을 설명하라.
- $O(\sqrt{T\log K})$ regret이면 평균 regret이 어떻게 되는지 보이라.
- full-information과 bandit feedback의 차이를 예로 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [후회 최소화](Regret-Minimization.md)
- 다음: [멀티암드 밴딧](Multi-Armed-Bandit.md)

## 참조 (References)

- [Regret-Minimization.md](Regret-Minimization.md)
- [Math/Probability-Statistics/Expectation.md](../../Math/Probability-Statistics/Expectation.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
