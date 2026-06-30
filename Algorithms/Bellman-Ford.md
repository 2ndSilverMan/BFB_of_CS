# 벨만-포드 (Bellman-Ford)

- Level: Intermediate
- Prerequisites: [Algorithms/Dijkstra.md](Dijkstra.md), [Math/Discrete/Graph-Theory.md](../Math/Discrete/Graph-Theory.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

벨만-포드는 **음수 간선이 있어도** 단일 출발점 최단 경로를 구하고, 출발점에서 도달 가능한 **음수 사이클을 탐지**한다. [다익스트라](Dijkstra.md)의 그리디 가정을 버리고 "모든 간선을 충분히 완화"하는 DP다.

## 직관 (Intuition)

다익스트라는 "확정한 거리는 다시 안 준다"는 가정에 기대 음수 간선에서 무너진다. 벨만-포드는 그 가정 없이 **"모든 간선을 $V-1$ 번 완화하면 안정된다"** 는 무식하지만 견고한 전략을 쓴다. 근거: 최단 경로는 간선을 최대 $V-1$ 개 지난다(사이클 없으니).

## 이론 (Theory)

### 1. 완화와 $V-1$ 회의 증명

$d[s]=0$, 나머지 ∞. 완화 $d[v]\leftarrow\min(d[v],\,d[u]+w(u,v))$ 를 **모든 간선에** $V-1$ 번 반복.

**귀납**: "$i$ 번째 라운드 후, 간선 $\le i$ 개인 최단 경로의 거리가 확정"됨을 보인다. 최단 경로 간선 수 $\le V-1$ 이므로 $V-1$ 라운드면 전부 확정.

### 2. 음수 사이클 탐지와 추출

$V$ 번째 라운드에서도 완화가 일어나면 → 도달 가능한 **음수 사이클** 존재("최단"이 −∞로 발산). 어떤 정점이 그때 완화되면, `prev` 를 $V$ 번 거슬러 올라가면 사이클 위 정점에 도달 → 사이클을 **추출**할 수 있다.

### 3. 변형과 응용 구조

- **조기 종료**: 한 라운드에 완화가 없으면 즉시 종료.
- **SPFA**: 완화된 정점만 큐로 관리(평균 빠름, 최악 여전히 $O(VE)$).
- **차이 제약(difference constraints)** $x_j-x_i\le w$ 를 간선으로 보면 BF로 해 존재/해를 구한다.
- **환율 차익(arbitrage)**: 환율에 $-\log$ 를 취하면 차익 = 음수 사이클.

## 구현 (Implementation)

```python
def bellman_ford(n, edges, src):          # edges: (u, v, w)
    dist = [float("inf")] * n
    dist[src] = 0
    for i in range(n - 1):                # V-1 라운드
        changed = False
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w; changed = True
        if not changed:                   # 조기 종료
            break
    for u, v, w in edges:                 # 한 번 더 완화되면 음수 사이클
        if dist[u] + w < dist[v]:
            return None
    return dist
```

## 복잡도 (Complexity)

| | 시간 | 공간 |
|---|---|---|
| 일반 | $O(VE)$ | $O(V)$ |
| 밀집($E\approx V^2$) | $O(V^3)$ | $O(V)$ |

[다익스트라](Dijkstra.md)($O(E\log V)$)보다 느리지만 음수 간선을 다룬다. **워크드 예제.** `s→a(4), s→b(5), b→a(-3)`: 라운드1에서 `a=4, b=5`, 그 뒤 `b→a` 완화 → `a=min(4, 5-3)=2`. 음수 사이클 없으니 한 번 더 완화 안 됨 → `[0,2,5]`.

## 응용 (Applications)

- 음수 가중치 최단 경로, 음수 사이클 탐지.
- 환율 차익 거래 탐지, 차이 제약 시스템.
- 거리 벡터 라우팅(RIP)의 기반, [Johnson](Floyd-Warshall.md) 재가중의 1단계.

## 흔한 오해 (Common Misunderstandings)

- **음수 사이클이 있으면 "최단 경로"가 정의 안 됨**(무한히 감소) — BF는 탐지만.
- **음수 간선 ≠ 음수 사이클** — 사이클만 없으면 최단 경로는 잘 정의된다.
- **다익스트라에 음수 간선을 넣어 "고치는" 트릭은 일반적으로 틀린다**.
- **$V-1$ 보다 적게 수렴할 수 있다** — 변화 없으면 조기 종료.

## TMI

- 환율 그래프에 $-\log$ 를 취하면 차익 거래가 음수 사이클 탐지로 정확히 환원된다.
- 거리 벡터 라우팅의 "count to infinity"는 분산 환경 BF의 고전적 난점이다(split horizon으로 완화).
- SPFA는 대회에서 빠르다고 인기였으나, 의도적 최악 케이스($O(VE)$)에 막혀 "SPFA is dead" 밈이 생겼다.

## 연습 / 확인 문제 (Exercises)

- 음수 간선 그래프에서 $V-1$ 라운드 완화를 손으로 수행하라.
- 음수 사이클을 만든 뒤 $V$ 번째 완화에서 탐지되고, `prev` 로 사이클을 추출하라.
- 다익스트라가 음수 간선에서 틀리는 반례를 만들어라.
- 차이 제약 $x_j-x_i\le w$ 들을 그래프로 바꿔 해를 구하라.

## 이어서 읽기 (Reading Path)

- 이전: [다익스트라](Dijkstra.md)
- 다음: [플로이드-워셜](Floyd-Warshall.md)
- 관련: [그래프 이론](../Math/Discrete/Graph-Theory.md)

## 참조 (References)

- [Algorithms/Dijkstra.md](Dijkstra.md)
- [Algorithms/Floyd-Warshall.md](Floyd-Warshall.md)
- [Reference/Books.md](../Reference/Books.md)
