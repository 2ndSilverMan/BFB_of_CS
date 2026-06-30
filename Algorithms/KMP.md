# KMP (Knuth-Morris-Pratt)

- Level: Intermediate
- Prerequisites: [Programming/Arrays-and-Strings.md](../Programming/Arrays-and-Strings.md), [Algorithms/Complexity.md](Complexity.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

KMP는 텍스트에서 패턴을 **$O(n+m)$** 에 찾는다. 패턴의 **접두사-접미사(border) 정보**(실패 함수)를 미리 계산해, 불일치 시 텍스트를 되감지 않고 패턴만 똑똑하게 미끄러뜨린다.

## 직관 (Intuition)

소박한 매칭은 불일치 시 텍스트 포인터를 한 칸 물려 처음부터 다시 본다 — 이미 맞춘 정보를 버린다. KMP는 "지금까지 맞은 접두사의 *접미사 일부가 다시 패턴의 접두사*"라는 사실을 이용해, **텍스트는 절대 되감지 않고** 패턴만 적절히 점프시킨다.

## 이론 (Theory)

### 1. 실패 함수 (LPS / border)

$\pi[i]$ = $P[0..i]$ 에서 **자기 자신을 제외한, 접두사이자 접미사인 최대 길이**(longest proper border). 불일치가 $P[j]$ 에서 나면 $j\leftarrow\pi[j-1]$ 로 점프 — "더 짧은 일치 접두사"로 후퇴.

### 2. 선형성 증명 (amortized)

텍스트 인덱스 $i$ 는 **단조 증가**(절대 후퇴 안 함). 패턴 인덱스 $j$ 는 일치할 때 +1, 불일치 때 $\pi$ 로 감소. $j$ 의 총 증가량이 $\le n$ 이라 총 감소량도 $\le n$ → 전체 비교 $O(n)$. 전처리도 같은 논리로 $O(m)$.

### 3. border와 주기

문자열의 **최소 주기**는 $n-\pi[n-1]$. 실패 함수는 모든 border를 $\pi[n-1],\pi[\pi[n-1]-1],\dots$ 사슬로 준다. KMP는 결정적 유한 오토마톤(DFA)으로도 볼 수 있다.

## 구현 (Implementation)

```python
def build_lps(p):
    lps, k = [0]*len(p), 0
    for i in range(1, len(p)):
        while k and p[i] != p[k]:
            k = lps[k-1]               # 불일치 → border 사슬로 점프
        if p[i] == p[k]: k += 1
        lps[i] = k
    return lps

def kmp_search(text, p):
    lps, k, res = build_lps(p), 0, []
    for i, ch in enumerate(text):
        while k and ch != p[k]:
            k = lps[k-1]
        if ch == p[k]: k += 1
        if k == len(p):
            res.append(i - k + 1)      # 매칭 위치
            k = lps[k-1]               # 다음 매칭 위해 점프
    return res
```

## 복잡도 (Complexity)

| | 시간 | 공간 |
|---|---|---|
| 전처리(LPS) | $O(m)$ | $O(m)$ |
| 검색 | $O(n)$ | — |

소박한 매칭의 최악 $O(nm)$ 을 $O(n+m)$ 으로. **워크드 예제(`ababaca`).** $\pi$: a=0, ab=0, aba=1, abab=2, ababa=3, ababac=0, ababaca=1. `ababa` 에서 불일치 시 $j=3$ 로 점프 → 이미 맞은 `aba` 를 재활용.

## 응용 (Applications)

- 텍스트 검색·grep류, 부분 문자열 포함·반복 주기 탐지.
- DNA 서열 매칭, 스트리밍 온라인 매칭(텍스트 되감기 불필요).
- [Aho–Corasick](Aho-Corasick.md)(실패 링크)의 토대.

## 흔한 오해 (Common Misunderstandings)

- **실패 함수는 "다음에 볼 문자"가 아니라 "접두사=접미사 최대 길이"**.
- **여러 패턴 동시 검색엔 부적합** — 그건 Aho–Corasick.
- **평균은 소박한 매칭도 빠를 수 있다** — 최악 보장이 KMP의 가치.
- **텍스트 포인터가 절대 후퇴 안 함**이 선형성의 열쇠.

## TMI

- 1977년 Knuth·Morris·Pratt 세 사람. Morris와 Pratt가 독립 발견한 것을 Knuth가 이론으로 정리했다.
- 최소 주기 $n-\pi[n-1]$ 한 줄로 "문자열이 어떤 짧은 패턴의 반복인가"를 즉시 안다.
- 실패 함수 아이디어가 Aho–Corasick의 실패 링크, Z 함수로 자연스럽게 확장된다.

## 연습 / 확인 문제 (Exercises)

- `ababaca` 의 실패 함수를 손으로 계산하라.
- KMP로 최소 반복 주기를 구하는 방법을 보여라($n-\pi[n-1]$).
- 소박한 매칭이 $O(nm)$ 이 되는 텍스트/패턴(예: `aaa...ab` 검색)을 만들어라.
- KMP를 DFA로 변환해 상태 전이표를 그려라.

## 이어서 읽기 (Reading Path)

- 이전: [최소 비용 최대 유량 (MCMF)](MCMF.md)
- 다음: [Z 알고리즘](Z-Algorithm.md)
- 관련: [Aho–Corasick](Aho-Corasick.md), [트라이](../Data-Structures/Trie.md)

## 참조 (References)

- [Programming/Arrays-and-Strings.md](../Programming/Arrays-and-Strings.md)
- [Algorithms/Z-Algorithm.md](Z-Algorithm.md)
- [Reference/Books.md](../Reference/Books.md)
