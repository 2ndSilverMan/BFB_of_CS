# Linux 패키지와 로그 (Packages and Logs)

- Level: Beginner
- Prerequisites: [Systems/Operating-Systems/Linux/Linux-Processes-and-Services.md](Linux-Processes-and-Services.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

패키지 관리자는 소프트웨어 설치, 업데이트, 제거를 관리하고, 로그는 시스템과 서비스가 남긴 사건 기록이다. Linux 운영의 기본 진단은 "무엇이 설치되어 있고, 무엇이 기록되었는가"를 확인하는 데서 시작한다.

## 직관 (Intuition)

패키지 관리자는 앱스토어와 업데이트 관리자에 가깝고, 로그는 서버의 블랙박스다. 장애가 나면 감으로 고치기보다 로그와 설치 이력을 따라가야 한다.

## 이론 (Theory)

배포판마다 패키지 형식과 관리자가 다르다. Debian/Ubuntu 계열은 `apt`, RHEL/Fedora 계열은 `dnf`/`yum`, Arch 계열은 `pacman`을 쓴다. 패키지는 의존성, 버전, repository, signature를 통해 관리된다.

로그는 전통적으로 `/var/log` 아래 파일에 남고, systemd 환경에서는 journald가 `journalctl`로 조회되는 구조화된 로그를 제공한다. 좋은 진단은 시간 범위, 서비스 이름, 에러 메시지, 직전 변경을 함께 본다.

## 구현 (Implementation)

```bash
apt search package-name
apt show package-name
journalctl -xe
journalctl -u my-service --since "1 hour ago"
tail -n 100 /var/log/syslog
```

패키지 설치·삭제는 시스템 상태를 바꾸므로 실습 환경과 운영 환경을 구분한다.

## 복잡도 (Complexity)

패키지 의존성이 꼬이면 설치·업데이트가 실패할 수 있다. 로그는 양이 많아 시간 필터, 서비스 필터, trace/request ID가 없으면 원인 추적이 어렵다.

## 응용 (Applications)

- 필요한 도구 설치와 버전 확인
- 서비스 실패 원인 추적
- 보안 업데이트 관리
- 배포 후 회귀 진단

## 흔한 오해 (Common Misunderstandings)

- 최신 버전 설치가 항상 안전한 것은 아니다. 호환성과 롤백을 고려해야 한다.
- 로그에 에러가 없다고 문제가 없는 것은 아니다. 로그 수준 설정이 낮을 수 있다.
- 같은 명령도 배포판에 따라 패키지 이름과 경로가 다를 수 있다.
- 운영 서버에서 즉흥적으로 패키지를 바꾸면 재현성과 감사가 어려워진다.

## TMI

- `journalctl -f`는 로그를 실시간으로 따라간다.
- 패키지 lock 파일이 남으면 다른 설치 작업과 충돌할 수 있다.
- Infrastructure as Code를 쓰면 패키지 상태도 코드로 재현할 수 있다.

## 연습 / 확인 문제 (Exercises)

- 사용하는 배포판의 패키지 관리자를 확인하라.
- 특정 서비스의 최근 1시간 로그를 필터링하는 명령을 작성하라.
- 장애 진단 시 로그에서 확인할 정보 5가지를 정리하라.

## 이어서 읽기 (Reading Path)

- 이전: [프로세스와 서비스](Linux-Processes-and-Services.md)
- 다음: [Engineering/DevOps](../../../Engineering/DevOps/), [Debugging](../../../Engineering/Debugging/)

## 참조 (References)

- [Engineering/Debugging/Structured-Logging.md](../../../Engineering/Debugging/Structured-Logging.md)
- [Engineering/DevOps/Metrics-Alerts.md](../../../Engineering/DevOps/Metrics-Alerts.md)
- [Reference/Books.md](../../../Reference/Books.md)
