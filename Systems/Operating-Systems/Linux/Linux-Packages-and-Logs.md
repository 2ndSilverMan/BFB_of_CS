# Linux 패키지와 로그 (Packages and Logs)

- Level: Beginner
- Prerequisites: [Systems/Operating-Systems/Linux/Linux-Processes-and-Services.md](Linux-Processes-and-Services.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

패키지 관리자는 소프트웨어 설치·업데이트·제거를 **의존성·버전·서명**과 함께 관리하고, 로그는 시스템·서비스가 남긴 사건 기록이다. Linux 진단은 "**무엇이 설치됐고, 무엇이 기록됐는가**"에서 시작한다.

## 직관 (Intuition)

패키지 관리자는 앱스토어 + 업데이트 관리자, 로그는 서버의 블랙박스다. 장애가 나면 감으로 고치지 말고 **로그 + 설치 이력 + 직전 변경**을 따라간다.

## 이론 (Theory)

### 1. 패키지 관리자와 의존성 해소

| 배포판 | 관리자 | 패키지 |
|---|---|---|
| Debian/Ubuntu | `apt`/`dpkg` | `.deb` |
| RHEL/Fedora | `dnf`/`rpm` | `.rpm` |
| Arch | `pacman` | `.pkg.tar` |

설치 시 **의존성 그래프**를 풀어(필요한 라이브러리도 함께 설치) **서명**으로 무결성을 검증한다. 의존성 충돌(같은 라이브러리의 다른 버전 요구)이 설치 실패의 단골.

### 2. 로그: /var/log vs journald

전통적으론 `/var/log/*` 텍스트 파일. systemd 환경은 **journald**가 **구조화된 로그**(서비스·우선순위·타임스탬프 메타데이터 포함)를 `journalctl` 로 질의하게 한다 — 시간·서비스·우선순위로 **필터링**이 핵심.

## 구현 (Implementation)

```bash
apt show nginx                  # 패키지 정보(버전·의존성)
sudo apt install -y nginx       # 의존성까지 설치

journalctl -u nginx -p err --since "1 hour ago"   # nginx의 error만, 최근 1시간
journalctl -f                   # 실시간 추적(tail -f)
tail -n 100 /var/log/syslog     # 전통 로그
```

**워크드 예제(장애 진단).** 서비스가 죽었다 → ① `systemctl status svc`(상태·exit code) → ② `journalctl -u svc -p err --since "10 min ago"`(에러만 좁혀) → ③ 직전 `apt`/설정 변경 확인 → ④ 환경·권한·포트 점검. **시간 범위 + 서비스 + 우선순위**로 좁히는 게 핵심.

## 복잡도 (Complexity)

| 항목 | 특성 |
|---|---|
| 의존성 해소 | 충돌 시 설치/업데이트 실패 |
| 로그 양 | 시간·서비스·request ID 필터 없으면 추적 난망 |

## 응용 (Applications)

- 도구 설치·버전 확인, 서비스 실패 원인 추적.
- 보안 업데이트 관리, 배포 후 회귀 진단.

## 흔한 오해 (Common Misunderstandings)

- **최신 설치가 항상 안전하지 않다** — 호환성·롤백 고려.
- **로그에 에러가 없다고 정상이 아니다** — 로그 레벨이 낮을 수 있다(`-p` 확인).
- **같은 명령도 배포판마다 패키지명·경로가 다르다**.
- **운영 서버에서 즉흥 패키지 변경은** 재현성·감사를 해친다 → IaC.

## TMI

- `journalctl -p` 우선순위: 0(emerg)~7(debug) — `-p warning` 은 warning 이상만.
- 패키지 lock 파일(`/var/lib/dpkg/lock`)이 남으면 다른 설치와 충돌("could not get lock").
- Infrastructure as Code(Ansible/Terraform)로 패키지 상태를 코드로 재현해 "스노우플레이크 서버"를 막는다.

## 연습 / 확인 문제 (Exercises)

- 사용하는 배포판의 패키지 관리자와 패키지 형식을 확인하라.
- 특정 서비스의 최근 1시간 error 로그만 필터링하는 `journalctl` 명령을 작성하라.
- 장애 진단 시 좁혀 갈 순서(상태→로그→변경→환경)를 적어라.
- 의존성 충돌이 왜 생기는지 라이브러리 버전으로 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [프로세스와 서비스](Linux-Processes-and-Services.md)
- 다음: [로깅 시스템](../../../Engineering/DevOps/Logging-Systems.md)
- 관련: [메트릭 & 알람](../../../Engineering/DevOps/Metrics-Alerts.md)

## 참조 (References)

- [Engineering/Debugging/Structured-Logging.md](../../../Engineering/Debugging/Structured-Logging.md)
- [Engineering/DevOps/Metrics-Alerts.md](../../../Engineering/DevOps/Metrics-Alerts.md)
- [Reference/Books.md](../../../Reference/Books.md)
