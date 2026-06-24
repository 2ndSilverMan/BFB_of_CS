# 레드-블랙 트리 (Red-Black Tree)

- Level: Advanced
- Prerequisites: [Data-Structures/BST.md](BST.md), [Data-Structures/AVL-Tree.md](AVL-Tree.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

레드-블랙 트리는 노드에 빨강/검정 색을 부여하고 색 규칙으로 균형을 유지하는 자기 균형 이진 탐색 트리다. AVL보다 느슨하게 균형을 잡아 삽입·삭제 시 회전이 적어, 표준 라이브러리의 정렬 맵/셋에 널리 쓰인다.

## 직관 (Intuition)

완벽한 균형을 고집하면(AVL) 갱신할 때마다 회전이 많아진다. 레드-블랙은 "대충 균형"을 색 규칙으로 보장한다. 가장 긴 경로가 가장 짧은 경로의 2배를 넘지 않도록만 묶으면, 높이는 여전히 `O(log n)`이면서 삽입/삭제의 재조정 비용은 줄어든다.

## 이론 (Theory)

다섯 가지 불변식:

1. 모든 노드는 빨강 또는 검정.
2. 루트는 검정.
3. 모든 리프(NIL)는 검정.
4. 빨강 노드의 자식은 검정(빨강이 연속될 수 없음).
5. 임의 노드에서 자손 리프까지 경로의 검정 노드 수(black-height)는 모두 같다.

이 규칙들로 최장 경로 $\le 2\times$ 최단 경로가 보장되어 높이 $\le 2\log_2(n+1)$. 삽입·삭제는 색 변경(recoloring)과 회전으로 불변식을 복구하며, 각각 상수 개의 회전으로 끝난다.

## 구현 (Implementation)

```python
# 삽입 후 회복(개념): 빨강-빨강 위반 처리
def insert_fixup(T, z):
    while z.parent.color == RED:
        uncle = sibling_of_parent(z)
        if uncle.color == RED:            # 경우1: 색만 바꿈
            z.parent.color = BLACK
            uncle.color = BLACK
            z.grandparent.color = RED
            z = z.grandparent
        else:                             # 경우2/3: 회전 + 재색칠
            z = rotate_and_recolor(T, z)
    T.root.color = BLACK
```

## 복잡도 (Complexity)

| 연산 | 시간 |
|---|---|
| 탐색 | `O(log n)` |
| 삽입 | `O(log n)` (상수 회전) |
| 삭제 | `O(log n)` (상수 회전) |

공간은 노드당 색 비트 1개 추가. AVL 대비 회전이 적어 갱신이 잦은 워크로드에 유리하고, 조회는 약간 느릴 수 있다.

## 응용 (Applications)

- C++ `std::map`/`std::set`, Java `TreeMap`/`TreeSet`
- 리눅스 커널의 스케줄러·메모리 영역 관리
- 순서 통계·구간 트리의 기반
- 정렬 유지가 필요한 인메모리 인덱스

## 흔한 오해 (Common Misunderstandings)

- "더 적은 회전"이지 "회전 없음"은 아니다. 삽입/삭제 모두 회전이 가능하다.
- black-height는 노드 자체 높이가 아니라 경로의 검정 노드 수다.
- 레드-블랙이 AVL보다 항상 빠르지 않다. 조회 위주면 AVL이 유리하다.
- 색은 의미가 아니라 균형을 위한 보조 정보일 뿐이다.

## TMI

- 레드-블랙 트리는 2-3-4 트리(B-트리의 일종)와 동형으로 해석할 수 있다.
- 원래 1972년 "대칭 이진 B-트리"로 발표됐다가 1978년 빨강/검정 색으로 재정식화됐다.
- 삭제의 회복 로직은 악명 높게 복잡해, 많은 교과서가 삽입만 자세히 다룬다.

## 연습 / 확인 문제 (Exercises)

- 다섯 불변식이 어떻게 높이 `O(log n)`을 보장하는지 설명하라.
- 빨강-빨강 위반에서 삼촌이 빨강일 때와 검정일 때의 처리 차이를 비교하라.
- 같은 삽입 순서에 대해 AVL과 레드-블랙의 회전 횟수를 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [AVL 트리](AVL-Tree.md)
- 다음: [Systems/Databases/Indexes-and-B-Tree.md](../Systems/Databases/Indexes-and-B-Tree.md)

## 참조 (References)

- [Data-Structures/AVL-Tree.md](AVL-Tree.md)
- [Systems/Databases/Indexes-and-B-Tree.md](../Systems/Databases/Indexes-and-B-Tree.md)
- [Reference/Books.md](../Reference/Books.md)
