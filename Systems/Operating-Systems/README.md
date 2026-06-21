# 운영체제 (Operating Systems)

> 하드웨어와 애플리케이션 사이의 관리자.

**선수지식**: [Systems/Computer-Architecture/](../Computer-Architecture/)

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

| 주제 | 파일 | Status |
|---|---|---|
| 프로세스와 스레드 | [Processes-and-Threads.md](Processes-and-Threads.md) | Draft |
| CPU 스케줄링 | Scheduling.md | Planned |
| 동기화 (뮤텍스, 세마포어) | Synchronization.md | Planned |
| 교착 상태 (Deadlock) | Deadlock.md | Planned |
| 메모리 관리 (페이징, 세그멘테이션) | [Memory-Management.md](Memory-Management.md) | Draft |
| 가상 메모리와 페이지 교체 | Virtual-Memory.md | Planned |
| 파일 시스템 | File-Systems.md | Planned |
| 입출력과 디바이스 드라이버 | IO-and-Drivers.md | Planned |

### 실습 트랙

| 주제 | 위치 | 설명 | Status |
|---|---|---|---|
| Linux 학습 트랙 | [Linux/](Linux/) | 셸, 파일 시스템, 권한, 프로세스, 서비스 운영 기초 | Planned |

---

## 학습 순서

```text
Processes-and-Threads → Scheduling
        ↓
Synchronization → Deadlock
        ↓
Memory-Management → Virtual-Memory
        ↓
File-Systems → IO-and-Drivers
        ↓
Linux 실습 트랙
```

---

## 연관 섹션

- [Systems/Computer-Architecture/](../Computer-Architecture/) — CPU, 메모리, I/O 하드웨어 기반
- [Systems/Parallel-Computing/](../Parallel-Computing/) — 스레드, 동기화, 병렬 실행 모델
- [Systems/Networks/](../Networks/) — 소켓, 커널 네트워크 스택
- [Engineering/Debugging/](../../Engineering/Debugging/) — 프로세스, 메모리, 동시성 버그 분석
- [Engineering/DevOps/](../../Engineering/DevOps/) — Linux 서버 운영과 배포 자동화
