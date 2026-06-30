# 확장성 (Scalability)

- Level: Intermediate
- Prerequisites: [Engineering/System-Design/Approach.md](Approach.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

확장성은 load가 증가할 때 resource를 추가해 목표 성능·신뢰성을 유지하는 능력이다. Scale up은 한 node를 크게, scale out은 node 수를 늘린다.

## 직관 (Intuition)

한 계산대를 빠르게 만드는 것과 계산대를 여러 개 여는 차이다. 여러 계산대는 더 확장되지만 queue 분배, shared inventory, failure 조정이 필요하다.

## 이론 (Theory)

Stateless service는 load balancer 뒤 replica를 늘리기 쉽다. Stateful tier는 partitioning, replication, consistency가 필요하다. Amdahl 법칙은 serial fraction $s$가 speedup을 제한한다.

$$S(p)=\frac{1}{s+(1-s)/p}$$

Throughput·latency·queue length·saturation을 함께 보고 load test로 knee point를 찾는다. Autoscaling은 관측 지연과 startup time 때문에 reactive lag가 있다.

## 구현 (Implementation)

```python
def amdahl_speedup(serial_fraction, workers):
    return 1 / (serial_fraction + (1 - serial_fraction) / workers)


print(amdahl_speedup(0.1, 16))
```

## 복잡도 (Complexity)

Scale out은 capacity를 늘리지만 coordination·network·replication overhead도 증가한다. Queueing에서는 utilization이 100%에 가까워질수록 latency가 비선형적으로 커진다.

## 응용 (Applications)

- web service replica·autoscaling
- database sharding·read replica
- batch·stream parallelism
- regional deployment

## 흔한 오해 (Common Misunderstandings)

- horizontal scaling이 state를 자동 분산하지 않는다.
- CPU utilization 하나만으로 autoscaling하면 queue·I/O 병목을 놓칠 수 있다.
- replica 증가가 downstream capacity도 늘리지는 않는다.
- scalability와 availability는 동일 개념이 아니다.

## TMI

- Little's Law $L=\lambda W$는 동시 처리량, arrival rate, latency를 연결한다.
- hot partition은 전체 평균 capacity가 남아도 병목을 만든다.
- load shedding은 overload에서 일부 요청을 빠르게 거부해 전체 붕괴를 막는다.

## 연습 / 확인 문제 (Exercises)

- serial fraction 5%의 최대 speedup을 계산하라.
- stateless API와 database 확장 전략을 비교하라.
- overload 보호 정책을 설계하라.

## 이어서 읽기 (Reading Path)

- 이전: [시스템 설계 접근](Approach.md)
- 다음: [캐싱](Caching.md)
- 관련: [데이터베이스 선택과 샤딩](Database-Design.md)

## 참조 (References)

- [Systems/Distributed-Systems/Partitioning.md](../../Systems/Distributed-Systems/Partitioning.md)
- [Reference/Papers.md](../../Reference/Papers.md)
- [Reference/Books.md](../../Reference/Books.md)
