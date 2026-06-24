# 강한 연결 요소 (Strongly Connected Components)

- Level: Advanced
- Prerequisites: [Algorithms/BFS-DFS.md](BFS-DFS.md), [Algorithms/Topological-Sort.md](Topological-Sort.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

강한 연결 요소(SCC)는 방향 그래프에서 서로 도달 가능한 정점들의 최대 집합이다. SCC들을 하나의 정점으로 압축하면 사이클 없는 방향 그래프(DAG)가 된다. 코사라주와 타잔 알고리즘이 대표적이다.

## 직관 (Intuition)

방향 그래프에서 "A에서 B로 갈 수 있고 B에서도 A로 올 수 있으면" 둘은 같은 덩어리다. 이 덩어리(SCC) 안에서는 어디든 오갈 수 있다. 덩어리들끼리는 한 방향으로만 이어져 사이클이 없는 구조(DAG)를 이룬다. 이 압축이 의존성·도달성 분석을 단순하게 만든다.

## 이론 (Theory)

**코사라주**: ① 원그래프에서 DFS로 종료 시각 순서를 기록, ② 간선을 뒤집은 전치 그래프에서 종료 시각 역순으로 DFS, 각 트리가 하나의 SCC. 두 번의 DFS로 `O(V+E)`.

**타잔**: 한 번의 DFS로 각 정점의 방문 순서 `disc`와 도달 가능한 최소 순서 `low`를 추적, 스택을 이용해 SCC를 식별한다. `low[u]==disc[u]`이면 $u$가 SCC의 루트.

SCC를 정점으로 축약한 **응축 그래프(condensation)**는 항상 DAG이며, 위상 정렬과 결합해 도달성·2-SAT을 푼다.

## 구현 (Implementation)

```python
def tarjan_scc(graph, n):
    idx = [None]*n; low = [0]*n; on_stack=[False]*n
    stack=[]; counter=[0]; sccs=[]
    def dfs(u):
        idx[u]=low[u]=counter[0]; counter[0]+=1
        stack.append(u); on_stack[u]=True
        for v in graph[u]:
            if idx[v] is None:
                dfs(v); low[u]=min(low[u], low[v])
            elif on_stack[v]:
                low[u]=min(low[u], idx[v])
        if low[u]==idx[u]:                 # SCC 루트
            comp=[]
            while True:
                w=stack.pop(); on_stack[w]=False; comp.append(w)
                if w==u: break
            sccs.append(comp)
    for u in range(n):
        if idx[u] is None: dfs(u)
    return sccs
```

## 복잡도 (Complexity)

| | 시간 | 공간 |
|---|---|---|
| 코사라주/타잔 | `O(V+E)` | `O(V+E)` |

두 알고리즘 모두 선형이다. 코사라주는 그래프를 두 번 순회하고 전치 그래프가 필요하며, 타잔은 한 번의 DFS로 끝나 상수가 작은 편이다.

## 응용 (Applications)

- 2-SAT 해결(함의 그래프의 SCC)
- 의존성 사이클 탐지(빌드·패키지·데드락)
- 웹/소셜 그래프의 상호 도달 군집
- 컴파일러의 호출 그래프 분석

## 흔한 오해 (Common Misunderstandings)

- SCC는 방향 그래프 개념이다. 무방향 그래프의 "연결 요소"와 다르다.
- 단일 정점도 SCC가 될 수 있다(자기 자신만 도달).
- 응축 그래프가 DAG라는 사실이 위상 정렬·DP를 가능케 한다.
- 타잔의 `low` 정의(스택 위 정점만 갱신)를 잘못 쓰면 틀린다.

## TMI

- 2-SAT은 변수와 그 부정을 함의 그래프로 만들어, $x$와 $\lnot x$가 같은 SCC면 불가능으로 판정한다.
- 타잔은 이 외에도 LCA·브리지 등 수많은 그래프 알고리즘을 남긴 거장이다.
- 코사라주 알고리즘은 직관이 명확해 교육용으로, 타잔은 효율 때문에 실전에서 선호된다.

## 연습 / 확인 문제 (Exercises)

- 작은 방향 그래프에서 SCC를 손으로 찾고 응축 그래프를 그려라.
- 응축 그래프가 항상 DAG인 이유를 설명하라.
- 2-SAT 한 사례를 함의 그래프 SCC로 풀어라.

## 이어서 읽기 (Reading Path)

- 이전: [위상 정렬](Topological-Sort.md)
- 다음: [최대 유량](Max-Flow.md)

## 참조 (References)

- [Algorithms/BFS-DFS.md](BFS-DFS.md)
- [Algorithms/Topological-Sort.md](Topological-Sort.md)
- [Reference/Books.md](../Reference/Books.md)
