# 메시지 큐 (Message Queues)

- Level: Intermediate
- Prerequisites: [Systems/Distributed-Systems/Message-Queues-Event-Streaming.md](../../Systems/Distributed-Systems/Message-Queues-Event-Streaming.md), [Engineering/System-Design/Scalability.md](Scalability.md)
- Status: Draft
- Reviewed-by: -

---

> 📍 **초점**: **시스템 설계 관점**에서 메시지 큐의 용도·전달 의미·DLQ를 다룬다.

## 개념 (Concept)

메시지 큐는 producer와 consumer 사이에 메시지를 저장해 비동기 처리, 부하 완충, 서비스 결합도 감소를 제공하는 시스템 구성요소다.

## 직관 (Intuition)

주문을 받는 직원과 요리사가 직접 동시에 맞춰 움직이지 않아도, 주문표를 줄에 쌓아 두면 각자 속도에 맞춰 일할 수 있다. 줄이 너무 길어지면 병목 신호이기도 하다.

## 이론 (Theory)

큐는 at-most-once, at-least-once, effectively-once 처리 의미를 가진다. At-least-once에서는 중복 처리가 가능하므로 consumer는 idempotent해야 한다. Dead-letter queue는 계속 실패하는 메시지를 격리한다.

Event streaming은 append-only log와 consumer offset을 중심으로 하고, queue는 작업 분배에 더 집중하는 경우가 많다.

## 구현 (Implementation)

```python
message = {
    "id": "order-123",
    "type": "OrderCreated",
    "payload": {"user_id": 7},
    "created_at": "2026-06-23T00:00:00Z",
}
```

메시지에는 idempotency key, schema version, trace ID를 포함하는 편이 좋다.

## 복잡도 (Complexity)

Queue lag는 producer rate와 consumer 처리량의 차이로 커진다. 재시도와 backoff가 없으면 장애 시 메시지 폭풍이 생길 수 있다.

## 응용 (Applications)

- 이메일·알림 비동기 전송
- 주문 후속 처리
- 이미지·영상 변환 job
- microservice 간 이벤트 전달

## 흔한 오해 (Common Misunderstandings)

- 큐를 넣으면 작업이 사라지는 것이 아니라 나중으로 밀린다.
- 메시지 중복 가능성을 무시하면 결제·재고 같은 영역에서 사고가 난다.
- 순서 보장은 partition과 key 설계에 따라 달라진다.
- 큐가 DB 트랜잭션을 자동으로 대신하지 않는다.

## TMI

- Outbox pattern은 DB 변경과 메시지 발행 사이 일관성을 다루는 패턴이다.
- Backpressure는 downstream이 감당 가능한 속도로 upstream을 제어한다.
- DLQ는 버리는 곳이 아니라 조사와 재처리를 위한 격리소다.

## 연습 / 확인 문제 (Exercises)

- 알림 발송 시스템에 큐를 넣는 이유를 설명하라.
- At-least-once 처리에서 idempotent consumer를 설계하라.
- DLQ 운영 절차를 작성하라.

## 이어서 읽기 (Reading Path)

- 이전: [확장성](Scalability.md)
- 다음: [마이크로서비스](Microservices.md), [설계 사례](System-Design-Case-Studies.md)
- 같은 주제 다른 관점: [메시지 큐와 이벤트 스트리밍 (분산 시스템 관점)](../../Systems/Distributed-Systems/Message-Queues-Event-Streaming.md)

## 참조 (References)

- [Systems/Distributed-Systems/Message-Queues-Event-Streaming.md](../../Systems/Distributed-Systems/Message-Queues-Event-Streaming.md)
- [Reference/Books.md](../../Reference/Books.md)
