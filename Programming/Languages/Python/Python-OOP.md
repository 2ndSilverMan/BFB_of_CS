# Python 클래스와 객체 (Python OOP)

- Level: Beginner
- Prerequisites: [Python 함수와 모듈](Python-Functions-and-Modules.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

Python의 클래스는 데이터와 동작을 함께 묶는 사용자 정의 타입이다. 객체는 클래스에서 만들어진 인스턴스이며, 속성과 메서드를 가진다.

## 직관 (Intuition)

딕셔너리로도 데이터를 묶을 수 있지만, 클래스는 "이 데이터로 무엇을 할 수 있는가"까지 같은 곳에 둔다. 작은 도메인 모델을 표현할 때 유용하다.

## 핵심 문법 (Core Syntax)

```python
class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}"


user = User("Ada")
print(user.greet())
```

`self`는 현재 인스턴스를 가리킨다. 메서드를 호출하면 Python이 인스턴스를 첫 번째 인자로 넘긴다.

## 이론 (Theory)

Python은 duck typing을 자주 사용한다. 어떤 객체가 필요한 메서드를 제공하면 구체 클래스보다 행동이 중요하다. 상속은 강력하지만, 단순 데이터 묶음에는 `dataclass`가 더 읽기 쉬울 수 있다.

## 구현 (Implementation)

상태를 가진 개념은 class로 묶고, 값 객체는 `dataclass`로 시작하면 좋다. 상속보다 composition을 먼저 고려하고, method가 객체 상태를 실제로 사용하는지 확인해 불필요한 class를 피한다.

```python
from dataclasses import dataclass


@dataclass
class Point:          # 값 객체는 dataclass로 시작
    x: int
    y: int

    def moved(self, dx, dy):
        return Point(self.x + dx, self.y + dy)


p = Point(1, 2)
print(p.moved(3, 4))   # Point(x=4, y=6)
```

## 복잡도 (Complexity)

객체는 `dict` 기반 attribute 저장 등으로 단순 tuple보다 memory overhead가 크다. 많은 객체를 만들거나 attribute 접근이 hot path가 되면 `__slots__`, dataclass 옵션, 자료구조 변경을 검토한다.

## 응용 (Applications)

- 도메인 객체 표현
- 상태와 동작 캡슐화
- 테스트용 fake 객체 작성
- 라이브러리 API 모델링

## 흔한 오해 (Common Misunderstandings)

- 모든 것을 클래스로 만들 필요는 없다. 함수와 간단한 자료구조가 더 나을 때가 많다.
- `self`는 예약어는 아니지만 관례적으로 반드시 그렇게 쓴다.
- 클래스 변수와 인스턴스 변수를 혼동하면 상태가 공유될 수 있다.
- 상속보다 composition이 더 단순한 설계가 될 때가 많다.

## TMI

- `@dataclass`는 반복적인 초기화 코드를 줄여 준다.
- `__str__`, `__repr__` 같은 dunder method는 객체의 특별한 동작을 정의한다.
- Python의 private은 강제 접근 제한보다 이름 관례에 가깝다.

## 연습 / 확인 문제 (Exercises)

- `BankAccount` 클래스를 만들고 입금/출금 메서드를 작성하라.
- 클래스 변수와 인스턴스 변수의 차이를 예제로 보여라.
- `dataclass`로 간단한 좌표 객체를 만들어라.

## 이어서 읽기 (Reading Path)

- 이전: [Python 함수와 모듈](Python-Functions-and-Modules.md), [OOP](../../OOP.md)
- 다음: [Data-Structures](../../../Data-Structures/)

## 참조 (References)

- [Programming/OOP.md](../../OOP.md)
- [Engineering/Software-Design/Clean-Code.md](../../../Engineering/Software-Design/Clean-Code.md)
