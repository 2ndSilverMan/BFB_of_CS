# 조건부 중단점과 로깅 포인트

- Level: Intermediate
- Prerequisites: [Engineering/Debugging/Breakpoints-and-Stepping.md](Breakpoints-and-Stepping.md), [Engineering/Debugging/Structured-Logging.md](Structured-Logging.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

조건부 중단점은 특정 조건이 참일 때만 실행을 멈추는 중단점이고, 로깅 포인트는 코드를 수정하지 않고 디버거가 로그를 남기게 하는 기능이다.

## 직관 (Intuition)

루프가 백만 번 도는데 한 번만 이상하다면 매번 멈출 수 없다. 조건부 중단점은 "user_id가 42일 때만 멈춰" 같은 필터다.

## 이론 (Theory)

조건식은 디버거가 평가하므로 부작용이 없는 표현식을 써야 한다. Logpoint는 production-like 환경에서 코드 변경 없이 관찰을 늘릴 때 유용하지만 성능과 민감정보 노출을 조심한다.

## 구현 (Implementation)

```text
break if order.id == "A123"
logpoint: "total={total}, discount={discount}"
```

## 복잡도 (Complexity)

조건식은 breakpoint hit마다 평가되므로 hot path에서는 실행이 크게 느려질 수 있다. 대신 조건을 잘 잡으면 수천 번의 불필요한 중단을 피하고, 특정 입력·상태에서만 멈춰 관찰 비용을 줄인다.

## 응용 (Applications)

- 특정 사용자·요청만 추적
- 큰 반복문 디버깅
- 일시적 관찰성 추가
- 재현 어려운 상태 포착

## 흔한 오해 (Common Misunderstandings)

- 조건식에 상태 변경 함수를 넣으면 디버깅이 문제를 바꿀 수 있다.
- Logpoint는 정식 로깅 설계를 대체하지 않는다.
- 조건부 중단점도 너무 많이 쓰면 실행이 느려질 수 있다.
- 민감정보를 디버그 로그에 남기면 안 된다.

## TMI

- Hit count breakpoint는 n번째 도달 때 멈춘다.
- Exception breakpoint는 예외가 던져지는 순간 멈춘다.
- Tracepoint라는 이름으로 제공되는 도구도 있다.

## 연습 / 확인 문제 (Exercises)

- 특정 ID에서만 멈추는 조건부 중단점을 설정하라.
- Logpoint와 코드 로그의 장단점을 비교하라.
- 부작용 있는 조건식 예시를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [중단점과 스텝 실행](Breakpoints-and-Stepping.md)
- 다음: [원격 디버깅](Remote-Debugging.md), [구조화 로깅](Structured-Logging.md)

## 참조 (References)

- [Engineering/Debugging/Structured-Logging.md](Structured-Logging.md)
- [Reference/Books.md](../../Reference/Books.md)
