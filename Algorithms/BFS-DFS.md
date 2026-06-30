# BFS / DFS

- Level: Beginner
- Prerequisites: [Data-Structures/Graph-Representation.md](../Data-Structures/Graph-Representation.md), [Data-Structures/Queue.md](../Data-Structures/Queue.md), [Data-Structures/Stack.md](../Data-Structures/Stack.md), [Algorithms/Complexity.md](Complexity.md)
- Status: Review
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

BFS·DFS는 그래프/트리의 모든 정점을 체계적으로 방문하는 두 탐색이다. **BFS는 가까운 층부터 물결처럼**(큐), **DFS는 한 길을 끝까지 갔다 되돌아온다**(스택/재귀). 둘 다 $O(V+E)$ 지만, 만드는 **방문 트리의 구조**가 달라 풀 수 있는 문제가 갈린다.

## 직관 (Intuition)

미로에서 BFS는 거리 1, 2, 3… 칸으로 퍼져 **최단 간선 수**를 보장한다. DFS는 한 갈래를 끝까지 파고들어 **연결성·사이클·순서(위상)** 구조를 드러낸다. 공통 필수: **방문 표시** — 없으면 사이클에서 무한 반복한다.

| | 자료구조 | 보장 | 대표 응용 |
|---|---|---|---|
| BFS | 큐 | 무가중 최단 거리 | 최단경로, 이분 판정 |
| DFS | 스택/재귀 | 깊이 우선 시간 구조 | 위상정렬, SCC, 사이클 |

## 이론 (Theory)

### 1. BFS = 무가중 최단 거리 (증명 스케치)

BFS는 거리 $d$ 인 정점을 모두 큐에서 처리한 뒤 거리 $d+1$ 을 처리한다(층 단위). 귀납으로 "큐에서 꺼낼 때의 `dist`가 최단 거리"임이 성립 — 더 짧은 경로가 있었다면 그 이웃이 더 일찍 큐에 들어갔을 것이기 때문. 그래서 **간선 가중치가 모두 같을 때만** 최단을 보장한다(가중치 있으면 다익스트라).

### 2. DFS의 간선 분류와 시간

DFS는 각 정점에 **발견(discovery)·종료(finish) 시각**을 매기고 간선을 분류한다:

- **tree edge**: 새 정점으로
- **back edge**: 조상으로 → **사이클의 증거**(방향 그래프 사이클 판정 핵심)
- **forward / cross edge**: 방향 그래프에서만

**괄호 정리**: 두 정점의 `[discovery, finish]` 구간은 포함되거나 서로소다(겹치지 않음). 이 구조에서 **위상 정렬**(finish 역순), **SCC**(Tarjan/Kosaraju)가 따라 나온다.

### 3. 응용 매핑

- BFS: 무가중 최단경로, 연결 요소, **이분 그래프 판정**(2색칠), 다중 시작점 BFS, 0-1 BFS([덱](../Data-Structures/Deque.md)).
- DFS: [위상 정렬](Topological-Sort.md), [SCC](SCC.md), 사이클 판정(back edge), 단절점·다리, [백트래킹](Backtracking.md).

## 구현 (Implementation)

```python
from collections import deque

def bfs_dist(graph, start):                  # 무가중 최단 거리
    dist = {start: 0}
    q = deque([start])
    while q:
        u = q.popleft()
        for v in graph[u]:
            if v not in dist:                # 큐에 넣을 때 방문 표시(중복 삽입 방지)
                dist[v] = dist[u] + 1
                q.append(v)
    return dist

def dfs_iter(graph, start):                  # 명시적 스택: 깊은 그래프에서 안전
    visited, order, stack = set(), [], [start]
    while stack:
        u = stack.pop()
        if u in visited: continue
        visited.add(u); order.append(u)
        for v in reversed(graph[u]):         # 재귀와 같은 순서로
            if v not in visited:
                stack.append(v)
    return order
```

## 복잡도 (Complexity)

| 표현 | 시간 | 탐색 보조 공간 |
|---|---|---|
| 인접 리스트 | $O(V+E)$ | $O(V)$ (visited + 프런티어) |
| 인접 행렬 | $O(V^2)$ | $O(V)$ |

각 정점·간선을 한 번씩 본다. **워크드 예제.** `A:[B,C], B:[A,D], C:[A], D:[B]`, 시작 A. BFS 순서 `A,B,C,D`(거리 0,1,1,2). DFS(재귀) `A,B,D,C` — 한 갈래(A→B→D)를 끝까지 간 뒤 백트래킹해 C.

## 응용 (Applications)

- 연결성·도달 가능성, 무가중 최단 거리, 미로/격자.
- 사이클 탐지, 위상 정렬, 강한 연결 요소.
- 이분 그래프 판정, 플러드 필, 트리 순회.

## 흔한 오해 (Common Misunderstandings)

- **방문 순서는 인접 리스트 순서에 의존** — 유일하지 않다.
- **BFS가 항상 최단경로는 아니다** — 간선 가중치가 같거나 없을 때만 최단 간선 수를 보장(가중치 있으면 [다익스트라](Dijkstra.md)).
- **DFS 재귀는 깊은 그래프에서 스택 오버플로** — 명시적 스택이 안전.
- **방문 표시를 큐에서 꺼낼 때 하면 중복 삽입** — *넣을 때* 표시.

## TMI

- BFS는 큐에 한 층이 통째로 쌓여 메모리를 크게 먹을 수 있다(폭이 넓은 그래프). DFS는 깊이만큼만 쌓인다 — 메모리 트레이드오프.
- 온라인 저지에서 Python 재귀 DFS는 깊은 입력에 `RecursionError`가 잦아, `sys.setrecursionlimit` 보다 명시적 스택이 안전한 경우가 많다.
- BFS의 층 구조는 "6단계 분리 이론"(소셜 네트워크의 평균 거리) 측정의 기본 도구다.

## 연습 / 확인 문제 (Exercises)

- 2D 격자 미로의 최단 거리를 BFS로 구하라(다중 시작점 변형도).
- 무방향 그래프의 연결 요소 수를 DFS로 세라.
- 방향 그래프에서 back edge로 사이클을 탐지하라.
- 2색칠 BFS로 이분 그래프 여부를 판정하라.

## 이어서 읽기 (Reading Path)

- 이전: [이진 탐색](Binary-Search.md)
- 다음: [위상 정렬](Topological-Sort.md)
- 관련: [백트래킹](Backtracking.md), [다익스트라](Dijkstra.md), [강한 연결 요소](SCC.md)

## 참조 (References)

- [Algorithms/Complexity.md](Complexity.md)
- [Data-Structures/Graph-Representation.md](../Data-Structures/Graph-Representation.md)
- [Data-Structures/Queue.md](../Data-Structures/Queue.md)
- [Data-Structures/Stack.md](../Data-Structures/Stack.md)
- [Reference/Books.md](../Reference/Books.md)
- [Reference/Courses.md](../Reference/Courses.md)
- [Reference/Papers.md](../Reference/Papers.md)
