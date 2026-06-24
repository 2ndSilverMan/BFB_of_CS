# 함수 공간 (Function Spaces)

- Level: Advanced
- Prerequisites: [Math/Real-Analysis/Measure-Theory.md](Measure-Theory.md), [Math/Linear-Algebra/Vectors.md](../Linear-Algebra/Vectors.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

함수 공간은 함수를 vector처럼 더하고 scalar를 곱하며 norm·inner product·distance로 비교하는 공간이다. $C([a,b])$, $L^p$, Hilbert·Banach space가 대표적이다.

## 직관 (Intuition)

유한 차원 vector의 좌표 대신 함수 전체를 하나의 점으로 본다. 두 함수가 얼마나 가까운지는 최대 오차, 평균 절대 오차, 제곱 적분 등 목적에 맞는 norm으로 정한다.

## 이론 (Theory)

$$\|f\|_p=\left(\int|f(x)|^p\,d\mu\right)^{1/p},\qquad
\|f\|_\infty=\operatorname*{ess\,sup}|f|$$

$L^p$는 almost everywhere 같은 함수를 동일시한다. Banach space는 norm에 대해 complete하고, Hilbert space는 inner product가 norm을 유도하는 complete space다. $L^2$의 inner product는 $\langle f,g\rangle=\int f g$이며 orthogonal projection과 Fourier expansion을 일반화한다.

## 구현 (Implementation)

표본 grid에서 $L^2$ distance를 근사한다.

```python
import math


def discrete_l2(f_values, g_values, dx):
    return math.sqrt(sum((f - g) ** 2 for f, g in zip(f_values, g_values)) * dx)
```

## 복잡도 (Complexity)

$n$개 grid point의 discrete norm은 `O(n)`이다. Infinite-dimensional 문제는 basis truncation·finite element 등으로 유한 근사한다.

## 응용 (Applications)

- differential equation·signal processing
- kernel method와 RKHS
- probability random variable norm
- function approximation·learning theory

## 흔한 오해 (Common Misunderstandings)

- 다른 norm은 다른 convergence 개념을 만든다.
- $L^p$ 원소는 pointwise 함수보다 almost-everywhere equivalence class다.
- 모든 Banach space가 inner product를 갖는 것은 아니다.
- 유한 차원 intuition이 무한 차원에서 항상 유지되지 않는다.

## TMI

- 모든 Hilbert space는 orthonormal basis에 대해 좌표를 가질 수 있다.
- RKHS에서는 point evaluation이 continuous linear functional이다.
- Fourier series는 function을 orthogonal basis coefficient로 표현한다.

## 연습 / 확인 문제 (Exercises)

- 같은 두 함수의 $L^1,L^2,L^\infty$ 거리를 비교하라.
- $L^2$에서 두 함수의 직교성을 확인하라.
- finite-dimensional vector norm과 function norm을 연결하라.

## 이어서 읽기 (Reading Path)

- 이전: [측도론 입문](Measure-Theory.md)
- 다음: [이론적 머신러닝](../../AI/Theoretical-ML/)

## 참조 (References)

- [Math/Real-Analysis/Measure-Theory.md](Measure-Theory.md)
- [Math/Linear-Algebra/Vectors.md](../Linear-Algebra/Vectors.md)
- [Reference/Books.md](../../Reference/Books.md)
