# 지연 계산 (Lazy Evaluation)

- Level: Intermediate
- Prerequisites: [Algorithms/Complexity.md](../../Algorithms/Complexity.md), [Engineering/Performance/Memoization-Caching.md](Memoization-Caching.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

지연 계산은 값이 실제로 필요할 때까지 계산을 미루는 전략이다. 필요 없는 작업을 하지 않는 것이 핵심 이득이다.

## 직관 (Intuition)

마트에서 살지 말지 모르는 물건을 미리 계산대에 올리지 않는다. 정말 필요해진 순간에만 비용을 낸다.

## 이론 (Theory)

Lazy sequence, generator, stream processing은 memory footprint를 낮추고 early termination을 가능하게 한다. 반대로 evaluation timing이 늦어져 exception 위치가 애매해지고, resource lifetime이 길어질 수 있다. Memoized lazy value는 한 번 계산한 결과를 재사용하지만 invalidation 문제가 생긴다.

## 구현 (Implementation)

```python
def first_even_square(values):
    squares = (x * x for x in values)
    return next(v for v in squares if v % 2 == 0)
```

위 generator는 전체 square list를 만들지 않고 조건을 만족하는 첫 값까지만 계산한다.

## 복잡도 (Complexity)

최악 복잡도는 같아도 실제 비용은 소비한 prefix에 비례할 수 있다. Memory는 materialized collection보다 작아질 수 있다.

## 응용 (Applications)

- large file streaming
- pagination·cursor
- query execution plan
- infinite sequence modeling

## 흔한 오해 (Common Misunderstandings)

- lazy가 항상 빠른 것은 아니다. 반복 iteration은 재계산을 만들 수 있다.
- 지연된 I/O는 resource close 시점을 놓치게 할 수 있다.
- Debugging이 어려워질 수 있다.
- Side effect가 있는 계산을 lazy하게 만들면 순서 문제가 생긴다.

## TMI

- Database query도 실제 materialization 전까지 plan만 쌓는 경우가 많다.
- Functional language의 lazy evaluation은 메모리 누수를 만들기도 한다.
- Backpressure와 결합하면 streaming system에서 중요한 제어 방식이 된다.

## 연습 / 확인 문제 (Exercises)

- list comprehension과 generator expression의 memory 사용량을 비교하라.
- early termination이 있는 pipeline을 eager/lazy로 구현하라.
- lazy evaluation 때문에 exception 발생 위치가 달라지는 예를 만들라.

## 이어서 읽기 (Reading Path)

- 이전: [메모이제이션과 캐싱](Memoization-Caching.md)
- 다음: [락 경합](Lock-Contention.md)

## 참조 (References)

- [Algorithms/Complexity.md](../../Algorithms/Complexity.md)
- [Engineering/System-Design/Caching.md](../System-Design/Caching.md)

