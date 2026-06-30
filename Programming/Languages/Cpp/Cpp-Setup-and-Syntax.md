# C++ 실행 환경과 기본 문법

- Level: Intermediate
- Prerequisites: [Programming/Languages/C/](../C/), [Programming/Variables-and-Types.md](../../Variables-and-Types.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

C++은 C 문법 위에 **객체지향 · 제네릭(템플릿) · RAII · 표준 라이브러리**를 더한 정적 타입 컴파일 언어다. 핵심 철학은 **"제로 오버헤드 추상화"** — 안 쓰는 기능엔 비용이 없고, 쓰는 추상화도 손으로 짠 코드만큼 빠르다.

## 직관 (Intuition)

C처럼 하드웨어 가까이 가면서도 `std::vector`·`std::string`·클래스·템플릿으로 더 안전·고수준 코드를 쓴다. 대가는 **선택지의 폭** — 같은 일을 여러 방식으로 할 수 있어 스타일 규칙(현대 C++ 가이드라인)이 중요하다.

## 핵심 문법 (Core Syntax)

```cpp
#include <iostream>
#include <vector>
int main() {
    std::vector<int> xs = {1, 2, 3};
    int total = 0;
    for (auto& x : xs) total += x;              // auto + range-for + 참조
    std::cout << total / static_cast<double>(xs.size()) << "\n";  // 2
}
```

```bash
c++ -std=c++20 -Wall -Wextra -fsanitize=address main.cpp -o main
```

## 이론 (Theory)

### 1. 현대 C++의 기본값

raw 배열·`new`/`delete` 대신 `std::vector`·`std::string`·스마트 포인터를 우선한다(메모리 안전·예외 안전). `auto` 타입 추론, range-for, 참조, [RAII](Cpp-References-and-RAII.md)가 기본 관용구.

### 2. 컴파일 모델과 ODR

C와 같은 분리 컴파일이지만 **템플릿은 헤더에** 두는 경우가 많다(인스턴스화가 사용처에서 일어남). **ODR(One Definition Rule)**: 같은 엔터티는 정의가 하나여야 — `inline`/템플릿이 예외. 표준 버전(C++11/14/17/20/23)이 언어를 크게 바꾼다.

### 3. 정적 vs 동적 다형성

가상 함수(런타임)와 템플릿(컴파일 타임) 두 다형성이 공존 — 비용·유연성 트레이드오프(아래 클래스·템플릿 문서).

## 구현 (Implementation)

```cpp
#include <iostream>
#include <string>
#include <vector>
int main() {
    std::string name = "Ada";                   // RAII 문자열(자동 해제)
    std::vector<int> v;
    v.reserve(3);                               // 재할당 최소화
    for (int i = 1; i <= 3; i++) v.push_back(i);
    for (auto x : v) std::cout << x << " ";
    std::cout << "| " << name << "\n";
}
```

## 복잡도 (Complexity)

| 항목 | 특성 |
|---|---|
| 실행 시간 | 알고리즘 + **객체 복사/이동** 비용 |
| 컴파일 시간 | 템플릿·include·최적화에 민감(헤더-only는 빌드↑) |
| binary 크기 | 템플릿 인스턴스화 수에 비례 |

## 응용 (Applications)

- 고성능 서버·게임 엔진, 시스템·임베디드, 그래픽스·실시간.
- 성능 민감 라이브러리(추상화 + 속도 동시).

## 흔한 오해 (Common Misunderstandings)

- **C++ ≠ "클래스가 있는 C"** — 훨씬 넓은 멀티패러다임 언어.
- **현대 C++에서 `new`/`delete` 직접 사용은 줄인다** — 컨테이너·스마트 포인터.
- **`auto` 남용은 의미를 흐린다** — 명확성과 균형.
- **컴파일이 느리다** — 빌드 구조(전방 선언·PCH·모듈)가 중요.

## TMI

- C++20 **모듈**은 헤더의 전처리 복붙 모델을 대체해 빌드 시간을 줄이려는 시도다.
- `static_cast`/`dynamic_cast`/`reinterpret_cast`/`const_cast` 로 변환 의도를 명시한다(C 스타일 캐스트 지양).
- `std::cout` 은 iostream 객체라 `"\n"` 이 `std::endl`(flush 동반)보다 보통 빠르다.

## 연습 / 확인 문제 (Exercises)

- `std::string`/`std::vector` 로 간단한 자기소개를 출력하라.
- C 배열 코드를 `std::vector` 로 바꾸고 경계 검사를 비교하라.
- `-std=c++20` 과 sanitizer를 켜고 빌드하라.
- 가상 함수와 템플릿 다형성을 각각 한 줄로 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [C 트랙](../C/)
- 다음: [참조와 RAII](Cpp-References-and-RAII.md)
- 관련: [클래스와 템플릿](Cpp-Classes-and-Templates.md)

## 참조 (References)

- [Programming/Languages/C/](../C/)
- [Reference/Books.md](../../../Reference/Books.md)
