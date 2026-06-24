# 연속 함수 (Continuous Functions)

- Level: Advanced
- Prerequisites: [Math/Real-Analysis/Sequences-Series.md](Sequences-Series.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

함수 $f$가 $a$에서 연속이라는 것은 $x$를 $a$에 충분히 가깝게 하면 $f(x)$를 $f(a)$에 원하는 만큼 가깝게 만들 수 있다는 뜻이다.

## 직관 (Intuition)

입력을 조금 바꿨을 때 출력이 갑자기 뛰지 않는다. 다만 "조금"의 크기는 위치 $a$와 원하는 출력 오차에 따라 달라질 수 있다.

## 이론 (Theory)

$$\forall\varepsilon>0\ \exists\delta>0:
|x-a|<\delta\Rightarrow |f(x)-f(a)|<\varepsilon$$

이는 모든 $x_n\to a$에 대해 $f(x_n)\to f(a)$인 sequential characterization과 동치다. 연속함수의 합·곱·합성은 연속이다. Compact interval의 연속함수는 최대·최소를 가지며 intermediate value theorem을 만족한다.

## 구현 (Implementation)

Bisection은 연속함수의 부호가 바뀌는 구간에 root가 있다는 중간값 정리를 사용한다.

```python
def bisect(f, low, high, steps=60):
    for _ in range(steps):
        mid = (low + high) / 2
        if f(low) * f(mid) <= 0:
            high = mid
        else:
            low = mid
    return (low + high) / 2
```

## 복잡도 (Complexity)

Bisection은 구간 폭을 절반으로 줄여 `O(log((b-a)/ε))` 함수 평가가 필요하다.

## 응용 (Applications)

- root finding·optimization
- 안정적 perturbation 분석
- neural network의 연속 mapping
- compact set의 extrema 존재

## 흔한 오해 (Common Misunderstandings)

- 연속이어도 미분 가능하지 않을 수 있다.
- 정의역에 없는 점에서 함수 연속성을 말할 때 경계를 주의한다.
- pointwise continuity가 uniform continuity를 자동 보장하지 않는다.
- float graph가 매끄러워 보여도 증명은 아니다.

## TMI

- $|x|$는 0에서 연속이지만 미분 불가능하다.
- Dirichlet function은 모든 점에서 불연속이다.
- Compact domain의 연속함수는 uniform continuous하다.

## 연습 / 확인 문제 (Exercises)

- $x^2$의 한 점 연속성을 epsilon-delta로 증명하라.
- 연속이지만 미분 불가능한 함수를 제시하라.
- Bisection의 사전조건을 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [수열과 급수](Sequences-Series.md)
- 다음: [균등 연속성](Uniform-Continuity.md), [측도론](Measure-Theory.md)

## 참조 (References)

- [Math/Real-Analysis/Sequences-Series.md](Sequences-Series.md)
- [Reference/Books.md](../../Reference/Books.md)
