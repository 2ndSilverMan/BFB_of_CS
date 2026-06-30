# 최소 비용 최대 유량 (Min-Cost Max-Flow)

- Level: Advanced
- Prerequisites: [Algorithms/Max-Flow.md](Max-Flow.md), [Algorithms/Bellman-Ford.md](Bellman-Ford.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

MCMF는 최대 유량을 흘리되 **그 흐름의 총비용을 최소화**한다. 각 간선에 용량과 단위 비용이 있고, 가능한 최대 유량 중 가장 싼 흐름을 구한다(또는 목표 유량까지의 최소 비용).

## 직관 (Intuition)

최대 유량은 "얼마나 보낼 수 있나"만 본다. MCMF는 "같은 양을 가장 싸게"를 더 요구해, 증가 경로를 아무거나가 아니라 **비용 기준 최단 경로**로 골라 흘린다 — 최단 경로 + 유량의 결합.

## 이론 (Theory)

### 1. SSP(successive shortest paths)와 볼록성

매 단계 **비용 최단 증가 경로**로 흘리면, 흐름량이 늘어도 그 유량에서의 최소 비용이 유지된다. 근거: 최소 비용은 유량에 대해 **볼록**(convex)이고, 증가 경로 비용이 단조 비감소라 그리디가 최적.

### 2. 음수 역간선 → 포텐셜

흐름을 흘리면 역간선의 비용은 $-\text{cost}$ 라 음수가 생겨 단순 다익스트라를 못 쓴다. **Johnson 포텐셜** $h[v]$ 로 간선 비용을 $w'(u,v)=w+h[u]-h[v]\ge0$ 로 재가중하면 이후 **다익스트라**로 가속(첫 회는 Bellman-Ford/SPFA로 $h$ 초기화).

### 3. 할당 문제

가중 이분 매칭(작업-기계 최소 비용 배정)은 MCMF의 깔끔한 특수 경우 → 헝가리안 알고리즘과 동치.

## 구현 (Implementation)

```python
from collections import deque
INF = float("inf")
def mcmf(graph, s, t, n):                    # graph[u]=[[to,cap,cost,rev],...]
    flow = cost = 0
    while True:
        dist = [INF]*n; inq = [False]*n; pe = [None]*n
        dist[s] = 0; q = deque([s])
        while q:                              # SPFA로 비용 최단 경로
            u = q.popleft(); inq[u] = False
            for i, (v, cap, c, _) in enumerate(graph[u]):
                if cap > 0 and dist[u]+c < dist[v]:
                    dist[v] = dist[u]+c; pe[v] = (u, i)
                    if not inq[v]: inq[v] = True; q.append(v)
        if dist[t] == INF: break              # 더 못 흘림
        push = INF; v = t                     # 경로 병목
        while v != s:
            u, i = pe[v]; push = min(push, graph[u][i][1]); v = u
        v = t
        while v != s:                          # 정/역간선 갱신
            u, i = pe[v]; graph[u][i][1] -= push
            rev = graph[u][i][3]; graph[v][rev][1] += push; v = u
        flow += push; cost += push * dist[t]
    return flow, cost
```

## 복잡도 (Complexity)

| 방식 | 시간 |
|---|---|
| SPFA 기반 SSP | 대략 $O(\text{flow}\cdot VE)$ |
| Johnson 포텐셜 + 다익스트라 | $O(\text{flow}\cdot E\log V)$ |

정확한 경계는 비용·용량 분포에 의존. **워크드 예제(할당).** 2×2 비용 행렬을 $s$→좌(cap1)·우→$t$(cap1)·좌-우(cap1,cost=행렬값)로 만들면, MCMF가 최소 비용 완전 매칭을 준다.

## 응용 (Applications)

- 할당 문제(작업-기계 최소 비용), 가중 이분 매칭.
- 운송·물류 최소 비용 흐름, 일정·자원 최적화.
- 영상 분할·재구성의 비용 흐름 모델.

## 흔한 오해 (Common Misunderstandings)

- **역간선 비용은 음수($-\text{cost}$)** 라 단순 다익스트라 불가 → 포텐셜 필요.
- **"최대 유량 먼저, 비용 나중" 분리는 일반적으로 틀린다** — 동시에 최적화.
- **최소 비용은 유량마다 다르다** — "어느 유량에서의 최소 비용인지" 명시.
- **음수 비용 사이클이 있으면 정의가 달라진다**(먼저 소거).

## TMI

- 비용이 유량에 대해 볼록이라는 성질이 SSP 정당성의 핵심 — "지금 가장 싼 경로"가 미래를 망치지 않는다.
- Johnson 포텐셜은 [Bellman-Ford](Bellman-Ford.md) 재가중을 흐름 문제에 적용한 우아한 트릭.
- 헝가리안 알고리즘은 할당 문제 전용 MCMF로 $O(n^3)$ 을 보장한다.

## 연습 / 확인 문제 (Exercises)

- 작은 그래프에서 비용 최단 증가 경로를 반복해 MCMF를 구하라.
- 가중 이분 매칭을 MCMF 그래프로 변환하라.
- 역간선 비용이 왜 음수여야 하는지 설명하라.
- Johnson 포텐셜이 비용을 비음수로 만드는 과정을 보여라.

## 이어서 읽기 (Reading Path)

- 이전: [이분 매칭](Bipartite-Matching.md)
- 다음: [KMP](KMP.md)
- 관련: [벨만-포드](Bellman-Ford.md), [다익스트라](Dijkstra.md)

## 참조 (References)

- [Algorithms/Max-Flow.md](Max-Flow.md)
- [Algorithms/Bellman-Ford.md](Bellman-Ford.md)
- [Reference/Books.md](../Reference/Books.md)
