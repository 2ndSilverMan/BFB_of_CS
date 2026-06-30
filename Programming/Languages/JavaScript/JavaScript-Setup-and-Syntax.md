# JavaScript 실행 환경과 기본 문법

- Level: Beginner
- Prerequisites: [Programming/Variables-and-Types.md](../../Variables-and-Types.md), [Programming/Control-Flow.md](../../Control-Flow.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

JavaScript는 **브라우저와 Node.js의 단일 스레드 + 이벤트 루프** 위에서 도는 동적 타입·**프로토타입 기반** 언어다. 언어 자체(ECMAScript)와 **호스트 API**(DOM, Node `fs`)는 분리해서 봐야 한다 — 같은 언어라도 환경마다 제공 API가 다르다.

## 직관 (Intuition)

버튼을 눌러 화면이 바뀌는 상호작용 뒤엔 대개 JS가 있다. Node.js를 쓰면 같은 언어로 서버·도구도 만든다. 핵심은 "언어 코어 vs 환경 API"를 구분하는 것 — `Array.map` 은 어디서나 되지만 `document`/`fs` 는 환경 전용.

## 핵심 문법 (Core Syntax)

```javascript
const name = "Ada";          // 재할당 금지(바인딩 고정, 객체 내부는 변경 가능)
let count = 0;               // 재할당 가능, 블록 스코프
if (count === 0) console.log(`Hello, ${name}`);
for (let i = 0; i < 3; i++) console.log(i);
```

## 이론 (Theory)

### 1. 모듈 시스템 (ESM vs CommonJS)

브라우저·현대 Node는 **ESM**(`import`/`export`, 정적·비동기 로드). 구형 Node는 **CommonJS**(`require`/`module.exports`, 동기). `.js` 를 ESM으로 쓰려면 `package.json` 의 `"type": "module"` 또는 `.mjs`. 둘은 로딩 시점·`this`·top-level await가 달라 섞으면 문제가 생긴다.

### 2. strict mode와 런타임

`"use strict"`(ESM은 기본 strict)는 조용한 오류를 예외로 바꾼다. 엔진(V8 등)은 **JIT 컴파일 + hidden class + GC** 로 동작 — 객체 속성 구조를 일관되게 유지하면 hidden class가 안정돼 빠르다.

### 3. `const` 의 의미

`const` 는 **바인딩**을 고정할 뿐 값을 얼리지 않는다 → `const a=[]; a.push(1)` 은 합법. 불변이 필요하면 `Object.freeze`.

## 구현 (Implementation)

```javascript
// add.mjs
export function add(a, b) { return a + b; }   // ESM export
// main.mjs
import { add } from "./add.mjs";              // 정적 import
console.log(add(2, 3));                        // 5

const cfg = Object.freeze({ retries: 3 });     // 얕은 불변
```

## 복잡도 (Complexity)

| 항목 | 특성 |
|---|---|
| JIT warmup | 처음엔 느리고 hot 코드가 최적화됨 |
| hidden class | 속성 추가 순서가 일관돼야 빠름 |
| 브라우저 DOM/layout | 단순 계산보다 훨씬 비쌈 |
| Node I/O | 이벤트 루프 점유·대기가 핵심 |

## 응용 (Applications)

- 웹 UI 동작, Node.js 서버·스크립트, JSON 처리.
- 프론트엔드 프레임워크(React/Vue) 학습 기반.

## 흔한 오해 (Common Misunderstandings)

- **JavaScript ≠ Java** — 이름만 비슷한 별개 언어.
- **`==` 는 암묵 변환** — 보통 `===`.
- **`const` 는 값을 얼리지 않는다** — 바인딩만 고정.
- **`var` 는 함수 스코프** — 혼란의 원천, `let`/`const` 기본.
- **언어 코어와 호스트 API 혼동** — `document` 는 브라우저 전용.

## TMI

- JavaScript는 1995년 약 10일 만에 설계돼 역사적 특이점이 많다(`typeof null` 등).
- ECMAScript는 표준 이름이고, ES2015(ES6)가 `let`/`const`/화살표/클래스/모듈을 들여온 분기점.
- 브라우저 콘솔은 즉석 실험용 REPL로 훌륭하다.

## 연습 / 확인 문제 (Exercises)

- `let`/`const` 차이와 "`const` 객체 변경 가능"을 예제로 보여라.
- ESM `export`/`import` 로 모듈을 분리해 실행하라.
- `==` 와 `===` 가 다르게 동작하는 예를 찾아라.
- `Object.freeze` 전후로 객체 변경 시도 결과를 비교하라(strict).

## 이어서 읽기 (Reading Path)

- 이전: [변수와 타입](../../Variables-and-Types.md)
- 다음: [값과 타입 변환](JavaScript-Values-and-Coercion.md)
- 관련: [함수와 스코프](JavaScript-Functions-and-Scope.md)

## 참조 (References)

- [Programming/Variables-and-Types.md](../../Variables-and-Types.md)
- [Reference/Books.md](../../../Reference/Books.md)
