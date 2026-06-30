# DP 최적화 (DP Optimization)

- Level: Advanced
- Prerequisites: [Algorithms/DP-Basics.md](DP-Basics.md), [Math/Discrete/Recurrences.md](../Math/Discrete/Recurrences.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

DP 최적화는 점화식의 **구조적 성질**(볼록성·단조성·사각 부등식)을 이용해 DP 시간을 낮추는 기법들이다 — 컨벡스 헐 트릭(CHT), 분할 정복 최적화, Knuth 최적화, 단조 큐.

## 직관 (Intuition)

전이가 "이전 모든 상태를 훑는" 형태($O(n)$)면 전체 $O(n^2)$. 그러나 **최적 분기점이나 비용 함수가 단조롭게 움직이는** 숨은 규칙이 있으면, 매번 전부 보지 않고 후보를 좁혀 $O(n\log n)$·$O(n)$ 으로 줄인다. 핵심은 "쓸모없는 후보를 버리는 구조"를 찾는 것.

## 이론 (Theory)

### 1. 컨벡스 헐 트릭 (CHT)

전이가 $dp[i]=\min_j(m_j\,x_i+b_j)$ (선형)면, 직선들의 **하한 포락선(lower envelope)** 만 유지하면 된다. 기울기·질의가 단조면 단조 스택 + 포인터로 $O(1)$, 아니면 **Li Chao 트리**(세그먼트 트리 변형)로 임의 순서도 $O(\log n)$.

### 2. 분할 정복 최적화

$opt(i)$(= $dp[i]$ 를 최소화하는 분기점)가 $i$ 에 대해 **단조**이면, "구간 $[l,r]$ 의 $opt$ 는 $[opt_l, opt_r]$ 안" 이라는 사실로 분할 정복 → $O(kn^2)\to O(kn\log n)$. 단조성은 비용의 **사각 부등식(Monge)** $C(a,c)+C(b,d)\le C(a,d)+C(b,c)$ 에서 따라온다.

### 3. Knuth 최적화 / 단조 큐

구간 DP에서 $opt[i][j-1]\le opt[i][j]\le opt[i+1][j]$ 면 $O(n^3)\to O(n^2)$. 윈도우 최적 전이는 **단조 큐**로 amortized $O(1)$([덱](../Data-Structures/Deque.md)의 monotonic deque).

## 구현 (Implementation)

```python
class CHT:                                  # 최소, 기울기 감소 직선 추가
    def __init__(self): self.lines = []     # (m, b)
    def _bad(self, l1, l2, l3):             # l2가 불필요한가 (교점 비교)
        return (l3[1]-l1[1])*(l1[0]-l2[0]) <= (l2[1]-l1[1])*(l1[0]-l3[0])
    def add(self, m, b):
        while len(self.lines) >= 2 and self._bad(self.lines[-2], self.lines[-1], (m, b)):
            self.lines.pop()
        self.lines.append((m, b))
    def query(self, x):                     # 단조 질의면 포인터, 아니면 이분
        lo, hi = 0, len(self.lines)-1
        while lo < hi:
            mid = (lo+hi)//2
            if self._val(mid, x) >= self._val(mid+1, x): lo = mid+1
            else: hi = mid
        m, b = self.lines[lo]; return m*x + b
    def _val(self, i, x): m, b = self.lines[i]; return m*x + b
```

## 복잡도 (Complexity)

| 기법 | 개선 | 전제 |
|---|---|---|
| CHT | $O(n^2)\to O(n\log n)$/$O(n)$ | 전이 선형 |
| 분할 정복 최적화 | $O(kn^2)\to O(kn\log n)$ | $opt$ 단조(Monge) |
| Knuth 최적화 | $O(n^3)\to O(n^2)$ | 사각 부등식 |
| 단조 큐 | $O(n^2)\to O(n)$ | 윈도우 단조 |

**전제 조건이 성립할 때만** 옳다 — 검증 없이 쓰면 빠르게 *틀린* 답을 낸다.

## 응용 (Applications)

- 작업 분할·일정 비용 최소화 DP, 구간 병합(파일 합치기·행렬 곱 순서).
- 통신·압축의 최적 분할, 기하·게임 이론 DP 가속.

## 흔한 오해 (Common Misunderstandings)

- **모든 DP가 최적화되지 않는다** — 구조적 조건 필수.
- **CHT 구현은 단조성에 따라** 스택 vs Li Chao로 갈린다.
- **Knuth의 사각 부등식을 증명 없이 가정하면 위험**.
- **상수 개선과 점근 개선을 혼동하지 말 것**.

## TMI

- Li Chao 트리는 임의 순서의 직선/질의도 다루는 CHT의 세그먼트 트리 일반화다.
- 분할 정복 최적화의 단조성은 Monge 조건(사각 부등식)에서 나온다 — 행렬 검색(SMAWK)과도 연결.
- 이 기법들은 주로 경쟁 프로그래밍에서 정밀히 쓰이고 실무에선 드물지만 강력하다.

## 연습 / 확인 문제 (Exercises)

- 선형 전이 DP를 CHT로 가속하는 과정을 한 예로 보여라.
- Knuth 사각 부등식이 무엇을 의미하는지 설명하라.
- 단조 큐로 슬라이딩 윈도우 최소 전이를 $O(n)$ 에 처리하라.
- 분할 정복 최적화의 $opt$ 단조성이 왜 $O(n\log n)$ 을 주는지 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [DP 기초](DP-Basics.md)
- 다음: [비트마스크 DP](Bitmask-DP.md)
- 관련: [세그먼트 트리](../Data-Structures/Segment-Tree.md), [트리 DP](Tree-DP.md)

## 참조 (References)

- [Algorithms/DP-Basics.md](DP-Basics.md)
- [Data-Structures/Segment-Tree.md](../Data-Structures/Segment-Tree.md)
- [Reference/Books.md](../Reference/Books.md)
