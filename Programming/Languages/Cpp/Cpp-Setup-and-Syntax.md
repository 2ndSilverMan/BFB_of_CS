# C++ 실행 환경과 기본 문법

- Level: Intermediate
- Prerequisites: [Programming/Languages/C/](../C/), [Programming/Variables-and-Types.md](../../Variables-and-Types.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

C++은 C 계열 문법 위에 객체지향, 제네릭, RAII, 표준 라이브러리 추상화를 더한 정적 타입 컴파일 언어다. 성능과 추상화를 함께 다루는 데 강하다.

## 직관 (Intuition)

C++은 C처럼 하드웨어 가까이 갈 수 있지만, `std::vector`, `std::string`, 클래스, 템플릿으로 더 안전하고 높은 수준의 코드를 쓸 수 있다. 다만 가능한 선택지가 많아 스타일 규칙이 중요하다.

## 핵심 문법 (Core Syntax)

```cpp
#include <iostream>
#include <string>

int main() {
    std::string name = "Ada";
    int age = 20;
    std::cout << name << ": " << age << "\n";
}
```

컴파일 예:

```bash
c++ -std=c++20 main.cpp -o main
```

## 이론 (Theory)

C++ 표준은 계속 발전한다. 현대 C++에서는 raw array와 raw pointer보다 `std::vector`, `std::string`, smart pointer 같은 표준 타입을 우선 사용한다.

## 구현 (Implementation)

`-std=c++20`, 경고 옵션, sanitizer를 켠 작은 프로그램으로 문법을 확인한다. `namespace`, `auto`, range-for, reference, RAII 같은 C++ 기본 관용구를 C 스타일 코드와 비교하며 익힌다.

## 복잡도 (Complexity)

실행 시간은 선택한 알고리즘과 객체 복사·이동 비용에 좌우된다. 컴파일 시간은 template, include, optimization 수준에 민감하며, header-only 설계는 사용 편의성과 빌드 비용을 맞바꿀 수 있다.

## 응용 (Applications)

- 고성능 서버와 게임 엔진
- 시스템·임베디드 프로그래밍
- 그래픽스와 실시간 처리
- 성능 민감 라이브러리

## 흔한 오해 (Common Misunderstandings)

- C++은 "클래스가 있는 C"보다 훨씬 넓은 언어다.
- 현대 C++에서 `new`/`delete`를 직접 쓰는 일은 줄이는 편이 좋다.
- Namespace는 이름 충돌을 줄이기 위한 도구다.
- 컴파일이 느린 언어라 빌드 구조가 중요하다.

## TMI

- `std::cout`은 iostream 기반 출력 객체다.
- C++ 표준 버전은 C++11, C++14, C++17, C++20처럼 부른다.
- `auto`는 타입 추론을 해 주지만 의미를 흐리게 쓰면 읽기 어려워진다.

## 연습 / 확인 문제 (Exercises)

- `std::string`과 `std::cout`을 사용해 자기소개를 출력하라.
- C 배열 대신 `std::vector<int>`를 만들어 값을 넣어라.
- `-std=c++20` 옵션의 의미를 찾아 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [C 트랙](../C/)
- 다음: [참조와 RAII](Cpp-References-and-RAII.md)

## 참조 (References)

- [Programming/Languages/C/](../C/)
- [Reference/Books.md](../../../Reference/Books.md)
