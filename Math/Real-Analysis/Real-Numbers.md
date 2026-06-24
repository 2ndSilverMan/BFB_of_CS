# 실수의 완비성 (Completeness of Real Numbers)

- Level: Advanced
- Prerequisites: [Math/Calculus/README.md](../Calculus/README.md), [Math/Discrete/Logic.md](../Discrete/Logic.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

실수의 완비성은 위로 유계인 비어 있지 않은 실수 집합이 최소상계(supremum)를 가진다는 성질이다. 유리수에는 없는 "틈이 없음"을 엄밀하게 표현하며 수렴 정리의 기반이다.

## 직관 (Intuition)

$x^2<2$인 유리수들을 계속 모으면 경계 $\sqrt2$에 가까워지지만 유리수 안에는 그 경계가 없다. 실수는 이런 경계값을 포함하도록 완비되어 있다.

## 이론 (Theory)

상계 $M$은 모든 $x\in A$에 $x\le M$을 만족한다. Supremum $s=\sup A$는 상계 중 가장 작다. 완비성은 nested interval theorem, monotone convergence theorem, Bolzano–Weierstrass theorem과 동치 형태로 나타난다.

Archimedean property는 임의의 실수 $x$보다 큰 자연수가 존재함을 말하고, 실수 사이에 유리수와 무리수가 모두 존재하는 density가 따른다.

## 구현 (Implementation)

제곱근 2의 경계를 이분 탐색으로 근사한다.

```python
low, high = 1.0, 2.0
for _ in range(60):
    mid = (low + high) / 2
    if mid * mid < 2:
        low = mid
    else:
        high = mid
print((low + high) / 2)
```

부동소수점은 실수 전체가 아니라 유한 근사임을 구분한다.

## 복잡도 (Complexity)

이분 탐색은 오차 구간을 매번 절반으로 줄여 정확도 $\varepsilon$에 `O(log(1/ε))` 반복이 필요하다.

## 응용 (Applications)

- 극한·연속·미분·적분 정리
- 수치 알고리즘의 수렴 근거
- 확률·측도 공간의 실수값 함수
- 최적화에서 infimum 존재 분석

## 흔한 오해 (Common Misunderstandings)

- supremum이 집합 원소일 필요는 없다.
- 유계 집합에 maximum이 항상 존재하는 것은 아니다.
- 완비성과 compactness는 동일한 개념이 아니다.
- 컴퓨터 float가 실수의 완비성을 구현하지 않는다.

## TMI

- Dedekind cut과 Cauchy sequence equivalence class는 실수를 구성하는 두 방법이다.
- $\mathbb Q$는 조밀하지만 완비하지 않다.
- Infimum은 $\inf A=-\sup(-A)$로 연결된다.

## 연습 / 확인 문제 (Exercises)

- $(0,1)$의 supremum, infimum, maximum, minimum을 구분하라.
- 단조 유계 수열이 수렴함을 완비성으로 설명하라.
- 유리수의 비완비성 예를 제시하라.

## 이어서 읽기 (Reading Path)

- 이전: [미적분](../Calculus/)
- 다음: [수열과 급수](Sequences-Series.md)

## 참조 (References)

- [Math/Calculus/README.md](../Calculus/README.md)
- [Reference/Books.md](../../Reference/Books.md)
