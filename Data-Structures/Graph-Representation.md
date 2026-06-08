# 그래프 표현 (Graph Representation)

- Level: Beginner
- Prerequisites: [Data-Structures/Array.md](Array.md), [Data-Structures/Linked-List.md](Linked-List.md)
- Status: Draft

---

## 개념 (Concept)

그래프는 정점(Vertex)과 간선(Edge)으로 관계를 표현하는 구조다. 그래프 표현은 이 정점과 간선을 프로그램에서 저장하는 방법이다.

## 직관 (Intuition)

도시와 도로, 사람과 친구 관계, 웹 페이지와 링크, 작업과 의존성은 모두 그래프로 볼 수 있다. 알고리즘이 그래프를 탐색하려면 "어떤 정점이 어떤 정점과 연결되어 있는지"를 빠르게 확인할 수 있어야 한다.

대표 표현은 인접 리스트와 인접 행렬이다.

## 이론 (Theory)

| 표현 | 저장 방식 | 장점 | 단점 |
|---|---|---|---|
| 인접 리스트 | 각 정점마다 연결된 이웃 목록 저장 | 희소 그래프에 효율적 | 두 정점 연결 여부 확인이 느릴 수 있음 |
| 인접 행렬 | `V x V` 표에 간선 여부 저장 | 연결 여부 O(1) 확인 | 공간 O(V^2) 필요 |

희소 그래프는 가능한 간선 수보다 실제 간선 수가 훨씬 적은 그래프다. 대부분의 실제 네트워크는 희소 그래프에 가까워 인접 리스트를 많이 쓴다.

그래프는 방향성과 가중치에 따라 나뉜다.

| 종류 | 의미 |
|---|---|
| 무방향 그래프 | A-B가 양방향 연결 |
| 방향 그래프 | A -> B처럼 방향이 있음 |
| 가중치 그래프 | 간선에 비용/거리/시간이 있음 |

## 구현 (Implementation)

인접 리스트:

```python
graph = {
    "A": ["B", "C"],
    "B": ["A", "D"],
    "C": ["A"],
    "D": ["B"],
}
```

무방향 그래프에 간선 추가:

```python
def add_undirected_edge(graph, a, b):
    if a not in graph:
        graph[a] = []
    if b not in graph:
        graph[b] = []

    graph[a].append(b)
    graph[b].append(a)
```

인접 행렬:

```python
matrix = [
    [0, 1, 1, 0],
    [1, 0, 0, 1],
    [1, 0, 0, 0],
    [0, 1, 0, 0],
]

print(matrix[0][2] == 1)  # A-C 연결 여부
```

## 복잡도 (Complexity)

| 표현 | 공간 | 이웃 순회 | 간선 존재 확인 |
|---|---|---|---|
| 인접 리스트 | O(V + E) | O(deg(v)) | O(deg(v)) |
| 인접 행렬 | O(V^2) | O(V) | O(1) |

`V`는 정점 수, `E`는 간선 수, `deg(v)`는 정점 v의 차수다.

## 응용 (Applications)

- BFS/DFS 입력 표현
- 최단 경로 알고리즘
- 소셜 네트워크 분석
- 의존성 그래프와 빌드 시스템
- 라우팅과 네트워크 모델링

## 흔한 오해 (Common Misunderstandings)

- 인접 행렬이 항상 빠른 것은 아니다. 공간이 커지고 이웃 순회가 O(V)라 희소 그래프에서는 불리하다.
- 무방향 그래프는 간선을 양쪽에 모두 추가해야 한다.
- 정점 번호가 0부터 연속이면 배열 기반 표현이 편하고, 문자열/객체 키면 딕셔너리 기반 표현이 편하다.
- 가중치 그래프는 이웃을 단순 값이 아니라 `(neighbor, weight)` 형태로 저장해야 한다.

## TMI

- 그래프 이론의 대표적인 출발점으로 Euler의 "쾨니히스베르크의 일곱 다리" 문제가 자주 언급된다. 도시의 다리를 한 번씩만 건널 수 있는지 묻는 문제였다.
- 소셜 네트워크에서 "친구의 친구"를 찾는 일도 그래프의 이웃을 따라가는 연산으로 볼 수 있다.
- 그래프에는 자기 자신으로 돌아오는 self-loop나 같은 두 정점을 잇는 parallel edge도 있을 수 있다. 문제에서 금지하지 않았다면 표현 방식이 이를 감당하는지 확인해야 한다.
- 그래프 그림에서 정점 위치는 보통 의미가 없다. 선이 교차해 보여도 실제로 간선이 만나는지는 정점으로 표시되었는지 봐야 한다.

## 연습 / 확인 문제 (Exercises)

- 무방향 그래프의 간선 목록을 인접 리스트로 변환하라.
- 인접 행렬에서 특정 정점의 이웃 목록을 구하라.
- 같은 그래프를 인접 리스트와 인접 행렬로 각각 표현하고 공간 사용 차이를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [큐](Queue.md)
- 다음: [복잡도 분석](../Algorithms/Complexity.md)

## 참조 (References)

- [Algorithms/BFS-DFS.md](../Algorithms/BFS-DFS.md)
- [Data-Structures/Array.md](Array.md)
- [Reference/Books.md](../Reference/Books.md)
- [Reference/Courses.md](../Reference/Courses.md)
- [Reference/Papers.md](../Reference/Papers.md)
