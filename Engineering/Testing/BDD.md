# BDD (Behavior-Driven Development)

- Level: Intermediate
- Prerequisites: [Engineering/Testing/TDD.md](TDD.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

BDD는 시스템의 행동을 사용자와 비즈니스 언어로 표현하고, 그 행동을 테스트 가능한 시나리오로 연결하는 개발 방식이다. Given-When-Then 형식이 자주 쓰인다.

## 직관 (Intuition)

테스트를 개발자만 아는 함수 이름이 아니라 "이런 상황에서 사용자가 이렇게 하면 이런 결과가 나와야 한다"는 이야기로 쓴다.

## 이론 (Theory)

BDD는 요구사항 발견과 커뮤니케이션에 초점이 있다. Acceptance criteria를 명확히 하고, 예시를 통해 모호성을 줄인다. 자동화는 중요하지만, 시나리오가 너무 UI 세부사항에 묶이면 취약해진다.

## 구현 (Implementation)

```gherkin
Given 사용자가 장바구니에 상품을 담았다
When 결제를 완료한다
Then 주문이 생성되고 확인 이메일이 발송된다
```

## 복잡도 (Complexity)

시나리오 수가 늘면 유지보수 비용이 커진다. 핵심 사용자 행동 중심으로 유지하고 세부 조합은 더 낮은 테스트 층으로 내린다.

## 응용 (Applications)

- 제품 요구사항 합의
- 인수 테스트
- QA와 개발자 커뮤니케이션
- 도메인 규칙 문서화

## 흔한 오해 (Common Misunderstandings)

- BDD는 Gherkin 문법을 쓰는 것만을 의미하지 않는다.
- 모든 단위 테스트를 Given-When-Then으로 바꿀 필요는 없다.
- 시나리오가 너무 기술적이면 비즈니스 대화 도구가 되지 못한다.
- UI 자동화와 BDD는 같은 말이 아니다.

## TMI

- Specification by Example은 BDD와 잘 맞는 요구사항 발견 방식이다.
- Living documentation은 테스트와 문서가 함께 유지되는 이상을 말한다.
- 좋은 BDD 시나리오는 구현보다 행동을 설명한다.

## 연습 / 확인 문제 (Exercises)

- 로그인 실패 시나리오를 Given-When-Then으로 작성하라.
- 너무 기술적인 BDD 문장을 사용자 관점으로 바꿔라.
- BDD 시나리오와 단위 테스트의 역할 차이를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [TDD](TDD.md)
- 다음: [E2E 테스트](E2E-Testing.md)

## 참조 (References)

- [Engineering/Testing/TDD.md](TDD.md)
- [Reference/Books.md](../../Reference/Books.md)
