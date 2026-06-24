# 동시성 모델 (Concurrency Models)

- Level: Advanced
- Prerequisites: [Memory-Models.md](Memory-Models.md), [Systems/Operating-Systems/Synchronization.md](../../Systems/Operating-Systems/Synchronization.md), [Systems/Parallel-Computing/Multithreading.md](../../Systems/Parallel-Computing/Multithreading.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

동시성 모델은 여러 작업이 겹쳐 실행될 때 언어와 런타임이 작업 생성, 통신, 동기화, 메모리 공유를 어떻게 다루는지 정하는 규칙이다. thread/lock, actor, async/await, CSP, STM 등이 대표적이다.

## 직관 (Intuition)

여러 사람이 같은 문서를 동시에 고치면 충돌이 생긴다. 어떤 조직은 자물쇠를 쓰고, 어떤 조직은 메시지로 요청만 보내고, 어떤 조직은 변경 제안을 트랜잭션처럼 합친다. 동시성 모델은 이런 협업 규칙이다.

## 이론 (Theory)

대표 모델은 다음과 같다.

- Thread + lock: 공유 메모리에 mutex, semaphore, condition variable을 사용한다.
- Actor model: actor가 독립 상태를 갖고 메시지로 통신한다.
- CSP/channel: 프로세스나 goroutine이 channel로 값을 주고받는다.
- async/await: non-blocking I/O를 continuation/task로 표현한다.
- STM: 공유 상태 변경을 트랜잭션처럼 다룬다.

동시성 모델은 race condition, deadlock, starvation, backpressure, cancellation 같은 문제를 어떻게 노출하거나 숨기는지에 차이가 있다.

## 구현 (Implementation)

async/await는 I/O 대기 중 thread를 점유하지 않도록 표현할 수 있다.

```python
import asyncio


async def fetch_like(name):
    await asyncio.sleep(0.1)
    return name


async def main():
    results = await asyncio.gather(fetch_like("a"), fetch_like("b"))
    print(results)
```

CPU-bound 병렬성과 I/O concurrency는 구분해야 한다.

## 복잡도 (Complexity)

동시성 모델은 프로그램 구조 복잡도에 큰 영향을 준다. lock 기반 모델은 성능이 좋을 수 있지만 correctness가 어렵고, actor/async 모델은 공유 상태를 줄이는 대신 메시지 흐름과 backpressure 관리가 중요해진다.

## 응용 (Applications)

- 서버 I/O 처리
- UI event loop
- actor 기반 분산 시스템
- 안전한 병렬 처리 언어 설계

## 흔한 오해 (Common Misunderstandings)

- 동시성과 병렬성은 다르다. 동시성은 구조, 병렬성은 실제 동시 실행이다.
- async는 CPU 작업을 자동으로 병렬화하지 않는다.
- actor 모델도 메시지 순서와 mailbox 폭주 문제를 고려해야 한다.
- lock을 없애면 모든 동시성 버그가 사라지는 것은 아니다.

## TMI

- Go의 goroutine/channel은 CSP 스타일을 실용적으로 만든 사례다.
- Erlang/Elixir의 actor 모델은 fault tolerance와 supervision tree로 유명하다.
- Rust는 ownership과 Send/Sync trait으로 데이터 race를 컴파일 타임에 줄인다.

## 연습 / 확인 문제 (Exercises)

- 동시성과 병렬성의 차이를 예로 설명하라.
- actor 모델이 공유 상태 문제를 줄이는 이유를 말하라.
- async/await가 I/O-bound 서버에 유리한 이유를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [메모리 관리 모델](Memory-Models.md)
- 다음: [CS-Theory/Compilers/](../Compilers/)

## 참조 (References)

- [Systems/Operating-Systems/Synchronization.md](../../Systems/Operating-Systems/Synchronization.md)
- [Systems/Parallel-Computing/Multithreading.md](../../Systems/Parallel-Computing/Multithreading.md)
- [Memory-Models.md](Memory-Models.md)
- [Reference/Books.md](../../Reference/Books.md)
