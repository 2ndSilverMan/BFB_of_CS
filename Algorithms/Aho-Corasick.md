# 아호-코라식 (Aho-Corasick)

- Level: Advanced
- Prerequisites: [Algorithms/KMP.md](KMP.md), [Data-Structures/Trie.md](../Data-Structures/Trie.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

아호-코라식은 여러 패턴을 텍스트에서 한 번에 찾는 다중 패턴 매칭 알고리즘이다. 패턴들로 트라이를 만들고, KMP의 실패 함수를 일반화한 실패 링크를 더해, 텍스트를 한 번 훑으며 모든 패턴의 등장을 찾는다.

## 직관 (Intuition)

패턴이 여러 개일 때 각각 KMP를 돌리면 비효율적이다. 아호-코라식은 모든 패턴을 하나의 트라이로 합치고, 불일치가 나면 "지금까지 본 접미사 중 어떤 패턴의 접두사가 되는 가장 긴 곳"으로 점프한다. 이 점프(실패 링크)가 KMP 실패 함수의 다패턴 버전이다.

## 이론 (Theory)

1. 모든 패턴으로 **트라이** 구축.
2. BFS로 **실패 링크** 계산: 노드 $u$(문자열 $s$에 대응)의 실패 링크는 $s$의 가장 긴 진접미사이면서 트라이의 어떤 노드인 곳을 가리킨다.
3. **출력 링크**로 한 위치에서 끝나는 모든 패턴을 모은다.

텍스트를 한 글자씩 따라가며, 간선이 없으면 실패 링크로 이동한다. 자동자(automaton)로 보면 각 문자에 대한 전이가 미리 정해진 결정적 유한 오토마톤이다.

## 구현 (Implementation)

```python
from collections import deque
def build_aho(patterns):
    goto = [{}]; fail = [0]; out = [[]]
    for idx, p in enumerate(patterns):          # 트라이 구축
        cur = 0
        for ch in p:
            if ch not in goto[cur]:
                goto[cur][ch] = len(goto)
                goto.append({}); fail.append(0); out.append([])
            cur = goto[cur][ch]
        out[cur].append(idx)
    q = deque()
    for ch, nxt in goto[0].items():
        q.append(nxt)
    while q:                                     # BFS로 실패 링크
        u = q.popleft()
        for ch, v in goto[u].items():
            q.append(v)
            f = fail[u]
            while f and ch not in goto[f]: f = fail[f]
            fail[v] = goto[f].get(ch, 0) if f or ch in goto[0] else 0
            out[v] += out[fail[v]]               # 출력 링크 병합
    return goto, fail, out
```

## 복잡도 (Complexity)

| | 시간 | 공간 |
|---|---|---|
| 구축 | `O(Σ|패턴|·Σ알파벳)` | `O(Σ|패턴|)` |
| 검색 | `O(n + 매칭 수)` | — |

전체 패턴 길이 합과 텍스트 길이, 그리고 발견된 매칭 수에 선형이다. 패턴이 많을수록 개별 매칭 대비 이득이 크다.

## 응용 (Applications)

- 침입 탐지·바이러스 시그니처 스캔
- 금칙어·스팸 필터링
- 생물정보학의 다중 모티프 검색
- 검색 엔진의 사전 매칭

## 흔한 오해 (Common Misunderstandings)

- 실패 링크는 트라이의 부모가 아니라 "가장 긴 접미사 노드"를 가리킨다.
- 출력 링크를 빠뜨리면 한 위치에서 끝나는 일부 패턴을 놓친다.
- 단일 패턴이면 KMP로 충분하다 — 아호-코라식은 다패턴용이다.
- 알파벳이 크면 전이 테이블 메모리가 커진다(맵 vs 배열 트레이드오프).

## TMI

- 1975년 Aho와 Corasick이 도서관 문헌 검색을 위해 고안했다(이 Aho가 바로 컴파일러 "드래곤 북"의 그 Aho).
- `fgrep`(고정 문자열 다중 검색)의 고전적 구현이 이 알고리즘에 기반했다.
- 실패 링크 트리는 그 자체로 접미사 관계를 담아 추가 질의에 활용된다.

## 연습 / 확인 문제 (Exercises)

- {"he","she","his","hers"}로 트라이와 실패 링크를 그려라.
- 출력 링크가 왜 필요한지 "she"와 "he"로 설명하라.
- 같은 문제를 개별 KMP로 풀 때와 비용을 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [Rabin-Karp](Rabin-Karp.md)
- 다음: [서픽스 배열](Suffix-Array.md)

## 참조 (References)

- [Data-Structures/Trie.md](../Data-Structures/Trie.md)
- [Algorithms/KMP.md](KMP.md)
- [Reference/Books.md](../Reference/Books.md)
