# Linux 학습 트랙 (Linux)

> 리눅스 명령줄, 파일 시스템, 권한, 프로세스, 서비스 운영의 기초를 익히는 실습 트랙.

**선수지식**: [Systems/Operating-Systems/](../), [Programming/](../../../Programming/)

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

| Order | 주제 | 파일 | 설명 | Status |
|---|---|---|---|---|
| 1 | 셸과 기본 명령 | [Linux-Shell-Basics.md](Linux-Shell-Basics.md) | 터미널, 경로, `ls`, `cd`, `cp`, `mv`, `rm` | Draft |
| 2 | 파일 시스템 | [Linux-File-System.md](Linux-File-System.md) | 디렉토리 구조, 절대/상대 경로, 마운트 개념 | Draft |
| 3 | 사용자와 권한 | [Linux-Users-Permissions.md](Linux-Users-Permissions.md) | 사용자, 그룹, `chmod`, `chown`, sudo | Draft |
| 4 | 프로세스와 서비스 | [Linux-Processes-and-Services.md](Linux-Processes-and-Services.md) | `ps`, `top`, signal, systemd 서비스 | Draft |
| 5 | 패키지와 로그 | [Linux-Packages-and-Logs.md](Linux-Packages-and-Logs.md) | 패키지 관리자, 로그 위치, 기본 진단 흐름 | Draft |

---

## 학습 순서

```text
Linux-Shell-Basics -> Linux-File-System -> Linux-Users-Permissions
        ↓
Linux-Processes-and-Services -> Linux-Packages-and-Logs
```

---

## TMI

- Linux는 엄밀히 말하면 운영체제 전체가 아니라 커널 이름이다. 일상에서는 GNU 도구, 패키지 관리자, 데스크톱/서버 구성까지 묶어 Linux라고 부르는 경우가 많다.
- `rm -rf`는 매우 강력한 삭제 명령이다. 실습 문서에서는 장난처럼 쓰지 말고, 경로를 눈으로 확인하는 습관을 먼저 들인다.
- 리눅스에서 "모든 것은 파일"이라는 말은 과장된 표현이지만, 장치, 파이프, 소켓도 파일처럼 다루는 인터페이스가 많다는 점은 실제로 중요하다.
- 서버에서 문제를 볼 때 `journalctl`, `/var/log`, `systemctl status`만 익숙해져도 처음 보는 장애를 추적하는 속도가 크게 달라진다.

---

## 연관 섹션

- [Systems/Operating-Systems/](../) - 프로세스, 파일 시스템, 메모리 관리의 이론적 배경
- [Engineering/DevOps/](../../../Engineering/DevOps/) - 서버 운영, 배포, 컨테이너 실습
- [Engineering/Debugging/](../../../Engineering/Debugging/) - 로그와 프로세스 기반 문제 진단
