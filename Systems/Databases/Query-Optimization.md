# 쿼리 최적화 (Query Optimization)

- Level: Intermediate
- Prerequisites: [Systems/Databases/Indexes-and-B-Tree.md](Indexes-and-B-Tree.md), [Systems/Databases/Relational-Model-and-SQL.md](Relational-Model-and-SQL.md)
- Status: Draft
- Reviewed-by: -

---

> 📍 **초점**: 옵티마이저가 실행 계획을 고르는 **DB 내부 동작(RBO/CBO·통계·비용 모델)**을 다룬다.

## 개념 (Concept)

쿼리 최적화는 선언형 SQL 질의를 받아 **같은 결과를 내는 여러 실행 방법(실행 계획, query plan) 중 가장 비용이 적은 것을 고르는** 데이터베이스의 과정이다. 사용자는 "무엇을 원하는지(what)"만 쓰고, 옵티마이저가 "어떻게 가져올지(how)"를 결정한다.

## 직관 (Intuition)

목적지는 같아도 가는 길은 여러 갈래다 — 고속도로, 국도, 골목길. 옵티마이저는 내비게이션처럼 "예상 소요 시간(비용)"을 추정해 가장 빠른 경로를 고른다. 같은 `JOIN`도 어떤 테이블을 먼저 읽고 어떤 방식으로 합치느냐에 따라 수천 배 차이가 난다.

## 이론 (Theory)

옵티마이저는 두 종류가 있다.

| 종류 | 기준 |
|---|---|
| 규칙 기반(RBO) | 미리 정한 우선순위 규칙 |
| 비용 기반(CBO) | 통계(행 수, 분포, 인덱스)로 추정한 비용 — 현대 표준 |

비용 기반 옵티마이저는 **통계(statistics)** 를 바탕으로 각 후보 계획의 비용(디스크 I/O, CPU, 중간 결과 크기)을 추정한다. 핵심 결정은 다음과 같다.

- **접근 경로**: 풀 스캔 vs 인덱스 스캔 ([인덱스](Indexes-and-B-Tree.md) 참고)
- **조인 알고리즘**: 중첩 루프(nested loop), 해시 조인(hash join), 정렬 병합(sort-merge)
- **조인 순서**: 어떤 테이블을 먼저 합칠지(중간 결과를 작게 유지)

조인 순서의 경우의 수는 테이블 수에 대해 지수적으로 늘기 때문에, 옵티마이저는 동적 프로그래밍이나 휴리스틱으로 탐색 공간을 줄인다.

| 조인 알고리즘 | 유리한 경우 |
|---|---|
| 중첩 루프 | 한쪽이 매우 작고 다른 쪽에 인덱스 존재 |
| 해시 조인 | 큰 테이블끼리 등호 조인, 인덱스 없음 |
| 정렬 병합 | 양쪽이 이미 정렬됨, 범위/부등호 조인 |

## 구현 (Implementation)

실행 계획을 읽고 개선하는 흐름이다.

```sql
-- 1) 실행 계획과 실제 비용 확인
EXPLAIN ANALYZE
SELECT o.id, c.name
FROM orders o
JOIN customers c ON o.customer_id = c.id
WHERE o.created_at >= '2026-01-01';

-- 2) 계획에서 풀 스캔이 보이면 조건/조인 컬럼에 인덱스 추가
CREATE INDEX idx_orders_created ON orders(created_at);
CREATE INDEX idx_orders_customer ON orders(customer_id);

-- 3) 통계가 오래됐으면 갱신해 추정 정확도를 높임
ANALYZE orders;
```

## 복잡도 (Complexity)

| 요인 | 영향 |
|---|---|
| 조인 테이블 수 | 계획 탐색 공간이 지수적으로 증가 |
| 통계 정확도 | 부정확하면 잘못된 계획(나쁜 추정) 선택 |
| 결과 선택도(selectivity) | 결과가 적을수록 인덱스가 유리 |
| 중간 결과 크기 | 조인 순서가 좌우, 메모리 초과 시 디스크 사용 |

옵티마이저 자체의 계획 수립 시간과 실제 실행 시간 사이에도 트레이드오프가 있다(짧은 쿼리에 과한 최적화는 낭비).

## 응용 (Applications)

- 느린 쿼리 튜닝(실무 성능 작업의 핵심)
- 리포팅·분석 쿼리의 조인·집계 최적화
- 인덱스 설계 결정의 근거
- ORM이 생성한 비효율 쿼리 진단

## 흔한 오해 (Common Misunderstandings)

- SQL을 다르게 써도 결과가 같으면 보통 같은 계획으로 최적화된다. 형태보다 **인덱스·통계·데이터 분포**가 성능을 좌우한다.
- `EXPLAIN`의 비용 수치는 추정치이지 실제 시간(ms)이 아니다. 실제 측정은 `EXPLAIN ANALYZE`로 본다.
- 인덱스를 만들면 항상 빨라지는 건 아니다. 옵티마이저가 풀 스캔이 더 싸다고 판단하면 인덱스를 안 쓴다.
- 통계가 오래되면 좋은 인덱스가 있어도 나쁜 계획을 고른다. 주기적 통계 갱신이 중요하다.
- 서브쿼리가 항상 조인보다 느린 건 아니다. 옵티마이저가 종종 동일하게 재작성한다.

## TMI

- 비용 기반 옵티마이저는 1979년 IBM System R의 셀린저(Selinger) 논문에서 정립됐고, 지금도 거의 모든 RDBMS가 그 골격을 따른다.
- 통계가 어긋나면 "1행이 나올 줄 알았는데 100만 행"이라 추정해 재앙적 계획이 나온다. 옵티마이저 버그 신고의 상당수가 사실은 오래된 통계 문제다.
- 같은 쿼리가 어제는 빠르고 오늘은 느린 "계획 퇴행(plan regression)"은 통계 변화나 파라미터 스니핑 때문에 생기는, 실무에서 악명 높은 현상이다.

## 연습 / 확인 문제 (Exercises)

- 인덱스 추가 전후로 같은 조인 쿼리의 `EXPLAIN ANALYZE` 결과를 비교하라.
- 중첩 루프 조인과 해시 조인이 각각 선택되는 데이터 조건을 만들어 보라.
- 통계를 일부러 낡게 둔 뒤 `ANALYZE` 실행 전후의 계획 차이를 관찰하라.

## 이어서 읽기 (Reading Path)

- 이전: [인덱스와 B-트리](Indexes-and-B-Tree.md)
- 다음: [NoSQL](NoSQL.md), [분산 데이터베이스](Distributed-DB.md)
- 관련: [동시성 제어](Concurrency-Control.md)
- 같은 주제 다른 관점: [데이터베이스 쿼리 최적화 (성능 관점)](../../Engineering/Performance/Database-Query-Optimization.md)

## 참조 (References)

- [Systems/Databases/Indexes-and-B-Tree.md](Indexes-and-B-Tree.md)
- [Systems/Databases/Relational-Model-and-SQL.md](Relational-Model-and-SQL.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Papers.md](../../Reference/Papers.md)
