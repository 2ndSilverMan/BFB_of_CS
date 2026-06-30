# 데이터베이스 테스트 (Database Testing)

- Level: Intermediate
- Prerequisites: [Engineering/Testing/Integration-Test-Strategy.md](Integration-Test-Strategy.md), [Systems/Databases/Transactions-and-ACID.md](../../Systems/Databases/Transactions-and-ACID.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

데이터베이스 테스트는 실제 DB 또는 DB에 가까운 환경에서 query, transaction, migration, repository layer가 올바르게 동작하는지 검증한다.

## 직관 (Intuition)

DB 코드는 mock으로만 검증하면 SQL 문법, index, constraint, transaction 동작을 놓칠 수 있다. 중요한 경계는 실제와 비슷한 DB로 확인해야 한다.

## 이론 (Theory)

테스트 격리는 transaction rollback, schema reset, fixture loading, containerized DB로 만든다. 각 테스트가 독립적이어야 순서 의존 flakiness가 줄어든다. Migration도 테스트 대상이다.

### 데이터 상태와 격리

DB 테스트의 어려움은 query correctness보다 상태 관리에 있다. 테스트 간 데이터가 섞이면 순서 의존성이 생기고, 실제 transaction isolation과 다른 fixture는 운영 버그를 숨긴다. 각 테스트는 독립 schema, transaction rollback, deterministic seed 중 하나로 격리한다.

Migration, index, constraint, lock behavior는 mock DB로 잡기 어렵다. 중요한 query와 migration은 실제 DB engine에서 검증하고, production과 다른 SQLite 대체가 의미를 바꾸지 않는지 주의한다.

## 구현 (Implementation)

```text
setup schema -> load fixture -> run repository method -> assert rows -> rollback
```

Production DB와 다른 in-memory DB를 쓰면 dialect 차이를 조심해야 한다.

## 복잡도 (Complexity)

DB 테스트는 단위 테스트보다 느리다. Fixture가 커질수록 유지보수와 실행 시간이 늘어난다. 병렬 테스트는 schema와 connection isolation이 필요하다.

## 응용 (Applications)

- repository/query 검증
- migration 검증
- transaction rollback 확인
- constraint와 index 사용 확인

## 흔한 오해 (Common Misunderstandings)

- ORM을 쓴다고 DB 테스트가 불필요한 것은 아니다.
- In-memory DB가 production DB와 완전히 같은 동작을 보장하지 않는다.
- 테스트 데이터가 너무 크면 테스트 의도가 흐려진다.
- 테스트가 공유 DB 상태에 의존하면 flaky해진다.

## TMI

- Testcontainers류 접근은 실제 DB를 컨테이너로 띄워 dialect 차이를 줄인다.
- Migration down script도 복구 전략 관점에서 검증 가치가 있다.
- Seed data와 fixture는 목적이 다르다.

## 연습 / 확인 문제 (Exercises)

- 고유 제약 조건 위반 테스트를 작성하라.
- Transaction rollback 기반 격리 전략을 설명하라.
- In-memory DB 사용의 장단점을 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [통합 테스트 전략](Integration-Test-Strategy.md)
- 다음: [E2E 테스트](E2E-Testing.md)

## 참조 (References)

- [Systems/Databases/Transactions-and-ACID.md](../../Systems/Databases/Transactions-and-ACID.md)
- [Reference/Books.md](../../Reference/Books.md)
