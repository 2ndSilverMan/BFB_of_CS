# 입출력과 디바이스 드라이버 (I/O and Device Drivers)

- Level: Intermediate
- Prerequisites: [Systems/Operating-Systems/Processes-and-Threads.md](Processes-and-Threads.md), [Systems/Operating-Systems/File-Systems.md](File-Systems.md), [Systems/Computer-Architecture/IO-Systems.md](../Computer-Architecture/IO-Systems.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

입출력(I/O)은 프로그램이 디스크, 네트워크, 키보드, GPU 같은 외부 장치와 데이터를 주고받는 과정이다. 디바이스 드라이버는 운영체제 커널과 하드웨어 사이에서 장치별 제어 방법을 표준 인터페이스로 감싸는 소프트웨어다.

## 직관 (Intuition)

애플리케이션은 “파일을 읽어줘”라고 말하지만, 실제 장치는 레지스터 설정, 버퍼 주소, 인터럽트, DMA 같은 낮은 수준 절차를 요구한다. 운영체제와 드라이버는 이 복잡한 절차를 숨기고, 프로그램에는 read/write 같은 공통 인터페이스를 제공한다.

## 이론 (Theory)

일반적인 I/O 경로는 다음과 같다.

```text
application → system call → kernel I/O layer → device driver → controller → device
```

장치는 크게 block device와 character device로 나눌 수 있다. block device는 디스크처럼 고정 크기 블록 단위 접근에 적합하고, character device는 키보드나 serial port처럼 byte stream에 가깝다.

I/O 완료를 기다리는 방식도 중요하다.

- polling: CPU가 장치 상태를 반복 확인한다.
- interrupt: 장치가 완료 시 CPU에 알린다.
- DMA: CPU가 직접 복사하지 않고 장치와 메모리 사이 전송을 controller가 수행한다.

운영체제는 buffering, caching, scheduling으로 느린 장치와 빠른 CPU 사이의 속도 차이를 완화한다.

## 구현 (Implementation)

사용자 프로그램 관점에서는 파일 descriptor를 통한 I/O가 대표적이다.

```python
with open("example.txt", "w", encoding="utf-8") as f:
    f.write("hello\n")

with open("example.txt", "r", encoding="utf-8") as f:
    data = f.read()

print(data)
```

이 간단한 코드 뒤에는 파일 시스템, page cache, block layer, device driver, storage controller가 관여할 수 있다.

## 복잡도 (Complexity)

I/O 성능은 CPU 시간보다 latency, throughput, queue depth, cache hit rate, device 특성에 크게 좌우된다. 디스크 random I/O와 sequential I/O의 비용은 다르고, 네트워크 I/O는 syscall overhead와 copy 비용도 중요하다.

## 응용 (Applications)

- 파일 시스템과 저장장치 성능 이해
- 네트워크 socket I/O와 event loop 이해
- 서버 성능 튜닝과 병목 분석
- 커널 드라이버와 하드웨어 추상화 학습

## 흔한 오해 (Common Misunderstandings)

- read/write 호출이 항상 즉시 장치 접근을 의미하지는 않는다. cache에서 처리될 수 있다.
- interrupt가 항상 polling보다 좋은 것은 아니다. 매우 높은 빈도에서는 polling이 유리할 수 있다.
- 비동기 I/O는 작업이 빨라진다는 뜻이 아니라 기다리는 방식을 바꾸는 것이다.
- 드라이버 버그는 애플리케이션 버그보다 시스템 전체 안정성에 큰 영향을 줄 수 있다.

## TMI

- zero-copy는 kernel/user space 사이 복사를 줄여 네트워크와 파일 전송 성능을 높인다.
- Linux에서는 block layer, scheduler, page cache가 저장장치 I/O 성능에 큰 영향을 준다.
- memory-mapped I/O는 장치 레지스터를 메모리 주소처럼 접근하게 만든다.

## 연습 / 확인 문제 (Exercises)

- polling과 interrupt의 장단점을 비교하라.
- DMA가 CPU 부하를 줄이는 이유를 설명하라.
- 같은 `read()` 호출이 cache hit와 cache miss에서 어떻게 다르게 동작할지 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [파일 시스템](File-Systems.md)
- 다음: [Systems/Networks/Socket-Programming.md](../Networks/Socket-Programming.md)

## 참조 (References)

- [Systems/Operating-Systems/File-Systems.md](File-Systems.md)
- [Systems/Computer-Architecture/IO-Systems.md](../Computer-Architecture/IO-Systems.md)
- `Engineering/Performance/IO-Profiling.md` (예정)
- [Reference/Books.md](../../Reference/Books.md)
