# 자료구조 (Data Structures)

> 데이터를 효율적으로 저장하고 접근하는 방법.

**선수지식**: [Programming/](../Programming/) — 변수, 조건문, 반복문, 함수, 배열/문자열

---

## 읽는 법

- 링크가 걸린 `Draft` 문서는 지금 읽을 수 있는 초안이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

### 선형 구조

| 주제 | 파일 | 설명 | Status |
|---|---|---|---|
| 배열 (Array) | [Array.md](Array.md) | 고정 크기, O(1) 접근 | Draft |
| 연결 리스트 (Linked List) | [Linked-List.md](Linked-List.md) | 동적 크기, O(n) 접근 | Draft |
| 스택 (Stack) | [Stack.md](Stack.md) | LIFO | Draft |
| 큐 (Queue) | [Queue.md](Queue.md) | FIFO | Draft |
| 덱 (Deque) | Deque.md | 양방향 큐 | Planned |

### 트리 구조

| 주제 | 파일 | 설명 | Status |
|---|---|---|---|
| 이진 트리 (Binary Tree) | [Binary-Tree.md](Binary-Tree.md) | 계층 구조의 기본 | Draft |
| 이진 탐색 트리 (BST) | BST.md | O(log n) 탐색 (균형 시) | Planned |
| AVL 트리 | AVL-Tree.md | 자기 균형 BST | Planned |
| 레드-블랙 트리 | Red-Black-Tree.md | 자기 균형 BST (실용) | Planned |
| 힙 (Heap) | Heap.md | 우선순위 큐 구현 | Planned |
| 트라이 (Trie) | Trie.md | 문자열 탐색 특화 | Planned |
| 세그먼트 트리 | Segment-Tree.md | 구간 쿼리 | Planned |
| 펜윅 트리 (BIT) | Fenwick-Tree.md | 구간 합 쿼리 | Planned |

### 그래프

| 주제 | 파일 | 설명 | Status |
|---|---|---|---|
| 그래프 표현 | [Graph-Representation.md](Graph-Representation.md) | 인접 행렬 vs 인접 리스트 | Draft |
| 유니온-파인드 (DSU) | Union-Find.md | 집합 합병 및 탐색 | Planned |

### 해시

| 주제 | 파일 | 설명 | Status |
|---|---|---|---|
| 해시 테이블 | [Hash-Table.md](Hash-Table.md) | 평균 O(1) 접근 | Draft |
| 해시 함수 | Hash-Function.md | 충돌 처리 전략 | Planned |

---

## 학습 순서

현재 바로 읽을 수 있는 최소 경로:

```text
Array → Linked-List
   ↓        ↓
 Stack    Queue
      ↘   ↙
 Graph-Representation → Algorithms/BFS-DFS
```

트리와 해시는 입문자 로드맵 최종 완료 기준을 채우기 위한 다음 확장 주제다. 유니온-파인드는 알고리즘 확장 경로에서 다룬다.

---

## 복잡도 요약

| 구조 | 접근 | 탐색 | 삽입 | 삭제 |
|---|---|---|---|---|
| 배열 | O(1) | O(n) | O(n) | O(n) |
| 연결 리스트 | O(n) | O(n) | O(1)* | O(1)* |
| 스택 | O(1)** | O(n) | O(1) | O(1) |
| 큐 | O(1)** | O(n) | O(1) | O(1) |
| BST (균형) | — | O(log n) | O(log n) | O(log n) |
| 해시 테이블 | — | O(1)* | O(1)* | O(1)* |
| 힙 | — | — | O(log n) | O(log n) |

*해시 테이블은 평균 기준. 연결 리스트 삽입/삭제는 해당 위치의 노드를 이미 알고 있을 때 기준.
**스택은 top, 큐는 front 기준 접근.

---

## 연관 섹션

- [Algorithms/](../Algorithms/) — 자료구조 위에서 동작하는 알고리즘
- [Programming/](../Programming/) — 선수지식
