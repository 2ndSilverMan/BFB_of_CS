# 경사 하강법 수렴 분석 (Gradient Descent Convergence)

- Level: Advanced
- Prerequisites: [Math/Optimization/Gradient-Descent.md](../../Math/Optimization/Gradient-Descent.md), [Math/Optimization/Convex-Optimization.md](../../Math/Optimization/Convex-Optimization.md), [Double-Descent.md](Double-Descent.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

경사 하강법 수렴 분석은 반복식

$$
x_{t+1}=x_t-\eta \nabla f(x_t)
$$

이 어떤 조건에서 최적해나 stationary point에 가까워지는지, 그리고 몇 번의 반복이 필요한지 밝히는 이론이다. 학습률 $\eta$, smoothness, convexity, strong convexity가 핵심 가정이다.

## 직관 (Intuition)

경사는 가장 가파르게 올라가는 방향이므로 그 반대로 조금 움직이면 함수값이 내려간다. 하지만 너무 크게 움직이면 계곡을 지나쳐 발산할 수 있고, 지형이 평평하거나 비볼록이면 느리게 움직이거나 안장점 근처에서 머뭇거릴 수 있다. 수렴 분석은 “얼마나 조금씩, 얼마나 오래” 움직여야 하는지 계산한다.

## 이론 (Theory)

$f$가 $L$-smooth이면 다음 부등식이 성립한다.

$$
f(y)\le f(x)+\nabla f(x)^\top(y-x)+\frac{L}{2}\|y-x\|^2
$$

$\eta \le 1/L$로 두면 매 반복에서 충분한 감소를 보장할 수 있다. 볼록 함수에서는 대략

$$
f(x_T)-f(x^\*)=O\left(\frac{L\|x_0-x^\*\|^2}{T}\right)
$$

수렴률을 얻는다. $\mu$-strongly convex이면 더 강하게

$$
f(x_T)-f(x^\*) \le (1-\eta\mu)^T(f(x_0)-f(x^\*))
$$

형태의 선형 수렴이 가능하다.

비볼록 함수에서는 전역 최적성 대신 gradient norm이 작은 점을 찾는 보장을 자주 사용한다. $\eta=1/L$인 경우 평균적으로

$$
\min_{0\le t<T}\|\nabla f(x_t)\|^2
\le O\left(\frac{L(f(x_0)-f_\inf)}{T}\right)
$$

같은 stationary point 수렴 경계를 얻는다.

## 구현 (Implementation)

2차 함수에서는 수렴 조건을 직접 관찰할 수 있다.

```python
def gradient_descent_quadratic(a, x0, eta, steps):
    # f(x) = 0.5 * a * x^2, L = a
    x = x0
    history = []
    for _ in range(steps):
        history.append(0.5 * a * x * x)
        x = x - eta * a * x
    return history


print(gradient_descent_quadratic(a=4.0, x0=1.0, eta=0.2, steps=5))
print(gradient_descent_quadratic(a=4.0, x0=1.0, eta=0.6, steps=5))  # 너무 큼
```

여기서 $L=4$이고 안정적인 학습률은 대략 $0<\eta<2/L$ 범위다. 일반적인 보수적 분석은 $\eta\le1/L$를 자주 사용한다.

## 복잡도 (Complexity)

각 반복 비용은 gradient 계산 비용이다. 볼록 smooth 문제에서 $\epsilon$ 정확도까지는 보통 $O(1/\epsilon)$ 반복, strongly convex 문제에서는 $O(\log(1/\epsilon))$ 반복이 필요하다. 조건수가 나쁘면 실제 수렴은 훨씬 느려질 수 있다.

## 응용 (Applications)

- 선형/로지스틱 회귀 학습률 선택
- 딥러닝 optimizer 안정성 이해
- SGD, momentum, adaptive method 분석의 기초
- loss landscape와 implicit regularization 연구

## 흔한 오해 (Common Misunderstandings)

- 손실이 매번 감소한다고 해서 일반화가 좋아지는 것은 아니다.
- 비볼록 문제에서 gradient descent가 항상 전역 최적해를 찾는 것은 아니다.
- 학습률이 작을수록 무조건 좋은 것은 아니다. 안정하지만 지나치게 느릴 수 있다.
- 이론적 수렴률은 가정이 맞을 때의 보장이지 모든 실험 곡선의 예측치는 아니다.

## TMI

- 조건수가 큰 quadratic에서는 steepest descent가 좁은 계곡을 지그재그로 내려간다.
- momentum은 오래 유지되는 방향을 누적해 이런 지그재그를 줄일 수 있다.
- 딥러닝에서는 같은 훈련 손실 0 해 중 어떤 해로 가는지가 일반화와 연결되며, 이를 implicit bias 관점에서 분석한다.

## 연습 / 확인 문제 (Exercises)

- $f(x)=\frac{1}{2}ax^2$에서 경사 하강법 반복식을 닫힌형으로 풀어라.
- $L$-smooth 조건에서 descent lemma를 사용해 함수값 감소를 유도하라.
- convex와 strongly convex 수렴률 차이를 예시로 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [이중 강하](Double-Descent.md)
- 다음: [후회 최소화](Regret-Minimization.md)

## 참조 (References)

- [Math/Optimization/Gradient-Descent.md](../../Math/Optimization/Gradient-Descent.md)
- [Math/Optimization/Convex-Optimization.md](../../Math/Optimization/Convex-Optimization.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
