# 데이터베이스 쿼리 최적화 (Database Query Optimization)

- Level: Intermediate
- Prerequisites: [Systems/Databases/Query-Optimization.md](../../Systems/Databases/Query-Optimization.md), [Systems/Databases/Indexes-and-B-Tree.md](../../Systems/Databases/Indexes-and-B-Tree.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

> 📍 **초점**: 실행 계획·인덱스·조인을 손보는 **실무 쿼리 튜닝**에 집중한다.

## 개념 (Concept)

데이터베이스 쿼리 최적화는 실행 계획, 인덱스, join 방식, 통계, transaction 비용을 조정해 query latency와 resource 사용을 줄이는 작업이다.

## 직관 (Intuition)

데이터베이스가 테이블 전체를 뒤지는지, 바로 책갈피로 찾아가는지 확인하는 과정이다. 느린 쿼리는 대개 읽은 행 수가 기대보다 많다.

## 이론 (Theory)

Optimizer는 통계와 비용 모델로 plan을 고른다. Index scan, table scan, nested loop join, hash join, sort, materialization 같은 operator를 읽어야 한다. Selectivity가 낮은 index는 도움이 작고, 복합 index는 column 순서가 중요하다. N+1 query, lock wait, transaction isolation도 성능 원인이다.

### Query plan 중심 사고

DB 성능은 SQL 문자열보다 실행 계획이 말해 준다. Index scan, sequential scan, join order, estimated rows와 actual rows 차이를 확인한다. 통계가 낡거나 predicate selectivity가 틀리면 optimizer가 나쁜 계획을 고를 수 있다.

인덱스는 읽기를 빠르게 하지만 쓰기 비용과 저장 공간을 늘린다. 자주 쓰는 query, cardinality, covering index, partial index, migration 비용을 함께 고려한다.

## 구현 (Implementation)

```sql
EXPLAIN ANALYZE
SELECT *
FROM orders
WHERE customer_id = 42
ORDER BY created_at DESC
LIMIT 20;
```

`customer_id, created_at` 복합 인덱스가 있으면 filtering과 ordering을 함께 줄일 수 있다.

## 복잡도 (Complexity)

Index lookup은 보통 `O(log n)`이고 full scan은 `O(n)`이다. 하지만 random I/O, cache hit, join cardinality 때문에 실제 비용은 plan 전체로 봐야 한다.

## 응용 (Applications)

- slow query 개선
- API latency 감소
- batch job 비용 절감
- schema·index review

## 흔한 오해 (Common Misunderstandings)

- 인덱스를 많이 만들수록 항상 빠른 것은 아니다.
- `EXPLAIN` 예상치와 실제 실행 결과는 다를 수 있다.
- `SELECT *`는 I/O와 network 비용을 늘린다.
- ORM이 만든 쿼리도 실행 계획을 봐야 한다.

## TMI

- 통계가 오래되면 optimizer가 나쁜 plan을 고를 수 있다.
- Covering index는 table lookup을 줄인다.
- Query 최적화는 application access pattern과 schema 설계를 같이 봐야 한다.

## 연습 / 확인 문제 (Exercises)

- 같은 쿼리를 index 유무로 `EXPLAIN ANALYZE` 비교하라.
- N+1 query를 join이나 batch fetch로 고쳐라.
- 복합 인덱스 column 순서가 plan에 미치는 영향을 확인하라.

## 이어서 읽기 (Reading Path)

- 이전: [비동기 I/O](Async-IO.md)
- 다음: [네트워크 성능](Network-Performance.md)
- 같은 주제 다른 관점: [쿼리 최적화 (데이터베이스 관점)](../../Systems/Databases/Query-Optimization.md)

## 참조 (References)

- [Systems/Databases/Query-Optimization.md](../../Systems/Databases/Query-Optimization.md)
- [Systems/Databases/Indexes-and-B-Tree.md](../../Systems/Databases/Indexes-and-B-Tree.md)
