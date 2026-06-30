# 강한 연결 요소 (Strongly Connected Components)

- Level: Advanced
- Prerequisites: [Algorithms/BFS-DFS.md](BFS-DFS.md), [Algorithms/Topological-Sort.md](Topological-Sort.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

SCC는 방향 그래프에서 **서로 도달 가능한 정점들의 최대 집합**이다. SCC들을 한 정점으로 압축한 **응축 그래프(condensation)** 는 항상 DAG가 된다 — 방향 그래프를 "사이클 없는 뼈대"로 환원하는 핵심 도구.

## 직관 (Intuition)

"A→B 도 되고 B→A 도 되면" 둘은 같은 덩어리다. 덩어리(SCC) 안에선 어디든 오가지만, 덩어리끼리는 한 방향으로만 이어져 사이클이 없다. 이 압축이 도달성·의존성·2-SAT 분석을 단순화한다.

## 이론 (Theory)

### 1. 코사라주 (DFS 두 번)

① 원그래프 DFS로 **종료 시각** 기록 → ② **전치 그래프**(간선 뒤집기)에서 종료 시각 **역순**으로 DFS, 각 DFS 트리가 하나의 SCC. 정당성: 종료 시각이 가장 늦은 정점은 응축 DAG의 "소스 SCC"에 있고, 전치에서 그 SCC만 도달 가능하다.

### 2. 타잔 (DFS 한 번, low-link)

각 정점에 방문 순서 `disc`, 스택을 통해 도달 가능한 최소 순서 `low` 를 추적. **`low[u]==disc[u]` 이면 `u` 가 SCC 루트** → 스택에서 `u` 까지 팝. `low` 갱신은 **스택 위(on-stack) 정점**으로만(이미 끝난 SCC를 끌어들이지 않도록).

### 3. 응축 DAG와 2-SAT

응축 그래프는 항상 DAG → 위상 정렬·DP 가능. **2-SAT**: 절 $(a\lor b)$ 를 함의 $\lnot a\Rightarrow b,\ \lnot b\Rightarrow a$ 로 그래프화. **$x$ 와 $\lnot x$ 가 같은 SCC면 불가능**, 아니면 응축 DAG의 위상 역순으로 각 변수 값을 정해 해를 만든다.

## 구현 (Implementation)

```python
import sys
def tarjan_scc(graph, n):
    sys.setrecursionlimit(1 << 20)
    disc = [None]*n; low = [0]*n; on = [False]*n
    stack, t, sccs = [], [0], []
    def dfs(u):
        disc[u] = low[u] = t[0]; t[0] += 1
        stack.append(u); on[u] = True
        for v in graph[u]:
            if disc[v] is None:
                dfs(v); low[u] = min(low[u], low[v])
            elif on[v]:
                low[u] = min(low[u], disc[v])      # 스택 위만
        if low[u] == disc[u]:                       # SCC 루트
            comp = []
            while True:
                w = stack.pop(); on[w] = False; comp.append(w)
                if w == u: break
            sccs.append(comp)
    for u in range(n):
        if disc[u] is None: dfs(u)
    return sccs
```

## 복잡도 (Complexity)

| | 시간 | 공간 |
|---|---|---|
| 코사라주 / 타잔 | $O(V+E)$ | $O(V+E)$ |

둘 다 선형. 코사라주는 그래프를 두 번 돌고 전치가 필요, 타잔은 한 번의 DFS로 끝나 상수가 작다. **워크드 예제.** `1→2→3→1, 3→4`: {1,2,3}이 한 SCC(서로 도달), {4}는 단독. 응축 `[{1,2,3}]→[{4}]` 은 DAG.

## 응용 (Applications)

- **2-SAT** 판정·해 구성(함의 그래프 SCC).
- 의존성 사이클 탐지(빌드·패키지·데드락), 컴파일러 호출 그래프.
- 웹/소셜 그래프의 상호 도달 군집(코어).

## 흔한 오해 (Common Misunderstandings)

- **SCC는 방향 그래프 개념** — 무방향의 "연결 요소"와 다르다.
- **단일 정점도 SCC** 가 될 수 있다.
- **타잔의 `low` 갱신은 on-stack 정점만** — 끝난 SCC를 끌어들이면 틀린다.
- **응축이 DAG**라는 사실이 위상 정렬·DP를 가능케 한다.

## TMI

- 2-SAT이 다항 시간인데 3-SAT은 NP-완전인 경계는, 2-SAT만 함의 그래프 SCC로 환원되기 때문이다.
- 타잔은 SCC 외에도 LCA·브리지·offline 등 수많은 선형 그래프 알고리즘을 남긴 거장이다.
- 코사라주는 직관이 명확해 교육용, 타잔은 한 번의 DFS라 실전 선호.

## 연습 / 확인 문제 (Exercises)

- 작은 방향 그래프에서 SCC를 손으로 찾고 응축 그래프를 그려라.
- 응축 그래프가 항상 DAG인 이유를 설명하라.
- 2-SAT 한 사례를 함의 그래프 SCC로 풀고 해를 구성하라.
- 코사라주에서 "종료 시각 역순"이 왜 소스 SCC부터 주는지 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [위상 정렬](Topological-Sort.md)
- 다음: [최대 유량](Max-Flow.md)
- 관련: [BFS / DFS](BFS-DFS.md)

## 참조 (References)

- [Algorithms/BFS-DFS.md](BFS-DFS.md)
- [Algorithms/Topological-Sort.md](Topological-Sort.md)
- [Reference/Books.md](../Reference/Books.md)
