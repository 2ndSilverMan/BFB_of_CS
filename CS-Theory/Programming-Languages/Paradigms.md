# 패러다임 비교: 명령형, 함수형, 논리형

- Level: Intermediate
- Prerequisites: [Syntax-and-Semantics.md](Syntax-and-Semantics.md), [Lambda-Calculus.md](Lambda-Calculus.md), [Programming/Functional-Intro.md](../../Programming/Functional-Intro.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

프로그래밍 패러다임은 프로그램을 **어떤 관점으로 구성하고 실행을 이해할지**의 스타일이다. 명령형=상태 변경 절차, 함수형=값과 함수 합성, 논리형=관계와 추론. "무엇을 하라(how)" vs "무엇이 참인가(what)"의 축이 핵심.

## 직관 (Intuition)

같은 문제도 "무엇을 순서대로 바꿀까?"(명령형), "어떤 값을 어떤 함수로 변환할까?"(함수형), "어떤 관계를 만족하는 답을 찾을까?"(논리형)로 다르게 표현된다. 패러다임은 **사고의 렌즈**이고, 현대 언어는 대부분 다중 패러다임이다.

## 이론 (Theory)

| 패러다임 | 중심 개념 | 대표 | 추론 도구 |
|---|---|---|---|
| 명령형 | 변수·할당·제어 흐름·mutable state | C, Java | 단계별 상태 추적 |
| 함수형 | 순수 함수·불변·고차 함수·재귀·ADT | Haskell, OCaml | **참조 투명성**(식을 값으로 치환) |
| 논리형 | 사실·규칙·질의·**백트래킹 탐색** | Prolog | 통일 + 탐색 |
| 선언형(넓게) | "무엇"만 기술, "어떻게"는 엔진이 | SQL | 질의 최적화기 |

**참조 투명성**(같은 입력 → 항상 같은 출력, 부작용 없음)이 함수형의 핵심 — 식을 그 값으로 안전히 치환할 수 있어 reasoning·테스트·병렬화가 쉬워진다.

## 구현 (Implementation)

```python
# 명령형: 상태를 단계적으로 변경
total = 0
for x in [1, 2, 3]:
    if x % 2: total += x          # 누적 변수(mutable)

# 함수형: 부작용 없는 합성
total2 = sum(x for x in [1, 2, 3] if x % 2)   # 같은 결과, 상태 변경 없음
```

```prolog
% 논리형(Prolog): 사실 + 규칙을 선언하면 엔진이 탐색
parent(tom, bob).  parent(bob, ann).
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).
% ?- ancestor(tom, ann).  → true  (백트래킹으로 Z=bob 탐색)
```

## 복잡도 (Complexity)

패러다임 자체가 알고리즘 복잡도를 정하진 않는다. 단 **불변 자료구조**(공유 + 경로 복사), **lazy evaluation**(필요할 때 계산), **백트래킹 탐색**(지수 가능) 같은 구현 방식이 성능 특성을 크게 바꾼다.

## 응용 (Applications)

- 명령형: 시스템 프로그래밍·성능 민감 코드.
- 함수형: 데이터 변환·동시성·컴파일러(불변·합성).
- 논리형: 규칙 엔진·제약 해결·프로그램 분석.
- 선언형: SQL·빌드 시스템·인프라(Terraform).

## 흔한 오해 (Common Misunderstandings)

- **함수형이 반복문을 못 쓰는 게 아니다** — 상태 변경을 줄이는 스타일(재귀·고차 함수로 대체).
- **명령형이 항상 저수준/나쁜 게 아니다** — 많은 알고리즘이 자연스럽다.
- **논리형이 모든 문제를 자동·효율적으로 풀지 않는다** — 탐색이 폭발할 수 있다.
- **한 언어 = 한 패러다임이 아니다** — 대부분 다중 패러다임.

## TMI

- SQL은 가장 성공한 선언형 언어 — "어떻게 조인할지"는 질의 최적화기가 정한다.
- Lisp 계열은 함수형 + 매크로(코드=데이터)로 언어 확장성에서 독보적이다.
- Rust는 명령형 시스템 언어지만 함수형 요소(불변 기본·`Option`/`Result`·이터레이터)와 강한 타입을 차용했다.

## 연습 / 확인 문제 (Exercises)

- 같은 필터링 문제를 명령형·함수형으로 각각 표현하라.
- 참조 투명성이 테스트·병렬화에 유리한 이유를 설명하라.
- 위 Prolog `ancestor` 질의가 백트래킹으로 답을 찾는 과정을 추적하라.
- SQL이 왜 선언형인지 "무엇 vs 어떻게"로 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [타입 추론](Type-Inference.md)
- 다음: [메모리 관리 모델](Memory-Models.md)
- 관련: [함수형 입문](../../Programming/Functional-Intro.md)

## 참조 (References)

- [Syntax-and-Semantics.md](Syntax-and-Semantics.md)
- [Lambda-Calculus.md](Lambda-Calculus.md)
- [Programming/Functional-Intro.md](../../Programming/Functional-Intro.md)
- [Reference/Books.md](../../Reference/Books.md)
