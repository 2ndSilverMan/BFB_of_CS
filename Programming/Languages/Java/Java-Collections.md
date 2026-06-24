# Java 컬렉션

- Level: Beginner
- Prerequisites: [Java 인터페이스와 제네릭](Java-Generics-and-Interfaces.md), [Data-Structures/](../../../Data-Structures/)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

Java Collections Framework는 `List`, `Set`, `Map`, `Queue` 같은 자료구조 인터페이스와 구현체를 제공한다. 제네릭과 함께 타입 안전한 컨테이너를 만든다.

## 직관 (Intuition)

컬렉션은 데이터를 담는 표준 상자들이다. 순서가 필요하면 `List`, 중복 제거가 필요하면 `Set`, key-value 검색이 필요하면 `Map`을 먼저 떠올린다.

## 이론 (Theory)

Java 컬렉션은 인터페이스와 구현체를 분리한다. 같은 `List`라도 `ArrayList`와 `LinkedList`의 비용이 다르고, 같은 `Map`이라도 `HashMap`과 `TreeMap`의 ordering·lookup 특성이 다르다.

## 구현 (Implementation)

구현할 때는 변수 타입을 가능한 인터페이스로 두고, 실제 access pattern에 맞춰 구현체를 고른다. key로 쓰는 객체는 `equals`와 `hashCode` 계약을 지켜야 한다.

## 핵심 문법 (Core Syntax)

```java
List<String> names = new ArrayList<>();
names.add("Ada");

Set<String> tags = new HashSet<>();
tags.add("java");

Map<String, Integer> scores = new HashMap<>();
scores.put("Ada", 100);
```

## 복잡도 (Complexity)

`ArrayList`의 index 접근은 O(1), 중간 삽입은 O(n)이다. `HashMap`과 `HashSet`의 lookup은 평균 O(1)이다. `TreeMap`은 정렬을 유지하며 O(log n) 연산을 제공한다.

## 응용 (Applications)

- 목록과 테이블 데이터 처리
- 중복 제거
- 빈도수 계산
- BFS/DFS 같은 알고리즘 구현

## 흔한 오해 (Common Misunderstandings)

- 인터페이스 타입으로 변수를 선언하면 구현체 교체가 쉽다.
- `HashMap` 순서에 의존하면 안 된다.
- 객체를 `HashSet` key로 쓰려면 `equals`와 `hashCode`가 일관되어야 한다.
- 컬렉션을 순회 중 수정하면 `ConcurrentModificationException`이 날 수 있다.

## TMI

- `Collections`는 유틸리티 클래스, `Collection`은 인터페이스다.
- `List.of`는 불변 리스트를 만들 때 편리하다.
- Stream API는 컬렉션 처리 파이프라인을 선언적으로 표현한다.

## 연습 / 확인 문제 (Exercises)

- 문자열 목록의 중복을 `Set`으로 제거하라.
- `Map`으로 단어 빈도수를 계산하라.
- `ArrayList`와 `LinkedList`의 장단점을 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [인터페이스와 제네릭](Java-Generics-and-Interfaces.md)
- 다음: [Java 예외와 파일](Java-Exceptions-and-Files.md)

## 참조 (References)

- [Data-Structures/Array.md](../../../Data-Structures/Array.md)
- [Data-Structures/Hash-Table.md](../../../Data-Structures/Hash-Table.md)
