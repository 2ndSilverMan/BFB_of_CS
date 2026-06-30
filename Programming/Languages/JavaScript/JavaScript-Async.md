# JavaScript 비동기 프로그래밍 (Async JavaScript)

- Level: Beginner
- Prerequisites: [JavaScript 함수와 스코프](JavaScript-Functions-and-Scope.md), [JavaScript DOM과 이벤트](JavaScript-DOM-and-Events.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

비동기 프로그래밍은 네트워크·타이머·파일처럼 시간이 걸리는 일을 **기다리는 동안 멈추지 않게** 다룬다. JavaScript는 단일 스레드 + **이벤트 루프**로 callback → Promise → async/await 순으로 발전했다.

## 직관 (Intuition)

음식을 주문하고 주방 앞에 서 있는 대신, 번호표를 받고 다른 일을 하다 알림이 오면 받는다. 핵심은 **"비동기 ≠ 병렬"** — 한 스레드가 대기 시간을 *겹쳐서* 처리할 뿐이라, CPU를 오래 쥐는 작업은 루프 전체를 막는다.

## 핵심 문법 (Core Syntax)

```javascript
async function loadUser() {
  try {
    const res = await fetch("/api/user");   // settled까지 이 함수만 일시정지
    return await res.json();
  } catch (err) {
    console.error("failed", err);
  }
}
```

`async` 함수는 항상 Promise를 반환하고, `await` 는 그 함수의 진행만 멈춘다(전체 프로그램 아님).

## 이론 (Theory)

### 1. 이벤트 루프: 콜 스택 + 태스크 + 마이크로태스크

콜 스택이 비면 루프는 **마이크로태스크 큐(Promise 콜백)를 모두 비운 뒤** 매크로태스크(setTimeout, I/O) 하나를 꺼낸다. 그래서 **Promise 콜백이 `setTimeout(…,0)` 보다 먼저** 실행된다.

### 2. Promise 상태와 합성

Promise는 `pending → fulfilled | rejected`(한 번만 settle). 합성:

- `Promise.all` — 모두 성공 시 배열, 하나라도 실패 시 즉시 reject.
- `Promise.allSettled` — 성패 무관 전부 기다림.
- `Promise.race` — 가장 먼저 settle된 것(타임아웃 패턴).

### 3. async/await는 Promise의 문법설탕

`await p` 는 "`p.then(...)` 의 나머지"를 마이크로태스크로 예약하는 것과 같다. 그래서 직관적이지만 **순차 await는 직렬화**된다 — 독립 작업은 `Promise.all` 로 병렬화.

## 구현 (Implementation)

```javascript
function withTimeout(promise, ms) {
  const t = new Promise((_, rej) => setTimeout(() => rej(new Error("timeout")), ms));
  return Promise.race([promise, t]);                 // 성공 또는 타임아웃
}

// 순차 vs 병렬
const a = await f1(); const b = await f2();           // 직렬: t1 + t2
const [c, d] = await Promise.all([f1(), f2()]);       // 병렬: max(t1, t2)

// forEach 함정: 대기하지 않음 → for...of 사용
for (const url of urls) { await fetch(url); }         // 순차 보장
```

실행 순서: `console.log("A"); setTimeout(()=>log("B"),0); Promise.resolve().then(()=>log("C")); log("D")` → **A D C B**(동기 → 마이크로태스크 C → 매크로태스크 B).

## 복잡도 (Complexity)

| 항목 | 특성 |
|---|---|
| 비동기 | CPU를 빠르게 안 함 — 대기 시간 중첩으로 체감 latency↓ |
| pending Promise 다수 | 메모리·큐 관리 비용 |
| blocking CPU 작업 | 이벤트 루프 전체 정지(UI 멈춤) → Web Worker로 분리 |

## 응용 (Applications)

- API 호출·타이머·사용자 이벤트, Node.js 파일·네트워크.
- 독립 요청 병렬화(`Promise.all`), 동시성 제한(외부 과부하 방지).

## 흔한 오해 (Common Misunderstandings)

- **`await` 가 코드를 병렬로 만들지 않는다** — 독립 작업은 `Promise.all`.
- **rejection 미처리는 숨은 오류**(`unhandledRejection`) — 항상 catch.
- **`forEach` + `async` 는 대기하지 않는다** — `for...of` 또는 `map`+`Promise.all`.
- **CPU-heavy를 async로 감싸도 가벼워지지 않는다** — 루프를 막는다.

## TMI

- `AbortController` 로 fetch·이벤트를 취소한다(타임아웃·중복 요청 정리).
- 모듈 환경의 top-level `await` 로 import 시점에 비동기 초기화를 한다.
- `queueMicrotask` 로 직접 마이크로태스크를 예약할 수 있다(렌더 전 정리 작업 등).

## 연습 / 확인 문제 (Exercises)

- `console.log` + `setTimeout(0)` + `Promise.then` 의 출력 순서를 예측·검증하라(A D C B).
- 순차 `await` 와 `Promise.all` 의 총 시간을 비교하라.
- 실패하는 Promise를 `try/catch` 와 `.catch` 두 방식으로 처리하라.
- `Promise.race` 로 타임아웃을 구현하라.

## 이어서 읽기 (Reading Path)

- 이전: [DOM과 이벤트](JavaScript-DOM-and-Events.md)
- 다음: [비동기 I/O](../../../Engineering/Performance/Async-IO.md)
- 관련: [함수와 스코프](JavaScript-Functions-and-Scope.md)

## 참조 (References)

- [Engineering/Performance/Async-IO.md](../../../Engineering/Performance/Async-IO.md)
- [Reference/Books.md](../../../Reference/Books.md)
