# 트리 DP (Tree DP)

- Level: Intermediate
- Prerequisites: [Algorithms/DP-Basics.md](DP-Basics.md), [Algorithms/BFS-DFS.md](BFS-DFS.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

트리 DP는 **부분트리 단위로 부분 문제를 정의**하고 자식 결과를 모아 부모를 계산하는 DP다. 트리는 사이클이 없어 부분트리가 자연스러운 부분 문제가 된다 — 트리 지름·최대 독립 집합·부분트리 통계에 쓰인다.

## 직관 (Intuition)

각 노드의 답이 자식들의 답만으로 결정되므로, **잎에서 위로(post-order)** 정보를 모으면 된다. DFS로 자식을 먼저 처리하고 부모에서 합치는 것이 전형 패턴. "모든 노드를 루트로 했을 때"가 필요하면 **리루팅**으로 한 번 더.

## 이론 (Theory)

### 1. 부분트리 상태와 post-order

$dp[v][\cdot]$ = "$v$ 를 루트로 하는 부분트리의 최적값/통계". **최대 가중 독립 집합**:

$$dp[v][0]=\sum_c \max(dp[c][0],dp[c][1]),\qquad dp[v][1]=w_v+\sum_c dp[c][0]$$

($v$ 안 고름 / 고름; 고르면 자식은 못 고름).

### 2. 리루팅(rerooting) — $O(n^2)\to O(n)$

각 노드를 루트로 한 답을 각각 DFS하면 $O(n^2)$. 대신 ① 루트 고정 DFS로 부분트리 값 계산 → ② 부모→자식으로 내려가며 "부모 방향 기여"를 **차분으로 전파**하면 추가 $O(n)$ 에 전부 구한다.

### 3. 트리 지름

**두 번의 DFS**: 임의 노드에서 가장 먼 $u$, $u$ 에서 가장 먼 $v$ → $u$–$v$ 가 지름. (정당성: 가장 먼 노드는 항상 어떤 지름의 끝점.) 또는 각 노드에서 "가장 긴 두 자식 경로 합"의 최대.

## 구현 (Implementation)

```python
import sys
def max_independent_set(tree, root, w):
    sys.setrecursionlimit(1 << 20)
    dp = {}
    def dfs(v, parent):
        take, skip = w[v], 0
        for c in tree[v]:
            if c == parent: continue          # 부모로 되돌아가지 않기
            dfs(c, v)
            take += dp[c][0]                  # v 고름 → 자식 안 고름
            skip += max(dp[c][0], dp[c][1])   # v 안 고름 → 자식 자유
        dp[v] = (skip, take)                  # (v 안 고름, v 고름)
    dfs(root, -1)
    return max(dp[root])
```

## 복잡도 (Complexity)

| | 시간 | 공간 |
|---|---|---|
| 표준 트리 DP | $O(n)$ | $O(n)$ |
| 리루팅 | $O(n)$ | $O(n)$ |
| 트리 배낭 | $O(n\cdot K)$ 또는 $O(n^2)$ | — |

각 노드·간선을 상수 번 처리해 선형. **워크드 예제(경로 1-2-3, 가중치 1,10,1).** dp[3]=(0,1), dp[2]: skip=1+1=... take=10+dp[3][0]=10, skip=max(0,1)=1 → dp[2]=(1,10); dp[1]: take=1+dp[2][0]=1+1=2, skip=max(1,10)=10 → max=10(노드2만). 정답.

## 응용 (Applications)

- 트리 최대 독립 집합·최소 정점 덮개.
- 트리 지름·중심·부분트리 크기/합, 트리 배낭.
- 모든 노드 기준 답(리루팅), 트리 위 거리 통계.

## 흔한 오해 (Common Misunderstandings)

- **부모 방향으로 되돌아가지 않게 `parent` 추적**(무방향 트리).
- **깊은 트리는 재귀 DFS가 스택 오버플로** — 반복 DFS나 한도 상향.
- **모든 노드 기준 답에 각 노드 DFS는 $O(n^2)$** — 리루팅 필요.
- **트리 DP는 사이클이 없어 상태 정의가 단순** — 일반 그래프 DP와 다르다.

## TMI

- "두 번 DFS로 지름" 트릭은 가중치가 음이 아닐 때 성립하며, 우아한 고전이다.
- 트리 배낭이 부분트리 크기를 잘 합치면 $O(n^2)$ 가 보장되는 분석은 미묘하기로 유명하다(각 쌍이 LCA에서 한 번 곱해짐).
- 리루팅은 "한 번 계산하고 차분으로 옮긴다"는 발상으로 많은 트리 문제를 선형으로 만든다.

## 연습 / 확인 문제 (Exercises)

- 작은 트리에서 최대 가중 독립 집합 DP를 손으로 채워라.
- 두 번의 DFS로 트리 지름을 구하는 절차를 기술하고 정당성을 설명하라.
- 리루팅이 왜 $O(n^2)$ 를 $O(n)$ 으로 줄이는지 설명하라.
- 트리 배낭(각 노드 무게·가치, 부분트리 용량 $K$)을 구현하라.

## 이어서 읽기 (Reading Path)

- 이전: [비트마스크 DP](Bitmask-DP.md)
- 다음: [강한 연결 요소 (SCC)](SCC.md)
- 관련: [이진 트리](../Data-Structures/Binary-Tree.md), [BFS / DFS](BFS-DFS.md)

## 참조 (References)

- [Algorithms/DP-Basics.md](DP-Basics.md)
- [Data-Structures/Binary-Tree.md](../Data-Structures/Binary-Tree.md)
- [Reference/Books.md](../Reference/Books.md)
