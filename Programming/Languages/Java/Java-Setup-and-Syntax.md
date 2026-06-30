# Java 실행 환경과 기본 문법

- Level: Beginner
- Prerequisites: [Programming/Variables-and-Types.md](../../Variables-and-Types.md), [Programming/Control-Flow.md](../../Control-Flow.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

Java는 정적 타입 OOP 언어로, 소스를 **bytecode(`.class`)로 컴파일해 JVM이 실행**한다. "한 번 작성하면 어디서나 실행(write once, run anywhere)"은 bytecode + JVM 덕이다. 진입점은 `public static void main`.

## 직관 (Intuition)

Java는 실행 전에 타입·구조를 엄격히 확인해 큰 애플리케이션에서 IDE·리팩터링·생태계의 도움을 크게 받는다. 대가는 **장황함(verbosity)** 과 JVM 시작 비용. 핵심은 "소스 → `javac` → bytecode → JVM(JIT)"라는 2단계 실행 모델을 이해하는 것.

## 핵심 문법 (Core Syntax)

```java
public class Main {
    static int square(int x) { return x * x; }
    public static void main(String[] args) {
        for (int i = 1; i <= 3; i++) System.out.println(i + " -> " + square(i));
    }
}
```

```bash
javac Main.java && java Main      # 컴파일 후 JVM 실행
```

## 이론 (Theory)

### 1. JDK / JRE / JVM과 실행 흐름

JDK(컴파일러+도구) ⊃ JRE(실행 환경) ⊃ JVM(bytecode 실행기). `javac` 가 `.class` 를 만들고, JVM이 인터프리트하다 **JIT** 가 hot 메서드를 기계어로 컴파일한다. 그래서 장기 실행에서 점점 빨라진다.

### 2. 참조 vs primitive, String 비교

8개 primitive(`int`/`double`/`boolean`…)는 값, 나머지는 참조. **`String` 비교에 `==` 는 참조 비교** → 값 비교는 `.equals`. String은 불변 + 상수 풀 인터닝이라 리터럴은 `==` 가 우연히 true일 수 있어 더 헷갈린다.

### 3. 파일·패키지 규약

`public` 클래스 이름 = 파일명. 패키지는 디렉터리 구조와 일치해야 한다(`com.x.App` → `com/x/App.java`).

## 구현 (Implementation)

```java
public class Main {
    public static void main(String[] args) {
        String a = "hi", b = new String("hi");
        System.out.println(a == b);          // false (다른 객체)
        System.out.println(a.equals(b));     // true  (값 동일)
        int x = 20; double r = 0.5; boolean ok = x > 10;
        System.out.println(x + " " + r + " " + ok);
    }
}
```

## 복잡도 (Complexity)

| 항목 | 특성 |
|---|---|
| JVM 시작 | 작은 CLI에서 두드러짐(수십~수백 ms) |
| JIT warmup | 초기엔 느리고 hot 메서드가 빨라짐 |
| GC | allocation 패턴이 지연·throughput 좌우 |

## 응용 (Applications)

- 서버 애플리케이션, Android·JVM 생태계, 대규모 엔터프라이즈.
- 정적 타입 기반 OOP 학습.

## 흔한 오해 (Common Misunderstandings)

- **Java ≠ JavaScript** — 이름만 비슷.
- **모든 코드는 클래스 안에** (Java 21의 미리보기 제외).
- **`String` `==` 는 참조 비교** — 값은 `.equals`.
- **JVM이 있어도 성능은 무관하지 않다** — allocation·GC·warmup 고려.

## TMI

- `public static void main(String[])` 의 각 토큰엔 의미가 있다(공개·정적·반환없음·진입점·인자 배열).
- bytecode는 `javap -c Main` 으로 볼 수 있다(JVM 명령 집합).
- GraalVM native image는 JVM 없이 AOT 컴파일해 시작 비용을 없앤다(서버리스에 유리).

## 연습 / 확인 문제 (Exercises)

- `Hello, Java` 를 출력하는 클래스를 작성·컴파일·실행하라.
- `String` 의 `==` 와 `.equals` 차이를 리터럴/`new` 로 실험하라.
- `javap -c` 로 간단한 메서드의 bytecode를 확인하라.
- primitive와 참조 타입을 메서드에 넘겨 변경 가능 여부를 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [변수와 타입](../../Variables-and-Types.md)
- 다음: [Java 클래스와 객체](Java-Classes-and-Objects.md)
- 관련: [제어 흐름](../../Control-Flow.md)

## 참조 (References)

- [Programming/Variables-and-Types.md](../../Variables-and-Types.md)
- [Reference/Books.md](../../../Reference/Books.md)
