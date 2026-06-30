# 메모리 오류 (Memory Errors)

- Level: Advanced
- Prerequisites: [Programming/Languages/C/C-Pointers-and-Memory.md](../../Programming/Languages/C/C-Pointers-and-Memory.md), [Programming/Languages/Cpp/Cpp-Memory-and-Smart-Pointers.md](../../Programming/Languages/Cpp/Cpp-Memory-and-Smart-Pointers.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

메모리 오류는 프로그램이 잘못된 메모리를 읽거나 쓰는 버그다. Buffer overflow, use-after-free, double free, null dereference, uninitialized read가 대표적이다.

## 직관 (Intuition)

내 방 서랍만 써야 하는데 옆집 서랍을 열거나, 이미 버린 쪽지를 따라가거나, 빈 주소로 찾아가는 문제다. 운 좋게 동작해 보이다가 나중에 터질 수 있다.

## 이론 (Theory)

C/C++ 같은 언어는 메모리 수명과 범위 검사를 프로그래머가 많이 책임진다. Undefined behavior는 컴파일러 최적화와 결합해 예측 불가능한 결과를 낼 수 있다.

### 오류 유형 분리

메모리 오류는 use-after-free, double free, out-of-bounds, uninitialized read, leak, stack overflow처럼 원인이 다르다. 증상은 모두 crash나 corruption으로 보일 수 있으므로 allocator log, sanitizer report, core dump, repro input을 함께 본다.

메모리 corruption은 원인 지점과 crash 지점이 멀 수 있다. 최초 잘못된 write를 잡기 위해 ASan, guard page, heap poisoning, deterministic allocator 설정을 사용한다.

## 구현 (Implementation)

```c
int xs[3] = {1, 2, 3};
xs[3] = 4;  // out-of-bounds write
```

## 복잡도 (Complexity)

메모리 오류 탐색 비용은 allocation 수, object lifetime, 재현 안정성에 좌우된다. Sanitizer와 heap checker는 탐색 공간을 줄이지만 실행 시간·메모리 사용량을 늘리고, 타이밍 민감 버그의 재현성을 바꿀 수 있다.

## 응용 (Applications)

- native crash 분석
- 보안 취약점 조사
- 성능 민감 코드 안정화
- FFI/native extension 디버깅

## 흔한 오해 (Common Misunderstandings)

- 한 번 실행에서 정상이라고 안전한 것은 아니다.
- Segmentation fault 지점이 원인 지점과 다를 수 있다.
- 메모리 오류는 보안 취약점으로 이어질 수 있다.
- 스마트 포인터도 순환 참조와 수명 설계를 대신하지 않는다.

## TMI

- ASLR과 stack canary는 일부 메모리 공격 완화에 도움을 준다.
- UndefinedBehaviorSanitizer는 UB 탐지에 쓰인다.
- Use-after-free는 재현이 timing과 allocator 상태에 민감하다.

## 연습 / 확인 문제 (Exercises)

- Buffer overflow와 use-after-free 차이를 설명하라.
- Out-of-bounds read/write 예시를 작성하라.
- 메모리 오류가 보안 문제가 되는 이유를 말하라.

## 이어서 읽기 (Reading Path)

- 이전: [C 포인터와 메모리](../../Programming/Languages/C/C-Pointers-and-Memory.md)
- 다음: [Valgrind/AddressSanitizer](Valgrind-AddressSanitizer.md), [코어 덤프 분석](Core-Dump-Analysis.md)

## 참조 (References)

- [Programming/Languages/C/C-Pointers-and-Memory.md](../../Programming/Languages/C/C-Pointers-and-Memory.md)
- [Engineering/Security/Web-Security.md](../Security/Web-Security.md)
