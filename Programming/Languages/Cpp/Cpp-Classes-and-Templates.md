# C++ 클래스와 템플릿

- Level: Intermediate
- Prerequisites: [C++ 참조와 RAII](Cpp-References-and-RAII.md), [Programming/OOP.md](../../OOP.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

C++ 클래스는 데이터와 동작을 묶는 타입이고, 템플릿은 타입이나 값을 매개변수로 받아 컴파일 시점에 코드를 생성하는 제네릭 프로그래밍 도구다.

## 직관 (Intuition)

클래스는 타입을 직접 만드는 방법이고, 템플릿은 "어떤 타입이 들어와도 같은 패턴으로 동작하는 코드 틀"이다. STL 컨테이너와 알고리즘은 템플릿 위에 세워져 있다.

## 핵심 문법 (Core Syntax)

```cpp
class Point {
public:
    Point(int x, int y) : x_(x), y_(y) {}
    int x() const { return x_; }
private:
    int x_;
    int y_;
};

template <typename T>
T max_value(T a, T b) {
    return a < b ? b : a;
}
```

## 이론 (Theory)

클래스는 생성자, 소멸자, 복사/이동 연산을 통해 수명과 소유권을 제어한다. 템플릿은 컴파일 시점 다형성을 제공해 런타임 비용 없이 제네릭 코드를 만들 수 있지만, 오류 메시지가 길고 컴파일 시간이 늘 수 있다.

## 구현 (Implementation)

클래스는 불변식과 public interface를 먼저 정하고, 생성자·소멸자·복사/이동 동작을 의도적으로 설계한다. 템플릿은 header에 정의를 두는 경우가 많고, error message가 길어질 수 있어 작은 instantiation부터 확인한다.

```cpp
#include <iostream>

class Account {
public:
    explicit Account(int balance) : balance_(balance) {}
    void deposit(int amount) { if (amount > 0) balance_ += amount; }
    int balance() const { return balance_; }
private:
    int balance_;   // 불변식: 생성자에서 초기 잔액을 세움
};

template <typename T>
T clamp_min(T v, T lo) { return v < lo ? lo : v; }  // 작은 instantiation

int main() {
    Account a(100);
    a.deposit(50);
    std::cout << a.balance() << " " << clamp_min(-3, 0) << "\n";  // 150 0
}
```

## 복잡도 (Complexity)

Virtual dispatch는 보통 상수 시간 overhead지만 inlining을 막을 수 있다. Template은 runtime 추상화 비용을 줄일 수 있지만 instantiation 수가 많으면 compile time과 binary size가 커진다.

## 응용 (Applications)

- 값 타입과 도메인 모델 작성
- 타입 안전한 제네릭 함수
- STL 스타일 컨테이너·알고리즘 사용
- 성능 민감 추상화

## 흔한 오해 (Common Misunderstandings)

- 모든 다형성이 virtual 함수 기반일 필요는 없다.
- 템플릿은 단순 매크로가 아니라 타입 검사를 받는 컴파일 타임 도구다.
- 연산자 오버로딩은 편리하지만 의미를 흐리면 안 된다.
- Rule of Zero를 따르면 직접 소멸자/복사/이동을 작성하지 않아도 되는 경우가 많다.

## TMI

- Concepts는 템플릿 인자 요구사항을 명시하는 C++20 기능이다.
- CRTP는 컴파일 타임 다형성 패턴 중 하나다.
- `constexpr`는 컴파일 타임 계산과 연결된다.

## 연습 / 확인 문제 (Exercises)

- `Point` 클래스에 거리 계산 메서드를 추가하라.
- 두 값 중 큰 값을 반환하는 템플릿 함수를 작성하라.
- 런타임 다형성과 컴파일 타임 다형성을 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [참조와 RAII](Cpp-References-and-RAII.md)
- 다음: [STL](Cpp-STL.md)

## 참조 (References)

- [Programming/OOP.md](../../OOP.md)
- [Reference/Books.md](../../../Reference/Books.md)
