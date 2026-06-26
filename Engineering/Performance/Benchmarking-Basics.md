# 벤치마킹 기초 (Benchmarking Basics)

- Level: Intermediate
- Prerequisites: [Algorithms/Complexity.md](../../Algorithms/Complexity.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

벤치마킹은 정의된 workload에서 시간, throughput, latency, resource 사용을 반복 측정하고 비교하는 절차다. Microbenchmark는 작은 연산, macrobenchmark는 실제 user flow·system을 측정한다.

## 직관 (Intuition)

스톱워치 숫자 하나보다 같은 조건의 여러 측정과 분포가 중요하다. 무엇을 얼마나 빠르게 만들려는지 먼저 정의해야 숫자가 의사결정으로 이어진다.

## 이론 (Theory)

Latency는 요청 하나의 시간, throughput은 단위 시간 처리량이다. 평균만으로 tail을 숨길 수 있어 median, p95, p99를 함께 본다. warmup, cache, JIT, CPU frequency, background load, input size를 통제하고 baseline과 동일 환경에서 비교한다.

## 구현 (Implementation)

```python
import statistics
import time


def benchmark(fn, repeats=100):
    samples = []
    for _ in range(repeats):
        start = time.perf_counter_ns()
        fn()
        samples.append(time.perf_counter_ns() - start)
    return {"median_ns": statistics.median(samples),
            "min_ns": min(samples)}
```

## 복잡도 (Complexity)

반복 $R$, workload 비용 $C$면 측정 비용은 `O(RC)`다. 짧은 연산은 harness overhead가 지배하므로 묶어서 반복하거나 전용 도구를 사용한다.

## 응용 (Applications)

- 성능 회귀 CI
- 최적화 전후 비교
- capacity planning
- algorithm·library 선택

## 흔한 오해 (Common Misunderstandings)

- 한 번의 최솟값은 대표 성능이 아니다.
- synthetic benchmark가 production workload를 항상 대표하지 않는다.
- 평균 latency만으로 user experience를 설명할 수 없다.
- measurement instrumentation 자체가 결과에 영향을 줄 수 있다.

## TMI

- coordinated omission은 load generator가 느린 동안 요청을 덜 보내 tail latency를 축소한다.
- benchmark 결과에는 hardware·software version과 raw sample을 함께 남기는 편이 좋다.
- optimization은 측정 가능한 병목에서 시작해야 한다.

## 연습 / 확인 문제 (Exercises)

- list와 set lookup을 입력 크기별로 측정하라.
- mean과 p99가 크게 다른 sample을 분석하라.
- warmup 유무에 따른 결과를 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [복잡도 분석](../../Algorithms/Complexity.md)
- 다음: [CPU 프로파일링](CPU-Profiling.md)
- 관련: [부하 테스트, 스트레스 테스트, 소크 테스트](../Testing/Load-Stress-Soak-Testing.md)

## 참조 (References)

- [Algorithms/Complexity.md](../../Algorithms/Complexity.md)
- [Reference/Books.md](../../Reference/Books.md)
