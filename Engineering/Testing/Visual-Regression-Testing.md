# 시각적 회귀 테스트 (Visual Regression Testing)

- Level: Intermediate
- Prerequisites: [Engineering/Testing/UI-Test-Tools.md](UI-Test-Tools.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

시각적 회귀 테스트는 화면 screenshot이나 component render 결과를 baseline과 비교해 의도치 않은 UI 변화가 생겼는지 확인하는 테스트다.

## 직관 (Intuition)

기능은 동작하지만 버튼이 밀리거나 글자가 겹칠 수 있다. 시각적 회귀 테스트는 눈으로 보던 화면 비교를 자동화한다.

## 이론 (Theory)

Pixel diff는 민감하지만 font, anti-aliasing, viewport, OS 차이에 흔들린다. Threshold, mask, deterministic data, 고정 viewport, screenshot artifact review가 필요하다.

### 시각 차이의 노이즈 관리

Visual regression은 픽셀 차이를 찾지만 모든 차이가 결함은 아니다. 폰트 렌더링, anti-aliasing, 애니메이션, 날짜/랜덤 데이터, viewport 차이가 false positive를 만든다. 안정적인 seed, 고정된 clock, animation disable, threshold 정책이 필요하다.

시각 테스트는 핵심 컴포넌트와 대표 viewport를 골라 운영한다. 모든 페이지 전체 스크린샷을 무차별로 찍으면 승인 비용이 커지고 중요한 회귀를 놓치기 쉽다.

## 구현 (Implementation)

```text
render page -> take screenshot -> compare with approved baseline -> review diff
```

Baseline 변경은 코드 리뷰처럼 의도 여부를 확인하고 승인한다.

## 복잡도 (Complexity)

스크린샷 수가 늘면 저장소 용량과 리뷰 비용이 증가한다. 환경 차이를 줄이지 않으면 false positive가 많아진다.

## 응용 (Applications)

- 디자인 시스템 component 회귀
- responsive layout 확인
- PDF/이메일 template 검증
- 중요 landing page 보호

## 흔한 오해 (Common Misunderstandings)

- Pixel-perfect 비교가 항상 좋은 것은 아니다.
- Baseline을 무비판적으로 업데이트하면 테스트 의미가 사라진다.
- 기능 테스트를 시각 테스트로 대체할 수 없다.
- 동적 데이터와 시간은 screenshot을 불안정하게 만든다.

## TMI

- Storybook 기반 component screenshot 테스트가 자주 쓰인다.
- Animation은 끄거나 특정 frame으로 고정해야 한다.
- Visual diff는 디자이너와 QA가 함께 리뷰하기 좋은 artifact다.

## 연습 / 확인 문제 (Exercises)

- 시각 테스트를 안정화하기 위한 환경 고정 항목을 나열하라.
- Baseline 승인 절차를 설계하라.
- 시각 테스트로 잡을 수 없는 버그 예를 들어라.

## 이어서 읽기 (Reading Path)

- 이전: [UI 테스트 도구](UI-Test-Tools.md)
- 다음: [코드 커버리지](Code-Coverage.md)

## 참조 (References)

- [Engineering/Testing/E2E-Testing.md](E2E-Testing.md)
- [Reference/Books.md](../../Reference/Books.md)
