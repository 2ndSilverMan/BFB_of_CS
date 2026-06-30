# 디닉 알고리즘 (Dinic's Algorithm)

- Level: Advanced
- Prerequisites: [Algorithms/Max-Flow.md](Max-Flow.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

디닉은 최대 유량을 더 빠르게 구한다. BFS로 **레벨 그래프**를 만들고, DFS로 그 위에서 **막힘 흐름(blocking flow)** 을 한 번에 밀어 [Edmonds-Karp](Max-Flow.md)보다 효율적이다.

## 직관 (Intuition)

EK는 증가 경로를 하나씩 찾는다. 디닉은 source로부터의 **거리(레벨)** 를 매긴 뒤, 거리가 정확히 1씩 증가하는 간선만 쓰는 레벨 그래프에서 더 못 흘릴 때까지 한꺼번에 민다(한 phase). phase마다 sink까지 거리가 엄격히 늘어 적은 단계로 끝난다.

## 이론 (Theory)

### 1. 한 phase의 두 단계

1. **BFS**로 잔여 그래프의 레벨 계산. sink에 도달 못 하면 종료(최대 유량).
2. **DFS**로 레벨이 1씩 증가하는 간선만 따라 blocking flow를 흘린다. 포화된 간선은 **current-arc 포인터**로 영구히 건너뛴다.

### 2. phase 수가 $O(V)$ 인 이유

매 phase 후 sink까지의 **레벨(거리)이 엄격히 증가**한다(blocking flow가 그 거리의 모든 최단 경로를 포화시켰으므로). 거리는 $1\dots V$ 라 phase 수 $\le V-1$. 각 phase의 blocking flow는 current-arc 덕에 $O(VE)$ → 전체 $O(V^2E)$.

### 3. 단위 용량의 특별함

단위 용량(이분 매칭 등)에선 phase 수가 $O(\sqrt V)$, blocking flow가 $O(E)$ → **$O(E\sqrt V)$** ([Hopcroft-Karp](Bipartite-Matching.md)와 같은 경계).

## 구현 (Implementation)

```python
from collections import deque
class Dinic:
    def __init__(self, n):
        self.n = n; self.g = [[] for _ in range(n)]   # 간선: [to, cap, rev_index]
    def add(self, u, v, c):
        self.g[u].append([v, c, len(self.g[v])])
        self.g[v].append([u, 0, len(self.g[u])-1])    # 역간선 cap 0
    def bfs(self, s, t):
        self.lv = [-1]*self.n; self.lv[s] = 0; q = deque([s])
        while q:
            u = q.popleft()
            for v, c, _ in self.g[u]:
                if c > 0 and self.lv[v] < 0:
                    self.lv[v] = self.lv[u]+1; q.append(v)
        return self.lv[t] >= 0
    def dfs(self, u, t, f):
        if u == t: return f
        while self.it[u] < len(self.g[u]):
            e = self.g[u][self.it[u]]
            v, c, r = e
            if c > 0 and self.lv[v] == self.lv[u]+1:
                d = self.dfs(v, t, min(f, c))
                if d > 0:
                    e[1] -= d; self.g[v][r][1] += d; return d
            self.it[u] += 1                            # current-arc
        return 0
    def max_flow(self, s, t):
        flow = 0
        while self.bfs(s, t):
            self.it = [0]*self.n
            while (f := self.dfs(s, t, float("inf"))) > 0:
                flow += f
        return flow
```

## 복잡도 (Complexity)

| 그래프 | 시간 |
|---|---|
| 일반 | $O(V^2E)$ |
| 단위 용량(이분 매칭) | $O(E\sqrt V)$ |
| 단위 용량 + 단위 차수 | $O(E\sqrt E)$ |

EK의 $O(VE^2)$ 보다 훨씬 빠르며 실전 최대 유량의 표준. **워크드 예제.** 레벨 0(s),1,2,…로 나눈 뒤 한 DFS로 여러 경로를 동시에 포화 — 다음 BFS에서 sink 레벨이 +1 이상 올라간다.

## 응용 (Applications)

- 대규모 최대 유량/최소 컷, 이분 매칭($O(E\sqrt V)$).
- 프로젝트 선택·밀집 부분그래프, 스케줄링·할당의 흐름 모델.

## 흔한 오해 (Common Misunderstandings)

- **레벨 그래프 없이 단순 DFS면** EK만큼도 보장 못 한다.
- **current-arc 최적화를 빠뜨리면** phase가 $O(VE)$ 를 못 지켜 복잡도가 무너진다.
- **blocking flow ≠ 최대 유량** — "그 레벨 그래프에서 더 못 흘리는 흐름"일 뿐.
- **디닉이 항상 $O(V^2E)$ 는 아니다** — 단위 용량 등에서 더 빠르다.

## TMI

- 디닉(1970)은 학생 시절 고안했고, 냉전기 동·서방에서 한동안 독립적으로 발전했다.
- 단위 용량에서 디닉 = Hopcroft-Karp 경계라, 이분 매칭에 디닉을 그대로 써도 된다.
- 현대 최강은 push-relabel(FIFO/highest-label) 계열이며, 2022년 거의 선형 최대 유량이 발표됐다.

## 연습 / 확인 문제 (Exercises)

- 레벨 그래프를 BFS로 만드는 과정을 작은 예에서 보여라.
- current-arc 최적화가 왜 필요한지 설명하라.
- 단위 용량 그래프에서 phase 수가 $O(\sqrt V)$ 인 직관을 논하라.
- 디닉으로 이분 매칭을 풀고 $O(E\sqrt V)$ 임을 확인하라.

## 이어서 읽기 (Reading Path)

- 이전: [최대 유량](Max-Flow.md)
- 다음: [이분 매칭](Bipartite-Matching.md)
- 관련: [최소 비용 최대 유량 (MCMF)](MCMF.md)

## 참조 (References)

- [Algorithms/Max-Flow.md](Max-Flow.md)
- [Algorithms/Bipartite-Matching.md](Bipartite-Matching.md)
- [Reference/Books.md](../Reference/Books.md)
