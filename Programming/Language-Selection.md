# 언어 선택 가이드 (Language Selection)

- Level: Beginner
- Prerequisites: 없음
- Status: Review

---

## 개념 (Concept)

프로그래밍 언어 선택은 "무엇을 만들고 싶은가"와 "어떤 컴퓨터 지식을 먼저 익히고 싶은가"를 맞추는 결정이다. Python, JavaScript, C, Java, C++은 모두 입문에 쓸 수 있지만, 강조점이 다르다.

| 언어 | 먼저 배우기 좋은 경우 | 강하게 배우는 개념 |
|---|---|---|
| Python | 빠르게 자동화, 데이터 처리, AI 실습을 해 보고 싶을 때 | 표현력, 자료구조 사용, 라이브러리 활용 |
| JavaScript | 웹 페이지 상호작용, 프론트엔드, Node.js를 배우고 싶을 때 | DOM, 이벤트, 비동기, 런타임 API |
| C | 컴퓨터가 메모리와 CPU에서 어떻게 동작하는지 알고 싶을 때 | 포인터, 메모리, 컴파일, 저수준 표현 |
| Java | 객체지향과 안정적인 애플리케이션 구조를 배우고 싶을 때 | 클래스, 인터페이스, 예외, 컬렉션 |
| C++ | 성능과 추상화를 함께 다루고 싶을 때 | RAII, STL, 템플릿, 값/참조 모델 |

## 직관 (Intuition)

첫 언어는 평생 쓸 언어를 고르는 문제가 아니라, 사고방식을 여는 입구를 고르는 문제다.

- Python은 결과를 빨리 보게 해 준다.
- JavaScript는 웹 브라우저에서 바로 눈에 보이는 변화를 만들게 해 준다.
- C는 컴퓨터 내부를 숨기지 않는다.
- Java는 큰 프로그램을 구조화하는 방법을 강조한다.
- C++은 C에 가까운 성능과 고수준 추상화를 함께 다룬다.

한 언어를 깊게 배운 뒤 다른 언어로 넘어가면 변수, 조건문, 반복문, 함수, 배열 같은 공통 개념은 재사용된다. 달라지는 것은 문법, 타입 규칙, 메모리 모델, 표준 라이브러리다.

## 이론 (Theory)

언어를 고를 때는 다음 네 가지 축을 보면 된다.

| 축 | 질문 | 예 |
|---|---|---|
| 타입 검사 | 오류를 언제 잡는가 | Python/JavaScript는 동적 타입, C/Java/C++은 정적 타입 |
| 실행 방식 | 코드를 어떻게 실행하는가 | C/C++은 컴파일, Python/JavaScript는 런타임 중심, Java는 JVM |
| 메모리 관리 | 메모리를 누가 관리하는가 | C/C++은 직접 관리 요소가 크고, Java/Python/JavaScript는 런타임 관리가 크다 |
| 표준 생태계 | 기본 도구가 무엇을 잘하는가 | Python은 데이터/AI, JavaScript는 웹, Java는 서버, C/C++은 시스템/성능 |

처음에는 언어의 모든 기능을 외우기보다 다음 공통 흐름을 익히는 편이 좋다.

```text
값과 타입 -> 조건문/반복문 -> 함수 -> 배열/문자열 -> 모듈/파일 -> 오류 처리 -> 더 큰 프로그램 구조
```

## 구현 (Implementation)

같은 "Hello, world"도 언어마다 프로그램의 기본 단위가 다르다.

```python
print("Hello, world")
```

```javascript
console.log("Hello, world");
```

```c
#include <stdio.h>

int main(void) {
    printf("Hello, world\n");
    return 0;
}
```

```java
public class Main {
    public static void main(String[] args) {
        System.out.println("Hello, world");
    }
}
```

```cpp
#include <iostream>

int main() {
    std::cout << "Hello, world\n";
    return 0;
}
```

입문 단계에서는 문법의 길고 짧음보다 "이 코드가 어디서 시작하고, 값이 어떻게 흐르고, 오류가 어디서 잡히는가"를 보는 것이 더 중요하다.

## 복잡도 (Complexity)

언어 선택 자체에는 알고리즘의 시간/공간 복잡도가 없다. 대신 학습 비용과 실행 모델의 비용 차이가 있다.

| 관점 | Python | JavaScript | C | Java | C++ |
|---|---|---|---|---|---|
| 첫 실행까지의 난이도 | 낮음 | 낮음 | 중간 | 중간 | 중간 |
| 메모리 모델 노출 | 낮음 | 낮음 | 높음 | 중간 | 높음 |
| 대규모 구조화 | 중간 | 중간 | 낮음 | 높음 | 높음 |
| 성능 제어 | 낮음 | 중간 | 높음 | 중간 | 높음 |

성능이 중요한 분야라도 처음부터 C++만 정답은 아니다. 알고리즘과 자료구조를 이해하지 못하면 빠른 언어를 써도 느린 프로그램을 만들 수 있다.

## 응용 (Applications)

- Python: 자동화 스크립트, 데이터 분석, 머신러닝, 웹 백엔드 입문
- JavaScript: 웹 프론트엔드, Node.js 백엔드, 브라우저 자동화, 인터랙티브 UI
- C: 운영체제, 임베디드, 컴퓨터 구조, 네트워크 시스템 기초
- Java: 서버 애플리케이션, Android 기초, 객체지향 설계, 기업용 시스템
- C++: 게임 엔진, 고성능 시스템, 그래픽스, 알고리즘 대회, 실시간 처리

프로젝트 목표가 명확하지 않다면 Python으로 공통 개념을 익히고, 이후 C로 메모리와 시스템을 보강하는 경로가 무난하다.

## 흔한 오해 (Common Misunderstandings)

- 쉬운 언어를 먼저 배우면 나쁜 습관이 생긴다는 말은 과장이다. 중요한 것은 개념을 정확히 배우는 것이다.
- C를 먼저 배우지 않아도 CS를 배울 수 있다. 다만 메모리와 시스템 주제에서는 C가 강력한 도구가 된다.
- Java와 C++은 둘 다 객체지향을 지원하지만 같은 방식으로 프로그램을 짜는 언어는 아니다.
- Python은 느리기만 한 언어가 아니다. 적절한 라이브러리와 알고리즘을 쓰면 실용적인 성능을 낼 수 있다.
- JavaScript가 브라우저 전용 언어라는 말은 이제 맞지 않다. Node.js, 서버리스, 데스크톱 앱 도구에서도 널리 쓰인다.

## TMI

- Python은 Guido van Rossum이 1989년 12월 크리스마스 무렵의 취미 프로젝트로 시작했고, 이름은 뱀이 아니라 BBC 코미디 "Monty Python's Flying Circus"에서 왔다.
- JavaScript는 초기에 매우 짧은 시간 안에 만들어졌고, 지금은 웹 플랫폼의 핵심 언어가 되었다.
- C는 Bell Labs에서 Unix를 구현하는 과정과 함께 성장했고, 이름은 선행 언어인 B의 다음 글자라는 맥락을 가진다.
- Java는 처음에 Oak라는 이름으로 불렸고, 임베디드 소비자 전자기기용 언어에서 인터넷 중심 언어로 방향이 바뀌며 Java가 되었다.
- C++의 `++`는 C 계열 언어의 증가 연산자다. 이름 자체가 "C에서 한 단계 확장"이라는 농담을 품고 있다.
- Python에는 `import antigravity`라는 이스터에그가 있다. 실행하면 웹 브라우저로 관련 만화를 열려고 한다.
- JavaScript의 `NaN`은 자기 자신과도 같지 않다. `Number.isNaN()` 같은 전용 검사가 필요한 이유다.
- C의 `undefined behavior`는 "에러가 난다"가 아니라 "표준이 아무 보장도 하지 않는다"에 가깝다. 컴파일러가 그 상황은 없다고 가정하고 코드를 과감하게 바꿀 수도 있다.
- Java의 `String`은 불변이고, `==`는 문자열 내용 비교가 아니라 참조 비교다. 내용 비교는 보통 `.equals()`를 쓴다.
- C++에는 `std::vector<bool>`처럼 이름은 평범한데 내부 구현이 특수해서 초보자와 숙련자 모두를 당황시키는 타입도 있다.

## 연습 / 확인 문제 (Exercises)

- 다섯 언어 중 하나를 골라 "왜 이 언어부터 배우는지"를 세 문장으로 적어 보라.
- 같은 계산 `1부터 100까지 합`을 Python과 C 스타일 의사코드로 비교해 보라.
- 내가 만들고 싶은 프로그램이 자동화, 시스템, 서버, 게임 중 어디에 가까운지 분류해 보라.

## 이어서 읽기 (Reading Path)

- 이전: [배열과 문자열](Arrays-and-Strings.md)
- 다음: [Python 트랙](Languages/Python/), [JavaScript 트랙](Languages/JavaScript/), [C 트랙](Languages/C/), [Java 트랙](Languages/Java/), [C++ 트랙](Languages/Cpp/)
- 관련: [변수와 타입](Variables-and-Types.md), [조건문과 반복문](Control-Flow.md), [함수와 재귀](Functions-and-Recursion.md)

## 참조 (References)

- [Programming/Languages/](Languages/)
- [Reference/Books.md](../Reference/Books.md)
- [Reference/Courses.md](../Reference/Courses.md)
- [Python.org - Foreword for Programming Python](https://www.python.org/doc/essays/foreword/)
- [Dennis Ritchie - The Development of the C Language](https://www.bell-labs.com/usr/dmr/www/chist.pdf)
- [Oracle - Java Language Specification, First Edition Preface](https://docs.oracle.com/javase/specs/jls/se7/html/jls-0-preface1.html)
- [Bjarne Stroustrup - C++ FAQ](https://www.stroustrup.com/bs_faq.html)
