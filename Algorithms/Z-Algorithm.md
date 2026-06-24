# Z 알고리즘 (Z-Algorithm)

- Level: Intermediate
- Prerequisites: [Algorithms/KMP.md](KMP.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

Z 알고리즘은 문자열의 각 위치에서 "그 위치부터 시작하는 접미사와 전체 문자열의 공통 접두사 길이"(Z 배열)를 선형 시간에 구한다. 패턴 매칭, 주기 탐지 등 KMP가 푸는 문제를 다른 관점에서 해결한다.

## 직관 (Intuition)

문자열의 각 시작점에서 "맨 앞과 얼마나 똑같이 시작하는가"를 알면, 패턴+구분자+텍스트를 이어 붙여 한 번에 매칭할 수 있다. 핵심은 이미 계산한 일치 구간([l, r], Z-box)을 재활용해, 같은 비교를 반복하지 않는 것이다.

## 이론 (Theory)

$Z[i]$ = $S$와 $S[i..]$의 최장 공통 접두사 길이($Z[0]$은 정의상 보통 0 또는 전체 길이). 가장 오른쪽까지 뻗은 일치 구간 $[l,r]$을 유지한다.

- $i\le r$이면 대칭 위치 $Z[i-l]$를 재활용해 시작값을 얻고, 필요 시 $r$ 너머만 추가 비교.
- $i>r$이면 직접 비교로 새 Z-box를 연다.

각 문자는 상수 번만 비교되어 전체 `O(n)`이다. 패턴 $P$와 텍스트 $T$에 대해 $S=P+\#+T$의 Z 배열에서 $Z[i]=|P|$인 위치가 매칭이다.

## 구현 (Implementation)

```python
def z_function(s):
    n = len(s); z = [0]*n; l = r = 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])    # Z-box 내부: 대칭 재활용
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1                       # 추가 비교
        if i + z[i] > r:
            l, r = i, i + z[i]              # Z-box 갱신
    return z
```

## 복잡도 (Complexity)

| | 시간 | 공간 |
|---|---|---|
| Z 배열 | `O(n)` | `O(n)` |

KMP와 같은 선형 시간이며, 구현이 짧고 직관적이라 선호되기도 한다. 매칭은 결합 문자열 길이 `O(n+m)`.

## 응용 (Applications)

- 패턴 매칭(KMP 대체)
- 문자열의 주기·테두리(border) 분석
- 서로 다른 부분문자열 수 세기(다른 기법과 결합)
- 문자열 압축·반복 구조 탐지

## 흔한 오해 (Common Misunderstandings)

- $Z[0]$의 정의는 관례에 따라 다르다(0 또는 $n$).
- Z 알고리즘과 KMP는 표현만 다를 뿐 같은 문제를 선형에 푼다.
- 패턴 매칭 시 구분자는 텍스트·패턴에 없는 문자를 써야 한다.
- Z-box 재활용에서 `min(r-i, z[i-l])` 경계를 빠뜨리면 틀린다.

## TMI

- Z 함수와 KMP 실패 함수는 서로 변환 가능하다 — 같은 정보의 두 표현이다.
- 많은 경쟁 프로그래머가 짧은 코드 때문에 KMP보다 Z를 선호한다.
- "Z-box"라는 직관적 시각화가 알고리즘을 외우기 쉽게 만든다.

## 연습 / 확인 문제 (Exercises)

- "aabxaabxcaabxaabxay"의 Z 배열 일부를 손으로 구하라.
- Z 배열로 패턴 매칭을 수행하는 결합 문자열을 작성하라.
- Z와 KMP 실패 함수의 관계를 한 예로 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [KMP](KMP.md)
- 다음: [Rabin-Karp](Rabin-Karp.md)

## 참조 (References)

- [Algorithms/KMP.md](KMP.md)
- [Reference/Books.md](../Reference/Books.md)
