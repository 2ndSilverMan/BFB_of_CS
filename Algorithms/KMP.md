# KMP (Knuth-Morris-Pratt)

- Level: Intermediate
- Prerequisites: [Programming/Arrays-and-Strings.md](../Programming/Arrays-and-Strings.md), [Algorithms/Complexity.md](Complexity.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

KMP는 텍스트에서 패턴을 선형 시간에 찾는 문자열 매칭 알고리즘이다. 패턴의 접두사-접미사 정보(실패 함수)를 미리 계산해, 불일치 시 패턴을 처음부터 다시 비교하지 않고 똑똑하게 건너뛴다.

## 직관 (Intuition)

소박한 매칭은 불일치가 나면 텍스트 포인터를 한 칸 물려 처음부터 다시 본다. 하지만 이미 일치했던 부분에는 정보가 있다. "지금까지 맞은 접두사의 일부가 다시 접두사가 될 수 있다"는 점을 이용하면, 텍스트는 되돌리지 않고 패턴만 적절히 미끄러뜨리면 된다.

## 이론 (Theory)

**실패 함수(LPS, longest proper prefix-suffix)** $\pi[i]$ = 패턴 $P[0..i]$에서 자기 자신을 제외한, 접두사이자 접미사인 최대 길이. 불일치가 $P[j]$에서 나면 $j\leftarrow \pi[j-1]$로 점프해 재비교한다.

매칭 중 텍스트 인덱스는 절대 뒤로 가지 않으며, 패턴 인덱스만 실패 함수를 따라 줄어든다. 전처리(LPS 계산)도 같은 원리로 `O(m)`이다.

## 구현 (Implementation)

```python
def build_lps(p):
    lps = [0]*len(p); k = 0
    for i in range(1, len(p)):
        while k and p[i] != p[k]:
            k = lps[k-1]                  # 실패 시 점프
        if p[i] == p[k]: k += 1
        lps[i] = k
    return lps

def kmp_search(text, p):
    lps = build_lps(p); k = 0; res = []
    for i, ch in enumerate(text):
        while k and ch != p[k]:
            k = lps[k-1]
        if ch == p[k]: k += 1
        if k == len(p):
            res.append(i - k + 1); k = lps[k-1]
    return res
```

## 복잡도 (Complexity)

| | 시간 | 공간 |
|---|---|---|
| 전처리 | `O(m)` | `O(m)` |
| 검색 | `O(n)` | — |

길이 $n$ 텍스트, $m$ 패턴에서 전체 `O(n+m)`. 소박한 매칭의 최악 `O(nm)`을 선형으로 줄인다.

## 응용 (Applications)

- 텍스트 검색·grep류 도구
- 부분 문자열 포함·반복 주기 탐지
- DNA 서열 패턴 매칭
- 스트리밍 입력의 온라인 매칭(텍스트 되감기 불필요)

## 흔한 오해 (Common Misunderstandings)

- 실패 함수는 "다음에 볼 문자"가 아니라 "접두사이자 접미사인 최대 길이"다.
- KMP는 여러 패턴 동시 검색엔 부적합하다(그건 Aho-Corasick).
- 평균적으로는 단순 매칭도 빠를 수 있으나, 최악 보장은 KMP가 우월하다.
- 텍스트 포인터가 절대 뒤로 가지 않는다는 점이 선형성의 열쇠다.

## TMI

- KMP는 1977년 Knuth, Morris, Pratt 세 사람의 이름에서 왔다.
- 문자열의 최소 주기는 $n-\pi[n-1]$로 실패 함수에서 바로 얻을 수 있다.
- 실패 함수 아이디어는 Aho-Corasick의 실패 링크로 자연스럽게 확장된다.

## 연습 / 확인 문제 (Exercises)

- "ababaca"의 실패 함수를 손으로 계산하라.
- KMP로 문자열의 최소 반복 주기를 구하는 방법을 설명하라.
- 소박한 매칭이 `O(nm)`이 되는 텍스트/패턴 예를 만들어라.

## 이어서 읽기 (Reading Path)

- 이전: [최소 비용 최대 유량 (MCMF)](MCMF.md)
- 다음: [Z 알고리즘](Z-Algorithm.md), [Aho-Corasick](Aho-Corasick.md)

## 참조 (References)

- [Programming/Arrays-and-Strings.md](../Programming/Arrays-and-Strings.md)
- [Algorithms/Z-Algorithm.md](Z-Algorithm.md)
- [Reference/Books.md](../Reference/Books.md)
