# 메모리 관리 모델 (Memory Management Models)

- Level: Advanced
- Prerequisites: [Type-Systems.md](Type-Systems.md), [Programming/Pointers-and-Memory.md](../../Programming/Pointers-and-Memory.md), [Systems/Operating-Systems/Memory-Management.md](../../Systems/Operating-Systems/Memory-Management.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

메모리 관리 모델은 프로그램이 메모리를 **어떻게 할당·소유·공유·해제**하는지 정하는 언어·런타임 규칙이다. 수동(`malloc/free`), garbage collection(GC), reference counting, ownership/borrowing — 각각 **안전성·성능·예측 가능성**의 트레이드오프가 다르다.

## 직관 (Intuition)

메모리는 빌린 물건이다. "누가 빌렸고, 언제 돌려주며, 동시에 여럿이 써도 되는가"를 안 정하면 **분실(leak)·중복 반납(double free)·훼손(use-after-free)** 이 생긴다. 각 모델은 이 책임 추적을 *런타임에*(GC/refcount) 또는 *컴파일 타임에*(ownership) 한다.

## 이론 (Theory)

### 1. 네 모델

| 모델 | 메커니즘 | 강점 | 약점 |
|---|---|---|---|
| 수동 | `malloc/free` | 예측 가능·빠름 | 안전 버그(UAF·leak) |
| **GC(추적)** | 도달 가능 객체 추적 | 안전·편리 | pause·런타임 비용 |
| reference counting | 참조 수 0 → 즉시 해제 | 결정적·분산 비용 | **순환 참조 누수**·원자적 갱신 비용 |
| ownership/borrowing | 컴파일 타임 규칙 | 런타임 0·안전 | 학습 곡선 |

### 2. 추적 GC: tri-color marking

루트에서 도달 가능한 객체를 mark, 나머지를 sweep. **tri-color**(흰=미방문, 회=방문중, 검=완료) 불변식으로 동시(concurrent) GC를 가능케 한다 — "검은 객체가 흰 객체를 직접 가리키면 안 된다"(write barrier로 유지). 세대 GC는 "대부분 객체는 일찍 죽는다"는 가설로 young 영역만 자주 수집.

### 3. ownership: 컴파일 타임 소유권

한 값의 **소유자는 하나**, 소유권은 이동(move)하거나 빌려준다(borrow: 공유 불변 참조 다수 *또는* 가변 참조 하나). 소유자 수명이 끝나면 자동 해제 — Rust의 borrow checker가 정적으로 강제([RAII](../../Programming/Languages/Cpp/Cpp-References-and-RAII.md)의 일반화).

## 구현 (Implementation)

```python
# reference counting의 순환 누수 (CPython refcount + 보조 GC가 있어야 회수)
import sys, gc
class Node: pass
a, b = Node(), Node()
a.ref = b; b.ref = a            # 순환: 서로 참조 → refcount가 0이 안 됨
del a, b                        # refcount만으론 회수 불가
gc.collect()                    # 추적 GC가 순환을 수거
```

```text
# ownership/borrow 규칙 (의사)
let s = String::from("hi");     // s가 소유
let r = &s;                     // 불변 빌림(여럿 가능)
// let m = &mut s;              // 동시에 가변 빌림 → 컴파일 에러(데이터 레이스 방지)
// s가 scope 끝 → 자동 free
```

## 복잡도 (Complexity)

| 모델 | 할당 | 해제 | 지연 특성 |
|---|---|---|---|
| 수동 | allocator 비용 | 즉시 | 예측 가능 |
| 추적 GC | fast bump pointer | 일괄(pause) | **stop-the-world** 지연 |
| refcount | 보통 | 즉시(카운트 0) | 분산되나 원자 갱신 |
| ownership | 수동급 | scope 종료 | 런타임 0 |

## 응용 (Applications)

- 시스템 언어 설계(Rust ownership, C++ RAII), 런타임·VM(JVM/CLR GC).
- 안전한 동시성(데이터 레이스 방지), 성능 민감 앱의 메모리 전략(arena).

## 흔한 오해 (Common Misunderstandings)

- **GC가 있어도 누수는 가능** — 안 쓰는데 참조가 남으면(컬렉션·캐시·리스너) "논리적 누수".
- **수동 관리가 항상 빠르지 않다** — allocator 비용·단편화.
- **reference counting은 순환을 못 푼다** — 보조 추적 GC나 weak 참조 필요.
- **ownership은 런타임 비용을 줄이나 학습 비용**이 있다.

## TMI

- Region/arena allocation은 많은 객체를 **한 번에** 해제해(개별 free 없이) 컴파일러·게임에서 인기다.
- escape analysis는 객체가 함수 밖으로 새지 않으면 힙 대신 스택에 둔다(또는 제거).
- GC pause를 줄이는 동시·증분 수집기(ZGC·Shenandoah)는 sub-ms pause를 목표로 한다.

## 연습 / 확인 문제 (Exercises)

- use-after-free와 memory leak의 차이를 설명하라.
- reference counting의 순환 누수를 재현하고 weak 참조로 끊어라.
- tri-color 불변식이 동시 GC에서 왜 필요한지 write barrier로 설명하라.
- GC와 ownership 모델의 장단점을 지연·안전·학습비용으로 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [패러다임 비교](Paradigms.md)
- 다음: [동시성 모델](Concurrency-Models.md)
- 관련: [메모리 관리(OS)](../../Systems/Operating-Systems/Memory-Management.md)

## 참조 (References)

- [Programming/Pointers-and-Memory.md](../../Programming/Pointers-and-Memory.md)
- [Systems/Operating-Systems/Memory-Management.md](../../Systems/Operating-Systems/Memory-Management.md)
- [Type-Systems.md](Type-Systems.md)
- [Reference/Books.md](../../Reference/Books.md)
