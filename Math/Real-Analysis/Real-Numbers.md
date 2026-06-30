# 실수의 완비성 (Completeness of Real Numbers)

- Level: Advanced
- Prerequisites: [Math/Calculus/README.md](../Calculus/README.md), [Math/Discrete/Logic.md](../Discrete/Logic.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

실수의 완비성은 위로 유계인 비어 있지 않은 실수 집합이 최소상계(supremum)를 가진다는 성질이다. 유리수에는 없는 "틈이 없음"을 엄밀하게 표현하며 수렴 정리의 기반이다.

## 직관 (Intuition)

$x^2<2$인 유리수들을 계속 모으면 경계 $\sqrt2$에 가까워지지만 유리수 안에는 그 경계가 없다. 실수는 이런 경계값을 포함하도록 완비되어 있다.

```mermaid
flowchart LR
    Q["유리수 Q<br/>조밀하지만 틈 있음"] --> GAP["sqrt(2) 같은 경계 누락"]
    GAP --> R["실수 R<br/>완비"]
    R --> SUP["상한이 있으면 supremum 존재"]
    R --> CONV["Cauchy 수열 수렴"]
```

## 이론 (Theory)

상계 $M$은 모든 $x\in A$에 $x\le M$을 만족한다. Supremum $s=\sup A$는 상계 중 가장 작다. 완비성은 nested interval theorem, monotone convergence theorem, Bolzano–Weierstrass theorem과 동치 형태로 나타난다.

Archimedean property는 임의의 실수 $x$보다 큰 자연수가 존재함을 말하고, 실수 사이에 유리수와 무리수가 모두 존재하는 density가 따른다.

### supremum과 maximum

집합 $A=(0,1)$에서 1은 상계이고 그중 가장 작은 상계이므로 $\sup A=1$이다. 하지만 $1\notin A$이므로 maximum은 없다. 반면 $[0,1]$은 $\sup A=1$이면서 maximum도 1이다. 해석학에서 supremum을 쓰는 이유는 maximum이 없어도 경계값을 다룰 수 있기 때문이다.

### 완비성의 동치적 얼굴

실수의 완비성은 여러 정리로 나타난다.

| 형태 | 의미 |
|---|---|
| 최소상계 성질 | 위로 유계인 비공집합은 supremum을 가짐 |
| Cauchy 완비성 | 모든 Cauchy 수열이 실수 안에서 수렴 |
| 단조수렴정리 | 단조 증가하고 위로 유계인 수열은 수렴 |
| nested interval theorem | 길이가 0으로 가는 닫힌 구간 중첩의 교집합이 한 점 |

이 정리들은 서로 다른 상황에서 "틈이 없다"를 사용하는 방식이다.

### 유리수에서는 무엇이 깨지나

$A=\{q\in\mathbb{Q}:q^2<2\}$는 유리수 안에서 위로 유계지만 유리수 supremum을 갖지 않는다. 경계는 $\sqrt2$인데 유리수가 아니기 때문이다. 그래서 유리수만으로는 미적분의 극한과 수렴 정리를 안정적으로 세울 수 없다.

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
- 조밀하다는 것과 완비하다는 것은 다르다. $\mathbb Q$는 조밀하지만 완비하지 않다.
- infimum/supremum은 순서 구조의 개념이고, 거리나 노름이 항상 필요한 것은 아니다.

## TMI

- Dedekind cut과 Cauchy sequence equivalence class는 실수를 구성하는 두 방법이다.
- $\mathbb Q$는 조밀하지만 완비하지 않다.
- Infimum은 $\inf A=-\sup(-A)$로 연결된다.

## 연습 / 확인 문제 (Exercises)

- $(0,1)$의 supremum, infimum, maximum, minimum을 구분하라.
- 단조 유계 수열이 수렴함을 완비성으로 설명하라.
- 유리수의 비완비성 예를 제시하라.
- $A=\{x\in\mathbb R:x^2<2\}$의 supremum이 $\sqrt2$임을 설명하라.
- Cauchy 수열이 왜 "수렴 후보를 밖에서 미리 알 필요 없는" 정의인지 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [미적분](../Calculus/)
- 다음: [수열과 급수](Sequences-Series.md)

## 참조 (References)

- [Math/Calculus/README.md](../Calculus/README.md)
- [Reference/Books.md](../../Reference/Books.md)
