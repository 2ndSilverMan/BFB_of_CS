# 복잡도 분석 (Big-O)

- Level: Beginner
- Prerequisites: [Programming/Control-Flow.md](../Programming/Control-Flow.md), [Math/Discrete/Logic.md](../Math/Discrete/Logic.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

복잡도 분석은 입력 크기 $n$ 이 커질 때 알고리즘의 시간·공간 사용량이 **어떤 증가율로** 늘어나는지를 기계·언어와 무관하게 기술한다. Big-O는 그 증가율의 **점근적 상한**을 나타낸다.

## 직관 (Intuition)

작은 입력에선 대부분 코드가 충분히 빠르다. 문제는 $n$ 이 커질 때다 — $n=100$ 에서 멀쩡하던 $O(n^2)$ 가 $n=10^6$ 에서 안 끝난다. 복잡도는 "몇 초"가 아니라 **"작업량이 어떤 모양으로 자라는가"** 를 말한다. 그래서 하드웨어가 바뀌어도 결론이 유지된다.

## 이론 (Theory)

### 1. 점근 표기의 형식 정의

| 표기 | 의미 | 정의(대략) |
|---|---|---|
| $O(g)$ | 상한 | $f(n)\le c\,g(n)$ ($n\ge n_0$) 인 $c>0$ 존재 |
| $\Omega(g)$ | 하한 | $f(n)\ge c\,g(n)$ |
| $\Theta(g)$ | 상·하한(타이트) | $O(g)\cap\Omega(g)$ |
| $o(g)$ | 엄격한 상한 | $\lim f/g = 0$ |

Big-O는 **낮은 차수 항과 상수 계수를 버린다**: $3n^2+10n+5 = \Theta(n^2)$. 흔히 "O"라 말하지만 보통 의도는 타이트한 $\Theta$ 다.

### 2. 자주 보는 증가율과 한계

| 표기 | 이름 | 예 | $n$ ≈ (1초, 10⁸연산 가정) |
|---|---|---|---|
| $O(1)$ | 상수 | 배열 접근 | — |
| $O(\log n)$ | 로그 | 이진 탐색 | 거대 |
| $O(n)$ | 선형 | 순회 | $10^8$ |
| $O(n\log n)$ | 선형로그 | 비교 정렬 | $\sim5\times10^6$ |
| $O(n^2)$ | 이차 | 모든 쌍 | $\sim10^4$ |
| $O(2^n)$ | 지수 | 모든 부분집합 | $\sim26$ |

로그의 밑은 상수배라 무시한다($\log_2 n,\log_{10}n$ 둘 다 $O(\log n)$).

### 3. 어떤 경우(case)인가 + amortized

같은 알고리즘도 **최선·평균·최악**이 다르다(퀵정렬 평균 $O(n\log n)$, 최악 $O(n^2)$). **amortized**(분할상환)는 "최악의 연속 $n$ 연산 평균"으로, 동적 배열 `append`($O(1)$ amortized)처럼 가끔 비싼 연산을 고르게 본다 — 분석 도구는 aggregate·accounting·potential 세 가지([분할 상환 분석](Amortized-Analysis.md)).

### 4. 분할정복 점화식: 마스터 정리

$T(n)=a\,T(n/b)+f(n)$ 에서 $n^{\log_b a}$ 와 $f(n)$ 을 비교:

- $f=O(n^{\log_b a-\varepsilon})$ → $T=\Theta(n^{\log_b a})$ (잎이 지배)
- $f=\Theta(n^{\log_b a})$ → $T=\Theta(n^{\log_b a}\log n)$ (균형, 예: 병합정렬 $a=b=2,f=n$ → $n\log n$)
- $f=\Omega(n^{\log_b a+\varepsilon})$ + 정칙성 → $T=\Theta(f)$ (루트가 지배)

## 구현 (Implementation)

```python
def has_duplicate(values):          # O(n^2): 모든 쌍
    n = len(values)
    for i in range(n):
        for j in range(i + 1, n):
            if values[i] == values[j]:
                return True
    return False

def has_duplicate_fast(values):     # 평균 O(n), 공간 O(n): 시간-공간 트레이드오프
    seen = set()
    for v in values:
        if v in seen:
            return True
        seen.add(v)
    return False
```

중첩 루프라고 항상 $O(n^2)$ 는 아니다 — 안쪽 반복 횟수의 **총합**을 봐야 한다. 위 `has_duplicate`의 총 반복은 $\sum_{i}(n-i)=\binom{n}{2}=\Theta(n^2)$.

## 복잡도 (Complexity)

| 함수 | 시간 | 공간 |
|---|---|---|
| `has_duplicate` | $O(n^2)$ | $O(1)$ |
| `has_duplicate_fast` | 평균 $O(n)$ | $O(n)$ |

공간 복잡도는 **보조 자료구조 + 재귀 호출 스택**을 함께 센다(깊이 $h$ 재귀는 $O(h)$ 스택).

## 응용 (Applications)

- 알고리즘·자료구조 선택, 병목 예측, 입력 한계 판단.
- "이 제약($n\le10^5$)에서 어떤 복잡도까지 통과하나" — 경쟁 프로그래밍의 첫 계산.
- 점근이 같아도 상수·캐시가 가르는 실측은 [벤치마킹](../Engineering/Performance/Benchmarking-Basics.md)으로 검증.

## 흔한 오해 (Common Misunderstandings)

- **Big-O가 항상 최악은 아니다** — 최선/평균/최악 중 무엇인지 명시해야 한다.
- **$O(n)$ 이 $O(1)$ 보다 항상 느린 게 아니다** — 작은 $n$ 과 큰 상수에선 역전될 수 있다($n$ 점근이지 절대시간이 아님).
- **중첩 루프 ≠ 항상 $O(n^2)$** — 반복 범위와 입력의 관계를 봐야 한다.
- **해시 $O(1)$ 은 좋은 해시·적당한 부하율 가정** — 충돌이 심하면 $O(n)$.

## TMI

- Big-O는 Bachmann·Landau가 도입해 "Landau notation"이라고도 한다(원래 정수론 표기).
- "갤럭틱 알고리즘(galactic algorithm)"은 점근은 더 좋지만 상수가 천문학적이라 현실 입력에선 절대 안 쓰이는 알고리즘을 부르는 말이다.
- $O(n^2)$ 비교 정렬 하한, $\Omega(n\log n)$ 비교 정렬 하한처럼 **하한 증명**은 상한만큼 중요하다 — "이보다 빠를 수 없다".

## 연습 / 확인 문제 (Exercises)

- 배열 합 함수의 시간·공간 복잡도를 정의에 따라 보여라.
- 이중 루프인데 전체 반복이 $O(n)$ 인 예(예: 투 포인터)를 만들어라.
- 병합정렬 점화식 $T(n)=2T(n/2)+n$ 에 마스터 정리를 적용하라.
- $n\le10^4,\ 10^6,\ 10^9$ 각각에서 통과 가능한 최대 복잡도를 추정하라.

## 이어서 읽기 (Reading Path)

- 이전: [그래프 표현](../Data-Structures/Graph-Representation.md)
- 다음: [정렬](Sorting.md)
- 관련: [분할 상환 분석](Amortized-Analysis.md), [벤치마킹 기초](../Engineering/Performance/Benchmarking-Basics.md)

## 참조 (References)

- [Data-Structures/Array.md](../Data-Structures/Array.md)
- [Programming/Control-Flow.md](../Programming/Control-Flow.md)
- [Algorithms/Amortized-Analysis.md](Amortized-Analysis.md)
- [Reference/Books.md](../Reference/Books.md)
- [Reference/Courses.md](../Reference/Courses.md)
