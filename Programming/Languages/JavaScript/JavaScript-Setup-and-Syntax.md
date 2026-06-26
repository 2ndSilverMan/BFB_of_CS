# JavaScript 실행 환경과 기본 문법

- Level: Beginner
- Prerequisites: [Programming/Variables-and-Types.md](../../Variables-and-Types.md), [Programming/Control-Flow.md](../../Control-Flow.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

JavaScript는 브라우저와 Node.js에서 실행되는 동적 타입 언어다. 웹 페이지 조작, 서버 코드, CLI 도구, 자동화까지 넓게 쓰인다.

## 직관 (Intuition)

브라우저에서 버튼을 누르면 화면이 바뀌는 대부분의 상호작용 뒤에는 JavaScript가 있다. Node.js를 쓰면 같은 언어로 서버나 도구도 만들 수 있다.

## 이론 (Theory)

JavaScript는 동적 타입, prototype 기반 객체, event loop를 가진 언어다. 브라우저와 Node.js에서 같은 핵심 언어를 쓰지만 제공되는 API와 module 실행 환경은 다를 수 있다.

## 핵심 문법 (Core Syntax)

```javascript
const name = "Ada";
let count = 0;

if (count === 0) {
  console.log(`Hello, ${name}`);
}

for (let i = 0; i < 3; i++) {
  console.log(i);
}
```

값이 바뀌지 않는 이름에는 `const`, 재할당이 필요한 이름에는 `let`을 우선 사용한다.

## 구현 (Implementation)

같은 문법을 Node.js와 브라우저 console에서 실행해 보고, 사용 가능한 API 차이를 구분한다. `let`/`const`, module import/export, strict mode, package script를 작은 파일로 확인한다.

```javascript
// add.mjs — 모듈로 분리해 export
export function add(a, b) {
  return a + b;
}

// main.mjs — 다른 모듈을 import
import { add } from "./add.mjs";
console.log(add(2, 3)); // 5
```

`.js` 확장자를 쓰려면 `package.json`에 `"type": "module"`을 명시한다.

## 복잡도 (Complexity)

JavaScript runtime은 JIT warmup, hidden class, garbage collection의 영향을 받는다. 브라우저에서는 DOM 접근과 layout/repaint가 단순 계산보다 훨씬 비쌀 수 있고, Node.js에서는 I/O 대기와 event loop 점유가 중요하다.

## 응용 (Applications)

- 웹 UI 동작 구현
- Node.js 서버와 스크립트
- JSON 데이터 처리
- 프론트엔드 프레임워크 학습 기반

## 흔한 오해 (Common Misunderstandings)

- JavaScript와 Java는 이름이 비슷하지만 별개 언어다.
- `==`는 암묵적 변환을 하므로 보통 `===`를 사용한다.
- `var`는 함수 스코프라 초보자에게 혼란을 만들 수 있다.
- 브라우저 API와 JavaScript 언어 자체는 구분해야 한다.

## TMI

- JavaScript는 매우 짧은 기간에 만들어져 역사적 특이점이 많다.
- ECMAScript는 JavaScript 표준 이름이다.
- 브라우저 콘솔은 작은 실험을 하기에 좋은 REPL이다.

## 연습 / 확인 문제 (Exercises)

- `let`과 `const`의 차이를 예제로 설명하라.
- `==`와 `===`가 다르게 동작하는 예를 찾아라.
- Node.js에서 파일 하나를 실행해 `console.log`를 출력하라.

## 이어서 읽기 (Reading Path)

- 이전: [변수와 타입](../../Variables-and-Types.md)
- 다음: [값과 타입 변환](JavaScript-Values-and-Coercion.md)

## 참조 (References)

- [Programming/Variables-and-Types.md](../../Variables-and-Types.md)
- [Reference/Books.md](../../../Reference/Books.md)
