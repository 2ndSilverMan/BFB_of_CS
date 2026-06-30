# Linux 프로세스와 서비스 (Processes and Services)

- Level: Beginner
- Prerequisites: [Systems/Operating-Systems/Processes-and-Threads.md](../Processes-and-Threads.md), [Systems/Operating-Systems/Linux/Linux-Users-Permissions.md](Linux-Users-Permissions.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

Linux에서 프로세스는 실행 중인 프로그램(고유 **PID**, 부모-자식 트리), 서비스는 **백그라운드에서 관리되는 프로세스**다. 현대 배포판은 **systemd**가 서비스 시작·중지·상태·로그·재시작 정책을 관리한다.

## 직관 (Intuition)

명령을 직접 실행하면 터미널을 닫을 때 같이 끝날 수 있다. **서비스로 등록**하면 OS가 부팅 시 시작하고, 상태를 추적하고, 실패 시 재시작한다. 프로세스 제어의 핵심 메커니즘은 **시그널**(프로세스에 보내는 비동기 메시지)이다.

## 이론 (Theory)

### 1. PID 트리와 시그널

모든 프로세스는 부모가 있다(최상위 `init`/systemd, PID 1). **시그널**로 제어한다:

| 시그널 | 의미 | 잡기 가능? |
|---|---|---|
| `SIGTERM`(15) | 정상 종료 요청(정리 기회) | ✅ |
| `SIGKILL`(9) | 강제 종료(즉시) | ❌ |
| `SIGHUP`(1) | 터미널 종료/설정 reload | ✅ |
| `SIGCHLD` | 자식 종료 알림 | ✅ |

**graceful shutdown**: `SIGTERM` → 핸들러가 연결 종료·flush → 자발적 exit. 안 끝나면 일정 후 `SIGKILL`. (systemd의 `TimeoutStopSec` 가 이 흐름.)

### 2. zombie와 orphan

자식이 종료됐는데 부모가 **`wait`로 exit status를 회수 안 하면 zombie**(PID만 남음). 부모가 먼저 죽으면 **orphan** → PID 1이 입양해 회수. zombie가 쌓이면 PID 고갈.

### 3. systemd unit

unit 파일이 실행 명령·의존성·환경·재시작 정책(`Restart=on-failure`)·작업 디렉터리를 정의. 상태는 process state + exit code + journal을 **함께** 봐야 한다.

## 구현 (Implementation)

```bash
ps aux                          # 모든 프로세스(소유자·CPU·메모리)
ps -ef --forest                 # 부모-자식 트리
kill -TERM 1234                 # 정상 종료 요청(기본 시그널이 TERM)
kill -9 1234                    # 강제(최후의 수단)
systemctl status nginx          # 서비스 상태 + 최근 로그
journalctl -u nginx --since "10 min ago"
```

**워크드 예제(안전한 종료).** 운영 프로세스를 끌 때 `kill -KILL` 부터 쓰면 안 된다 — 먼저 `kill -TERM`(정리 기회) → 몇 초 기다림 → 안 죽으면 `kill -KILL`. DB·서버는 TERM에서 트랜잭션·연결을 정리한다.

## 복잡도 (Complexity)

| 항목 | 특성 |
|---|---|
| 프로세스 多 | CPU·메모리·fd·포트 경합 |
| 서비스 장애 원인 | 실행 파일보다 **환경 변수·권한·작업 디렉터리·의존 서비스**가 흔함 |

## 응용 (Applications)

- 서버 프로세스 상태 확인, 서비스 재시작·장애 진단.
- CPU/메모리 과다 프로세스 추적, 시그널 기반 graceful shutdown.

## 흔한 오해 (Common Misunderstandings)

- **`kill` 은 "죽이기"가 아니라 "시그널 보내기"** — `kill -HUP` 은 reload.
- **`SIGKILL` 은 정리 기회를 안 준다** — 데이터 손상 위험, 최후 수단.
- **프로세스가 떠 있어도 서비스가 정상은 아니다**(헬스 체크 필요).
- **`systemctl restart` 전에 로그·설정 변경 확인**.

## TMI

- daemon은 터미널과 분리돼(setsid) 백그라운드로 도는 프로세스 — 이름 끝 `d`(sshd, nginx... 실은 master).
- `nice`/`renice` 는 CPU 스케줄링 우선순위(vruntime 가중)를 조정한다.
- `systemctl` 없이 부팅 시작을 보려면 `systemd-analyze blame`(서비스별 부팅 소요).

## 연습 / 확인 문제 (Exercises)

- `ps`, `top`, `systemctl status` 가 각각 보여 주는 것을 비교하라.
- `SIGTERM` 과 `SIGKILL` 의 차이와 안전한 종료 순서를 설명하라.
- zombie와 orphan 프로세스의 차이를 부모 동작으로 설명하라.
- 서비스가 시작 안 될 때 확인할 5가지(환경·권한·의존성·포트·로그)를 적어라.

## 이어서 읽기 (Reading Path)

- 이전: [프로세스와 스레드](../Processes-and-Threads.md)
- 다음: [패키지와 로그](Linux-Packages-and-Logs.md)
- 관련: [구조적 로깅](../../../Engineering/Debugging/Structured-Logging.md)

## 참조 (References)

- [Systems/Operating-Systems/Processes-and-Threads.md](../Processes-and-Threads.md)
- [Engineering/Debugging/Structured-Logging.md](../../../Engineering/Debugging/Structured-Logging.md)
- [Reference/Books.md](../../../Reference/Books.md)
