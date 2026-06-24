# 비트마스크 DP (Bitmask DP)

- Level: Advanced
- Prerequisites: [Algorithms/DP-Basics.md](DP-Basics.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

비트마스크 DP는 부분집합을 정수의 비트로 인코딩해 상태로 삼는 동적 계획법이다. "어떤 원소들을 이미 사용/방문했는가" 같은 집합 상태를 $2^n$개의 정수로 표현해, 작은 $n$에서 지수 문제를 효율적으로 푼다.

## 직관 (Intuition)

방문 여부를 원소마다 0/1로 적으면 길이 $n$의 비트열이 되고, 이는 정수 하나다. 집합을 정수로 다루면 "이 집합 상태에서의 최적값"을 배열 인덱스로 저장할 수 있다. 외판원처럼 "방문한 도시 집합 + 현재 위치"가 상태인 문제에 딱 맞는다.

## 이론 (Theory)

상태를 $(\text{mask},\ \dots)$로 둔다. 비트 연산:
- 원소 $i$ 포함 여부: `mask & (1<<i)`
- 추가/제거: `mask | (1<<i)`, `mask & ~(1<<i)`
- 부분집합 순회: `for s in submasks(mask)`

**외판원(TSP)** 예: $dp[\text{mask}][i]$ = 방문 집합이 mask이고 현재 $i$에 있을 때 최소 비용.

$$dp[\text{mask}\,|\,(1\ll j)][j]=\min_i\ dp[\text{mask}][i]+w(i,j)$$

부분집합 합 DP, SOS(sum over subsets) DP 등도 같은 인코딩을 쓴다.

## 구현 (Implementation)

```python
def tsp(dist, n):
    INF = float('inf')
    dp = [[INF]*n for _ in range(1<<n)]
    dp[1][0] = 0                          # 0번 도시에서 시작
    for mask in range(1<<n):
        for i in range(n):
            if not (mask >> i) & 1 or dp[mask][i]==INF: continue
            for j in range(n):
                if (mask >> j) & 1: continue
                nm = mask | (1<<j)
                dp[nm][j] = min(dp[nm][j], dp[mask][i] + dist[i][j])
    full = (1<<n) - 1
    return min(dp[full][i] + dist[i][0] for i in range(n))
```

## 복잡도 (Complexity)

| 문제 | 시간 | 공간 |
|---|---|---|
| TSP | `O(2^n · n^2)` | `O(2^n · n)` |
| 부분집합 합 | `O(2^n · n)` | `O(2^n)` |

지수이지만 $n\le 20$ 정도까지 실용적이다. 모든 부분집합의 부분집합을 순회하면 전체가 `O(3^n)`이 된다.

## 응용 (Applications)

- 외판원 문제(TSP)와 변형
- 집합 분할·배정(작업-기계 매칭)
- 부분집합 합/곱, SOS DP
- 작은 그래프의 해밀턴 경로·채색

## 흔한 오해 (Common Misunderstandings)

- $n$이 커지면(>22 정도) $2^n$이 메모리·시간 모두 폭발한다.
- 비트 연산자 우선순위에 주의해야 한다(`mask & 1<<i`는 의도와 다름).
- "모든 부분집합 순회"와 "부분집합의 부분집합 순회"는 비용이 다르다($2^n$ vs $3^n$).
- 비트마스크 DP가 다항식 해법을 대체하지는 않는다. 작은 $n$ 전용이다.

## TMI

- TSP의 Held-Karp DP(1962)가 바로 이 비트마스크 DP로, 무차별 $O(n!)$을 $O(2^n n^2)$로 줄였다.
- `__builtin_popcount`(C/C++)나 `bin(x).count('1')`로 켜진 비트 수를 빠르게 센다.
- 부분집합 순회 `for s = mask; s; s = (s-1) & mask`는 비트 기교의 백미다.

## 연습 / 확인 문제 (Exercises)

- 4개 도시 TSP를 비트마스크 DP로 손으로 채워라.
- 주어진 mask의 모든 부분집합을 순회하는 코드를 작성하라.
- 전체 부분집합-부분집합 순회가 `O(3^n)`인 이유를 세어 보라.

## 이어서 읽기 (Reading Path)

- 이전: [DP 최적화](DP-Optimization.md)
- 다음: [트리 DP](Tree-DP.md)

## 참조 (References)

- [Algorithms/DP-Basics.md](DP-Basics.md)
- [Reference/Books.md](../Reference/Books.md)
