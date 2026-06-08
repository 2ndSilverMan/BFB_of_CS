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
| 4 | 분할 정복 (Divide & Conquer) | Divide-and-Conquer.md | Planned |
| 5 | 그리디 (Greedy) | Greedy.md | Planned |
| 6 | 백트래킹 (Backtracking) | Backtracking.md | Planned |

### 동적 프로그래밍

| Order | 주제 | 파일 | Status |
|---|---|---|---|
| 7 | DP 기초 | DP-Basics.md | Planned |
| 8 | DP 최적화 | DP-Optimization.md | Planned |
| 9 | 비트마스크 DP | Bitmask-DP.md | Planned |
| 10 | 트리 DP | Tree-DP.md | Planned |

### 그래프 알고리즘

| Order | 주제 | 파일 | Status |
|---|---|---|---|
| 11 | BFS / DFS | [BFS-DFS.md](BFS-DFS.md) | Review |
| 12 | 위상 정렬 | Topological-Sort.md | Planned |
| 13 | 강한 연결 요소 (SCC) | SCC.md | Planned |
| 14 | 최단 경로 — Dijkstra | Dijkstra.md | Planned |
| 15 | 최단 경로 — Bellman-Ford | Bellman-Ford.md | Planned |
| 16 | 최단 경로 — Floyd-Warshall | Floyd-Warshall.md | Planned |
| 17 | 최소 신장 트리 (Kruskal / Prim) | MST.md | Planned |

### 네트워크 플로우

| Order | 주제 | 파일 | Status |
|---|---|---|---|
| 18 | 최대 유량 (Ford-Fulkerson / Edmonds-Karp) | Max-Flow.md | Planned |
| 19 | Dinic's Algorithm | Dinic.md | Planned |
| 20 | 이분 매칭 | Bipartite-Matching.md | Planned |
| 21 | 최소 비용 최대 유량 (MCMF) | MCMF.md | Planned |

### 문자열 알고리즘

| Order | 주제 | 파일 | Status |
|---|---|---|---|
| 22 | KMP | KMP.md | Planned |
| 23 | Z 알고리즘 | Z-Algorithm.md | Planned |
| 24 | Rabin-Karp | Rabin-Karp.md | Planned |
| 25 | Aho-Corasick | Aho-Corasick.md | Planned |
| 26 | 서픽스 배열 | Suffix-Array.md | Planned |

### 수학적 알고리즘

| Order | 주제 | 파일 | Status |
|---|---|---|---|
| 27 | 정수론 & 소수 | Number-Theory.md | Planned |
| 28 | 고속 거듭제곱 / 행렬 거듭제곱 | Fast-Exponentiation.md | Planned |
| 29 | FFT / NTT | FFT.md | Planned |

### 고급 알고리즘 이론

| Order | 주제 | 파일 | Status |
|---|---|---|---|
| 30 | 분할 상환 분석 | Amortized-Analysis.md | Planned |
| 31 | 근사 알고리즘 | Approximation-Algorithms.md | Planned |
| 32 | 랜덤 알고리즘 | Randomized-Algorithms.md | Planned |
| 33 | 계산 기하학 | Computational-Geometry.md | Planned |
| 34 | 병렬 알고리즘 | Parallel-Algorithms.md | Planned |

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
