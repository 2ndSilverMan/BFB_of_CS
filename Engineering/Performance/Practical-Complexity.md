# 실전 복잡도 분석 (Practical Complexity)

- Level: Intermediate
- Prerequisites: [Algorithms/Complexity.md](../../Algorithms/Complexity.md), [Engineering/Performance/Benchmarking-Basics.md](Benchmarking-Basics.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

실전 복잡도 분석은 Big-O뿐 아니라 입력 크기, 상수 인자, cache locality, allocation, branch, I/O 비용을 함께 보는 성능 판단이다.

## 직관 (Intuition)

`O(n log n)`이 항상 `O(n)`보다 느린 것은 아니다. 실제 데이터 크기와 하드웨어 비용이 큰 결정을 만든다.

## 이론 (Theory)

Asymptotic complexity는 큰 입력에서 증가율을 설명하지만, production에서는 특정 입력 분포와 한정된 범위가 중요하다. Constant factor, memory hierarchy, vectorization, parallelism, algorithm stability, worst-case guardrail을 함께 검토한다. 성능 선택은 benchmark와 correctness risk를 같이 비교해야 한다.

## 구현 (Implementation)

```python
def choose_strategy(n: int) -> str:
    if n < 64:
        return "simple_scan"
    if n < 100_000:
        return "hash_index"
    return "partitioned_or_streaming"
```

실제 시스템에서는 threshold를 추측하지 않고 benchmark와 telemetry로 정한다.

## 복잡도 (Complexity)

복잡도 표기는 방향을 알려 주지만 실행 시간은 `algorithm cost + runtime overhead + memory/I/O cost`에 가깝다.

## 응용 (Applications)

- 자료구조 선택
- batch size·threshold 결정
- query plan 해석
- 성능 회귀 triage

## 흔한 오해 (Common Misunderstandings)

- Big-O가 같으면 성능도 같다고 볼 수 없다.
- 평균 case만 보고 adversarial input을 무시하면 장애가 날 수 있다.
- Microbenchmark로 전체 시스템 성능을 단정하면 안 된다.
- 가장 복잡한 알고리즘이 항상 실무적으로 최선은 아니다.

## TMI

- Small vector optimization처럼 작은 입력에 특화한 구현이 많다.
- Hash table은 평균 `O(1)`이지만 hash 품질과 load factor에 민감하다.
- Database optimizer도 결국 비용 모델로 실전 복잡도를 추정한다.

## 연습 / 확인 문제 (Exercises)

- 작은 n에서 insertion sort와 quicksort를 비교하라.
- hash table과 sorted array lookup을 입력 크기별로 측정하라.
- Big-O로 설명되지 않는 차이를 profile로 찾아라.

## 이어서 읽기 (Reading Path)

- 이전: [False Sharing](False-Sharing.md)
- 다음: [메모이제이션과 캐싱](Memoization-Caching.md)

## 참조 (References)

- [Algorithms/Complexity.md](../../Algorithms/Complexity.md)
- [Data-Structures/Hash-Table.md](../../Data-Structures/Hash-Table.md)

