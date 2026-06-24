# 인덱스와 B-트리 (Indexes and B-Tree)

- Level: Intermediate
- Prerequisites: [Systems/Databases/Relational-Model-and-SQL.md](Relational-Model-and-SQL.md), [Data-Structures/Binary-Tree.md](../../Data-Structures/Binary-Tree.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

인덱스는 테이블의 특정 열에 대해 **값 → 행 위치** 매핑을 미리 정렬·구성해 두어, 전체 탐색(full scan) 없이 빠르게 행을 찾게 하는 보조 자료구조다. 대부분의 관계형 데이터베이스는 인덱스를 **B-트리**(정확히는 B+트리)로 구현한다.

## 직관 (Intuition)

수백 쪽짜리 책에서 특정 단어를 찾을 때, 책을 처음부터 읽는 대신 뒤의 색인(index)을 보고 쪽 번호로 바로 간다. 데이터베이스 인덱스도 똑같다. 인덱스가 없으면 모든 행을 훑어야(`O(n)`) 하지만, 인덱스가 있으면 정렬된 트리를 타고 `O(log n)`에 도달한다.

## 이론 (Theory)

**B-트리**는 한 노드가 여러 키와 자식을 갖는 균형 탐색 트리다. 모든 잎의 깊이가 같아 항상 `O(log n)` 높이를 유지한다. 이진 트리와 달리 노드 하나가 **디스크 블록 하나**에 대응하도록 차수(order)를 크게 잡는다 — 한 번의 디스크 읽기로 수백 개 키를 가져오므로, 디스크 접근 횟수(=트리 높이)를 최소화한다.

**B+트리**는 B-트리의 변형으로, 실제 데이터(또는 행 포인터)를 **잎 노드에만** 두고 잎끼리 연결 리스트로 잇는다. 그래서:

- 점 조회(`= 값`)뿐 아니라 **범위 조회(`BETWEEN`, `>`, 정렬)** 가 잎 연결을 따라 효율적이다.
- 내부 노드는 키만 담아 더 많은 분기를 가져 트리가 더 낮아진다.

| 인덱스 종류 | 특징 |
|---|---|
| 클러스터형(clustered) | 행 자체가 인덱스 키 순서로 저장됨(테이블당 1개) |
| 비클러스터형(secondary) | 인덱스가 행의 위치만 가리킴(여러 개 가능) |
| 복합 인덱스(composite) | 여러 열을 묶음, 선두 열 순서가 중요 |
| 해시 인덱스 | 등호 조회에 `O(1)`, 범위 조회 불가 |

## 구현 (Implementation)

SQL에서 인덱스 생성과 활용이다.

```sql
-- 이메일로 자주 조회한다면 인덱스를 만든다
CREATE INDEX idx_users_email ON users(email);

-- 이 쿼리는 풀 스캔 대신 인덱스를 탄다
SELECT * FROM users WHERE email = 'a@example.com';

-- 복합 인덱스: (last_name, first_name) 순서
CREATE INDEX idx_name ON users(last_name, first_name);
-- last_name 단독 조회는 인덱스 사용 가능, first_name 단독은 불가(선두 열 규칙)
```

실행 계획으로 인덱스 사용 여부를 확인한다.

```sql
EXPLAIN SELECT * FROM users WHERE email = 'a@example.com';
```

## 복잡도 (Complexity)

`n`은 행 수다.

| 연산 | 인덱스 없음 | B+트리 인덱스 |
|---|---|---|
| 점 조회(`= 값`) | `O(n)` | `O(log n)` |
| 범위 조회 | `O(n)` | `O(log n + k)` (`k`=결과 수) |
| 삽입/삭제 | `O(1)` 끝에 추가 | `O(log n)` (인덱스 갱신 포함) |

인덱스는 조회를 빠르게 하지만 **쓰기마다 인덱스도 갱신**되므로 삽입·수정 비용과 저장 공간이 늘어난다.

## 응용 (Applications)

- 기본 키·외래 키 조회 가속(대개 자동 인덱싱)
- `WHERE`, `JOIN`, `ORDER BY`, `GROUP BY` 컬럼 최적화
- 유일성 제약(unique index)
- 파일 시스템·키-값 저장소의 색인 구조

## 흔한 오해 (Common Misunderstandings)

- 인덱스가 많을수록 좋은 게 아니다. 쓰기 성능과 저장 공간을 깎아먹으므로 자주 조회하는 열에만 만든다.
- 인덱스가 있어도 항상 쓰이는 건 아니다. 옵티마이저가 풀 스캔이 더 싸다고 판단하면(결과가 테이블 대부분이면) 인덱스를 무시한다.
- 복합 인덱스 `(A, B)`는 `B` 단독 조회에 쓰이지 않는다(선두 열 규칙). 열 순서가 중요하다.
- 인덱스 컬럼에 함수를 씌우면(`WHERE UPPER(name)=...`) 인덱스를 못 탄다. 함수 기반 인덱스를 따로 만들어야 한다.
- 데이터베이스 B-트리와 자료구조 수업의 이진 트리는 다르다. 노드당 수백 키를 담는 다분기 균형 트리다.

## TMI

- B-트리의 "B"가 무엇인지는 창안자 베이어(Bayer)도 명확히 밝히지 않아, Balanced·Bayer·Boeing 등 여러 설이 농담처럼 회자된다.
- 대부분의 RDBMS는 실제로 B+트리를 쓰지만 명령어와 문서에서는 그냥 "B-tree index"라 부른다.
- `SELECT COUNT(*)`가 느릴 때 적절한 인덱스 하나로 수십 배 빨라지는 일이 흔하다. 그래서 실무 튜닝의 첫걸음이 `EXPLAIN`으로 인덱스 사용 여부를 보는 것이다.

## 연습 / 확인 문제 (Exercises)

- 인덱스 유무에 따라 같은 조회의 실행 계획(`EXPLAIN`)이 어떻게 달라지는지 비교하라.
- 복합 인덱스 `(A, B)`가 사용되는 쿼리와 사용되지 않는 쿼리를 각각 작성하라.
- 범위 조회에서 B+트리가 해시 인덱스보다 유리한 이유를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [정규화](Database-Normalization.md)
- 다음: [쿼리 최적화](Query-Optimization.md)
- 관련: [이진 트리](../../Data-Structures/Binary-Tree.md)

## 참조 (References)

- [Systems/Databases/Relational-Model-and-SQL.md](Relational-Model-and-SQL.md)
- [Data-Structures/Binary-Tree.md](../../Data-Structures/Binary-Tree.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
