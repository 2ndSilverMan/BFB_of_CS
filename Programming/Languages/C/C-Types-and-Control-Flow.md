# C 타입과 제어 흐름

- Level: Beginner
- Prerequisites: [C 컴파일과 기본 문법](C-Setup-and-Compilation.md), [Programming/Control-Flow.md](../../Control-Flow.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

C의 타입(정수·부동소수점·문자·배열·포인터)은 **메모리 크기와 해석·연산 가능성**을 결정한다. 제어 흐름은 `if`/`switch`/`for`/`while`. C는 추상화가 얇아 **정수 승격·signed overflow UB·암묵 변환** 같은 함정이 그대로 드러난다.

## 직관 (Intuition)

C에서 타입은 단순 분류가 아니라 "이 비트들을 몇 바이트로, 부호 있게/없게 해석할지"의 지정이다. 같은 비트도 타입에 따라 다른 값이 된다 — 그래서 변환·비교 규칙을 모르면 조용한 버그가 난다.

## 핵심 문법 (Core Syntax)

```c
int count = 3;
double ratio = 0.5;
char grade = 'A';                 // 작은 정수 타입이기도
for (int i = 0; i < count; i++)
    if (i % 2 == 0) printf("%d\n", i);
```

## 이론 (Theory)

### 1. 정수: 부호·폭·승격

정수는 signed/unsigned와 폭(`char/short/int/long`)이 핵심. 작은 타입은 연산 전 **정수 승격(int로)** 된다. **signed overflow는 UB**(컴파일러가 "일어나지 않는다"고 가정해 최적화), **unsigned는 modulo 래핑**(정의됨). `unsigned` 와 `signed` 비교는 signed가 unsigned로 변환돼 음수가 거대값이 되는 함정.

### 2. 부동소수점은 근사

`0.1` 은 이진 부동소수점으로 정확히 표현 안 됨 → `0.1+0.2 != 0.3`. 동등 비교 대신 허용 오차(epsilon).

### 3. 조건과 fall-through

C는 **0=거짓, 비0=참**. `switch` 는 `break` 가 없으면 다음 case로 **fall-through**(의도적이면 주석으로 표시). `if (x = 5)` 는 대입(항상 참) — `==` 와 혼동 주의.

## 구현 (Implementation)

```c
#include <stdio.h>

char grade_of(int score) {
    if (score >= 90) return 'A';
    else if (score >= 80) return 'B';
    else return 'C';
}

int main(void) {
    unsigned u = 1; int s = -1;
    printf("%d\n", s < u);        // 0! s가 unsigned로 변환되어 거대값 > 1
    for (int i = 0; i < 3; i++) printf("%c ", grade_of((int[]){95,82,70}[i]));
}
```

## 복잡도 (Complexity)

| 항목 | 특성 |
|---|---|
| 조건 분기 | 보통 상수(분기 예측 영향) |
| 반복 | iteration 수 = 시간 복잡도 |
| 타입 폭 | 메모리·overflow 범위 결정 |
| signed overflow(UB) | 최적화 결과까지 바꿈 |

## 응용 (Applications)

- 입력 검증·반복 처리·상태 분기, 메모리 크기·형식 제어(임베디드·시스템).

## 흔한 오해 (Common Misunderstandings)

- **`=`(대입) vs `==`(비교)** — `if (x = 5)` 는 항상 참.
- **signed overflow는 UB** — "그냥 래핑"이 아니다(컴파일러가 제거할 수 있음).
- **signed/unsigned 비교 함정** — 음수가 거대 unsigned가 된다.
- **`switch` 의 `break` 누락** — fall-through.
- **부동소수점 동등 비교** — epsilon 필요.

## TMI

- `sizeof` 는 타입/객체 크기를 바이트로 주고 결과 타입은 `size_t`(unsigned) — 부호 비교 함정의 원천.
- `stdbool.h` 의 `bool/true/false`, `stdint.h` 의 `int32_t` 등 고정폭 정수가 이식성에 안전하다.
- printf format이 인자 타입과 안 맞으면(`%d` 에 `long`) 출력 깨짐·UB — `-Wformat` 경고.

## 연습 / 확인 문제 (Exercises)

- `sizeof(int/double/char)` 와 `size_t` 의 부호를 출력·확인하라.
- `s < u`(s 음수, u unsigned)가 왜 거짓인지 변환으로 설명하라.
- `switch` 에서 `break` 를 빼 fall-through를 관찰하라.
- `0.1+0.2 == 0.3` 이 거짓임을 확인하고 epsilon 비교로 고쳐라.

## 이어서 읽기 (Reading Path)

- 이전: [C 컴파일과 기본 문법](C-Setup-and-Compilation.md)
- 다음: [C 포인터와 메모리](C-Pointers-and-Memory.md)
- 관련: [데이터 표현](../../../Systems/Computer-Architecture/Data-Representation.md)

## 참조 (References)

- [Programming/Control-Flow.md](../../Control-Flow.md)
- [Reference/Books.md](../../../Reference/Books.md)
