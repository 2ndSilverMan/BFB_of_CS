# 분산 시스템 로그 상관 (Trace ID and Span)

- Level: Intermediate
- Prerequisites: [Engineering/Debugging/Structured-Logging.md](Structured-Logging.md), [Engineering/System-Design/Microservices.md](../System-Design/Microservices.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

분산 로그 상관은 여러 서비스에 흩어진 로그를 trace ID, span ID, request ID로 연결해 하나의 요청 흐름으로 재구성하는 방법이다.

## 직관 (Intuition)

주문 요청이 API, 결제, 재고, 알림 서비스를 지나가면 로그도 여러 곳에 흩어진다. 같은 택배 송장번호를 붙이면 어디서 지연되거나 실패했는지 따라갈 수 있다.

## 이론 (Theory)

Trace는 전체 요청 흐름이고, span은 그 안의 개별 작업 구간이다. Context propagation은 HTTP header나 message metadata로 trace 정보를 다음 서비스에 전달한다.

## 구현 (Implementation)

```json
{
  "trace_id": "abc",
  "span_id": "def",
  "service": "payment",
  "event": "payment_authorized"
}
```

## 복잡도 (Complexity)

상관 분석 비용은 요청이 지난 service 수, log event 수, trace/request ID 전파 품질에 비례한다. ID가 끊기면 시간 범위와 사용자 단서로 검색해야 해서 비용이 급격히 커진다.

## 응용 (Applications)

- 마이크로서비스 장애 추적
- latency breakdown
- queue 기반 비동기 흐름 추적
- 사용자 문의 조사

## 흔한 오해 (Common Misunderstandings)

- 서비스마다 request ID를 새로 만들면 end-to-end 상관이 끊긴다.
- 로그에 trace ID만 있고 metric/span이 없으면 latency 분석이 제한된다.
- 비동기 메시지에서도 correlation metadata를 전달해야 한다.
- Trace ID는 보안 토큰이 아니므로 인증에 쓰면 안 된다.

## TMI

- OpenTelemetry는 trace, metrics, logs를 연결하려는 표준 생태계다.
- Baggage는 trace와 함께 전달되는 추가 key-value context다.
- Sampling은 비용을 줄이지만 rare failure를 놓칠 수 있다.

## 연습 / 확인 문제 (Exercises)

- API→queue→worker 흐름에서 trace ID 전달 방식을 설계하라.
- Trace와 span의 차이를 설명하라.
- 로그 검색에서 trace ID가 없는 경우 대안을 제시하라.

## 이어서 읽기 (Reading Path)

- 이전: [구조화 로깅](Structured-Logging.md), [마이크로서비스](../System-Design/Microservices.md)
- 다음: [에러 트래킹](Error-Tracking.md), [Postmortem](Postmortem.md)

## 참조 (References)

- [Engineering/System-Design/Microservices.md](../System-Design/Microservices.md)
- [Engineering/DevOps/Metrics-Alerts.md](../DevOps/Metrics-Alerts.md)
