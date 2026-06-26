# Java 예외와 파일

- Level: Intermediate
- Prerequisites: [Java 컬렉션](Java-Collections.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

Java 예외는 실행 중 오류를 표현하는 객체이며, 파일 입출력은 `java.nio.file`과 stream/reader API로 처리한다. Java는 checked exception과 unchecked exception을 구분한다.

## 직관 (Intuition)

예외는 "정상 경로로 계속 갈 수 없다"는 신호다. 파일 작업은 실패할 수밖에 없는 외부 세계와 만나는 지점이므로 예외 처리가 기본이다.

## 핵심 문법 (Core Syntax)

```java
import java.nio.file.Files;
import java.nio.file.Path;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {
        try {
            String text = Files.readString(Path.of("input.txt"));
            System.out.println(text);
        } catch (IOException e) {
            System.err.println("파일을 읽지 못했습니다: " + e.getMessage());
        }
    }
}
```

## 이론 (Theory)

Checked exception은 메서드 시그니처에 선언하거나 잡아야 한다. Runtime exception은 주로 프로그래밍 오류를 나타낸다. Try-with-resources는 닫아야 하는 자원을 자동으로 정리한다.

## 구현 (Implementation)

파일은 `try-with-resources`로 열어 자동 close되게 하고, 예외는 구체 type별로 처리한다. 실패한 파일 경로, encoding, 권한 문제를 메시지에 남기되 민감 정보는 출력하지 않는다.

```java
import java.io.BufferedReader;
import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;

public class Main {
    public static void main(String[] args) {
        try (BufferedReader r = Files.newBufferedReader(Path.of("input.txt"))) {
            String line;
            while ((line = r.readLine()) != null) {  // try-with-resources
                System.out.println(line);
            }
        } catch (IOException e) {                     // 구체 예외 처리
            System.err.println("읽기 실패: " + e.getMessage());
        }
    }
}
```

## 복잡도 (Complexity)

정상 흐름에서 예외를 반복적으로 던지면 stack trace 생성 비용이 크다. 파일 I/O는 byte 수, buffering, storage latency에 좌우되며, 큰 파일은 streaming 처리로 memory 사용량을 제한한다.

## 응용 (Applications)

- 설정 파일 읽기
- 로그 파일 처리
- 사용자 입력 검증
- 오류를 의미 있는 도메인 예외로 변환

## 흔한 오해 (Common Misunderstandings)

- 예외를 빈 `catch`로 삼키면 디버깅이 어려워진다.
- 모든 오류를 checked exception으로 만들 필요는 없다.
- Stack trace는 숨길 것이 아니라 원인 추적에 필요한 정보다.
- 파일 경로는 실행 위치와 운영체제에 따라 다르게 해석될 수 있다.

## TMI

- `Path`와 `Files`는 현대 Java 파일 처리의 기본 API다.
- Try-with-resources는 `AutoCloseable`을 구현한 객체에 적용된다.
- 예외 wrapping은 low-level 오류를 domain-level 오류로 바꿀 때 쓴다.

## 연습 / 확인 문제 (Exercises)

- 파일을 읽어 줄 수를 세는 프로그램을 작성하라.
- 존재하지 않는 파일을 읽을 때의 예외를 처리하라.
- Checked exception과 unchecked exception 예시를 각각 찾아라.

## 이어서 읽기 (Reading Path)

- 이전: [Java 컬렉션](Java-Collections.md)
- 다음: [Engineering/Testing](../../../Engineering/Testing/), [Software Design](../../../Engineering/Software-Design/)

## 참조 (References)

- [Engineering/Debugging/Stack-Traces.md](../../../Engineering/Debugging/Stack-Traces.md)
- [Reference/Books.md](../../../Reference/Books.md)
