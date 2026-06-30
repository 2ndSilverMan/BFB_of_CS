# JavaScript DOM과 이벤트 (DOM and Events)

- Level: Beginner
- Prerequisites: [JavaScript 함수와 스코프](JavaScript-Functions-and-Scope.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

DOM(Document Object Model)은 HTML 문서를 **객체 트리**로 표현한 브라우저 API다. 이벤트는 클릭·입력·로딩처럼 발생하는 사건이며, **capture→target→bubble** 전파 모델로 핸들러에 전달된다.

## 직관 (Intuition)

HTML이 화면의 뼈대라면 DOM은 JS가 만질 수 있는 **살아 있는 나무**다. 이벤트가 오면 나무의 일부를 바꿔 화면을 갱신한다. 성능의 핵심은 "JS 실행"이 아니라 **layout(reflow)·paint** 가 비싸다는 것 — DOM 쓰기를 묶어야 한다.

## 핵심 문법 (Core Syntax)

```javascript
const button = document.querySelector("#save");
const msg = document.querySelector("#message");
button.addEventListener("click", () => { msg.textContent = "Saved!"; });
```

## 이론 (Theory)

### 1. 이벤트 전파와 위임(delegation)

이벤트는 **capture**(루트→타겟) → **target** → **bubble**(타겟→루트) 단계를 거친다. 그래서 **부모 하나에 핸들러를 달아** 많은 자식 이벤트를 처리하는 **event delegation** 이 가능하다(동적 목록에 특히 유용, 메모리·관리 절감).

### 2. layout thrashing

DOM **읽기**(`offsetHeight` 등)는 보류된 변경을 반영하려 **강제 동기 layout**을 유발한다. 루프에서 읽기↔쓰기를 번갈아 하면 매번 reflow가 일어나는 **layout thrashing** → 읽기를 모은 뒤 쓰기를 모으거나 `requestAnimationFrame` 으로 배치.

### 3. XSS와 textContent

`innerHTML` 에 사용자 입력을 넣으면 스크립트가 실행될 수 있다(**XSS**) → 텍스트는 `textContent`, HTML이 꼭 필요하면 sanitize([웹 보안](../../../Engineering/Security/Web-Security.md)).

## 구현 (Implementation)

```javascript
const list = document.querySelector("#todos");
// 항목마다 listener를 달지 않고 부모에서 한 번 (event delegation)
list.addEventListener("click", (e) => {
  const item = e.target.closest("li");        // 클릭된 가장 가까운 li
  if (item) item.classList.toggle("done");
});

// 배치 쓰기로 reflow 최소화
const frag = document.createDocumentFragment();
for (const t of todos) {
  const li = document.createElement("li");
  li.textContent = t;                          // textContent: XSS 안전
  frag.appendChild(li);
}
list.appendChild(frag);                        // DOM 삽입 1회
```

## 복잡도 (Complexity)

| 항목 | 특성 |
|---|---|
| `querySelector`/layout | 문서 크기·스타일 복잡도에 비례 |
| 개별 노드마다 listener | 메모리·관리 비용 ↑ → delegation |
| 잦은 DOM write | layout thrashing(reflow 폭발) |
| DocumentFragment 삽입 | reflow 1회로 묶음 |

## 응용 (Applications)

- 버튼·폼 상호작용, 동적 UI 갱신, 접근성 상태(`aria-*`) 반영.
- 간단한 브라우저 앱, 프레임워크의 기반 원리.

## 흔한 오해 (Common Misunderstandings)

- **`innerHTML` + 사용자 입력 = XSS** — `textContent` 또는 sanitize.
- **로드 전 선택은 `null`** — `DOMContentLoaded` 후 또는 스크립트를 끝에.
- **핸들러 안 `this` 는 호출 방식에 의존** — arrow면 렉시컬.
- **화면과 DOM 상태가 항상 같지 않다** — 보류된 layout/CSS 상태.

## TMI

- `data-*` 속성은 DOM에 작은 메타데이터를 붙인다(`el.dataset`).
- 가상 DOM(React)은 변경을 모아 실제 DOM 쓰기를 최소화하는 추상화 — 원리는 위 배치와 같다.
- `passive: true` 리스너는 스크롤 성능을 위해 `preventDefault` 를 포기한다고 브라우저에 알린다.

## 연습 / 확인 문제 (Exercises)

- 버튼 클릭 시 카운터가 증가하는 페이지를 만들어라.
- event delegation으로 동적 목록의 클릭을 부모에서 처리하라.
- `textContent` 와 `innerHTML` 의 XSS 차이를 사용자 입력으로 보여라.
- 읽기↔쓰기를 번갈아 하는 코드의 reflow를 DevTools로 관찰하고 배치로 고쳐라.

## 이어서 읽기 (Reading Path)

- 이전: [함수와 스코프](JavaScript-Functions-and-Scope.md)
- 다음: [비동기 프로그래밍](JavaScript-Async.md)
- 관련: [웹 보안](../../../Engineering/Security/Web-Security.md)

## 참조 (References)

- [Engineering/Security/Web-Security.md](../../../Engineering/Security/Web-Security.md)
- [Reference/Books.md](../../../Reference/Books.md)
