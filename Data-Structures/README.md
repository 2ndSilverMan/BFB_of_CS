# 자료구조 (Data Structures)

> 데이터를 효율적으로 저장하고 접근하는 방법.

**선수지식**: [Programming/](../Programming/) — 배열, 포인터, 재귀

---

## 주제 목록

### 선형 구조

| 주제 | 파일 | 특징 | Status |
|---|---|---|---|
| 배열 (Array) | Array.md | 고정 크기, O(1) 접근 | Planned |
| 연결 리스트 (Linked List) | Linked-List.md | 동적 크기, O(n) 접근 | Planned |
| 스택 (Stack) | Stack.md | LIFO | Planned |
| 큐 (Queue) | Queue.md | FIFO | Planned |
| 덱 (Deque) | Deque.md | 양방향 큐 | Planned |

### 트리 구조

| 주제 | 파일 | 특징 | Status |
|---|---|---|---|
| 이진 트리 (Binary Tree) | Binary-Tree.md | 계층 구조의 기본 | Planned |
| 이진 탐색 트리 (BST) | BST.md | O(log n) 탐색 (균형 시) | Planned |
| AVL 트리 | AVL-Tree.md | 자기 균형 BST | Planned |
| 레드-블랙 트리 | Red-Black-Tree.md | 자기 균형 BST (실용) | Planned |
| 힙 (Heap) | Heap.md | 우선순위 큐 구현 | Planned |
| 트라이 (Trie) | Trie.md | 문자열 탐색 특화 | Planned |
| 세그먼트 트리 | Segment-Tree.md | 구간 쿼리 | Planned |
| 펜윅 트리 (BIT) | Fenwick-Tree.md | 구간 합 쿼리 | Planned |

### 그래프

| 주제 | 파일 | 특징 | Status |
|---|---|---|---|
| 그래프 표현 | Graph-Representation.md | 인접 행렬 vs 인접 리스트 | Planned |
| 유니온-파인드 (DSU) | Union-Find.md | 집합 합병 및 탐색 | Planned |

### 해시

| 주제 | 파일 | 특징 | Status |
|---|---|---|---|
| 해시 테이블 | Hash-Table.md | 평균 O(1) 접근 | Planned |
| 해시 함수 | Hash-Function.md | 충돌 처리 전략 | Planned |

---

## 복잡도 요약

| 구조 | 접근 | 탐색 | 삽입 | 삭제 |
|---|---|---|---|---|
| 배열 | O(1) | O(n) | O(n) | O(n) |
| 연결 리스트 | O(n) | O(n) | O(1) | O(1) |
| BST (균형) | — | O(log n) | O(log n) | O(log n) |
| 해시 테이블 | — | O(1)* | O(1)* | O(1)* |
| 힙 | — | — | O(log n) | O(log n) |

*평균 기준

---

## 연관 섹션

- [Algorithms/](../Algorithms/) — 자료구조 위에서 동작하는 알고리즘
- [Programming/](../Programming/) — 선수지식
