# C 컴파일과 기본 문법

- Level: Beginner
- Prerequisites: [Programming/Variables-and-Types.md](../../Variables-and-Types.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

C는 소스 코드를 컴파일러가 기계어 실행 파일로 바꾸는 정적 타입 언어다. `main` 함수에서 실행이 시작되고, 헤더와 소스 파일을 조합해 프로그램을 만든다.

## 직관 (Intuition)

Python이 통역사를 옆에 두고 바로 읽히는 언어라면, C는 출발 전에 번역본 실행 파일을 만들어 두는 방식이다. 그래서 컴파일 오류와 링크 오류를 읽는 능력이 중요하다.

## 핵심 문법 (Core Syntax)

```c
#include <stdio.h>

int main(void) {
    int age = 20;
    printf("age = %d\n", age);
    return 0;
}
```

예시 컴파일:

```bash
cc main.c -o main
./main
```

## 이론 (Theory)

빌드는 전처리, 컴파일, 어셈블, 링크 단계를 거친다. 헤더 파일은 선언을 공유하고, 소스 파일은 정의를 담는다. 링커는 여러 object file과 library를 묶어 실행 파일을 만든다.

## 구현 (Implementation)

작은 `main.c`를 만들고 `gcc -Wall -Wextra -std=c17 main.c -o main`처럼 경고를 켠 상태로 컴파일한다. 헤더와 소스가 나뉘면 선언은 `.h`, 구현은 `.c`에 두고, 여러 파일은 Makefile이나 build system으로 의존성을 관리한다.

```c
#include <stdio.h>

static int square(int x) { return x * x; }  // 같은 파일 내 함수 분리

int main(void) {
    for (int i = 1; i <= 3; i++)
        printf("%d -> %d\n", i, square(i));
    return 0;
}
```

```bash
gcc -Wall -Wextra -std=c17 main.c -o main && ./main
```

## 복잡도 (Complexity)

컴파일 시간은 파일 수, include graph, 최적화 수준에 영향을 받는다. 실행 시간은 compile command가 아니라 생성된 코드와 알고리즘에 좌우되며, 최적화 플래그는 runtime 성능과 디버깅 편의성을 맞바꿀 수 있다.

## 응용 (Applications)

- 시스템 프로그래밍
- 임베디드와 드라이버
- 고성능 라이브러리
- 운영체제·컴파일러 학습

## 흔한 오해 (Common Misunderstandings)

- 컴파일이 성공해도 프로그램이 안전하다는 뜻은 아니다.
- `#include`는 파일 내용을 전처리 단계에서 가져오는 동작이다.
- C에는 문자열 타입이 따로 있는 것이 아니라 `char` 배열 관례를 쓴다.
- 경고를 무시하면 나중에 런타임 버그가 될 수 있다.

## TMI

- `-Wall -Wextra` 같은 경고 옵션을 켜는 습관이 좋다.
- C 표준과 컴파일러 확장은 구분해야 한다.
- Undefined behavior는 컴파일러가 어떤 결과도 낼 수 있게 만드는 위험한 영역이다.

## 연습 / 확인 문제 (Exercises)

- `printf`로 이름과 숫자를 출력하는 프로그램을 작성하라.
- 일부러 세미콜론을 빼고 컴파일 오류를 읽어 보라.
- `cc -Wall -Wextra`로 경고를 켜고 다시 빌드하라.

## 이어서 읽기 (Reading Path)

- 이전: [변수와 타입](../../Variables-and-Types.md)
- 다음: [C 타입과 제어 흐름](C-Types-and-Control-Flow.md)

## 참조 (References)

- [Programming/Variables-and-Types.md](../../Variables-and-Types.md)
- [Reference/Books.md](../../../Reference/Books.md)
