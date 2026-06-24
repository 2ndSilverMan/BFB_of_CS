# 마이크로서비스 vs 모놀리식 (Microservices vs Monolith)

- Level: Intermediate
- Prerequisites: [Engineering/System-Design/Message-Queues.md](Message-Queues.md), [Engineering/System-Design/Database-Design.md](Database-Design.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

모놀리식은 하나의 배포 단위 안에 여러 기능을 담는 구조이고, 마이크로서비스는 도메인별 작은 서비스들을 독립 배포 단위로 나누는 구조다. 핵심 tradeoff는 조직·배포 독립성과 분산 시스템 복잡도다.

## 직관 (Intuition)

모놀리식은 한 건물 안의 회사이고, 마이크로서비스는 여러 지점이 계약과 통신으로 협업하는 구조다. 지점별 자율성은 커지지만 이동과 조율 비용이 생긴다.

## 이론 (Theory)

서비스 경계는 bounded context와 데이터 소유권을 기준으로 잡는다. 각 서비스가 DB를 독립 소유하면 결합도는 줄지만 cross-service transaction과 query가 어려워진다.

마이크로서비스는 API contract, service discovery, observability, deployment automation, failure isolation이 준비되지 않으면 운영 난이도가 급증한다.

## 구현 (Implementation)

```text
User Service ── emits UserCreated
Order Service ── owns orders DB
Billing Service ── subscribes OrderPaid
```

서비스 간 통신은 동기 HTTP/gRPC와 비동기 messaging을 목적에 맞게 섞는다.

## 복잡도 (Complexity)

네트워크 호출, partial failure, distributed tracing, data consistency, schema evolution이 추가된다. 작은 팀·초기 제품에서는 modular monolith가 더 나은 선택일 수 있다.

## 응용 (Applications)

- 팀별 독립 배포가 필요한 대규모 조직
- 도메인 경계가 명확한 서비스
- 다른 확장 요구를 가진 기능 분리
- 장애 격리와 독립 scaling

## 흔한 오해 (Common Misunderstandings)

- 마이크로서비스는 성능을 자동으로 높이지 않는다.
- DB를 공유하면 서비스 분리 효과가 크게 줄어든다.
- 모놀리식은 나쁜 구조가 아니라 하나의 배포 선택이다.
- 서비스 수가 많을수록 성숙한 observability가 필요하다.

## TMI

- Modular monolith는 내부 모듈 경계를 엄격히 유지하는 단일 배포 구조다.
- Conway's Law는 조직 구조가 시스템 구조에 반영된다는 관찰이다.
- Saga pattern은 분산 transaction 대신 보상 작업을 조합한다.

## 연습 / 확인 문제 (Exercises)

- 쇼핑몰 도메인을 서비스 후보로 나눠 보라.
- Modular monolith와 microservices의 장단점을 비교하라.
- 서비스별 DB 소유권을 두면 생기는 쿼리 문제를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [메시지 큐](Message-Queues.md), [데이터베이스 설계](Database-Design.md)
- 다음: [설계 사례](System-Design-Case-Studies.md)

## 참조 (References)

- [Systems/Distributed-Systems/Distributed-Transactions.md](../../Systems/Distributed-Systems/Distributed-Transactions.md)
- [Reference/Books.md](../../Reference/Books.md)
