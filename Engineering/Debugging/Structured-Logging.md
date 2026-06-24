# 구조화 로깅 (Structured Logging)

- Level: Intermediate
- Prerequisites: [Engineering/Debugging/Scientific-Debugging.md](Scientific-Debugging.md), [Engineering/DevOps/Metrics-Alerts.md](../DevOps/Metrics-Alerts.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

구조화 로깅은 자유형 문자열 대신 timestamp, level, event name, request ID, key-value field를 schema에 맞춰 기록해 검색·집계·상관 분석을 가능하게 한다.

## 직관 (Intuition)

일기 문장보다 열이 정해진 사건 표에 가깝다. 사람이 읽을 message와 기계가 query할 field를 분리하면 "특정 model version의 timeout"을 정확히 찾을 수 있다.

## 이론 (Theory)

Log event에는 안정적인 event name, severity, timestamp, service/version, correlation ID, outcome과 필요한 context를 둔다. High-cardinality field는 log에는 가능하지만 metric label로 직접 변환하지 않는다.

비밀번호, token, session, 원문 개인정보는 allowlist·redaction으로 차단한다. Error log에는 stack과 retryability를 남기고 같은 failure를 여러 layer에서 중복 log하지 않는다. Sampling·retention은 비용과 조사 가능성을 교환한다.

## 구현 (Implementation)

```python
import json


event = {
    "event": "payment_failed",
    "level": "error",
    "request_id": "opaque-123",
    "reason": "gateway_timeout",
    "retryable": True,
}
print(json.dumps(event, ensure_ascii=False))
```

## 복잡도 (Complexity)

Serialization은 field data 크기에 선형이고 log I/O는 high-throughput path의 병목이 될 수 있다. Async buffer는 지연을 줄이지만 crash 시 유실 정책이 필요하다.

## 응용 (Applications)

- incident search·aggregation
- distributed request correlation
- audit trail
- error grouping·SLO 분석 보조

## 흔한 오해 (Common Misunderstandings)

- JSON 형식만 쓰면 schema가 자동 일관되지는 않는다.
- 모든 request body를 log하면 보안·비용 문제가 생긴다.
- log를 metric 대용으로 무제한 집계하면 비효율적이다.
- 동일 오류 중복 log는 signal보다 noise를 늘린다.

## TMI

- trace ID는 여러 service log를 연결하지만 사용자 identity와 같지 않다.
- event schema version은 consumer query의 호환성을 돕는다.
- sampling에서도 error·rare event는 별도 보존할 수 있다.

## 연습 / 확인 문제 (Exercises)

- login failure log의 안전한 schema를 설계하라.
- 민감 field redaction test를 작성하라.
- 문자열 log를 query 가능한 event로 바꿔라.

## 이어서 읽기 (Reading Path)

- 이전: [스택 트레이스](Stack-Traces.md)
- 다음: [분산 로그 상관](Distributed-Log-Correlation.md)

## 참조 (References)

- [Engineering/DevOps/Metrics-Alerts.md](../DevOps/Metrics-Alerts.md)
- [Reference/Books.md](../../Reference/Books.md)
