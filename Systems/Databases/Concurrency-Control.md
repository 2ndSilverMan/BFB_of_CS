# 동시성 제어 (Concurrency Control)

- Level: Intermediate
- Prerequisites: [Systems/Databases/Transactions-and-ACID.md](Transactions-and-ACID.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

동시성 제어는 여러 트랜잭션이 동시에 실행될 때도 **ACID의 격리성(Isolation)을 지키도록** 실행을 조율하는 기법이다. 목표는 동시 실행 결과가 "어떤 순서로든 하나씩 실행한 것(직렬 실행)"과 같아 보이게 만드는 것, 즉 **직렬 가능성(serializability)** 을 보장하는 것이다.

## 직관 (Intuition)

두 사람이 같은 통장에서 동시에 돈을 뽑으면, 잔액을 각자 읽고 각자 차감해 한쪽 출금이 사라질 수 있다(갱신 손실). 동시성 제어는 "동시에 만지면 안 되는 데이터" 앞에 교통 정리를 두어, 결과가 한 명씩 처리한 것과 같게 만든다. 운영체제의 [동기화](../Operating-Systems/Synchronization.md)와 같은 문제를 트랜잭션 수준에서 푸는 것이다.

## 이론 (Theory)

동시 실행에서 생기는 대표 이상 현상은 갱신 손실, 더티 리드, 반복 불가능 읽기, 팬텀이다. 이를 막는 두 큰 접근이 있다.

| 접근 | 핵심 | 특징 |
|---|---|---|
| 비관적(pessimistic) | 잠금(lock)으로 충돌을 미리 막음 | 충돌이 잦을 때 유리, 교착 위험 |
| 낙관적(optimistic) | 일단 실행하고 커밋 시 충돌 검사 | 충돌이 드물 때 유리, 재시도 발생 |

**2단계 잠금(2PL, Two-Phase Locking)** 은 비관적 기법의 대표로, 잠금을 **얻기만 하는 확장 단계**와 **풀기만 하는 수축 단계**로 나눈다. 한 번 잠금을 풀기 시작하면 새 잠금을 얻지 못한다는 규칙이 직렬 가능성을 보장한다. 단, 2PL은 교착 상태를 일으킬 수 있다.

**MVCC(다중 버전 동시성 제어)** 는 데이터를 수정할 때 새 버전을 만들어, **읽기는 잠그지 않고** 적절한 스냅샷 버전을 보게 한다. "읽기는 쓰기를 막지 않고, 쓰기는 읽기를 막지 않는다"가 핵심이라 동시성이 높다. PostgreSQL, MySQL(InnoDB), Oracle이 채택한다.

## 구현 (Implementation)

SQL 표준의 명시적 잠금과 격리 수준 설정이다.

```sql
-- 비관적 잠금: 읽은 행을 커밋까지 잠가 다른 트랜잭션의 수정을 막음
BEGIN;
SELECT balance FROM accounts WHERE id = 1 FOR UPDATE;   -- 행 잠금
UPDATE accounts SET balance = balance - 50 WHERE id = 1;
COMMIT;

-- 격리 수준 조정(동시성 ↔ 일관성 트레이드오프)
SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
```

낙관적 제어는 보통 버전 컬럼으로 구현한다.

```sql
UPDATE items SET stock = stock - 1, version = version + 1
WHERE id = 10 AND version = 3;   -- 영향받은 행이 0이면 충돌 → 재시도
```

## 복잡도 (Complexity)

성능은 **충돌 빈도**와 **격리 강도**의 함수다.

| 상황 | 영향 |
|---|---|
| 격리 수준 ↑ (Serializable) | 일관성↑, 동시성↓, 대기·중단↑ |
| 잠금 범위가 넓음(테이블 잠금) | 충돌·대기 증가 |
| MVCC | 읽기 동시성↑, 그러나 오래된 버전 정리(vacuum) 비용 |
| 낙관적 + 높은 충돌 | 재시도 폭증으로 비효율 |

## 응용 (Applications)

- 은행 이체·재고 차감처럼 갱신 충돌이 치명적인 트랜잭션
- 예약·티켓팅의 좌석 중복 판매 방지
- 협업 편집·버전 관리(낙관적 제어)
- 분산 데이터베이스의 일관성 유지

## 흔한 오해 (Common Misunderstandings)

- 격리 수준이 높을수록 항상 좋은 게 아니다. Serializable은 안전하지만 동시성이 떨어지고 중단·재시도가 늘어, 보통 Read Committed/Repeatable Read를 기본으로 쓴다.
- MVCC가 모든 잠금을 없애는 건 아니다. 쓰기-쓰기 충돌은 여전히 잠금이나 충돌 검사로 막아야 한다.
- 2PL의 "2단계"는 트랜잭션의 commit/rollback 두 단계가 아니라 잠금 **획득/해제** 두 단계를 뜻한다.
- 동시성 제어가 교착을 없애 주지 않는다. 오히려 2PL은 교착을 만들 수 있어, 교착 탐지·타임아웃이 함께 필요하다.

## TMI

- "팬텀 리드"는 같은 조건의 조회를 두 번 했는데 그사이 다른 트랜잭션이 새 행을 끼워 넣어 결과 행 수가 달라지는 현상이다. 범위 잠금(predicate/gap lock)으로 막는다.
- PostgreSQL의 MVCC는 삭제·갱신된 옛 버전(dead tuple)을 남기므로, 주기적인 `VACUUM`으로 정리하지 않으면 테이블이 부풀어 오른다(bloat).
- 격리 수준 이름은 SQL 표준이 정했지만, 실제 동작은 DBMS마다 미묘하게 다르다. 같은 "Repeatable Read"도 구현이 다르다.

## 연습 / 확인 문제 (Exercises)

- 두 트랜잭션이 같은 잔액을 동시에 갱신해 갱신 손실이 생기는 시나리오를 만들고, `FOR UPDATE`로 막아라.
- 2PL이 직렬 가능성을 보장하는 이유를 잠금 획득/해제 순서로 설명하라.
- 낙관적 버전 컬럼 방식으로 재고 차감을 구현하고, 충돌 시 재시도 로직을 추가하라.

## 이어서 읽기 (Reading Path)

- 이전: [트랜잭션과 ACID](Transactions-and-ACID.md)
- 다음: [복구](Recovery.md), [쿼리 최적화](Query-Optimization.md)
- 관련: [동기화](../Operating-Systems/Synchronization.md), [교착 상태](../Operating-Systems/Deadlock.md)

## 참조 (References)

- [Systems/Databases/Transactions-and-ACID.md](Transactions-and-ACID.md)
- [Systems/Operating-Systems/Synchronization.md](../Operating-Systems/Synchronization.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
