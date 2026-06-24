# 로깅 시스템 (Logging Systems)

- Level: Intermediate
- Prerequisites: [Engineering/Debugging/Structured-Logging.md](../Debugging/Structured-Logging.md), [Engineering/DevOps/Metrics-Alerts.md](Metrics-Alerts.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

로깅 시스템은 application과 infrastructure가 남긴 event record를 수집, 저장, 검색, 보존해 debugging과 audit에 활용하는 관찰 가능성 구성 요소다.

## 직관 (Intuition)

장애가 난 뒤 기억에 의존하지 않기 위해 서비스가 지나간 발자국을 시간순으로 남긴다. 좋은 로그는 나중의 나에게 보내는 편지다.

## 이론 (Theory)

로그 pipeline은 agent, collector, transport, storage, query UI로 구성된다. ELK/Elastic Stack은 search 중심, Loki는 label과 log stream 중심 접근을 제공한다. Structured logging은 JSON field로 검색성을 높인다. Cardinality, retention, sampling, PII masking, cost control이 중요하다. 로그는 metric·trace와 correlation ID로 연결될 때 가치가 커진다.

## 구현 (Implementation)

```json
{
  "level": "error",
  "message": "payment failed",
  "request_id": "req-123",
  "user_id": "u-42",
  "error": "timeout"
}
```

민감 정보는 수집 전에 제거하거나 마스킹한다.

## 복잡도 (Complexity)

로그량은 traffic과 log level에 비례해 빠르게 증가한다. 저장 비용, index 비용, query latency, retention 정책을 함께 설계한다.

## 응용 (Applications)

- 장애 원인 분석
- audit trail
- security event investigation
- deployment change 영향 확인

## 흔한 오해 (Common Misunderstandings)

- 로그를 많이 남기면 항상 좋은 것은 아니다.
- Debug level을 production에서 오래 켜면 비용과 개인정보 위험이 커진다.
- 로그만으로 metric alert를 대체하기 어렵다.
- Correlation ID가 없으면 분산 요청 추적이 급격히 어려워진다.

## TMI

- High-cardinality field를 index label로 쓰면 비용과 성능 문제가 생길 수 있다.
- Sampling은 비용을 줄이지만 rare event를 놓칠 수 있다.
- Audit log는 수정 불가능성과 접근 통제가 특히 중요하다.

## 연습 / 확인 문제 (Exercises)

- 결제 실패 로그에 필요한 field를 설계하라.
- 개인정보가 들어갈 수 있는 log field를 찾아라.
- 로그 retention 정책을 서비스 중요도별로 나눠라.

## 이어서 읽기 (Reading Path)

- 이전: [Ansible](Ansible.md)
- 다음: [분산 트레이싱](Distributed-Tracing.md)

## 참조 (References)

- [Engineering/Debugging/Structured-Logging.md](../Debugging/Structured-Logging.md)
- [Engineering/Debugging/Distributed-Log-Correlation.md](../Debugging/Distributed-Log-Correlation.md)

