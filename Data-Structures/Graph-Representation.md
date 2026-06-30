# 그래프 표현 (Graph Representation)

- Level: Beginner
- Prerequisites: [Data-Structures/Array.md](Array.md), [Data-Structures/Linked-List.md](Linked-List.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

그래프는 **정점(V)** 과 그들을 잇는 **간선(E)** 으로 관계를 표현한다. "그래프 표현"은 이 $V, E$ 를 메모리에 담는 방식이고, 선택에 따라 *공간*과 *연산 속도*가 근본적으로 갈린다 — 알고리즘 성능의 출발점이다.

## 직관 (Intuition)

도시-도로, 사람-친구, 웹페이지-링크, 작업-의존성은 모두 그래프다. 탐색 알고리즘에 필요한 핵심 질문은 둘: **"정점 v의 이웃을 모두 나열"**(BFS·DFS·다익스트라)과 **"u-v가 연결됐나"**(존재 확인). 어떤 표현은 전자가, 어떤 표현은 후자가 빠르다.

## 이론 (Theory)

### 1. 세 가지 핵심 표현

| 표현 | 저장 | 이웃 순회 | 간선 존재 확인 | 공간 |
|---|---|---|---|---|
| 인접 리스트 | 정점마다 이웃 목록 | $O(\deg v)$ | $O(\deg v)$ | $O(V+E)$ |
| 인접 행렬 | $V\times V$ 비트/값 표 | $O(V)$ | $O(1)$ | $O(V^2)$ |
| 인접 **셋**(해시) | 정점마다 이웃 해시셋 | $O(\deg v)$ | 평균 $O(1)$ | $O(V+E)$ |

간선 존재 확인이 잦으면 인접 셋이 리스트와 행렬의 장점을 절충한다.

### 2. 밀도(density)가 선택을 가른다

간선 수 $E$ 는 $O(V)$(희소)에서 $O(V^2)$(밀집)까지다. 대부분의 실제 네트워크는 **희소**($E \ll V^2$)라 인접 리스트가 표준이다. 밀집 그래프나 $O(V^2)$ 가 어차피 필요한 [Floyd–Warshall](../Algorithms/Floyd-Warshall.md) 류에선 인접 행렬이 캐시·코드 양면에서 유리하다.

### 3. 고성능 정적 표현: CSR

간선이 안 바뀌는 대형 그래프는 **CSR(Compressed Sparse Row)** 로 담는다: 모든 이웃을 하나의 평탄 배열 `adj`에, 정점별 시작 위치를 `start[]`에 둔다. 포인터·노드가 없어 **캐시 지역성**이 최고라 그래프 분석 엔진·GPU에서 쓴다(단, 간선 추가가 어렵다).

### 4. 방향·가중치·특수 간선

- 방향(`A→B`) vs 무방향(`A–B`, 양쪽에 추가).
- 가중치: 이웃을 `(neighbor, weight)` 로 저장.
- self-loop, parallel edge(다중 그래프) — 표현이 이를 감당하는지 확인.
- 격자(grid)처럼 규칙적이면 **암시적 그래프**(좌표 + 이동 규칙)로 메모리 0.

## 구현 (Implementation)

```python
# 인접 리스트 (가중치)
adj = {"A": [("B", 5), ("C", 2)], "B": [("D", 1)], "C": [], "D": []}

def add_undirected(adj, a, b, w=1):
    adj.setdefault(a, []).append((b, w))
    adj.setdefault(b, []).append((a, w))

# 인접 행렬 (V를 0..V-1로 라벨링)
INF = float("inf")
W = [[0, 5, 2, INF],
     [5, 0, INF, 1],
     [2, INF, 0, INF],
     [INF, 1, INF, 0]]
print(W[0][2])            # A-C 가중치 = 2, 존재 확인 O(1)

# CSR (정적): 이웃 [1,2 | 3 | | ]
start = [0, 2, 3, 3, 3]   # 정점 i의 이웃은 adj[start[i]:start[i+1]]
adj_flat = [1, 2, 3]
```

## 복잡도 (Complexity)

$V$=정점, $E$=간선, $\deg v$=차수.

| 표현 | 공간 | 이웃 순회 | 간선 확인 | 간선 추가 |
|---|---|---|---|---|
| 인접 리스트 | $O(V+E)$ | $O(\deg v)$ | $O(\deg v)$ | $O(1)$ |
| 인접 행렬 | $O(V^2)$ | $O(V)$ | $O(1)$ | $O(1)$ |
| CSR | $O(V+E)$ | $O(\deg v)$ | $O(\deg v)$ | 사실상 불가(재구축) |

**워크드 예제.** $V=1000$, $E=3000$(희소): 인접 리스트는 약 $V+2E \approx 7000$ 칸, 인접 행렬은 $10^6$ 칸 → **140배** 차이. 반대로 $E\approx V^2/2$ 면 둘이 비슷해지고, 이때 행렬의 $O(1)$ 간선 확인이 이득.

## 응용 (Applications)

- BFS/DFS·최단 경로·MST의 입력 표현.
- 소셜 네트워크 분석, 의존성 그래프·빌드 시스템(위상 정렬).
- 라우팅·네트워크 모델링, 추천(이분 그래프).

## 흔한 오해 (Common Misunderstandings)

- **인접 행렬이 항상 빠르지 않다** — 희소에선 공간 $O(V^2)$ 와 이웃 순회 $O(V)$ 가 모두 손해.
- **무방향은 간선을 양쪽에 추가**해야 한다.
- **정점이 0부터 연속이면 배열**, 문자열/객체 키면 딕셔너리/해시가 편하다.
- **가중치 그래프는 이웃을 단순 값이 아니라 `(neighbor, weight)`** 로 저장.
- 그림에서 **정점 위치·선 교차는 의미가 없다** — 연결은 간선으로만 정의된다.

## TMI

- 그래프 이론의 출발점으로 **오일러의 "쾨니히스베르크 일곱 다리"**(1736)가 자주 인용된다.
- 인접 행렬의 거듭제곱 $A^k$ 의 $(i,j)$ 성분은 **i→j 길이 $k$ 경로의 수**다 — 행렬 표현의 대수적 위력.
- 웹 그래프·소셜 그래프는 수십억 정점이라 CSR + 분산 저장이 필수다(예: Pregel, GraphX).

## 연습 / 확인 문제 (Exercises)

- 간선 목록 → 인접 리스트, 인접 리스트 → 인접 행렬 변환을 작성하라.
- $V=10^4$, $E=2\times10^4$ 일 때 두 표현의 메모리를 추산하고 어느 쪽을 쓸지 정하라.
- 인접 행렬에서 특정 정점의 이웃 목록을 $O(V)$ 에 구하고, CSR이 왜 더 빠른지 설명하라.
- $A^2$ 의 대각 성분이 무엇을 세는지 작은 그래프로 확인하라.

## 이어서 읽기 (Reading Path)

- 이전: [큐](Queue.md)
- 다음: [복잡도 분석](../Algorithms/Complexity.md)
- 관련: [BFS·DFS](../Algorithms/BFS-DFS.md), [유니온-파인드](Union-Find.md)

## 참조 (References)

- [Algorithms/BFS-DFS.md](../Algorithms/BFS-DFS.md)
- [Data-Structures/Array.md](Array.md)
- [Reference/Books.md](../Reference/Books.md)
- [Reference/Courses.md](../Reference/Courses.md)
- [Reference/Papers.md](../Reference/Papers.md)
