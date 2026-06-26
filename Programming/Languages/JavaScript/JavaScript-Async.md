# JavaScript 비동기 프로그래밍 (Async JavaScript)

- Level: Beginner
- Prerequisites: [JavaScript 함수와 스코프](JavaScript-Functions-and-Scope.md), [JavaScript DOM과 이벤트](JavaScript-DOM-and-Events.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

비동기 프로그래밍은 네트워크 요청, 타이머, 파일 작업처럼 시간이 걸리는 일을 기다리는 동안 프로그램이 멈추지 않게 다루는 방식이다. JavaScript는 callback, Promise, async/await를 사용한다.

## 직관 (Intuition)

음식을 주문하고 주방 앞에서 멈춰 서 있는 대신, 번호표를 받고 다른 일을 하다가 알림이 오면 결과를 받는 방식이다.

## 핵심 문법 (Core Syntax)

```javascript
async function loadUser() {
  try {
    const response = await fetch("/api/user");
    const user = await response.json();
    console.log(user.name);
  } catch (error) {
    console.error("failed to load user", error);
  }
}
```

`async` 함수는 Promise를 반환하고, `await`는 Promise가 settled될 때까지 해당 함수의 실행을 잠시 멈춘다.

## 이론 (Theory)

Event loop는 call stack, task queue, microtask queue를 조정한다. Promise callback은 microtask로 처리된다. 비동기는 병렬 실행과 같지 않으며, CPU를 오래 점유하는 작업은 UI를 막을 수 있다.

## 구현 (Implementation)

`async`/`await` 예제는 성공, 실패, timeout, cancellation 경로를 함께 작성한다. 독립 I/O는 `Promise.all`로 병렬화하되, 외부 API나 DB를 과부하시키지 않도록 concurrency limit을 둔다.

```javascript
function withTimeout(promise, ms) {
  const timeout = new Promise((_, reject) =>
    setTimeout(() => reject(new Error("timeout")), ms)
  );
  return Promise.race([promise, timeout]); // 성공 또는 timeout 중 먼저
}

async function main() {
  const results = await Promise.all([       // 독립 작업 병렬화
    Promise.resolve(1),
    Promise.resolve(2),
  ]);
  console.log(results); // [1, 2]
}
main();
```

## 복잡도 (Complexity)

비동기는 CPU 계산을 자동으로 빠르게 만들지 않고, 대기 시간을 겹쳐 체감 latency를 줄인다. pending promise가 많으면 memory와 queue 관리 비용이 늘고, blocking CPU 작업은 event loop 전체를 멈춘다.

## 응용 (Applications)

- API 호출
- 타이머와 사용자 이벤트 처리
- Node.js 파일·네트워크 작업
- 여러 요청 병렬 처리

## 흔한 오해 (Common Misunderstandings)

- `await`를 쓴다고 모든 코드가 병렬이 되는 것은 아니다.
- Promise rejection을 처리하지 않으면 숨은 오류가 된다.
- `forEach`와 `async` 조합은 의도한 순차 대기를 하지 않을 수 있다.
- CPU-heavy 작업은 비동기 함수로 감싼다고 가벼워지지 않는다.

## TMI

- `Promise.all`은 여러 작업을 동시에 시작하고 모두 완료될 때 기다린다.
- `AbortController`는 fetch 취소에 자주 쓰인다.
- Top-level await는 모듈 환경에서 사용할 수 있다.

## 연습 / 확인 문제 (Exercises)

- `fetch`로 JSON을 받아 화면에 표시하는 코드를 작성하라.
- `Promise.all`과 순차 `await`의 실행 시간을 비교하라.
- 실패하는 Promise를 `try/catch`로 처리하라.

## 이어서 읽기 (Reading Path)

- 이전: [DOM과 이벤트](JavaScript-DOM-and-Events.md)
- 다음: [Engineering/DevOps](../../../Engineering/DevOps/), [Testing](../../../Engineering/Testing/)

## 참조 (References)

- [Engineering/Performance/](../../../Engineering/Performance/)
- [Reference/Books.md](../../../Reference/Books.md)
