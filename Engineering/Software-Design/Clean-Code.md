# 클린 코드 (Clean Code)

- Level: Intermediate
- Prerequisites: [Engineering/Software-Design/SOLID.md](SOLID.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

클린 코드는 독자가 의도와 invariant를 빠르게 이해하고 안전하게 변경할 수 있는 코드다. 명명, 작은 응집 단위, 명시적 error handling, 일관성, test와 자동화된 formatter가 핵심 수단이다.

## 직관 (Intuition)

코드는 쓰는 시간보다 읽히는 시간이 길다. 짧음 자체보다 surprise가 적고 domain language와 control flow가 분명한 것이 중요하다.

## 이론 (Theory)

좋은 이름은 역할·단위·범위를 나타내며 comment는 "무엇"을 반복하기보다 "왜"와 제약을 남긴다. 함수는 하나의 abstraction level에서 cohesive task를 수행하고, hidden side effect와 boolean flag를 줄인다. Error를 삼키지 않고 context와 복구 책임을 명확히 한다.

Cleanliness는 보편적 줄 수 규칙이 아니라 team convention, language idiom, domain risk에 따른 품질 속성이다.

## 구현 (Implementation)

```python
def calculate_invoice_total(line_items, tax_rate):
    subtotal = sum(item.unit_price * item.quantity for item in line_items)
    tax = subtotal * tax_rate
    return subtotal + tax
```

`calc(x, r)`보다 domain 의미와 단위를 드러낸다.

## 복잡도 (Complexity)

성능 Big-O와 별개로 cognitive complexity를 낮춘다. 과도한 함수 분해와 indirection은 탐색 비용을 오히려 늘릴 수 있다.

## 응용 (Applications)

- code review·onboarding
- defect 예방과 refactoring
- public API·library
- long-lived business code

## 흔한 오해 (Common Misunderstandings)

- 짧은 함수가 항상 읽기 좋은 것은 아니다.
- comment를 모두 없애는 것이 목표가 아니다.
- clever one-liner가 명확한 loop보다 우월하지 않다.
- 스타일 통일만으로 architecture 문제를 해결하지 못한다.

## TMI

- formatter는 미학 논쟁을 자동화하고 review를 behavior에 집중시킨다.
- 단위가 포함된 이름은 money·time bug를 줄인다.
- 삭제 가능한 code가 가장 유지보수하기 쉬운 code라는 관점도 있다.

## 연습 / 확인 문제 (Exercises)

- 의미 없는 이름과 중첩 조건문을 refactor하라.
- 유용한 "왜" comment와 불필요한 comment를 구분하라.
- 함수 분해가 지나친 사례를 다시 응집하라.

## 이어서 읽기 (Reading Path)

- 이전: [SOLID](SOLID.md)
- 다음: [리팩토링](Refactoring.md)

## 참조 (References)

- [Engineering/Software-Design/SOLID.md](SOLID.md)
- [Reference/Books.md](../../Reference/Books.md)
