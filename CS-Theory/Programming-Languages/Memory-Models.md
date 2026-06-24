# 메모리 관리 모델 (Memory Management Models)

- Level: Advanced
- Prerequisites: [Type-Systems.md](Type-Systems.md), [Programming/Pointers-and-Memory.md](../../Programming/Pointers-and-Memory.md), [Systems/Operating-Systems/Memory-Management.md](../../Systems/Operating-Systems/Memory-Management.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

메모리 관리 모델은 프로그램이 메모리를 어떻게 할당, 소유, 공유, 해제하는지 정하는 언어와 런타임의 규칙이다. 수동 관리, garbage collection, reference counting, ownership/borrowing 같은 방식이 있다.

## 직관 (Intuition)

메모리는 빌린 물건과 비슷하다. 누가 빌렸고, 언제 돌려줘야 하며, 동시에 여러 사람이 써도 되는지를 정하지 않으면 분실, 중복 반납, 훼손이 생긴다. 언어별 메모리 모델은 이 문제를 다르게 해결한다.

## 이론 (Theory)

대표 모델은 다음과 같다.

- Manual management: `malloc/free`, `new/delete`처럼 프로그래머가 직접 관리한다.
- Garbage collection: 도달 가능한 객체를 추적해 더 이상 쓰지 않는 객체를 회수한다.
- Reference counting: 참조 수가 0이 되면 즉시 해제한다.
- Ownership/borrowing: 컴파일 시간 규칙으로 소유권 이동과 참조 수명을 제한한다.

각 모델은 성능, 예측 가능성, 안전성, 구현 복잡도에서 trade-off를 가진다. GC는 use-after-free를 줄이지만 pause와 런타임 비용이 있고, 수동 관리는 빠를 수 있지만 안전 버그 위험이 크다.

## 구현 (Implementation)

소유권 모델의 직관은 한 값의 책임자를 명확히 두는 것이다.

```text
owner creates value
owner may move value to another owner
borrowers may read or mutate only under rules
value is released when owner lifetime ends
```

구체 규칙은 언어마다 다르며, Rust의 borrow checker가 대표적인 정적 소유권 검사기다.

## 복잡도 (Complexity)

수동 관리는 런타임 오버헤드는 작을 수 있지만 개발 복잡도가 높다. GC는 allocation fast path를 빠르게 만들 수 있지만 collection 비용과 latency가 있다. Reference counting은 비용이 분산되지만 cycle 처리가 어렵다.

## 응용 (Applications)

- 시스템 프로그래밍 언어 설계
- 런타임과 VM 구현
- 안전한 동시성 모델
- 성능 민감 애플리케이션의 메모리 전략

## 흔한 오해 (Common Misunderstandings)

- GC가 있으면 메모리 누수가 절대 없다는 뜻은 아니다. 불필요한 참조가 남으면 누수처럼 된다.
- 수동 관리가 항상 빠른 것은 아니다. allocator 비용과 fragmentation이 있다.
- reference counting은 cycle을 자동으로 해결하지 못할 수 있다.
- ownership 모델은 런타임 비용을 줄일 수 있지만 학습 비용이 있다.

## TMI

- Region/arena allocation은 많은 객체를 한 번에 해제하는 전략이다.
- Escape analysis는 객체를 heap 대신 stack에 둘 수 있는지 판단한다.
- 메모리 모델은 언어의 concurrency safety와 깊게 연결된다.

## 연습 / 확인 문제 (Exercises)

- use-after-free와 memory leak의 차이를 설명하라.
- reference counting에서 cycle 문제가 생기는 예를 들어라.
- GC와 ownership 모델의 장단점을 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [패러다임 비교](Paradigms.md)
- 다음: [동시성 모델](Concurrency-Models.md)

## 참조 (References)

- [Programming/Pointers-and-Memory.md](../../Programming/Pointers-and-Memory.md)
- [Systems/Operating-Systems/Memory-Management.md](../../Systems/Operating-Systems/Memory-Management.md)
- [Type-Systems.md](Type-Systems.md)
- [Reference/Books.md](../../Reference/Books.md)
