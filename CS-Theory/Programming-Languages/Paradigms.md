# 패러다임 비교: 명령형, 함수형, 논리형

- Level: Intermediate
- Prerequisites: [Syntax-and-Semantics.md](Syntax-and-Semantics.md), [Lambda-Calculus.md](Lambda-Calculus.md), [Programming/Functional-Intro.md](../../Programming/Functional-Intro.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

프로그래밍 패러다임은 프로그램을 어떤 관점으로 구성하고 실행을 어떻게 이해할지에 대한 스타일이다. 명령형은 상태 변경 절차, 함수형은 값과 함수 합성, 논리형은 관계와 추론을 중심으로 한다.

## 직관 (Intuition)

같은 문제도 “무엇을 순서대로 바꿀까?”, “어떤 값을 어떤 함수로 변환할까?”, “어떤 관계를 만족하는 답을 찾을까?”로 다르게 표현할 수 있다. 패러다임은 사고의 렌즈다.

## 이론 (Theory)

명령형 패러다임은 변수, 할당, 제어 흐름, mutable state를 중심으로 한다. C, Java, Python의 많은 코드가 이 스타일을 사용한다.

함수형 패러다임은 순수 함수, 불변성, 고차 함수, 재귀, algebraic data type을 강조한다. 부작용을 줄이면 reasoning과 병렬화가 쉬워질 수 있다.

논리형 패러다임은 사실과 규칙을 선언하고, 시스템이 질의에 맞는 값을 탐색한다. Prolog가 대표적이다.

현대 언어는 대부분 다중 패러다임이다. 중요한 것은 문제와 팀에 맞는 표현 방식을 선택하는 것이다.

## 구현 (Implementation)

같은 합산도 패러다임에 따라 표현이 달라진다.

```python
# imperative
total = 0
for x in [1, 2, 3]:
    total += x

# functional style
total2 = sum(map(lambda x: x, [1, 2, 3]))
```

논리형에서는 “합이 무엇인가”를 관계로 정의하고 질의하는 식으로 접근한다.

## 복잡도 (Complexity)

패러다임 자체가 알고리즘 복잡도를 결정하지는 않는다. 다만 immutable data structure, lazy evaluation, backtracking search 같은 구현 방식은 성능 특성을 크게 바꿀 수 있다.

## 응용 (Applications)

- 명령형: 시스템 프로그래밍, 성능 민감 코드
- 함수형: 데이터 변환, 동시성, 컴파일러
- 논리형: 규칙 엔진, 제약 해결, 프로그램 분석
- 다중 패러다임 설계와 언어 선택

## 흔한 오해 (Common Misunderstandings)

- 함수형은 반복문을 못 쓴다는 뜻이 아니라 상태 변경을 줄이는 스타일이다.
- 명령형이 항상 저수준이거나 나쁜 것은 아니다.
- 논리형은 모든 문제를 자동으로 효율적으로 풀어주지 않는다.
- 한 언어가 한 패러다임에만 속한다고 단정하기 어렵다.

## TMI

- SQL은 선언형 패러다임의 실용적 예로 볼 수 있다.
- Lisp 계열은 함수형뿐 아니라 매크로와 언어 확장성으로 유명하다.
- Rust는 명령형 시스템 언어지만 함수형 요소와 강한 타입 시스템을 많이 차용한다.

## 연습 / 확인 문제 (Exercises)

- 명령형과 함수형 스타일로 같은 필터링 문제를 표현해 보라.
- 순수 함수가 테스트에 유리한 이유를 설명하라.
- 논리형 패러다임이 적합한 문제 예를 하나 들어라.

## 이어서 읽기 (Reading Path)

- 이전: [타입 추론](Type-Inference.md)
- 다음: [메모리 관리 모델](Memory-Models.md)

## 참조 (References)

- [Syntax-and-Semantics.md](Syntax-and-Semantics.md)
- [Lambda-Calculus.md](Lambda-Calculus.md)
- [Programming/Functional-Intro.md](../../Programming/Functional-Intro.md)
- [Reference/Books.md](../../Reference/Books.md)
