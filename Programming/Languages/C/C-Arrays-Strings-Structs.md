# C 배열, 문자열, 구조체

- Level: Intermediate
- Prerequisites: [C 포인터와 메모리](C-Pointers-and-Memory.md), [Programming/Arrays-and-Strings.md](../../Arrays-and-Strings.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

C 배열은 같은 타입을 연속 메모리에 둔 것, 문자열은 **`'\0'`(null) 으로 끝나는 `char` 배열**, 구조체는 여러 필드를 묶은 사용자 타입이다. 세 가지 모두 **메모리 레이아웃이 그대로 노출**되어, 경계·종료 문자·정렬(padding)을 직접 의식해야 한다.

## 직관 (Intuition)

배열은 번호 붙은 칸의 줄, 문자열은 끝에 "여기서 끝" 표시가 붙은 문자 줄, 구조체는 서로 다른 칸을 가진 기록 카드. C는 길이를 자동 저장하지 않으므로 **버퍼 크기와 종료 문자**가 항상 프로그래머의 책임이다.

## 핵심 문법 (Core Syntax)

```c
int scores[3] = {90, 80, 70};
char name[] = "Ada";              // 실제 크기 4: 'A','d','a','\0'
struct Point { int x, y; };
struct Point p = {10, 20};
```

## 이론 (Theory)

### 1. 배열-포인터 decay

배열 이름은 대부분의 표현식에서 **첫 원소 포인터로 decay**한다. 그래서 함수에 배열을 넘기면 길이 정보가 사라진다 → **길이를 따로 전달**해야 한다. `sizeof(array)`(전체 바이트) ≠ 포인터의 `sizeof`(8).

### 2. 문자열과 버퍼 안전

`strlen` 은 `'\0'` 까지 읽어 $O(n)$. `strcpy`/`strcat` 은 길이 검사가 없어 **buffer overflow**의 단골 → `snprintf`, `strncpy`(종료 문자 보장 주의). null 종료를 빠뜨리면 함수가 버퍼 밖을 계속 읽는다.

### 3. 구조체 padding와 정렬

각 필드는 자기 크기로 정렬되어 **빈 padding** 이 생긴다. 그래서 `sizeof` 가 필드 합보다 클 수 있다. 배치 순서를 정렬 크기 내림차순으로 두면 padding이 줄어든다.

### 4. 복사 의미

구조체 대입(`b = a`)은 **필드 값을 얕게 복사**한다 — 포인터 필드는 같은 대상을 가리킨다(깊은 복사 아님).

## 구현 (Implementation)

```c
#include <stdio.h>
#include <string.h>

int sum(const int *a, int n) {            // 배열은 길이를 따로
    int s = 0; for (int i = 0; i < n; i++) s += a[i]; return s;
}

struct Mixed { char a; int b; char c; };  // padding 발생

int main(void) {
    int xs[] = {90, 80, 70};
    int n = sizeof xs / sizeof xs[0];      // 요소 개수 = 3
    printf("sum=%d len=%zu size=%zu\n", sum(xs, n), strlen("Ada"), sizeof(struct Mixed));
    // sum=240 len=3 size=12  (a@0, pad 1-3, b@4-7, c@8, pad 9-11; 정렬 4)
}
```

## 복잡도 (Complexity)

| 연산 | 비용 |
|---|---|
| 배열 인덱스 | $O(1)$ |
| `strlen` | $O(n)$ (null 탐색) |
| 큰 구조체 값 전달 | 크기에 비례 복사 → 포인터 전달 고려 |
| 구조체 배열 순회 | cache locality에 유리(연속) |

## 응용 (Applications)

- 고정 크기 데이터·레코드·메시지 표현, C API 문자열 처리.
- 연결 리스트·트리 노드(구조체 + 포인터 필드).

## 흔한 오해 (Common Misunderstandings)

- **C 배열은 경계 검사를 안 한다** — overflow는 조용히 UB.
- **문자열은 null 종료 공간이 필요** — `char buf[3]` 에 `"abc"` 는 못 담는다.
- **`sizeof(array)` ≠ `sizeof(pointer)`** — decay 후엔 포인터 크기.
- **구조체 대입은 얕은 복사** — 포인터 필드 공유.

## TMI

- `struct`를 `typedef` 로 별칭화하는 스타일이 흔하다(`typedef struct {...} Point;`).
- `memcpy` 는 타입 의미를 무시한 raw 복사 — 겹치는 영역은 `memmove`.
- **Flexible array member**(`int data[];` 구조체 끝)는 헤더 + 가변 데이터를 한 번에 할당하는 관용구다.

## 연습 / 확인 문제 (Exercises)

- 정수 배열의 최댓값을 찾는 함수를 길이를 받아 작성하라.
- `strlen` 을 직접 구현하라.
- `struct Mixed` 의 `sizeof` 를 예측하고 필드 순서를 바꿔 padding을 줄여라.
- 배열을 함수에 넘긴 뒤 `sizeof` 가 왜 8이 되는지 설명하라(decay).

## 이어서 읽기 (Reading Path)

- 이전: [C 포인터와 메모리](C-Pointers-and-Memory.md)
- 다음: [C 파일과 빌드](C-Files-and-Builds.md)
- 관련: [배열](../../../Data-Structures/Array.md)

## 참조 (References)

- [Programming/Arrays-and-Strings.md](../../Arrays-and-Strings.md)
- [Data-Structures/Array.md](../../../Data-Structures/Array.md)
