# C 컴파일과 기본 문법

- Level: Beginner
- Prerequisites: [Programming/Variables-and-Types.md](../../Variables-and-Types.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

C는 소스를 **컴파일러가 기계어 실행 파일로 번역**하는 정적 타입 언어다. 실행은 `main` 에서 시작하고, 빌드는 **전처리 → 컴파일 → 어셈블 → 링크** 4단계를 거친다 — 이 파이프라인을 알아야 컴파일 오류와 링크 오류를 구분해 읽는다.

## 직관 (Intuition)

Python이 통역사를 옆에 두는 언어라면, C는 출발 전에 번역본(실행 파일)을 만들어 두는 방식. 그래서 "런타임에 알게 되는 것"이 적고, 대신 **컴파일·링크 단계의 오류 메시지를 읽는 능력**이 핵심 기술이다.

## 핵심 문법 (Core Syntax)

```c
#include <stdio.h>           // 전처리: stdio.h 내용을 끌어옴
int main(void) {
    int age = 20;
    printf("age = %d\n", age);
    return 0;                // 종료 코드 0 = 성공
}
```

```bash
cc -Wall -Wextra -std=c17 main.c -o main && ./main
```

## 이론 (Theory)

### 1. 빌드 4단계

| 단계 | 입력→출력 | 하는 일 |
|---|---|---|
| 전처리 | `.c`→`.i` | `#include` 펼치기, 매크로 치환, `#ifdef` |
| 컴파일 | `.i`→`.s` | C → 어셈블리(최적화 여기서) |
| 어셈블 | `.s`→`.o` | 어셈블리 → 기계어 object |
| 링크 | `.o`+lib→실행 | 심볼 해소, 라이브러리 결합 |

**컴파일 오류**(문법·타입)와 **링크 오류**(`undefined reference`, 선언은 보였으나 정의 없음)는 단계가 달라 원인도 다르다.

### 2. 헤더 vs 소스, UB

선언(무엇이 있는지)은 `.h`, 정의(실체)는 `.c`. **Undefined Behavior(UB)** 는 컴파일러가 "일어나지 않는다"고 가정해 *어떤 결과도* 낼 수 있는 위험 영역 — 경고(`-Wall -Wextra`)와 sanitizer로 줄인다.

## 구현 (Implementation)

```c
#include <stdio.h>
static int square(int x) { return x * x; }   // static: 이 파일 내부 연결

int main(void) {
    for (int i = 1; i <= 3; i++) printf("%d -> %d\n", i, square(i));
    return 0;
}
```

```bash
gcc -Wall -Wextra -std=c17 -fsanitize=address,undefined main.c -o main
```

## 복잡도 (Complexity)

| 항목 | 특성 |
|---|---|
| 컴파일 시간 | 파일 수·include 그래프·최적화 수준에 비례 |
| 실행 시간 | 컴파일 명령이 아니라 생성 코드·알고리즘이 결정 |
| `-O2`/`-O3` | 런타임 성능 ↔ 디버깅 편의·컴파일 시간 트레이드오프 |

## 응용 (Applications)

- 시스템 프로그래밍, 임베디드·드라이버, 고성능 라이브러리.
- 운영체제·컴파일러 학습의 기반 언어.

## 흔한 오해 (Common Misunderstandings)

- **컴파일 성공 ≠ 안전** — UB·메모리 버그는 런타임에 터진다.
- **`#include` 는 텍스트 삽입** — 전처리 단계의 복붙.
- **C에 문자열 타입은 없다** — `char` 배열 + null 종료 관례.
- **경고를 무시하면** 다수가 잠재 런타임 버그다 — `-Werror` 로 강제 가능.

## TMI

- `gcc -E`(전처리만), `-S`(어셈블리), `-c`(object까지)로 각 단계를 따로 볼 수 있다.
- C 표준(C99/C11/C17)과 컴파일러 확장(GNU)을 구분해야 이식성이 보장된다.
- `cc`/`gcc`/`clang` 은 대체로 같은 플래그를 받지만 진단 메시지·최적화가 다르다.

## 연습 / 확인 문제 (Exercises)

- `printf` 로 이름과 숫자를 출력하는 프로그램을 작성·빌드하라.
- 세미콜론을 빼서 **컴파일 오류**를, 함수 정의를 빼서 **링크 오류**를 각각 내고 메시지를 비교하라.
- `gcc -E` 로 `#include` 가 펼쳐진 결과를 확인하라.
- `-Wall -Wextra` 를 켜고 경고가 가리키는 잠재 버그를 고쳐라.

## 이어서 읽기 (Reading Path)

- 이전: [변수와 타입](../../Variables-and-Types.md)
- 다음: [C 타입과 제어 흐름](C-Types-and-Control-Flow.md)
- 관련: [C 파일과 빌드](C-Files-and-Builds.md)

## 참조 (References)

- [Programming/Variables-and-Types.md](../../Variables-and-Types.md)
- [Reference/Books.md](../../../Reference/Books.md)
