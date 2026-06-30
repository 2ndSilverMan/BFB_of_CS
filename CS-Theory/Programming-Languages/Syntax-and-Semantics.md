# 구문과 의미론 (Syntax and Semantics)

- Level: Intermediate
- Prerequisites: [CS-Theory/Computation-Theory/Context-Free.md](../Computation-Theory/Context-Free.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

프로그래밍 언어의 **구문(syntax)** 은 어떤 문자열이 올바른 프로그램인지 정하고, **의미론(semantics)** 은 그 프로그램이 무엇을 뜻하고 어떻게 실행되는지 정한다. `1 + 2`가 문법에 맞는 식이라는 사실은 구문의 문제이고, 이 식이 정수 `3`으로 평가된다는 사실은 의미론의 문제다.

## 직관 (Intuition)

구문은 문장의 철자와 문법, 의미론은 그 문장이 전달하는 뜻에 가깝다. 문법에 맞아도 뜻이 없을 수 있고, 비슷한 뜻을 여러 문법으로 표현할 수도 있다. 컴파일러는 먼저 토큰과 구문 트리를 만들고, 그 위에서 이름·타입·실행 규칙을 해석한다.

```mermaid
flowchart LR
    S[소스 코드] --> T[토큰]
    T --> A[추상 구문 트리]
    A --> M[정적 의미 검사]
    M --> E[평가 또는 코드 생성]
```

## 이론 (Theory)

구문은 보통 문맥 자유 문법으로 정의한다. 다음 문법은 정수와 덧셈으로 이뤄진 작은 식 언어를 나타낸다.

$$
e ::= n \mid e + e \mid (e)
$$

의미론에는 대표적으로 세 가지 관점이 있다.

| 방식 | 핵심 질문 | 표현 |
|---|---|---|
| 조작적 의미론 | 프로그램이 어떤 단계로 실행되는가? | 상태 전이, 평가 규칙 |
| 지시적 의미론 | 프로그램을 어떤 수학적 대상으로 해석하는가? | 함수, 영역(domain) |
| 공리적 의미론 | 실행 전후에 무엇을 증명할 수 있는가? | 논리식, Hoare triple |

작은 단계 조작적 의미론에서는 한 번의 계산을 $e \rightarrow e'$로 쓴다. 예를 들어 덧셈의 왼쪽 항이 한 단계 진행하면 전체 식도 진행한다.

$$
\frac{e_1 \rightarrow e_1'}{e_1 + e_2 \rightarrow e_1' + e_2}
$$

공리적 의미론의 Hoare triple $\{P\}\ C\ \{Q\}$는 사전 조건 $P$에서 명령 $C$를 실행해 종료하면 사후 조건 $Q$가 성립한다는 뜻이다. 각 의미론은 같은 언어를 다른 목적—실행기 구현, 수학적 모델링, 프로그램 검증—으로 바라본다.

## 구현 (Implementation)

작은 식 언어의 AST를 파이썬 튜플로 표현하고 조작적 의미를 직접 부여해 보자.

```python
def evaluate(expr):
    tag = expr[0]
    if tag == "number":
        return expr[1]
    if tag == "add":
        return evaluate(expr[1]) + evaluate(expr[2])
    if tag == "multiply":
        return evaluate(expr[1]) * evaluate(expr[2])
    raise ValueError(f"unknown syntax: {tag}")


tree = ("add", ("number", 1), ("multiply", ("number", 2), ("number", 3)))
print(evaluate(tree))  # 7
```

여기서 튜플의 허용된 모양은 구문이고, `evaluate`의 각 분기는 그 구문에 대응하는 의미 규칙이다.

## 복잡도 (Complexity)

구문과 의미론 자체는 복잡도 클래스가 아니라 **언어 정의 방법**이다. 위처럼 각 AST 노드를 한 번 방문하는 평가기는 노드 수를 $n$, 재귀 깊이를 $h$라 할 때 시간 `O(n)`, 호출 스택 `O(h)`를 사용한다. 실제 언어에서는 환경 조회, 함수 호출, 메모리 효과에 따라 비용 모델이 달라진다.

## 응용 (Applications)

- 언어 명세에서 구현체들이 같은 프로그램을 일관되게 해석하도록 규정
- 인터프리터와 컴파일러의 프런트엔드 설계
- 타입 안전성, 종료성, 프로그램 동치 같은 성질의 증명
- 정적 분석기, 검증기, 코드 변환 도구의 정확성 기준 제공

## 흔한 오해 (Common Misunderstandings)

- 문법에 맞는 프로그램이 반드시 의미적으로 올바른 것은 아니다. `1 + true`는 파싱되더라도 타입 오류일 수 있다.
- 의미론은 자연어 설명만을 뜻하지 않는다. 추론 규칙과 수학적 함수로 엄밀하게 정의할 수 있다.
- 구현체의 현재 동작이 곧 언어의 의미는 아니다. 명세가 정의하지 않은 동작이나 구현 버그일 수 있다.
- 구문 오류, 정적 의미 오류, 실행 시간 오류는 서로 다른 단계에서 발견된다.

## TMI

- C 계열의 `x++ + ++x` 같은 표현이 위험한 까닭은 구문보다 평가 순서와 부수 효과의 의미 규칙이 복잡하기 때문이다.
- 괄호가 많아 보이는 Lisp 계열은 구문이 거의 AST와 일치해 파서가 단순한 대신, 매크로가 구문 자체를 데이터처럼 다룰 수 있다.
- 의미론 연구에서는 언어 기능을 추가할 때 기존 증명을 얼마나 적게 고쳐도 되는지도 중요한 설계 문제다.

## 연습 / 확인 문제 (Exercises)

- `subtract`와 `if-zero` 노드를 위 평가기에 추가하고 각각의 의미 규칙을 말로 설명하라.
- `1 + true`가 구문상 허용되지만 의미상 거부되도록 정적 검사기를 설계하라.
- 대입문 `x := x + 1`에 대해 적절한 Hoare triple 하나를 작성하라.

## 이어서 읽기 (Reading Path)

- 이전: [문맥 자유 문법과 푸시다운 오토마타](../Computation-Theory/Context-Free.md)
- 다음: [람다 대수](Lambda-Calculus.md)
- 관련: [타입 시스템](Type-Systems.md), [추상 구문 트리](../Compilers/AST.md)

## 참조 (References)

- [CS-Theory/Computation-Theory/Context-Free.md](../Computation-Theory/Context-Free.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
