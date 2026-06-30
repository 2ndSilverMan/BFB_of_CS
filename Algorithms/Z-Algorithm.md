# Z 알고리즘 (Z-Algorithm)

- Level: Intermediate
- Prerequisites: [Algorithms/KMP.md](KMP.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

Z 알고리즘은 각 위치 $i$ 에서 **"$S[i..]$ 와 $S$ 전체의 최장 공통 접두사 길이"**(Z 배열)를 $O(n)$ 에 구한다. [KMP](KMP.md)가 푸는 문제를 다른 관점에서 — border가 아니라 "맨 앞과의 일치 길이"로 — 해결한다.

## 직관 (Intuition)

각 시작점이 "맨 앞과 얼마나 똑같이 시작하나"를 알면, `패턴 # 텍스트` 를 이어 붙여 한 번에 매칭한다. 핵심은 이미 계산한 일치 구간(**Z-box** $[l,r]$, 가장 오른쪽까지 뻗은 일치)을 **대칭으로 재활용**해 같은 비교를 반복하지 않는 것.

## 이론 (Theory)

### 1. Z-box 재활용

$[l,r]$ = 지금까지 본 것 중 "$S$ 의 접두사와 일치하며 가장 오른쪽까지 뻗은 구간". 새 $i$ 에 대해:

- $i\le r$: $i$ 는 Z-box 안 → 대칭 위치 $i-l$ 의 값 $Z[i-l]$ 을 재활용해 $Z[i]=\min(r-i,\ Z[i-l])$ 로 시작, $r$ 너머만 추가 비교.
- $i>r$: 직접 비교로 새 Z-box를 연다.

### 2. 선형성 (amortized)

추가 비교는 **$r$ 을 전진시킬 때만** 일어나고 $r$ 은 단조 증가($\le n$) → 총 추가 비교 $O(n)$. KMP와 같은 선형이지만 코드가 짧다.

### 3. 매칭과 KMP 관계

$S=P\,\#\,T$ ($\#$ 는 양쪽에 없는 구분자)의 Z 배열에서 $Z[i]=|P|$ 인 위치가 매칭. **Z 함수와 KMP 실패 함수는 상호 변환 가능** — 같은 정보의 두 표현이다.

## 구현 (Implementation)

```python
def z_function(s):
    n = len(s); z = [0]*n; l = r = 0
    for i in range(1, n):
        if i < r:
            z[i] = min(r - i, z[i - l])         # Z-box 내부: 대칭 재활용
        while i + z[i] < n and s[z[i]] == s[i + z[i]]:
            z[i] += 1                            # 추가 비교 (r 전진 시에만)
        if i + z[i] > r:
            l, r = i, i + z[i]                   # Z-box 갱신
    return z

def search(pat, text, sep="\x00"):
    s = pat + sep + text; z = z_function(s); m = len(pat)
    return [i - m - 1 for i in range(m+1, len(s)) if z[i] == m]
```

## 복잡도 (Complexity)

| | 시간 | 공간 |
|---|---|---|
| Z 배열 | $O(n)$ | $O(n)$ |
| 매칭 | $O(n+m)$ | $O(n+m)$ |

**워크드 예제(`aabxaab...`).** `aab` 로 시작하는 문자열에서 $i=4$ 가 다시 `aab` 면 $Z[4]\ge3$. Z-box를 열어 두면 그 안의 위치들은 대칭 값으로 즉시 채워진다.

## 응용 (Applications)

- 패턴 매칭(KMP 대체, 짧은 코드).
- 문자열 주기·border 분석, 서로 다른 부분문자열 수(다른 기법과 결합).
- 문자열 압축·반복 구조 탐지.

## 흔한 오해 (Common Misunderstandings)

- **$Z[0]$ 정의는 관례에 따라** 0 또는 $n$.
- **Z와 KMP는 표현만 다를 뿐 같은 문제**를 선형에 푼다.
- **구분자는 텍스트·패턴에 없는 문자**여야 한다.
- **`min(r-i, z[i-l])` 경계를 빠뜨리면** Z-box 밖을 잘못 신뢰해 틀린다.

## TMI

- 많은 경쟁 프로그래머가 짧은 코드 때문에 KMP보다 Z를 선호한다.
- "Z-box" 시각화가 알고리즘을 외우기 쉽게 만든다.
- Z 함수는 접미사 배열·LCP의 직관과도 이어진다(문자열 알고리즘의 공통 뼈대).

## 연습 / 확인 문제 (Exercises)

- `aabxaabxcaabxaabxay` 의 Z 배열 일부를 손으로 구하라.
- Z 배열로 패턴 매칭하는 결합 문자열을 작성하라.
- Z와 KMP 실패 함수를 한 예에서 상호 변환하라.
- $r$ 이 단조 증가하므로 총 비교가 $O(n)$ 임을 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [KMP](KMP.md)
- 다음: [Rabin-Karp](Rabin-Karp.md)
- 관련: [서픽스 배열](Suffix-Array.md)

## 참조 (References)

- [Algorithms/KMP.md](KMP.md)
- [Reference/Books.md](../Reference/Books.md)
