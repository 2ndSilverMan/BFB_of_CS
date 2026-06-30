# JavaScript 함수와 스코프 (Functions and Scope)

- Level: Beginner
- Prerequisites: [Programming/Functions-and-Recursion.md](../../Functions-and-Recursion.md), [JavaScript 값과 타입 변환](JavaScript-Values-and-Coercion.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

JavaScript 함수는 값처럼 전달되는 **일급 객체**다. **스코프**(이름이 보이는 범위)와 **클로저**(생성 시점의 외부 변수를 기억), 그리고 **`this` 바인딩 규칙**이 함수 동작의 핵심 3축이다.

## 직관 (Intuition)

함수는 명령 묶음이 아니라 넘길 수 있는 작은 행동 객체다. 클로저는 함수가 자기 주변 환경을 **가방처럼 들고 다니는** 것. `this` 는 "함수가 누구의 것이냐"가 아니라 **어떻게 호출됐느냐**로 결정된다 — 이 오해가 JS 버그의 단골이다.

## 핵심 문법 (Core Syntax)

```javascript
const multiply = (a, b) => a * b;          // arrow
function makeCounter() {
  let count = 0;                            // 클로저가 캡처
  return () => ++count;
}
const next = makeCounter();
next(); next();                             // 1, 2 (상태 기억)
```

## 이론 (Theory)

### 1. 스코프, 호이스팅, TDZ

`let`/`const` 는 **블록 스코프**, `var` 는 **함수 스코프**. 선언은 끌어올려지지만(hoisting), `let`/`const` 는 선언 전 접근 시 **TDZ(temporal dead zone)** 에러. `var` 는 `undefined` 로 보여 버그를 숨긴다 → `let`/`const` 기본.

### 2. 클로저 = 렉시컬 환경 캡처

내부 함수는 외부 변수를 **참조로** 캡처한다(값 복사 아님). 이로써 **private 상태**(모듈 패턴)를 만들지만, 루프에서 `var` 로 만든 클로저는 최종 값을 공유하는 함정이 있다(`let` 은 반복마다 새 바인딩이라 안전).

### 3. `this` 바인딩 4규칙 + arrow

| 호출 방식 | `this` |
|---|---|
| 일반 호출 `f()` | undefined(strict) / global |
| 메서드 `o.f()` | `o` |
| `f.call(x)`/`apply`/`bind` | 명시한 `x` |
| `new F()` | 새 인스턴스 |

**arrow 함수는 자기 `this` 가 없다** — 정의된 곳의 렉시컬 `this` 를 그대로 쓴다(콜백에서 `this` 보존에 유용).

## 구현 (Implementation)

```javascript
const obj = {
  name: "A",
  greetLater() {
    setTimeout(function () { console.log(this.name); }, 0); // undefined ← 일반 호출
    setTimeout(() => console.log(this.name), 0);            // "A" ← arrow가 obj의 this 캡처
  },
};

for (var i = 0; i < 3; i++) setTimeout(() => console.log(i), 0); // 3 3 3 (var 공유)
for (let j = 0; j < 3; j++) setTimeout(() => console.log(j), 0); // 0 1 2 (let 새 바인딩)
```

## 복잡도 (Complexity)

| 항목 | 특성 |
|---|---|
| 함수 호출/클로저 생성 | 보통 작음, hot loop에서 누적 |
| 재귀 | 콜 스택 깊이 제한(엔진별), 일부만 꼬리 호출 최적화 |
| 캡처한 큰 객체 | 오래 살면 메모리 retention(누수 유사) |

## 응용 (Applications)

- 이벤트 핸들러, 배열 고차 함수(`map`/`filter`/`reduce`).
- 상태를 숨긴 도구(모듈 패턴), 비동기 콜백·커링.

## 흔한 오해 (Common Misunderstandings)

- **arrow는 자기 `this` 를 안 만든다** — 렉시컬 `this`.
- **`this` 는 호출 방식에 따라 달라진다** — 정의 위치가 아니다(arrow 제외).
- **`var` 루프 클로저는 최종 값을 공유** — `let` 사용.
- **호이스팅에 기대 선언 전 사용**은 가독성·TDZ 문제.

## TMI

- `bind`/`call`/`apply` 로 `this` 와 인자를 명시 제어한다(`call`=인자 나열, `apply`=배열).
- IIFE `(()=>{...})()` 는 모듈 시스템 이전에 private 스코프를 만드는 표준 기법이었다.
- 클로저가 캡처한 변수는 디버거의 "Scope > Closure"에서 직접 볼 수 있다.

## 연습 / 확인 문제 (Exercises)

- `makeCounter` 로 클로저가 상태를 기억함을 확인하라.
- `var`/`let` 루프 + `setTimeout` 의 출력 차이를 재현·설명하라.
- 일반 함수 콜백에서 `this` 가 깨지는 것을 arrow로 고쳐라.
- `bind` 로 부분 적용(partial application) 함수를 만들어라.

## 이어서 읽기 (Reading Path)

- 이전: [값과 타입 변환](JavaScript-Values-and-Coercion.md)
- 다음: [DOM과 이벤트](JavaScript-DOM-and-Events.md)
- 관련: [비동기 프로그래밍](JavaScript-Async.md)

## 참조 (References)

- [Programming/Functions-and-Recursion.md](../../Functions-and-Recursion.md)
- [Reference/Books.md](../../../Reference/Books.md)
