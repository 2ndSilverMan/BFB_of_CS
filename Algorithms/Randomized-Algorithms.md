# 랜덤 알고리즘 (Randomized Algorithms)

- Level: Advanced
- Prerequisites: [Math/Probability-Statistics/Expectation.md](../Math/Probability-Statistics/Expectation.md), [Algorithms/Complexity.md](Complexity.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

랜덤 알고리즘은 무작위성을 계산에 사용해, 기대 시간이나 확률적 정확성으로 더 단순하거나 빠른 해법을 얻는다. 라스베이거스(항상 정답, 기대 시간 무작위)와 몬테카를로(빠르지만 확률적 오답 가능)로 나뉜다.

## 직관 (Intuition)

적대적 최악 입력을 피하는 좋은 방법은 "예측 불가능하게 행동하는 것"이다. 퀵정렬이 무작위 피벗을 고르면 어떤 입력에도 평균적으로 빠르다. 또는 정확성을 조금 양보하고 속도를 얻거나(몬테카를로), 시간을 양보하고 정확성을 지킨다(라스베이거스). 무작위성이 단순함과 효율을 동시에 준다.

## 이론 (Theory)

- **라스베이거스**: 출력은 항상 옳고, 실행 시간이 확률 변수(예: 무작위 퀵정렬, 기대 `O(n log n)`).
- **몬테카를로**: 실행 시간은 고정, 정답이 확률 $1-\delta$로 옳다. 반복으로 오류율을 지수적으로 낮춘다(예: 밀러-라빈, $k$회 반복 시 오류 $\le 2^{-k}$).

분석 도구: 기댓값의 선형성, 마르코프·체비쇼프 부등식, 체르노프 한계(독립 사건 합의 집중). **여론 증폭(amplification)**: 독립 반복으로 오류 확률을 줄인다. 무작위 동전 던지기가 결정적 알고리즘으로 항상 대체되는 것은 아니다($P\stackrel{?}{=}BPP$는 열린 문제이나 많은 이가 같다고 믿는다).

## 구현 (Implementation)

```python
import random
def quicksort(a):
    if len(a) <= 1: return a
    pivot = a[random.randrange(len(a))]    # 무작위 피벗 → 적대적 입력 회피
    lt = [x for x in a if x < pivot]
    eq = [x for x in a if x == pivot]
    gt = [x for x in a if x > pivot]
    return quicksort(lt) + eq + quicksort(gt)
```

## 복잡도 (Complexity)

| 알고리즘 | 유형 | 기대/보장 |
|---|---|---|
| 무작위 퀵정렬 | 라스베이거스 | 기대 `O(n log n)` |
| 밀러-라빈 | 몬테카를로 | `O(k log^3 n)`, 오류 `≤ 2^{-k}` |
| 무작위 최소 컷(Karger) | 몬테카를로 | `O(n^2)` per trial |

기대 시간·오류 확률은 무작위 비트에 대한 것이며, 입력에 대한 평균이 아니다.

## 응용 (Applications)

- 소수 판정·해싱(universal hashing)
- 빠른 정렬·선택(QuickSelect)
- 그래프 최소 컷(Karger), 스케치·스트리밍 알고리즘
- 몬테카를로 적분·시뮬레이션

## 흔한 오해 (Common Misunderstandings)

- 라스베이거스는 절대 틀리지 않는다. 틀릴 수 있는 것은 몬테카를로다.
- 기대 시간이 좋다고 개별 실행이 항상 빠른 것은 아니다(분산 존재).
- 무작위성은 "평균 입력"이 아니라 알고리즘 내부의 동전 던지기에서 온다.
- 의사난수 생성기의 품질이 보장에 영향을 줄 수 있다(암호 맥락 주의).

## TMI

- Karger의 최소 컷 알고리즘은 무작위 간선 수축만으로 동작하는, 놀랄 만큼 단순하고 우아한 사례다.
- 체르노프 한계는 "많은 독립 동전의 합은 평균 근처에 강하게 몰린다"를 정량화해 분산 시스템·ML 이론의 핵심 도구다.
- $P=BPP$ 추측은 "무작위성이 다항 시간 계산력을 본질적으로 늘리지 않는다"는 믿음을 담는다.

## 연습 / 확인 문제 (Exercises)

- 무작위 퀵정렬의 기대 비교 횟수가 `O(n log n)`임을 직관적으로 설명하라.
- 몬테카를로 알고리즘의 오류율을 반복으로 $2^{-k}$로 낮추는 원리를 보여라.
- 라스베이거스와 몬테카를로의 차이를 한 예로 대조하라.

## 이어서 읽기 (Reading Path)

- 이전: [근사 알고리즘](Approximation-Algorithms.md)
- 다음: [계산 기하학](Computational-Geometry.md)

## 참조 (References)

- [Math/Probability-Statistics/Expectation.md](../Math/Probability-Statistics/Expectation.md)
- [Algorithms/Sorting.md](Sorting.md)
- [Reference/Books.md](../Reference/Books.md)
