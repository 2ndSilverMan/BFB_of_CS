# 적분 (Integration)

- Level: Intermediate
- Prerequisites: [Math/Calculus/Differentiation.md](Differentiation.md), [Math/Calculus/Limits.md](Limits.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

적분은 함수 아래의 넓이를 구하는 연산이자, 미분의 역연산이다. 정적분은 누적량(넓이, 총합)을, 부정적분은 도함수가 주어진 함수를 찾는 일을 뜻한다.

## 직관 (Intuition)

곡선 아래 넓이를 직사각형으로 잘게 쪼개 더하고, 그 폭을 0으로 보내는 극한이 정적분이다. "변화율을 알 때 누적량을 복원한다"는 점에서 미분의 거꾸로다. 속도를 적분하면 거리, 확률밀도를 적분하면 확률이 된다.

## 이론 (Theory)

리만 합의 극한으로 정적분을 정의한다.

$$\int_a^b f(x)\,dx=\lim_{n\to\infty}\sum_{i=1}^{n} f(x_i^*)\,\Delta x$$

**미적분학의 기본정리**가 미분과 적분을 잇는다. $F'=f$이면

$$\int_a^b f(x)\,dx=F(b)-F(a)$$

기법: 치환적분(연쇄 법칙의 역), 부분적분 $\int u\,dv=uv-\int v\,du$, 부분분수. 이상적분은 무한 구간·특이점을 극한으로 다룬다. 모든 초등함수가 초등적 부정적분을 갖지는 않는다(예: $e^{-x^2}$).

## 구현 (Implementation)

```python
def integrate(f, a, b, n=1000):     # 사다리꼴 규칙
    h = (b - a) / n
    total = 0.5 * (f(a) + f(b))
    for i in range(1, n):
        total += f(a + i * h)
    return total * h
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

## TMI

- 적분 기호 $\int$는 라이프니츠가 "합(summa)"의 S를 늘여 만든 것이다.
- $\int e^{-x^2}dx$는 초등함수로 안 되지만, 정적분 $\int_{-\infty}^{\infty}e^{-x^2}dx=\sqrt\pi$는 깔끔하다(가우스 적분).
- 몬테카를로 적분은 고차원에서 결정적 방법을 압도해, 통계물리·금융·렌더링에서 표준이다.

## 연습 / 확인 문제 (Exercises)

- $\int_0^1 x^2\,dx$를 기본정리로 구하고 사다리꼴 근사와 비교하라.
- 부분적분으로 $\int x e^x\,dx$를 구하라.
- 사다리꼴 규칙과 심프슨 규칙의 수렴 차수를 같은 함수에서 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [미분](Differentiation.md)
- 다음: [다변수 적분](Multivariable-Integration.md), [Math/Probability-Statistics/Expectation.md](../Probability-Statistics/Expectation.md)

## 참조 (References)

- [Math/Calculus/Differentiation.md](Differentiation.md)
- [Math/Probability-Statistics/Expectation.md](../Probability-Statistics/Expectation.md)
- [Reference/Books.md](../../Reference/Books.md)
