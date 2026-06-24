# 비동기 I/O (Async I/O)

- Level: Intermediate
- Prerequisites: [Systems/Operating-Systems/IO-and-Drivers.md](../../Systems/Operating-Systems/IO-and-Drivers.md), [Systems/Networks/Socket-Programming.md](../../Systems/Networks/Socket-Programming.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

비동기 I/O는 I/O 완료를 기다리는 동안 thread를 막지 않고 다른 작업을 처리하게 하는 concurrency 모델이다.

## 직관 (Intuition)

음식이 나올 때까지 주방 앞에서 멈춰 있지 않고, 번호표를 받아 다른 일을 하다가 알림이 오면 돌아온다.

## 이론 (Theory)

Event loop는 readiness나 completion event를 받아 callback·coroutine을 실행한다. Non-blocking socket, epoll/kqueue/IOCP, io_uring 같은 OS primitive가 기반이다. Async는 I/O-bound concurrency에 강하지만 CPU-bound 작업이 event loop를 점유하면 전체 latency가 나빠진다. Cancellation과 timeout 전파가 중요하다.

## 구현 (Implementation)

```python
import asyncio

async def fetch_like(i):
    await asyncio.sleep(0.1)
    return i

async def main():
    results = await asyncio.gather(*(fetch_like(i) for i in range(10)))
    print(results)

asyncio.run(main())
```

## 복잡도 (Complexity)

동시 요청 수가 많을수록 thread-per-request보다 memory와 context switch 부담이 작다. 하지만 callback scheduling과 state machine overhead는 존재한다.

## 응용 (Applications)

- high-concurrency web server
- proxy·gateway
- chat·streaming service
- bulk API client

## 흔한 오해 (Common Misunderstandings)

- async는 parallel CPU execution을 자동 제공하지 않는다.
- blocking call 하나가 event loop 전체를 멈출 수 있다.
- timeout 없는 async 작업은 resource leak이 된다.
- coroutine을 만들기만 하고 await하지 않으면 실행되지 않을 수 있다.

## TMI

- io_uring은 Linux에서 submission/completion queue 기반으로 async I/O 비용을 줄이려는 인터페이스다.
- Structured concurrency는 task lifetime을 scope와 묶어 누수를 줄인다.
- Backpressure 없는 async pipeline은 memory를 빠르게 소모한다.

## 연습 / 확인 문제 (Exercises)

- 순차 sleep과 `gather` sleep의 총 시간을 비교하라.
- event loop 안에서 blocking sleep을 호출해 문제를 재현하라.
- timeout과 cancellation을 포함한 async API를 설계하라.

## 이어서 읽기 (Reading Path)

- 이전: [스레드 풀 튜닝](Thread-Pool-Tuning.md)
- 다음: [데이터베이스 쿼리 최적화](Database-Query-Optimization.md)

## 참조 (References)

- [Systems/Operating-Systems/IO-and-Drivers.md](../../Systems/Operating-Systems/IO-and-Drivers.md)
- [Systems/Networks/Socket-Programming.md](../../Systems/Networks/Socket-Programming.md)

