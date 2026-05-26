# 디버깅 (Debugging)

> 버그를 재현하고, 원인을 추적하고, 수정을 검증하는 체계적 접근법.

**선수지식**: [Programming/](../../Programming/)

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

### 디버깅 전략

| 주제 | 파일 | Status |
|---|---|---|
| 과학적 디버깅 — 가설 수립 → 실험 → 검증 사이클 | Scientific-Debugging.md | Planned |
| 버그 재현 — 최소 재현 케이스(MRE) 만들기 | Minimal-Reproducible-Example.md | Planned |
| 이분 탐색 디버깅 — git bisect, 주석 제거 | Bisect-Debugging.md | Planned |
| 러버 덕 디버깅과 코드 리뷰 활용 | Rubber-Duck-Debugging.md | Planned |

### 디버거 사용법

| 주제 | 파일 | Status |
|---|---|---|
| 중단점, 스텝 실행, 변수 감시 | Breakpoints-and-Stepping.md | Planned |
| 스택 트레이스 읽기 | Stack-Traces.md | Planned |
| 조건부 중단점과 로깅 포인트 | Conditional-Breakpoints.md | Planned |
| 원격 디버깅 | Remote-Debugging.md | Planned |
| 코어 덤프 분석 | Core-Dump-Analysis.md | Planned |

### 로깅과 관찰 가능성

| 주제 | 파일 | Status |
|---|---|---|
| 로깅 수준 설계 — DEBUG/INFO/WARN/ERROR | Logging-Levels.md | Planned |
| 구조화 로깅 (Structured Logging) — JSON 포맷 | Structured-Logging.md | Planned |
| 분산 시스템 로그 상관 — Trace ID, Span | Distributed-Log-Correlation.md | Planned |

### 메모리 & 동시성 버그

| 주제 | 파일 | Status |
|---|---|---|
| 메모리 오류 — 버퍼 오버플로우, Use-After-Free | Memory-Errors.md | Planned |
| Valgrind / AddressSanitizer | Valgrind-AddressSanitizer.md | Planned |
| 레이스 컨디션 디버깅 | Race-Condition-Debugging.md | Planned |
| 데드락 탐지 | Deadlock-Detection.md | Planned |

### 프로덕션 디버깅

| 주제 | 파일 | Status |
|---|---|---|
| 카나리 배포와 기능 플래그 활용 | Canary-Feature-Flags.md | Planned |
| 에러 트래킹 — Sentry, Rollbar | Error-Tracking.md | Planned |
| 사후 분석 (Postmortem) 작성법 | Postmortem.md | Planned |

---

## 학습 순서

```text
과학적 디버깅 전략
        ↓
디버거 기초 사용법
        ↓
로깅 설계
        ↓
메모리 & 동시성 버그
        ↓
프로덕션 디버깅
```

---

## 연관 섹션

- [Engineering/Testing/](../Testing/) — 테스트로 버그를 사전에 포착
- [Engineering/Performance/](../Performance/) — 성능 문제 디버깅
- [Engineering/DevOps/](../DevOps/) — 프로덕션 모니터링과 경보
- [Systems/Operating-Systems/](../../Systems/Operating-Systems/) — 프로세스/메모리 모델 이해
