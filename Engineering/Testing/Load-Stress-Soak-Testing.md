# 부하 테스트, 스트레스 테스트, 소크 테스트

- Level: Intermediate
- Prerequisites: [Engineering/Performance/Benchmarking-Basics.md](../Performance/Benchmarking-Basics.md), [Engineering/System-Design/Scalability.md](../System-Design/Scalability.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

부하 테스트는 예상 트래픽에서 성능을 확인하고, 스트레스 테스트는 한계를 넘겨 붕괴 지점을 찾고, 소크 테스트는 긴 시간 동안 자원 누수와 성능 저하를 찾는다.

## 직관 (Intuition)

부하 테스트는 평일 점심 장사, 스트레스 테스트는 갑작스러운 축제 인파, 소크 테스트는 며칠 동안 계속 문을 열었을 때 냉장고와 직원 체력이 버티는지 보는 것이다.

## 이론 (Theory)

성능 테스트는 workload model, arrival rate, concurrency, think time, data distribution을 정의해야 한다. 평균 latency보다 percentile과 error rate가 중요하다. System under test와 dependency capacity를 분리해 본다.

### 세 테스트의 목적 차이

Load test는 예상 부하에서 SLO를 만족하는지 확인한다. Stress test는 한계를 넘어 어디서 어떻게 무너지는지 찾는다. Soak test는 긴 시간 동안 memory leak, connection leak, cache growth, log volume 같은 누적 문제를 찾는다.

결과 해석에는 latency percentile, error rate, saturation, queue length, GC, DB lock, downstream dependency를 함께 봐야 한다. 평균 latency만 보면 tail failure를 놓친다.

## 구현 (Implementation)

```text
scenario: login -> search -> checkout
target: 500 rps
SLO: p95 latency < 300ms, error rate < 1%
```

## 복잡도 (Complexity)

테스트 환경이 production과 다르면 결과 해석이 어렵다. 부하 생성기도 병목이 될 수 있어 generator metric도 확인한다.

## 응용 (Applications)

- release 전 capacity 검증
- autoscaling 정책 검증
- memory leak 탐지
- overload 보호 확인

## 흔한 오해 (Common Misunderstandings)

- 평균 응답 시간만 보면 tail latency를 놓친다.
- 작은 테스트 환경 결과를 production에 그대로 외삽하면 위험하다.
- 스트레스 테스트는 고객 영향이 없는 격리 환경에서 해야 한다.
- 캐시가 이미 warm한 상태만 보면 cold start 문제를 놓친다.

## TMI

- Soak test는 몇 시간에서 며칠 동안 누수와 누적 지연을 본다.
- Spike test는 급격한 트래픽 증가를 다룬다.
- Load shedding과 rate limiting은 스트레스 테스트에서 검증할 중요한 방어다.

## 연습 / 확인 문제 (Exercises)

- API의 부하 테스트 시나리오와 SLO를 정의하라.
- Stress test와 soak test의 목적 차이를 설명하라.
- 부하 테스트 결과에서 병목을 찾는 절차를 작성하라.

## 이어서 읽기 (Reading Path)

- 이전: [벤치마킹 기초](../Performance/Benchmarking-Basics.md)
- 다음: [k6/JMeter](K6-JMeter.md), [성능 공학](../Performance/)

## 참조 (References)

- [Engineering/Performance/Benchmarking-Basics.md](../Performance/Benchmarking-Basics.md)
- [Engineering/System-Design/Scalability.md](../System-Design/Scalability.md)
