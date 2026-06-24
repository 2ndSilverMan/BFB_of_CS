# 디닉 알고리즘 (Dinic's Algorithm)

- Level: Advanced
- Prerequisites: [Algorithms/Max-Flow.md](Max-Flow.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

디닉 알고리즘은 최대 유량을 더 빠르게 구하는 방법이다. BFS로 레벨 그래프를 만들고, DFS로 그 위에서 여러 증가 경로(blocking flow)를 한꺼번에 흘려, Edmonds-Karp보다 훨씬 효율적이다.

## 직관 (Intuition)

Edmonds-Karp는 증가 경로를 하나씩 찾는다. 디닉은 "source로부터의 거리(레벨)"를 매긴 뒤, 거리가 정확히 1씩 증가하는 방향으로만 흘리는 레벨 그래프에서 막힘 흐름(더 못 흘릴 때까지)을 한 번에 밀어낸다. 이 단계(phase)를 반복하면 거리 상한이 빠르게 늘어 적은 단계로 끝난다.

## 이론 (Theory)

각 phase:
1. **BFS**로 잔여 그래프의 레벨(거리)을 계산. sink에 도달 못 하면 종료(최대 유량).
2. **DFS**로 레벨이 1씩 증가하는 간선만 따라 blocking flow를 흘린다. 막힌 간선은 포인터로 건너뛴다(current-arc 최적화).

phase 수는 `O(V)`이고, 각 phase의 blocking flow는 `O(VE)`다. 단위 용량 그래프(이분 매칭 등)에서는 `O(E√V)`로 더 빠르다.

## 구현 (Implementation)

```python
# 핵심 구조 (개념): 레벨 BFS + 막힘 흐름 DFS
def dinic(graph, s, t, n):
    def bfs():
        level[:] = [-1]*n; level[s] = 0
        q = deque([s])
        while q:
            u = q.popleft()
            for e in graph[u]:
                if level[e.to] < 0 and e.cap > 0:
                    level[e.to] = level[u] + 1; q.append(e.to)
        return level[t] >= 0
    def dfs(u, pushed):
        if u == t: return pushed
        while it[u] < len(graph[u]):
            e = graph[u][it[u]]
            if e.cap > 0 and level[e.to] == level[u] + 1:
                d = dfs(e.to, min(pushed, e.cap))
                if d > 0:
                    e.cap -= d; e.rev.cap += d
                    return d
            it[u] += 1                      # current-arc: 막힌 간선 건너뜀
        return 0
    flow = 0
    while bfs():
        it[:] = [0]*n
        while (f := dfs(s, float('inf'))) > 0:
            flow += f
    return flow
```

## 복잡도 (Complexity)

| 그래프 | 시간 |
|---|---|
| 일반 | `O(V^2 E)` |
| 단위 용량(이분 매칭) | `O(E√V)` |

일반적으로 Edmonds-Karp의 `O(VE^2)`보다 훨씬 빠르며, 실전 최대 유량의 표준 선택이다.

## 응용 (Applications)

- 대규모 최대 유량/최소 컷
- 이분 매칭(Hopcroft-Karp와 동일한 `O(E√V)`)
- 프로젝트 선택·밀집 부분그래프
- 스케줄링·할당의 흐름 모델

## 흔한 오해 (Common Misunderstandings)

- 레벨 그래프 없이 단순 DFS만 하면 Edmonds-Karp만큼도 보장 못 한다.
- current-arc 최적화를 빠뜨리면 각 phase가 느려져 복잡도가 무너진다.
- 디닉이 항상 `O(V^2E)`로 도는 것은 아니며 특수 그래프에서 더 빠르다.
- blocking flow는 "최대 유량"이 아니라 "그 레벨 그래프에서 더 못 흘리는 흐름"이다.

## TMI

- 디닉(1970)은 학생 시절 이 알고리즘을 고안했고, 냉전기 동·서방에서 한동안 독립적으로 발전했다.
- 이분 매칭에서 디닉은 Hopcroft-Karp와 같은 `O(E√V)` 경계를 달성한다.
- 스케일링(scaling) 기법을 더하면 용량이 큰 그래프에서 더 개선된다.

## 연습 / 확인 문제 (Exercises)

- 레벨 그래프를 BFS로 만드는 과정을 작은 예에서 보여라.
- current-arc 최적화가 왜 필요한지 설명하라.
- 단위 용량 그래프에서 phase 수가 `O(√V)`인 직관을 논하라.

## 이어서 읽기 (Reading Path)

- 이전: [최대 유량](Max-Flow.md)
- 다음: [이분 매칭](Bipartite-Matching.md), [최소 비용 최대 유량 (MCMF)](MCMF.md)

## 참조 (References)

- [Algorithms/Max-Flow.md](Max-Flow.md)
- [Algorithms/Bipartite-Matching.md](Bipartite-Matching.md)
- [Reference/Books.md](../Reference/Books.md)
