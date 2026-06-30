# 이분 매칭 (Bipartite Matching)

- Level: Advanced
- Prerequisites: [Algorithms/Max-Flow.md](Max-Flow.md), [Algorithms/BFS-DFS.md](BFS-DFS.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

이분 매칭은 두 그룹 $L, R$ 사이에서 **끝점을 공유하지 않는 최대 간선 집합**을 찾는다. "한 사람은 한 작업, 한 작업은 한 사람"인 배정을 모형화한다.

## 직관 (Intuition)

지원자와 일자리가 있고 각자 할 수 있는 일이 정해졌다. 최대한 많이 짝지으려면 이미 맺어진 짝을 **살짝 재배치(증가 경로)** 해 빈자리를 만든다. "내가 들어가면 밀려난 사람이 다른 자리로 갈 수 있나"를 따라가는 것이 핵심.

## 이론 (Theory)

### 1. 증가 경로 (Berge 정리)

매칭/비매칭 간선이 **번갈아 나오며 양 끝이 미매칭**인 경로가 증가 경로. 이를 뒤집으면 매칭이 1 늘어난다. **매칭이 최대 ⟺ 증가 경로가 없다**(Berge).

### 2. 쌍대성 정리들

- **쾨니그 정리**: 이분 그래프에서 **최대 매칭 = 최소 정점 덮개**. (NP-난해인 정점 덮개가 이분에선 다항.)
- **홀의 결혼 정리**: $L$ 의 완전 매칭 ⟺ 모든 $S\subseteq L$ 에 대해 $|N(S)|\ge|S|$.
- 최대 독립 집합 = $|V|$ − 최대 매칭(쾨니그의 따름).

### 3. 최대 유량 환원

$s\to L$, $R\to t$ 에 용량 1 → **최대 유량 = 최대 매칭**. [디닉](Dinic.md)을 적용하면 $O(E\sqrt V)$.

## 구현 (Implementation)

```python
def kuhn(adj, n_left, n_right):              # 증가 경로(쿤)
    match_r = [-1] * n_right
    def try_aug(u, seen):
        for v in adj[u]:
            if not seen[v]:
                seen[v] = True
                if match_r[v] == -1 or try_aug(match_r[v], seen):
                    match_r[v] = u           # 증가 경로 → 재배치
                    return True
        return False
    res = 0
    for u in range(n_left):
        if try_aug(u, [False]*n_right):
            res += 1
    return res
```

## 복잡도 (Complexity)

| 알고리즘 | 시간 |
|---|---|
| 쿤(증가 경로) | $O(VE)$ |
| Hopcroft-Karp | $O(E\sqrt V)$ |
| 일반 그래프(Blossom) | $O(V^3)$ |

**워크드 예제.** $L=\{a,b\}, R=\{1,2\}$, `a-1, a-2, b-1`: a→1 매칭. b→1 시도, 1은 a가 점유 → a의 대안 2로 재배치(증가 경로 b-1-a-2) → 매칭 `{b-1, a-2}` 크기 2.

## 응용 (Applications)

- 작업·자원 배정, 시간표·시프트 스케줄링.
- 네트워크 스위치 스케줄링, 특징점 대응.
- 최소 정점 덮개·최대 독립 집합(이분), DAG 최소 경로 덮개.

## 흔한 오해 (Common Misunderstandings)

- **탐욕 매칭은 최적이 아니다** — 증가 경로 재배치 필요.
- **일반(비이분) 그래프 매칭은 훨씬 어렵다** — Edmonds Blossom 필요.
- **최대 매칭은 유일하지 않을 수 있다**.
- **가중치가 있으면 단순 매칭이 아니라 할당 문제**(헝가리안/[MCMF](MCMF.md)).

## TMI

- 일반 그래프 매칭이 다항 시간임을 처음 보인 Edmonds의 Blossom(1965)은 "다항 시간 = 효율적"이라는 정의를 대중화한 역사적 논문이다.
- 쾨니그 정리는 이분에서 정점 덮개(일반적으로 NP-난해)가 다항이 되는 드문 사례다.
- Hopcroft-Karp는 한 phase에 **서로소 최단 증가 경로를 동시에** 늘려 $\sqrt V$ phase로 끝낸다(디닉의 단위 용량 특수화).

## 연습 / 확인 문제 (Exercises)

- 작은 이분 그래프에서 증가 경로로 최대 매칭을 구하라.
- 최대 매칭 = 최소 정점 덮개를 한 예로 확인하라(쾨니그).
- 매칭을 최대 유량으로 환원하는 그래프를 그려라.
- 홀의 조건이 깨지는 그래프를 만들어 완전 매칭이 없음을 보여라.

## 이어서 읽기 (Reading Path)

- 이전: [Dinic's Algorithm](Dinic.md)
- 다음: [최소 비용 최대 유량 (MCMF)](MCMF.md)
- 관련: [최대 유량](Max-Flow.md)

## 참조 (References)

- [Algorithms/Max-Flow.md](Max-Flow.md)
- [Algorithms/Dinic.md](Dinic.md)
- [Reference/Books.md](../Reference/Books.md)
