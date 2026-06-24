# C++ 참조와 RAII

- Level: Intermediate
- Prerequisites: [C++ 기본 문법](Cpp-Setup-and-Syntax.md), [Programming/Pointers-and-Memory.md](../../Pointers-and-Memory.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

참조(reference)는 기존 객체의 별칭이고, RAII(Resource Acquisition Is Initialization)는 자원 획득과 해제를 객체 수명에 묶는 C++의 핵심 패턴이다.

## 직관 (Intuition)

RAII는 "객체가 태어날 때 자원을 잡고, 죽을 때 자동으로 놓는다"는 원칙이다. 덕분에 예외가 발생해도 파일, 메모리, 락 같은 자원이 정리된다.

## 핵심 문법 (Core Syntax)

```cpp
#include <fstream>

void write_file(const std::string& path) {
    std::ofstream out(path);
    out << "hello\n";
} // out의 destructor가 파일을 닫음
```

참조는 복사를 피하면서 값을 읽거나 수정할 때 쓴다.

```cpp
void increment(int& x) {
    ++x;
}
```

## 이론 (Theory)

객체 수명은 생성자와 소멸자에 의해 관리된다. Stack 객체는 scope를 벗어날 때 소멸자가 호출된다. 이 성질이 C++ 예외 안전성과 자원 관리의 기반이다.

## 구현 (Implementation)

Resource를 획득하는 생성자와 해제하는 소멸자를 한 쌍으로 설계하고, 함수 인자는 소유권이 없으면 `const&`, 소유권 이동이면 value나 rvalue reference로 표현한다. Scope를 벗어날 때 해제가 실제로 일어나는지 로그나 테스트로 확인한다.

## 복잡도 (Complexity)

RAII 자체는 점근 복잡도를 바꾸지 않지만 cleanup 시점을 결정적으로 만든다. Reference 전달은 큰 객체 복사를 피하지만 lifetime 제약을 만들고, move는 보통 싸지만 type별로 비용이 다를 수 있다.

## 응용 (Applications)

- 파일·소켓·락 자동 정리
- 복사 비용 줄이기
- 예외 안전 코드
- 소유권 모델 설계

## 흔한 오해 (Common Misunderstandings)

- 참조는 null이 될 수 없는 별칭으로 사용하는 것이 일반적이다.
- 지역 객체의 참조를 반환하면 dangling reference가 된다.
- RAII는 메모리뿐 아니라 모든 자원에 적용된다.
- 소멸자에서 예외를 던지는 것은 매우 위험하다.

## TMI

- `const T&`는 큰 객체를 읽기 전용으로 넘길 때 자주 쓴다.
- Move semantics는 자원을 복사하지 않고 옮기는 현대 C++ 핵심이다.
- `std::lock_guard`는 mutex lock을 RAII로 관리한다.

## 연습 / 확인 문제 (Exercises)

- 참조로 값을 바꾸는 함수를 작성하라.
- 파일 객체가 scope를 벗어날 때 자동으로 닫히는 이유를 설명하라.
- Dangling reference 예시를 만들고 피하는 방법을 말하라.

## 이어서 읽기 (Reading Path)

- 이전: [C++ 기본 문법](Cpp-Setup-and-Syntax.md)
- 다음: [클래스와 템플릿](Cpp-Classes-and-Templates.md)

## 참조 (References)

- [Programming/Pointers-and-Memory.md](../../Pointers-and-Memory.md)
- [Reference/Books.md](../../../Reference/Books.md)
