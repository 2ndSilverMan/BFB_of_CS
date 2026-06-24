# 볼록 최적화 기초 (Convex Optimization)

- Level: Intermediate
- Prerequisites: [Math/Calculus/Differentiation.md](../Calculus/Differentiation.md), [Math/Linear-Algebra/Vectors.md](../Linear-Algebra/Vectors.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

볼록 최적화는 볼록 집합 위에서 볼록 목적 함수를 최소화하는 문제다. 볼록 문제에서는 모든 지역 최솟값이 전역 최솟값이므로, 해의 품질을 이론적으로 보장하면서 효율적인 알고리즘을 설계할 수 있다.

## 직관 (Intuition)

볼록 함수의 그래프는 그릇처럼 가운데가 내려가 있고 두 점을 잇는 선분이 그래프 아래로 파고들지 않는다. 어느 지점에서 내려가도 서로 다른 깊은 골짜기에 갇힐 일이 없다. 반면 비볼록 함수는 여러 골짜기와 안장점을 가질 수 있다.

## 이론 (Theory)

집합 $C$가 볼록이라는 뜻은 $\mathbf{x},\mathbf{y}\in C$와 $\lambda\in[0,1]$에 대해

$$
\lambda\mathbf{x}+(1-\lambda)\mathbf{y}\in C
$$

인 것이다. 함수 $f$는 볼록 집합에서

$$
f(\lambda\mathbf{x}+(1-\lambda)\mathbf{y})
\le \lambda f(\mathbf{x})+(1-\lambda)f(\mathbf{y})
$$

를 만족하면 볼록하다. 미분 가능하면 일차 조건

$$
f(\mathbf{y})\ge f(\mathbf{x})+\nabla f(\mathbf{x})^\top(\mathbf{y}-\mathbf{x})
$$

로 판정할 수 있다. 두 번 미분 가능한 함수는 Hessian이 모든 지점에서 양의 준정부호이면 볼록하다. affine 함수, norm, log-sum-exp, 양의 준정부호 이차형식이 대표 예다.

## 구현 (Implementation)

볼록 이차함수 $f(x)=(x-4)^2+1$의 접선이 항상 함수 아래에 있는지 표본점으로 확인한다.

```python
def f(x):
    return (x - 4) ** 2 + 1


def grad(x):
    return 2 * (x - 4)


x0 = 1.0
for y in [-2.0, 0.0, 3.0, 8.0]:
    tangent = f(x0) + grad(x0) * (y - x0)
    assert f(y) >= tangent
```

실전에서는 문제를 규율에 맞는 원자 함수 조합으로 표현하고 검증된 convex solver를 사용한다.

## 복잡도 (Complexity)

복잡도는 함수 구조와 정확도 $\varepsilon$에 따라 달라진다. 매끄러운 볼록 함수의 경사 하강법은 대표적으로 함수값 오차 $O(1/t)$, 강볼록이면 적절한 조건에서 선형 수렴을 보인다. 내부점법은 높은 정확도에 강하지만 큰 문제에서 한 스텝 비용이 크다.

## 응용 (Applications)

- 선형·로지스틱 회귀와 규제
- 포트폴리오, 자원 배분, 스케줄링의 완화 문제
- 신호 복원과 sparse optimization
- 제어, 추정, 네트워크 최적화

## 흔한 오해 (Common Misunderstandings)

- 볼록 함수가 항상 매끄러운 것은 아니다. 절댓값과 norm은 꺾인 점을 가진다.
- 목적 함수만 볼록하면 충분하지 않다. 최소화 문제의 feasible set도 볼록해야 한다.
- Hessian이 양의 준정부호라는 기준은 두 번 미분 가능한 함수에 대한 조건이다.
- 볼록하다고 대규모 문제가 자동으로 싸지는 것은 아니다.

## TMI

- 최대화 문제에서는 concave 함수를 최대화하는 것이 볼록 최적화의 표준 형태다.
- Jensen 부등식은 볼록 함수와 기댓값을 연결하며 확률·정보 이론에 자주 등장한다.
- 비볼록 문제를 볼록 문제로 완화해 계산 가능한 하한이나 근사해를 얻기도 한다.

## 연습 / 확인 문제 (Exercises)

- $x^2$, $|x|$, $-\log x$의 볼록성을 정의나 이차 미분으로 확인하라.
- 두 볼록 집합의 교집합이 볼록임을 증명하라.
- 선형 회귀의 MSE가 파라미터에 대해 볼록인 이유를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [미분](../Calculus/Differentiation.md)
- 다음: [경사 하강법](Gradient-Descent.md)
- 관련: [라그랑주 승수법](Lagrangian.md)

## 참조 (References)

- [Math/Calculus/Differentiation.md](../Calculus/Differentiation.md)
- [Math/Linear-Algebra/Vectors.md](../Linear-Algebra/Vectors.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
