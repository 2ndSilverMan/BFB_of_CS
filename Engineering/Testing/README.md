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
| 테스트 피라미드 — 단위/통합/E2E의 비율과 원칙 | [Testing-Pyramid.md](Testing-Pyramid.md) | Draft |
| 테스트 더블 — Mock, Stub, Fake, Spy | [Test-Doubles.md](Test-Doubles.md) | Draft |
| 경계값 분석과 동등 분할 | [Boundary-Value-Analysis.md](Boundary-Value-Analysis.md) | Draft |

### 단위 테스트

| 주제 | 파일 | Status |
|---|---|---|
| 단위 테스트 작성 원칙 — FIRST, AAA 패턴 | [Unit-Test-Principles.md](Unit-Test-Principles.md) | Draft |
| TDD (Test-Driven Development) — Red-Green-Refactor | [TDD.md](TDD.md) | Draft |
| BDD (Behavior-Driven Development) | [BDD.md](BDD.md) | Draft |
| 테스트 가능한 설계 — 의존성 주입, 인터페이스 분리 | [Testable-Design.md](Testable-Design.md) | Draft |

### 통합 테스트

| 주제 | 파일 | Status |
|---|---|---|
| 통합 테스트 전략 — 서비스 간 경계 검증 | [Integration-Test-Strategy.md](Integration-Test-Strategy.md) | Draft |
| 계약 테스트 (Contract Testing) — Pact | [Contract-Testing.md](Contract-Testing.md) | Draft |
| 데이터베이스 테스트 — 트랜잭션 롤백, 픽스처 | [Database-Testing.md](Database-Testing.md) | Draft |

### E2E & UI 테스트

| 주제 | 파일 | Status |
|---|---|---|
| E2E 테스트 개념과 주의점 | [E2E-Testing.md](E2E-Testing.md) | Draft |
| Selenium / Playwright / Cypress | [UI-Test-Tools.md](UI-Test-Tools.md) | Draft |
| 시각적 회귀 테스트 | [Visual-Regression-Testing.md](Visual-Regression-Testing.md) | Draft |

### 성능 & 부하 테스트

| 주제 | 파일 | Status |
|---|---|---|
| 부하 테스트 vs 스트레스 테스트 vs 소크 테스트 | [Load-Stress-Soak-Testing.md](Load-Stress-Soak-Testing.md) | Draft |
| k6 / JMeter | [K6-JMeter.md](K6-JMeter.md) | Draft |

### 테스트 커버리지 & 품질

| 주제 | 파일 | Status |
|---|---|---|
| 코드 커버리지 — 라인/브랜치/조건 커버리지 | [Code-Coverage.md](Code-Coverage.md) | Draft |
| 뮤테이션 테스트 | [Mutation-Testing.md](Mutation-Testing.md) | Draft |
| 정적 분석과 린터 | [Static-Analysis-Linting.md](Static-Analysis-Linting.md) | Draft |

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
