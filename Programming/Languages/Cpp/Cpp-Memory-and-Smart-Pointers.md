# C++ 스마트 포인터와 메모리

- Level: Intermediate
- Prerequisites: [C++ 참조와 RAII](Cpp-References-and-RAII.md), [Programming/Pointers-and-Memory.md](../../Pointers-and-Memory.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

스마트 포인터는 동적 객체의 소유권과 해제를 RAII로 관리하는 표준 타입이다. `std::unique_ptr`은 단독 소유, `std::shared_ptr`은 공유 소유, `std::weak_ptr`은 소유하지 않는 관찰 참조를 표현한다.

## 직관 (Intuition)

Raw pointer가 주소만 적힌 쪽지라면, 스마트 포인터는 "누가 이 자원을 책임지는가"까지 적힌 계약서다. 계약서가 scope를 벗어나면 자원을 자동으로 정리한다.

## 핵심 문법 (Core Syntax)

```cpp
#include <memory>

auto p = std::make_unique<int>(42);

auto shared = std::make_shared<std::string>("hello");
std::weak_ptr<std::string> weak = shared;
```

## 이론 (Theory)

`unique_ptr`은 복사할 수 없고 move할 수 있다. `shared_ptr`은 reference count가 0이 되면 객체를 해제한다. 순환 참조가 있으면 reference count가 0이 되지 않을 수 있으므로 `weak_ptr`이 필요하다.

## 구현 (Implementation)

기본 소유권은 `std::unique_ptr`로 표현하고, 실제 공유 소유가 필요할 때만 `std::shared_ptr`를 쓴다. 순환 참조가 가능한 구조는 `std::weak_ptr`를 포함해 설계하고, raw pointer는 비소유 관찰자로 제한한다.

## 복잡도 (Complexity)

`unique_ptr` 이동은 가볍지만 `shared_ptr` 복사는 reference count 갱신 비용이 있다. 동적 allocation은 cache locality와 fragmentation에 영향을 주며, 작은 객체를 많이 만들면 allocator 비용이 병목이 될 수 있다.

## 응용 (Applications)

- 동적 객체 소유권 표현
- 팩토리 함수 반환값
- 트리·그래프 구조 일부
- 예외 안전 자원 관리

## 흔한 오해 (Common Misunderstandings)

- 스마트 포인터가 모든 메모리 문제를 자동으로 해결하지는 않는다.
- 기본 선택은 보통 `unique_ptr`이다. 필요할 때만 `shared_ptr`을 쓴다.
- `shared_ptr` 남발은 소유권을 흐리게 만든다.
- Raw pointer도 비소유 관찰 용도로는 쓸 수 있지만 수명 보장이 필요하다.

## TMI

- `make_unique`, `make_shared`는 안전하고 간결한 생성 패턴이다.
- Move semantics는 `unique_ptr` 소유권 이전의 기반이다.
- RAII는 mutex, file, socket에도 같은 방식으로 적용된다.

## 연습 / 확인 문제 (Exercises)

- `unique_ptr`을 함수에서 반환하는 예제를 작성하라.
- `shared_ptr` 순환 참조가 왜 문제인지 설명하라.
- Raw pointer, `unique_ptr`, `shared_ptr`의 사용 기준을 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [참조와 RAII](Cpp-References-and-RAII.md), [STL](Cpp-STL.md)
- 다음: [Systems](../../../Systems/), [Performance](../../../Engineering/Performance/)

## 참조 (References)

- [Programming/Pointers-and-Memory.md](../../Pointers-and-Memory.md)
- [Reference/Books.md](../../../Reference/Books.md)
