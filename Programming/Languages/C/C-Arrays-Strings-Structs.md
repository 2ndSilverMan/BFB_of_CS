# C 배열, 문자열, 구조체

- Level: Intermediate
- Prerequisites: [C 포인터와 메모리](C-Pointers-and-Memory.md), [Programming/Arrays-and-Strings.md](../../Arrays-and-Strings.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

C 배열은 같은 타입 값을 연속 메모리에 저장하고, C 문자열은 null 문자 `'\0'`로 끝나는 `char` 배열이다. 구조체는 여러 필드를 하나의 사용자 정의 타입으로 묶는다.

## 직관 (Intuition)

배열은 번호가 붙은 칸들의 줄이고, 문자열은 마지막에 "여기서 끝" 표시가 붙은 문자 줄이다. 구조체는 서로 다른 종류의 칸을 가진 작은 기록 카드다.

## 핵심 문법 (Core Syntax)

```c
int scores[3] = {90, 80, 70};
char name[] = "Ada";

struct Point {
    int x;
    int y;
};

struct Point p = {10, 20};
printf("%d %s\n", scores[0], name);
```

## 이론 (Theory)

배열 이름은 많은 표현식에서 첫 원소 포인터로 decay된다. 문자열 함수는 null terminator를 찾을 때까지 읽으므로 버퍼 크기와 종료 문자를 항상 의식해야 한다. 구조체는 padding 때문에 필드 크기 합보다 클 수 있다.

## 구현 (Implementation)

배열은 길이를 별도로 전달하고, 문자열은 null terminator 공간까지 확보하며, 구조체는 값 복사와 포인터 전달의 차이를 의식해 작성한다. `sizeof`, bounds check, 초기화 여부를 작은 예제로 확인한다.

```c
#include <stdio.h>
#include <string.h>

int sum(const int *a, int n) {        // 길이를 따로 전달
    int s = 0;
    for (int i = 0; i < n; i++) s += a[i];
    return s;
}

int main(void) {
    int xs[] = {90, 80, 70};
    int n = sizeof xs / sizeof xs[0];  // 요소 개수 계산
    char name[] = "Ada";
    printf("sum=%d len=%zu\n", sum(xs, n), strlen(name));  // sum=240 len=3
}
```

## 복잡도 (Complexity)

배열 index 접근은 `O(1)`이지만 문자열 길이 계산은 null terminator를 찾는 `O(n)` 작업이다. 큰 구조체를 값으로 넘기면 크기에 비례한 복사 비용이 생기며, 구조체 배열은 cache locality에 영향을 준다.

## 응용 (Applications)

- 고정 크기 데이터 처리
- C API와 문자열 처리
- 좌표, 레코드, 메시지 구조 표현
- 연결 리스트 같은 자료구조 구현

## 흔한 오해 (Common Misunderstandings)

- C 배열은 길이를 자동으로 검사하지 않는다.
- 문자열 버퍼에 null terminator 공간이 필요하다.
- `sizeof(array)`와 포인터에 대한 `sizeof(pointer)`는 다르다.
- 구조체 대입은 필드 값을 복사하지만 포인터 필드가 가리키는 데이터까지 깊은 복사하지는 않는다.

## TMI

- `struct`를 `typedef`로 별칭화하는 스타일도 흔하다.
- `memcpy`는 raw memory 복사라 타입의 의미를 보장하지 않는다.
- Flexible array member는 구조체 끝에 가변 길이 데이터를 붙일 때 쓰인다.

## 연습 / 확인 문제 (Exercises)

- 정수 배열의 최댓값을 찾는 함수를 작성하라.
- 문자열 길이를 직접 세는 함수를 작성하라.
- `struct Student`를 만들고 배열로 여러 학생을 저장하라.

## 이어서 읽기 (Reading Path)

- 이전: [C 포인터와 메모리](C-Pointers-and-Memory.md)
- 다음: [C 파일과 빌드](C-Files-and-Builds.md)

## 참조 (References)

- [Programming/Arrays-and-Strings.md](../../Arrays-and-Strings.md)
- [Data-Structures/Array.md](../../../Data-Structures/Array.md)
