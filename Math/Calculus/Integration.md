# 적분 (Integration)

- Level: Intermediate
- Prerequisites: [Math/Calculus/Differentiation.md](Differentiation.md), [Math/Calculus/Limits.md](Limits.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

적분은 함수 아래의 넓이를 구하는 연산이자, 미분의 역연산이다. 정적분은 누적량(넓이, 총합)을, 부정적분은 도함수가 주어진 함수를 찾는 일을 뜻한다.

## 직관 (Intuition)

곡선 아래 넓이를 직사각형으로 잘게 쪼개 더하고, 그 폭을 0으로 보내는 극한이 정적분이다. "변화율을 알 때 누적량을 복원한다"는 점에서 미분의 거꾸로다. 속도를 적분하면 거리, 확률밀도를 적분하면 확률이 된다.

```mermaid
flowchart LR
    RATE["변화율 f(x)"] --> SUM["작은 구간의 기여<br/>f(x_i) Delta x"]
    SUM --> LIMIT["분할을 촘촘히<br/>Delta x -> 0"]
    LIMIT --> INT["정적분<br/>누적량"]
    INT --> FTC["F(b)-F(a)<br/>기본정리"]
```

## 이론 (Theory)

리만 합의 극한으로 정적분을 정의한다.

$$\int_a^b f(x)\,dx=\lim_{n\to\infty}\sum_{i=1}^{n} f(x_i^*)\,\Delta x$$

**미적분학의 기본정리**가 미분과 적분을 잇는다. $F'=f$이면

$$\int_a^b f(x)\,dx=F(b)-F(a)$$

기법: 치환적분(연쇄 법칙의 역), 부분적분 $\int u\,dv=uv-\int v\,du$, 부분분수. 이상적분은 무한 구간·특이점을 극한으로 다룬다. 모든 초등함수가 초등적 부정적분을 갖지는 않는다(예: $e^{-x^2}$).

### 정적분과 부정적분을 구분하기

부정적분은 함수족을 찾는 일이다.

$$
\int f(x)\,dx=F(x)+C
$$

정적분은 구간 위 누적값을 계산하는 일이다.

$$
\int_a^b f(x)\,dx
$$

두 개념은 미적분학의 기본정리로 연결되지만, 의미가 다르다. 부정적분은 상수 차이를 구분하지 못하고, 정적분은 구간과 방향이 중요하다. $a>b$이면 $\int_a^b f(x)\,dx=-\int_b^a f(x)\,dx$다.

### 치환적분은 변수 단위 보정이다

$u=g(x)$로 변수를 바꾸면 $du=g'(x)dx$가 함께 바뀐다. 이 항을 빼먹으면 작은 구간의 폭이 어떻게 늘어나거나 줄어드는지를 반영하지 못한다. 다변수 적분의 야코비안도 같은 생각이다.

### 워크드 예제

$$
\int_0^1 x^2\,dx=\left[\frac{x^3}{3}\right]_0^1=\frac13
$$

수치 적분은 이 값을 근사한다. 사다리꼴 규칙은 구간을 직선으로 이어 넓이를 더하므로, 함수가 많이 휘어 있을수록 더 촘촘한 분할이 필요하다.

## 구현 (Implementation)

```python
def integrate(f, a, b, n=1000):     # 사다리꼴 규칙
    h = (b - a) / n
    total = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        total += f(a + i * h)
    return total * h

print(integrate(lambda x: x*x, 0.0, 1.0, n=1000))  # ~1/3
```

몬테카를로 적분은 구간에서 무작위 표본을 뽑아 평균을 구한다.

```python
import random

def monte_carlo_integrate(f, a, b, samples=10000):
    avg = sum(f(random.uniform(a, b)) for _ in range(samples)) / samples
    return (b - a) * avg
```

## 복잡도 (Complexity)

수치 적분은 분할 수 $n$에 비례해 `O(n)` 평가가 든다. 사다리꼴은 오차 `O(h^2)`, 심프슨 규칙은 `O(h^4)`로 더 빠르게 수렴한다. 고차원 적분은 차원의 저주로 격자 방식이 폭발해 몬테카를로 적분을 쓴다(오차가 차원과 무관하게 `O(1/√N)`).

## 응용 (Applications)

- 확률밀도의 누적분포·기댓값 계산
- 물리량(일, 질량, 전하)의 누적
- 신호 처리의 면적·에너지
- 머신러닝의 주변화(marginalization), 정규화 상수

## 흔한 오해 (Common Misunderstandings)

- 부정적분에는 상수 $+C$가 붙는다(도함수가 같은 함수는 무수히 많다).
- 모든 함수가 닫힌 형식 적분을 갖지는 않는다.
- 정적분 값은 넓이이지만, 축 아래 부분은 음의 기여를 한다.
- 적분 가능성과 연속성은 다르다(유한 불연속이어도 적분 가능할 수 있다).
- 치환적분에서 $dx$가 어떻게 바뀌는지 추적하지 않으면 스케일이 틀린다.
- 수치 적분값이 안정적으로 보인다고 오차 추정이 끝난 것은 아니다. 분할 수를 바꾸거나 다른 규칙과 비교해야 한다.

## TMI

- 적분 기호 $\int$는 라이프니츠가 "합(summa)"의 S를 늘여 만든 것이다.
- $\int e^{-x^2}dx$는 초등함수로 안 되지만, 정적분 $\int_{-\infty}^{\infty}e^{-x^2}dx=\sqrt\pi$는 깔끔하다(가우스 적분).
- 몬테카를로 적분은 고차원에서 결정적 방법을 압도해, 통계물리·금융·렌더링에서 표준이다.

## 연습 / 확인 문제 (Exercises)

- $\int_0^1 x^2\,dx$를 기본정리로 구하고 사다리꼴 근사와 비교하라.
- 부분적분으로 $\int x e^x\,dx$를 구하라.
- 사다리꼴 규칙과 심프슨 규칙의 수렴 차수를 같은 함수에서 비교하라.
- 치환 $u=x^2+1$로 $\int 2x(x^2+1)^3 dx$를 계산하라.
- 몬테카를로 적분의 표본 수를 4배로 늘렸을 때 오차가 대략 어떻게 변하는지 관찰하라.

## 이어서 읽기 (Reading Path)

- 이전: [미분](Differentiation.md)
- 다음: [다변수 적분](Multivariable-Integration.md), [Math/Probability-Statistics/Expectation.md](../Probability-Statistics/Expectation.md)

## 참조 (References)

- [Math/Calculus/Differentiation.md](Differentiation.md)
- [Math/Probability-Statistics/Expectation.md](../Probability-Statistics/Expectation.md)
- [Reference/Books.md](../../Reference/Books.md)
