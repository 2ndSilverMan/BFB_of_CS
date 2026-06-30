# 중단점, 스텝 실행, 변수 감시

- Level: Beginner
- Prerequisites: [Engineering/Debugging/Minimal-Reproducible-Example.md](Minimal-Reproducible-Example.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

중단점은 프로그램 실행을 특정 줄에서 멈추게 하고, 스텝 실행은 한 줄 또는 한 함수씩 진행하며 상태 변화를 관찰하는 디버거 기능이다. 변수 감시는 현재 값과 변화 흐름을 보여 준다.

## 직관 (Intuition)

프로그램을 빠르게 지나가는 영화가 아니라 프레임 단위로 멈춰 보는 것이다. 값이 기대와 달라지는 정확한 순간을 찾는다.

## 이론 (Theory)

Step over는 함수 내부로 들어가지 않고 다음 줄로, step into는 함수 내부로, step out은 현재 함수가 끝날 때까지 진행한다. Watch expression은 특정 표현식 값을 계속 보여 준다.

### 관찰 지점 설계

중단점은 멈추고 싶은 줄이 아니라 가설을 구분하는 관찰 지점에 둔다. 입력이 잘못됐는지, 상태 전이가 잘못됐는지, 출력 직전 변환이 잘못됐는지를 나눠 보는 위치가 좋다.

스텝 실행은 강력하지만 느리다. 반복문이나 고빈도 경로에서는 watch expression, conditional breakpoint, logpoint를 사용해 필요한 이벤트에서만 멈추도록 한다.

## 구현 (Implementation)

```text
breakpoint at calculate_total
step into discount
watch: subtotal, discount_rate, total
```

## 복잡도 (Complexity)

중단점과 step 실행의 비용은 멈추는 횟수와 관찰해야 할 call depth에 비례한다. Hot loop나 동시성 코드에서 자주 멈추면 프로그램 타이밍 자체가 바뀔 수 있으므로, 의심 구간을 좁힌 뒤 사용한다.

## 응용 (Applications)

- 조건문 분기 확인
- 변수 값 변화 추적
- 호출 순서 이해
- 예외 발생 직전 상태 관찰

## 흔한 오해 (Common Misunderstandings)

- 디버거로 본 값도 최적화 빌드에서는 예상과 다를 수 있다.
- 멀티스레드 프로그램은 멈추는 순간 다른 스레드 상태도 고려해야 한다.
- 너무 많은 중단점은 흐름 이해를 방해한다.
- 디버거 관찰이 timing bug를 숨길 수 있다.

## TMI

- Data breakpoint는 특정 메모리 값이 바뀔 때 멈춘다.
- Logpoint는 멈추지 않고 로그만 남기는 중단점이다.
- IDE 디버거와 CLI 디버거는 같은 개념을 다른 UI로 제공한다.

## 연습 / 확인 문제 (Exercises)

- 작은 함수에 중단점을 걸고 step into/over 차이를 확인하라.
- 변수 watch로 값이 처음 틀어지는 줄을 찾아라.
- 예외가 발생하는 줄에서 call stack을 읽어라.

## 이어서 읽기 (Reading Path)

- 이전: [최소 재현 케이스](Minimal-Reproducible-Example.md)
- 다음: [조건부 중단점](Conditional-Breakpoints.md), [스택 트레이스](Stack-Traces.md)

## 참조 (References)

- [Engineering/Debugging/Stack-Traces.md](Stack-Traces.md)
- [Reference/Books.md](../../Reference/Books.md)
