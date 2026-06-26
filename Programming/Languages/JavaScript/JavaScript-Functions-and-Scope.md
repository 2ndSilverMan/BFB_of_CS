# JavaScript 함수와 스코프 (Functions and Scope)

- Level: Beginner
- Prerequisites: [Programming/Functions-and-Recursion.md](../../Functions-and-Recursion.md), [JavaScript 값과 타입 변환](JavaScript-Values-and-Coercion.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

JavaScript 함수는 값처럼 전달할 수 있는 first-class object다. 스코프는 이름이 보이는 범위이며, closure는 함수가 만들어진 당시의 외부 변수를 기억하는 성질이다.

## 직관 (Intuition)

함수는 단순한 명령 묶음이 아니라 다른 함수에 넘길 수 있는 작은 행동 객체다. Closure는 함수가 자기 주변 환경을 작은 가방처럼 들고 다니는 느낌이다.

## 핵심 문법 (Core Syntax)

```javascript
function add(a, b) {
  return a + b;
}

const multiply = (a, b) => a * b;

function makeCounter() {
  let count = 0;
  return () => {
    count += 1;
    return count;
  };
}
```

## 이론 (Theory)

`let`과 `const`는 블록 스코프를 갖고, `var`는 함수 스코프를 갖는다. 함수 선언은 hoisting되지만, 함수 표현식과 arrow function은 변수 초기화 규칙을 따른다.

## 구현 (Implementation)

함수는 입력과 반환값을 분명히 하고, closure가 어떤 binding을 캡처하는지 console로 확인한다. `var` 대신 `let`/`const`를 기본으로 쓰고, callback에서 `this`가 필요한 경우 arrow function과 일반 function의 차이를 실험한다.

```javascript
function makeAdder(base) {
  return (x) => base + x;   // base를 캡처하는 closure
}

const add10 = makeAdder(10);
console.log(add10(5));      // 15

const next = (() => {
  let count = 0;            // 외부에서 접근 불가능한 private 상태
  return () => (count += 1);
})();
console.log(next(), next()); // 1 2
```

## 복잡도 (Complexity)

함수 호출과 closure 생성은 보통 작지만 hot loop에서는 누적될 수 있다. 재귀는 call stack 깊이 제한을 받으며, 캡처한 큰 객체가 오래 살아 있으면 memory retention 문제가 생긴다.

## 응용 (Applications)

- 이벤트 핸들러
- 배열 고차 함수 `map`, `filter`, `reduce`
- 상태를 숨긴 작은 도구 만들기
- 비동기 callback 구성

## 흔한 오해 (Common Misunderstandings)

- Arrow function은 자기만의 `this`를 만들지 않는다.
- Closure는 강력하지만 의도치 않은 상태 공유를 만들 수 있다.
- Hoisting을 믿고 선언 전 사용을 남발하면 읽기 어려워진다.
- `this`는 호출 방식에 따라 달라진다.

## TMI

- JavaScript의 함수형 스타일은 UI 코드에서 자주 쓰인다.
- `bind`, `call`, `apply`는 `this`와 인자 전달을 제어한다.
- Closure는 모듈 패턴과 캡슐화에 오래 쓰였다.

## 연습 / 확인 문제 (Exercises)

- `makeCounter`를 직접 실행해 closure가 상태를 기억하는지 확인하라.
- `map`과 `filter`로 숫자 배열을 변환하라.
- Arrow function과 일반 function의 `this` 차이를 예제로 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [값과 타입 변환](JavaScript-Values-and-Coercion.md)
- 다음: [DOM과 이벤트](JavaScript-DOM-and-Events.md), [비동기 프로그래밍](JavaScript-Async.md)

## 참조 (References)

- [Programming/Functions-and-Recursion.md](../../Functions-and-Recursion.md)
- [Reference/Books.md](../../../Reference/Books.md)
