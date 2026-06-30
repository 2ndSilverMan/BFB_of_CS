# Java 예외와 파일

- Level: Intermediate
- Prerequisites: [Java 컬렉션](Java-Collections.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

Java 예외는 실행 중 오류를 표현하는 **객체**, 파일 I/O는 `java.nio.file`(`Path`/`Files`)와 stream/reader로 처리한다. Java는 **checked**(컴파일러가 처리를 강제)와 **unchecked**(런타임) 예외를 구분한다.

## 직관 (Intuition)

예외는 "정상 경로로 못 간다"는 신호다. 파일은 *실패할 수밖에 없는 외부 세계*와 만나는 지점이라 예외 처리가 기본. 핵심 도구는 **try-with-resources** — 자원을 자동으로 닫아 누수를 막는다([RAII](../Cpp/Cpp-References-and-RAII.md)의 Java판).

## 핵심 문법 (Core Syntax)

```java
import java.nio.file.*; import java.io.IOException;
try {
    String text = Files.readString(Path.of("input.txt"));
    System.out.println(text);
} catch (IOException e) {                       // checked: 잡거나 throws 선언
    System.err.println("읽기 실패: " + e.getMessage());
}
```

## 이론 (Theory)

### 1. checked vs unchecked

| | checked | unchecked(RuntimeException) |
|---|---|---|
| 예 | `IOException`, `SQLException` | `NullPointerException`, `IllegalArgument` |
| 의미 | 복구 가능한 외부 실패 | 주로 프로그래밍 오류 |
| 강제 | 잡거나 `throws` 선언 | 강제 없음 |

### 2. try-with-resources와 unwinding

`try (Reader r = ...)` 는 블록을 벗어날 때 **예외 여부와 무관하게** `r.close()` 를 부른다(`AutoCloseable`). 여러 자원은 **선언 역순**으로 닫히고, close 중 예외는 **suppressed exception** 으로 보존된다.

### 3. 예외 wrapping과 비용

low-level 예외를 도메인 예외로 **wrapping**(`throw new ServiceException(e)`)해 추상화를 지킨다. 예외 생성은 **stack trace 캡처 비용**이 커서, 정상 흐름 제어에 예외를 쓰면 안 된다.

## 구현 (Implementation)

```java
import java.io.*; import java.nio.file.*;
public class Main {
    static long countLines(Path p) throws IOException {
        try (BufferedReader r = Files.newBufferedReader(p)) {   // 자동 close
            long n = 0; while (r.readLine() != null) n++; return n;   // 스트리밍
        }
    }
    public static void main(String[] args) {
        try { System.out.println(countLines(Path.of("input.txt"))); }
        catch (NoSuchFileException e) { System.err.println("없는 파일: " + e.getFile()); }
        catch (IOException e) { System.err.println("I/O 오류: " + e.getMessage()); }
    }
}
```

## 복잡도 (Complexity)

| 항목 | 특성 |
|---|---|
| 예외 throw | stack trace 캡처 비용(흐름 제어로 남용 금지) |
| 파일 I/O | 바이트 수·버퍼링·스토리지 지연 |
| `readString`(전체) | 메모리 $O(\text{파일})$ → 큰 파일은 스트리밍 |

## 응용 (Applications)

- 설정·로그 파일 처리, 사용자 입력 검증.
- low-level 오류를 의미 있는 도메인 예외로 변환.

## 흔한 오해 (Common Misunderstandings)

- **빈 `catch` 로 삼키면** 디버깅 불가(조용한 붕괴).
- **모든 오류를 checked로 만들 필요 없다** — 프로그래밍 오류는 unchecked.
- **stack trace는 숨길 게 아니라** 원인 추적 정보 — 로그로 보존.
- **파일 경로는 실행 위치·OS에 따라** 다르게 해석된다.

## TMI

- `Path`/`Files`(NIO.2)가 현대 표준 — 옛 `java.io.File` 보다 풍부·안전.
- try-with-resources는 `AutoCloseable` 구현 객체(파일·소켓·DB 커넥션)에 적용.
- `Files.lines(path)`(Stream)는 lazy 스트리밍이라 반드시 try-with-resources로 닫아야 한다(파일 핸들 유지).

## 연습 / 확인 문제 (Exercises)

- 파일 줄 수를 try-with-resources + 스트리밍으로 세라.
- 없는 파일 읽기의 `NoSuchFileException` 을 구체적으로 처리하라.
- checked/unchecked 예외 예를 각각 만들고 컴파일러 강제 차이를 보여라.
- low-level `IOException` 을 도메인 예외로 wrapping하라(원인 보존).

## 이어서 읽기 (Reading Path)

- 이전: [Java 컬렉션](Java-Collections.md)
- 다음: [테스트 더블](../../../Engineering/Testing/Test-Doubles.md)
- 관련: [스택 트레이스](../../../Engineering/Debugging/Stack-Traces.md)

## 참조 (References)

- [Engineering/Debugging/Stack-Traces.md](../../../Engineering/Debugging/Stack-Traces.md)
- [Reference/Books.md](../../../Reference/Books.md)
