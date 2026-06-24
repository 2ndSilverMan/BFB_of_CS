# 플로이드-워셜 (Floyd-Warshall)

- Level: Intermediate
- Prerequisites: [Algorithms/Bellman-Ford.md](Bellman-Ford.md), [Algorithms/DP-Basics.md](DP-Basics.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

플로이드-워셜은 모든 정점 쌍 사이의 최단 경로(all-pairs shortest path)를 구하는 동적 계획법 알고리즘이다. 음의 간선을 허용하며(음의 사이클은 없어야 함), 간결한 삼중 루프로 구현된다.

## 직관 (Intuition)

"$i$에서 $j$로 가는 최단 경로"를 "중간에 거쳐도 되는 정점 집합"을 하나씩 늘려 가며 개선한다. 처음엔 직접 간선만 보고, 그다음 1번 정점을 경유해도 되게 하고, 2번도... 모든 정점을 경유 후보로 추가하고 나면 모든 쌍의 최단 거리가 완성된다. "경유점을 허락한다"는 발상이 핵심이다.

## 이론 (Theory)

$d_k[i][j]$ = 정점 $\{1,\dots,k\}$만 중간 경유로 허용했을 때 $i\to j$ 최단 거리. 점화식:

$$d_k[i][j]=\min\big(d_{k-1}[i][j],\ d_{k-1}[i][k]+d_{k-1}[k][j]\big)$$

$k$ 차원은 제자리 갱신(in-place)으로 없앨 수 있어 2차원 배열이면 충분하다. 대각선 $d[i][i]$가 음수가 되면 음의 사이클을 탐지한 것이다.

## 구현 (Implementation)

```python
def floyd_warshall(dist):          # dist[i][j]: 초기 인접(없으면 inf)
    n = len(dist)
    for k in range(n):             # 경유 허용 정점
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    return dist
```

## 복잡도 (Complexity)

| | 시간 | 공간 |
|---|---|---|
| 일반 | `O(V^3)` | `O(V^2)` |

조밀 그래프의 모든 쌍 최단 경로에 단순하고 효율적이다. 희소 그래프에서 모든 쌍이 필요하면 각 정점에서 다익스트라를 돌리는 `O(V·E log V)`가 더 빠를 수 있다.

## 응용 (Applications)

- 모든 정점 쌍 최단 거리(작은 조밀 그래프)
- 그래프의 전이 폐쇄(transitive closure, 도달 가능성)
- 네트워크 지름·중심성 계산
- 라우팅 테이블 사전 계산

## 흔한 오해 (Common Misunderstandings)

- $k$ 루프가 가장 바깥에 와야 한다. 순서를 바꾸면 틀린다.
- 음의 사이클이 있으면 결과가 무의미하다(대각선 음수로 탐지 가능).
- `O(V^3)`이라 정점 수가 수백을 넘으면 비현실적이다.
- 경로 자체가 필요하면 다음 정점(next) 배열을 따로 기록해야 한다.

## TMI

- 같은 점화식 구조가 전이 폐쇄(워셜 알고리즘)와 최단 경로(플로이드)에 동시에 적용된다.
- 삼중 루프 다섯 줄이라는 간결함 덕에 "가장 외우기 쉬운 그래프 알고리즘"으로 꼽힌다.
- min-plus 행렬 곱으로 보면, 거듭제곱을 통한 일반화도 가능하다.

## 연습 / 확인 문제 (Exercises)

- 4개 정점 그래프에서 $k$를 1,2,3,4로 늘려 가며 거리 행렬을 갱신하라.
- $k$ 루프를 안쪽에 두면 왜 틀리는지 반례로 설명하라.
- next 배열로 실제 경로를 복원하는 방법을 기술하라.

## 이어서 읽기 (Reading Path)

- 이전: [최단 경로 — Bellman-Ford](Bellman-Ford.md)
- 다음: [강한 연결 요소 (SCC)](SCC.md)

## 참조 (References)

- [Algorithms/Bellman-Ford.md](Bellman-Ford.md)
- [Algorithms/DP-Basics.md](DP-Basics.md)
- [Reference/Books.md](../Reference/Books.md)
