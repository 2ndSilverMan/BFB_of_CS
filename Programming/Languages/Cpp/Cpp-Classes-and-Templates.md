# C++ 클래스와 템플릿

- Level: Intermediate
- Prerequisites: [C++ 참조와 RAII](Cpp-References-and-RAII.md), [Programming/OOP.md](../../OOP.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

C++ 클래스는 데이터+동작을 묶는 타입, 템플릿은 **타입/값을 매개변수로 받아 컴파일 시점에 코드를 생성**하는 제네릭 도구다. 클래스가 **수명·소유권**(생성자/소멸자/복사/이동)을 제어하고, 템플릿이 **런타임 비용 없는 다형성**을 준다.

## 직관 (Intuition)

클래스는 타입을 직접 만드는 법, 템플릿은 "어떤 타입이 와도 같은 패턴으로 도는 코드 틀"이다. STL 전체가 템플릿 위에 서 있다. 핵심 통찰: **다형성에는 두 종류**가 있다 — 가상 함수(런타임 vtable)와 템플릿(컴파일 타임 인스턴스화).

## 핵심 문법 (Core Syntax)

```cpp
class Point {
public:
    Point(int x, int y) : x_(x), y_(y) {}      // 멤버 초기화 리스트
    int x() const { return x_; }                // const 멤버 함수
private:
    int x_, y_;
};

template <typename T>
T max_value(T a, T b) { return a < b ? b : a; } // 제네릭
```

## 이론 (Theory)

### 1. 특수 멤버 함수와 rule of 0/5

클래스는 **생성자·소멸자·복사 생성/대입·이동 생성/대입**으로 수명을 제어한다. 자원을 직접 들면 **rule of 5**(다섯을 모두 정의), 자원이 없으면 **rule of 0**(컴파일러에 위임). `explicit` 는 암묵 변환을 막는다.

### 2. 두 다형성

| | 런타임(가상 함수) | 컴파일 타임(템플릿) |
|---|---|---|
| 분기 | vtable 간접 호출 | 타입별 코드 생성 |
| 비용 | 작은 상수 + inline 방해 | 런타임 0, binary↑·컴파일↑ |
| 유연성 | 런타임 타입 결정 | 정적, 더 빠름 |

### 3. 템플릿의 대가

타입 검사를 받는 컴파일 타임 도구(매크로 아님)지만, **오류 메시지가 길고** 인스턴스화가 많으면 컴파일 시간·binary 크기가 커진다. C++20 **Concepts** 로 인자 요구사항을 명시해 오류를 개선한다.

## 구현 (Implementation)

```cpp
class Account {
public:
    explicit Account(int balance) : balance_(balance) {}   // explicit: 암묵 변환 차단
    void deposit(int amt) { if (amt > 0) balance_ += amt; } // 불변식: 음수 무시
    int balance() const { return balance_; }
private:
    int balance_;                                           // 불변식: >= 0 유지
};

template <typename T>
T clamp_min(T v, T lo) { return v < lo ? lo : v; }          // 작은 인스턴스화부터

// 런타임 다형성
struct Shape { virtual double area() const = 0; virtual ~Shape() = default; };
struct Circle : Shape { double r; double area() const override { return 3.14159*r*r; } };
```

## 복잡도 (Complexity)

| 항목 | 특성 |
|---|---|
| 가상 디스패치 | 상수 오버헤드 + inline 방해 |
| 템플릿 | 런타임 추상화 비용 0 |
| 인스턴스화 다수 | 컴파일 시간·binary 크기 ↑ |

## 응용 (Applications)

- 값 타입·도메인 모델, 타입 안전 제네릭 함수/컨테이너.
- STL 스타일 알고리즘, 성능 민감 추상화(정책 기반 설계).

## 흔한 오해 (Common Misunderstandings)

- **모든 다형성이 virtual일 필요 없다** — 정적 다형성(템플릿/CRTP)이 더 빠를 때가 많다.
- **템플릿은 매크로가 아니다** — 타입 검사를 받는 컴파일 타임 도구.
- **연산자 오버로딩은 의미를 흐리면 안 된다** — 직관적 의미만.
- **rule of 0** 을 따르면 특수 멤버를 직접 안 써도 되는 경우가 많다.

## TMI

- **CRTP**(Curiously Recurring Template Pattern)는 부모가 자식을 템플릿 인자로 받아 가상 함수 없이 정적 다형성을 구현한다.
- `constexpr`/`consteval` 함수는 컴파일 타임 계산으로 런타임 비용을 0으로 만든다.
- 가상 소멸자를 빠뜨리고 기반 클래스 포인터로 delete하면 파생 소멸자가 안 불려 leak/UB가 된다.

## 연습 / 확인 문제 (Exercises)

- `Point` 에 두 점 거리 메서드를 추가하라(`const` 멤버).
- 두 값 중 큰 값을 반환하는 템플릿을 작성하고 다른 타입으로 인스턴스화하라.
- 가상 함수와 CRTP로 같은 다형성을 구현해 비용을 비교하라.
- 자원을 가진 클래스에 rule of 5를, 안 가진 클래스에 rule of 0을 적용하라.

## 이어서 읽기 (Reading Path)

- 이전: [참조와 RAII](Cpp-References-and-RAII.md)
- 다음: [STL](Cpp-STL.md)
- 관련: [OOP](../../OOP.md)

## 참조 (References)

- [Programming/OOP.md](../../OOP.md)
- [Reference/Books.md](../../../Reference/Books.md)
