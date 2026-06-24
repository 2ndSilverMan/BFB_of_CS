# 구조 패턴 (Structural Patterns)

- Level: Intermediate
- Prerequisites: [Creational-Patterns.md](Creational-Patterns.md), [Engineering/Software-Design/SOLID.md](SOLID.md), [Programming/OOP.md](../../Programming/OOP.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

구조 패턴은 클래스와 객체를 조합해 더 큰 구조를 만드는 방법을 다룬다. Adapter, Composite, Decorator는 기존 코드를 바꾸지 않고 인터페이스를 맞추거나, 트리 구조를 통일적으로 다루거나, 기능을 동적으로 덧붙이는 데 쓰인다.

## 직관 (Intuition)

소프트웨어는 작은 부품을 이어 붙여 만든다. 부품의 모양이 맞지 않으면 adapter가 필요하고, 여러 부품과 단일 부품을 같은 방식으로 다루려면 composite가 필요하며, 기존 부품에 포장지를 한 겹씩 씌워 기능을 더하려면 decorator가 유용하다.

## 이론 (Theory)

- Adapter: 기존 클래스의 인터페이스를 클라이언트가 기대하는 인터페이스로 변환한다.
- Composite: leaf와 container를 같은 인터페이스로 다뤄 트리 구조를 표현한다.
- Decorator: 같은 인터페이스를 유지하며 객체에 책임을 동적으로 추가한다.

이 패턴들은 inheritance보다 composition을 선호하는 설계와 잘 맞는다. 기존 코드를 직접 수정하지 않고 확장하는 open-closed principle에도 연결된다.

## 구현 (Implementation)

Decorator는 같은 인터페이스를 감싸 기능을 추가한다.

```python
class Notifier:
    def send(self, message):
        print(message)


class LoggingNotifier:
    def __init__(self, wrapped):
        self.wrapped = wrapped

    def send(self, message):
        print(f"log: {message}")
        self.wrapped.send(message)


notifier = LoggingNotifier(Notifier())
notifier.send("hello")
```

호출자는 `send` 인터페이스만 사용하므로 decorator가 끼어도 클라이언트 변경이 작다.

## 복잡도 (Complexity)

구조 패턴은 변경에는 강해지지만 객체 래핑과 indirection이 늘어난다. 너무 많은 decorator나 adapter는 실행 흐름을 추적하기 어렵게 만든다.

## 응용 (Applications)

- 외부 라이브러리 인터페이스 감싸기
- UI 컴포넌트 트리
- middleware, stream, filter chain
- 캐시, 로깅, 인증 같은 횡단 관심사 추가

## 흔한 오해 (Common Misunderstandings)

- Adapter는 임시 땜질만이 아니라 경계 안정화 도구다.
- Composite는 트리 구조가 없으면 과하다.
- Decorator와 inheritance를 섞으면 책임 위치가 흐려질 수 있다.
- 패턴을 쓰면 코드가 자동으로 단순해지는 것은 아니다.

## TMI

- 많은 웹 프레임워크의 middleware는 decorator/chain 구조와 비슷하다.
- 파일 시스템의 파일/디렉터리는 composite 예시로 자주 설명된다.
- Adapter는 레거시 코드 이행에서 안전한 완충층 역할을 한다.

## 연습 / 확인 문제 (Exercises)

- Adapter와 Facade의 차이를 설명하라.
- Composite가 유리한 트리 구조 예를 하나 제시하라.
- Decorator를 사용해 캐싱 기능을 추가하는 설계를 그려라.

## 이어서 읽기 (Reading Path)

- 이전: [생성 패턴](Creational-Patterns.md)
- 다음: [행동 패턴](Behavioral-Patterns.md)

## 참조 (References)

- [Creational-Patterns.md](Creational-Patterns.md)
- [Engineering/Software-Design/SOLID.md](SOLID.md)
- [Reference/Books.md](../../Reference/Books.md)
