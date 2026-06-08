# JavaScript 학습 트랙 (JavaScript)

> 웹 브라우저와 Node.js에서 동작하는 언어로, UI 상호작용과 비동기 프로그래밍을 익히는 언어 트랙.

**선수지식**: [Programming/](../../), [조건문과 반복문](../../Control-Flow.md), [함수와 재귀](../../Functions-and-Recursion.md)

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

| Order | 주제 | 파일 | 설명 | Status |
|---|---|---|---|---|
| 1 | 실행 환경과 기본 문법 | JavaScript-Setup-and-Syntax.md | 브라우저 콘솔, Node.js, 변수 선언, 기본 입출력 | Planned |
| 2 | 값과 타입 변환 | JavaScript-Values-and-Coercion.md | `null`, `undefined`, truthy/falsy, 암묵적 변환 | Planned |
| 3 | 함수와 스코프 | JavaScript-Functions-and-Scope.md | function, arrow function, closure, lexical scope | Planned |
| 4 | DOM과 이벤트 | JavaScript-DOM-and-Events.md | HTML 요소 선택, 이벤트 처리, 브라우저 API | Planned |
| 5 | 비동기 프로그래밍 | JavaScript-Async.md | callback, Promise, async/await, fetch | Planned |

---

## 학습 순서

```text
JavaScript-Setup-and-Syntax -> JavaScript-Values-and-Coercion
        ↓
JavaScript-Functions-and-Scope -> JavaScript-DOM-and-Events -> JavaScript-Async
```

---

## TMI

- JavaScript와 Java는 이름이 비슷하지만 같은 계열 언어가 아니다. 초창기 웹 시대의 마케팅과 역사적 사정 때문에 이름이 이렇게 굳었다.
- `[] + []`는 빈 문자열이 되고, `[] + {}` 같은 표현은 실행 위치와 파싱 방식에 따라 이상해 보이는 결과가 나올 수 있다. 장난감 예제 같지만 타입 변환 규칙을 이해하는 데는 도움이 된다.
- `NaN`은 자기 자신과도 같지 않다. 그래서 `NaN === NaN`은 `false`이고, 보통 `Number.isNaN()`으로 검사한다.
- `setTimeout(fn, 0)`은 "즉시 실행"이 아니라 현재 실행 스택이 비고 이벤트 루프가 다음 작업을 처리할 때 실행하겠다는 뜻에 가깝다.

---

## 연관 섹션

- [Programming/](../../) - 언어 공통 개념
- [Engineering/Software-Design/](../../../Engineering/Software-Design/) - 프론트엔드/백엔드 코드 구조화
- [Engineering/Testing/](../../../Engineering/Testing/) - JavaScript 애플리케이션 테스트
