# 입출력 (I/O) 시스템 (I/O Systems)

- Level: Intermediate
- Prerequisites: [Systems/Computer-Architecture/CPU-and-ISA.md](CPU-and-ISA.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

I/O 시스템은 CPU·메모리와 외부 장치(디스크, 네트워크, 키보드 등) 사이의 데이터 이동을 다룬다. 폴링, 인터럽트, DMA가 핵심 메커니즘이며, 장치 속도 차이를 다루는 것이 관건이다.

## 직관 (Intuition)

CPU는 매우 빠르고 장치는 느리다. CPU가 느린 장치를 계속 기다리며 확인(폴링)하면 시간 낭비다. 그래서 "끝나면 알려 줘"(인터럽트)라고 맡기거나, 아예 "데이터를 메모리로 직접 옮겨 줘"(DMA)라고 위임해 CPU는 다른 일을 한다.

## 이론 (Theory)

**통신 방식**:
- **폴링(programmed I/O)**: CPU가 장치 상태를 반복 확인. 단순하나 CPU 낭비.
- **인터럽트**: 장치가 완료 시 CPU에 신호 → CPU가 핸들러 실행. 비동기.
- **DMA**: DMA 컨트롤러가 CPU 개입 없이 장치↔메모리 전송, 완료 시 인터럽트.

**주소 지정**: 메모리 맵 I/O(주소 공간 공유) vs 포트 I/O(별도 명령). 장치는 드라이버를 통해 OS가 추상화한다. 인터럽트는 우선순위·벡터로 관리된다.

## 구현 (Implementation)

```text
폴링:    while not device.ready: pass     # CPU 바쁜 대기(낭비)
         data = device.read()

인터럽트: device.start_read()
         # CPU는 다른 작업 수행 ...
         # 완료 시 -> ISR(인터럽트 서비스 루틴) 실행

DMA:     dma.setup(src=device, dst=mem_buf, len=N)
         dma.start()
         # CPU 개입 없이 전송, 끝나면 인터럽트 1회
```

## 복잡도 (Complexity)

성능 지표는 지연(latency)과 대역폭(bandwidth)이다. 폴링은 CPU 시간을 장치 대기에 낭비하고, 인터럽트는 컨텍스트 전환 오버헤드가 있으며, DMA는 대량 전송에서 CPU를 해방시킨다. 인터럽트가 너무 잦으면(고속 네트워크) 오히려 부하라 폴링·배칭(NAPI)으로 전환하기도 한다.

## 응용 (Applications)

- 디스크·SSD·네트워크 카드 데이터 전송
- 키보드·마우스·센서 입력
- GPU·고속 장치의 DMA
- 실시간 시스템의 인터럽트 처리

## 흔한 오해 (Common Misunderstandings)

- 인터럽트가 항상 폴링보다 낫지 않다 — 초고속 장치에선 인터럽트 폭주가 문제다.
- DMA 중에도 CPU와 DMA가 메모리 버스를 다툴 수 있다(사이클 스틸링).
- 메모리 맵 I/O 주소는 캐싱하면 안 된다(부작용·일관성 문제).
- 드라이버 버그는 커널 권한이라 시스템 전체를 위협한다.

## TMI

- 고속 네트워크의 인터럽트 폭주를 막는 리눅스 NAPI는 인터럽트와 폴링을 적응적으로 전환한다.
- DMA는 악용되면 보안 위협이 되어(메모리 직접 접근), IOMMU로 보호한다.
- 옛 PC의 "IRQ 충돌"은 인터럽트 라인 공유 문제로 악명 높았다.

## 연습 / 확인 문제 (Exercises)

- 폴링, 인터럽트, DMA의 CPU 사용을 한 표로 비교하라.
- 대량 디스크 전송에 DMA가 유리한 이유를 설명하라.
- 인터럽트 폭주가 성능을 해치는 상황과 완화책을 논하라.

## 이어서 읽기 (Reading Path)

- 이전: [가상 메모리](Virtual-Memory-Hardware.md)
- 다음: [병렬 아키텍처](Parallel-Architecture.md), [Systems/Operating-Systems/IO-and-Drivers.md](../Operating-Systems/IO-and-Drivers.md)

## 참조 (References)

- [Systems/Operating-Systems/IO-and-Drivers.md](../Operating-Systems/IO-and-Drivers.md)
- [Reference/Books.md](../../Reference/Books.md)
