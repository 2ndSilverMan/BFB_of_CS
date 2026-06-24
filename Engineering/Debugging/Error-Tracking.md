# 에러 트래킹 (Error Tracking)

- Level: Intermediate
- Prerequisites: [Engineering/Debugging/Logging-Levels.md](Logging-Levels.md), [Engineering/Debugging/Distributed-Log-Correlation.md](Distributed-Log-Correlation.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

에러 트래킹은 production에서 발생한 예외와 crash를 수집, 그룹화, 알림, triage하는 운영 체계다. Sentry, Rollbar 같은 도구가 이 범주에 속한다.

## 직관 (Intuition)

사용자가 오류를 겪고 떠난 뒤에야 알면 늦다. 에러 트래킹은 오류가 어디서 얼마나 자주 누구에게 발생했는지 알려 주는 레이더다.

## 이론 (Theory)

좋은 error event에는 stack trace, release version, environment, user/session fingerprint, request ID, breadcrumbs가 포함된다. Grouping은 같은 root cause를 묶어 noise를 줄인다.

## 구현 (Implementation)

```json
{
  "error": "NullPointerException",
  "release": "2026.06.23",
  "trace_id": "abc",
  "user_impact": "checkout_failed"
}
```

## 복잡도 (Complexity)

Error tracking 비용은 event volume, grouping cardinality, symbolication 품질에 좌우된다. 좋은 grouping은 수많은 event를 소수 issue로 압축하지만, 과도한 fingerprint는 같은 버그를 여러 issue로 쪼갤 수 있다.

## 응용 (Applications)

- production exception triage
- release regression 감지
- 사용자 영향 범위 파악
- crash-free session metric

## 흔한 오해 (Common Misunderstandings)

- 에러 수만 많다고 우선순위가 높은 것은 아니다. 사용자 영향과 빈도를 함께 본다.
- 민감정보를 error context에 남기면 안 된다.
- 모든 예외를 잡아 보고만 하면 프로그램이 잘못된 상태로 계속될 수 있다.
- Grouping이 잘못되면 서로 다른 원인이 섞인다.

## TMI

- Breadcrumb은 오류 전 사용자의 주요 행동 기록이다.
- Release tracking을 켜면 새 배포와 오류 증가를 연결하기 쉽다.
- Alert fatigue를 막으려면 ownership과 severity 기준이 필요하다.

## 연습 / 확인 문제 (Exercises)

- 에러 이벤트에 포함할 필드를 설계하라.
- 사용자 영향 기준 severity를 정의하라.
- 새 release 후 오류 급증을 triage하는 절차를 작성하라.

## 이어서 읽기 (Reading Path)

- 이전: [로그 수준](Logging-Levels.md), [분산 로그 상관](Distributed-Log-Correlation.md)
- 다음: [Postmortem](Postmortem.md)

## 참조 (References)

- [Engineering/Debugging/Stack-Traces.md](Stack-Traces.md)
- [Engineering/DevOps/Metrics-Alerts.md](../DevOps/Metrics-Alerts.md)
