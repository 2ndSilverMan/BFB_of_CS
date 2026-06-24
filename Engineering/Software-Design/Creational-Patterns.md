# 생성 패턴 (Creational Patterns)

- Level: Intermediate
- Prerequisites: [Design-Principles.md](Design-Principles.md), [Engineering/Software-Design/SOLID.md](SOLID.md), [Programming/OOP.md](../../Programming/OOP.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

생성 패턴은 객체를 어떻게 만들지에 대한 책임을 분리하는 디자인 패턴이다. 대표적으로 Singleton, Factory, Builder가 있으며, 생성 과정이 복잡하거나 구현 선택을 숨기고 싶을 때 사용한다.

## 직관 (Intuition)

객체 생성이 단순한 한 줄이면 패턴이 필요 없다. 하지만 어떤 구현체를 만들지 조건에 따라 달라지거나, 생성 순서와 검증이 복잡하면 생성 로직이 여러 곳에 흩어진다. 생성 패턴은 이 로직을 한 곳으로 모아 변경 영향을 줄인다.

## 이론 (Theory)

- Singleton: 인스턴스를 하나만 유지해야 하는 경우 사용하지만 전역 상태가 되기 쉬워 신중해야 한다.
- Factory: 클라이언트가 구체 클래스를 몰라도 인터페이스에 맞는 객체를 받게 한다.
- Builder: 선택 옵션이 많거나 생성 단계가 복잡한 객체를 읽기 쉽게 조립한다.

핵심은 객체 생성의 변화 가능성을 사용하는 코드와 분리하는 것이다.

## 구현 (Implementation)

Factory는 조건에 따른 구체 클래스 선택을 숨길 수 있다.

```python
class JsonExporter:
    def export(self, data):
        return "json"


class CsvExporter:
    def export(self, data):
        return "csv"


def create_exporter(kind):
    if kind == "json":
        return JsonExporter()
    if kind == "csv":
        return CsvExporter()
    raise ValueError(kind)
```

호출자는 `exporter.export(data)`만 알면 되고, 구체 생성 규칙은 factory에 모인다.

## 복잡도 (Complexity)

생성 패턴은 런타임 비용보다 구조적 비용이 중요하다. 작은 코드에 패턴을 과하게 넣으면 파일과 타입 수가 늘어 복잡해진다. 생성 규칙이 여러 곳에서 반복되거나 변경이 잦을 때 비용을 회수한다.

## 응용 (Applications)

- 외부 API 클라이언트 생성
- 설정에 따른 저장소/전략 구현체 선택
- 복잡한 request, query, test fixture 구성
- dependency injection container와 객체 조립

## 흔한 오해 (Common Misunderstandings)

- Singleton은 편하지만 테스트와 병렬 실행을 어렵게 만들 수 있다.
- Factory가 있으면 무조건 좋은 설계가 되는 것은 아니다.
- Builder는 매개변수가 조금 많은 모든 함수에 필요한 것은 아니다.
- 패턴 이름을 쓰는 것보다 생성 책임을 왜 분리하는지가 중요하다.

## TMI

- 의존성 주입은 factory와 함께 객체 생성을 애플리케이션 경계로 밀어내는 데 자주 쓰인다.
- Builder는 immutable object 생성과 잘 어울린다.
- 많은 언어의 named argument나 data class가 Builder 필요성을 줄여주기도 한다.

## 연습 / 확인 문제 (Exercises)

- Factory를 쓰면 클라이언트 코드가 어떤 구체 지식에서 자유로워지는지 설명하라.
- Singleton이 테스트를 어렵게 만드는 예를 들어라.
- Builder가 적합한 객체 생성 사례를 하나 설계하라.

## 이어서 읽기 (Reading Path)

- 이전: [Design Principles](Design-Principles.md)
- 다음: [구조 패턴](Structural-Patterns.md)

## 참조 (References)

- [Engineering/Software-Design/SOLID.md](SOLID.md)
- [Engineering/Software-Design/Refactoring.md](Refactoring.md)
- [Reference/Books.md](../../Reference/Books.md)
