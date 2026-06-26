# C 파일과 빌드

- Level: Intermediate
- Prerequisites: [C 배열, 문자열, 구조체](C-Arrays-Strings-Structs.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

C 프로그램은 여러 `.c` 소스 파일과 `.h` 헤더 파일로 나눠 구성할 수 있다. 파일 입출력은 `FILE*`와 표준 라이브러리 함수로 처리하고, 빌드는 컴파일과 링크를 조합한다.

## 직관 (Intuition)

작은 프로그램은 파일 하나로 충분하지만, 커지면 선언은 헤더에, 구현은 소스 파일에 나눠야 한다. 빌드는 그 조각들을 다시 실행 파일로 조립하는 과정이다.

## 핵심 문법 (Core Syntax)

```c
FILE *f = fopen("data.txt", "r");
if (f == NULL) {
    return 1;
}

char buffer[128];
while (fgets(buffer, sizeof buffer, f) != NULL) {
    printf("%s", buffer);
}
fclose(f);
```

여러 파일 빌드:

```bash
cc main.c util.c -o app
```

## 이론 (Theory)

헤더에는 함수 선언, 타입 정의, 매크로를 둔다. 같은 선언이 여러 번 포함되어도 안전하도록 include guard나 `#pragma once`를 사용한다. 링커 오류는 선언은 보였지만 실제 정의를 찾지 못할 때 자주 발생한다.

## 구현 (Implementation)

파일 I/O는 `fopen` 실패, partial read/write, `fclose` 오류를 확인하는 코드로 작성한다. 여러 translation unit을 빌드할 때는 header guard, object file, linker error를 구분해 보고 build dependency를 명시한다.

```c
#include <stdio.h>

int main(void) {
    FILE *f = fopen("data.txt", "r");
    if (f == NULL) {                 // 열기 실패 확인
        perror("fopen");
        return 1;
    }
    int lines = 0, c;
    while ((c = fgetc(f)) != EOF)
        if (c == '\n') lines++;
    if (fclose(f) != 0) perror("fclose");  // 닫기 오류도 확인
    printf("lines=%d\n", lines);
}
```

## 복잡도 (Complexity)

파일 처리 시간은 byte 수, buffering, syscall 횟수, storage latency에 좌우된다. Build 시간은 source file 수와 header dependency에 비례해 늘고, incremental build는 바뀐 dependency만 다시 컴파일할 때 효과가 크다.

## 응용 (Applications)

- 설정·데이터 파일 읽기
- 프로그램을 모듈로 분리
- 라이브러리 작성
- make 기반 빌드 자동화

## 흔한 오해 (Common Misunderstandings)

- 헤더에 일반 함수 정의를 넣으면 중복 정의 문제가 생길 수 있다.
- 파일 열기에 실패할 수 있으므로 `NULL` 확인이 필요하다.
- `fgets`는 개행 문자를 포함할 수 있다.
- 컴파일 오류와 링크 오류는 원인이 다르다.

## TMI

- Makefile은 파일 의존성과 빌드 명령을 선언한다.
- `stderr`는 오류 메시지 출력용 표준 스트림이다.
- Binary mode와 text mode는 플랫폼에 따라 차이를 만들 수 있다.

## 연습 / 확인 문제 (Exercises)

- 텍스트 파일의 줄 수를 세는 C 프로그램을 작성하라.
- `util.h`, `util.c`, `main.c`로 함수를 분리해 빌드하라.
- 일부러 함수 정의를 빼고 링크 오류를 읽어 보라.

## 이어서 읽기 (Reading Path)

- 이전: [C 배열, 문자열, 구조체](C-Arrays-Strings-Structs.md)
- 다음: [Systems/Operating-Systems](../../../Systems/Operating-Systems/), [C++ 트랙](../Cpp/)

## 참조 (References)

- [Systems/Operating-Systems/Linux/Linux-Shell-Basics.md](../../../Systems/Operating-Systems/Linux/Linux-Shell-Basics.md)
- [Reference/Books.md](../../../Reference/Books.md)
