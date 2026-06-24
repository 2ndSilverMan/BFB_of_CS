# AVL 트리 (AVL Tree)

- Level: Intermediate
- Prerequisites: [Data-Structures/BST.md](BST.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

AVL 트리는 모든 노드에서 좌우 부분트리 높이 차이를 1 이하로 유지하는 자기 균형 이진 탐색 트리다. 삽입·삭제 후 회전으로 균형을 복구해, 탐색·삽입·삭제를 항상 `O(log n)`에 보장한다.

## 직관 (Intuition)

일반 BST는 정렬된 데이터를 넣으면 한쪽으로 치우쳐 연결 리스트처럼 퇴화해 `O(n)`이 된다. AVL은 "키가 너무 한쪽으로 기울면 회전으로 바로 펴 준다". 각 노드가 균형 정보를 들고 있다가, 불균형이 감지되면 국소적인 회전으로 즉시 높이를 낮춘다.

## 이론 (Theory)

각 노드의 **균형 인수(balance factor)** = (왼쪽 높이) − (오른쪽 높이) ∈ {−1, 0, 1}. 삽입/삭제로 이 값이 ±2가 되면 네 가지 경우로 회전한다.

- **LL**: 오른쪽 단일 회전
- **RR**: 왼쪽 단일 회전
- **LR**: 왼쪽-오른쪽 이중 회전
- **RL**: 오른쪽-왼쪽 이중 회전

AVL 트리의 높이는 $h\le 1.44\log_2(n+2)$로 묶여, 레드-블랙보다 더 빡빡하게 균형을 잡는다. 회전은 부분트리 구조를 바꾸되 중위 순회 순서(정렬 순서)를 보존한다.

## 구현 (Implementation)

```python
def rotate_right(y):
    x = y.left
    y.left = x.right
    x.right = y
    update_height(y); update_height(x)   # 높이 재계산
    return x                              # 새 부분트리 루트

def balance(node):
    bf = height(node.left) - height(node.right)
    if bf > 1:                            # 왼쪽 무거움
        if height(node.left.left) < height(node.left.right):
            node.left = rotate_left(node.left)   # LR
        return rotate_right(node)                # LL
    if bf < -1:                           # 오른쪽 무거움
        ...
    return node
```

## 복잡도 (Complexity)

| 연산 | 시간 |
|---|---|
| 탐색 | `O(log n)` |
| 삽입 | `O(log n)` |
| 삭제 | `O(log n)` |

공간은 `O(n)`. 회전은 각 삽입/삭제당 상수 개로 충분하다(삽입은 최대 1회 회전, 삭제는 루트까지 전파될 수 있으나 각 레벨 상수).

## 응용 (Applications)

- 빈번한 조회가 필요한 정렬된 집합·맵
- 데이터베이스·파일시스템 인덱스의 균형 트리 사촌
- 구간 통계가 필요한 순서 통계 트리
- 메모리 내 정렬 유지 컬렉션

## 흔한 오해 (Common Misunderstandings)

- AVL과 레드-블랙은 둘 다 `O(log n)`이지만, AVL이 더 엄격해 조회는 빠르고 삽입/삭제는 회전이 잦다.
- 회전은 정렬 순서를 망가뜨리지 않는다.
- 균형 인수는 높이 차이지, 노드 수 차이가 아니다.
- 자기 균형이라도 디스크 기반 대용량에는 B-트리가 더 적합하다.

## TMI

- AVL은 1962년 고안자 Adelson-Velsky와 Landis의 이름 약자다 — 최초의 자기 균형 트리.
- 표준 라이브러리의 정렬 맵(예: C++ `std::map`)은 보통 레드-블랙을 쓰지만, 조회 위주 워크로드엔 AVL이 유리할 수 있다.
- 회전은 포인터 몇 개만 바꾸는 국소 연산이라 비용이 작다.

## 연습 / 확인 문제 (Exercises)

- 1,2,3을 순서대로 삽입할 때 발생하는 불균형과 회전을 그려라.
- LR 회전이 필요한 삽입 시퀀스를 만들어라.
- AVL과 일반 BST에 정렬된 1..n을 넣었을 때 높이를 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [이진 탐색 트리 (BST)](BST.md)
- 다음: [레드-블랙 트리](Red-Black-Tree.md), [Systems/Databases/Indexes-and-B-Tree.md](../Systems/Databases/Indexes-and-B-Tree.md)

## 참조 (References)

- [Data-Structures/BST.md](BST.md)
- [Data-Structures/Red-Black-Tree.md](Red-Black-Tree.md)
- [Reference/Books.md](../Reference/Books.md)
