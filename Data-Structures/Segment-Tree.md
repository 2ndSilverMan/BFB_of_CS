# 세그먼트 트리 (Segment Tree)

- Level: Advanced
- Prerequisites: [Data-Structures/Array.md](Array.md), [Data-Structures/Binary-Tree.md](Binary-Tree.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

세그먼트 트리는 배열의 **구간 질의(합·min·max·gcd…)와 갱신을 모두 $O(\log n)$** 에 처리하는 이진 트리다. 각 노드가 한 구간을 담당하고, 부모는 두 자식 구간을 **결합(merge)** 한 값을 저장한다.

## 직관 (Intuition)

매번 구간을 더하면 질의가 $O(n)$, 누적합을 쓰면 갱신이 $O(n)$ — 둘 다 한쪽이 느리다. 세그먼트 트리는 구간을 **절반씩 쪼개 미리 합쳐** 둔다. 임의 구간은 이 미리 계산된 조각 $O(\log n)$ 개로 조립되고, 한 값이 바뀌면 그 값을 포함하는 루트까지의 경로 노드만 다시 결합한다.

## 이론 (Theory)

### 1. 모노이드 요구

결합 연산 $\oplus$ 는 **결합법칙**과 **항등원**을 가진 모노이드여야 한다(합·min·max·gcd·OR…). 평균은 그대로는 안 되지만 `(합, 개수)`를 저장하면 모노이드가 되어 가능하다 — *상태를 결합 가능하게 설계*하는 게 요령.

### 2. 질의가 $O(\log n)$ 인 이유 (canonical cover)

질의 `[l, r]`는 루트에서 내려가며 **완전히 포함된 노드는 즉시 채택**, 걸친 노드만 양쪽 재귀한다. 각 레벨에서 "걸친" 노드는 좌·우 경계 각 1개씩 **최대 2개**뿐이라, 채택·방문 노드가 레벨당 $O(1)$ → 전체 $O(\log n)$. 점 갱신도 리프→루트 한 경로($O(\log n)$).

### 3. 구간 갱신과 lazy propagation

"구간 [l,r]에 +v"를 매 원소에 적용하면 $O(n)$. 대신 노드에 **미룬 갱신(lazy tag)** 을 달아 두고, 그 서브트리로 더 내려갈 때 비로소 자식에 밀어 내린다(push-down). 질의·갱신 모두 $O(\log n)$ 유지.

## 구현 (Implementation)

반복적(iterative) 합 세그먼트 트리 — 짧고 빠름:

```python
class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.t = [0]*self.n + list(arr)        # 리프는 뒤쪽 [n, 2n)
        for i in range(self.n - 1, 0, -1):     # 내부 노드 = 두 자식 합
            self.t[i] = self.t[2*i] + self.t[2*i+1]

    def update(self, i, val):                  # arr[i] = val
        i += self.n; self.t[i] = val
        while i > 1:
            i >>= 1
            self.t[i] = self.t[2*i] + self.t[2*i+1]

    def query(self, l, r):                     # 합 [l, r)
        l += self.n; r += self.n; s = 0
        while l < r:
            if l & 1: s += self.t[l]; l += 1   # l이 오른쪽 자식이면 채택
            if r & 1: r -= 1; s += self.t[r]   # r이 오른쪽 자식이면 한 칸 당겨 채택
            l >>= 1; r >>= 1
        return s
```

min 트리로 바꾸려면 `+`를 `min`으로, 초기 누적값을 $+\infty$ 로 바꾸면 된다(모노이드만 교체).

## 복잡도 (Complexity)

| 연산 | 시간 | 공간 |
|---|---|---|
| 구축 | $O(n)$ | $2n$(반복) ~ $4n$(재귀) |
| 점 갱신 | $O(\log n)$ | — |
| 구간 질의 | $O(\log n)$ | — |
| 구간 갱신(lazy) | $O(\log n)$ | lazy 배열 추가 |

**워크드 예제.** 길이 8 합 트리에서 `query(2,6)`(반열린 [2,6)): 리프 인덱스 `l=10, r=14`. `l` 짝→스킵, `r` 짝→스킵, 올라가서 `l=5,r=7`; `l` 홀→t[5] 채택 l=6, `r` 홀→r=6 t[6] 채택; `l=3,r=3` 종료. 두 노드 t[5],t[6]만 더해 $O(\log n)$.

## 응용 (Applications)

- 구간 합/최소/최대 + 갱신, 경쟁 프로그래밍의 구간 처리.
- 좌표 압축과 결합한 구간 카운팅, 2D 확장(영역 질의).
- persistent 세그먼트 트리: 과거 버전 보존 → "k번째 작은 수" 류.

## 흔한 오해 (Common Misunderstandings)

- **누적합과 다르다** — 누적합은 갱신 $O(n)$, 세그먼트 트리는 $O(\log n)$.
- **결합 연산은 결합법칙을 만족해야** 한다(평균은 `(합,개수)`로 재설계 필요).
- **구간 갱신은 lazy propagation 없이는 $O(n)$**.
- **[펜윅 트리](Fenwick-Tree.md)가 구간 합엔 더 간단**하지만, 세그먼트 트리가 min/max 등으로 더 일반적이다.

## TMI

- 반복적(상향식) 세그먼트 트리는 재귀형보다 상수배 빠르고 코드가 짧아 경쟁 프로그래밍에서 인기다.
- lazy propagation은 "필요할 때까지 미룬다"는 [게으른 평가](../Engineering/Performance/Lazy-Evaluation.md)의 자료구조판이다.
- persistent 세그먼트 트리는 갱신마다 바뀐 $O(\log n)$ 노드만 새로 만들고 나머지는 공유한다 — [스냅샷의 redirect-on-write](../Engineering/DevOps/Server-Images-and-Snapshots.md)와 같은 발상.

## 연습 / 확인 문제 (Exercises)

- 길이 8 합 세그먼트 트리를 그리고 `query(2,6)` 경로(위 예제)를 표시하라.
- min 세그먼트 트리로 바꾸려면 어디를 고쳐야 하는지(모노이드·항등원) 적어라.
- "구간 +v, 구간 합" 을 lazy propagation으로 설계하고 push-down 시점을 설명하라.
- 누적합·펜윅·세그먼트 트리의 갱신/질의 비용과 일반성을 표로 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [이진 트리](Binary-Tree.md)
- 다음: [펜윅 트리 (BIT)](Fenwick-Tree.md)
- 관련: [동적 계획법 기초](../Algorithms/DP-Basics.md)

## 참조 (References)

- [Data-Structures/Fenwick-Tree.md](Fenwick-Tree.md)
- [Data-Structures/Array.md](Array.md)
- [Data-Structures/Binary-Tree.md](Binary-Tree.md)
- [Reference/Books.md](../Reference/Books.md)
