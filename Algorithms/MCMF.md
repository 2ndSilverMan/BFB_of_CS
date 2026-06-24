# 최소 비용 최대 유량 (Min-Cost Max-Flow)

- Level: Advanced
- Prerequisites: [Algorithms/Max-Flow.md](Max-Flow.md), [Algorithms/Bellman-Ford.md](Bellman-Ford.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

MCMF는 최대 유량을 흘리되 그 흐름의 총비용을 최소화하는 문제다. 각 간선에 용량과 단위 비용이 있고, 가능한 최대 유량 중 가장 싼 흐름을 구한다.

## 직관 (Intuition)

최대 유량은 "얼마나 보낼 수 있나"만 본다. MCMF는 "같은 양을 보내되 가장 싸게"를 추가로 요구한다. 그래서 증가 경로를 아무거나가 아니라 "가장 비용이 싼 경로(최단 경로, 비용 기준)"로 골라 흘린다. 비용을 가중치로 보는 최단 경로 + 유량의 결합이다.

## 이론 (Theory)

증가 경로를 비용 기준 최단 경로로 선택한다(SPFA/벨만-포드, 음의 역간선 비용 때문). 매 단계 최단 비용 경로로 흘리면, 흐름량이 늘어도 최소 비용이 유지된다(볼록성).

음의 간선 처리를 위해 **존슨의 포텐셜(Johnson potential)**을 쓰면 이후 다익스트라로 가속할 수 있다. 비용은 흐른 양 × 단위 비용의 합이고, 목표는 주어진 유량(보통 최대 유량)에서 이 합을 최소화하는 것이다.

## 구현 (Implementation)

```python
# SPFA 기반 MCMF 핵심 루프 (개념)
def min_cost_max_flow(graph, s, t, n):
    flow = cost = 0
    while True:
        dist, in_queue, prev_e = [INF]*n, [False]*n, [None]*n
        dist[s] = 0; q = deque([s])
        while q:                            # SPFA로 최소 비용 경로
            u = q.popleft(); in_queue[u] = False
            for e in graph[u]:
                if e.cap > 0 and dist[u] + e.cost < dist[e.to]:
                    dist[e.to] = dist[u] + e.cost
                    prev_e[e.to] = e
                    if not in_queue[e.to]:
                        in_queue[e.to] = True; q.append(e.to)
        if dist[t] == INF: break            # 더 흘릴 경로 없음
        push = min_along_path(prev_e, s, t)
        apply_flow(prev_e, s, t, push)
        flow += push; cost += push * dist[t]
    return flow, cost
```

## 복잡도 (Complexity)

SPFA 기반은 대략 `O(V·E·flow)` 수준으로 그래프와 유량에 따라 달라진다. 존슨 포텐셜 + 다익스트라(SSP)는 `O(flow · E log V)`로 개선된다. 정확한 경계는 간선 비용·용량 분포에 의존한다.

## 응용 (Applications)

- 할당 문제(작업-기계 최소 비용 배정)
- 운송·물류의 최소 비용 흐름
- 가중 이분 매칭
- 일정·자원 최적화

## 흔한 오해 (Common Misunderstandings)

- 역간선의 비용은 음수($-\text{cost}$)라, 단순 다익스트라를 바로 못 쓴다(포텐셜 필요).
- "최대 유량을 먼저 구하고 비용을 줄이는" 단순 분리는 일반적으로 틀린다.
- 최소 비용은 흐름량마다 다르므로 "어느 유량에서의 최소 비용인지" 분명히 해야 한다.
- 음의 비용 사이클이 있으면 문제 정의가 달라진다(소거 필요).

## TMI

- 가중 이분 매칭(할당 문제)은 MCMF의 특수 경우로 깔끔히 환원된다.
- 비용 단조 증가(증가 경로 비용이 비감소)라는 성질이 SSP 알고리즘의 정당성을 준다.
- 존슨 포텐셜은 전이 비용을 비음수로 재가중해 다익스트라를 가능케 하는 우아한 트릭이다.

## 연습 / 확인 문제 (Exercises)

- 작은 그래프에서 최소 비용 증가 경로를 반복해 MCMF를 구하라.
- 가중 이분 매칭을 MCMF 그래프로 변환하라.
- 역간선 비용이 왜 음수여야 하는지 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [이분 매칭](Bipartite-Matching.md)
- 다음: [KMP](KMP.md)

## 참조 (References)

- [Algorithms/Max-Flow.md](Max-Flow.md)
- [Algorithms/Bellman-Ford.md](Bellman-Ford.md)
- [Reference/Books.md](../Reference/Books.md)
