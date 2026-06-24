# 최대 유량 (Max-Flow: Ford-Fulkerson / Edmonds-Karp)

- Level: Advanced
- Prerequisites: [Algorithms/BFS-DFS.md](BFS-DFS.md), [Math/Discrete/Graph-Theory.md](../Math/Discrete/Graph-Theory.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

최대 유량 문제는 용량이 있는 방향 그래프에서 출발점(source)에서 도착점(sink)으로 보낼 수 있는 최대 흐름을 구한다. Ford-Fulkerson은 증가 경로를 반복해 찾고, Edmonds-Karp는 BFS로 그 경로를 고른다.

## 직관 (Intuition)

파이프 망에서 "수도(source)에서 배수구(sink)로 물을 최대한 흘리기"가 최대 유량이다. 아직 여유 있는 경로를 찾아 흘릴 수 있는 만큼 흘리고, 잘못 보낸 흐름을 되돌릴 수 있게 "역방향 여유"를 남긴다. 더 흘릴 경로가 없으면 그때가 최대다.

## 이론 (Theory)

잔여 그래프(residual graph)에서 source→sink 증가 경로를 찾아, 그 경로의 최소 잔여 용량(bottleneck)만큼 흘린다. 역간선에 같은 양을 더해 되돌림을 허용한다.

**최대 유량 최소 컷 정리**: 최대 유량의 값 = 최소 컷(source/sink를 가르는 간선 용량 합의 최소)이다.

Ford-Fulkerson은 경로 선택을 명시 안 해 무리수 용량에서 종료가 보장되지 않을 수 있다. **Edmonds-Karp**는 BFS로 최단(간선 수) 증가 경로를 골라 `O(VE^2)`를 보장한다.

## 구현 (Implementation)

```python
from collections import deque
def edmonds_karp(cap, s, t, n):            # cap[u][v]: 잔여 용량 행렬
    flow = 0
    while True:
        parent = [-1]*n; parent[s] = s
        q = deque([s])
        while q:                            # BFS로 증가 경로 탐색
            u = q.popleft()
            for v in range(n):
                if parent[v] == -1 and cap[u][v] > 0:
                    parent[v] = u; q.append(v)
        if parent[t] == -1: break           # 더 없음 → 최대
        b, v = float('inf'), t
        while v != s: b = min(b, cap[parent[v]][v]); v = parent[v]
        v = t
        while v != s:
            cap[parent[v]][v] -= b; cap[v][parent[v]] += b   # 정/역간선 갱신
            v = parent[v]
        flow += b
    return flow
```

## 복잡도 (Complexity)

| 알고리즘 | 시간 |
|---|---|
| Ford-Fulkerson(정수 용량) | `O(E · maxflow)` |
| Edmonds-Karp | `O(VE^2)` |

Edmonds-Karp는 경로 선택을 BFS로 고정해 용량과 무관한 다항 시간을 보장한다. 더 빠른 Dinic은 별도 문서로 다룬다.

## 응용 (Applications)

- 이분 매칭, 작업 배정
- 네트워크/공급망 용량 계획
- 이미지 분할(그래프 컷), 프로젝트 선택
- 최소 컷 기반 신뢰성·분리 분석

## 흔한 오해 (Common Misunderstandings)

- 역간선(되돌림)이 없으면 탐욕적 흐름이 최적을 놓친다 — 잔여 그래프가 핵심이다.
- Ford-Fulkerson은 BFS를 안 쓰면 비효율적이거나 종료 안 될 수 있다.
- 최대 유량과 최소 컷이 같다는 것은 정리이지 자명한 사실이 아니다.
- 무방향/다중 간선·정점 용량은 변환이 필요하다.

## TMI

- 최대 유량-최소 컷 정리(1956)는 조합 최적화의 가장 아름다운 쌍대성 중 하나로 꼽힌다.
- 그래프 컷은 한때 이미지 분할의 표준이었고, 지금도 일부 비전 문제에서 쓰인다.
- 정점 용량은 정점을 둘로 쪼개 그 사이 간선에 용량을 주는 표준 트릭으로 처리한다.

## 연습 / 확인 문제 (Exercises)

- 작은 그래프에서 증가 경로를 반복해 최대 유량을 구하라.
- 같은 그래프의 최소 컷을 찾아 최대 유량과 같음을 확인하라.
- 역간선이 없을 때 답이 틀리는 예를 만들어라.

## 이어서 읽기 (Reading Path)

- 이전: [강한 연결 요소 (SCC)](SCC.md)
- 다음: [Dinic's Algorithm](Dinic.md), [이분 매칭](Bipartite-Matching.md)

## 참조 (References)

- [Algorithms/Dinic.md](Dinic.md)
- [Algorithms/Bipartite-Matching.md](Bipartite-Matching.md)
- [Reference/Books.md](../Reference/Books.md)
