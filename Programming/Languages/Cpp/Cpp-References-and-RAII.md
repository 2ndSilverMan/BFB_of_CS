# C++ 참조와 RAII

- Level: Intermediate
- Prerequisites: [C++ 기본 문법](Cpp-Setup-and-Syntax.md), [Programming/Pointers-and-Memory.md](../../Pointers-and-Memory.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

참조는 기존 객체의 **별칭**(null 불가, 재바인딩 불가), RAII(Resource Acquisition Is Initialization)는 **자원 획득·해제를 객체 수명에 묶는** C++의 핵심 패턴이다. RAII가 C++ 예외 안전성과 결정적 자원 관리의 토대다.

## 직관 (Intuition)

RAII = "객체가 태어날 때 자원을 잡고, 죽을 때 자동으로 놓는다". 덕분에 **예외가 던져져도** 스택이 풀리며(unwinding) 소멸자가 호출돼 파일·메모리·락이 정리된다 — `finally` 가 필요 없는 이유.

## 핵심 문법 (Core Syntax)

```cpp
void increment(int& x) { ++x; }            // 참조: 복사 없이 수정
void read(const std::string& s);           // const&: 복사 없이 읽기

void write(const std::string& path) {
    std::ofstream out(path);
    out << "hello\n";
}                                           // out의 소멸자가 파일을 닫음
```

## 이론 (Theory)

### 1. 수명과 스택 unwinding

스택 객체는 scope를 벗어날 때 **선언의 역순으로** 소멸자가 호출된다. 예외가 전파될 때도 이 unwinding이 일어나 자원이 누수 없이 정리된다 — RAII 객체가 cleanup을 보장한다.

### 2. 인자 전달 규칙

| 의도 | 전달 방식 |
|---|---|
| 읽기만(큰 객체) | `const T&` |
| 수정 | `T&` |
| 소유권 이전 | `T` (by value) 또는 `T&&` |
| 작은 값 | `T` (복사가 더 쌈) |

### 3. rvalue 참조와 이동

`T&&` (rvalue 참조)는 "곧 사라질 임시"를 가리켜 **이동(move)** 을 가능케 한다 — 자원을 복사 대신 옮긴다. 자원을 가진 클래스는 **rule of 5**(소멸자/복사 생성·대입/이동 생성·대입)를, 자원이 없으면 **rule of 0**(전부 컴파일러에 위임)를 따른다.

## 구현 (Implementation)

```cpp
#include <iostream>
class Timer {
public:
    Timer()  { std::cout << "start\n"; }   // 획득
    ~Timer() { std::cout << "stop\n";  }   // 해제(scope 종료·예외 시 자동)
};

void run(const std::string& label) {       // const&: 복사 없이 읽기
    Timer t;                                // RAII
    std::cout << "work: " << label << "\n";
}                                           // 여기서 ~Timer() → stop
// 출력: start / work: ... / stop  (예외가 나도 stop은 보장)

std::lock_guard<std::mutex> guard(mtx);     // 락도 RAII로 자동 해제
```

## 복잡도 (Complexity)

| 항목 | 특성 |
|---|---|
| RAII | 점근은 그대로, **cleanup 시점을 결정적**으로 |
| `const&` 전달 | 큰 객체 복사 회피(단, 수명 제약) |
| move | 보통 싸지만 타입별로 다름(포인터 교환 수준) |

## 응용 (Applications)

- 파일·소켓·락·메모리 자동 정리, 예외 안전 코드.
- 복사 비용 절감(`const&`), 소유권·이동 모델 설계.

## 흔한 오해 (Common Misunderstandings)

- **참조는 null이 될 수 없는 별칭** — 재바인딩도 안 됨(포인터와 다름).
- **지역 객체 참조 반환은 dangling** — 수명 끝난 스택.
- **RAII는 메모리만이 아니다** — 모든 자원(락·핸들·트랜잭션).
- **소멸자에서 예외를 던지면 위험** — unwinding 중 두 번째 예외 → `terminate`.

## TMI

- `std::lock_guard`/`unique_lock` 은 mutex를, `std::scoped_lock` 은 여러 mutex를 데드락 없이 RAII로 잡는다.
- 이동 후 원본은 "유효하지만 미지정" 상태 — 다시 대입하거나 소멸만 안전.
- `[[nodiscard]]` 와 RAII를 결합해 자원 핸들을 실수로 버리는 것을 막는다.

## 연습 / 확인 문제 (Exercises)

- 참조로 두 값을 swap하는 함수를 작성하라.
- `Timer` 가 예외 발생 시에도 "stop"을 출력함을 보여라(스택 unwinding).
- dangling reference 예시를 만들고 피하는 법을 설명하라.
- 자원을 가진 클래스에 rule of 5를 적용하라.

## 이어서 읽기 (Reading Path)

- 이전: [C++ 기본 문법](Cpp-Setup-and-Syntax.md)
- 다음: [클래스와 템플릿](Cpp-Classes-and-Templates.md)
- 관련: [스마트 포인터와 메모리](Cpp-Memory-and-Smart-Pointers.md)

## 참조 (References)

- [Programming/Pointers-and-Memory.md](../../Pointers-and-Memory.md)
- [Reference/Books.md](../../../Reference/Books.md)
