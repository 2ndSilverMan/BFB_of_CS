# 정규화 (Database Normalization)

- Level: Intermediate
- Prerequisites: [Systems/Databases/Relational-Model-and-SQL.md](Relational-Model-and-SQL.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

정규화는 관계형 데이터베이스에서 **중복을 줄이고 이상(anomaly)을 없애도록 테이블을 분해**하는 설계 절차다. 데이터가 한 곳에만 저장되도록(single source of truth) 함수 종속(functional dependency)을 분석해 테이블을 단계적으로(1NF, 2NF, 3NF, BCNF) 나눈다.

## 직관 (Intuition)

한 거대한 엑셀 시트에 주문·고객·상품 정보를 모두 담으면, 고객 주소가 바뀔 때 그 고객의 모든 주문 행을 고쳐야 한다. 하나라도 빠뜨리면 데이터가 모순된다. 정규화는 "같은 사실은 한 번만 적는다"는 원칙으로 이 시트를 의미 단위의 작은 테이블로 쪼개는 작업이다.

## 이론 (Theory)

핵심 개념은 **함수 종속** $X \rightarrow Y$ — "$X$가 정해지면 $Y$가 유일하게 정해진다"이다. 정규형은 종속 구조에 대한 제약을 단계별로 강화한다.

| 정규형 | 조건 |
|---|---|
| 1NF | 모든 속성이 원자값(반복 그룹·다중값 금지) |
| 2NF | 1NF + 부분 함수 종속 제거(복합 키의 일부에만 종속되는 속성 없음) |
| 3NF | 2NF + 이행 함수 종속 제거(키가 아닌 속성에 종속되는 속성 없음) |
| BCNF | 모든 결정자(determinant)가 후보 키 |

정규화가 막는 **세 가지 이상(anomaly)** 이 핵심 동기다.

- **삽입 이상**: 주문이 없으면 상품 정보를 넣을 수 없음
- **갱신 이상**: 중복된 값 일부만 고쳐 모순 발생
- **삭제 이상**: 행을 지우면 보존하려던 다른 정보까지 사라짐

3NF와 BCNF는 대부분 일치하지만, 후보 키가 겹치는 특수한 경우 BCNF가 더 엄격하다.

## 구현 (Implementation)

비정규 테이블을 3NF로 분해하는 예다.

```text
-- 비정규: 학생 정보가 수강마다 중복
수강(학번, 이름, 학과, 학과사무실, 과목코드, 성적)
  학번 → 이름, 학과 ;  학과 → 학과사무실  (이행 종속)

-- 3NF 분해
학생(학번 PK, 이름, 학과)
학과(학과 PK, 학과사무실)
수강(학번 FK, 과목코드, 성적,  PK(학번, 과목코드))
```

SQL로는 외래 키로 분해된 테이블을 다시 연결(JOIN)한다.

```sql
SELECT s.이름, d.학과사무실, e.성적
FROM 수강 e
JOIN 학생 s ON e.학번 = s.학번
JOIN 학과 d ON s.학과 = d.학과;
```

## 복잡도 (Complexity)

알고리즘 복잡도가 아니라 **읽기/쓰기 트레이드오프**가 핵심이다.

| 측면 | 정규화 ↑ | 비정규화(역정규화) |
|---|---|---|
| 데이터 중복 | 적음 | 많음 |
| 쓰기·갱신 일관성 | 쉬움 | 어려움(여러 곳 갱신) |
| 읽기 시 조인 수 | 많음 | 적음(빠른 조회) |
| 저장 공간 | 절약 | 증가 |

## 응용 (Applications)

- OLTP(트랜잭션 처리) 시스템의 스키마 설계
- 데이터 무결성이 중요한 금융·재고·예약 시스템
- 반대로 OLAP·분석 시스템은 조회 성능을 위해 의도적으로 역정규화(스타 스키마)

## 흔한 오해 (Common Misunderstandings)

- 정규화가 항상 옳은 것은 아니다. 읽기 성능이 중요하면 의도적으로 역정규화(denormalization)한다.
- "더 높은 정규형이 항상 더 좋다"는 오해다. 보통 3NF/BCNF면 충분하고, 그 이상(4NF, 5NF)은 특수한 다치 종속에서만 의미가 있다.
- 정규화는 성능 최적화 기법이 아니라 무결성 설계 기법이다. 성능은 인덱스·캐시·역정규화로 따로 다룬다.
- 외래 키만 걸면 정규화가 끝나는 게 아니다. 함수 종속 분석이 본질이다.

## TMI

- 정규형 이론은 1970년대 관계형 모델의 창시자 E. F. 코드(Codd)가 1NF~3NF를, 이후 보이스-코드(BCNF)를 정립했다.
- 실무에서는 "3NF로 설계하고, 측정된 병목에 한해 역정규화하라"가 정설이다. 미리 역정규화하는 것은 조기 최적화로 취급된다.
- 스타 스키마(star schema)는 데이터 웨어하우스에서 일부러 역정규화한 대표 구조로, 분석 쿼리의 조인을 줄여 속도를 얻는다.

## 연습 / 확인 문제 (Exercises)

- 주어진 비정규 테이블에서 함수 종속을 모두 찾고 3NF로 분해하라.
- 갱신 이상이 실제로 발생하는 시나리오를 하나 만들고, 정규화로 해결됨을 보여라.
- 3NF이지만 BCNF가 아닌 테이블 예를 만들어 차이를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [관계형 모델과 SQL](Relational-Model-and-SQL.md)
- 다음: [인덱스와 B-트리](Indexes-and-B-Tree.md)
- 관련: [트랜잭션과 ACID](Transactions-and-ACID.md)

## 참조 (References)

- [Systems/Databases/Relational-Model-and-SQL.md](Relational-Model-and-SQL.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
