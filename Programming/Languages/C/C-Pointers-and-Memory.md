# C 포인터와 메모리

- Level: Intermediate
- Prerequisites: [Programming/Pointers-and-Memory.md](../../Pointers-and-Memory.md), [C 타입과 제어 흐름](C-Types-and-Control-Flow.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

포인터는 메모리 주소를 저장하는 값이다. C에서는 주소 연산자 `&`, 역참조 연산자 `*`, 동적 할당 `malloc`/`free`를 통해 메모리를 직접 다룬다.

## 직관 (Intuition)

일반 변수는 상자 안의 값이고, 포인터는 상자가 놓인 주소를 적은 쪽지다. 쪽지를 따라가면 값을 읽거나 바꿀 수 있지만, 잘못된 주소를 따라가면 프로그램이 망가진다.

## 핵심 문법 (Core Syntax)

```c
int x = 10;
int *p = &x;
*p = 20;

printf("%d\n", x);  // 20
```

동적 할당:

```c
int *arr = malloc(sizeof(int) * 10);
if (arr == NULL) {
    return 1;
}
free(arr);
```

## 이론 (Theory)

스택 메모리는 함수 호출과 함께 자동으로 관리되고, 힙 메모리는 프로그래머가 할당과 해제를 책임진다. 이미 해제한 메모리를 다시 쓰면 use-after-free, 범위를 넘으면 buffer overflow가 된다.

## 구현 (Implementation)

포인터는 선언 직후 초기화하고, ownership을 주석이나 함수 이름으로 분명히 한다. `malloc` 결과 확인, `free` 위치, double free·use-after-free 여부를 sanitizer나 debugger로 함께 검증한다.

```c
#include <stdio.h>
#include <stdlib.h>

int main(void) {
    int n = 5;
    int *arr = malloc(n * sizeof *arr);  // 크기 계산
    if (arr == NULL) return 1;           // 결과 확인
    for (int i = 0; i < n; i++) arr[i] = i * i;
    printf("%d\n", arr[4]);             // 16
    free(arr);                           // 해제
    arr = NULL;                          // dangling 포인터 방지
}
```

## 복잡도 (Complexity)

포인터 역참조는 상수 시간처럼 보이지만 cache miss와 잘못된 locality가 큰 비용을 만든다. 동적 allocation은 allocator lock, fragmentation, metadata overhead가 있으며, leak은 장기 실행 프로그램에서 공간 비용을 계속 누적한다.

## 응용 (Applications)

- 배열과 문자열 처리
- 함수에서 값 수정
- 동적 자료구조 구현
- 시스템 API 호출

## 흔한 오해 (Common Misunderstandings)

- 포인터 자체도 값이며 타입이 있다.
- `free`는 포인터 변수를 NULL로 바꾸지 않는다.
- 지역 변수 주소를 함수 밖에서 사용하면 수명이 끝난 메모리를 참조할 수 있다.
- 배열과 포인터는 밀접하지만 완전히 같은 것은 아니다.

## TMI

- `valgrind`와 AddressSanitizer는 메모리 오류를 찾는 데 도움을 준다.
- `const int *p`와 `int *const p`는 의미가 다르다.
- 포인터 산술은 가리키는 타입 크기 단위로 움직인다.

## 연습 / 확인 문제 (Exercises)

- 포인터로 변수 값을 바꾸는 함수를 작성하라.
- `malloc`한 배열에 값을 넣고 합을 구한 뒤 `free`하라.
- use-after-free가 왜 위험한지 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [포인터와 메모리](../../Pointers-and-Memory.md)
- 다음: [C 배열, 문자열, 구조체](C-Arrays-Strings-Structs.md)

## 참조 (References)

- [Programming/Pointers-and-Memory.md](../../Pointers-and-Memory.md)
- [Engineering/Debugging/](../../../Engineering/Debugging/)
