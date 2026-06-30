# 관계형 모델과 SQL (Relational Model and SQL)

- Level: Beginner
- Prerequisites: [Data-Structures/](../../Data-Structures/)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

관계형 모델은 데이터를 **테이블(릴레이션)** 로 표현한다. 각 행(row, 튜플)은 하나의 레코드, 각 열(column, 속성)은 그 레코드의 한 항목이다. **SQL(Structured Query Language)** 은 이 테이블을 정의하고 질의하는 표준 언어다.

## 직관 (Intuition)

엑셀 시트를 떠올리면 된다. 시트가 테이블, 한 줄이 레코드, 한 칸의 머리글이 열이다. 다른 점은, 관계형 데이터베이스는 (1) 행마다 고유 식별자(기본키)를 두고, (2) 테이블끼리 키로 연결하며, (3) SQL로 "어떻게"가 아니라 "무엇을" 원하는지 선언적으로 질의한다는 것이다.

## 이론 (Theory)

핵심 개념:

| 용어 | 의미 |
|---|---|
| 릴레이션(relation) | 테이블 |
| 튜플(tuple) | 행, 하나의 레코드 |
| 속성(attribute) | 열 |
| 기본키(primary key) | 행을 유일하게 식별하는 속성(들) |
| 외래키(foreign key) | 다른 테이블의 기본키를 참조해 관계를 맺는 속성 |

질의의 바탕인 관계대수에는 선택($\sigma$, 행 고르기), 투영($\pi$, 열 고르기), 조인($\bowtie$, 테이블 결합)이 있다. 예를 들어 "나이가 20 이상인 학생의 이름"은 다음과 같다.

$$\pi_{\text{name}}\big(\sigma_{\text{age} \ge 20}(\text{Student})\big)$$

SQL은 데이터 정의(DDL: `CREATE`, `ALTER`)와 데이터 조작(DML: `SELECT`, `INSERT`, `UPDATE`, `DELETE`)으로 나뉜다.

## 구현 (Implementation)

```sql
CREATE TABLE student (
    id    INTEGER PRIMARY KEY,
    name  TEXT NOT NULL,
    age   INTEGER
);

INSERT INTO student (id, name, age) VALUES (1, 'Ada', 36), (2, 'Grace', 30);

-- 나이가 32 미만인 학생 이름을 나이 순으로
SELECT name, age
FROM student
WHERE age < 32
ORDER BY age;
```

파이썬 표준 라이브러리로 바로 실행해 볼 수 있다.

```python
import sqlite3

conn = sqlite3.connect(":memory:")
conn.execute("CREATE TABLE student (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)")
conn.executemany("INSERT INTO student VALUES (?, ?, ?)",
                 [(1, "Ada", 36), (2, "Grace", 30)])
rows = conn.execute("SELECT name FROM student WHERE age < 32").fetchall()
print(rows)   # [('Grace',)]
```

## 복잡도 (Complexity)

`n`은 테이블의 행 수다.

| 질의 | 인덱스 없음 | 인덱스 있음(B-트리) |
|---|---|---|
| 특정 키 조회 | `O(n)` 전체 스캔 | `O(log n)` |
| 범위 조회 | `O(n)` | `O(log n + k)` |
| 조인(중첩 루프) | `O(n · m)` | 인덱스/해시 조인으로 개선 |

인덱스는 조회를 빠르게 하지만 저장 공간과 쓰기 비용을 늘린다. 자세한 내용은 인덱스·B-트리 문서에서 다룬다.

## 응용 (Applications)

- 웹·모바일 백엔드의 영속 저장소
- 거래·재고·사용자 등 정형 데이터 관리
- 분석 질의(집계, 그룹화, 조인)
- 다른 시스템 간 신뢰할 수 있는 데이터 공유

## 흔한 오해 (Common Misunderstandings)

- "관계(relation)"는 테이블을 뜻하지, 테이블 사이의 관계(relationship)를 뜻하지 않는다.
- NoSQL이 항상 더 빠르거나 우월한 것은 아니다. 정합성·조인·트랜잭션이 중요하면 관계형이 강하다.
- `NULL`은 0이나 빈 문자열이 아니라 "값 없음/모름"이다. 비교 결과는 참/거짓이 아니라 `UNKNOWN`이 될 수 있으며, `NULL = NULL`도 참이 아니라 `UNKNOWN`이다. `NULL` 여부는 `IS NULL`로 검사한다.
- `SELECT *`가 항상 편한 것은 아니다. 필요한 열만 고르면 I/O와 네트워크 비용이 준다.

## TMI

- 관계형 모델은 1970년 IBM의 Edgar F. Codd가 제안했다("A Relational Model of Data for Large Shared Data Banks").
- SQL의 발음은 "에스큐엘"과 "시퀄(sequel)"이 모두 쓰인다. 초기 이름이 SEQUEL이었던 데서 후자가 유래했다.
- 같은 SQL이라도 데이터베이스 제품마다 방언(dialect)이 있어, 표준 SQL과 벤더 확장이 섞여 있다.

## 연습 / 확인 문제 (Exercises)

- `student` 테이블에 `major` 열을 추가하고, 전공별 평균 나이를 구하는 `GROUP BY` 질의를 작성하라.
- `course` 테이블을 만들고 `student`와 외래키로 연결한 뒤, 두 테이블을 조인해 보라.
- `WHERE age = NULL`이 왜 원하는 결과를 주지 않는지, 올바른 표현은 무엇인지 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: 없음
- 다음: [정규화](Database-Normalization.md), [인덱스와 B-트리](Indexes-and-B-Tree.md)
- 관련: [이진 트리](../../Data-Structures/Binary-Tree.md), [해시 테이블](../../Data-Structures/Hash-Table.md)

## 참조 (References)

- [Data-Structures/](../../Data-Structures/)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
