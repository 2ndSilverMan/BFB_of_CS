# 비트마스크 DP (Bitmask DP)

- Level: Advanced
- Prerequisites: [Algorithms/DP-Basics.md](DP-Basics.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

비트마스크 DP는 **부분집합을 정수의 비트로 인코딩**해 상태로 삼는 DP다. "어떤 원소를 이미 사용/방문했나" 같은 집합 상태를 $2^n$ 개 정수로 표현해, 작은 $n(\le20)$ 에서 지수 문제를 효율적으로 푼다.

## 직관 (Intuition)

방문 여부를 원소마다 0/1로 적으면 길이 $n$ 비트열 = 정수 하나. 집합을 정수로 다루면 "이 집합 상태의 최적값"을 배열 인덱스로 저장한다. 외판원처럼 "방문 집합 + 현재 위치"가 상태인 문제에 딱 맞는다.

## 이론 (Theory)

### 1. 비트 연산

- 포함 여부: `mask & (1<<i)`
- 추가/제거: `mask | (1<<i)` / `mask & ~(1<<i)`
- 켜진 비트 수: popcount
- **부분집합 순회**: `s = mask; while s: ...; s = (s-1) & mask`

### 2. Held-Karp TSP

$dp[\text{mask}][i]$ = 방문 집합 mask, 현재 $i$ 일 때 최소 비용:

$$dp[\text{mask}\mid(1\ll j)][j]=\min_i\big(dp[\text{mask}][i]+w(i,j)\big)$$

### 3. 부분집합-부분집합 순회는 $3^n$

각 원소가 "마스크 밖 / 부분집합 안 / 부분집합 밖" 셋 중 하나 → 모든 (mask, submask) 쌍 수 $=\sum_{\text{mask}}2^{|\text{mask}|}=3^n$. **SOS(sum over subsets) DP**는 이를 $O(n2^n)$ 으로 줄인다(차원별 누적).

## 구현 (Implementation)

```python
def tsp(dist, n):
    INF = float("inf")
    dp = [[INF]*n for _ in range(1 << n)]
    dp[1][0] = 0                                  # 0번에서 시작
    for mask in range(1 << n):
        for i in range(n):
            if not (mask >> i) & 1 or dp[mask][i] == INF: continue
            for j in range(n):
                if (mask >> j) & 1: continue
                nm = mask | (1 << j)
                dp[nm][j] = min(dp[nm][j], dp[mask][i] + dist[i][j])
    full = (1 << n) - 1
    return min(dp[full][i] + dist[i][0] for i in range(n))   # 시작점 복귀
```

## 복잡도 (Complexity)

| 문제 | 시간 | 공간 |
|---|---|---|
| TSP (Held-Karp) | $O(2^n n^2)$ | $O(2^n n)$ |
| 부분집합 합 | $O(2^n n)$ | $O(2^n)$ |
| 부분집합-부분집합 순회 | $O(3^n)$ | — |

$n\le20$ 정도까지 실용적. **워크드 예제(n=3).** `dp[001][0]=0` → `dp[011][1]=w(0,1)`, `dp[101][2]=w(0,2)` → `dp[111][·]` 채운 뒤 시작점 복귀 최소. $2^3\cdot3^2=72$ 전이.

## 응용 (Applications)

- TSP·해밀턴 경로·작은 그래프 채색.
- 집합 분할·배정(작업-기계 매칭), 부분집합 합/곱.
- SOS DP(부분집합 합 누적), 프로파일 DP(broken profile).

## 흔한 오해 (Common Misunderstandings)

- **$n>22$ 정도면 $2^n$ 이 메모리·시간 모두 폭발** — 작은 $n$ 전용.
- **비트 연산자 우선순위 주의** — `mask & 1<<i` 는 의도와 다름(괄호 필요).
- **"모든 부분집합"($2^n$)과 "부분집합의 부분집합"($3^n$)은 비용이 다르다**.
- **다항식 해법을 대체하지 않는다** — NP-난해를 작은 입력에서 푸는 도구.

## TMI

- Held-Karp(1962)가 바로 이 비트마스크 DP로, 무차별 $O(n!)$ 을 $O(2^n n^2)$ 로 줄였다(여전히 지수지만 큰 개선).
- `(s-1) & mask` 부분집합 순회는 비트 기교의 백미로 꼽힌다.
- TSP의 정확한 해는 여전히 지수지만, 비트마스크 DP는 $n\approx20$, 분기한정은 수천 도시까지 실전 처리한다.

## 연습 / 확인 문제 (Exercises)

- 4도시 TSP를 비트마스크 DP로 손으로 채워라.
- 주어진 mask의 모든 부분집합을 순회하는 코드를 작성하라.
- 전체 부분집합-부분집합 순회가 $O(3^n)$ 인 이유를 세어 보라.
- SOS DP로 "각 mask의 모든 부분집합 합"을 $O(n2^n)$ 에 구하라.

## 이어서 읽기 (Reading Path)

- 이전: [DP 최적화](DP-Optimization.md)
- 다음: [트리 DP](Tree-DP.md)
- 관련: [해밀턴 경로 / TSP — 근사](Approximation-Algorithms.md)

## 참조 (References)

- [Algorithms/DP-Basics.md](DP-Basics.md)
- [Reference/Books.md](../Reference/Books.md)
