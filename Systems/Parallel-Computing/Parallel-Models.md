# 병렬 컴퓨팅 모델 (Parallel Computing Models)

- Level: Intermediate
- Prerequisites: [Systems/Operating-Systems/Processes-and-Threads.md](../Operating-Systems/Processes-and-Threads.md), [Systems/Distributed-Systems/System-Models.md](../Distributed-Systems/System-Models.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

병렬 컴퓨팅 모델은 여러 처리 요소가 작업과 데이터를 나누고 통신하는 방식을 설명한다. 공유 메모리, 분산 메모리, data parallel, task parallel이 대표적이다.

## 직관 (Intuition)

여러 요리사가 한 주방과 재료를 공유하면 빠르게 협력하지만 충돌을 조정해야 한다. 각자 주방이 따로 있으면 충돌은 적지만 재료와 결과를 메시지로 주고받아야 한다.

## 이론 (Theory)

공유 메모리는 thread가 같은 address space를 사용해 lock·atomic·memory consistency가 중요하다. 분산 메모리는 process별 memory와 message passing을 사용해 communication latency·partitioning이 핵심이다.

| 모델 | 강점 | 주요 비용 |
|---|---|---|
| Shared memory | 낮은 통신 지연 | race, contention, cache coherence |
| Distributed memory | 확장성과 failure isolation | serialization, network, partition |
| Data parallel | 동일 연산의 대량 적용 | load imbalance, reduction |
| Task parallel | 서로 다른 작업 동시 실행 | dependency scheduling |

## 구현 (Implementation)

```python
from concurrent.futures import ProcessPoolExecutor


def square(x):
    return x * x


with ProcessPoolExecutor() as pool:
    print(list(pool.map(square, range(8))))
```

작은 작업은 process 생성·직렬화 비용이 계산 이득보다 클 수 있다.

## 복잡도 (Complexity)

이상적 시간은 $T_1/p$지만 실제로는 $T_p=T_1/p+T_{comm}+T_{sync}+T_{imbalance}$에 가깝다. work와 span 관점에서 $T_p\ge\max(T_1/p,T_\infty)$다.

## 응용 (Applications)

- multicore server와 HPC cluster
- distributed data processing
- GPU batch computation
- pipeline·workflow execution

## 흔한 오해 (Common Misunderstandings)

- core 수를 두 배로 늘려도 항상 두 배 빨라지지 않는다.
- concurrency와 parallelism은 관련되지만 동일하지 않다.
- shared memory도 cache coherence라는 통신 비용이 있다.
- 작업 수만 균등해도 계산량이 균등하다는 보장은 없다.

## TMI

- BSP는 local computation, communication, barrier를 superstep으로 묶는다.
- fork-join은 recursive task parallelism에 잘 맞는다.
- NUMA에서는 같은 shared memory라도 접근 위치에 따라 latency가 다르다.

## 연습 / 확인 문제 (Exercises)

- matrix multiplication을 data parallel task로 나눠라.
- shared와 distributed memory에서 reduction을 비교하라.
- work/span으로 가능한 speedup 상한을 계산하라.

## 이어서 읽기 (Reading Path)

- 이전: [프로세스와 스레드](../Operating-Systems/Processes-and-Threads.md)
- 다음: [멀티스레딩](Multithreading.md)

## 참조 (References)

- [Systems/Operating-Systems/Processes-and-Threads.md](../Operating-Systems/Processes-and-Threads.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
