# SOLID 원칙

- Level: Intermediate
- Prerequisites: 객체지향 프로그래밍 기초
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

SOLID는 변경 이유를 분리하고 의존 방향을 제어하기 위한 다섯 객체지향 설계 원칙이다: 단일 책임, 개방-폐쇄, Liskov 치환, interface 분리, 의존성 역전.

## 직관 (Intuition)

서로 다른 이유로 바뀌는 코드를 한 덩어리에 넣으면 작은 변경이 연쇄 수정으로 번진다. 역할과 contract를 분리하고 고수준 정책이 구체 구현보다 abstraction에 의존하게 한다.

## 이론 (Theory)

| 원칙 | 핵심 질문 |
|---|---|
| SRP | 이 module의 변경 이유가 하나의 actor에 모이는가? |
| OCP | 새 behavior를 기존 핵심 수정보다 확장으로 추가할 수 있는가? |
| LSP | subtype이 base contract를 깨지 않고 대체되는가? |
| ISP | client가 쓰지 않는 method에 의존하는가? |
| DIP | 정책이 세부 구현이 아닌 abstraction에 의존하는가? |

원칙은 metric이나 법칙보다 tradeoff를 탐색하는 질문이다. Abstraction 비용이 실제 변경 가능성보다 크면 overengineering이 된다.

## 구현 (Implementation)

```python
class PaymentGateway:
    def charge(self, amount):
        raise NotImplementedError


class CheckoutService:
    def __init__(self, gateway: PaymentGateway):
        self.gateway = gateway

    def checkout(self, total):
        return self.gateway.charge(total)
```

## 복잡도 (Complexity)

Runtime 복잡도보다 변경·test·dependency 비용을 다룬다. Interface와 object 수가 늘어 인지 비용이 생기므로 volatile boundary에 선택적으로 적용한다.

## 응용 (Applications)

- domain service와 adapter 분리
- test double 주입
- plugin architecture
- legacy refactoring 기준

## 흔한 오해 (Common Misunderstandings)

- class마다 함수 하나만 두는 것이 SRP는 아니다.
- OCP는 어떤 변경에도 기존 코드를 절대 수정하지 말라는 뜻이 아니다.
- inheritance를 쓰면 자동으로 LSP가 성립하지 않는다.
- interface를 많이 만들수록 좋은 설계가 아니다.

## TMI

- LSP는 method signature보다 pre/postcondition과 invariant를 포함한다.
- DIP와 dependency injection은 관련되지만 원칙과 구현 기법으로 구분된다.
- SOLID는 functional design에도 일부 의존 방향 관점으로 적용할 수 있다.

## 연습 / 확인 문제 (Exercises)

- 파일 저장·메일 전송·계산을 한 class에서 분리하라.
- LSP를 위반하는 subtype 예를 만들어라.
- abstraction이 불필요한 작은 코드 사례를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [설계 원칙](Design-Principles.md)
- 다음: [클린 코드](Clean-Code.md), [리팩토링](Refactoring.md)

## 참조 (References)

- [Engineering/Testing/README.md](../Testing/README.md)
- [Reference/Books.md](../../Reference/Books.md)
