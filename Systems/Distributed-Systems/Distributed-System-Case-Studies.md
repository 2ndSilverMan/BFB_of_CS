# 분산 시스템 사례 (Distributed System Case Studies)

- Level: Advanced
- Prerequisites: [CAP-Theorem.md](CAP-Theorem.md), [Replication.md](Replication.md), [Partitioning.md](Partitioning.md), [Message-Queues-Event-Streaming.md](Message-Queues-Event-Streaming.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

분산 시스템 사례 학습은 Kafka, Cassandra 같은 실제 시스템이 replication, partitioning, ordering, consistency trade-off를 어떻게 조합했는지 분석하는 것이다. 목적은 제품 암기가 아니라 설계 선택의 이유와 결과를 이해하는 것이다.

## 직관 (Intuition)

분산 시스템 이론은 레고 블록이고, 실제 시스템은 그 블록으로 지은 건물이다. 같은 블록을 써도 어떤 문제를 우선하느냐에 따라 구조가 달라진다. 사례 분석은 “왜 이렇게 만들었을까?”를 묻는 훈련이다.

## 이론 (Theory)

사례 분석 프레임은 다음 질문으로 시작한다.

- 데이터 모델: log, key-value, table, document 중 무엇인가?
- partitioning: 어떤 key로 나누는가?
- replication: leader 기반인가, leaderless인가?
- consistency: 어떤 읽기/쓰기 보장을 제공하는가?
- failure handling: 노드 장애와 네트워크 파티션을 어떻게 다루는가?
- operational model: rebalancing, compaction, monitoring은 어떻게 하는가?

예를 들어 Kafka는 partitioned append-only log와 consumer offset 모델이 핵심이고, Cassandra류 시스템은 consistent hashing, replication factor, tunable consistency가 핵심 설계 요소다.

## 구현 (Implementation)

사례 분석은 표로 정리하면 비교가 쉽다.

```python
systems = [
    {"name": "Kafka", "core": "partitioned log", "order": "per partition"},
    {"name": "Cassandra", "core": "wide-column store", "order": "by partition key"},
]

for s in systems:
    print(f"{s['name']}: {s['core']} / ordering={s['order']}")
```

실무에서는 공식 문서의 architecture, failure mode, consistency guarantee를 함께 읽는다.

## 복잡도 (Complexity)

실제 시스템은 단일 알고리즘보다 운영 복잡도가 크다. compaction, rebalancing, backpressure, tombstone, split-brain, schema evolution 같은 세부 요소가 성능과 안정성에 영향을 준다.

## 응용 (Applications)

- 기술 선택 평가
- 시스템 설계 면접 준비
- 장애 사례 분석
- 운영 runbook과 capacity planning

## 흔한 오해 (Common Misunderstandings)

- 유명한 시스템의 설계가 모든 문제에 맞는 것은 아니다.
- “Kafka를 쓴다”는 말은 메시징 문제 전체가 해결됐다는 뜻이 아니다.
- 사례를 볼 때 benchmark 수치보다 workload와 consistency 요구를 먼저 봐야 한다.
- 제품 이름보다 underlying design pattern을 이해하는 것이 더 오래 간다.

## TMI

- Cassandra의 tunable consistency는 읽기/쓰기 quorum 조합으로 trade-off를 조절한다.
- Kafka의 partition은 병렬성과 순서 보장의 단위다.
- 좋은 장애 회고는 시스템의 추상 설계보다 운영 현실을 더 많이 알려준다.

## 연습 / 확인 문제 (Exercises)

- Kafka partition이 ordering과 throughput에 주는 영향을 설명하라.
- leaderless replication 시스템에서 read repair가 필요한 이유를 말하라.
- 새로운 분산 저장소를 평가할 때 물어볼 질문 5개를 작성하라.

## 이어서 읽기 (Reading Path)

- 이전: [메시지 큐와 이벤트 스트리밍](Message-Queues-Event-Streaming.md)
- 다음: [Engineering/System-Design/](../../Engineering/System-Design/)

## 참조 (References)

- [CAP-Theorem.md](CAP-Theorem.md)
- [Replication.md](Replication.md)
- [Partitioning.md](Partitioning.md)
- [Reference/Papers.md](../../Reference/Papers.md)
