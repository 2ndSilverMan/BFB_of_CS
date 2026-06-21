# 트랜잭션과 ACID (Transactions and ACID)

- Level: Intermediate
- Prerequisites: [Systems/Databases/Relational-Model-and-SQL.md](Relational-Model-and-SQL.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

트랜잭션은 "하나로 묶여 전부 성공하거나 전부 취소되어야 하는" 데이터베이스 작업 단위다. **ACID**는 데이터베이스가 트랜잭션에 보장하는 네 가지 성질 — 원자성, 일관성, 격리성, 지속성 — 의 머리글자다.

## 직관 (Intuition)

계좌 이체를 생각하자. "A에서 50 출금"과 "B에 50 입금"은 반드시 둘 다 일어나거나 둘 다 일어나지 않아야 한다. 출금만 되고 입금이 안 되면 돈이 사라진다. 트랜잭션은 이 두 작업을 하나의 묶음으로 보고, 중간에 실패하면 통째로 되돌린다(rollback).

## 이론 (Theory)

| 성질 | 의미 |
|---|---|
| 원자성(Atomicity) | 전부 반영되거나 전부 취소(중간 상태 없음) |
| 일관성(Consistency) | 트랜잭션 전후로 무결성 제약이 유지됨 |
| 격리성(Isolation) | 동시에 실행되는 트랜잭션이 서로 간섭하지 않음 |
| 지속성(Durability) | 커밋된 결과는 장애가 나도 보존됨 |

격리성은 비용이 크기 때문에 보통 **격리 수준(isolation level)** 으로 강도를 조절한다. 약한 격리에서는 다음 이상 현상이 나타날 수 있다.

| 격리 수준 | Dirty Read | Non-repeatable Read | Phantom |
|---|---|---|---|
| Read Uncommitted | 가능 | 가능 | 가능 |
| Read Committed | 불가 | 가능 | 가능 |
| Repeatable Read | 불가 | 불가 | 가능 |
| Serializable | 불가 | 불가 | 불가 |

이 표는 SQL 표준 관점의 요약이다. 실제 DBMS는 이름이 같은 격리 수준도 구현이 다를 수 있다. 예를 들어 PostgreSQL의 Repeatable Read는 스냅샷 격리로 팬텀을 막고, 일부 DBMS는 Read Uncommitted를 요청해도 실제 dirty read를 허용하지 않는다.

높은 격리일수록 정합성은 좋지만 동시성·성능은 떨어진다.

## 구현 (Implementation)

```python
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE account (id INTEGER PRIMARY KEY, balance INTEGER)")
conn.executemany("INSERT INTO account VALUES (?, ?)", [(1, 100), (2, 0)])

try:
    conn.execute("BEGIN")
    conn.execute("UPDATE account SET balance = balance - 50 WHERE id = 1")
    conn.execute("UPDATE account SET balance = balance + 50 WHERE id = 2")
    conn.commit()      # 두 갱신이 함께 확정 (원자성)
except Exception:
    conn.rollback()    # 하나라도 실패하면 전부 취소

print(conn.execute("SELECT id, balance FROM account").fetchall())
# [(1, 50), (2, 50)]
```

## 복잡도 (Complexity)

빅오가 아니라 **정합성과 동시성의 트레이드오프**가 핵심이다.

| 선택 | 정합성 | 동시성/성능 |
|---|---|---|
| 낮은 격리 수준 | 약함 | 높음 |
| 높은 격리 수준 | 강함 | 낮음(잠금·대기 증가) |

잠금(lock)을 많이 쥘수록 충돌·대기·교착 가능성이 커진다.

## 응용 (Applications)

- 금융 이체, 결제, 재고 차감
- 여러 테이블을 함께 갱신하는 모든 업무 로직
- 동시 사용자가 같은 데이터를 다룰 때의 정합성 보장
- 장애 복구(커밋된 데이터의 영속성)

## 흔한 오해 (Common Misunderstandings)

- ACID가 느려서 실무에서 안 쓴다는 것은 오해다. 대부분의 관계형 DB는 기본으로 ACID를 보장한다.
- 격리성은 "직렬화"만을 뜻하지 않는다. 여러 수준이 있고, 대부분의 시스템은 기본값으로 중간 수준을 쓴다.
- 커밋 전 변경은 다른 트랜잭션에 보여서는 안 된다(격리). 보이면 Dirty Read 문제다.
- 트랜잭션이 항상 여러 문장일 필요는 없다. 단일 문장도 트랜잭션으로 처리된다.

## TMI

- 분산 시스템에서는 ACID 대신 **BASE**(Basically Available, Soft state, Eventually consistent)를 택하기도 한다. 가용성·확장성을 위해 강한 일관성을 완화하는 절충이다.
- 많은 DB가 잠금 대신 **MVCC**(다중 버전 동시성 제어)로 읽기와 쓰기가 서로를 막지 않게 한다. PostgreSQL이 대표적이다.
- "I" 격리성은 ACID에서 가장 구현이 까다롭고, 성능 튜닝에서 가장 자주 건드리는 항목이다.

## 연습 / 확인 문제 (Exercises)

- 위 코드에서 두 번째 `UPDATE`가 예외를 던지도록 만들고, 롤백 후 잔액이 그대로인지 확인하라.
- Dirty Read, Non-repeatable Read, Phantom Read를 각각 한 문장 시나리오로 설명하라.
- 어떤 업무가 Serializable이 필요하고 어떤 업무가 Read Committed로 충분한지 예를 들어 보라.

## 이어서 읽기 (Reading Path)

- 이전: [관계형 모델과 SQL](Relational-Model-and-SQL.md)
- 다음: 동시성 제어 (예정 `Concurrency-Control.md`), 복구 (예정 `Recovery.md`)

## 참조 (References)

- [Systems/Databases/Relational-Model-and-SQL.md](Relational-Model-and-SQL.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
