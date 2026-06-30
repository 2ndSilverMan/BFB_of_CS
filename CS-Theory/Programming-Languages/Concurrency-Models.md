# 동시성 모델 (Concurrency Models)

- Level: Advanced
- Prerequisites: [Memory-Models.md](Memory-Models.md), [Systems/Operating-Systems/Synchronization.md](../../Systems/Operating-Systems/Synchronization.md), [Systems/Parallel-Computing/Multithreading.md](../../Systems/Parallel-Computing/Multithreading.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

동시성 모델은 여러 작업이 겹쳐 실행될 때 **작업 생성·통신·동기화·메모리 공유**를 어떻게 다루는지 정하는 규칙이다. thread/lock, actor, CSP/channel, async/await, STM이 대표 — 각각 race·deadlock 같은 위험을 *노출하거나 숨기는* 방식이 다르다.

## 직관 (Intuition)

여러 사람이 같은 문서를 동시에 고치면 충돌한다. 자물쇠를 쓰거나(lock), 메시지로 요청만 보내거나(actor), 변경을 트랜잭션으로 합친다(STM). 핵심 구분: **동시성(구조: 겹쳐 다룸) ≠ 병렬성(실제 동시 실행)** — 단일 코어에서도 동시성은 가능하다.

## 이론 (Theory)

### 1. 모델 비교

| 모델 | 공유 상태 | 통신 | 주 위험 | 예 |
|---|---|---|---|---|
| thread + lock | 공유 메모리 | mutex/조건변수 | deadlock·race | pthreads, Java |
| actor | 없음(독립) | 비동기 메시지 | mailbox 폭주·순서 | Erlang, Akka |
| CSP/channel | 없음 | 동기 channel | channel deadlock | Go, occam |
| async/await | 공유(단일 스레드 흔함) | continuation | blocking이 루프 정지 | JS, Python |
| STM | 트랜잭션 메모리 | 낙관적 커밋 | 충돌 재시도 | Haskell, Clojure |

### 2. deadlock의 4조건(Coffman)

상호 배제 + 점유 대기 + 비선점 + **순환 대기** 가 모두 성립해야 deadlock — 하나라도 깨면(예: 락 순서 고정) 막는다([동기화](../../Systems/Operating-Systems/Synchronization.md)).

### 3. backpressure

생산이 소비보다 빠르면 큐가 무한히 자란다 → actor mailbox·channel·async 큐는 **backpressure**(한계 + 흐름 제어)로 생산자를 늦춰야 메모리 폭발을 막는다.

## 구현 (Implementation)

```python
import asyncio
async def fetch(name):
    await asyncio.sleep(0.1); return name          # I/O 대기 중 스레드 안 잡음

async def main():
    # 독립 I/O를 동시에 → 총 ~0.1s(직렬이면 0.2s). 단, CPU 병렬화는 아님
    print(await asyncio.gather(fetch("a"), fetch("b")))
```

```go
// CSP (Go): 공유 메모리 대신 channel로 통신
ch := make(chan int)
go func() { ch <- compute() }()   // goroutine이 결과를 channel로
result := <-ch                     // 받기(동기화 겸 통신)
```

## 복잡도 (Complexity)

| 모델 | correctness | 성능 |
|---|---|---|
| lock | 어려움(race·deadlock) | 좋을 수 있음 |
| actor/CSP | 공유 줄여 추론 쉬움 | 메시지·복사 오버헤드 |
| async | 단일 스레드라 race 적음 | I/O 중첩, CPU엔 무이득 |

## 응용 (Applications)

- 서버 I/O 처리(async), UI 이벤트 루프.
- actor 기반 분산 시스템(fault tolerance), 안전 병렬 언어 설계.

## 흔한 오해 (Common Misunderstandings)

- **동시성 ≠ 병렬성** — 구조 vs 실제 동시 실행.
- **async는 CPU 작업을 병렬화하지 않는다** — I/O 중첩일 뿐(CPU는 워커/프로세스).
- **actor도 메시지 순서·mailbox 폭주**를 고려해야 한다.
- **lock을 없앤다고 모든 버스가 사라지지 않는다** — lock-free에도 ABA·메모리 순서 문제.

## TMI

- Go의 goroutine/channel은 "Don't communicate by sharing memory; share memory by communicating"라는 CSP 철학을 대중화했다.
- Erlang/Elixir의 actor + supervision tree는 "let it crash" 철학으로 fault tolerance를 얻는다.
- Rust는 ownership + `Send`/`Sync` trait으로 **데이터 race를 컴파일 타임에** 차단한다(fearless concurrency).

## 연습 / 확인 문제 (Exercises)

- 동시성과 병렬성의 차이를 단일 코어 예로 설명하라.
- Coffman 4조건 중 하나를 깨서 deadlock을 막는 방법(락 순서)을 보여라.
- actor 모델이 공유 상태 문제를 줄이는 이유를 mailbox로 설명하라.
- async/await가 I/O-bound 서버에 유리하고 CPU-bound엔 무이득인 이유를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [메모리 관리 모델](Memory-Models.md)
- 다음: [동기화](../../Systems/Operating-Systems/Synchronization.md)
- 관련: [멀티스레딩](../../Systems/Parallel-Computing/Multithreading.md)

## 참조 (References)

- [Systems/Operating-Systems/Synchronization.md](../../Systems/Operating-Systems/Synchronization.md)
- [Systems/Parallel-Computing/Multithreading.md](../../Systems/Parallel-Computing/Multithreading.md)
- [Memory-Models.md](Memory-Models.md)
- [Reference/Books.md](../../Reference/Books.md)
