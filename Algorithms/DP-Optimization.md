# DP 최적화 (DP Optimization)

- Level: Advanced
- Prerequisites: [Algorithms/DP-Basics.md](DP-Basics.md), [Math/Discrete/Recurrences.md](../Math/Discrete/Recurrences.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

DP 최적화는 점화식의 구조적 성질을 이용해 동적 계획법의 시간 복잡도를 낮추는 기법들이다. 컨벡스 헐 트릭, 분할 정복 최적화, Knuth 최적화, 단조 큐 등이 있다.

## 직관 (Intuition)

기본 DP의 전이가 "이전 모든 상태를 훑는" 형태($O(n)$ 전이)면 전체가 $O(n^2)$가 된다. 하지만 전이 비용이나 최적 분기점이 단조롭게 움직이는 등 숨은 규칙이 있으면, 매번 전부 보지 않고 후보를 좁혀 $O(n\log n)$이나 $O(n)$으로 줄일 수 있다. 핵심은 "불필요한 후보를 버리는 구조"를 찾는 것이다.

## 이론 (Theory)

대표 기법:

- **컨벡스 헐 트릭(CHT)**: 전이가 $dp[i]=\min_j(a_j\cdot x_i+b_j)$ 형태(선형)면, 직선들의 하한 포락선을 유지해 질의 `O(log n)` 또는 `O(1)`.
- **분할 정복 최적화**: 최적 분기점 $opt(i)$가 $i$에 대해 단조이면, 분할 정복으로 $O(n^2)\to O(n\log n)$.
- **Knuth 최적화**: 구간 DP에서 $opt[i][j-1]\le opt[i][j]\le opt[i+1][j]$(사각 부등식)이면 $O(n^3)\to O(n^2)$.
- **단조 큐/슬라이딩 윈도우**: 윈도우 최적 전이를 분할상환 `O(1)`로.

각 기법은 비용 함수의 볼록성·단조성·사각 부등식 같은 조건을 요구한다.

## 구현 (Implementation)

```python
# 컨벡스 헐 트릭(최소): 기울기 감소 직선들의 하한 포락선
class CHT:
    def __init__(self):
        self.lines = []   # (m, b), 기울기 감소 순
    def add(self, m, b):
        while len(self.lines) >= 2 and self._bad(self.lines[-2], self.lines[-1], (m, b)):
            self.lines.pop()
        self.lines.append((m, b))
    def query(self, x):
        # 이분 탐색으로 최소를 주는 직선 선택
        lo, hi = 0, len(self.lines) - 1
        while lo < hi:
            mid = (lo + hi) // 2
            if self._val(self.lines[mid], x) >= self._val(self.lines[mid+1], x):
                lo = mid + 1
            else:
                hi = mid
        m, b = self.lines[lo]
        return m * x + b
```

## 복잡도 (Complexity)

| 기법 | 개선 |
|---|---|
| 컨벡스 헐 트릭 | `O(n^2)` → `O(n log n)` 또는 `O(n)` |
| 분할 정복 최적화 | `O(kn^2)` → `O(kn log n)` |
| Knuth 최적화 | `O(n^3)` → `O(n^2)` |

전제 조건(볼록성·단조성)이 성립할 때만 적용된다. 조건 검증 없이 쓰면 틀린 답을 빠르게 낼 뿐이다.

## 응용 (Applications)

- 작업 분할·일정의 비용 최소화 DP
- 구간 병합(파일 합치기, 행렬 곱 순서)
- 통신·압축의 최적 분할
- 기하·게임 이론 DP의 가속

## 흔한 오해 (Common Misunderstandings)

- 모든 DP가 최적화되는 것은 아니다. 구조적 조건이 필요하다.
- CHT는 기울기·질의의 단조성에 따라 구현(스택 vs Li Chao 트리)이 달라진다.
- Knuth 최적화의 사각 부등식은 증명 없이 가정하면 위험하다.
- 상수 개선과 점근 개선을 혼동하면 안 된다.

## TMI

- Li Chao 트리는 임의 순서의 직선/질의도 다루는 CHT의 일반화된 세그먼트 트리 변형이다.
- 분할 정복 최적화의 단조성은 비용 함수의 사각 부등식(Monge 조건)에서 따라온다.
- 이런 기법들은 주로 경쟁 프로그래밍에서 정밀하게 쓰이며 실무에선 드물지만 강력하다.

## 연습 / 확인 문제 (Exercises)

- 선형 전이 DP를 CHT로 가속하는 과정을 한 예로 보여라.
- Knuth 최적화의 사각 부등식이 무엇을 의미하는지 설명하라.
- 단조 큐로 슬라이딩 윈도우 최소 전이를 `O(n)`에 처리하라.

## 이어서 읽기 (Reading Path)

- 이전: [DP 기초](DP-Basics.md)
- 다음: [비트마스크 DP](Bitmask-DP.md), [트리 DP](Tree-DP.md)

## 참조 (References)

- [Algorithms/DP-Basics.md](DP-Basics.md)
- [Data-Structures/Segment-Tree.md](../Data-Structures/Segment-Tree.md)
- [Reference/Books.md](../Reference/Books.md)
