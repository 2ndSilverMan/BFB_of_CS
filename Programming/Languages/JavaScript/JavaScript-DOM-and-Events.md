# JavaScript DOM과 이벤트 (DOM and Events)

- Level: Beginner
- Prerequisites: [JavaScript 함수와 스코프](JavaScript-Functions-and-Scope.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

DOM(Document Object Model)은 HTML 문서를 객체 트리로 표현한 브라우저 API다. 이벤트는 클릭, 입력, 로딩처럼 브라우저에서 발생하는 사건이며 JavaScript handler로 반응할 수 있다.

## 직관 (Intuition)

HTML이 화면의 뼈대라면 DOM은 JavaScript가 만질 수 있는 살아 있는 나무다. 버튼 클릭 같은 이벤트가 오면 나무의 일부를 바꾸어 화면을 갱신한다.

## 핵심 문법 (Core Syntax)

```javascript
const button = document.querySelector("#save");
const message = document.querySelector("#message");

button.addEventListener("click", () => {
  message.textContent = "Saved!";
});
```

사용자 입력은 신뢰하지 말고 필요한 경우 검증·escape를 적용한다.

## 이론 (Theory)

이벤트는 capture, target, bubble 단계를 거쳐 전파될 수 있다. DOM 변경은 layout과 paint 비용을 만들 수 있으므로 큰 변경은 묶어서 처리하는 편이 좋다.

## 구현 (Implementation)

DOM 변경은 query, event listener, state update를 분리해 작성한다. 반복되는 child element에는 event delegation을 고려하고, layout을 읽고 쓰는 작업을 섞지 않도록 작은 예제로 reflow를 관찰한다.

## 복잡도 (Complexity)

DOM query와 layout 계산은 문서 크기와 style 복잡도에 영향을 받는다. 많은 listener를 개별 node에 붙이면 memory와 관리 비용이 커지고, 잦은 DOM write는 layout thrashing을 만들 수 있다.

## 응용 (Applications)

- 버튼과 폼 상호작용
- 동적 UI 갱신
- 간단한 브라우저 앱
- 접근성 상태 반영

## 흔한 오해 (Common Misunderstandings)

- `innerHTML`에 사용자 입력을 넣으면 XSS 위험이 있다.
- DOM 요소가 아직 로드되기 전에 선택하면 `null`이 나올 수 있다.
- 이벤트 handler 안의 `this`는 함수 형태에 따라 달라질 수 있다.
- 화면에 보이는 것과 DOM 상태가 항상 같지는 않다.

## TMI

- Event delegation은 부모에 handler를 달아 많은 자식 이벤트를 처리하는 패턴이다.
- `data-*` attribute는 DOM에 작은 메타데이터를 붙일 때 편리하다.
- 현대 프레임워크는 DOM 변경을 추상화하지만 기본 원리는 여전히 중요하다.

## 연습 / 확인 문제 (Exercises)

- 버튼 클릭 시 카운터가 증가하는 페이지를 만들어라.
- 폼 입력값을 읽어 화면에 출력하라.
- `textContent`와 `innerHTML`의 보안 차이를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [함수와 스코프](JavaScript-Functions-and-Scope.md)
- 다음: [비동기 프로그래밍](JavaScript-Async.md)

## 참조 (References)

- [Engineering/Security/Web-Security.md](../../../Engineering/Security/Web-Security.md)
- [Reference/Books.md](../../../Reference/Books.md)
