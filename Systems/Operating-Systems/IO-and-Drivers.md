# 입출력과 디바이스 드라이버 (I/O and Device Drivers)

- Level: Intermediate
- Prerequisites: [Systems/Operating-Systems/Processes-and-Threads.md](Processes-and-Threads.md), [Systems/Operating-Systems/File-Systems.md](File-Systems.md), [Systems/Computer-Architecture/IO-Systems.md](../Computer-Architecture/IO-Systems.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

I/O는 프로그램이 디스크·네트워크·키보드·GPU 같은 외부 장치와 데이터를 주고받는 과정이다. **디바이스 드라이버**는 커널과 하드웨어 사이에서 장치별 제어를 **표준 인터페이스(read/write)** 로 감싼다 — "느린 외부 세계"를 추상화하는 계층.

## 직관 (Intuition)

앱은 "파일을 읽어줘"라고 말하지만, 실제 장치는 레지스터 설정·버퍼 주소·인터럽트·DMA 같은 저수준 절차를 요구한다. OS와 드라이버가 이 복잡함을 숨긴다. 핵심 통찰: **I/O는 CPU보다 수천~수백만 배 느려**, "어떻게 기다리고 어떻게 겹치느냐"가 성능의 전부다.

## 이론 (Theory)

### 1. I/O 경로

```mermaid
flowchart LR
    A[application] -->|read syscall| K[kernel I/O layer]
    K --> C[page cache]
    C -->|miss| D[device driver]
    D --> CT[controller] --> DEV[device]
```

### 2. 장치 유형과 대기 방식

| 축 | 종류 |
|---|---|
| 장치 | block(디스크, 블록 단위) / character(키보드·serial, byte stream) |
| 대기 | polling(CPU가 상태 반복 확인) / interrupt(완료 시 알림) / **DMA**(controller가 메모리↔장치 직접 전송, CPU 우회) |

### 3. blocking vs non-blocking vs async

blocking(완료까지 스레드 정지), non-blocking(즉시 반환 + 재시도), **async**(완료를 콜백/이벤트로) — async는 *빨라지는 게 아니라* 대기를 겹쳐 throughput을 올린다([비동기 I/O](../../Engineering/Performance/Async-IO.md)).

## 구현 (Implementation)

```python
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("hello\n")            # write(2) → page cache(보통 즉시 디스크 아님)
with open("example.txt", "r", encoding="utf-8") as f:
    data = f.read()              # cache hit면 디스크 미접근
```

이 한 줄 뒤에 파일시스템·page cache·block layer·드라이버·controller가 관여한다. `f.flush()` + `os.fsync()` 라야 실제 디스크 영속.

## 복잡도 (Complexity)

| 접근 | 대략 latency |
|---|---|
| page cache hit(RAM) | ~100 ns |
| SSD random read | ~100 μs |
| HDD random read(탐색) | ~10 ms |
| 네트워크 왕복 | ~0.5 ms (LAN) ~ 100 ms (대륙간) |

**워크드 예제.** 같은 `read()` 가 cache hit면 ~100ns, miss면 SSD ~100μs로 **1000배** 차이. 그래서 OS는 buffering·caching·read-ahead로 느린 장치와 빠른 CPU의 간극을 메운다.

## 응용 (Applications)

- 파일/저장장치 성능 이해, 소켓 I/O·이벤트 루프.
- 서버 성능 튜닝·병목 분석, 커널 드라이버·하드웨어 추상화.

## 흔한 오해 (Common Misunderstandings)

- **read/write가 항상 즉시 장치 접근은 아니다** — cache에서 처리될 수 있다.
- **interrupt가 항상 polling보다 낫지 않다** — 초고빈도(고속 NIC)에선 polling(NAPI·DPDK)이 유리.
- **비동기 I/O는 작업을 빠르게 하지 않는다** — 대기 방식을 바꿀 뿐.
- **드라이버 버그는 앱 버그보다 시스템 전체 안정성**에 큰 영향(커널 권한).

## TMI

- **zero-copy**(`sendfile`)는 kernel↔user 복사를 없애 파일 전송 성능을 크게 올린다.
- memory-mapped I/O는 장치 레지스터를 메모리 주소처럼 접근하게 한다(`mmap`).
- `io_uring`(Linux)은 syscall 오버헤드를 줄인 현대 비동기 I/O 인터페이스로 고성능 서버에 채택된다.

## 연습 / 확인 문제 (Exercises)

- polling과 interrupt의 장단점을 빈도 관점에서 비교하라.
- DMA가 CPU 부하를 줄이는 이유를 데이터 경로로 설명하라.
- 같은 `read()` 가 cache hit/miss에서 latency가 어떻게 다른지 위 표로 설명하라.
- blocking vs async I/O가 throughput에 주는 차이를 동시 요청 100개로 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [파일 시스템](File-Systems.md)
- 다음: [소켓 프로그래밍](../Networks/Socket-Programming.md)
- 관련: [비동기 I/O](../../Engineering/Performance/Async-IO.md)

## 참조 (References)

- [Systems/Operating-Systems/File-Systems.md](File-Systems.md)
- [Systems/Computer-Architecture/IO-Systems.md](../Computer-Architecture/IO-Systems.md)
- [Engineering/Performance/IO-Profiling.md](../../Engineering/Performance/IO-Profiling.md)
- [Reference/Books.md](../../Reference/Books.md)
