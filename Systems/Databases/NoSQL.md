# NoSQL: 키-값, 문서, 컬럼, 그래프 데이터베이스

- Level: Intermediate
- Prerequisites: [Relational-Model-and-SQL.md](Relational-Model-and-SQL.md), [Indexes-and-B-Tree.md](Indexes-and-B-Tree.md), [Systems/Distributed-Systems/CAP-Theorem.md](../Distributed-Systems/CAP-Theorem.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

NoSQL은 관계형 모델만으로 다루기 어려운 확장성, 유연한 스키마, 특정 접근 패턴을 위해 설계된 데이터베이스 계열을 넓게 부르는 말이다. 키-값, 문서, 컬럼 패밀리, 그래프 데이터베이스가 대표적이다.

## 직관 (Intuition)

모든 데이터를 표와 조인으로 다루는 것이 항상 최선은 아니다. 캐시처럼 키로 바로 꺼내야 하는 데이터, JSON 문서처럼 구조가 유연한 데이터, 거대한 로그/시계열, 복잡한 관계 탐색은 각각 다른 저장 모델이 더 잘 맞을 수 있다.

## 이론 (Theory)

대표 유형은 다음과 같다.

- Key-value store: key로 value를 빠르게 읽고 쓴다.
- Document DB: JSON/BSON 같은 문서 단위 저장과 질의.
- Wide-column store: row key와 column family 중심의 대규모 분산 저장.
- Graph DB: 노드와 간선을 중심으로 관계 탐색.

NoSQL 선택은 CAP, consistency model, query pattern, index 지원, transaction 지원 범위를 함께 봐야 한다. “스키마가 없다”기보다 스키마 제약이 애플리케이션 쪽으로 이동하는 경우가 많다.

## 구현 (Implementation)

문서형 모델에서는 한 객체의 관련 정보를 한 문서에 묶어 읽기 패턴을 최적화할 수 있다.

```json
{
  "user_id": "u1",
  "name": "Ada",
  "addresses": [
    {"type": "home", "city": "Seoul"},
    {"type": "work", "city": "Pangyo"}
  ]
}
```

자주 함께 읽는 데이터는 embedding이 유리할 수 있고, 독립적으로 자주 수정되는 데이터는 reference가 유리할 수 있다.

## 복잡도 (Complexity)

NoSQL 시스템의 비용은 자료구조와 분산 설계에 따라 다르다. 키-값 조회는 보통 빠르지만, ad-hoc query나 join은 제한적일 수 있다. 분산 저장에서는 replication, partitioning, consistency 비용이 성능과 운영 복잡도를 좌우한다.

## 응용 (Applications)

- 캐시와 세션 저장
- 이벤트 로그와 시계열 저장
- 유연한 사용자 프로필 문서
- 소셜 그래프와 추천 관계 탐색

## 흔한 오해 (Common Misunderstandings)

- NoSQL이 SQL보다 항상 빠르다는 뜻은 아니다.
- NoSQL이 트랜잭션을 전혀 지원하지 않는다는 말도 정확하지 않다. 제품마다 범위가 다르다.
- 스키마가 없으면 운영이 쉬워지는 것이 아니라, 스키마 관리 위치가 바뀐다.
- 관계형 DB로 충분한 문제에 NoSQL을 도입하면 복잡도만 늘 수 있다.

## TMI

- 많은 현대 관계형 DB도 JSON, full-text, replication 등 NoSQL적 기능을 흡수했다.
- 데이터 모델 선택은 “무엇을 저장하는가”보다 “어떻게 읽고 쓰는가”에 더 좌우된다.
- polyglot persistence는 서비스별로 적합한 저장소를 조합하는 접근이다.

## 연습 / 확인 문제 (Exercises)

- key-value store와 document DB의 차이를 예로 설명하라.
- NoSQL에서 denormalization이 자주 쓰이는 이유를 말하라.
- 어떤 요구사항이면 관계형 DB를 그대로 선택하는 편이 더 안전한지 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [쿼리 최적화](Query-Optimization.md)
- 다음: [분산 데이터베이스](Distributed-DB.md)

## 참조 (References)

- [Relational-Model-and-SQL.md](Relational-Model-and-SQL.md)
- [Indexes-and-B-Tree.md](Indexes-and-B-Tree.md)
- [Systems/Distributed-Systems/CAP-Theorem.md](../Distributed-Systems/CAP-Theorem.md)
- [Reference/Books.md](../../Reference/Books.md)
