# 분산 트랜잭션: 2PC와 Saga

- Level: Advanced
- Prerequisites: [Systems/Databases/Transactions-and-ACID.md](../Databases/Transactions-and-ACID.md), [Consensus.md](Consensus.md), [Replication.md](Replication.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

분산 트랜잭션은 여러 노드나 서비스에 걸친 작업을 하나의 논리적 단위로 처리하려는 기술이다. 대표 방식으로 2PC(Two-Phase Commit)와 Saga가 있으며, 각각 강한 원자성과 장기 실행 보상 트랜잭션 사이의 trade-off를 가진다.

## 직관 (Intuition)

항공권 예약과 결제를 동시에 처리한다고 하자. 결제만 되고 예약이 실패하면 안 된다. 한 시스템 안에서는 DB 트랜잭션으로 묶기 쉽지만, 여러 서비스와 DB가 얽히면 “모두 성공하거나 모두 되돌리기”가 훨씬 어려워진다.

## 이론 (Theory)

2PC는 coordinator가 participant들에게 prepare를 요청하고, 모두 준비되면 commit을 지시한다.

```text
Phase 1: prepare / vote
Phase 2: commit or abort
```

2PC는 원자성을 제공하지만 coordinator 장애 시 blocking 문제가 생길 수 있다. 또한 긴 lock 보유로 latency와 availability에 부담을 준다.

Saga는 긴 비즈니스 과정을 여러 local transaction의 순서로 나누고, 중간 실패 시 이미 완료된 단계의 보상 트랜잭션을 실행한다. Saga는 강한 isolation보다는 eventual consistency와 비즈니스 보상 로직에 의존한다.

## 구현 (Implementation)

Saga 단계는 명시적으로 실행/보상 함수를 쌍으로 둔다.

```python
steps = [
    ("reserve_inventory", "release_inventory"),
    ("charge_payment", "refund_payment"),
    ("create_shipment", "cancel_shipment"),
]


def planned_compensations(done_steps):
    return [comp for _, comp in reversed(done_steps)]


print(planned_compensations(steps[:2]))
```

실제 구현은 idempotency key, retry policy, outbox pattern, 상태 저장이 필수다.

## 복잡도 (Complexity)

2PC는 네트워크 round trip과 participant 수에 따라 latency가 늘고, lock 유지 시간이 길어진다. Saga는 runtime coordination은 덜 blocking일 수 있지만, 보상 로직과 중간 상태 노출을 설계해야 한다.

## 응용 (Applications)

- 주문/결제/배송 워크플로
- 다중 데이터베이스 업데이트
- 마이크로서비스 간 비즈니스 프로세스
- 금융·재고 시스템의 일관성 관리

## 흔한 오해 (Common Misunderstandings)

- Saga는 ACID 트랜잭션의 완전한 대체물이 아니다.
- 보상 트랜잭션은 항상 원래 작업을 완벽히 되돌릴 수 있는 것이 아니다.
- 2PC는 consensus와 같지 않다.
- 분산 트랜잭션을 도입하기 전에 데이터 소유권과 서비스 경계를 다시 봐야 한다.

## TMI

- Transactional outbox는 DB 변경과 이벤트 발행을 같은 local transaction에 묶어 메시지 유실을 줄인다.
- TCC(Try-Confirm-Cancel)는 예약 기반 비즈니스 프로토콜로 볼 수 있다.
- 많은 시스템은 강한 분산 트랜잭션보다 aggregate 경계와 eventual consistency를 선택한다.

## 연습 / 확인 문제 (Exercises)

- 2PC의 두 단계를 설명하라.
- Saga에서 보상 트랜잭션이 어려운 예를 들어라.
- 주문 시스템에서 outbox pattern이 필요한 이유를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [Consensus](Consensus.md)
- 다음: [시간과 순서](Time-and-Ordering.md)

## 참조 (References)

- [Systems/Databases/Transactions-and-ACID.md](../Databases/Transactions-and-ACID.md)
- [Consensus.md](Consensus.md)
- [Replication.md](Replication.md)
- [Reference/Books.md](../../Reference/Books.md)
