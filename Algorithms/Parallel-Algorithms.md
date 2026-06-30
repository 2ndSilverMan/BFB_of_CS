# 병렬 알고리즘 (Parallel Algorithms)

- Level: Advanced
- Prerequisites: [Algorithms/Divide-and-Conquer.md](Divide-and-Conquer.md), [Algorithms/Complexity.md](Complexity.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

병렬 알고리즘은 여러 프로세서가 동시에 작업해 문제를 푼다. **작업(work, $W$)** 과 **깊이(depth/span, $D$)** 로 성능을 분석하며, 리덕션·스캔·분할 정복이 토대다.

## 직관 (Intuition)

순차는 한 일꾼이 차례로, 병렬은 여러 일꾼이 동시에. 하지만 무작정 나눈다고 빨라지지 않는다 — 독립적으로 쪼갤 수 있어야 하고 **합치는 단계가 병목**이다. "총 일의 양($W$)"과 "가장 긴 의존 사슬($D$)"을 함께 봐야 진짜 속도를 안다.

## 이론 (Theory)

### 1. 작업-깊이 모델과 Brent 정리

$P$ 개 프로세서에서 시간:

$$T_P \le \frac{W}{P} + D$$

병렬성(parallelism) $=W/D$ (프로세서를 더 줘도 이 이상 못 빨라짐). **work-efficient** = $W$ 가 최선 순차와 같음(이게 안 되면 적은 코어에서 오히려 느려진다).

### 2. Amdahl vs Gustafson

순차 비율 $s$ 면 **암달**: 최대 속도향상 $\le1/s$ (고정 문제). **거스타프슨**: 문제를 키우면 $s+P(1-s)$ 로 더 낙관적(확장 문제) — 두 법칙은 "고정 vs 확장 문제"의 관점 차이.

### 3. 핵심 패턴

- **리덕션**: 합·최대를 트리로 $W=O(n), D=O(\log n)$.
- **스캔(prefix sum, Blelloch)**: up-sweep(리덕션) + down-sweep, $W=O(n), D=O(\log n)$ — work-efficient.
- **병렬 분할 정복**: 병합 정렬 $W=O(n\log n), D=O(\log^2 n)$.

## 구현 (Implementation)

```python
def parallel_reduce(arr, op):                 # 깊이 O(log n): 쌍을 동시에 결합
    while len(arr) > 1:                        # 한 레벨 = depth 1 (실제론 동시 실행)
        nxt = [op(arr[i], arr[i+1]) for i in range(0, len(arr)-1, 2)]
        if len(arr) % 2: nxt.append(arr[-1])
        arr = nxt
    return arr[0]

def prefix_sum_sequential(a):                 # 병렬 스캔의 결과(검증용)
    out, acc = [], 0
    for x in a: acc += x; out.append(acc)
    return out
```

## 복잡도 (Complexity)

| 패턴 | Work | Depth |
|---|---|---|
| 리덕션 | $O(n)$ | $O(\log n)$ |
| 스캔(Blelloch) | $O(n)$ | $O(\log n)$ |
| 병합 정렬(병렬) | $O(n\log n)$ | $O(\log^2 n)$ |

**워크드 예제(암달).** 순차 비율 $s=10\%$, 무한 프로세서 → 최대 속도향상 $1/0.1=10$ 배. $P=4$ 면 $1/(0.1+0.9/4)=1/0.325\approx3.08$ 배.

## 응용 (Applications)

- GPU 연산(딥러닝·그래픽스), 대규모 데이터(MapReduce·Spark).
- 과학 계산·시뮬레이션, 멀티코어 정렬·검색.

## 흔한 오해 (Common Misunderstandings)

- **프로세서 2배 ≠ 2배 빠름**(암달, 통신·동기화 비용).
- **work가 늘면(비효율 병렬화) 적은 코어에선 오히려 느릴 수 있다**.
- **depth만 보면 안 된다** — $W$ 와 함께 봐야 실제 성능.
- **동기화·경쟁 조건·캐시 일관성**이 이론 속도를 깎는다([동시성 제어](../Systems/Operating-Systems/Synchronization.md)).

## TMI

- Brent 정리는 "충분한 프로세서가 없어도 $W/P+D$ 면 된다"는 스케줄링 보장을 준다(work-stealing의 이론적 근거).
- Blelloch 스캔은 단순해 보여도 GPU 알고리즘(정렬·압축·그래프)의 핵심 빌딩 블록이다.
- PRAM 모델(EREW/CREW/CRCW)은 동시 메모리 접근 규칙으로 병렬 이론을 분류한다.

## 연습 / 확인 문제 (Exercises)

- 병렬 리덕션 깊이가 $O(\log n)$ 인 이유를 트리로 설명하라.
- 순차 비율 10%일 때 암달의 법칙으로 $P=4,\infty$ 의 속도향상을 구하라.
- Blelloch 스캔의 up-sweep/down-sweep가 왜 work-efficient($O(n)$)인지 설명하라.
- 병렬 병합 정렬의 depth가 왜 $O(\log^2 n)$ 인지 분석하라.

## 이어서 읽기 (Reading Path)

- 이전: [계산 기하학](Computational-Geometry.md)
- 다음: [병렬 모델](../Systems/Parallel-Computing/Parallel-Models.md)
- 관련: [분할 정복](Divide-and-Conquer.md), [동기화](../Systems/Operating-Systems/Synchronization.md)

## 참조 (References)

- [Systems/Parallel-Computing/Parallel-Models.md](../Systems/Parallel-Computing/Parallel-Models.md)
- [Algorithms/Divide-and-Conquer.md](Divide-and-Conquer.md)
- [Reference/Books.md](../Reference/Books.md)
