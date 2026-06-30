# 볼록 최적화 기초 (Convex Optimization)

- Level: Intermediate
- Prerequisites: [Math/Calculus/Differentiation.md](../Calculus/Differentiation.md), [Math/Linear-Algebra/Vectors.md](../Linear-Algebra/Vectors.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

볼록 최적화는 볼록 집합 위에서 볼록 목적 함수를 최소화하는 문제다. 볼록 문제에서는 모든 지역 최솟값이 전역 최솟값이므로, 해의 품질을 이론적으로 보장하면서 효율적인 알고리즘을 설계할 수 있다.

## 직관 (Intuition)

볼록 함수의 그래프는 그릇처럼 가운데가 내려가 있고 두 점을 잇는 선분이 그래프 아래로 파고들지 않는다. 어느 지점에서 내려가도 서로 다른 깊은 골짜기에 갇힐 일이 없다. 반면 비볼록 함수는 여러 골짜기와 안장점을 가질 수 있다.

```mermaid
flowchart LR
    PROB["최적화 문제"] --> SET["가능 영역이 볼록인가?"]
    SET --> OBJ["목적 함수가 볼록인가?"]
    OBJ --> GUAR["지역 최솟값 = 전역 최솟값"]
    GUAR --> ALG["경사법, 내부점법, 쌍대성"]
```

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

### 왜 지역 최솟값이 전역 최솟값인가

볼록 함수에서 어떤 점 $x^\*$가 지역 최솟값인데 더 좋은 점 $y$가 있다고 가정해 보자. $x^\*$와 $y$를 잇는 선분 위의 점은 볼록성 때문에 함수값이 $f(x^\*)$에서 $f(y)$ 쪽으로 내려가는 방향을 가져야 한다. 그러면 $x^\*$ 주변에도 더 낮은 점이 생겨 지역 최솟값이라는 가정과 모순된다. 이 단순한 구조가 볼록 최적화의 가장 큰 힘이다.

### 강볼록성과 매끄러움

볼록성은 전역 최적 구조를 주지만, 수렴 속도는 곡률 조건에 크게 좌우된다.

| 조건 | 의미 | 최적화 영향 |
|---|---|---|
| $L$-smooth | gradient가 너무 급격히 변하지 않음 | 안정적인 학습률 상한 제공 |
| $\mu$-strongly convex | 모든 방향에 최소 곡률이 있음 | 해가 유일하고 선형 수렴 가능 |
| condition number $L/\mu$ | 길쭉한 정도 | 클수록 경사하강이 지그재그 |

이차함수 $f(x)=\frac12x^\top Qx+c^\top x$에서는 $Q$의 고유값이 곡률을 나타낸다. 가장 큰 고유값은 학습률 상한, 가장 작은 양의 고유값은 강볼록성을 결정한다.

### 문제 정식화가 알고리즘만큼 중요하다

같은 현실 문제도 변수 선택과 제약 표현에 따라 볼록 문제가 되기도 하고 비볼록 문제가 되기도 한다. 예를 들어 norm 최소화, hinge loss, log-sum-exp는 볼록 원자지만, 변수끼리 곱하거나 rank 제약을 넣으면 비볼록성이 생기기 쉽다. 실무의 첫 단계는 "이 문제가 볼록으로 표현되는가"를 확인하는 것이다.

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

Hessian으로 이차함수의 볼록성을 확인하는 작은 예:

```python
import numpy as np

Q = np.array([[3.0, 1.0],
              [1.0, 2.0]])
eigenvalues = np.linalg.eigvalsh(Q)
print(eigenvalues)            # 모두 양수이면 양정부호
print(np.all(eigenvalues >= -1e-12))
```

## 복잡도 (Complexity)

복잡도는 함수 구조와 정확도 $\varepsilon$에 따라 달라진다. 매끄러운 볼록 함수의 경사 하강법은 대표적으로 함수값 오차 $O(1/t)$, 강볼록이면 적절한 조건에서 선형 수렴을 보인다. 내부점법은 높은 정확도에 강하지만 큰 문제에서 한 스텝 비용이 크다.

대규모 ML에서는 정확도 높은 해보다 충분히 좋은 해가 더 중요할 수 있어 first-order method를 많이 쓴다. 반대로 제약이 강하고 정확한 feasibility가 중요한 운영 최적화에서는 solver 기반 방법이 더 적합하다.

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
- 선형 함수는 볼록이면서 오목이다. 그래서 선형 목적과 선형 제약은 볼록 최적화에 들어간다.
- 볼록 문제도 잘못 스케일링하면 수치적으로 어려울 수 있다. 변수 단위와 조건수를 확인해야 한다.

## TMI

- 최대화 문제에서는 concave 함수를 최대화하는 것이 볼록 최적화의 표준 형태다.
- Jensen 부등식은 볼록 함수와 기댓값을 연결하며 확률·정보 이론에 자주 등장한다.
- 비볼록 문제를 볼록 문제로 완화해 계산 가능한 하한이나 근사해를 얻기도 한다.

## 연습 / 확인 문제 (Exercises)

- $x^2$, $|x|$, $-\log x$의 볼록성을 정의나 이차 미분으로 확인하라.
- 두 볼록 집합의 교집합이 볼록임을 증명하라.
- 선형 회귀의 MSE가 파라미터에 대해 볼록인 이유를 설명하라.
- $f(x,y)=x^2+10y^2$의 Hessian 고유값과 condition number를 계산하라.
- 변수 곱 $xy$가 들어간 제약이 왜 볼록성을 깨뜨릴 수 있는지 예를 들어 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [미분](../Calculus/Differentiation.md)
- 다음: [경사 하강법](Gradient-Descent.md)
- 관련: [라그랑주 승수법](Lagrangian.md)

## 참조 (References)

- [Math/Calculus/Differentiation.md](../Calculus/Differentiation.md)
- [Math/Linear-Algebra/Vectors.md](../Linear-Algebra/Vectors.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
