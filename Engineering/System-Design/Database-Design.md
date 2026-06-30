# 데이터베이스 선택과 샤딩 (Database Design and Sharding)

- Level: Intermediate
- Prerequisites: [Systems/Databases/Relational-Model-and-SQL.md](../../Systems/Databases/Relational-Model-and-SQL.md), [Systems/Distributed-Systems/Partitioning.md](../../Systems/Distributed-Systems/Partitioning.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

시스템 설계에서 데이터베이스 선택은 데이터 모델, 일관성, 쿼리 패턴, 확장성, 운영 난이도에 맞는 저장소를 고르는 일이다. 샤딩은 데이터를 여러 partition으로 나눠 저장하는 확장 전략이다.

## 직관 (Intuition)

모든 데이터를 하나의 거대한 서랍에 넣으면 찾기와 확장이 어려워진다. 사용 패턴에 맞는 서랍장을 고르고, 너무 커지면 규칙에 따라 여러 서랍장으로 나눈다.

## 이론 (Theory)

관계형 DB는 트랜잭션과 정합성, 복잡한 질의에 강하다. Key-value, document, wide-column, graph DB는 특정 접근 패턴과 확장성에 최적화된다.

샤딩 키는 데이터 분포와 쿼리 패턴을 결정한다. 나쁜 샤딩 키는 hot shard, cross-shard query, resharding 비용을 만든다. Replication은 read scale과 availability를 높이지만 consistency lag를 고려해야 한다.

## 구현 (Implementation)

```python
def shard_for_user(user_id, shard_count):
    return hash(user_id) % shard_count
```

실제 설계는 resharding, backup, migration, transaction boundary를 함께 고려한다.

## 복잡도 (Complexity)

샤딩은 write/read capacity를 늘리지만 cross-shard join과 transaction을 어렵게 한다. 운영 복잡도는 shard 수, schema migration, failover 전략에 따라 증가한다.

## 응용 (Applications)

- 사용자 단위 대규모 서비스
- multi-tenant SaaS
- time-series partitioning
- read replica 기반 조회 확장

## 흔한 오해 (Common Misunderstandings)

- NoSQL이 항상 더 확장성 있는 선택은 아니다.
- 처음부터 샤딩하면 개발과 운영이 불필요하게 복잡해질 수 있다.
- Read replica는 쓰기 확장을 해결하지 않는다.
- 샤딩 키는 나중에 바꾸기 매우 어렵다.

## TMI

- Directory-based sharding은 key→shard mapping을 별도 저장해 유연성을 높인다.
- Time-based partition은 오래된 데이터 archive에 유리하다.
- Dual write는 일관성 문제가 생기기 쉬워 outbox 같은 패턴을 고려한다.

## 연습 / 확인 문제 (Exercises)

- 채팅 서비스의 샤딩 키 후보를 비교하라.
- 관계형 DB와 document DB 선택 기준을 표로 정리하라.
- Resharding 계획에 필요한 단계를 작성하라.

## 이어서 읽기 (Reading Path)

- 이전: [확장성](Scalability.md)
- 다음: [메시지 큐](Message-Queues.md), [마이크로서비스](Microservices.md)

## 참조 (References)

- [Systems/Databases/Distributed-DB.md](../../Systems/Databases/Distributed-DB.md)
- [Systems/Distributed-Systems/Partitioning.md](../../Systems/Distributed-Systems/Partitioning.md)
