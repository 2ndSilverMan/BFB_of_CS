# 최대 유량 (Max-Flow: Ford-Fulkerson / Edmonds-Karp)

- Level: Advanced
- Prerequisites: [Algorithms/BFS-DFS.md](BFS-DFS.md), [Math/Discrete/Graph-Theory.md](../Math/Discrete/Graph-Theory.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

최대 유량은 용량이 있는 방향 그래프에서 source $s$ 에서 sink $t$ 로 보낼 수 있는 **최대 흐름**을 구한다. Ford-Fulkerson은 증가 경로를 반복해 찾고, Edmonds-Karp는 그 경로를 BFS로 골라 다항 시간을 보장한다.

## 직관 (Intuition)

파이프 망에서 수도($s$)→배수구($t$)로 물을 최대한 흘리기. 여유 있는 경로로 흘릴 수 있는 만큼 흘리되, **잘못 보낸 흐름을 되돌릴 "역방향 여유"** 를 남긴다. 더 흘릴 경로가 없으면 그때가 최대 — 그리고 그 값은 **최소 컷**과 정확히 같다.

## 이론 (Theory)

### 1. 잔여 그래프와 증가 경로

각 간선의 잔여 용량 = 용량 − 현재 흐름. **잔여 그래프**에서 $s\to t$ 경로(증가 경로)를 찾아 그 경로의 **최소 잔여 용량(bottleneck)** 만큼 흘리고, 역간선에 같은 양을 더해 되돌림을 허용한다. **역간선이 핵심** — 없으면 그리디가 최적을 놓친다.

### 2. 최대 유량 최소 컷 정리

다음 세 명제가 **동치**다: ① 흐름 $f$ 가 최대 ② 잔여 그래프에 증가 경로 없음 ③ $|f|$ = 어떤 컷의 용량. 따라서

$$\max\text{-flow} = \min\text{-cut}$$

(증명 스케치: ②면 $s$ 에서 잔여로 도달 가능한 집합 $S$ 가 컷을 이루고, 그 컷을 가로지르는 간선은 포화·역간선은 0 → $|f|=$ 컷 용량.)

### 3. 종료와 복잡도

Ford-Fulkerson은 경로 선택을 안 정해 **무리수 용량에서 종료 안 될 수 있다**. **Edmonds-Karp**는 BFS로 최단(간선 수) 증가 경로를 골라, "각 간선이 critical이 되는 횟수 $O(V)$ × 간선 $E$ × BFS $O(E)$" 로 **$O(VE^2)$** 를 보장한다(증가 경로 길이가 단조 비감소라는 보조정리).

### 4. 환원(reduction)

| 문제 | 변환 |
|---|---|
| 이분 매칭 | 단위 용량, $s$→좌, 우→$t$ |
| 정점 용량 | 정점을 둘로 쪼개 사이 간선에 용량 |
| 무방향 간선 | 양방향 간선 두 개 |
| 다중 source/sink | 슈퍼 source/sink |

**정수성 정리**: 용량이 정수면 최대 유량도 정수해를 가진다.

## 구현 (Implementation)

```python
from collections import deque
def edmonds_karp(cap, s, t, n):            # cap[u][v]: 잔여 용량 행렬
    flow = 0
    while True:
        parent = [-1]*n; parent[s] = s
        q = deque([s])
        while q:                            # BFS 최단 증가 경로
            u = q.popleft()
            for v in range(n):
                if parent[v] == -1 and cap[u][v] > 0:
                    parent[v] = u; q.append(v)
        if parent[t] == -1: break           # 증가 경로 없음 → 최대
        b, v = float("inf"), t
        while v != s: b = min(b, cap[parent[v]][v]); v = parent[v]
        v = t
        while v != s:
            cap[parent[v]][v] -= b; cap[v][parent[v]] += b   # 정/역 간선
            v = parent[v]
        flow += b
    return flow
```

## 복잡도 (Complexity)

| 알고리즘 | 시간 |
|---|---|
| Ford-Fulkerson(정수) | $O(E\cdot\text{maxflow})$ |
| Edmonds-Karp | $O(VE^2)$ |
| [Dinic](Dinic.md) | $O(V^2 E)$ (단위 용량 $O(E\sqrt V)$) |

**워크드 예제.** `s→a(3), s→b(2), a→b(1), a→t(2), b→t(3)`: 증가 경로 `s-a-t`(2), `s-b-t`(2), `s-a-b-t`(1) → 최대 5. 최소 컷 $\{s\}$ vs 나머지 = $3+2=5$ 로 일치.

## 응용 (Applications)

- **이분 매칭**·작업 배정, 네트워크/공급망 용량 계획.
- 이미지 분할(그래프 컷), 프로젝트 선택(최대 가중 닫힘).
- 최소 컷 기반 신뢰성·분리 분석, 야구 우승 가능성 등.

## 흔한 오해 (Common Misunderstandings)

- **역간선이 없으면** 그리디 흐름이 최적을 놓친다 — 잔여 그래프가 핵심.
- **Ford-Fulkerson은 BFS 없이는** 비효율/비종료 가능.
- **max-flow = min-cut은 정리**이지 자명하지 않다.
- **무방향/정점 용량/다중 source는 변환**이 필요하다.

## TMI

- 최대 유량-최소 컷 정리(1956, Ford·Fulkerson)는 LP 쌍대성의 아름다운 조합론적 사례다.
- 그래프 컷은 한때 이미지 분할의 표준(GrabCut)이었고 지금도 일부 비전에 쓰인다.
- 현대 최강은 push-relabel·Dinic 계열이며, 2022년 거의 선형 시간 최대 유량 알고리즘이 발표돼 화제였다.

## 연습 / 확인 문제 (Exercises)

- 작은 그래프에서 증가 경로를 반복해 최대 유량을 구하라.
- 같은 그래프의 최소 컷을 찾아 최대 유량과 같음을 확인하라.
- 역간선이 없을 때 답이 틀리는 예를 만들어라.
- 이분 매칭을 최대 유량으로 환원해 풀어라.

## 이어서 읽기 (Reading Path)

- 이전: [강한 연결 요소 (SCC)](SCC.md)
- 다음: [Dinic's Algorithm](Dinic.md)
- 관련: [이분 매칭](Bipartite-Matching.md)

## 참조 (References)

- [Algorithms/Dinic.md](Dinic.md)
- [Algorithms/Bipartite-Matching.md](Bipartite-Matching.md)
- [Math/Discrete/Graph-Theory.md](../Math/Discrete/Graph-Theory.md)
- [Reference/Books.md](../Reference/Books.md)
