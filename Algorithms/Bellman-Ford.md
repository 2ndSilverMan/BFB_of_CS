# 벨만-포드 (Bellman-Ford)

- Level: Intermediate
- Prerequisites: [Algorithms/Dijkstra.md](Dijkstra.md), [Math/Discrete/Graph-Theory.md](../Math/Discrete/Graph-Theory.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

벨만-포드는 음의 가중치 간선이 있는 그래프에서도 단일 출발점 최단 경로를 구하는 알고리즘이다. 모든 간선을 반복적으로 완화(relax)하며, 음의 사이클 존재 여부도 탐지한다.

## 직관 (Intuition)

다익스트라는 "한 번 확정한 거리는 다시 줄지 않는다"는 가정에 기대 음의 간선에서 무너진다. 벨만-포드는 그런 가정 없이 "모든 간선을 충분히 여러 번 완화하면 최단 거리가 안정된다"는 무식하지만 견고한 전략을 쓴다. 최단 경로는 간선을 최대 $V-1$개 지나므로 $V-1$번 전체 완화면 충분하다.

## 이론 (Theory)

거리 $d[s]=0$, 나머지 $\infty$로 시작. 완화 연산은

$$d[v]\leftarrow \min(d[v],\ d[u]+w(u,v))$$

모든 간선에 대해 이 완화를 $V-1$번 반복하면 최단 거리가 확정된다(최단 경로의 간선 수 ≤ $V-1$). $V$번째 반복에서도 완화가 일어나면 출발점에서 도달 가능한 **음의 사이클**이 존재한다는 뜻이다. SPFA는 큐로 완화 대상을 관리하는 실용적 개선이다.

## 구현 (Implementation)

```python
def bellman_ford(n, edges, src):
    dist = [float('inf')] * n
    dist[src] = 0
    for _ in range(n - 1):                 # V-1번 반복
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w      # 완화
    for u, v, w in edges:                  # 한 번 더 → 음의 사이클 탐지
        if dist[u] + w < dist[v]:
            return None                    # 음의 사이클 존재
    return dist
```

## 복잡도 (Complexity)

| | 시간 | 공간 |
|---|---|---|
| 일반 | `O(VE)` | `O(V)` |

정점 $V$, 간선 $E$. 다익스트라(`O(E log V)`)보다 느리지만 음의 간선을 다룰 수 있다. 밀집 그래프에서는 $E\approx V^2$이라 `O(V^3)`에 이른다.

## 응용 (Applications)

- 음의 가중치가 있는 최단 경로(환율 차익 거래 탐지 등)
- 음의 사이클 탐지
- 거리 벡터 라우팅 프로토콜(RIP)의 기반
- 차이 제약 시스템(difference constraints) 풀이

## 흔한 오해 (Common Misunderstandings)

- 음의 사이클이 있으면 "최단 경로"가 정의되지 않는다(무한히 줄어듦) — 벨만-포드는 이를 탐지만 한다.
- $V-1$번이 아니라 더 적게 반복해도 일찍 수렴할 수 있다(변화 없으면 조기 종료).
- 음의 간선이 있어도 음의 사이클이 없으면 최단 경로는 잘 정의된다.
- 다익스트라에 음의 간선을 넣어 "고치는" 단순 트릭은 일반적으로 틀린다.

## TMI

- 환율 그래프에 로그를 취하면 차익 거래 탐지가 음의 사이클 탐지로 환원된다.
- SPFA(Shortest Path Faster Algorithm)는 평균적으로 빠르지만 최악엔 여전히 `O(VE)`다.
- 거리 벡터 라우팅의 "count to infinity" 문제는 분산 환경의 벨만-포드가 겪는 고전적 난점이다.

## 연습 / 확인 문제 (Exercises)

- 음의 간선이 있는 작은 그래프에서 $V-1$번 완화를 손으로 수행하라.
- 음의 사이클을 만든 뒤 $V$번째 완화에서 탐지됨을 확인하라.
- 다익스트라가 음의 간선에서 틀리는 반례를 만들어라.

## 이어서 읽기 (Reading Path)

- 이전: [최단 경로 — Dijkstra](Dijkstra.md)
- 다음: [최단 경로 — Floyd-Warshall](Floyd-Warshall.md)

## 참조 (References)

- [Algorithms/Dijkstra.md](Dijkstra.md)
- [Algorithms/Floyd-Warshall.md](Floyd-Warshall.md)
- [Reference/Books.md](../Reference/Books.md)
