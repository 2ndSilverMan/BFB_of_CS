# C++ 스마트 포인터와 메모리

- Level: Intermediate
- Prerequisites: [C++ 참조와 RAII](Cpp-References-and-RAII.md), [Programming/Pointers-and-Memory.md](../../Pointers-and-Memory.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

스마트 포인터는 동적 객체의 **소유권과 해제를 RAII로** 관리한다. `unique_ptr`=단독 소유(이동만), `shared_ptr`=공유 소유(참조 카운트), `weak_ptr`=비소유 관찰(순환 끊기). 소유권을 *타입으로 표현*해 leak·double free·use-after-free를 구조적으로 막는다.

## 직관 (Intuition)

raw pointer가 주소만 적힌 쪽지라면, 스마트 포인터는 **"누가 이 자원을 책임지나"까지 적힌 계약서**다. 계약서가 scope를 벗어나면 자원을 자동 정리한다. 핵심 질문은 항상 "이 객체의 소유자는 누구인가" — 답이 하나면 `unique_ptr`, 여럿이면 `shared_ptr`.

## 핵심 문법 (Core Syntax)

```cpp
#include <memory>
auto p = std::make_unique<int>(42);              // 단독 소유
auto s = std::make_shared<std::string>("hi");    // 공유 소유
std::weak_ptr<std::string> w = s;                // 비소유 관찰
```

## 이론 (Theory)

### 1. unique_ptr — 제로 오버헤드

복사 불가, **이동만** 가능(소유권 이전). 크기·성능이 raw pointer와 사실상 같다(제로 오버헤드 추상화). 기본 선택지.

### 2. shared_ptr — 제어 블록과 원자적 카운트

별도 **control block**(강한 카운트 + 약한 카운트)을 둔다. 복사 시 카운트 **원자적 증가**(스레드 안전하지만 비용), 0이 되면 객체 해제. `make_shared` 는 객체+제어블록을 **한 번에 할당**(2회 → 1회).

### 3. 순환 참조와 weak_ptr

두 `shared_ptr` 이 서로를 가리키면 카운트가 **0이 되지 않아 leak**. 한쪽을 `weak_ptr` 로 바꿔 끊는다. `weak_ptr` 은 `lock()` 으로 살아 있을 때만 `shared_ptr` 를 얻는다(만료 시 빈 포인터).

## 구현 (Implementation)

```cpp
#include <memory>
struct Node {
    std::shared_ptr<Node> next;        // 강한 참조
    std::weak_ptr<Node> prev;          // 약한 참조: 순환 끊기 (이게 shared면 leak)
};

auto factory() {                       // 팩토리: unique_ptr 반환이 자연스러움
    return std::make_unique<int>(7);
}

int main() {
    auto owner = std::make_unique<int>(42);
    auto moved = std::move(owner);     // 소유권 이전
    // owner == nullptr, moved == 42
    auto a = std::make_shared<Node>(), b = std::make_shared<Node>();
    a->next = b; b->prev = a;          // prev가 weak라 누수 없음
}
```

## 복잡도 (Complexity)

| 연산 | 비용 |
|---|---|
| `unique_ptr` 이동 | 포인터 대입(제로 오버헤드) |
| `shared_ptr` 복사/소멸 | **원자적** 카운트 갱신(경합 시 비쌈) |
| `make_shared` | 객체+제어블록 1회 할당 |
| 작은 객체 대량 할당 | allocator·단편화 병목 |

## 응용 (Applications)

- 동적 객체 소유권, 팩토리 반환값, 트리·그래프(부모는 weak).
- 예외 안전 자원 관리(스택 unwinding에서 자동 해제).

## 흔한 오해 (Common Misunderstandings)

- **스마트 포인터가 모든 메모리 문제를 풀지 않는다** — 순환·dangling은 설계로.
- **기본은 `unique_ptr`** — 진짜 공유일 때만 `shared_ptr`(남발은 소유권을 흐린다).
- **`shared_ptr` 순환은 leak** — 한쪽을 `weak_ptr`.
- **raw pointer는 비소유 관찰**로만(수명은 다른 곳이 보장).

## TMI

- `make_shared` 는 객체와 제어블록이 한 메모리 블록이라, `weak_ptr` 이 남아 있으면 객체 메모리도 못 푼다(미묘한 retention).
- `unique_ptr<T[]>` 와 커스텀 deleter로 배열·C 자원(FILE*, fd)도 RAII 관리한다.
- move semantics가 `unique_ptr` 소유권 이전의 기반 — `std::move` 는 "이동해도 된다"는 캐스트일 뿐.

## 연습 / 확인 문제 (Exercises)

- `unique_ptr` 을 함수에서 반환하고 호출부에서 받아라(이동).
- `shared_ptr` 순환 참조로 leak을 재현하고 `weak_ptr` 로 고쳐라(sanitizer 확인).
- raw/`unique_ptr`/`shared_ptr` 의 사용 기준을 표로 정리하라.
- 커스텀 deleter로 `FILE*` 를 RAII로 닫아라.

## 이어서 읽기 (Reading Path)

- 이전: [C++ 참조와 RAII](Cpp-References-and-RAII.md)
- 다음: [Systems/Operating-Systems](../../../Systems/Operating-Systems/)
- 관련: [STL](Cpp-STL.md)

## 참조 (References)

- [Programming/Pointers-and-Memory.md](../../Pointers-and-Memory.md)
- [Reference/Books.md](../../../Reference/Books.md)
