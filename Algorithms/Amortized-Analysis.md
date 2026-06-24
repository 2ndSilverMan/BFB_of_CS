# 분할 상환 분석 (Amortized Analysis)

- Level: Advanced
- Prerequisites: [Algorithms/Complexity.md](Complexity.md), [Data-Structures/Array.md](../Data-Structures/Array.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

분할 상환 분석은 일련의 연산 전체의 평균 비용을 분석하는 방법이다. 가끔 비싼 연산이 있어도, 자주 일어나는 싼 연산과 평균 내면 한 연산당 비용이 낮음을 엄밀히 보인다. 최악 케이스 한 번이 아니라 시퀀스 전체를 본다.

## 직관 (Intuition)

동적 배열은 보통 삽입이 `O(1)`이지만, 가득 차면 두 배로 키우며 전체를 복사해 `O(n)`이 든다. 이 비싼 복사는 드물게 일어나고, 그 비용을 앞선 싼 삽입들에 "나눠 청구"하면 평균 `O(1)`이다. 분할 상환은 이 "나눠 내기"를 수학적으로 정당화한다.

## 이론 (Theory)

세 가지 기법:

- **집계법(aggregate)**: $n$개 연산의 총비용 $T(n)$을 구해 $T(n)/n$을 평균 비용으로.
- **회계법(accounting)**: 각 연산에 실제보다 큰 "요금"을 매겨 미리 적립하고, 비싼 연산은 적립금으로 충당. 잔액이 음수가 안 되면 평균이 보장됨.
- **포텐셜법(potential)**: 자료구조 상태에 포텐셜 $\Phi$를 정의. 분할 상환 비용 = 실제 비용 + $\Delta\Phi$. $\Phi\ge 0$, $\Phi_0=0$이면 총 분할 상환 비용이 총 실제 비용의 상한.

분할 상환은 평균 케이스(확률)가 아니라 **최악 시퀀스에 대한 보장**이라는 점이 중요하다.

## 구현 (Implementation)

```python
# 동적 배열: 가득 차면 2배 확장 (개별 O(n), 분할상환 O(1))
class DynamicArray:
    def __init__(self):
        self.data = [None]; self.size = 0
    def append(self, x):
        if self.size == len(self.data):
            new = [None] * (2 * len(self.data))   # 가끔 O(n) 복사
            for i in range(self.size): new[i] = self.data[i]
            self.data = new
        self.data[self.size] = x; self.size += 1
        # n번 append의 총 복사 비용 ≤ 2n → 분할상환 O(1)
```

## 복잡도 (Complexity)

| 자료구조 | 분할 상환 |
|---|---|
| 동적 배열 append | `O(1)` |
| 이진 카운터 증가 | `O(1)` |
| 스플레이 트리 연산 | `O(log n)` |

개별 최악은 더 클 수 있지만($O(n)$), 시퀀스 평균은 위와 같이 작다.

## 응용 (Applications)

- 동적 배열·해시 테이블의 재할당
- 스플레이 트리·피보나치 힙 분석
- union-find의 경로 압축
- 증가 카운터, 큐의 두 스택 구현

## 흔한 오해 (Common Misunderstandings)

- 분할 상환은 평균 케이스(확률적)가 아니다. 무작위성 없이 최악 시퀀스를 보장한다.
- 개별 연산이 여전히 `O(n)`일 수 있다 — 평균이 `O(1)`일 뿐이다.
- 포텐셜 함수 선택이 분석의 핵심이며 잘못 고르면 느슨한 경계가 나온다.
- "분할 상환 `O(1)`"이 "항상 `O(1)`"을 뜻하지 않는다(실시간 시스템 주의).

## TMI

- 포텐셜법은 물리의 위치 에너지와 비유된다 — 상태에 저장된 "잠재 비용".
- 피보나치 힙의 우아한(하지만 까다로운) 분석은 포텐셜법의 대표 사례다.
- 실시간 시스템에서는 분할 상환 `O(1)`이라도 개별 `O(n)` 지연이 문제라, deamortized 변형을 쓰기도 한다.

## 연습 / 확인 문제 (Exercises)

- 동적 배열 $n$번 append의 총 복사 비용이 $\le 2n$임을 보여라.
- 이진 카운터 증가의 분할 상환 비용을 회계법으로 분석하라.
- 두 스택으로 큐를 만들 때 dequeue가 분할 상환 `O(1)`임을 보여라.

## 이어서 읽기 (Reading Path)

- 이전: [FFT / NTT](FFT.md)
- 다음: [근사 알고리즘](Approximation-Algorithms.md)

## 참조 (References)

- [Algorithms/Complexity.md](Complexity.md)
- [Data-Structures/Union-Find.md](../Data-Structures/Union-Find.md)
- [Reference/Books.md](../Reference/Books.md)
