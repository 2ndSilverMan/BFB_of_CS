# 중간 표현 (Intermediate Representation, IR)

- Level: Advanced
- Prerequisites: [Semantic-Analysis.md](Semantic-Analysis.md), [AST.md](AST.md), [CS-Theory/Programming-Languages/Syntax-and-Semantics.md](../Programming-Languages/Syntax-and-Semantics.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

중간 표현(IR)은 소스 언어와 대상 기계어 사이에서 프로그램을 표현하는 내부 형식이다. 컴파일러는 AST를 더 분석과 최적화에 적합한 IR로 낮추고, 이후 최적화와 코드 생성을 수행한다.

## 직관 (Intuition)

여러 언어를 여러 CPU로 번역해야 한다면 모든 조합을 직접 만들기 어렵다. IR은 공통 중간 언어 역할을 한다. 프론트엔드는 소스 언어를 IR로 바꾸고, 백엔드는 IR을 목표 아키텍처로 바꾼다.

## 이론 (Theory)

IR은 수준에 따라 나뉜다.

- High-level IR: 소스 언어 구조를 어느 정도 유지한다.
- Mid-level IR: 제어 흐름과 타입 정보를 보존하며 최적화에 적합하다.
- Low-level IR: 기계어와 가까운 연산, 레지스터, 메모리 접근을 표현한다.

대표 형태로 three-address code, control-flow graph, SSA(Static Single Assignment)가 있다. SSA는 각 변수가 한 번만 정의되도록 하여 데이터 흐름 분석과 최적화를 단순화한다.

## 구현 (Implementation)

three-address code는 복잡한 식을 단순한 임시 변수 연산으로 나눈다.

```text
# source: x = (a + b) * c
t1 = a + b
t2 = t1 * c
x = t2
```

이 표현은 최적화 pass가 각 명령을 독립적으로 검사하기 쉽게 만든다.

## 복잡도 (Complexity)

IR 변환은 보통 AST 크기에 선형이지만, SSA 구성과 최적화 분석은 control-flow graph 구조에 의존한다. 좋은 IR 설계는 이후 pass 수와 복잡도를 크게 줄인다.

## 응용 (Applications)

- 언어 프론트엔드와 백엔드 분리
- 최적화 pass 구현
- 정적 분석과 데이터 흐름 분석
- JIT 컴파일과 interpreter 내부 표현

## 흔한 오해 (Common Misunderstandings)

- IR은 하나만 있는 것이 아니다. 컴파일러는 여러 단계 IR을 가질 수 있다.
- AST와 IR은 목적이 다르다. AST는 구문 구조, IR은 분석/실행에 더 적합하다.
- SSA는 실제 기계 레지스터가 한 번만 쓰인다는 뜻이 아니다.
- IR 설계가 나쁘면 최적화와 코드 생성이 어려워진다.

## TMI

- LLVM IR은 typed SSA 기반의 널리 쓰이는 IR이다.
- MLIR은 여러 abstraction level을 가진 IR 생태계를 만들려는 프로젝트로 유명하다.
- bytecode도 넓은 의미의 IR로 볼 수 있다.

## 연습 / 확인 문제 (Exercises)

- AST와 three-address code의 차이를 설명하라.
- SSA에서 phi node가 필요한 이유를 분기 예제로 설명하라.
- IR을 쓰면 다중 언어/다중 아키텍처 지원이 쉬워지는 이유를 말하라.

## 이어서 읽기 (Reading Path)

- 이전: [의미 분석](Semantic-Analysis.md)
- 다음: [코드 최적화](Optimization.md)

## 참조 (References)

- [Semantic-Analysis.md](Semantic-Analysis.md)
- [AST.md](AST.md)
- [Reference/Books.md](../../Reference/Books.md)
