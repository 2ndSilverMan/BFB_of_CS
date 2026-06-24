# 코어 덤프 분석 (Core Dump Analysis)

- Level: Advanced
- Prerequisites: [Programming/Languages/C/C-Pointers-and-Memory.md](../../Programming/Languages/C/C-Pointers-and-Memory.md), [Engineering/Debugging/Stack-Traces.md](Stack-Traces.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

코어 덤프는 프로세스가 비정상 종료될 때의 메모리와 레지스터 상태를 저장한 파일이다. 분석하면 crash 당시 call stack, 변수, 메모리 상태를 확인할 수 있다.

## 직관 (Intuition)

사고가 난 순간의 블랙박스 영상이다. 프로그램이 이미 죽었어도 그 순간 어디서 무엇을 하다 죽었는지 볼 수 있다.

## 이론 (Theory)

코어 덤프 분석에는 실행 파일, symbol/debug info, core file이 필요하다. 최적화와 symbol strip 여부에 따라 stack 품질이 달라진다. 민감정보가 메모리에 포함될 수 있어 보관과 공유에 주의해야 한다.

## 구현 (Implementation)

```text
debugger binary corefile
bt
frame 0
print variable
```

## 복잡도 (Complexity)

Core dump 분석 비용은 dump 크기, symbol 품질, 최적화 수준, thread 수에 좌우된다. 수집 자체는 사후 분석에 강하지만 storage·개인정보·민감 메모리 유출 위험 때문에 보존 정책이 필요하다.

## 응용 (Applications)

- C/C++ segmentation fault 분석
- production crash 사후 분석
- native extension 장애 조사
- 메모리 corruption 단서 확인

## 흔한 오해 (Common Misunderstandings)

- 코어 덤프만 있으면 항상 원인이 보이는 것은 아니다.
- Debug symbol이 없으면 stack이 부정확할 수 있다.
- 메모리 corruption은 crash 지점보다 훨씬 전에 발생했을 수 있다.
- Core file에는 비밀값이 들어 있을 수 있다.

## TMI

- Linux에서는 `ulimit -c`와 core pattern 설정이 관련된다.
- Split debug symbol 패키지를 따로 보관하는 운영도 있다.
- Crash dump 분석은 재현이 어려운 native bug에서 특히 가치가 크다.

## 연습 / 확인 문제 (Exercises)

- 코어 덤프에 필요한 세 가지 artifact를 설명하라.
- Crash 지점과 root cause가 다를 수 있는 이유를 말하라.
- Core file 공유 전 보안 검토 항목을 작성하라.

## 이어서 읽기 (Reading Path)

- 이전: [스택 트레이스](Stack-Traces.md)
- 다음: [메모리 오류](Memory-Errors.md), [Valgrind/ASan](Valgrind-AddressSanitizer.md)

## 참조 (References)

- [Programming/Languages/C/C-Pointers-and-Memory.md](../../Programming/Languages/C/C-Pointers-and-Memory.md)
- [Reference/Books.md](../../Reference/Books.md)
