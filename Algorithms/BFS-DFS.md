# BFS / DFS

- Level: Beginner
- Prerequisites: [Data-Structures/Graph-Representation.md](../Data-Structures/Graph-Representation.md), [Data-Structures/Queue.md](../Data-Structures/Queue.md), [Data-Structures/Stack.md](../Data-Structures/Stack.md), [Algorithms/Complexity.md](Complexity.md)
- Status: Review
- Reviewed-by: -

---

## 개념 (Concept)

BFS와 DFS는 그래프나 트리의 모든 노드를 방문하는 대표적인 탐색 알고리즘이다. BFS는 가까운 노드부터 층별로 방문하고, DFS는 한 방향으로 깊게 들어간 뒤 되돌아온다.

## 직관 (Intuition)

미로를 탐색한다고 생각하면 BFS는 출발점에서 거리 1인 칸, 거리 2인 칸처럼 물결이 퍼지듯 탐색한다. DFS는 한 길을 끝까지 따라가 보고 막히면 마지막 갈림길로 돌아온다.

| 알고리즘 | 핵심 자료구조 | 특징 |
|---|---|---|
| BFS | 큐 | 최단 간선 수 거리 탐색에 적합 |
| DFS | 스택 또는 재귀 | 연결성, 사이클, 백트래킹에 적합 |

## 이론 (Theory)

그래프는 보통 인접 리스트로 표현한다.

```text
A: B, C
B: A, D
C: A
D: B
```

탐색에서 중요한 것은 방문 여부를 기록하는 것이다. 방문 기록이 없으면 같은 노드를 반복 방문하거나 사이클에서 끝나지 않을 수 있다.

BFS는 가중치가 없는 그래프에서 시작점으로부터의 최단 간선 수를 구할 수 있다. DFS는 트리 순회, 연결 요소 탐색, 위상 정렬, SCC 같은 알고리즘의 기반이 된다.

## 구현 (Implementation)

BFS:

```python
from collections import deque


def bfs(graph, start):
    visited = set([start])
    order = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order
```

DFS:

```python
def dfs(graph, start):
    visited = set()
    order = []

    def visit(node):
        visited.add(node)
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visit(neighbor)

    visit(start)
    return order
```

예시:

```python
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"],
}

print(bfs(graph, "A"))
print(dfs(graph, "A"))
```

## 복잡도 (Complexity)

| 표현 | 시간 | 그래프 저장 공간 | 탐색 보조 공간 |
|---|---|---|---|
| 인접 리스트 | O(V + E) | O(V + E) | O(V) |
| 인접 행렬 | O(V^2) | O(V^2) | O(V) |

`V`는 정점 수, `E`는 간선 수다. 인접 리스트에서는 각 정점과 각 간선을 한 번씩 확인한다. 탐색 보조 공간은 `visited`, 큐/스택, 재귀 호출 스택처럼 그래프 저장 공간을 제외한 추가 공간이다.

## 응용 (Applications)

- 그래프 연결성 확인
- 최단 간선 수 거리 계산
- 미로 탐색
- 트리 순회
- 사이클 탐지
- 위상 정렬과 강한 연결 요소 알고리즘의 기반

## 흔한 오해 (Common Misunderstandings)

- BFS와 DFS의 방문 순서는 인접 리스트의 순서에 따라 달라질 수 있다.
- BFS가 항상 최단 경로를 찾는 것은 아니다. 간선 가중치가 모두 같거나 없을 때 최단 간선 수를 보장한다.
- DFS 재귀 구현은 깊은 그래프에서 호출 스택 한계에 걸릴 수 있다.
- 방문 처리를 큐에서 꺼낼 때 할지, 큐에 넣을 때 할지에 따라 중복 삽입이 생길 수 있다.

## TMI

- BFS는 "가까운 곳부터 넓게" 퍼지는 탐색이라 소셜 네트워크의 몇 단계 연결, 격자 미로 최단 거리 같은 문제와 잘 맞는다.
- DFS는 "한 길을 끝까지" 들어가는 탐색이라 백트래킹, 퍼즐 탐색, 트리 순회에서 자주 보인다.
- BFS는 최단 거리를 잘 찾지만 큐에 많은 정점이 한꺼번에 쌓일 수 있어 메모리를 크게 먹을 수 있다.
- 온라인 저지에서 Python 재귀 DFS는 입력이 깊으면 `RecursionError`가 나기 쉽다. 재귀 제한을 올리는 방법도 있지만, 명시적 스택이 더 안전한 경우가 많다.

## 연습 / 확인 문제 (Exercises)

- 2차원 격자 미로에서 시작점에서 도착점까지의 최단 거리를 BFS로 구하라.
- 무방향 그래프의 연결 요소 개수를 DFS로 구하라.
- DFS를 재귀 대신 명시적 스택으로 구현하라.

## 이어서 읽기 (Reading Path)

- 이전: [이진 탐색](Binary-Search.md)
- 다음: [입문자 로드맵](../Roadmaps/Beginner.md)에서 완료 기준을 확인한다.
- 관련: [백트래킹](Backtracking.md), [위상 정렬](Topological-Sort.md)

## 참조 (References)

- [Algorithms/Complexity.md](Complexity.md)
- [Data-Structures/Graph-Representation.md](../Data-Structures/Graph-Representation.md)
- [Data-Structures/Queue.md](../Data-Structures/Queue.md)
- [Data-Structures/Stack.md](../Data-Structures/Stack.md)
- [Reference/Books.md](../Reference/Books.md)
- [Reference/Courses.md](../Reference/Courses.md)
- [Reference/Papers.md](../Reference/Papers.md)
