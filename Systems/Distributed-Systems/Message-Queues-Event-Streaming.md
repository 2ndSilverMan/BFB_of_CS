# 메시지 큐와 이벤트 스트리밍 (Message Queues and Event Streaming)

- Level: Intermediate
- Prerequisites: [Systems/Networks/TCP-UDP.md](../Networks/TCP-UDP.md), [Replication.md](Replication.md), [Time-and-Ordering.md](Time-and-Ordering.md)
- Status: Draft
- Reviewed-by: -

---

> 📍 **초점**: producer/consumer·offset·파티션 등 **분산 시스템 내부 동작**과 이벤트 스트리밍을 다룬다.

## 개념 (Concept)

메시지 큐와 이벤트 스트리밍은 서비스들이 직접 동기 호출로 강하게 결합되지 않고, 메시지나 이벤트를 통해 비동기적으로 통신하게 하는 시스템이다. 큐는 작업 전달과 소비에, 스트리밍 로그는 이벤트의 순서 있는 저장과 재처리에 강하다.

## 직관 (Intuition)

식당에서 주문을 주방에 직접 외치는 대신 주문표를 큐에 넣으면, 주방은 자기 속도대로 처리할 수 있다. 이벤트 스트리밍은 주문표가 사라지는 것이 아니라 시간순 장부에 남아 여러 팀이 각자 읽는 것에 가깝다.

## 이론 (Theory)

핵심 개념은 다음과 같다.

- Producer: 메시지를 발행한다.
- Consumer: 메시지를 읽고 처리한다.
- Topic/queue: 메시지의 논리적 채널.
- Offset/ack: 어디까지 처리했는지 기록한다.
- Consumer group: 여러 consumer가 partition을 나누어 처리한다.

전송 보장은 at-most-once, at-least-once, effectively-once 같은 수준으로 나뉜다. 정확히 한 번 처리처럼 보이게 하려면 idempotent consumer, transactional outbox, deduplication, offset commit 순서를 함께 설계해야 한다.

## 구현 (Implementation)

consumer는 메시지를 처리한 뒤 ack 또는 offset commit을 해야 한다.

```python
processed = set()


def handle(message):
    if message["id"] in processed:
        return "duplicate ignored"
    # side effect would happen here
    processed.add(message["id"])
    return "processed"


print(handle({"id": "m1", "payload": "create-order"}))
print(handle({"id": "m1", "payload": "create-order"}))
```

중복 처리를 견디는 idempotency가 메시징 시스템 안정성의 핵심이다.

## 복잡도 (Complexity)

큐 자체는 처리량을 높일 수 있지만 end-to-end latency, retry 폭주, poison message, ordering constraint가 복잡도를 만든다. partition을 늘리면 병렬성은 늘지만 key별 순서 보장 범위는 partition 내부로 제한된다.

## 응용 (Applications)

- 비동기 작업 처리
- 이벤트 기반 마이크로서비스
- 로그 수집과 스트림 처리
- 데이터 파이프라인과 CDC

## 흔한 오해 (Common Misunderstandings)

- 메시지 큐를 넣으면 시스템이 자동으로 느슨하게 결합되는 것은 아니다. 이벤트 스키마가 새로운 계약이 된다.
- at-least-once 전송에서는 중복 처리를 반드시 고려해야 한다.
- 큐는 장애를 없애지 않고 지연시키거나 흡수한다.
- 메시지 순서는 전체 순서인지 key/partition별 순서인지 구분해야 한다.

## TMI

- Kafka류 로그 기반 시스템은 메시지를 소비 후 즉시 삭제하지 않고 보존 기간 동안 재처리를 허용한다.
- Dead-letter queue는 계속 실패하는 메시지를 별도 격리해 전체 처리를 막지 않게 한다.
- Outbox와 CDC를 결합하면 DB 변경과 이벤트 발행의 원자성 문제를 완화할 수 있다.

## 연습 / 확인 문제 (Exercises)

- queue와 event stream의 차이를 설명하라.
- at-least-once 처리에서 idempotent consumer가 필요한 이유를 말하라.
- partition key 선택이 ordering과 throughput에 미치는 영향을 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [시간과 순서](Time-and-Ordering.md)
- 다음: [분산 시스템 사례](Distributed-System-Case-Studies.md)
- 같은 주제 다른 관점: [메시지 큐 (시스템 설계 관점)](../../Engineering/System-Design/Message-Queues.md)

## 참조 (References)

- [Time-and-Ordering.md](Time-and-Ordering.md)
- [Replication.md](Replication.md)
- [Systems/Networks/TCP-UDP.md](../Networks/TCP-UDP.md)
- [Reference/Books.md](../../Reference/Books.md)
