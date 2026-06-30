# 분할 상환 분석 (Amortized Analysis)

- Level: Advanced
- Prerequisites: [Algorithms/Complexity.md](Complexity.md), [Data-Structures/Array.md](../Data-Structures/Array.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

분할 상환 분석은 **연산 시퀀스 전체의 평균 비용**을 분석한다. 가끔 비싼 연산이 있어도 자주 일어나는 싼 연산과 평균 내면 한 연산당 비용이 낮음을 *엄밀히* 보인다 — 최악 한 번이 아니라 시퀀스 전체를 본다.

## 직관 (Intuition)

[동적 배열](../Data-Structures/Array.md)은 보통 append가 $O(1)$ 이지만 가득 차면 2배로 키우며 전체를 복사해 $O(n)$. 이 비싼 복사는 드물고, 그 비용을 앞선 싼 삽입들에 **"나눠 청구"** 하면 평균 $O(1)$. 분할 상환은 이 나눠 내기를 수학적으로 정당화한다 — **확률이 아니라 최악 시퀀스에 대한 보장**.

## 이론 (Theory)

### 세 가지 기법

- **집계법(aggregate)**: $n$ 연산 총비용 $T(n)$ 을 구해 $T(n)/n$.
- **회계법(accounting)**: 각 연산에 실제보다 큰 "요금"을 매겨 적립, 비싼 연산은 적립금으로 충당. **잔액이 음수가 안 되면** 평균 보장.
- **포텐셜법(potential)**: 상태에 $\Phi\ge0$ ($\Phi_0=0$) 정의. 분할 상환 비용 $\hat c_i = c_i + \Phi_i-\Phi_{i-1}$. 합하면 $\sum\hat c_i = \sum c_i + \Phi_n-\Phi_0 \ge \sum c_i$ → $\sum\hat c_i$ 가 총 실제 비용의 상한.

### 적용 예의 포텐셜

- 동적 배열: $\Phi = 2\cdot\text{size} - \text{capacity}$.
- 이진 카운터 증가: $\Phi$ = 켜진 비트 수 → 증가당 amortized $O(1)$.
- 두 스택 큐·[Union-Find](../Data-Structures/Union-Find.md) 경로 압축·스플레이 트리·피보나치 힙.

## 구현 (Implementation)

```python
class DynamicArray:                          # 가득 차면 2배 (개별 O(n), amortized O(1))
    def __init__(self):
        self.data, self.size = [None], 0
    def append(self, x):
        if self.size == len(self.data):
            new = [None] * (2 * len(self.data))   # 가끔 O(n) 복사
            for i in range(self.size): new[i] = self.data[i]
            self.data = new
        self.data[self.size] = x; self.size += 1
        # n번 append의 총 복사 ≤ 2n → amortized O(1)

class BinaryCounter:                          # 증가의 amortized O(1)
    def __init__(self, k): self.bits = [0]*k
    def increment(self):
        i = 0
        while i < len(self.bits) and self.bits[i] == 1:
            self.bits[i] = 0; i += 1          # 비싼 캐리지만 비트당 1번만 0→1
        if i < len(self.bits): self.bits[i] = 1
```

## 복잡도 (Complexity)

| 자료구조 | 분할 상환 | 개별 최악 |
|---|---|---|
| 동적 배열 append | $O(1)$ | $O(n)$ |
| 이진 카운터 증가 | $O(1)$ | $O(\log n)$ |
| 스플레이 트리 연산 | $O(\log n)$ | $O(n)$ |
| 피보나치 힙 decrease-key | $O(1)$ | $O(\log n)$ |

**워크드 예제(동적 배열).** $n$ 번 append 중 복사가 일어나는 시점의 크기 $1,2,4,\dots\le n$ → 총 복사 $\le 2n$, 삽입 $n$ → $(n+2n)/n=3=O(1)$.

## 응용 (Applications)

- 동적 배열·해시 테이블의 재할당, 큐의 두 스택 구현.
- 스플레이 트리·피보나치 힙 분석, Union-Find 경로 압축.
- 증가 카운터, 동적 연결성의 재구축 기법.

## 흔한 오해 (Common Misunderstandings)

- **분할 상환 ≠ 평균 케이스(확률적)** — 무작위 없이 최악 시퀀스를 보장.
- **개별 연산은 여전히 $O(n)$ 일 수 있다** — 평균만 $O(1)$.
- **포텐셜 함수 선택이 핵심** — 잘못 고르면 느슨한 경계.
- **"amortized $O(1)$"이 "항상 $O(1)$"이 아니다** — 실시간 시스템 주의.

## TMI

- 포텐셜법은 물리의 위치 에너지에 비유된다 — 상태에 저장된 "잠재 비용".
- 피보나치 힙의 우아하지만 까다로운 분석이 포텐셜법의 대표 사례다.
- 실시간 시스템은 개별 $O(n)$ 지연이 문제라 **deamortized** 변형(점진적 재구축)을 쓰기도 한다.

## 연습 / 확인 문제 (Exercises)

- 동적 배열 $n$ 번 append의 총 복사 비용 $\le 2n$ 을 보여라.
- 이진 카운터 증가의 amortized 비용을 회계법(비트당 1코인)으로 분석하라.
- 두 스택 큐의 dequeue가 amortized $O(1)$ 임을 포텐셜법으로 보여라.
- 동적 배열의 포텐셜 $\Phi=2\,\text{size}-\text{capacity}$ 로 append가 amortized $O(1)$ 임을 유도하라.

## 이어서 읽기 (Reading Path)

- 이전: [FFT / NTT](FFT.md)
- 다음: [근사 알고리즘](Approximation-Algorithms.md)
- 관련: [복잡도 분석](Complexity.md), [Union-Find](../Data-Structures/Union-Find.md)

## 참조 (References)

- [Algorithms/Complexity.md](Complexity.md)
- [Data-Structures/Union-Find.md](../Data-Structures/Union-Find.md)
- [Data-Structures/Array.md](../Data-Structures/Array.md)
- [Reference/Books.md](../Reference/Books.md)
