# 테스트 (Testing)

> 소프트웨어의 정확성을 검증하는 전략, 기법, 도구.

**선수지식**: [Programming/](../../Programming/)

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

### 테스트 기초

| 주제 | 파일 | Status |
|---|---|---|
| 테스트 피라미드 — 단위/통합/E2E의 비율과 원칙 | Testing-Pyramid.md | Planned |
| 테스트 더블 — Mock, Stub, Fake, Spy | Test-Doubles.md | Planned |
| 경계값 분석과 동등 분할 | Boundary-Value-Analysis.md | Planned |

### 단위 테스트

| 주제 | 파일 | Status |
|---|---|---|
| 단위 테스트 작성 원칙 — FIRST, AAA 패턴 | Unit-Test-Principles.md | Planned |
| TDD (Test-Driven Development) — Red-Green-Refactor | TDD.md | Planned |
| BDD (Behavior-Driven Development) | BDD.md | Planned |
| 테스트 가능한 설계 — 의존성 주입, 인터페이스 분리 | Testable-Design.md | Planned |

### 통합 테스트

| 주제 | 파일 | Status |
|---|---|---|
| 통합 테스트 전략 — 서비스 간 경계 검증 | Integration-Test-Strategy.md | Planned |
| 계약 테스트 (Contract Testing) — Pact | Contract-Testing.md | Planned |
| 데이터베이스 테스트 — 트랜잭션 롤백, 픽스처 | Database-Testing.md | Planned |

### E2E & UI 테스트

| 주제 | 파일 | Status |
|---|---|---|
| E2E 테스트 개념과 주의점 | E2E-Testing.md | Planned |
| Selenium / Playwright / Cypress | UI-Test-Tools.md | Planned |
| 시각적 회귀 테스트 | Visual-Regression-Testing.md | Planned |

### 성능 & 부하 테스트

| 주제 | 파일 | Status |
|---|---|---|
| 부하 테스트 vs 스트레스 테스트 vs 소크 테스트 | Load-Stress-Soak-Testing.md | Planned |
| k6 / JMeter | K6-JMeter.md | Planned |

### 테스트 커버리지 & 품질

| 주제 | 파일 | Status |
|---|---|---|
| 코드 커버리지 — 라인/브랜치/조건 커버리지 | Code-Coverage.md | Planned |
| 뮤테이션 테스트 | Mutation-Testing.md | Planned |
| 정적 분석과 린터 | Static-Analysis-Linting.md | Planned |

---

## 학습 순서

```text
테스트 피라미드 & 테스트 더블
           ↓
      단위 테스트 → TDD
           ↓
      통합 테스트
           ↓
      E2E 테스트
           ↓
  부하 테스트 / 커버리지 분석
```

---

## 연관 섹션

- [Engineering/Software-Design/](../Software-Design/) — 테스트 가능한 설계 (SOLID, 의존성 주입)
- [Engineering/Debugging/](../Debugging/) — 실패한 테스트에서 버그 추적
- [Engineering/DevOps/](../DevOps/) — CI 파이프라인에서 자동화 테스트
- [Engineering/Performance/](../Performance/) — 성능 테스트 심화
