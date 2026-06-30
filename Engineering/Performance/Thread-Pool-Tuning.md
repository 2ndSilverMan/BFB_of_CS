# 스레드 풀 튜닝 (Thread Pool Tuning)

- Level: Intermediate
- Prerequisites: [Systems/Operating-Systems/Scheduling.md](../../Systems/Operating-Systems/Scheduling.md), [Systems/Operating-Systems/Processes-and-Threads.md](../../Systems/Operating-Systems/Processes-and-Threads.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

스레드 풀 튜닝은 worker 수, queue 크기, rejection policy, task granularity를 조정해 throughput과 latency를 균형 있게 맞추는 작업이다.

## 직관 (Intuition)

일꾼이 너무 적으면 줄이 길어지고, 너무 많으면 서로 자리를 뺏느라 느려진다. 적정 수는 작업 성격에 따라 달라진다.

## 이론 (Theory)

CPU-bound 작업은 core 수 근처가 적절한 경우가 많고, I/O-bound 작업은 wait time 때문에 더 많은 concurrency가 필요할 수 있다. Queue가 무한하면 overload가 latency로 숨고, queue가 너무 작으면 burst를 흡수하지 못한다. Backpressure, timeout, cancellation이 함께 설계되어야 한다.

### Pool 크기와 작업 성격

스레드 풀 크기는 CPU-bound와 I/O-bound 작업에서 다르게 정한다. CPU-bound는 core 수 근처가 출발점이고, I/O-bound는 대기 비율에 따라 더 클 수 있다. 하지만 너무 큰 풀은 context switch, memory, lock contention을 늘린다.

Queue length, active thread, task wait time, rejection count를 함께 봐야 한다. Thread 수만 늘려 throughput이 오르지 않으면 downstream 병목이나 lock 경합을 의심한다.

## 구현 (Implementation)

```python
from concurrent.futures import ThreadPoolExecutor

def handle(item):
    return item * item

with ThreadPoolExecutor(max_workers=8) as pool:
    results = list(pool.map(handle, range(1000)))
```

실제 서비스에서는 worker 수를 CPU, blocking ratio, downstream capacity, p95 latency로 조정한다.

## 복잡도 (Complexity)

Task 수가 `n`이고 평균 처리 시간이 `c`라면 이상적 시간은 `n*c/workers`지만 scheduling, context switch, queueing, lock 비용이 붙는다.

## 응용 (Applications)

- web request handler
- background job worker
- file processing pipeline
- RPC client concurrency 제한

## 흔한 오해 (Common Misunderstandings)

- 스레드를 늘리면 항상 빨라지지 않는다.
- 무한 queue는 장애를 늦게 터뜨릴 뿐이다.
- CPU-bound 작업에 너무 많은 thread는 context switching을 늘린다.
- Downstream limit을 무시하면 전체 시스템을 과부하시킨다.

## TMI

- Little's Law는 concurrency, throughput, latency 관계를 직관적으로 설명한다.
- Work stealing pool은 task imbalance를 줄이는 데 도움이 된다.
- Async runtime도 내부적으로 thread pool과 blocking pool을 구분하는 경우가 많다.

## 연습 / 확인 문제 (Exercises)

- worker 수를 바꾸며 throughput과 p95 latency를 측정하라.
- queue size 제한과 rejection policy를 설계하라.
- CPU-bound와 I/O-bound 작업의 적정 worker 차이를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [락 경합](Lock-Contention.md)
- 다음: [비동기 I/O](Async-IO.md)

## 참조 (References)

- [Systems/Operating-Systems/Scheduling.md](../../Systems/Operating-Systems/Scheduling.md)
- [Systems/Parallel-Computing/Multithreading.md](../../Systems/Parallel-Computing/Multithreading.md)
