# 랜덤 알고리즘 (Randomized Algorithms)

- Level: Advanced
- Prerequisites: [Math/Probability-Statistics/Expectation.md](../Math/Probability-Statistics/Expectation.md), [Algorithms/Complexity.md](Complexity.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

랜덤 알고리즘은 **무작위성을 계산에 사용**해 더 단순하거나 빠른 해법을 얻는다. **라스베이거스**(항상 정답, 시간이 확률 변수)와 **몬테카를로**(시간 고정, 확률적 오답 가능)로 나뉜다.

## 직관 (Intuition)

적대적 최악 입력을 피하는 좋은 방법은 **예측 불가능하게 행동**하는 것이다. 퀵정렬이 무작위 피벗을 고르면 *어떤* 입력에도 평균 빠르다. 무작위성은 정확성을 조금 양보해 속도를 얻거나(몬테카를로), 시간을 양보해 정확성을 지킨다(라스베이거스).

## 이론 (Theory)

### 1. 두 부류

- **라스베이거스**: 출력 항상 옳음, 시간이 확률 변수(무작위 퀵정렬 기대 $O(n\log n)$).
- **몬테카를로**: 시간 고정, 정답 확률 $1-\delta$. 독립 반복으로 오류 지수 감소(밀러-라빈 $k$ 회 → 오류 $\le4^{-k}$).

### 2. 분석 도구

**기댓값의 선형성**(독립 불필요)이 가장 강력. 집중 부등식: Markov, Chebyshev, **Chernoff**(독립 합이 평균에 강하게 몰림). **증폭(amplification)**: 독립 반복으로 오류를 $\delta^k$ 로.

### 3. Karger 최소 컷

무작위로 간선을 골라 양 끝을 **수축(contract)** 반복 → 2정점 남으면 그 사이 간선이 컷 후보. 특정 최소 컷이 살아남을 확률 $\ge\dfrac{2}{n(n-1)}=1/\binom n2$. $O(n^2\log n)$ 번 반복하면 높은 확률로 최소 컷을 찾는다 — 무작위성만으로 동작하는 우아한 예.

## 구현 (Implementation)

```python
import random
def quicksort(a):                            # 라스베이거스: 항상 정답
    if len(a) <= 1: return a
    p = a[random.randrange(len(a))]          # 무작위 피벗 → 적대적 입력 회피
    lt = [x for x in a if x < p]
    eq = [x for x in a if x == p]
    gt = [x for x in a if x > p]
    return quicksort(lt) + eq + quicksort(gt)
```

무작위 퀵정렬 기대 비교 횟수: 두 원소 $a_i, a_j$ 가 비교될 확률 $=\frac{2}{j-i+1}$ → 총 기대 $\sum_{i<j}\frac{2}{j-i+1}=O(n\log n)$(조화급수).

## 복잡도 (Complexity)

| 알고리즘 | 유형 | 기대/보장 |
|---|---|---|
| 무작위 퀵정렬 | 라스베이거스 | 기대 $O(n\log n)$ |
| 밀러-라빈 | 몬테카를로 | $O(k\log^3 n)$, 오류 $\le4^{-k}$ |
| Karger 최소 컷 | 몬테카를로 | $O(n^2)$/시도, 성공 $\ge1/\binom n2$ |
| QuickSelect | 라스베이거스 | 기대 $O(n)$ |

기대 시간·오류는 **무작위 비트에 대한 것**이지 입력 평균이 아니다.

## 응용 (Applications)

- 소수 판정·해싱(universal hashing), 빠른 정렬·선택.
- 그래프 최소 컷(Karger), 스케치·스트리밍(Count-Min, HyperLogLog).
- 몬테카를로 적분·시뮬레이션, 무작위 라운딩(근사 알고리즘).

## 흔한 오해 (Common Misunderstandings)

- **라스베이거스는 절대 안 틀린다** — 틀릴 수 있는 건 몬테카를로.
- **기대 시간이 좋아도 개별 실행이 항상 빠르진 않다**(분산 존재).
- **무작위성은 "평균 입력"이 아니라 알고리즘 내부 동전**에서 온다 — 최악 입력에도 보장.
- **PRNG 품질이 보장에 영향** — 암호 맥락에선 CSPRNG 필요.

## TMI

- Karger 최소 컷은 무작위 수축만으로 동작하는 놀랍도록 단순·우아한 사례다.
- Chernoff 한계는 분산 시스템·ML 일반화 이론의 핵심 도구다.
- $P=BPP$ 추측은 "무작위성이 다항 시간 계산력을 본질적으로 늘리지 않는다"는 믿음 — 많은 이가 참이라 본다(탈무작위화).

## 연습 / 확인 문제 (Exercises)

- 무작위 퀵정렬 기대 비교 $O(n\log n)$ 을 $\frac{2}{j-i+1}$ 논증으로 보여라.
- 몬테카를로 오류율을 반복으로 $4^{-k}$ 로 낮추는 원리를 설명하라.
- 라스베이거스와 몬테카를로를 한 예로 대조하라.
- Karger가 왜 $O(n^2\log n)$ 반복으로 높은 확률을 얻는지 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [근사 알고리즘](Approximation-Algorithms.md)
- 다음: [계산 기하학](Computational-Geometry.md)
- 관련: [기댓값](../Math/Probability-Statistics/Expectation.md), [해시 함수](../Data-Structures/Hash-Function.md)

## 참조 (References)

- [Math/Probability-Statistics/Expectation.md](../Math/Probability-Statistics/Expectation.md)
- [Algorithms/Sorting.md](Sorting.md)
- [Reference/Books.md](../Reference/Books.md)
