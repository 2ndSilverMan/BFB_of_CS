# Java 클래스와 객체

- Level: Beginner
- Prerequisites: [Programming/OOP.md](../../OOP.md), [Java 기본 문법](Java-Setup-and-Syntax.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

Java 클래스는 필드, 생성자, 메서드를 묶어 객체의 상태와 행동을 정의한다. 객체는 클래스에서 만들어진 인스턴스다.

## 직관 (Intuition)

클래스는 설계도, 객체는 그 설계도로 만든 물건이다. Java는 이 구조를 언어의 중심에 두어 큰 프로그램을 타입과 모듈 단위로 정리한다.

## 핵심 문법 (Core Syntax)

```java
class User {
    private final String name;

    User(String name) {
        this.name = name;
    }

    String greet() {
        return "Hello, " + name;
    }
}
```

`private` 필드와 public 메서드로 내부 상태를 보호하는 캡슐화가 기본 패턴이다.

## 이론 (Theory)

생성자는 객체 초기화를 담당한다. `this`는 현재 객체를 가리킨다. `static` 멤버는 인스턴스가 아니라 클래스에 속한다. 상속은 `extends`, 인터페이스 구현은 `implements`로 표현한다.

## 구현 (Implementation)

필드, 생성자, method를 작게 정의하고 class invariant를 constructor에서 세운다. `private` field와 public method로 캡슐화한 뒤, `toString`, `equals`, `hashCode`가 필요한 객체인지 의도적으로 결정한다.

## 복잡도 (Complexity)

객체 allocation은 GC 대상이 되고, 많은 작은 객체는 memory pressure를 만들 수 있다. Method dispatch는 보통 상수 비용이지만 JIT inlining 여부와 class hierarchy에 따라 실제 비용이 달라진다.

## 응용 (Applications)

- 도메인 모델링
- 서비스 객체 구성
- 캡슐화와 불변 객체
- 테스트 가능한 단위 설계

## 흔한 오해 (Common Misunderstandings)

- 필드를 무조건 public으로 열면 캡슐화가 깨진다.
- `static`을 전역 변수처럼 남발하면 테스트와 상태 관리가 어려워진다.
- 상속이 항상 재사용의 최선은 아니다.
- `final`은 참조 재할당을 막지만 객체 내부 변경 가능성까지 항상 막지는 않는다.

## TMI

- Record는 단순 데이터 carrier를 간결하게 선언하는 Java 기능이다.
- Lombok 같은 도구는 반복 코드를 줄이지만 빌드 도구 이해가 필요하다.
- 불변 객체는 동시성 버그를 줄이는 데 도움이 된다.

## 연습 / 확인 문제 (Exercises)

- `Book` 클래스를 만들고 제목과 저자를 필드로 저장하라.
- `private` 필드와 getter를 사용해 캡슐화를 구현하라.
- `static` 필드와 인스턴스 필드의 차이를 예제로 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [Java 기본 문법](Java-Setup-and-Syntax.md), [OOP](../../OOP.md)
- 다음: [인터페이스와 제네릭](Java-Generics-and-Interfaces.md)

## 참조 (References)

- [Programming/OOP.md](../../OOP.md)
- [Engineering/Software-Design/SOLID.md](../../../Engineering/Software-Design/SOLID.md)
