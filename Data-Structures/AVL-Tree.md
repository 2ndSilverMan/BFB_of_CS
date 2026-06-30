# AVL 트리 (AVL Tree)

- Level: Intermediate
- Prerequisites: [Data-Structures/BST.md](BST.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

AVL 트리는 모든 노드에서 **좌우 서브트리 높이 차를 1 이하로** 유지하는 자기 균형 [BST](BST.md)다. 삽입·삭제 후 **회전(rotation)** 으로 균형을 즉시 복구해 탐색·삽입·삭제를 항상 $O(\log n)$ 으로 보장한다. 최초(1962)의 자기 균형 트리다.

## 직관 (Intuition)

일반 BST는 정렬 입력에서 한 줄로 퇴화해 $O(n)$ 이 된다([BST](BST.md)의 약점). AVL은 "한쪽으로 너무 기울면 **국소 회전으로 즉시 펴 준다**". 각 노드가 균형 정보를 들고 있다가 ±2가 되는 순간, 포인터 몇 개만 바꾸는 상수 시간 회전으로 높이를 낮춘다.

## 이론 (Theory)

### 1. 균형 인수와 4가지 회전

**균형 인수(balance factor)** = (왼쪽 높이) − (오른쪽 높이) ∈ {−1, 0, 1}. 삽입/삭제로 ±2가 되면 불균형 패턴에 따라 회전한다.

| 패턴 | 모양 | 복구 |
|---|---|---|
| LL | 왼쪽-왼쪽 직선 | 오른쪽 단일 회전 |
| RR | 오른쪽-오른쪽 직선 | 왼쪽 단일 회전 |
| LR | 왼쪽-오른쪽 꺾임 | 왼쪽→오른쪽 이중 회전 |
| RL | 오른쪽-왼쪽 꺾임 | 오른쪽→왼쪽 이중 회전 |

RR 단일 회전(왼쪽 회전)의 구조 변화 — **중위(정렬) 순서는 보존**된다:

```text
   x                 y
    \               / \
     y     →       x   z
      \
       z
```

### 2. 높이 경계가 $O(\log n)$ 인 증명 (피보나치)

높이 $h$ 인 AVL이 가질 수 있는 **최소 노드 수** $N(h)$ 는 한쪽이 $h-1$, 다른 쪽이 $h-2$ 일 때이므로

$$N(h) = N(h-1) + N(h-2) + 1,\quad N(0)=1,\ N(1)=2$$

이는 피보나치와 $N(h)=F(h+3)-1$ 로 연결되고, $F(h)\sim \varphi^h/\sqrt5$ ($\varphi=\tfrac{1+\sqrt5}{2}$) 이므로

$$h \le \log_\varphi(n) \approx 1.44\,\log_2 n$$

즉 AVL 높이는 완전 균형($\log_2 n$)의 1.44배 이내로, 레드-블랙($2\log_2 n$)보다 빡빡하다.

### 3. 회전 횟수 비대칭

**삽입**은 첫 불균형 노드에서 단일/이중 회전 1번이면 전체 높이가 복구된다(상수). **삭제**는 회전이 루트까지 전파될 수 있어 최대 $O(\log n)$ 번 — 이 비대칭이 "쓰기 잦으면 레드-블랙" 논거의 핵심이다.

## 구현 (Implementation)

```python
def height(n): return n.h if n else 0
def update(n): n.h = 1 + max(height(n.left), height(n.right))
def bf(n):     return height(n.left) - height(n.right)

def rotate_right(y):
    x = y.left
    y.left, x.right = x.right, y
    update(y); update(x)           # 아래쪽(y) 먼저 갱신
    return x                        # 새 서브트리 루트

def rotate_left(x):
    y = x.right
    x.right, y.left = y.left, x
    update(x); update(y)
    return y

def rebalance(n):
    update(n)
    if bf(n) > 1:                          # 왼쪽 무거움
        if bf(n.left) < 0:
            n.left = rotate_left(n.left)    # LR
        return rotate_right(n)              # LL
    if bf(n) < -1:                         # 오른쪽 무거움
        if bf(n.right) > 0:
            n.right = rotate_right(n.right) # RL
        return rotate_left(n)              # RR
    return n
```

삽입은 일반 BST 삽입 뒤, 되돌아오는 경로마다 `rebalance`를 호출하면 된다.

## 복잡도 (Complexity)

| 연산 | 시간 | 회전 |
|---|---|---|
| 탐색 | $O(\log n)$ | — |
| 삽입 | $O(\log n)$ | 단일/이중 1회 |
| 삭제 | $O(\log n)$ | 최대 $O(\log n)$ 회 |

공간 $O(n)$, 노드당 높이(또는 균형 인수) 필드 추가. **워크드 예제.** 빈 트리에 `1,2,3` 삽입: 3 삽입 직후 루트 1의 균형 인수 −2(RR) → 1에서 왼쪽 회전 → 2가 루트, 1·3이 자식. 높이 2→1로 복구.

## 응용 (Applications)

- **조회가 압도적으로 잦은** 정렬 집합·맵(빡빡한 균형 → 짧은 경로).
- 순서 통계 트리(서브트리 크기 증강 → select/rank, [BST](BST.md) 참고).
- 인메모리 정렬 인덱스. 디스크 대용량은 [B-트리](../Systems/Databases/Indexes-and-B-Tree.md)가 더 적합.

## 흔한 오해 (Common Misunderstandings)

- **AVL과 레드-블랙 둘 다 $O(\log n)$** 이지만, AVL이 더 엄격해 **조회는 빠르고 삽입/삭제 회전은 잦다**.
- **회전은 정렬 순서를 망가뜨리지 않는다** — 중위 순회 불변.
- **균형 인수는 높이 차이지 노드 수 차이가 아니다**.
- 자기 균형이라도 **디스크 기반 대용량엔 B-트리**가 낫다(노드당 키가 많아 트리 높이가 더 낮음).

## TMI

- AVL은 고안자 **A**delson-**V**elsky·**L**andis(1962)의 머리글자다.
- 회전은 포인터 3~5개만 바꾸는 국소 연산이라 비용이 작다 — 비싼 건 균형 *판단*이 아니라 회전이 *전파*될 때.
- 높이 필드 대신 균형 인수(2비트)만 저장하면 메모리를 아끼지만 갱신 로직이 까다로워진다.

## 연습 / 확인 문제 (Exercises)

- `1,2,3`을 순서대로 삽입할 때 불균형과 회전을 그려라(위 워크드 예제 확장).
- LR 회전이 필요한 최소 삽입 시퀀스를 만들어라.
- AVL과 일반 BST에 정렬된 `1..n`을 넣었을 때 높이를 비교하라.
- $N(h)=N(h-1)+N(h-2)+1$ 로 $N(0..5)$ 를 계산하고 피보나치와의 관계를 확인하라.

## 이어서 읽기 (Reading Path)

- 이전: [이진 탐색 트리 (BST)](BST.md)
- 다음: [레드-블랙 트리](Red-Black-Tree.md)
- 관련: [B-트리와 인덱스](../Systems/Databases/Indexes-and-B-Tree.md)

## 참조 (References)

- [Data-Structures/BST.md](BST.md)
- [Data-Structures/Red-Black-Tree.md](Red-Black-Tree.md)
- [Systems/Databases/Indexes-and-B-Tree.md](../Systems/Databases/Indexes-and-B-Tree.md)
- [Reference/Books.md](../Reference/Books.md)
