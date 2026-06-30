# 복잡도 클래스 (Complexity Classes: P, NP, PSPACE)

- Level: Advanced
- Prerequisites: [CS-Theory/Computation-Theory/Turing-Machine.md](Turing-Machine.md), [Algorithms/Complexity.md](../../Algorithms/Complexity.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

복잡도 클래스는 문제를 **풀거나 검증하는 데 필요한 자원(시간·공간)** 의 양에 따라 분류한 집합이다. 결정 가능한 문제 중에서도 "현실적으로 빠르게 풀리는 것"과 "답을 검증만 빠르게 할 수 있는 것"을 구분하는 것이 핵심이며, 그 경계가 유명한 **P vs NP** 문제다.

## 직관 (Intuition)

어떤 문제는 **푸는 것**과 **답을 확인하는 것**의 난이도가 크게 다르다. 스도쿠를 처음부터 푸는 것은 어렵지만, 완성된 답이 맞는지 확인하는 것은 순식간이다. P는 "빠르게 풀 수 있는" 문제, NP는 "답을 빠르게 확인할 수 있는" 문제다. "확인이 쉬우면 푸는 것도 쉬운가?"가 바로 P=NP? 질문이다.

## 이론 (Theory)

복잡도 클래스는 [튜링 머신](Turing-Machine.md)이 쓰는 자원으로 정의된다(결정 문제, 즉 yes/no 문제 기준).

| 클래스 | 정의 |
|---|---|
| P | 결정적 튜링 머신이 **다항 시간**에 푸는 문제 |
| NP | 답(증거)이 주어지면 다항 시간에 **검증**할 수 있는 문제 |
| co-NP | "아니다"라는 답을 다항 시간에 검증할 수 있는 문제 |
| PSPACE | 다항 **공간**으로 푸는 문제 |
| EXPTIME | 지수 시간에 푸는 문제 |

알려진 포함 관계는 다음과 같다.

$$\text{P} \subseteq \text{NP} \subseteq \text{PSPACE} \subseteq \text{EXPTIME}$$

이 중 $\text{P} \subsetneq \text{EXPTIME}$만 진부분집합임이 증명됐고, 나머지 포함이 등호인지 진부분집합인지는 대부분 미해결이다. **P vs NP** ($\text{P} = \text{NP}$인가?)는 그중 가장 유명하며, 대부분의 학자는 $\text{P} \ne \text{NP}$라고 믿지만 증명되지 않았다(밀레니엄 문제, 상금 100만 달러).

NP는 "비결정적(nondeterministic) 튜링 머신이 다항 시간에 푸는 문제"로도 정의되며, 이 정의가 "검증 가능" 정의와 동치다.

## 구현 (Implementation)

NP의 본질인 "검증은 쉽다"를 부분집합 합 문제(subset sum)로 보인다.

```python
# 푸는 것: 모든 부분집합 탐색 → 최악 O(2^n) (어려움)
def solve_subset_sum(nums, target):
    n = len(nums)
    for mask in range(1 << n):
        s = sum(nums[i] for i in range(n) if mask & (1 << i))
        if s == target:
            return [nums[i] for i in range(n) if mask & (1 << i)]
    return None

# 검증: 후보 답이 맞는지 확인 → O(n) (쉬움) ← NP의 핵심
def verify(subset, target):
    return sum(subset) == target

print(verify([3, 7], 10))   # True  (증거만 있으면 즉시 확인)
```

## 복잡도 (Complexity)

| 질문 | 현재 상태 |
|---|---|
| P ⊆ NP | 참(풀 수 있으면 검증도 가능) |
| P = NP? | 미해결(대부분 ≠ 라고 추측) |
| NP = co-NP? | 미해결 |
| P = PSPACE? | 미해결 |

이 클래스들은 입력 크기에 대한 **점근적** 자원으로 정의되므로, 상수 인자나 작은 입력은 무시한다.

## 응용 (Applications)

- 문제의 본질적 난이도 분류(빠른 알고리즘이 존재할 가망 판단)
- 암호학: 많은 암호가 "NP 문제를 빠르게 풀 수 없다"는 가정에 의존
- 최적화 문제가 NP-난해이면 정확해 대신 근사·휴리스틱을 선택
- 알고리즘 설계에서 "이건 다항 시간에 안 될 수도 있다"는 신호

## 흔한 오해 (Common Misunderstandings)

- NP는 "Non-Polynomial(비다항)"의 약자가 **아니다**. "Nondeterministic Polynomial"이다. P는 NP의 부분집합이다.
- NP 문제가 모두 어려운 것은 아니다. P ⊆ NP이므로 쉬운 문제도 NP에 속한다. 어려운 것은 NP-완전 문제다.
- P=NP가 증명돼도 모든 게 즉시 빨라지는 건 아니다. 다항식의 차수가 거대하면 실용성은 별개다.
- "검증이 쉽다"와 "풀기가 쉽다"는 다르다. NP의 정의는 검증 가능성이지 풀이 가능성이 아니다.

## TMI

- P vs NP는 클레이 수학연구소의 7대 밀레니엄 문제 중 하나로, 해결하면 100만 달러를 받는다. 해결되지 않은 채 가장 유명한 미해결 문제로 꼽힌다.
- 만약 P=NP라면 대부분의 공개키 암호가 무너지고, 단백질 접힘·최적 스케줄링 같은 문제가 단번에 풀린다. 그 파급력 때문에 대부분의 학자는 P≠NP를 희망 섞어 믿는다.
- 사빈치-사비치(Savitch) 정리는 비결정적 공간과 결정적 공간이 제곱 차이밖에 안 난다는 놀라운 결과로, $\text{NPSPACE}=\text{PSPACE}$를 함의한다(시간 세계와 대조적).

## 연습 / 확인 문제 (Exercises)

- P, NP, co-NP의 정의를 "풀기"와 "검증하기" 관점에서 구분해 설명하라.
- 부분집합 합 문제에서 "푸는 비용"과 "검증 비용"의 차이를 복잡도로 비교하라.
- P=NP가 참이라면 암호학에 어떤 일이 생길지 서술하라.

## 이어서 읽기 (Reading Path)

- 이전: [결정 불가능성과 정지 문제](Undecidability.md)
- 다음: [NP-완전성과 환원](NP-Completeness.md)
- 관련: [복잡도 분석](../../Algorithms/Complexity.md)

## 참조 (References)

- [CS-Theory/Computation-Theory/Turing-Machine.md](Turing-Machine.md)
- [Algorithms/Complexity.md](../../Algorithms/Complexity.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Papers.md](../../Reference/Papers.md)
