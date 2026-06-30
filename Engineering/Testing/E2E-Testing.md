# E2E 테스트 (End-to-End Testing)

- Level: Intermediate
- Prerequisites: [Engineering/Testing/Testing-Pyramid.md](Testing-Pyramid.md), [Engineering/Testing/Integration-Test-Strategy.md](Integration-Test-Strategy.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

E2E 테스트는 사용자의 핵심 흐름을 실제 시스템에 가깝게 통과시키는 테스트다. 로그인, 검색, 결제, 주문 확인처럼 여러 계층을 함께 검증한다.

## 직관 (Intuition)

부품 테스트가 모두 통과해도 자동차가 실제 도로에서 움직이는지는 따로 봐야 한다. E2E는 전체 경험이 이어지는지 확인하는 마지막 안전망이다.

## 이론 (Theory)

E2E는 confidence가 높지만 느리고 flaky하기 쉽다. 테스트 데이터, 외부 의존성, 브라우저 timing, 네트워크 상태를 통제해야 한다. 핵심 journey만 적게 유지하고, 세부 경우의 수는 낮은 층 테스트로 내린다.

### E2E의 범위 통제

E2E 테스트는 가장 현실적이지만 가장 비싸고 취약하다. 그래서 모든 edge case를 E2E로 올리기보다 로그인, 결제, 권한, 데이터 생성처럼 사용자의 신뢰에 직결되는 대표 journey를 선택한다. 실패 원인이 backend, frontend, network, data 중 어디인지 빠르게 좁힐 수 있도록 trace와 screenshot, network log를 함께 남긴다.

Flaky E2E는 제품 신뢰를 갉아먹는다. 단순 retry로 숨기지 말고 원인을 time, async wait, shared data, external dependency, browser variance로 분류해 수정한다.

## 구현 (Implementation)

```text
Given 새 사용자가 가입했다
When 상품을 장바구니에 넣고 결제한다
Then 주문 상세 페이지에서 결제 완료를 볼 수 있다
```

## 복잡도 (Complexity)

실행 시간은 환경 준비, 브라우저 자동화, 네트워크, 데이터 reset 비용의 합이다. 병렬화하려면 사용자 계정과 테스트 데이터를 격리해야 한다.

## 응용 (Applications)

- 핵심 사용자 여정 검증
- release smoke test
- 여러 서비스 통합 확인
- regression 방지

## 흔한 오해 (Common Misunderstandings)

- 모든 버그를 E2E로 잡으려 하면 suite가 느리고 불안정해진다.
- Sleep 기반 대기는 flaky test의 원인이 된다.
- UI 문구나 CSS에 과도하게 의존하면 유지보수가 어렵다.
- E2E 실패는 원인 위치를 바로 알려주지 않는다.

## TMI

- Smoke test는 배포 후 가장 중요한 경로만 빠르게 확인한다.
- Test data factory는 E2E 데이터 준비를 안정화한다.
- Screenshot/video artifact는 실패 분석에 큰 도움이 된다.

## 연습 / 확인 문제 (Exercises)

- 쇼핑몰의 E2E 핵심 경로 3개를 고르라.
- Flaky E2E test 원인을 timing/data/environment로 분류하라.
- E2E에서 확인할 것과 unit test로 내릴 것을 구분하라.

## 이어서 읽기 (Reading Path)

- 이전: [테스트 피라미드](Testing-Pyramid.md)
- 다음: [UI 테스트 도구](UI-Test-Tools.md), [시각적 회귀 테스트](Visual-Regression-Testing.md)

## 참조 (References)

- [Engineering/Testing/Testing-Pyramid.md](Testing-Pyramid.md)
- [Reference/Books.md](../../Reference/Books.md)
