# 마이크로컨트롤러와 인터페이스 (Microcontrollers and Interfaces)

- Level: Intermediate
- Prerequisites: [회로 기초](Circuits-and-Electronics.md), [C 언어](../Programming/Languages/C/)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (핵심 원리와 제한된 검증 모형)

---

## 개념 (Concept)

MCU는 CPU·메모리와 GPIO·타이머·통신 장치 같은 주변장치를 결합한 제어용 컴퓨터다. 주변장치를 다룬다는 것은 레지스터에 숫자를 쓰는 일뿐 아니라 시간·전기적 조건·상태 전이를 맞추는 일이다. 여기서는 인터럽트와 이벤트 처리, 통신 방식의 선택, 타이머 wraparound를 다룬다. 특정 보드의 배선·레지스터 주소는 범위 밖이다.

## 직관 (Intuition)

센서가 값을 만든 시각과 프로그램이 읽은 시각은 다르다. 폴링은 주기적으로 확인하고, 인터럽트는 발생 사실을 알리고, DMA는 전송 자체를 주변장치가 수행하도록 돕는다. 인터럽트가 있다는 이유만으로 이벤트가 유실되지 않거나 지연이 항상 작다고 보장되지는 않는다.

## 이론 (Theory)

메모리 매핑 I/O의 주소는 일반 RAM과 다른 부작용을 가질 수 있다. 읽으면 상태가 지워지거나, 1을 써서 비트를 지우는 레지스터도 있다. 읽기-수정-쓰기 중 다른 실행 주체가 변경하면 업데이트를 잃을 수 있다. C의 volatile은 지정한 접근의 최적화와 관련된 도구이지 상호 배제·원자성·메모리 순서 전체를 보장하는 동기화 장치가 아니다.

| 방식 | 전달 구조 | 설계할 경계 |
|---|---|---|
| GPIO | 개별 디지털 입력·출력 | 전압, 풀업, 바운스, 드라이브 능력 |
| UART | 송수신 양쪽의 시간 기준으로 비트 복원 | baud 오차, 프레임, 수신 버퍼 |
| SPI | 클록과 데이터, 보통 칩 선택선 | 클록 위상·극성, 전송 길이, 선택 타이밍 |
| I2C | 주소를 사용하는 공유 버스 | 풀업, 상승 시간, 주소 충돌, timeout |

[Raspberry Pi Pico SDK의 Hardware APIs](https://www.raspberrypi.com/documentation/pico-sdk/hardware.html)는 GPIO·IRQ·타이머·UART·SPI·I2C를 구별한 실제 API 예다. 이 문서의 설명을 모든 MCU의 레지스터 동작으로 일반화하지 않는다.

인터럽트 처리기에서는 상태를 확인·정리하고 짧은 이벤트를 전달한다. 오래 걸리거나 블로킹하는 처리는 메인 루프/태스크로 넘긴다. 큐 용량은 최대 burst와 소비 지연에 근거해 정하며 넘쳤을 때 버리기·재시도·장애 보고 정책이 필요하다.

## 구현 (Implementation)

32비트 밀리초 카운터는 $2^{32}$에서 순환한다. unsigned 차이 $(now-start)\bmod2^{32}$는 실제 경과가 한 바퀴 미만일 때 경과시간을 복원한다. 이 조건을 놓치면 오랫동안 꺼져 있던 장치의 시간 차이를 잘못 해석한다. 아래 정책은 timeout을 반 바퀴 미만으로 제한하고 그 시간 안에 충분히 자주 확인한다고 가정한다.

```python
MASK = (1 << 32) - 1

def expired(start, now, timeout):
    if not 0 <= start <= MASK or not 0 <= now <= MASK:
        raise ValueError("32-bit counter required")
    if not 0 <= timeout < (1 << 31):
        raise ValueError("timeout outside policy")
    return ((now - start) & MASK) >= timeout

start = 0xFFFFFFF0
assert not expired(start, 0x0000000F, 32)  # 31ms
assert expired(start, 0x00000010, 32)      # 32ms
assert expired(100, 100, 0)
```

이벤트 큐의 독립적인 동작 모델이다. 실제 ISR과 메인 루프 사이의 원자성은 모델링하지 않는다.

```python
from collections import deque
events = deque()
capacity, dropped = 2, 0
for event in ["edge-1", "edge-2", "edge-3"]:
    if len(events) == capacity:
        dropped += 1
    else:
        events.append(event)
assert dropped == 1
assert list(events) == ["edge-1", "edge-2"]
```

## 복잡도 (Complexity)

큐 삽입·제거는 이 모델에서 상수 시간이고 저장 공간은 용량에 비례한다. 실제 지연은 인터럽트 마스킹 시간, 높은 우선순위 ISR, 처리 시간, 버스 전송 시간의 영향을 받는다. 예를 들어 1ms마다 이벤트가 오는데 소비가 10ms 중단되고 빈 큐에서 시작한다면 경계 도착 순서까지 고려해 최소 10개보다 넉넉한 용량 또는 명시적인 손실 정책이 필요하다.

## 응용 (Applications)

버튼 입력, 센서 샘플링, 통신 패킷 수신, watchdog 상태 보고에 적용한다. 접점 바운스와 재전송은 모두 “여러 알림이 하나의 물리 사건인가”라는 의미 해석도 필요하다.

## 흔한 오해 (Common Misunderstandings)

- ISR에서 처리하면 항상 실시간이다: 우선순위와 최악 지연을 계산해야 한다.
- 큐를 크게 하면 유실이 사라진다: 평균 생산량이 소비량을 넘으면 결국 가득 찬다.
- I2C/SPI/UART가 같으면 직접 연결해도 된다: 핀 전압과 전기적 구성을 먼저 확인한다.

## TMI

- 디버거가 멈춘 동안 주변장치 타이머가 계속 도는지는 MCU 설정에 따라 다르다.
- 통신 timeout과 전체 요청의 deadline은 다르다. 재시도를 여러 번 하면 전체 deadline을 넘을 수 있다.

## 연습 / 확인 문제 (Exercises)

1. start=0xfffffff0, now=0이면 경과시간은? **답:** 16ms.
2. 한 번의 카운터 순환보다 긴 시간이 지났는데 같은 값이 돌아오면 위 함수가 감지하는가? **답:** 못한다. 상위 시간 정보나 오버플로 누적이 필요하다.
3. 이벤트 100개/s, 처리 가능량 80개/s에서 큐만 늘리는 해결책의 한계는? **답:** 초당 평균 20개가 누적된다. 유입 제한·처리 개선·합치기·손실 정책이 필요하다.

## 이어서 읽기 (Reading Path)

- 다음: [실시간 설계](Embedded-Real-Time-Design.md).
- 관련: [동기화](../Systems/Operating-Systems/Synchronization.md), [I/O 시스템](../Systems/Computer-Architecture/IO-Systems.md).

## 참조 (References)

- [Raspberry Pi Pico SDK, Hardware APIs](https://www.raspberrypi.com/documentation/pico-sdk/hardware.html) — 주변장치·인터럽트·타이머 API의 구체적 예. 보드에 적용할 때 SDK 버전과 칩 데이터시트를 별도 고정한다.

## 재작성 메모 (Rewrite Notes)

- 재사용할 재료: 순환 타이머의 가정·경계 입력, 유한 큐 손실 정책, 인터럽트/태스크 분리.
- 보충할 내용: 실제 MCU의 ISR 큐 구현과 원자성, DMA 소유권, UART 오류·I2C timeout의 보드 실험.
- 확인 상태: 2026-09-18 Pico SDK Hardware API 범위 확인. 본문 코드는 Python 모형이며 MCU 컴파일·배선·실행은 하지 않았다. Python 3.12/Windows에서 본문의 Python 2개 블록과 assert를 독립 실행해 통과했다. 재실행 검사는 test_new_domain_examples.py에서 관리한다.
