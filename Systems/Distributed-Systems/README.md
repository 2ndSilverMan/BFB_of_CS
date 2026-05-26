# 분산 시스템 (Distributed Systems)

> 여러 컴퓨터가 협력하는 시스템의 원리와 어려움.

**선수지식**: [Systems/Networks/](../Networks/), [Systems/Databases/](../Databases/), [Systems/Operating-Systems/](../Operating-Systems/)

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

| 주제 | 파일 | Status |
|---|---|---|
| 시스템 모델과 장애 유형 | System-Models.md | Planned |
| CAP 정리와 PACELC | CAP-Theorem.md | Planned |
| 분산 합의 (Paxos, Raft) | Consensus.md | Planned |
| 복제 (단일 리더, 다중 리더, 리더리스) | Replication.md | Planned |
| 파티셔닝 (샤딩) | Partitioning.md | Planned |
| 분산 트랜잭션 (2PC, Saga) | Distributed-Transactions.md | Planned |
| 시간과 순서 (논리적 시계, 벡터 시계) | Time-and-Ordering.md | Planned |
| 메시지 큐와 이벤트 스트리밍 | Message-Queues-Event-Streaming.md | Planned |
| 분산 시스템 사례 (Kafka, Cassandra 등) | Distributed-System-Case-Studies.md | Planned |

---

## 학습 순서

```text
System-Models → Time-and-Ordering
       ↓
CAP-Theorem → Replication → Partitioning
       ↓
Consensus → Distributed-Transactions
       ↓
Message-Queues-Event-Streaming → Distributed-System-Case-Studies
```

---

## 연관 섹션

- [Systems/Networks/](../Networks/) — 분산 노드 간 통신과 장애 모델
- [Systems/Databases/](../Databases/) — 복제, 샤딩, 트랜잭션의 저장 시스템 적용
- [Engineering/System-Design/](../../Engineering/System-Design/) — 대규모 서비스 아키텍처 설계
- [Engineering/DevOps/](../../Engineering/DevOps/) — 분산 시스템 배포와 운영 자동화
