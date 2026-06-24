# C 타입과 제어 흐름

- Level: Beginner
- Prerequisites: [C 컴파일과 기본 문법](C-Setup-and-Compilation.md), [Programming/Control-Flow.md](../../Control-Flow.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

C의 기본 타입은 정수, 부동소수점, 문자, 배열, 포인터 등으로 구성된다. 조건문과 반복문은 `if`, `switch`, `for`, `while`로 작성한다.

## 직관 (Intuition)

C는 값을 메모리에 어떻게 놓고 어떤 크기로 해석할지 비교적 직접적으로 드러낸다. 타입은 단순 분류가 아니라 메모리 크기와 연산 가능성을 결정한다.

## 핵심 문법 (Core Syntax)

```c
int count = 3;
double ratio = 0.5;
char grade = 'A';

for (int i = 0; i < count; i++) {
    if (i % 2 == 0) {
        printf("%d\n", i);
    }
}
```

## 이론 (Theory)

정수 타입은 signed/unsigned와 크기가 중요하다. 부동소수점은 근사값이다. `char`는 작은 정수 타입이기도 하며 문자 표현에 쓰인다. C의 조건식에서 0은 거짓, 0이 아닌 값은 참으로 취급된다.

## 구현 (Implementation)

변수 선언, 조건문, 반복문을 작은 함수로 분리해 작성하고 compiler warning을 확인한다. 정수 크기, signed/unsigned 비교, 명시적 cast, `switch`의 `break` 누락처럼 C에서 흔한 함정을 예제로 검증한다.

## 복잡도 (Complexity)

조건문 자체는 보통 상수 비용이지만 반복문은 iteration 수가 곧 시간 복잡도를 만든다. 타입 크기는 메모리 사용량과 overflow 범위를 결정하고, signed overflow처럼 정의되지 않은 동작은 최적화 결과까지 바꿀 수 있다.

## 응용 (Applications)

- 입력값 검사
- 반복 처리
- 상태에 따른 분기
- 메모리 크기와 형식 제어

## 흔한 오해 (Common Misunderstandings)

- `=`는 대입이고 `==`는 비교다.
- 정수 overflow는 타입에 따라 위험한 결과를 만든다.
- 배열 크기는 자동으로 저장되지 않는다.
- `switch`에서 `break`를 빼면 다음 case로 fall-through된다.

## TMI

- `sizeof`는 타입이나 객체의 크기를 byte 단위로 준다.
- `stdbool.h`를 쓰면 `bool`, `true`, `false`를 사용할 수 있다.
- Format specifier가 타입과 맞지 않으면 출력이 깨지거나 UB가 될 수 있다.

## 연습 / 확인 문제 (Exercises)

- `sizeof(int)`, `sizeof(double)`, `sizeof(char)`를 출력하라.
- `switch`에서 `break`를 빼고 동작을 확인하라.
- 1부터 100까지 짝수 합을 구하는 코드를 작성하라.

## 이어서 읽기 (Reading Path)

- 이전: [C 기본 문법](C-Setup-and-Compilation.md)
- 다음: [C 포인터와 메모리](C-Pointers-and-Memory.md)

## 참조 (References)

- [Programming/Control-Flow.md](../../Control-Flow.md)
- [Reference/Books.md](../../../Reference/Books.md)
