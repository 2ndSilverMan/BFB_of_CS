# 병렬 알고리즘 (Parallel Algorithms)

- Level: Advanced
- Prerequisites: [Algorithms/Divide-and-Conquer.md](Divide-and-Conquer.md), [Algorithms/Complexity.md](Complexity.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

병렬 알고리즘은 여러 프로세서가 동시에 작업을 수행해 문제를 푸는 알고리즘이다. 작업(work)과 깊이(depth/span)로 성능을 분석하며, 분할 정복·스캔·리덕션 같은 패턴이 토대다.

## 직관 (Intuition)

순차 알고리즘은 한 일꾼이 차례로 일한다. 병렬은 여러 일꾼이 동시에 일한다. 하지만 무작정 나눈다고 빨라지지 않는다 — 일을 독립적으로 쪼갤 수 있어야 하고, 합치는 단계가 병목이 된다. "총 일의 양"과 "가장 긴 의존 사슬"을 함께 봐야 진짜 속도를 안다.

## 이론 (Theory)

**작업-깊이 모델**: $W$(work, 총 연산 수), $D$(depth, 임계 경로). $P$개 프로세서에서 시간은 브렌트 정리로

$$T_P \le \frac{W}{P} + D$$

병렬성(parallelism) = $W/D$. **암달의 법칙**: 순차 비율 $s$가 있으면 최대 속도 향상은 $1/s$로 제한된다. **거스타프슨의 법칙**은 문제 크기를 키우면 더 낙관적임을 보인다.

기본 병렬 패턴:
- **리덕션**: 합·최대 등을 트리로 `O(log n)` 깊이.
- **스캔(prefix sum)**: 병렬 접두사 합, work `O(n)`, depth `O(log n)`.
- **병렬 분할 정복**: 병합 정렬 등.

## 구현 (Implementation)

```python
# 병렬 리덕션의 깊이 O(log n) 구조 (개념)
def parallel_reduce(arr, op):
    # 실제로는 스레드/태스크로 동시에 실행
    while len(arr) > 1:
        nxt = []
        for i in range(0, len(arr) - 1, 2):
            nxt.append(op(arr[i], arr[i+1]))   # 쌍을 동시에 결합
        if len(arr) % 2: nxt.append(arr[-1])
        arr = nxt                              # 한 레벨 = 1 depth
    return arr[0]
```

## 복잡도 (Complexity)

| 패턴 | Work | Depth |
|---|---|---|
| 리덕션 | `O(n)` | `O(log n)` |
| 스캔 | `O(n)` | `O(log n)` |
| 병합 정렬(병렬) | `O(n log n)` | `O(log^2 n)` |

work가 순차 알고리즘과 같으면(work-efficient) 이상적이다. depth가 작을수록 더 많은 프로세서로 가속된다.

## 응용 (Applications)

- GPU 연산(딥러닝, 그래픽스)
- 대규모 데이터 처리(MapReduce, Spark)
- 과학 계산·시뮬레이션
- 멀티코어·분산 정렬·검색

## 흔한 오해 (Common Misunderstandings)

- 프로세서를 2배 늘려도 2배 빨라지지 않는다(암달의 법칙, 통신·동기화 비용).
- work가 늘면(비효율적 병렬화) 적은 코어에선 오히려 느릴 수 있다.
- depth만 보면 안 된다 — work와 함께 봐야 실제 성능을 안다.
- 동기화·경쟁 조건·캐시 일관성이 이론적 속도를 깎는다.

## TMI

- 브렌트 정리는 "충분한 프로세서가 없어도 work/P + D면 된다"는 스케줄링 보장을 준다.
- 병렬 접두사 합(Blelloch scan)은 단순해 보이지만 GPU 알고리즘의 핵심 빌딩 블록이다.
- 암달 vs 거스타프슨 논쟁은 "고정 문제 vs 확장 문제"라는 관점 차이에서 비롯된다.

## 연습 / 확인 문제 (Exercises)

- 병렬 리덕션의 깊이가 `O(log n)`인 이유를 트리로 설명하라.
- 순차 비율 10%일 때 암달의 법칙으로 최대 속도 향상을 구하라.
- 병렬 접두사 합의 work와 depth를 분석하라.

## 이어서 읽기 (Reading Path)

- 이전: [계산 기하학](Computational-Geometry.md)
- 다음: [Systems/Parallel-Computing/Parallel-Models.md](../Systems/Parallel-Computing/Parallel-Models.md)

## 참조 (References)

- [Systems/Parallel-Computing/Parallel-Models.md](../Systems/Parallel-Computing/Parallel-Models.md)
- [Algorithms/Divide-and-Conquer.md](Divide-and-Conquer.md)
- [Reference/Books.md](../Reference/Books.md)
