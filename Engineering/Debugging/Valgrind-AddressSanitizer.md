# Valgrind / AddressSanitizer

- Level: Advanced
- Prerequisites: [Engineering/Debugging/Memory-Errors.md](Memory-Errors.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

Valgrind와 AddressSanitizer(ASan)는 C/C++ 프로그램의 메모리 오류를 찾는 도구다. 잘못된 read/write, use-after-free, leak 같은 문제를 실행 중 탐지한다.

## 직관 (Intuition)

프로그램이 메모리를 만질 때 옆에서 검사원이 지켜보는 방식이다. 평소엔 조용히 넘어가던 실수를 즉시 큰 소리로 알려 준다.

## 이론 (Theory)

Valgrind는 가상 실행 환경에서 메모리 접근을 추적해 강력하지만 느리다. ASan은 컴파일러 instrumentation으로 redzone과 shadow memory를 사용해 빠르게 오류를 잡는다.

## 구현 (Implementation)

```bash
cc -fsanitize=address -g main.c -o main
./main
```

## 복잡도 (Complexity)

Valgrind는 binary instrumentation 때문에 느리지만 정밀한 관찰을 제공하고, AddressSanitizer는 compile-time instrumentation으로 상대적으로 빠르게 CI에 넣기 좋다. 비용은 test suite 길이, memory footprint, sanitizer 종류에 따라 달라진다.

## 응용 (Applications)

- CI에서 native memory bug 탐지
- crash 원인 조사
- leak 탐지
- fuzzing과 결합

## 흔한 오해 (Common Misunderstandings)

- 도구가 모든 메모리 버그를 잡는 것은 아니다.
- Sanitizer 빌드는 production 성능과 다르다.
- 보고서의 첫 오류가 가장 중요한 원인일 가능성이 높다.
- 최적화와 debug symbol 설정이 리포트 품질에 영향을 준다.

## TMI

- ASan 외에도 UBSan, TSan, MSan이 있다.
- Valgrind는 ASan보다 느리지만 recompile 없이 쓸 수 있는 경우가 많다.
- LeakSanitizer는 ASan과 함께 동작하는 경우가 많다.

## 연습 / 확인 문제 (Exercises)

- 의도적 out-of-bounds 코드를 ASan으로 실행하라.
- Valgrind와 ASan의 장단점을 비교하라.
- Sanitizer report에서 stack trace를 읽어 원인 줄을 찾으라.

## 이어서 읽기 (Reading Path)

- 이전: [메모리 오류](Memory-Errors.md)
- 다음: [레이스 컨디션 디버깅](Race-Condition-Debugging.md)

## 참조 (References)

- [Engineering/Debugging/Memory-Errors.md](Memory-Errors.md)
- [Reference/Books.md](../../Reference/Books.md)
