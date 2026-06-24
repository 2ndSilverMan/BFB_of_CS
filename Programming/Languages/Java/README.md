# Java 학습 트랙 (Java)

> 정적 타입, 객체지향, 예외, 컬렉션을 바탕으로 큰 프로그램 구조를 익히는 언어 트랙.

**선수지식**: [Programming/](../../), [함수와 재귀](../../Functions-and-Recursion.md)

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

| Order | 주제 | 파일 | 설명 | Status |
|---|---|---|---|---|
| 1 | 실행 환경과 기본 문법 | [Java-Setup-and-Syntax.md](Java-Setup-and-Syntax.md) | JDK, main 메서드, 컴파일/실행, 기본 타입 | Draft |
| 2 | 클래스와 객체 | [Java-Classes-and-Objects.md](Java-Classes-and-Objects.md) | 클래스, 필드, 메서드, 생성자, 캡슐화 | Draft |
| 3 | 인터페이스와 제네릭 | [Java-Generics-and-Interfaces.md](Java-Generics-and-Interfaces.md) | interface, generic type, 다형성 기본 | Draft |
| 4 | 컬렉션 | [Java-Collections.md](Java-Collections.md) | List, Set, Map과 반복 패턴 | Draft |
| 5 | 예외와 파일 | [Java-Exceptions-and-Files.md](Java-Exceptions-and-Files.md) | checked/unchecked exception, 파일 입출력 | Draft |

---

## 학습 순서

```text
Java-Setup-and-Syntax -> Java-Classes-and-Objects
        ↓
Java-Generics-and-Interfaces -> Java-Collections -> Java-Exceptions-and-Files
```

---

## TMI

- Java는 처음에 Oak라는 이름으로 불렸다. Oracle의 Java Language Specification 초판 서문도 이 사실을 언급한다.
- 원래는 임베디드 소비자 전자기기 쪽을 목표로 했지만, 이후 인터넷과 웹 브라우저 시대에 맞춰 방향이 크게 바뀌었다.
- Java의 유명한 구호인 "write once, run anywhere"는 JVM 위에서 같은 바이트코드를 여러 환경에서 실행한다는 아이디어와 연결된다.
- `String` 비교에서 `==`가 가끔 맞아 보이는 이유는 문자열 interning 때문이다. 그래도 내용 비교는 `.equals()`를 쓰는 것이 맞다.
- Java의 `NullPointerException`은 너무 흔해서, 최근 Java는 어떤 변수가 null이었는지 더 자세히 알려 주는 메시지를 제공한다.
- `public static void main(String[] args)`에서 `String[] args`는 `String... args`로도 쓸 수 있다. 입문서에는 잘 안 나오지만 같은 진입점으로 인정된다.

---

## 연관 섹션

- [Programming/](../../) - 언어 공통 개념
- [Engineering/Software-Design/](../../../Engineering/Software-Design/) - 객체지향 이후 설계 원칙
- [Engineering/Testing/](../../../Engineering/Testing/) - Java 애플리케이션 품질 관리

## 참조

- [Oracle - Java Language Specification, First Edition Preface](https://docs.oracle.com/javase/specs/jls/se7/html/jls-0-preface1.html)
