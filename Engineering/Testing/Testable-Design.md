# 테스트 가능한 설계 (Testable Design)

- Level: Intermediate
- Prerequisites: [Engineering/Software-Design/SOLID.md](../Software-Design/SOLID.md), [Engineering/Testing/Test-Doubles.md](Test-Doubles.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

테스트 가능한 설계는 코드가 의존성을 통제하고, 부작용을 격리하고, 작은 단위로 검증 가능하도록 만드는 설계다. 의존성 주입과 인터페이스 분리가 대표 기법이다.

## 직관 (Intuition)

코드가 DB, 시간, 네트워크, 전역 상태에 단단히 붙어 있으면 테스트가 어려워진다. 플러그처럼 갈아 끼울 수 있게 만들면 테스트도 쉬워진다.

## 이론 (Theory)

테스트하기 쉬운 코드는 대개 결합도가 낮고 응집도가 높다. Pure function은 테스트가 쉽고, side effect는 경계로 밀어내면 통제 가능하다. Dependency inversion은 고수준 정책이 저수준 구현에 직접 의존하지 않게 한다.

## 구현 (Implementation)

```python
class OrderService:
    def __init__(self, payment_gateway):
        self.payment_gateway = payment_gateway
```

테스트에서는 `payment_gateway`를 fake로 바꿔 성공·실패를 재현한다.

## 복잡도 (Complexity)

추상화를 너무 많이 만들면 코드가 장황해진다. 테스트 가능성은 단순성과 균형을 맞춰야 한다.

## 응용 (Applications)

- 외부 API 의존 코드
- 시간·랜덤성 제어
- 도메인 로직 분리
- 레거시 코드 리팩터링

## 흔한 오해 (Common Misunderstandings)

- 테스트 가능하게 만들기 위해 모든 클래스를 인터페이스로 감쌀 필요는 없다.
- Private 메서드를 직접 테스트하려는 욕구는 설계 냄새일 수 있다.
- 전역 singleton은 테스트 격리를 어렵게 한다.
- 테스트 가능한 설계는 테스트만이 아니라 유지보수성도 높인다.

## TMI

- Hexagonal architecture는 외부 adapter와 내부 domain을 분리한다.
- Clock, random generator, ID generator는 주입하기 좋은 의존성이다.
- Characterization test는 레거시 코드 변경 전 현재 행동을 고정한다.

## 연습 / 확인 문제 (Exercises)

- 현재 시간을 직접 호출하는 코드를 테스트 가능하게 바꿔라.
- 외부 결제 API 의존성을 인터페이스로 분리하라.
- Pure function과 side-effecting function을 분리하는 예를 작성하라.

## 이어서 읽기 (Reading Path)

- 이전: [테스트 더블](Test-Doubles.md)
- 다음: [계약 테스트](Contract-Testing.md), [리팩터링](../Software-Design/Refactoring.md)

## 참조 (References)

- [Engineering/Software-Design/SOLID.md](../Software-Design/SOLID.md)
- [Engineering/Testing/Test-Doubles.md](Test-Doubles.md)
