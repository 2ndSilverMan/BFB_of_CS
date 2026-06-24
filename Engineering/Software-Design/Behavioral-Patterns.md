# 행동 패턴 (Behavioral Patterns)

- Level: Intermediate
- Prerequisites: [Structural-Patterns.md](Structural-Patterns.md), [Engineering/Software-Design/SOLID.md](SOLID.md), [Programming/Functions-and-Recursion.md](../../Programming/Functions-and-Recursion.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

행동 패턴은 객체들이 책임을 나누고 상호작용하는 방법을 다룬다. Strategy, Observer, Command는 알고리즘 교체, 이벤트 전파, 요청 캡슐화처럼 “행동의 변화”를 분리하는 데 사용된다.

## 직관 (Intuition)

프로그램에서 자주 바뀌는 것은 데이터 구조만이 아니라 행동이다. 정렬 방식, 알림 대상, 실행할 작업이 바뀔 수 있다. 행동 패턴은 이런 변화 지점을 객체나 함수로 빼내어 교체 가능하게 만든다.

## 이론 (Theory)

- Strategy: 같은 문제를 푸는 여러 알고리즘을 공통 인터페이스 뒤에 숨겨 교체한다.
- Observer: 주체의 상태 변화가 여러 구독자에게 전달되도록 한다.
- Command: 실행할 요청을 객체로 만들어 큐잉, 취소, 재시도, 로깅을 쉽게 한다.

이 패턴들은 조건문 증가를 줄이고, 변경되는 행동을 독립적으로 테스트할 수 있게 한다.

## 구현 (Implementation)

Strategy는 함수를 주입하는 방식으로도 구현할 수 있다.

```python
def sort_items(items, key_strategy):
    return sorted(items, key=key_strategy)


items = [
    {"name": "a", "score": 10},
    {"name": "b", "score": 5},
]

by_score = lambda item: item["score"]
by_name = lambda item: item["name"]

print(sort_items(items, by_score))
print(sort_items(items, by_name))
```

객체지향 언어에서는 strategy 인터페이스와 구현 클래스로 같은 구조를 만들 수 있다.

## 복잡도 (Complexity)

행동 패턴은 조건문과 결합도를 줄이는 대신 추상화 단위를 늘린다. 변화 가능성이 낮은 곳에 적용하면 오히려 읽기 어려워질 수 있다. 이벤트 기반 Observer는 흐름 추적과 디버깅이 어려워질 수 있다.

## 응용 (Applications)

- 결제/배송/가격 정책 교체
- UI 이벤트와 pub-sub 시스템
- 작업 큐, undo/redo, retry command
- 테스트에서 행동 주입과 mock 대체

## 흔한 오해 (Common Misunderstandings)

- Strategy는 무조건 클래스로만 구현해야 하는 것이 아니다. 함수도 훌륭한 strategy가 될 수 있다.
- Observer는 편하지만 이벤트 순서와 중복 호출을 관리해야 한다.
- Command는 단순 함수 호출을 복잡하게 만들 수 있으므로 기록·취소·큐잉이 필요할 때 빛난다.
- 패턴은 조건문을 모두 없애기 위한 도구가 아니다.

## TMI

- GUI 프레임워크는 Observer 패턴의 거대한 실전 예시다.
- Command sourcing과 event sourcing은 요청/사건을 기록 가능한 객체로 보는 관점과 연결된다.
- Strategy와 dependency injection은 테스트 가능한 설계와 잘 맞는다.

## 연습 / 확인 문제 (Exercises)

- Strategy로 if-else 결제 분기를 줄이는 설계를 작성하라.
- Observer에서 memory leak이 생길 수 있는 이유를 설명하라.
- Command 패턴이 retry 구현에 유리한 이유를 말하라.

## 이어서 읽기 (Reading Path)

- 이전: [구조 패턴](Structural-Patterns.md)
- 다음: [Engineering/Testing/](../Testing/)

## 참조 (References)

- [Structural-Patterns.md](Structural-Patterns.md)
- [Engineering/Software-Design/SOLID.md](SOLID.md)
- [Engineering/Testing/Unit-Test-Principles.md](../Testing/Unit-Test-Principles.md)
- [Reference/Books.md](../../Reference/Books.md)
