# 통합 테스트 전략 (Integration Test Strategy)

- Level: Intermediate
- Prerequisites: [Engineering/Testing/Unit-Test-Principles.md](Unit-Test-Principles.md), [Systems/Databases/Transactions-and-ACID.md](../../Systems/Databases/Transactions-and-ACID.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

통합 테스트는 application과 database, queue, filesystem, external service adapter 같은 경계가 실제 contract대로 함께 동작하는지 검증한다.

## 직관 (Intuition)

부품을 각각 검사해도 connector 규격이 다르면 조립품은 실패한다. Integration test는 serialization, transaction, migration, configuration처럼 경계에서 생기는 결함을 찾는다.

## 이론 (Theory)

Test scope를 명시하고 실제 dependency, emulator, fake, stub 중 위험에 맞는 대역을 선택한다. DB test는 production과 같은 engine·migration을 우선하고 test isolation을 transaction rollback, unique schema, disposable container로 만든다.

외부 API는 contract test와 제한된 sandbox test를 조합한다. Timeout, retry, duplicate, partial failure를 포함하고 test data cleanup과 parallel execution을 설계한다.

### 경계 우선순위

통합 테스트는 모든 조합을 다 연결하는 것이 아니라 위험한 경계를 실제로 검증하는 것이다. DB transaction, message queue, 외부 API, serialization format, auth middleware, migration은 단위 테스트로 놓치기 쉬운 결함이 많다.

좋은 전략은 각 경계의 contract, test fixture, 격리 방식, failure mode를 정한다. Testcontainers나 ephemeral database를 쓰면 현실성을 높일 수 있지만 suite 시간이 늘어나므로 병렬화와 데이터 cleanup이 중요하다.

## 구현 (Implementation)

```python
def test_order_is_persisted(repository, migrated_database):
    order_id = repository.create(customer_id="c1", total=500)
    loaded = repository.get(order_id)
    assert loaded.total == 500
    assert loaded.customer_id == "c1"
```

## 복잡도 (Complexity)

환경 시작·migration·I/O 때문에 unit test보다 비싸다. Container·fixture 재사용은 빠르지만 state leakage를 막아야 한다.

## 응용 (Applications)

- repository·migration 검증
- message publish/consume contract
- service adapter와 serialization
- transaction·retry behavior

## 흔한 오해 (Common Misunderstandings)

- 모든 dependency를 mock하면 통합 test가 아니다.
- in-memory DB가 production DB semantic을 완전히 대표하지 않는다.
- sleep으로 eventual consistency를 기다리면 느리고 flaky하다.
- 성공 path만으로 retry·duplicate behavior를 검증할 수 없다.

## TMI

- Testcontainers류 접근은 disposable 실제 dependency를 제공한다.
- polling with deadline은 고정 sleep보다 빠르고 안정적이다.
- consumer-driven contract test는 service 간 기대를 versioned artifact로 만든다.

## 연습 / 확인 문제 (Exercises)

- DB isolation 전략 세 가지를 비교하라.
- at-least-once message duplicate test를 작성하라.
- external API timeout·retry scenario를 설계하라.

## 이어서 읽기 (Reading Path)

- 이전: [단위 테스트 원칙](Unit-Test-Principles.md)
- 다음: [계약 테스트](Contract-Testing.md)

## 참조 (References)

- [Systems/Databases/Transactions-and-ACID.md](../../Systems/Databases/Transactions-and-ACID.md)
- [Reference/Books.md](../../Reference/Books.md)
