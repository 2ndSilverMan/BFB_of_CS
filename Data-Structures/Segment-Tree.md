# 세그먼트 트리 (Segment Tree)

- Level: Advanced
- Prerequisites: [Data-Structures/Array.md](Array.md), [Data-Structures/Binary-Tree.md](Binary-Tree.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

세그먼트 트리는 배열의 구간 질의(합, 최소, 최대 등)와 점 갱신을 모두 `O(log n)`에 처리하는 트리 자료구조다. 각 노드가 한 구간을 담당하며, 부모는 두 자식 구간을 합친 결과를 저장한다.

## 직관 (Intuition)

"구간 [l, r]의 합"을 매번 더하면 `O(n)`이고, 미리 다 더해 두면 갱신이 `O(n)`이다. 세그먼트 트리는 구간을 절반씩 쪼개 트리로 미리 합쳐 둔다. 임의 구간은 이 미리 계산된 조각 `O(log n)`개로 조립되고, 한 값이 바뀌면 그 값을 포함하는 조각들(루트까지 경로)만 갱신하면 된다.

## 이론 (Theory)

길이 $n$ 배열에 대해 높이 $O(\log n)$의 이진 트리를 만든다. 리프는 원소, 내부 노드는 자식들의 결합(merge) 결과다. 결합 연산은 결합법칙을 만족하는 모노이드여야 한다(합, min, max, gcd 등).

- **질의 [l,r]**: 루트에서 내려가며 완전히 포함된 노드는 즉시 반환, 걸친 노드는 양쪽 재귀 → `O(log n)`.
- **점 갱신**: 해당 리프부터 루트까지 경로의 노드만 다시 결합 → `O(log n)`.
- **구간 갱신**: lazy propagation으로 갱신을 미뤄 전파, 여전히 `O(log n)`.

## 구현 (Implementation)

```python
class SegTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.t = [0] * (2 * self.n)        # 반복적(iterative) 구현
        self.t[self.n:] = arr
        for i in range(self.n - 1, 0, -1):
            self.t[i] = self.t[2*i] + self.t[2*i+1]

    def update(self, i, val):
        i += self.n; self.t[i] = val
        while i > 1:
            i //= 2
            self.t[i] = self.t[2*i] + self.t[2*i+1]

    def query(self, l, r):                 # [l, r)
        l += self.n; r += self.n; s = 0
        while l < r:
            if l & 1: s += self.t[l]; l += 1
            if r & 1: r -= 1; s += self.t[r]
            l //= 2; r //= 2
        return s
```

## 복잡도 (Complexity)

| 연산 | 시간 |
|---|---|
| 구축 | `O(n)` |
| 점 갱신 | `O(log n)` |
| 구간 질의 | `O(log n)` |
| 구간 갱신(lazy) | `O(log n)` |

공간은 `O(n)`(보통 $2n$ 또는 $4n$ 배열). 정적 배열의 구간 합만 필요하면 누적합이 더 싸지만, 갱신이 섞이면 세그먼트 트리가 우월하다.

## 응용 (Applications)

- 구간 합/최소/최대 질의 + 갱신
- 경쟁 프로그래밍의 구간 처리
- 좌표 압축과 결합한 구간 카운팅
- 2D로 확장해 영역 질의

## 흔한 오해 (Common Misunderstandings)

- 누적합(prefix sum)과 다르다. 누적합은 갱신이 `O(n)`, 세그먼트 트리는 `O(log n)`.
- 결합 연산이 결합법칙을 만족해야 한다(평균은 그대로는 안 됨).
- 구간 갱신은 lazy propagation 없이는 `O(n)`이 될 수 있다.
- 펜윅 트리가 구간 합엔 더 간단하지만, 세그먼트 트리가 더 일반적(min/max 등)이다.

## TMI

- 반복적 세그먼트 트리는 재귀형보다 상수 배 빠르고 코드가 짧아 경쟁 프로그래밍에서 인기다.
- lazy propagation은 "필요할 때까지 갱신을 미룬다"는 게으른 평가의 자료구조판이다.
- 持久(persistent) 세그먼트 트리는 과거 버전을 유지해 "k번째 작은 수" 같은 질의에 쓰인다.

## 연습 / 확인 문제 (Exercises)

- 길이 8 배열로 합 세그먼트 트리를 그리고 구간 [2,5] 질의 경로를 표시하라.
- min 세그먼트 트리로 바꾸려면 무엇을 수정해야 하는지 설명하라.
- 누적합과 세그먼트 트리의 갱신 비용을 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [이진 트리](Binary-Tree.md)
- 다음: [펜윅 트리 (BIT)](Fenwick-Tree.md), [Algorithms/DP-Basics.md](../Algorithms/DP-Basics.md)

## 참조 (References)

- [Data-Structures/Fenwick-Tree.md](Fenwick-Tree.md)
- [Data-Structures/Array.md](Array.md)
- [Reference/Books.md](../Reference/Books.md)
