# 비볼록 최적화에서의 수렴 (Non-Convex Convergence)

- Level: Advanced
- Prerequisites: [Convex-Learning.md](Convex-Learning.md), [GD-Convergence.md](GD-Convergence.md), [AI/Deep-Learning/Loss-Functions.md](../Deep-Learning/Loss-Functions.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

비볼록 수렴 분석은 목적 함수에 여러 local minimum, saddle point, 평평한 영역이 있을 때 gradient 기반 알고리즘이 어떤 의미로 “좋은 지점”에 도달하는지 연구한다. 딥러닝 학습 분석의 기본 언어다.

## 직관 (Intuition)

비볼록 지형에서는 아래로 내려가도 전역 최저점에 도착한다는 보장이 없다. 그래도 실무에서는 gradient descent와 SGD가 꽤 잘 작동한다. 이론은 전역 최적해 대신 gradient가 작은 점, saddle 회피, overparameterized 조건에서의 좋은 해 도달 등을 목표로 삼는다.

## 이론 (Theory)

$f$가 $L$-smooth이고 아래로 유계라고 하자. gradient descent에 $\eta=1/L$를 쓰면 다음 형태의 보장이 가능하다.

$$
\min_{0\le t<T}\|\nabla f(x_t)\|^2
\le O\left(\frac{L(f(x_0)-f_\inf)}{T}\right)
$$

이는 전역 최적해 보장이 아니라 first-order stationary point에 가까워진다는 보장이다. 더 강한 second-order stationary point 보장을 얻으려면 saddle point의 음의 곡률 방향을 탈출하는 perturbation이나 stochasticity가 필요할 수 있다.

딥러닝에서는 overparameterization, neural tangent kernel 근사, Polyak-Lojasiewicz 조건, strict saddle property, landscape connectivity 같은 가정 아래 더 강한 결과가 연구된다.

### First-order와 second-order stationarity

First-order stationary point는 gradient norm이 작다는 뜻이다. 하지만 saddle point도 gradient가 0일 수 있다. Second-order stationary point는 Hessian의 큰 음의 고유값이 없어, 명확한 하강 곡률 방향도 없다는 더 강한 조건이다.

비볼록 분석에서 전역 최적해 대신 이런 stationarity 개념을 목표로 삼는 이유는 일반 문제에서 전역 최적성이 너무 어렵기 때문이다.

### Strict saddle과 noise

Strict saddle property가 있으면 최적이 아닌 stationary point에는 음의 곡률 방향이 존재한다. 작은 perturbation이나 SGD noise는 이 방향을 통해 saddle을 탈출하는 데 도움을 줄 수 있다.

그러나 모든 딥러닝 loss가 깨끗한 strict saddle 구조를 갖는 것은 아니다. Plateau, symmetry, degeneracy가 많아 분석이 복잡하다.

### PL 조건

Polyak-Lojasiewicz 조건은 convexity보다 약하지만 gradient norm이 function suboptimality를 제어하게 해 준다.

$$
\frac{1}{2}\|\nabla f(x)\|^2 \ge \mu(f(x)-f^\*)
$$

PL 조건이 있으면 비볼록이어도 gradient descent가 전역 최적값으로 수렴하는 형태의 결과를 얻을 수 있다.

### Overparameterization

과매개변수 모델은 해가 많아 최적화가 쉬워질 수 있다. Neural tangent kernel 관점에서는 충분히 넓은 네트워크가 초기화 근처에서 거의 선형 모델처럼 움직인다고 보고 수렴을 분석한다. 하지만 이 설명이 모든 feature learning 현상을 포착하는 것은 아니다.

## 구현 (Implementation)

비볼록 함수에서도 gradient norm을 모니터링할 수 있다.

```python
import math


def f(x):
    return x ** 4 - 3 * x ** 2 + 2


def grad(x):
    return 4 * x ** 3 - 6 * x


x = 0.3
eta = 0.05
for _ in range(20):
    x -= eta * grad(x)

print(round(x, 3), round(f(x), 3), round(abs(grad(x)), 3))
```

실제 신경망에서는 loss뿐 아니라 gradient norm, validation performance, sharpness, seed별 편차를 함께 본다.

```python
def stationarity_report(grad_norm, hessian_min_eig=None):
    report = {"first_order_small": grad_norm < 1e-3}
    if hessian_min_eig is not None:
        report["negative_curvature"] = hessian_min_eig < -1e-3
    return report
```

비볼록 문제에서는 "loss가 낮다"와 "좋은 stationary point다"를 분리해 봐야 한다.

## 복잡도 (Complexity)

first-order stationary point까지의 반복 수는 일반적으로 $\epsilon^{-2}$ 또는 그와 비슷한 형태로 나타난다. 전역 최적성 보장은 문제 구조 없이는 어렵다. saddle 회피와 second-order 방법은 gradient 외에 Hessian 정보나 추가 계산을 요구할 수 있다.

## 응용 (Applications)

- 딥러닝 optimizer 분석
- matrix factorization과 representation learning 이론
- saddle point와 flat minimum 연구
- overparameterized model의 학습 가능성 분석

## 흔한 오해 (Common Misunderstandings)

- 비볼록이라고 해서 아무 보장도 없는 것은 아니다.
- gradient가 0에 가깝다는 사실만으로 좋은 일반화가 보장되지는 않는다.
- local minimum이 항상 나쁜 것은 아니다. 많은 overparameterized 문제에서는 좋은 local/global minimum이 많을 수 있다.
- 훈련 loss 수렴과 안전한 모델 행동은 별개 문제다.

## TMI

- strict saddle 성질이 있으면 작은 noise가 saddle 탈출에 도움을 줄 수 있다.
- SGD의 stochasticity는 최적화와 일반화 양쪽에 영향을 준다.
- loss landscape 시각화는 유용하지만 2차원 투영에 크게 의존한다.

## 연습 / 확인 문제 (Exercises)

- first-order stationary point와 global minimum의 차이를 설명하라.
- saddle point가 gradient descent를 느리게 만들 수 있는 이유를 말하라.
- overparameterization이 최적화 지형을 좋게 만들 수 있는 직관을 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [볼록 학습](Convex-Learning.md)
- 다음: [경사 하강법 수렴 분석](GD-Convergence.md), [암묵적 규제](Implicit-Regularization.md)

## 참조 (References)

- [Convex-Learning.md](Convex-Learning.md)
- [GD-Convergence.md](GD-Convergence.md)
- [AI/Deep-Learning/Loss-Functions.md](../Deep-Learning/Loss-Functions.md)
- [Reference/Books.md](../../Reference/Books.md)
