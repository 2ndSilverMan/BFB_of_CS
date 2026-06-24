# UI 테스트 도구 (Selenium, Playwright, Cypress)

- Level: Intermediate
- Prerequisites: [Engineering/Testing/E2E-Testing.md](E2E-Testing.md), [Programming/Languages/JavaScript/JavaScript-DOM-and-Events.md](../../Programming/Languages/JavaScript/JavaScript-DOM-and-Events.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

UI 테스트 도구는 브라우저를 자동화해 사용자의 클릭, 입력, 이동, 화면 검증을 수행한다. Selenium, Playwright, Cypress는 대표적인 브라우저 자동화/테스트 도구다.

## 직관 (Intuition)

사람이 매번 브라우저를 열고 버튼을 누르는 일을 스크립트가 대신한다. 다만 화면은 timing과 환경에 민감하므로 안정적인 selector와 대기 전략이 중요하다.

## 이론 (Theory)

좋은 UI 테스트는 사용자 관점의 stable locator를 사용하고, 네트워크·애니메이션·비동기 렌더링을 명시적으로 기다린다. Page object나 screen object 패턴은 반복 조작을 캡슐화한다.

## 구현 (Implementation)

```javascript
await page.getByRole("button", { name: "Save" }).click();
await expect(page.getByText("Saved")).toBeVisible();
```

구현 세부 CSS보다 접근성 role이나 테스트 전용 id를 쓰는 편이 안정적이다.

## 복잡도 (Complexity)

브라우저 테스트는 느리고 resource를 많이 쓴다. 병렬 실행은 격리된 계정, 독립 데이터, 안정적인 환경이 필요하다.

## 응용 (Applications)

- 핵심 UI flow 검증
- 크로스 브라우저 확인
- 배포 전 smoke test
- 회귀 재현 자동화

## 흔한 오해 (Common Misunderstandings)

- UI 테스트 도구가 flaky 문제를 자동으로 해결하지 않는다.
- CSS selector를 깊게 타면 UI 리팩터링에 쉽게 깨진다.
- 실제 사용자를 완전히 대체할 수는 없다.
- 모든 validation을 UI 테스트로만 확인하면 비용이 크다.

## TMI

- Headless mode는 CI에서 브라우저 UI 없이 실행할 때 유용하다.
- Trace viewer는 실패한 UI 테스트의 단계별 상태를 보는 데 좋다.
- Accessibility-friendly selector는 테스트와 접근성을 동시에 돕는다.

## 연습 / 확인 문제 (Exercises)

- 로그인 버튼 클릭 테스트를 작성하라.
- Flaky selector를 stable selector로 바꿔라.
- Page object 패턴의 장단점을 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [E2E 테스트](E2E-Testing.md)
- 다음: [시각적 회귀 테스트](Visual-Regression-Testing.md)

## 참조 (References)

- [Programming/Languages/JavaScript/JavaScript-DOM-and-Events.md](../../Programming/Languages/JavaScript/JavaScript-DOM-and-Events.md)
- [Reference/Books.md](../../Reference/Books.md)
