# 알고리즘 (Algorithms)

> 문제를 효율적으로 푸는 방법과 그 복잡도 분석.

**선수지식**: [Data-Structures/](../Data-Structures/), [Math/Discrete/](../Math/Discrete/)

---

## 읽는 법

- 링크가 걸린 `Draft` 문서는 지금 읽을 수 있는 초안이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

### 기초 및 정렬

| Order | 주제 | 파일 | Status |
|---|---|---|---|
| 1 | 복잡도 분석 (Big-O) | [Complexity.md](Complexity.md) | Draft |
| 2 | 정렬 (Sorting) | [Sorting.md](Sorting.md) | Review |
| 3 | 이진 탐색 (Binary Search) | [Binary-Search.md](Binary-Search.md) | Draft |
| 4 | 분할 정복 (Divide & Conquer) | [Divide-and-Conquer.md](Divide-and-Conquer.md) | Draft |
| 5 | 그리디 (Greedy) | [Greedy.md](Greedy.md) | Draft |
| 6 | 백트래킹 (Backtracking) | [Backtracking.md](Backtracking.md) | Draft |

### 동적 프로그래밍

| Order | 주제 | 파일 | Status |
|---|---|---|---|
| 7 | DP 기초 | [DP-Basics.md](DP-Basics.md) | Draft |
| 8 | DP 최적화 | [DP-Optimization.md](DP-Optimization.md) | Draft |
| 9 | 비트마스크 DP | [Bitmask-DP.md](Bitmask-DP.md) | Draft |
| 10 | 트리 DP | [Tree-DP.md](Tree-DP.md) | Draft |

### 그래프 알고리즘

| Order | 주제 | 파일 | Status |
|---|---|---|---|
| 11 | BFS / DFS | [BFS-DFS.md](BFS-DFS.md) | Review |
| 12 | 위상 정렬 | [Topological-Sort.md](Topological-Sort.md) | Draft |
| 13 | 강한 연결 요소 (SCC) | [SCC.md](SCC.md) | Draft |
| 14 | 최단 경로 — Dijkstra | [Dijkstra.md](Dijkstra.md) | Draft |
| 15 | 최단 경로 — Bellman-Ford | [Bellman-Ford.md](Bellman-Ford.md) | Draft |
| 16 | 최단 경로 — Floyd-Warshall | [Floyd-Warshall.md](Floyd-Warshall.md) | Draft |
| 17 | 최소 신장 트리 (Kruskal / Prim) | [MST.md](MST.md) | Draft |

### 네트워크 플로우

| Order | 주제 | 파일 | Status |
|---|---|---|---|
| 18 | 최대 유량 (Ford-Fulkerson / Edmonds-Karp) | [Max-Flow.md](Max-Flow.md) | Draft |
| 19 | Dinic's Algorithm | [Dinic.md](Dinic.md) | Draft |
| 20 | 이분 매칭 | [Bipartite-Matching.md](Bipartite-Matching.md) | Draft |
| 21 | 최소 비용 최대 유량 (MCMF) | [MCMF.md](MCMF.md) | Draft |

### 문자열 알고리즘

| Order | 주제 | 파일 | Status |
|---|---|---|---|
| 22 | KMP | [KMP.md](KMP.md) | Draft |
| 23 | Z 알고리즘 | [Z-Algorithm.md](Z-Algorithm.md) | Draft |
| 24 | Rabin-Karp | [Rabin-Karp.md](Rabin-Karp.md) | Draft |
| 25 | Aho-Corasick | [Aho-Corasick.md](Aho-Corasick.md) | Draft |
| 26 | 서픽스 배열 | [Suffix-Array.md](Suffix-Array.md) | Draft |

### 수학적 알고리즘

| Order | 주제 | 파일 | Status |
|---|---|---|---|
| 27 | 정수론 & 소수 | [Number-Theory.md](Number-Theory.md) | Draft |
| 28 | 고속 거듭제곱 / 행렬 거듭제곱 | [Fast-Exponentiation.md](Fast-Exponentiation.md) | Draft |
| 29 | FFT / NTT | [FFT.md](FFT.md) | Draft |

### 고급 알고리즘 이론

| Order | 주제 | 파일 | Status |
|---|---|---|---|
| 30 | 분할 상환 분석 | [Amortized-Analysis.md](Amortized-Analysis.md) | Draft |
| 31 | 근사 알고리즘 | [Approximation-Algorithms.md](Approximation-Algorithms.md) | Draft |
| 32 | 랜덤 알고리즘 | [Randomized-Algorithms.md](Randomized-Algorithms.md) | Draft |
| 33 | 계산 기하학 | [Computational-Geometry.md](Computational-Geometry.md) | Draft |
| 34 | 병렬 알고리즘 | [Parallel-Algorithms.md](Parallel-Algorithms.md) | Draft |

---

## 학습 순서

현재 바로 읽을 수 있는 최소 경로:

```text
Complexity → Sorting → Binary-Search
       ↓
Data-Structures/Stack + Data-Structures/Queue + Data-Structures/Graph-Representation
       ↓
BFS-DFS
```

DP, 그리디, 백트래킹, 최단 경로는 이후 확장 주제다.

---

## 복잡도 클래스 빠른 참조

| 표기 | 이름 | 예시 |
|---|---|---|
| O(1) | 상수 | 해시 접근 |
| O(log n) | 로그 | 이진 탐색 |
| O(n) | 선형 | 배열 순회 |
| O(n log n) | 선형 로그 | 합병 정렬 |
| O(n²) | 이차 | 버블 정렬 |
| O(2ⁿ) | 지수 | 부분집합 열거 |

---

## 연관 섹션

- [Data-Structures/](../Data-Structures/) — 선수지식
- [CS-Theory/Computation-Theory/](../CS-Theory/Computation-Theory/) — P vs NP, 복잡도 클래스
- [Math/Discrete/](../Math/Discrete/) — 수학적 기반
