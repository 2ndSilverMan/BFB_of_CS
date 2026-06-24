# Linux 프로세스와 서비스 (Processes and Services)

- Level: Beginner
- Prerequisites: [Systems/Operating-Systems/Processes-and-Threads.md](../Processes-and-Threads.md), [Systems/Operating-Systems/Linux/Linux-Users-Permissions.md](Linux-Users-Permissions.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

Linux에서 프로세스는 실행 중인 프로그램이고, 서비스는 백그라운드에서 지속적으로 실행되도록 관리되는 프로세스 집합이다. 현대 배포판에서는 systemd가 서비스 시작, 중지, 상태 확인, 로그 연결을 관리하는 경우가 많다.

## 직관 (Intuition)

명령을 직접 실행하면 터미널을 닫을 때 같이 끝날 수 있다. 서비스로 등록하면 운영체제가 부팅 시 시작하고, 상태를 추적하고, 실패 시 재시작 정책을 적용할 수 있다.

## 이론 (Theory)

프로세스는 PID를 갖고 부모-자식 관계를 이룬다. Signal은 프로세스에 보내는 제어 메시지다. 예를 들어 `SIGTERM`은 정상 종료 요청, `SIGKILL`은 강제 종료다.

systemd unit은 서비스의 실행 명령, 의존성, 환경, 재시작 정책을 정의한다. 상태 확인은 process state와 exit code, journal log를 함께 봐야 한다.

## 구현 (Implementation)

```bash
ps aux
top
kill -TERM 1234
systemctl status nginx
journalctl -u nginx
```

운영 서버에서 프로세스를 종료할 때는 대상 PID와 서비스 영향을 먼저 확인한다.

## 복잡도 (Complexity)

프로세스가 많아지면 CPU, 메모리, 파일 디스크립터, 네트워크 포트 경합이 생긴다. 서비스 장애는 실행 파일보다 환경 변수, 권한, working directory, 의존 서비스 때문에 생기기도 한다.

## 응용 (Applications)

- 서버 프로세스 상태 확인
- 서비스 재시작과 장애 진단
- CPU·메모리 과다 사용 프로세스 찾기
- signal 기반 graceful shutdown

## 흔한 오해 (Common Misunderstandings)

- `kill`은 항상 죽인다는 뜻이 아니라 signal을 보낸다는 뜻이다.
- `SIGKILL`은 강력하지만 정리 작업을 할 기회를 주지 않는다.
- 프로세스가 떠 있다고 서비스가 정상이라는 뜻은 아니다.
- `systemctl restart` 전에 로그와 설정 변경 내용을 확인해야 한다.

## TMI

- Zombie process는 종료됐지만 부모가 exit status를 회수하지 않은 상태다.
- Daemon은 터미널과 분리되어 백그라운드에서 동작하는 프로세스다.
- `nice`와 `renice`는 CPU 스케줄링 우선순위에 영향을 준다.

## 연습 / 확인 문제 (Exercises)

- `ps`, `top`, `systemctl status`가 각각 무엇을 보여 주는지 비교하라.
- `SIGTERM`과 `SIGKILL`의 차이를 설명하라.
- 서비스가 시작되지 않을 때 확인할 항목 5가지를 적어라.

## 이어서 읽기 (Reading Path)

- 이전: [프로세스와 스레드](../Processes-and-Threads.md)
- 다음: [패키지와 로그](Linux-Packages-and-Logs.md)

## 참조 (References)

- [Systems/Operating-Systems/Processes-and-Threads.md](../Processes-and-Threads.md)
- [Engineering/Debugging/Structured-Logging.md](../../../Engineering/Debugging/Structured-Logging.md)
- [Reference/Books.md](../../../Reference/Books.md)
