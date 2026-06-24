# 트리 DP (Tree DP)

- Level: Intermediate
- Prerequisites: [Algorithms/DP-Basics.md](DP-Basics.md), [Algorithms/BFS-DFS.md](BFS-DFS.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

트리 DP는 트리 구조 위에서 부분트리 단위로 부분 문제를 정의하고 결합하는 동적 계획법이다. 자식의 결과를 모아 부모를 계산하며, 루트에서 답을 얻는다. 트리 지름, 최대 독립 집합, 부분트리 통계 등에 쓰인다.

## 직관 (Intuition)

트리는 사이클이 없어 "부분트리"가 자연스러운 부분 문제다. 각 노드의 답이 자식들의 답만으로 결정되므로, 잎에서 위로 올라오며 정보를 모으면 된다. DFS로 자식을 먼저 처리(post-order)하고 부모에서 합치는 것이 전형적 패턴이다.

## 이론 (Theory)

상태는 보통 $dp[v][\cdot]$ = "$v$를 루트로 하는 부분트리에서의 최적값/통계". 자식 $c$들의 결과로 전이한다.

**예: 최대 가중 독립 집합**

$$dp[v][0]=\sum_c \max(dp[c][0],dp[c][1]),\qquad dp[v][1]=w_v+\sum_c dp[c][0]$$

($v$를 안 고름 / 고름). **리루팅(rerooting)** 기법은 한 번의 DFS로 모든 노드를 루트로 했을 때의 답을 추가 `O(n)`에 구한다. 트리 지름은 두 번의 DFS 또는 각 노드에서 가장 긴 두 자식 경로 합으로 구한다.

## 구현 (Implementation)

```python
import sys
def max_independent_set(tree, root, weight):
    dp = {}
    def dfs(v, parent):
        take, skip = weight[v], 0
        for c in tree[v]:
            if c == parent: continue
            dfs(c, v)
            take += dp[c][1]                       # 자식 안 고름
            skip += max(dp[c][0], dp[c][1])        # 자유
        dp[v] = (take, skip)                       # (v 고름, v 안 고름)
    sys.setrecursionlimit(10**6)
    dfs(root, -1)
    return max(dp[root])
```

## 복잡도 (Complexity)

| | 시간 | 공간 |
|---|---|---|
| 표준 트리 DP | `O(n)` | `O(n)` |
| 리루팅 | `O(n)` | `O(n)` |

각 노드와 간선을 상수 번 처리해 선형이다. 깊은 트리는 재귀 깊이가 커 반복적 DFS나 재귀 한도 상향이 필요하다.

## 응용 (Applications)

- 트리의 최대 독립 집합·최소 정점 덮개
- 트리 지름·중심·부분트리 크기/합
- 모든 노드 기준 답(리루팅)
- 트리 위 배낭(tree knapsack)

## 흔한 오해 (Common Misunderstandings)

- 부모 방향으로 다시 내려가지 않도록 `parent`를 추적해야 한다(무방향 트리).
- 깊은 트리는 재귀 DFS가 스택 오버플로를 일으킬 수 있다.
- 모든 노드 기준 답이 필요하면 각 노드마다 DFS는 `O(n^2)`이므로 리루팅을 써야 한다.
- 트리 DP는 일반 그래프 DP와 달리 사이클이 없어 상태 정의가 단순하다.

## TMI

- 트리 지름을 "임의 노드에서 가장 먼 노드 u, u에서 가장 먼 노드 v" 두 번 BFS로 구하는 트릭은 우아한 고전이다.
- 리루팅(재근화)은 "한 번 계산하고 차분으로 옮겨 간다"는 발상으로 많은 트리 문제를 선형으로 만든다.
- 트리 배낭은 부분트리 크기를 잘 합치면 `O(n^2)`가 보장되는 미묘한 분석으로 유명하다.

## 연습 / 확인 문제 (Exercises)

- 작은 트리에서 최대 가중 독립 집합 DP를 손으로 채워라.
- 두 번의 DFS로 트리 지름을 구하는 절차를 기술하라.
- 리루팅이 왜 `O(n^2)`를 `O(n)`으로 줄이는지 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [비트마스크 DP](Bitmask-DP.md)
- 다음: [강한 연결 요소 (SCC)](SCC.md)

## 참조 (References)

- [Algorithms/DP-Basics.md](DP-Basics.md)
- [Data-Structures/Binary-Tree.md](../Data-Structures/Binary-Tree.md)
- [Reference/Books.md](../Reference/Books.md)
