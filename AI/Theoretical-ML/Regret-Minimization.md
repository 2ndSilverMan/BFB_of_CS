# 후회 최소화 (Regret Minimization)

- Level: Advanced
- Prerequisites: [GD-Convergence.md](GD-Convergence.md), [Math/Optimization/Convex-Optimization.md](../../Math/Optimization/Convex-Optimization.md), [AI/Reinforcement-Learning/MDP.md](../Reinforcement-Learning/MDP.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

후회(regret)는 온라인 의사결정에서 내가 실제로 받은 누적 손실과, 사후적으로 가장 좋았던 고정 행동의 누적 손실 차이다. 후회 최소화는 시간이 지날수록 이 차이를 작게 만들어 평균적으로 최선의 고정 전략만큼 잘하는 알고리즘을 설계하는 분야다.

## 직관 (Intuition)

매일 여러 전문가 중 한 명의 예측을 따라 투자한다고 하자. 처음에는 누가 좋은지 모르지만, 시간이 지나며 잘 맞힌 전문가에게 더 큰 가중치를 줄 수 있다. 후회가 작다는 말은 “처음부터 최고의 전문가를 알았더라면 얻었을 이득”과 비교해 크게 뒤처지지 않았다는 뜻이다.

## 이론 (Theory)

$T$라운드, 행동 집합 $A$, 손실 $\ell_t(a)$가 있다고 하자. 알고리즘이 고른 행동을 $a_t$라고 하면 외부 후회는

$$
Regret_T=
\sum_{t=1}^{T}\ell_t(a_t)
-\min_{a\in A}\sum_{t=1}^{T}\ell_t(a)
$$

이다. 목표는 $Regret_T=o(T)$, 즉 평균 후회 $Regret_T/T$가 0으로 가는 것이다.

전문가 문제에서 Hedge/Exponentiated Weights 알고리즘은 $K$개 전문가에 대해 적절한 학습률을 쓰면

$$
Regret_T=O(\sqrt{T\log K})
$$

를 달성한다. 연속 convex decision set에서는 Online Gradient Descent가 지름 $D$, gradient norm 상계 $G$에 대해

$$
Regret_T=O(DG\sqrt{T})
$$

형태의 보장을 준다.

### Regret의 기준점

외부 후회는 사후 최선의 고정 행동과 비교한다. 이는 매 라운드 최선 행동을 안다는 더 강한 기준과 다르다. 환경이 계속 바뀌면 최선 고정 행동과의 비교는 달성 가능하지만, 매 시점 최선과의 비교는 불가능하거나 너무 강할 수 있다.

Internal regret이나 swap regret은 더 강한 균형 개념과 연결된다. 어떤 기준점을 선택하는지가 알고리즘과 보장 의미를 바꾼다.

### Stochastic과 adversarial

Stochastic setting에서는 손실이 고정 분포에서 생성된다고 보고, adversarial setting에서는 손실 sequence가 매우 적대적일 수 있다고 본다. Adversarial regret bound는 더 강하지만 보수적이고, stochastic 구조를 활용하면 더 빠른 rate나 gap-dependent bound가 가능하다.

### OCO 관점

Online convex optimization에서는 매 라운드 $x_t$를 고르고 convex loss $f_t$를 받은 뒤 gradient를 이용해 다음 결정을 조정한다. Projection은 feasible set constraint를 유지한다.

이 프레임워크는 online learning, adaptive optimization, game dynamics를 하나의 언어로 묶는다.

### 평균 후회의 의미

$Regret_T=o(T)$이면 평균 후회가 0으로 간다. 즉 장기적으로는 최선 고정 행동과 라운드당 손실 차이가 사라진다. 하지만 초기 몇 라운드의 큰 손실이나 fairness constraint는 별도 관리가 필요하다.

## 구현 (Implementation)

Hedge 알고리즘의 핵심은 손실이 작은 전문가의 가중치를 지수적으로 덜 깎는 것이다.

```python
import math


def hedge(losses, eta):
    # losses[t][k]: t라운드에서 k번째 전문가의 손실
    k = len(losses[0])
    weights = [1.0 / k] * k
    choices = []

    for row in losses:
        choices.append(max(range(k), key=lambda i: weights[i]))
        weights = [w * math.exp(-eta * loss) for w, loss in zip(weights, row)]
        z = sum(weights)
        weights = [w / z for w in weights]

    return choices, weights


losses = [
    [0.1, 0.6, 0.4],
    [0.2, 0.5, 0.3],
    [0.8, 0.2, 0.4],
]

print(hedge(losses, eta=0.8))
```

실제 알고리즘은 가중치 분포에서 행동을 샘플링하거나 기대 손실을 최소화하는 방식으로 사용된다.

```python
def average_regret(total_regret, rounds):
    return total_regret / rounds
```

Regret bound는 누적량으로 쓰지만, 장기 성능 해석은 평균 후회가 줄어드는지를 본다.

## 복잡도 (Complexity)

전문가 $K$개, 라운드 $T$개이면 Hedge의 기본 구현은 $O(TK)$ 시간과 $O(K)$ 메모리를 사용한다. 연속 공간의 online gradient descent는 라운드마다 gradient 계산과 feasible set projection 비용이 든다.

## 응용 (Applications)

- 온라인 예측과 전문가 조합
- 광고/추천의 순차적 의사결정
- 게임 이론에서 no-regret learning과 균형 근사
- 강화학습, bandit, adaptive routing의 이론적 기초

## 흔한 오해 (Common Misunderstandings)

- 후회 최소화는 미래 손실을 예언한다는 뜻이 아니다. 사후 최선 고정 행동과의 차이를 통제한다.
- 낮은 regret은 모든 시점에서 최고 행동을 골랐다는 뜻이 아니다.
- adversarial setting의 보장은 stochastic setting의 기대 보장과 다르다.
- exploration이 필요한 bandit 문제에서는 전체 손실 벡터를 보는 전문가 문제보다 더 어렵다.

## TMI

- no-regret 알고리즘들이 서로 게임을 하면 경험적 행동 분포가 균형 개념에 가까워질 수 있다.
- multiplicative weights는 알고리즘, 최적화, 게임 이론, 부스팅에 반복해서 등장하는 강력한 원형이다.
- bandit feedback에서는 선택한 행동의 손실만 보이므로 regret bound에 행동 수 의존성이 더 크게 들어간다.

## 연습 / 확인 문제 (Exercises)

- $Regret_T=O(\sqrt{T})$이면 평균 후회가 0으로 감을 보이라.
- Hedge에서 $\eta$가 너무 크면 어떤 문제가 생길지 설명하라.
- 전문가 문제와 multi-armed bandit의 피드백 차이를 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [경사 하강법 수렴 분석](GD-Convergence.md)
- 다음: [전문가 알고리즘](Expert-Algorithms.md), [멀티암드 밴딧](Multi-Armed-Bandit.md)

## 참조 (References)

- [GD-Convergence.md](GD-Convergence.md)
- [Math/Optimization/Convex-Optimization.md](../../Math/Optimization/Convex-Optimization.md)
- [AI/Reinforcement-Learning/MDP.md](../Reinforcement-Learning/MDP.md)
- [Reference/Books.md](../../Reference/Books.md)
