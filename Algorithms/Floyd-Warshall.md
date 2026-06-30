# 플로이드-워셜 (Floyd-Warshall)

- Level: Intermediate
- Prerequisites: [Algorithms/Bellman-Ford.md](Bellman-Ford.md), [Algorithms/DP-Basics.md](DP-Basics.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

플로이드-워셜은 **모든 정점 쌍 최단 경로(APSP)** 를 구하는 DP다. 음수 간선을 허용(음수 사이클은 없어야)하고, 삼중 루프 다섯 줄로 끝난다.

## 직관 (Intuition)

"$i\to j$ 최단 경로"를 **경유 허용 정점 집합을 하나씩 늘리며** 개선한다. 처음엔 직접 간선만, 그다음 1번 경유 허용, 2번도… 모든 정점을 경유 후보로 추가하면 모든 쌍이 완성된다. "경유점을 허락한다"가 핵심.

## 이론 (Theory)

### 1. DP 정의와 점화식

$d_k[i][j]$ = 중간 경유를 $\{1,\dots,k\}$ 로 제한했을 때 $i\to j$ 최단 거리.

$$d_k[i][j]=\min\big(d_{k-1}[i][j],\ d_{k-1}[i][k]+d_{k-1}[k][j]\big)$$

"$k$ 를 경유 안 함" vs "$k$ 를 경유함(앞·뒤 토막은 $\{1..k{-}1\}$ 만 경유)"의 비교다.

### 2. $k$ 가 가장 바깥 + in-place 정당성

$k$ 루프가 **가장 바깥**이어야 한다 — 안쪽에 두면 $d_{k-1}$ 가 준비되기 전에 참조해 틀린다. $k$ 차원은 제자리(2D)로 없앨 수 있는데, 라운드 $k$ 에서 $d[i][k]$ 와 $d[k][j]$ 는 **그 라운드에 바뀌지 않기 때문**이다($d[k][k]=0$ 이라 자기 자신 경유는 개선이 없음, 음수 사이클이 없을 때). 대각선 $d[i][i]<0$ 이 되면 음수 사이클 탐지.

### 3. 일반화

같은 점화식이 **전이 폐쇄**(Warshall, `min/+`를 `or/and`로)와 최단 경로(Floyd)에 동시에 적용된다. **min-plus 행렬 곱**으로 보면 거듭제곱 일반화도 가능하다.

## 구현 (Implementation)

```python
def floyd_warshall(dist):                 # dist[i][j]: 초기 인접(없으면 inf, dist[i][i]=0)
    n = len(dist)
    nxt = [[j for j in range(n)] for _ in range(n)]   # 경로 복원용
    for k in range(n):                    # 경유 허용 정점 (가장 바깥!)
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    nxt[i][j] = nxt[i][k]
    return dist, nxt

def path(nxt, i, j):                      # 실제 경로 복원
    if nxt[i][j] is None: return []
    out = [i]
    while i != j:
        i = nxt[i][j]; out.append(i)
    return out
```

## 복잡도 (Complexity)

| | 시간 | 공간 |
|---|---|---|
| 일반 | $O(V^3)$ | $O(V^2)$ |

조밀 그래프 APSP에 단순·효율적. **희소 그래프 APSP는 각 정점 다익스트라**($O(V\,E\log V)$)나 Johnson($O(VE + V^2\log V)$)이 더 빠를 수 있다. **워크드 예제(3정점).** `0→1:4, 0→2:1, 2→1:2`. $k=2$ 라운드에서 `d[0][1]=min(4, d[0][2]+d[2][1]=1+2=3)=3`. 다른 경유로는 개선 없음 → `d[0][1]=3`.

## 응용 (Applications)

- 작은 조밀 그래프의 모든 쌍 최단 거리, 라우팅 테이블 사전 계산.
- 전이 폐쇄(도달 가능성), 네트워크 지름·중심성.
- DP 상태 간 "도달 가능" 전처리.

## 흔한 오해 (Common Misunderstandings)

- **$k$ 루프가 가장 바깥** — 순서를 바꾸면 틀린다.
- **음수 사이클이 있으면 결과 무의미**(대각선 음수로 탐지).
- **$O(V^3)$** — 정점 수백 넘으면 비현실적.
- **경로가 필요하면 next 배열을 따로** 기록해야 한다.

## TMI

- 같은 점화식이 Warshall(전이 폐쇄)과 Floyd(최단 경로)에 동시에 적용돼 합쳐 부른다.
- 다섯 줄 삼중 루프라 "가장 외우기 쉬운 그래프 알고리즘"으로 꼽힌다.
- min-plus(트로피컬) 반환으로 보면 거리 행렬의 거듭제곱이 "간선 $\le 2^k$ 개 최단 경로"를 준다.

## 연습 / 확인 문제 (Exercises)

- 4정점 그래프에서 $k=1,2,3,4$ 로 거리 행렬을 갱신하라.
- $k$ 를 안쪽에 두면 왜 틀리는지 반례로 보여라.
- next 배열로 실제 경로를 복원하라.
- 전이 폐쇄(`or/and` 버전)로 도달 가능성 행렬을 구하라.

## 이어서 읽기 (Reading Path)

- 이전: [벨만-포드](Bellman-Ford.md)
- 다음: [강한 연결 요소 (SCC)](SCC.md)
- 관련: [DP 기초](DP-Basics.md)

## 참조 (References)

- [Algorithms/Bellman-Ford.md](Bellman-Ford.md)
- [Algorithms/DP-Basics.md](DP-Basics.md)
- [Reference/Books.md](../Reference/Books.md)
