# 서픽스 배열 (Suffix Array)

- Level: Advanced
- Prerequisites: [Algorithms/Sorting.md](Sorting.md), [Algorithms/KMP.md](KMP.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

서픽스 배열은 문자열의 **모든 접미사를 사전순으로 정렬한 인덱스 배열**이다. **LCP(최장 공통 접두사) 배열**과 함께 쓰면 부분문자열 검색·서로 다른 부분문자열 수·반복 구조를 효율적으로 푼다 — 접미사 트리와 같은 표현력에 메모리는 훨씬 적다.

## 직관 (Intuition)

모든 접미사를 정렬해 두면 **어떤 부분문자열도 정렬된 접미사들의 연속 구간**으로 나타난다. 그래서 이진 탐색으로 패턴을 찾고, 이웃 접미사의 공통 접두사(LCP)를 보면 반복·중복 구조가 드러난다. "접미사를 정렬한다"는 단순한 발상이 강력한 문자열 인덱스가 된다.

## 이론 (Theory)

### 1. 구성: 접두사 배가(prefix doubling)

소박한 정렬은 비교당 $O(n)$ 이라 $O(n^2\log n)$. 대신 길이 $1,2,4,\dots,2^k$ 접두사 기준 순위(rank)를 반복 갱신한다. 길이 $2k$ 순위는 `(길이 k 자기 순위, k칸 뒤 순위)` 쌍으로 결정 → 정렬당 $O(n\log n)$, 전체 $O(n\log^2 n)$(기수 정렬이면 $O(n\log n)$). **SA-IS** 는 $O(n)$.

### 2. LCP 배열 (Kasai $O(n)$)

서픽스 배열에서 인접 접미사의 LCP. Kasai 알고리즘은 "원문 위치 순으로 보면 LCP가 1씩만 줄어든다"는 성질로 $O(n)$. **서로 다른 부분문자열 수** $=\binom{n+1}{2}-\sum_i \text{LCP}[i]$ 같은 공식이 즉시 따라온다.

### 3. 패턴 검색

패턴 $P$ 는 정렬된 접미사에서 연속 구간을 차지 → 이진 탐색 $O(m\log n)$, LCP 보강 시 $O(m+\log n)$.

## 구현 (Implementation)

```python
def suffix_array(s):                          # 접두사 배가
    s += "\x00"; n = len(s)                    # 종결 문자
    sa = sorted(range(n), key=lambda i: s[i])
    rank = [0]*n
    for i in range(1, n):
        rank[sa[i]] = rank[sa[i-1]] + (s[sa[i]] != s[sa[i-1]])
    k = 1
    while k < n:
        key = lambda i: (rank[i], rank[i+k] if i+k < n else -1)
        sa.sort(key=key)
        tmp = [0]*n
        for i in range(1, n):
            tmp[sa[i]] = tmp[sa[i-1]] + (key(sa[i]) > key(sa[i-1]))
        rank = tmp; k <<= 1
    return sa[1:]                              # 종결 문자 제외

def kasai_lcp(s, sa):                          # 인접 LCP, O(n)
    n = len(s); rank = [0]*n
    for i, p in enumerate(sa): rank[p] = i
    lcp = [0]*n; h = 0
    for i in range(n):
        if rank[i] > 0:
            j = sa[rank[i]-1]
            while i+h < n and j+h < n and s[i+h] == s[j+h]: h += 1
            lcp[rank[i]] = h
            if h: h -= 1
    return lcp
```

## 복잡도 (Complexity)

| 구성 | 시간 | 공간 |
|---|---|---|
| 접두사 배가 | $O(n\log n)$ | $O(n)$ |
| SA-IS | $O(n)$ | $O(n)$ |
| LCP(Kasai) | $O(n)$ | $O(n)$ |
| 패턴 검색 | $O(m\log n)$ | — |

**워크드 예제(`banana`).** 접미사 정렬: `a, ana, anana, banana, na, nana` → SA=`[5,3,1,0,4,2]`. LCP 인접: `a`–`ana`=1, `ana`–`anana`=3, … 최장 반복 부분문자열 = max LCP = 3(`ana`).

## 응용 (Applications)

- 부분문자열 검색·빈도, 서로 다른 부분문자열 수, 최장 반복 부분문자열.
- 최장 공통 부분문자열(여러 문자열을 구분자로 결합).
- 데이터 압축: **BWT**(bzip2)·**FM-index**(유전체 정렬 BWA/Bowtie)의 토대.

## 흔한 오해 (Common Misunderstandings)

- **서픽스 배열만으로는 부족** — LCP 배열과 함께 써야 진가.
- **소박한 정렬은 $O(n^2\log n)$** — 큰 입력엔 배가/SA-IS.
- **접미사 트리와 동등하나 메모리가 훨씬 적다**(상수·포인터 절감).
- **종결 문자($)를 붙이는 관례**가 경계 처리를 단순화한다.

## TMI

- BWT는 서픽스 배열로 계산되며 bzip2·FM-index의 핵심 — "정렬된 회전의 마지막 열".
- SA-IS(2009)는 선형 시간 구성을 비교적 짧은 코드로 달성해 표준이 됐다.
- FM-index는 압축된 상태에서 검색해, 사람 유전체(30억 염기)를 노트북 메모리에 인덱싱한다.

## 연습 / 확인 문제 (Exercises)

- `banana$` 의 서픽스 배열과 LCP 배열을 손으로 구하라.
- LCP 배열로 서로 다른 부분문자열 수를 계산하라.
- 서픽스 배열에서 패턴을 이진 탐색으로 찾는 절차를 기술하라.
- 두 문자열의 최장 공통 부분문자열을 결합 + LCP로 구하라.

## 이어서 읽기 (Reading Path)

- 이전: [Aho-Corasick](Aho-Corasick.md)
- 다음: [정수론 & 소수](Number-Theory.md)
- 관련: [정렬](Sorting.md), [KMP](KMP.md)

## 참조 (References)

- [Algorithms/Sorting.md](Sorting.md)
- [Algorithms/KMP.md](KMP.md)
- [Reference/Books.md](../Reference/Books.md)
