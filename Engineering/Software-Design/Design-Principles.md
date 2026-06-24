# DRY / KISS / YAGNI 설계 원칙

- Level: Intermediate
- Prerequisites: [Programming/OOP.md](../../Programming/OOP.md), [Engineering/Software-Design/Clean-Code.md](Clean-Code.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

DRY, KISS, YAGNI는 소프트웨어 설계에서 복잡도와 중복을 줄이는 실용 원칙이다. DRY는 지식의 중복을 줄이고, KISS는 설계를 단순하게 유지하며, YAGNI는 지금 필요하지 않은 기능을 미리 만들지 말라는 원칙이다.

## 직관 (Intuition)

좋은 설계는 멋진 구조를 많이 넣는 것이 아니라, 바뀌는 부분을 작게 만들고 읽는 사람이 쉽게 따라오게 하는 것이다. 중복된 규칙은 한 곳에서 고치기 어렵고, 과한 추상화는 아직 오지도 않은 미래를 위해 현재를 복잡하게 만든다.

## 이론 (Theory)

DRY의 핵심은 코드 줄 중복이 아니라 지식 중복이다. 같은 비즈니스 규칙이 여러 곳에 흩어져 있으면 한 규칙 변경이 여러 수정으로 번진다.

KISS는 단순한 해결책을 선호한다. 단순함은 기능 부족이 아니라, 문제를 해결하는 데 필요한 개념 수와 의존성을 줄이는 것이다.

YAGNI는 speculative generality를 경계한다. 미래에 필요할 것 같은 확장 포인트를 미리 만들면 실제 요구사항과 어긋난 추상화가 생길 수 있다.

## 구현 (Implementation)

중복 제거는 의미가 같은 규칙을 함수로 추출할 때 효과가 크다.

```python
def is_free_shipping(order_total):
    return order_total >= 50_000


def shipping_fee(order_total):
    return 0 if is_free_shipping(order_total) else 3_000


def banner_message(order_total):
    if is_free_shipping(order_total):
        return "무료 배송"
    return "5만원 이상 무료 배송"
```

단, 우연히 모양만 같은 코드는 성급히 합치지 않는다. 변경 이유가 다르면 분리하는 편이 낫다.

## 복잡도 (Complexity)

이 원칙들은 런타임 복잡도보다 변경 복잡도를 다룬다. 잘 적용하면 수정 범위와 인지 부하가 줄지만, 과하게 적용하면 추상화 계층이 늘어 오히려 이해가 어려워질 수 있다.

## 응용 (Applications)

- 비즈니스 규칙 중복 제거
- 과한 framework-style 추상화 방지
- MVP와 점진적 설계
- 리팩토링 우선순위 판단

## 흔한 오해 (Common Misunderstandings)

- DRY는 모든 비슷한 코드를 즉시 합치라는 뜻이 아니다.
- KISS는 설계를 대충 하라는 뜻이 아니다.
- YAGNI는 확장성을 전혀 고려하지 말라는 뜻이 아니다. 확실한 변화 축은 남겨둘 수 있다.
- 원칙들은 충돌할 수 있으므로 맥락에 따라 trade-off를 판단해야 한다.

## TMI

- “Rule of three”는 같은 중복이 세 번 나타날 때 추상화를 고려하라는 경험칙이다.
- 잘못된 추상화는 중복보다 제거하기 어려울 때가 많다.
- 설계 원칙은 코드 리뷰에서 비난용 구호가 아니라 의사결정 언어로 써야 한다.

## 연습 / 확인 문제 (Exercises)

- 코드 중복과 지식 중복의 차이를 예로 설명하라.
- YAGNI를 어겨 생긴 불필요한 확장 포인트 예를 만들어라.
- DRY와 KISS가 충돌하는 상황을 하나 제시하라.

## 이어서 읽기 (Reading Path)

- 이전: [Programming/OOP.md](../../Programming/OOP.md)
- 다음: [SOLID](SOLID.md)

## 참조 (References)

- [Engineering/Software-Design/Clean-Code.md](Clean-Code.md)
- [Engineering/Software-Design/Refactoring.md](Refactoring.md)
- [Reference/Books.md](../../Reference/Books.md)
