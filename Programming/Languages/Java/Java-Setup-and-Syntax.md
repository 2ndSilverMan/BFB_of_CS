# Java 실행 환경과 기본 문법

- Level: Beginner
- Prerequisites: [Programming/Variables-and-Types.md](../../Variables-and-Types.md), [Programming/Control-Flow.md](../../Control-Flow.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

Java는 정적 타입 객체지향 언어이며, 소스 코드를 bytecode로 컴파일한 뒤 JVM 위에서 실행한다. `main` 메서드가 프로그램 진입점이다.

## 직관 (Intuition)

Java는 실행 전에 타입과 구조를 비교적 엄격하게 확인한다. 대신 큰 애플리케이션에서 IDE, 리팩터링, 라이브러리 생태계의 도움을 많이 받을 수 있다.

## 핵심 문법 (Core Syntax)

```java
public class Main {
    public static void main(String[] args) {
        int age = 20;
        String name = "Ada";
        System.out.println(name + ": " + age);
    }
}
```

파일명과 public class 이름은 보통 일치해야 한다.

## 이론 (Theory)

JDK는 컴파일러와 개발 도구를 포함하고, JRE/JVM은 실행 환경이다. Java 코드는 `javac`로 `.class` bytecode가 되고, JVM이 이를 실행한다.

## 구현 (Implementation)

`javac`와 `java`로 작은 `main` class를 컴파일·실행하고, package 이름과 directory 구조가 맞는지 확인한다. IDE를 쓰더라도 classpath, build tool, entry point가 실제로 어떻게 연결되는지 한 번은 터미널에서 확인한다.

## 복잡도 (Complexity)

Java 코드는 JVM startup, JIT warmup, GC의 영향을 받는다. 작은 CLI에서는 startup 비용이 두드러지고, 장기 실행 서버에서는 hot method 최적화와 allocation pattern이 성능을 크게 좌우한다.

## 응용 (Applications)

- 서버 애플리케이션
- Android와 JVM 생태계
- 대규모 엔터프라이즈 시스템
- 정적 타입 기반 OOP 학습

## 흔한 오해 (Common Misunderstandings)

- Java는 JavaScript와 다른 언어다.
- 모든 코드는 클래스 안에 들어간다.
- `String` 비교에 `==`를 쓰면 참조 비교가 될 수 있다. 값 비교에는 `.equals`를 쓴다.
- JVM이 있다고 성능을 전혀 신경 쓰지 않아도 되는 것은 아니다.

## TMI

- Java의 "write once, run anywhere"는 bytecode와 JVM 덕분이다.
- `public static void main`은 초보자에게 길어 보이지만 각각 의미가 있다.
- Java는 가비지 컬렉션으로 메모리 해제를 자동화한다.

## 연습 / 확인 문제 (Exercises)

- `Hello, Java`를 출력하는 클래스를 작성하라.
- `int`, `double`, `boolean`, `String` 변수를 선언해 출력하라.
- `String`의 `==`와 `.equals` 차이를 실험하라.

## 이어서 읽기 (Reading Path)

- 이전: [변수와 타입](../../Variables-and-Types.md)
- 다음: [Java 클래스와 객체](Java-Classes-and-Objects.md)

## 참조 (References)

- [Programming/Variables-and-Types.md](../../Variables-and-Types.md)
- [Reference/Books.md](../../../Reference/Books.md)
