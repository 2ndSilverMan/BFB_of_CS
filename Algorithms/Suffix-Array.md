# 서픽스 배열 (Suffix Array)

- Level: Advanced
- Prerequisites: [Algorithms/Sorting.md](Sorting.md), [Algorithms/KMP.md](KMP.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

서픽스 배열은 문자열의 모든 접미사를 사전순으로 정렬한 인덱스 배열이다. LCP(최장 공통 접두사) 배열과 함께 쓰면, 부분문자열 검색·서로 다른 부분문자열 수·반복 구조 등을 효율적으로 푼다. 접미사 트리보다 메모리가 적다.

## 직관 (Intuition)

문자열의 모든 접미사를 정렬해 두면, 어떤 부분문자열도 정렬된 접미사들의 연속 구간으로 나타난다. 그래서 이진 탐색으로 패턴을 찾고, 이웃한 접미사들의 공통 접두사(LCP)를 보면 반복·중복 구조가 드러난다. "접미사를 정렬한다"는 단순한 발상이 강력한 문자열 인덱스가 된다.

## 이론 (Theory)

길이 $n$ 문자열의 접미사 $n$개를 정렬한다. 소박하게는 비교당 `O(n)`이라 `O(n^2\log n)`이지만, **접두사 배가(prefix doubling)**로 길이 $2^k$ 접두사 기준 순위를 반복 갱신하면 `O(n\log^2 n)` 또는 `O(n\log n)`, SA-IS 알고리즘은 `O(n)`이다.

**LCP 배열**: 서픽스 배열에서 인접한 접미사의 LCP. **Kasai 알고리즘**으로 `O(n)`에 구한다. 서로 다른 부분문자열 수 = $\binom{n+1}{2} - \sum \text{LCP}$ 같은 공식이 즉시 따라온다.

## 구현 (Implementation)

```python
def suffix_array(s):                       # 접두사 배가, O(n log^2 n)
    n = len(s)
    sa = list(range(n))
    rank = [ord(c) for c in s]
    k = 1
    while k < n:
        key = lambda i: (rank[i], rank[i + k] if i + k < n else -1)
        sa.sort(key=key)                   # (현재 순위, k칸 뒤 순위)로 정렬
        tmp = [0]*n
        for i in range(1, n):
            tmp[sa[i]] = tmp[sa[i-1]] + (key(sa[i]) > key(sa[i-1]))
        rank = tmp
        k <<= 1
    return sa
```

## 복잡도 (Complexity)

| 구성 | 시간 | 공간 |
|---|---|---|
| 접두사 배가 | `O(n log n)` | `O(n)` |
| SA-IS | `O(n)` | `O(n)` |
| LCP(Kasai) | `O(n)` | `O(n)` |

패턴 검색은 이진 탐색으로 `O(m log n)`(또는 LCP 보강 시 `O(m + log n)`). 접미사 트리보다 상수·메모리가 작아 실무에서 선호된다.

## 응용 (Applications)

- 부분문자열 검색·빈도 계산
- 서로 다른 부분문자열 수, 최장 반복 부분문자열
- 최장 공통 부분문자열(여러 문자열 결합)
- 데이터 압축(BWT, bzip2)의 토대

## 흔한 오해 (Common Misunderstandings)

- 접미사 배열만으로는 부족하고 LCP 배열과 함께 써야 진가가 난다.
- 소박한 정렬은 `O(n^2 log n)`이라 큰 입력엔 배가/SA-IS가 필요하다.
- 접미사 트리와 동등한 표현력이지만 메모리가 훨씬 적다.
- 끝에 고유한 종결 문자($)를 붙이는 관례가 경계 처리를 단순화한다.

## TMI

- BWT(Burrows-Wheeler Transform)는 서픽스 배열로 계산되며 bzip2·FM-index의 핵심이다.
- SA-IS(2009)는 선형 시간 서픽스 배열 구성을 비교적 간단한 코드로 달성해 표준이 됐다.
- FM-index는 서픽스 배열 + BWT로 압축된 상태에서 검색하는 유전체 정렬(BWA, Bowtie)의 기반이다.

## 연습 / 확인 문제 (Exercises)

- "banana$"의 서픽스 배열과 LCP 배열을 손으로 구하라.
- LCP 배열로 서로 다른 부분문자열 수를 계산하라.
- 서픽스 배열에서 패턴을 이진 탐색으로 찾는 절차를 기술하라.

## 이어서 읽기 (Reading Path)

- 이전: [Aho-Corasick](Aho-Corasick.md)
- 다음: [정수론 & 소수](Number-Theory.md)

## 참조 (References)

- [Algorithms/Sorting.md](Sorting.md)
- [Algorithms/KMP.md](KMP.md)
- [Reference/Books.md](../Reference/Books.md)
