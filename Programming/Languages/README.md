# 언어별 학습 트랙 (Programming Languages)

> Python, JavaScript, C, Java, C++을 공통 프로그래밍 개념에서 실제 언어 사용으로 연결하는 학습 경로.

**선수지식**: [Programming/](../)

---

## 현재 가용성

현재 이 하위 섹션은 언어별 목차를 먼저 제공한다. 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있고, `Planned` 파일명은 아직 본문이 없는 예정 주제다.

각 언어 트랙은 변수, 조건문, 반복문, 함수 같은 공통 개념을 이미 알고 있다는 전제로 시작한다. 처음이라면 [언어 선택 가이드](../Language-Selection.md)를 먼저 읽는다.

---

## 서브섹션

| 트랙 | 내용 | 권장 선수지식 | Status |
|---|---|---|---|
| [Python/](Python/) | 빠른 실습, 자동화, 데이터/AI 입문에 적합한 언어 | [변수와 타입](../Variables-and-Types.md), [조건문과 반복문](../Control-Flow.md) | Draft |
| [JavaScript/](JavaScript/) | 웹 브라우저와 Node.js에서 UI, 서버, 비동기를 다루는 언어 | [함수와 재귀](../Functions-and-Recursion.md) | Draft |
| [C/](C/) | 메모리, 포인터, 컴파일, 시스템 기초를 익히는 언어 | [배열과 문자열](../Arrays-and-Strings.md) | Draft |
| [Java/](Java/) | 객체지향, 타입, 예외, 컬렉션 기반 애플리케이션 언어 | [함수와 재귀](../Functions-and-Recursion.md) | Draft |
| [Cpp/](Cpp/) | 성능, RAII, STL, 템플릿을 함께 다루는 언어 | [C/](C/), [배열과 문자열](../Arrays-and-Strings.md) | Draft |

---

## 학습 순서

```text
언어 선택 가이드
      ↓
Python 또는 JavaScript ── 빠른 실습 / 웹 입문
      ↓
C ─────── 메모리와 시스템 감각
      ↓
Java 또는 C++ ── 애플리케이션 구조 / 성능 중심 추상화
```

Python을 반드시 먼저 해야 하는 것은 아니다. 웹 프론트엔드가 목표라면 JavaScript부터 시작해도 되고, 시스템과 임베디드가 목표라면 C부터 시작해도 된다.

---

## TMI

- [Python](Python/)은 이름만 보면 뱀 같지만, 실제 이름 유래는 BBC 코미디 "Monty Python's Flying Circus"다.
- [JavaScript](JavaScript/)는 Java와 이름이 비슷하지만 같은 언어 계열이 아니다.
- [C](C/)는 선행 언어 B의 흐름에서 나왔고, Unix와 거의 함께 성장했다.
- [Java](Java/)는 초기에 Oak라는 이름으로 불렸고, 소비자 전자기기용 언어에서 인터넷 시대의 언어로 방향이 바뀌었다.
- [C++](Cpp/)의 `++`는 C 계열 언어의 증가 연산자다. "C를 한 단계 올린다"는 뜻을 이름에 담은 셈이다.
- Python은 들여쓰기가 문법이라 코드 스타일 논쟁을 언어가 강제로 줄여 버린 쪽에 가깝다.
- JavaScript의 `NaN`은 자기 자신과 같지 않다. `NaN === NaN`은 `false`다.
- C는 작은 언어처럼 보이지만 `undefined behavior` 때문에 컴파일러와 표준을 모르면 매우 이상한 결과를 볼 수 있다.
- Java는 JVM 덕분에 Kotlin, Scala, Clojure 같은 다른 언어들과 같은 런타임 생태계를 공유한다.
- C++은 "가능은 한데 추천하지 않는 방법"이 많은 언어라, 팀의 코딩 규칙이 특히 중요하다.

---

## 연관 섹션

- [Data-Structures/](../../Data-Structures/) - 언어별 배열, 리스트, 컬렉션 사용 뒤에 이어지는 자료구조
- [Systems/](../../Systems/) - C/C++ 학습 뒤에 자연스럽게 이어지는 시스템 지식
- [Engineering/Software-Design/](../../Engineering/Software-Design/) - Java/C++ 객체지향 학습 뒤에 이어지는 설계 지식
