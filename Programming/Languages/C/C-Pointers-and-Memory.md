# C 포인터와 메모리

- Level: Intermediate
- Prerequisites: [Programming/Pointers-and-Memory.md](../../Pointers-and-Memory.md), [C 타입과 제어 흐름](C-Types-and-Control-Flow.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

포인터는 **메모리 주소를 담는 타입 있는 값**이다. C는 `&`(주소), `*`(역참조), `malloc`/`free`(동적 할당)로 메모리를 직접 다룬다 — 강력하지만 모든 메모리 안전 책임이 프로그래머에게 있다.

## 직관 (Intuition)

일반 변수는 상자 속 값, 포인터는 상자가 놓인 주소를 적은 쪽지다. 쪽지를 따라가 값을 읽고 바꾸지만, **잘못된 주소를 따라가면 프로그램이 무너진다**(또는 더 나쁘게, 조용히 손상된다). C의 거의 모든 보안 취약점이 여기서 나온다.

## 핵심 문법 (Core Syntax)

```c
int x = 10;
int *p = &x;        // p는 x의 주소
*p = 20;            // 역참조로 x를 변경 → x == 20

int *arr = malloc(sizeof(int) * 10);   // 힙 할당
if (arr == NULL) return 1;             // 실패 확인 필수
free(arr); arr = NULL;                 // 해제 후 NULL(dangling 방지)
```

## 이론 (Theory)

### 1. 스택 vs 힙

| | 스택 | 힙 |
|---|---|---|
| 관리 | 자동(함수 진입/반환) | 수동(`malloc`/`free`) |
| 수명 | 함수 범위 | 명시적 해제까지 |
| 위험 | 지역 변수 주소 반환 | leak, use-after-free, double free |

**지역 변수 주소를 함수 밖으로 반환하면** 수명이 끝난 스택을 가리켜 UB.

### 2. 포인터 산술은 타입 크기로 스케일

`p + 1` 은 `p` 가 가리키는 타입 **`sizeof(*p)` 바이트**만큼 이동한다. `int*` 면 +4, `char*` 면 +1. `arr[i]` 는 `*(arr + i)` 의 문법설탕.

### 3. const의 위치

- `const int *p` — *가리키는 값*이 const(p는 다른 곳을 가리킬 수 있음).
- `int *const p` — *포인터*가 const(값은 바꿀 수 있음).

### 4. 메모리 버그 분류

use-after-free, double free, buffer overflow(범위 초과), leak(해제 누락), dangling(해제된 곳 참조), NULL 역참조 — `valgrind`·AddressSanitizer(`-fsanitize=address`)로 검출.

## 구현 (Implementation)

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n = 5;
    int *arr = malloc(n * sizeof *arr);    // sizeof *arr: 타입 바뀌어도 안전
    if (!arr) return 1;                     // 할당 실패 확인
    for (int i = 0; i < n; i++) arr[i] = i * i;
    int *q = arr + 2;                       // 포인터 산술: arr[2]를 가리킴
    printf("%d %d\n", arr[4], *q);          // 16 4
    free(arr); arr = NULL;                  // 해제 + dangling 방지
}
```

## 복잡도 (Complexity)

| 항목 | 비용 |
|---|---|
| 역참조 | 상수처럼 보이나 **cache miss** 가 실제 비용 |
| `malloc`/`free` | allocator lock·단편화·메타데이터 오버헤드 |
| leak | 장기 실행에서 공간을 계속 누적 |

## 응용 (Applications)

- 배열·문자열 처리, 함수에서 값 수정(출력 매개변수).
- 동적 자료구조(연결 리스트·트리), 시스템 API(버퍼·핸들).

## 흔한 오해 (Common Misunderstandings)

- **포인터도 타입 있는 값** — `int*` 와 `char*` 는 산술 단위가 다르다.
- **`free` 는 포인터를 NULL로 안 만든다** — 직접 `= NULL`.
- **지역 변수 주소 반환은 UB** — 수명 끝난 스택.
- **배열과 포인터는 밀접하나 같지 않다**(`sizeof` 가 다름 — 아래 배열 문서).

## TMI

- `-fsanitize=address,undefined` 는 use-after-free·overflow·UB를 런타임에 잡아 주는 현대 디버깅의 필수 도구다.
- `calloc` 은 0으로 초기화 + 곱셈 오버플로 검사, `realloc` 은 크기 변경(실패 시 원본 유지에 주의).
- `void*` 는 어떤 객체 포인터와도 변환되는 제네릭 포인터지만, 함수 포인터와는 표준상 변환이 보장되지 않는다.

## 연습 / 확인 문제 (Exercises)

- 포인터로 두 변수를 swap하는 함수를 작성하라.
- `malloc` 한 배열에 값을 넣고 합을 구한 뒤 `free` 하라(누수 없이).
- `const int *` 와 `int *const` 각각에 대해 금지되는 대입을 보여라.
- use-after-free 코드를 AddressSanitizer로 잡아라.

## 이어서 읽기 (Reading Path)

- 이전: [포인터와 메모리](../../Pointers-and-Memory.md)
- 다음: [C 배열, 문자열, 구조체](C-Arrays-Strings-Structs.md)
- 관련: [Valgrind / AddressSanitizer](../../../Engineering/Debugging/Valgrind-AddressSanitizer.md)

## 참조 (References)

- [Programming/Pointers-and-Memory.md](../../Pointers-and-Memory.md)
- [Engineering/Debugging/Valgrind-AddressSanitizer.md](../../../Engineering/Debugging/Valgrind-AddressSanitizer.md)
