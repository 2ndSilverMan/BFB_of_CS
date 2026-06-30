# 아호-코라식 (Aho-Corasick)

- Level: Advanced
- Prerequisites: [Algorithms/KMP.md](KMP.md), [Data-Structures/Trie.md](../Data-Structures/Trie.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

아호-코라식은 **여러 패턴을 텍스트 한 번 훑어 모두 찾는** 다중 패턴 매칭이다. 패턴들로 [트라이](../Data-Structures/Trie.md)를 만들고, [KMP](KMP.md) 실패 함수를 일반화한 **실패 링크**를 더한다.

## 직관 (Intuition)

패턴이 여러 개일 때 각각 KMP를 돌리면 비효율적이다. 모든 패턴을 하나의 트라이로 합치고, 불일치가 나면 "지금까지 본 접미사 중 어떤 패턴의 접두사가 되는 가장 긴 곳"으로 점프한다 — 이 실패 링크가 KMP 실패 함수의 다패턴 버전이다.

## 이론 (Theory)

### 1. 세 가지 링크

1. **goto(트라이 간선)**: 패턴들로 트라이 구축.
2. **실패 링크(fail)**: 노드 $u$(문자열 $s$)의 fail은 $s$ 의 **가장 긴 진접미사이면서 트라이 노드**인 곳. BFS로 계산(부모의 fail을 따라가며).
3. **출력 링크(output)**: 한 위치에서 끝나는 모든 패턴을 모은다(fail 사슬을 따라 패턴 끝을 수집).

### 2. 오토마톤 관점

각 (상태, 문자) 전이를 미리 채우면(실패 링크를 흡수) **결정적 유한 오토마톤(DFA)** 이 되어, 텍스트를 글자당 $O(1)$ 전이로 훑는다.

## 구현 (Implementation)

```python
from collections import deque
def build_aho(patterns):
    goto = [{}]; fail = [0]; out = [[]]
    for idx, p in enumerate(patterns):            # 트라이
        cur = 0
        for ch in p:
            if ch not in goto[cur]:
                goto[cur][ch] = len(goto)
                goto.append({}); fail.append(0); out.append([])
            cur = goto[cur][ch]
        out[cur].append(idx)
    q = deque(goto[0].values())                   # 깊이 1은 fail=root
    while q:                                       # BFS로 실패 링크
        u = q.popleft()
        for ch, v in goto[u].items():
            q.append(v)
            f = fail[u]
            while f and ch not in goto[f]: f = fail[f]
            fail[v] = goto[f].get(ch, 0) if goto[f].get(ch) != v else 0
            out[v] += out[fail[v]]                 # 출력 링크 병합
    return goto, fail, out

def search(text, goto, fail, out):
    s, hits = 0, []
    for i, ch in enumerate(text):
        while s and ch not in goto[s]: s = fail[s]
        s = goto[s].get(ch, 0)
        for idx in out[s]: hits.append((i, idx))
    return hits
```

## 복잡도 (Complexity)

| | 시간 | 공간 |
|---|---|---|
| 구축 | $O(\sum|P_i|\cdot|\Sigma|)$ | $O(\sum|P_i|)$ |
| 검색 | $O(n + \text{매칭 수})$ | — |

전체 패턴 길이 합·텍스트 길이·매칭 수에 선형. **워크드 예제(`he,she,his,hers`).** 텍스트 `ushers` 처리 중 `she` 노드에서 fail이 `he` 노드를 가리켜, 출력 링크로 `she` 와 `he` 를 동시에 보고한다.

## 응용 (Applications)

- 침입 탐지·바이러스 시그니처 스캔, 금칙어·스팸 필터.
- 생물정보학 다중 모티프 검색, 검색 엔진 사전 매칭.
- `fgrep`(고정 문자열 다중 검색)의 고전 구현.

## 흔한 오해 (Common Misunderstandings)

- **실패 링크는 트라이 부모가 아니라 "가장 긴 접미사 노드"** 를 가리킨다.
- **출력 링크를 빠뜨리면** 한 위치에서 끝나는 일부 패턴(예: `she` 안의 `he`)을 놓친다.
- **단일 패턴이면 KMP로 충분** — 아호-코라식은 다패턴용.
- **알파벳이 크면 전이 테이블 메모리가 큼** — 맵 vs 배열 트레이드오프.

## TMI

- 1975년 Aho·Corasick이 도서관 문헌 검색용으로 고안 — 이 Aho가 컴파일러 "드래곤 북"의 그 Aho다.
- 실패 링크 트리는 그 자체로 "접미사 관계"를 담아 추가 질의(부분 문자열 빈도 등)에 쓰인다.
- 동적 다중 패턴(패턴 추가·삭제)이 필요하면 아호-코라식 대신 다른 구조를 쓴다(정적 구축이 전제).

## 연습 / 확인 문제 (Exercises)

- `{he, she, his, hers}` 로 트라이와 실패 링크를 그려라.
- 출력 링크가 왜 필요한지 `she` 안의 `he` 로 설명하라.
- 같은 문제를 개별 KMP로 풀 때와 비용을 비교하라.
- 전이를 미리 채워 DFA로 만들면 검색이 왜 글자당 $O(1)$ 인지 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [Rabin-Karp](Rabin-Karp.md)
- 다음: [서픽스 배열](Suffix-Array.md)
- 관련: [KMP](KMP.md), [트라이](../Data-Structures/Trie.md)

## 참조 (References)

- [Data-Structures/Trie.md](../Data-Structures/Trie.md)
- [Algorithms/KMP.md](KMP.md)
- [Reference/Books.md](../Reference/Books.md)
