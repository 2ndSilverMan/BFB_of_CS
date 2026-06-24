# 객체지향 프로그래밍 (Object-Oriented Programming)

- Level: Intermediate
- Prerequisites: [Programming/Functions-and-Recursion.md](Functions-and-Recursion.md), [Programming/Arrays-and-Strings.md](Arrays-and-Strings.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

객체지향 프로그래밍(OOP)은 데이터(상태)와 그 데이터를 다루는 동작(메서드)을 객체라는 단위로 묶어 프로그램을 구성하는 패러다임이다. 캡슐화, 상속, 다형성, 추상화가 네 기둥이다.

## 직관 (Intuition)

절차적 코드는 데이터와 함수가 흩어져, 프로그램이 커지면 "이 데이터를 누가 어떻게 바꾸는가"를 추적하기 어렵다. OOP는 관련된 상태와 행동을 한 객체에 모아 경계를 만든다. 그러면 객체는 외부에 "무엇을 할 수 있는가"만 노출하고 내부 구현은 숨겨, 큰 시스템을 부품처럼 조립하고 교체할 수 있다.

## 이론 (Theory)

- **캡슐화(encapsulation)**: 상태를 숨기고 공개 인터페이스로만 접근하게 해 불변식(invariant)을 보호한다.
- **상속(inheritance)**: 기존 클래스를 확장해 코드를 재사용한다. 다만 "is-a" 관계가 성립할 때만 적절하다.
- **다형성(polymorphism)**: 같은 인터페이스 호출이 객체 타입에 따라 다르게 동작한다(동적 디스패치).
- **추상화(abstraction)**: 본질만 드러내고 세부를 감춘다(추상 클래스/인터페이스).

설계 지침으로 "상속보다 합성(composition over inheritance)"과 SOLID 원칙이 자주 인용된다. 다형성은 LSP(리스코프 치환 원칙)에 기대어, 부모 타입 자리에 자식을 넣어도 프로그램이 올바르게 동작해야 한다.

## 구현 (Implementation)

```python
class Shape:                     # 추상화: 공통 인터페이스
    def area(self) -> float:
        raise NotImplementedError

class Circle(Shape):             # 상속
    def __init__(self, r):
        self._r = r              # 캡슐화: 내부 상태
    def area(self) -> float:
        return 3.14159 * self._r ** 2

def total_area(shapes):
    return sum(s.area() for s in shapes)   # 다형성: 타입과 무관하게 area() 호출
```

## 복잡도 (Complexity)

OOP 자체는 알고리즘 복잡도를 바꾸지 않는다. 동적 디스패치는 가상 함수 테이블 조회로 약간의 런타임 비용을 더하지만 보통 무시할 만하다. 진짜 비용·이득은 설계 복잡도다. 적절한 캡슐화는 변경 범위를 줄이지만, 과도한 상속 계층은 이해와 유지보수를 어렵게 한다.

## 응용 (Applications)

- GUI, 게임 엔진의 엔티티/컴포넌트 모델링
- 도메인 모델링(주문, 계정 등 비즈니스 객체)
- 프레임워크의 확장 지점(인터페이스/추상 클래스)
- 디자인 패턴 대부분의 토대

## 흔한 오해 (Common Misunderstandings)

- 상속이 코드 재사용의 기본 수단은 아니다. 많은 경우 합성이 더 유연하다.
- 모든 것을 클래스로 만드는 것이 OOP가 아니다. 데이터만 담는 클래스는 과설계일 수 있다.
- getter/setter를 다는 것만으로 캡슐화가 되는 것은 아니다. 핵심은 불변식 보호다.
- OOP가 함수형 등 다른 패러다임보다 항상 낫지는 않다. 문제에 따라 선택한다.

## TMI

- "object-oriented"라는 용어는 1960~70년대 Smalltalk·Simula에서 비롯됐고, Alan Kay는 핵심을 "메시지 전달"로 봤다.
- Java의 "모든 것은 객체"와 C++의 "멀티패러다임"은 OOP를 받아들이는 상반된 태도를 보여 준다.
- 다이아몬드 상속 문제는 다중 상속 언어(C++)가 겪는 모호성으로, 인터페이스/믹스인으로 우회한다.

## 연습 / 확인 문제 (Exercises)

- 같은 기능을 상속과 합성 두 방식으로 설계하고 변경 용이성을 비교하라.
- 캡슐화가 불변식을 어떻게 보호하는지 은행 계좌 예제로 설명하라.
- 다형성을 쓰지 않은 `if type ==` 분기 코드를 다형성으로 리팩터링하라.

## 이어서 읽기 (Reading Path)

- 이전: [함수와 재귀](Functions-and-Recursion.md)
- 다음: [함수형 프로그래밍 입문](Functional-Intro.md), [Engineering/Software-Design/SOLID.md](../Engineering/Software-Design/SOLID.md)

## 참조 (References)

- [Programming/Functions-and-Recursion.md](Functions-and-Recursion.md)
- [Engineering/Software-Design/SOLID.md](../Engineering/Software-Design/SOLID.md)
- [Reference/Books.md](../Reference/Books.md)
