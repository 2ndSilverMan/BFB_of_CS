# 데이터베이스 (Databases)

> 데이터를 영구적으로 저장하고 효율적으로 질의하는 시스템.

**선수지식**: [Data-Structures/](../../Data-Structures/) (기본 자료구조)

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

| 주제 | 파일 | Status |
|---|---|---|
| 관계형 모델과 SQL | [Relational-Model-and-SQL.md](Relational-Model-and-SQL.md) | Draft |
| 정규화 (1NF ~ BCNF) | [Database-Normalization.md](Database-Normalization.md) | Draft |
| 인덱스와 B-트리 | [Indexes-and-B-Tree.md](Indexes-and-B-Tree.md) | Draft |
| 트랜잭션과 ACID | [Transactions-and-ACID.md](Transactions-and-ACID.md) | Draft |
| 동시성 제어 (잠금, MVCC) | [Concurrency-Control.md](Concurrency-Control.md) | Draft |
| 복구 (WAL, REDO/UNDO) | [Recovery.md](Recovery.md) | Draft |
| 쿼리 최적화 | [Query-Optimization.md](Query-Optimization.md) | Draft |
| NoSQL (키-값, 문서, 컬럼, 그래프) | [NoSQL.md](NoSQL.md) | Draft |
| 분산 데이터베이스 | [Distributed-DB.md](Distributed-DB.md) | Draft |

---

## 학습 순서

```text
Relational-Model-and-SQL → Database-Normalization → Indexes-and-B-Tree
        ↓
Transactions-and-ACID → Concurrency-Control → Recovery
        ↓
Query-Optimization → NoSQL → Distributed-DB
```

---

## 연관 섹션

- [Data-Structures/](../../Data-Structures/) — B-트리, 해시, 그래프 등 저장 구조 기반
- [Systems/Distributed-Systems/](../Distributed-Systems/) — 복제, 샤딩, 분산 트랜잭션
- [Engineering/System-Design/](../../Engineering/System-Design/) — 데이터 저장소 선택과 확장 설계
- [Engineering/Performance/](../../Engineering/Performance/) — 인덱스, 쿼리 계획, I/O 병목 최적화
