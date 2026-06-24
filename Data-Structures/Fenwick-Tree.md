# 펜윅 트리 (Fenwick Tree, Binary Indexed Tree)

- Level: Advanced
- Prerequisites: [Data-Structures/Array.md](Array.md), [Data-Structures/Segment-Tree.md](Segment-Tree.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

펜윅 트리(BIT)는 누적 합(prefix sum)을 효율적으로 갱신·질의하는 배열 기반 자료구조다. 점 갱신과 접두사 합 질의를 모두 `O(log n)`에 처리하며, 세그먼트 트리보다 코드가 짧고 상수가 작다.

## 직관 (Intuition)

누적합 배열은 질의는 `O(1)`이지만 한 값이 바뀌면 뒤를 전부 고쳐 `O(n)`이다. 펜윅 트리는 각 인덱스가 "이진수에서 특정 길이의 구간 합"을 담게 영리하게 배치한다. 그러면 한 값이 바뀔 때 영향받는 칸이 이진수의 비트 수만큼(`O(log n)`)으로 줄고, 접두사 합도 같은 수의 칸을 더해 얻는다.

## 이론 (Theory)

인덱스 $i$의 트리 노드는 $[i-\text{lowbit}(i)+1,\ i]$ 구간 합을 저장한다. 여기서 $\text{lowbit}(i)=i\ \&\ (-i)$는 가장 낮은 켜진 비트다.

- **접두사 합 $\text{sum}(i)$**: $i$에서 $\text{lowbit}$만큼 빼며 거슬러 올라가 더한다.
- **갱신 $\text{add}(i,\Delta)$**: $i$에서 $\text{lowbit}$만큼 더하며 올라가 갱신한다.

구간 합 $[l,r]=\text{sum}(r)-\text{sum}(l-1)$. 두 BIT를 결합하면 구간 갱신 + 구간 질의도 가능하다.

## 구현 (Implementation)

```python
class BIT:
    def __init__(self, n):
        self.t = [0] * (n + 1)

    def add(self, i, delta):          # 1-indexed
        while i < len(self.t):
            self.t[i] += delta
            i += i & (-i)             # lowbit 만큼 상승
    def sum(self, i):                 # prefix sum [1, i]
        s = 0
        while i > 0:
            s += self.t[i]
            i -= i & (-i)             # lowbit 만큼 하강
        return s
```

## 복잡도 (Complexity)

| 연산 | 시간 |
|---|---|
| 점 갱신 | `O(log n)` |
| 접두사/구간 합 | `O(log n)` |
| 구축 | `O(n)` 또는 `O(n log n)` |

공간은 `O(n)`(배열 하나). 세그먼트 트리와 같은 점-갱신/구간-합 성능이지만 상수가 작고 메모리가 절반 수준이다.

## 응용 (Applications)

- 동적 누적 합·빈도 카운팅
- 역순 쌍(inversion) 세기
- 좌표 압축과 결합한 순위 질의
- 구간 갱신/질의(이중 BIT)

## 흔한 오해 (Common Misunderstandings)

- 펜윅 트리는 보통 1-indexed로 구현한다(0은 종료 조건).
- 합·xor처럼 역연산이 있는 모노이드에 적합하다. min/max는 일반적으로 BIT로 구간 질의가 안 된다(세그먼트 트리 필요).
- 세그먼트 트리보다 항상 낫지 않다. 더 일반적인 질의엔 세그먼트 트리가 필요하다.
- `i & (-i)`는 2의 보수 표현에 의존한다.

## TMI

- 1994년 Peter Fenwick이 제안했고, "binary indexed tree"라는 이름이 비트 구조를 잘 드러낸다.
- 역순 쌍 세기는 병합 정렬로도 되지만, BIT + 좌표 압축이 온라인 처리에 유리하다.
- `lowbit` 트릭 `i & -i`는 비트 조작의 우아함을 보여 주는 대표 예다.

## 연습 / 확인 문제 (Exercises)

- $\text{lowbit}(12)$를 계산하고 그 의미를 설명하라.
- BIT로 배열의 역순 쌍 개수를 구하는 알고리즘을 기술하라.
- 같은 문제를 세그먼트 트리와 펜윅 트리로 풀 때 코드·메모리를 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [세그먼트 트리](Segment-Tree.md)
- 다음: [Algorithms/Sorting.md](../Algorithms/Sorting.md), [Algorithms/DP-Basics.md](../Algorithms/DP-Basics.md)

## 참조 (References)

- [Data-Structures/Segment-Tree.md](Segment-Tree.md)
- [Data-Structures/Array.md](Array.md)
- [Reference/Books.md](../Reference/Books.md)
