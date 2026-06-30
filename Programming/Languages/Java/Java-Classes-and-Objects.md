# Java 클래스와 객체

- Level: Beginner
- Prerequisites: [Java 기본 문법](Java-Setup-and-Syntax.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

Java 클래스는 **필드·생성자·메서드**로 객체의 상태와 행동을 정의한다. 객체는 그 인스턴스이며, **primitive를 제외한 모든 것은 참조(reference)** 로 다뤄지고 힙에 할당돼 GC가 관리한다.

## 직관 (Intuition)

클래스는 설계도, 객체는 그 설계도로 만든 물건. Java는 이 구조를 언어 중심에 둬 큰 프로그램을 타입·모듈로 정리한다. `private` 필드 + public 메서드로 내부 상태를 보호하는 **캡슐화**가 기본 패턴.

## 핵심 문법 (Core Syntax)

```java
class User {
    private final String name;            // final: 재할당 불가
    User(String name) { this.name = name; }   // 생성자
    String greet() { return "Hello, " + name; }
}
```

## 이론 (Theory)

### 1. 참조 시맨틱

`User a = new User("Ada"); User b = a;` 는 **같은 객체**를 가리킨다(aliasing). 인자 전달은 "참조의 값 전달" — 객체 내부는 바꿀 수 있지만 호출자의 변수를 다른 객체로 바꿀 순 없다. `==` 는 참조 동일성, `.equals` 는 값 동등성.

### 2. equals/hashCode/toString 계약

컬렉션·맵 키로 쓰려면 **`equals` 와 `hashCode` 를 함께** 오버라이드해야 한다(같으면 같은 해시). `toString` 은 디버깅·로그용. `record` 는 이 셋 + 생성자를 자동 생성한다.

### 3. final과 불변성

`final` 은 **참조 재바인딩만** 막는다 — `final List l` 의 내부는 변경 가능. 진짜 불변 객체는 모든 필드 final + 방어적 복사. 불변 객체는 **스레드 안전**이라 동시성 버그를 줄인다.

### 4. static

`static` 멤버는 인스턴스가 아니라 **클래스에 속한다**(공유). 전역 변수처럼 남발하면 테스트·상태 관리가 어렵다.

## 구현 (Implementation)

```java
class Counter {
    private int count = 0;                // 불변식: count >= 0
    void increment() { count++; }
    int value() { return count; }
    @Override public String toString() { return "Counter(" + count + ")"; }
}
record Point(int x, int y) {}             // equals/hashCode/toString/생성자 자동

public class Main {
    public static void main(String[] args) {
        Counter c = new Counter(); c.increment(); c.increment();
        System.out.println(c);             // Counter(2)
        System.out.println(new Point(1,2).equals(new Point(1,2)));  // true
    }
}
```

## 복잡도 (Complexity)

| 항목 | 특성 |
|---|---|
| 객체 할당 | 힙 + GC 대상, 많은 작은 객체는 메모리 압박 |
| 메서드 디스패치 | 보통 상수, JIT inlining·계층에 따라 변동 |
| 불변 객체 | 공유 안전(복사 불필요)하나 변경 시 새 객체 |

## 응용 (Applications)

- 도메인 모델링, 서비스 객체, 캡슐화·불변 객체, 테스트 가능한 단위.

## 흔한 오해 (Common Misunderstandings)

- **필드를 public으로 열면 캡슐화가 깨진다** — `private` + 접근자.
- **`static` 남발은 전역 상태** — 테스트·동시성 악화.
- **상속이 항상 최선의 재사용이 아니다** — 합성 우선.
- **`final` 은 깊은 불변이 아니다** — 참조만 고정, 내부는 변경 가능.

## TMI

- `record`(Java 16+)는 불변 데이터 carrier를 한 줄로 — `equals`/`hashCode`/`toString`/접근자 자동.
- `equals` 만 오버라이드하고 `hashCode` 를 안 하면 `HashMap` 에서 못 찾는 유명한 버그가 난다.
- Lombok 같은 도구가 boilerplate를 줄이지만 빌드 도구·애너테이션 처리 이해가 필요하다.

## 연습 / 확인 문제 (Exercises)

- `Book` 클래스를 만들고 제목·저자를 `private` + getter로 캡슐화하라.
- `equals` 만 오버라이드하고 `hashCode` 를 빼서 `HashSet` 중복이 안 걸리는 버그를 재현하라.
- `static` 필드와 인스턴스 필드의 차이를 예제로 보여라.
- 같은 데이터를 `class` 와 `record` 로 만들어 코드량을 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [Java 기본 문법](Java-Setup-and-Syntax.md)
- 다음: [인터페이스와 제네릭](Java-Generics-and-Interfaces.md)
- 관련: [OOP](../../OOP.md)

## 참조 (References)

- [Programming/OOP.md](../../OOP.md)
- [Engineering/Software-Design/SOLID.md](../../../Engineering/Software-Design/SOLID.md)
