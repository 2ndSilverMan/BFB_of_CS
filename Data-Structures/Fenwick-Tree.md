# 펜윅 트리 (Fenwick Tree, Binary Indexed Tree)

- Level: Advanced
- Prerequisites: [Data-Structures/Array.md](Array.md), [Data-Structures/Segment-Tree.md](Segment-Tree.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

펜윅 트리(BIT)는 **점 갱신과 접두사 합 질의를 모두 $O(\log n)$** 에 처리하는 배열 한 개짜리 구조다. [세그먼트 트리](Segment-Tree.md)와 같은 성능이지만 코드가 짧고 상수가 작으며 메모리가 절반 수준이다.

## 직관 (Intuition)

누적합 배열은 질의가 $O(1)$ 이지만 한 값이 바뀌면 뒤를 전부 고쳐 $O(n)$. 펜윅 트리는 각 칸이 "**이진수 구조에 맞춘 특정 길이 구간의 합**"을 담도록 영리하게 배치한다. 그러면 한 값이 바뀔 때 손대는 칸이 이진수 비트 수($O(\log n)$)로 줄고, 접두사 합도 같은 수의 칸을 더해 얻는다.

## 이론 (Theory)

### 1. lowbit과 책임 구간

$\text{lowbit}(i)=i\,\&\,(-i)$ 는 가장 낮은 켜진 비트(2의 보수 이용). 인덱스 $i$ 의 칸은 구간 $(\,i-\text{lowbit}(i),\ i\,]$ 의 합을 담당한다.

| $i$ | 이진 | lowbit | 책임 구간 |
|---|---|---|---|
| 6 | `110` | 2 | (4, 6] = {5,6} |
| 8 | `1000` | 8 | (0, 8] = {1..8} |
| 12 | `1100` | 4 | (8, 12] = {9..12} |

### 2. 두 핵심 순회

- **접두사 합 `sum(i)`** = $[1, i]$: $i$ 에서 lowbit만큼 **빼며** 0까지 더한다. 손대는 칸 수 = $i$ 의 켜진 비트 수 $\le \log n$.
- **갱신 `add(i, Δ)`**: $i$ 에서 lowbit만큼 **더하며** $n$ 까지 올라가 갱신. 손대는 칸 수 $\le \log n$.

구간 합 $[l, r] = \text{sum}(r) - \text{sum}(l-1)$ (합처럼 **역연산이 있는** 모노이드라 가능).

### 3. $O(n)$ 구축과 구간 갱신

순진하게 `add`를 $n$ 번 하면 $O(n\log n)$ 이지만, 각 $i$ 의 값을 부모 $i+\text{lowbit}(i)$ 로 전파하면 **$O(n)$** 에 구축된다. **구간 갱신 + 구간 질의**는 BIT 두 개($B_1, B_2$)로 차분(difference) 기법을 써서 둘 다 $O(\log n)$ 으로 확장된다:

$$\text{prefix}(i) = \text{sum}(B_1, i)\cdot i - \text{sum}(B_2, i)$$

## 구현 (Implementation)

```python
class BIT:
    def __init__(self, n):
        self.t = [0] * (n + 1)             # 1-indexed (0은 종료 조건)

    def add(self, i, delta):
        while i < len(self.t):
            self.t[i] += delta
            i += i & (-i)                  # lowbit 만큼 상승

    def sum(self, i):                      # 접두사 합 [1, i]
        s = 0
        while i > 0:
            s += self.t[i]
            i -= i & (-i)                  # lowbit 만큼 하강
        return s

    def range_sum(self, l, r):             # [l, r]
        return self.sum(r) - self.sum(l - 1)
```

## 복잡도 (Complexity)

| 연산 | 시간 | 공간 |
|---|---|---|
| 점 갱신 | $O(\log n)$ | $O(n)$ 배열 1개 |
| 접두사/구간 합 | $O(\log n)$ | — |
| 구축 | $O(n)$ (전파) 또는 $O(n\log n)$ | — |

**워크드 예제.** `sum(13)`: 13=`1101` → 13, 13−lowbit(1)=12(`1100`), 12−4=8(`1000`), 8−8=0 종료 → 칸 **13,12,8** 세 개 합. `add(5, Δ)`: 5=`101` → 5, 5+1=6, 6+2=8, 8+8=16, …→ 칸 **5,6,8,16,…** 갱신. 둘 다 비트 수만큼($\le\log n$)만 만진다.

## 응용 (Applications)

- 동적 누적 합·빈도 카운팅, 순위(rank) 질의(좌표 압축과 결합).
- **역순 쌍(inversion) 세기**: 오른쪽에서 왼쪽으로 훑으며 "지금까지 더 작은 수 개수"를 BIT로.
- 구간 갱신/질의(이중 BIT), 2D BIT(부분 행렬 합).

## 흔한 오해 (Common Misunderstandings)

- **보통 1-indexed로 구현**한다 — 0은 `sum`의 종료 조건이라 데이터에 못 쓴다.
- **역연산이 있는 모노이드(합·xor)에 적합** — min/max는 일반적으로 BIT로 구간 질의가 안 된다(세그먼트 트리 필요).
- **세그먼트 트리보다 항상 낫지 않다** — 더 일반적인 질의엔 세그먼트 트리.
- **`i & (-i)`는 2의 보수 표현에 의존**한다.

## TMI

- 1994년 Peter Fenwick이 제안. "binary indexed tree"라는 이름이 비트 구조를 잘 드러낸다.
- `lowbit = i & -i` 트릭은 비트 조작의 우아함을 보여 주는 대표 예 — `-i`가 2의 보수라 "최하위 1비트만 남고 나머지는 반전+1"되는 성질을 이용한다.
- 역순 쌍 세기는 병합 정렬로도 되지만, BIT + 좌표 압축은 **온라인(스트리밍)** 처리에 유리하다.

## 연습 / 확인 문제 (Exercises)

- $\text{lowbit}(12)$ 와 그 책임 구간을 구하라(위 표 확인).
- `sum(11)` 과 `add(6, Δ)` 가 각각 어떤 칸을 만지는지 이진수로 추적하라.
- BIT + 좌표 압축으로 배열의 역순 쌍 개수를 구하는 절차를 기술하라.
- 같은 "구간 합 + 점 갱신" 문제를 펜윅과 세그먼트 트리로 풀고 코드·메모리를 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [세그먼트 트리](Segment-Tree.md)
- 다음: [정렬](../Algorithms/Sorting.md)
- 관련: [동적 계획법 기초](../Algorithms/DP-Basics.md)

## 참조 (References)

- [Data-Structures/Segment-Tree.md](Segment-Tree.md)
- [Data-Structures/Array.md](Array.md)
- [Reference/Books.md](../Reference/Books.md)
