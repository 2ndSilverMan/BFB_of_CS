# 레드-블랙 트리 (Red-Black Tree)

- Level: Advanced
- Prerequisites: [Data-Structures/BST.md](BST.md), [Data-Structures/AVL-Tree.md](AVL-Tree.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

레드-블랙 트리는 노드에 **빨강/검정** 색을 부여하고 색 규칙으로 "대충 균형"을 유지하는 자기 균형 [BST](BST.md)다. [AVL](AVL-Tree.md)보다 느슨히 균형 잡아 **삽입·삭제당 회전이 상수 개**라, 표준 라이브러리의 정렬 맵/셋(C++ `std::map`, Java `TreeMap`)에 널리 쓰인다.

## 직관 (Intuition)

완벽 균형(AVL)을 고집하면 갱신마다 회전이 잦다. 레드-블랙은 "**가장 긴 경로가 가장 짧은 경로의 2배를 넘지 않게**"만 색으로 강제한다. 높이는 여전히 $O(\log n)$ 이면서 재조정 비용은 줄어 — 읽기·쓰기 균형이 좋다.

## 이론 (Theory)

### 1. 다섯 불변식

1. 모든 노드는 빨강 또는 검정.
2. 루트는 검정.
3. 모든 리프(NIL 센티넬)는 검정.
4. **빨강 노드의 자식은 검정**(빨강이 연속 불가).
5. 임의 노드에서 자손 리프까지 경로의 **검정 노드 수(black-height, `bh`)가 모두 같다**.

### 2. 높이 경계 $\le 2\log_2(n+1)$ 증명

불변식 5로 모든 루트→리프 경로의 검정 수가 같고(`bh`), 불변식 4로 빨강은 연속될 수 없어 어떤 경로든 빨강이 절반을 넘지 못한다 → 실제 높이 $h \le 2\,bh$. 한편 귀납으로 "`bh`가 $b$ 인 서브트리의 내부 노드 수 $\ge 2^{b}-1$" 이 성립하므로 $n \ge 2^{bh}-1$, 즉 $bh \le \log_2(n+1)$. 둘을 합치면

$$h \le 2\,bh \le 2\log_2(n+1)$$

### 3. 삽입 회복(insert-fixup)의 3경우

새 노드는 **빨강**으로 넣는다(불변식 5를 안 깨려고). 부모도 빨강이면 4 위반 → **삼촌(uncle) 색**으로 분기:

| 경우 | 삼촌 | 처리 |
|---|---|---|
| 1 | 빨강 | 부모·삼촌을 검정, 조부모를 빨강으로 **재색칠** 후 조부모에서 위로 반복 |
| 2 | 검정, 꺾임(triangle) | 부모에서 회전해 직선(case 3)으로 변환 |
| 3 | 검정, 직선(line) | 조부모에서 회전 + 재색칠 → 종료 |

case 1은 위로 전파될 수 있어 재색칠은 $O(\log n)$ 번이지만, **회전은 전체 2회 이하**. 삭제는 "double-black"을 밀어 올리며 해소하는 더 복잡한 로직이나 회전은 역시 3회 이하다.

### 4. 2-3-4 트리와의 동형

레드-블랙은 **2-3-4 트리([B-트리](../Systems/Databases/Indexes-and-B-Tree.md)의 일종)와 동형**이다. 검정 노드 + 그에 매달린 빨강 자식들이 2-3-4 노드 하나에 대응한다 — 색 규칙이 사실은 B-트리 노드를 이진으로 흉내 낸 것.

## 구현 (Implementation)

```python
RED, BLACK = 0, 1

def insert_fixup(T, z):                 # z: 방금 삽입한 빨강 노드
    while z.parent.color == RED:
        gp = z.parent.parent
        if z.parent is gp.left:
            uncle = gp.right
            if uncle.color == RED:                  # 경우1: 재색칠
                z.parent.color = uncle.color = BLACK
                gp.color = RED
                z = gp
            else:
                if z is z.parent.right:             # 경우2: 꺾임→직선
                    z = z.parent
                    left_rotate(T, z)
                z.parent.color = BLACK              # 경우3: 회전+재색칠
                gp.color = RED
                right_rotate(T, gp)
        else:
            ...                                     # 좌우 대칭
    T.root.color = BLACK                            # 불변식 2 복구
```

## 복잡도 (Complexity)

| 연산 | 시간 | 회전 |
|---|---|---|
| 탐색 | $O(\log n)$ | — |
| 삽입 | $O(\log n)$ | ≤ 2 |
| 삭제 | $O(\log n)$ | ≤ 3 |

노드당 **색 비트 1개**만 추가. AVL 대비 회전이 적어 갱신 잦은 워크로드에 유리하고, 경로가 약간 길어 조회는 미세하게 느릴 수 있다.

## 응용 (Applications)

- C++ `std::map`/`std::set`, Java `TreeMap`/`TreeSet`.
- 리눅스 커널: CFS 스케줄러의 런큐, 가상 메모리 영역(VMA) 관리, `epoll`.
- 순서 통계·구간 트리의 균형 기반.

## 흔한 오해 (Common Misunderstandings)

- **"더 적은 회전"이지 "회전 없음"이 아니다** — 삽입/삭제 모두 회전 가능.
- **black-height는 노드 높이가 아니라 경로의 검정 노드 수**.
- **레드-블랙이 AVL보다 항상 빠르지 않다** — 조회 위주면 AVL이 유리.
- **색은 의미가 없다** — 균형용 보조 비트일 뿐.

## TMI

- 1972년 Rudolf Bayer의 "대칭 이진 B-트리"가 원형이고, 1978년 Guibas·Sedgewick이 빨강/검정 색으로 재정식화했다.
- **삭제 회복은 악명 높게 복잡**해 많은 교과서가 삽입만 자세히 다룬다 — Sedgewick의 **좌편향(left-leaning) 레드-블랙**은 경우를 줄여 구현을 단순화하려는 변형이다.
- "왜 하필 2색?" — 2-3-4 트리의 노드(2·3·4-노드)를 이진 + 1비트로 인코딩하는 데 색 하나면 충분하기 때문.

## 연습 / 확인 문제 (Exercises)

- 다섯 불변식이 높이 $O(\log n)$ 을 어떻게 보장하는지 위 증명을 따라 적어라.
- 삼촌이 빨강일 때(재색칠)와 검정일 때(회전)의 처리 차이를 그림으로 비교하라.
- 같은 삽입 순서에 대해 AVL과 레드-블랙의 회전 횟수를 비교하라.
- 작은 레드-블랙 트리를 대응하는 2-3-4 트리로 변환해 동형을 확인하라.

## 이어서 읽기 (Reading Path)

- 이전: [AVL 트리](AVL-Tree.md)
- 다음: [B-트리와 인덱스](../Systems/Databases/Indexes-and-B-Tree.md)
- 관련: [이진 탐색 트리](BST.md)

## 참조 (References)

- [Data-Structures/AVL-Tree.md](AVL-Tree.md)
- [Data-Structures/BST.md](BST.md)
- [Systems/Databases/Indexes-and-B-Tree.md](../Systems/Databases/Indexes-and-B-Tree.md)
- [Reference/Books.md](../Reference/Books.md)
