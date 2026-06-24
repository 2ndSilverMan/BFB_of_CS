# CPU 프로파일링 (CPU Profiling)

- Level: Intermediate
- Prerequisites: [Engineering/Performance/Benchmarking-Basics.md](Benchmarking-Basics.md), [Systems/Operating-Systems/Scheduling.md](../../Systems/Operating-Systems/Scheduling.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

CPU 프로파일링은 프로그램이 CPU 시간을 어디서 소비하는지 call stack·function·source line별로 측정한다. Sampling은 주기적으로 stack을 관찰하고 instrumentation은 호출에 측정 코드를 삽입한다.

## 직관 (Intuition)

모든 코드를 추측으로 고치지 않고 실제 시간이 몰린 hot path를 찾는다. 표본을 많이 모으면 각 함수가 실행 중일 확률이 소비 시간 비율을 근사한다.

## 이론 (Theory)

On-CPU와 off-CPU 시간을 구분한다. Self time은 함수 자체, inclusive time은 child call을 포함한다. Sampling frequency가 너무 낮으면 짧은 hotspot을 놓치고 너무 높으면 overhead가 커진다. Release-like workload와 symbol·stack unwinding 품질이 중요하다.

## 구현 (Implementation)

```python
import cProfile
import pstats


def workload():
    return sum(i * i for i in range(1_000_000))


profiler = cProfile.Profile()
profiler.runcall(workload)
pstats.Stats(profiler).sort_stats("cumulative").print_stats(10)
```

## 복잡도 (Complexity)

Sampling overhead는 frequency와 stack depth에, instrumentation overhead는 event 수에 비례한다. 결과 저장·symbolization 비용도 대규모 서비스에서는 고려한다.

## 응용 (Applications)

- hotspot·unexpected call 탐색
- lock·serialization·allocation 비용 분석
- 성능 회귀 원인 추적
- flame graph 입력 수집

## 흔한 오해 (Common Misunderstandings)

- CPU profile에 안 보이는 시간이 I/O·lock wait일 수 있다.
- debug build 결과가 production 최적화 build를 대표하지 않을 수 있다.
- 가장 자주 호출된 함수가 가장 많은 시간을 쓰는 함수는 아니다.
- profiler overhead를 무시하면 작은 차이를 오해한다.

## TMI

- flame graph 폭은 일반적으로 stack sample 비율이지 시간 순서가 아니다.
- off-CPU profiling은 sleep·I/O·lock wait stack을 분석한다.
- hardware performance counter로 cache miss·branch miss를 측정할 수 있다.

## 연습 / 확인 문제 (Exercises)

- self와 cumulative time 차이를 예제로 설명하라.
- I/O-bound workload가 CPU profile에서 어떻게 보이는지 확인하라.
- hotspot 하나를 최적화하고 benchmark로 효과를 검증하라.

## 이어서 읽기 (Reading Path)

- 이전: [벤치마킹 기초](Benchmarking-Basics.md)
- 다음: [캐시 친화적 코드](Cache-Friendly-Code.md)

## 참조 (References)

- [Systems/Operating-Systems/Scheduling.md](../../Systems/Operating-Systems/Scheduling.md)
- [Reference/Books.md](../../Reference/Books.md)
