# C 파일과 빌드

- Level: Intermediate
- Prerequisites: [C 배열, 문자열, 구조체](C-Arrays-Strings-Structs.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

C 프로그램은 여러 `.c`(정의)와 `.h`(선언)로 나눈다. 파일 I/O는 `FILE*` 와 표준 라이브러리(`fopen`/`fgets`/`fclose`), 빌드는 **각 `.c` 를 독립 translation unit으로 컴파일 후 링크**한다.

## 직관 (Intuition)

작은 프로그램은 파일 하나로 충분하지만, 커지면 선언은 헤더에·구현은 소스에 나눈다. 빌드는 그 조각(object 파일)을 다시 실행 파일로 조립하는 과정 — **incremental build**(바뀐 것만 재컴파일)가 큰 프로젝트의 속도를 좌우한다.

## 핵심 문법 (Core Syntax)

```c
FILE *f = fopen("data.txt", "r");
if (!f) { perror("fopen"); return 1; }       // 실패 확인 필수
char buf[128];
while (fgets(buf, sizeof buf, f)) fputs(buf, stdout);
fclose(f);
```

## 이론 (Theory)

### 1. 분리 컴파일과 include guard

각 `.c` 는 헤더를 포함해 독립 컴파일된다. 같은 헤더가 여러 번 포함돼도 안전하도록 **include guard**(`#ifndef X_H ... #endif`) 또는 `#pragma once`. 헤더에 **함수 정의**(선언이 아닌)를 넣으면 여러 TU에 정의가 중복돼 링크 오류(`multiple definition`).

### 2. 링크 오류의 두 얼굴

- `undefined reference` — 선언은 봤으나 정의를 못 찾음(파일 빌드 누락, 라이브러리 미연결).
- `multiple definition` — 같은 심볼이 둘 이상(헤더에 정의, `static`/`inline` 누락).

### 3. 파일 I/O 견고성

`fopen` 실패(`NULL`), **partial read/write**, `fclose` 실패까지 확인해야 한다. `fgets` 는 **개행 문자를 포함**할 수 있고, 텍스트/바이너리 모드는 플랫폼별로 줄바꿈 변환이 다르다.

## 구현 (Implementation)

```c
#include <stdio.h>
int main(void) {
    FILE *f = fopen("data.txt", "r");
    if (!f) { perror("fopen"); return 1; }       // 열기 실패
    int lines = 0, c;
    while ((c = fgetc(f)) != EOF) if (c == '\n') lines++;
    if (fclose(f) != 0) perror("fclose");         // 닫기 오류도 확인
    printf("lines=%d\n", lines);
}
```

```makefile
app: main.o util.o          # 바뀐 .o만 재컴파일(incremental)
	cc main.o util.o -o app
%.o: %.c util.h
	cc -Wall -Wextra -c $< -o $@
```

## 복잡도 (Complexity)

| 항목 | 특성 |
|---|---|
| 파일 처리 | 바이트 수·버퍼링·**syscall 횟수**·스토리지 지연 |
| 전체 빌드 | 소스 수 × 헤더 의존성에 비례 |
| incremental build | 바뀐 의존성만 재컴파일 → 큰 이득 |

## 응용 (Applications)

- 설정·데이터 파일 읽기, 프로그램을 모듈로 분리.
- 라이브러리 작성(`.a`/`.so`), make/CMake 기반 빌드 자동화.

## 흔한 오해 (Common Misunderstandings)

- **헤더에 함수 정의를 넣으면 중복 정의** — 선언만(또는 `static inline`).
- **`fopen` 은 실패할 수 있다** — `NULL` 확인.
- **`fgets` 는 개행을 포함** — 필요 시 제거.
- **컴파일 오류 ≠ 링크 오류** — 단계가 다르다.

## TMI

- Makefile은 "타깃: 의존성 / 명령" 규칙으로 의존성 그래프를 선언하고, 변경된 것만 다시 빌드한다.
- `stderr` 는 오류용 표준 스트림이라 `2>` 로 따로 리디렉션된다(로그와 분리).
- `static` 함수는 파일 내부 연결(다른 TU에서 안 보임)이라 링크 충돌·심볼 오염을 줄인다.

## 연습 / 확인 문제 (Exercises)

- 텍스트 파일의 줄 수를 세는 프로그램을 작성하라(실패 처리 포함).
- `util.h`/`util.c`/`main.c` 로 분리해 빌드하고 include guard를 넣어라.
- 함수 정의를 빼서 `undefined reference` 를, 헤더에 정의를 넣어 `multiple definition` 을 각각 재현하라.
- Makefile로 한 파일만 고쳤을 때 그 파일만 재컴파일됨을 확인하라.

## 이어서 읽기 (Reading Path)

- 이전: [C 배열, 문자열, 구조체](C-Arrays-Strings-Structs.md)
- 다음: [C++ 설정과 문법](../Cpp/Cpp-Setup-and-Syntax.md)
- 관련: [Linux 셸 기초](../../../Systems/Operating-Systems/Linux/Linux-Shell-Basics.md)

## 참조 (References)

- [Systems/Operating-Systems/Linux/Linux-Shell-Basics.md](../../../Systems/Operating-Systems/Linux/Linux-Shell-Basics.md)
- [Reference/Books.md](../../../Reference/Books.md)
