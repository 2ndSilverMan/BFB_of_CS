# 의미 분석과 타입 검사 (Semantic Analysis and Type Checking)

- Level: Advanced
- Prerequisites: [Parser.md](Parser.md), [AST.md](AST.md), [CS-Theory/Programming-Languages/Type-Systems.md](../Programming-Languages/Type-Systems.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

의미 분석은 파싱된 AST가 언어의 의미 규칙을 만족하는지 검사하는 컴파일러 단계다. 타입 검사, 이름 해석, 스코프 검사, 선언 전 사용 검사, 함수 호출 인자 검사 등이 여기에 속한다.

## 직관 (Intuition)

파서는 문장이 문법적으로 맞는지만 본다. “사과를 더한다” 같은 문장은 문법적으로 그럴듯해도 의미적으로 이상할 수 있다. 의미 분석은 프로그램이 언어 규칙 안에서 말이 되는지 확인한다.

## 이론 (Theory)

대표 작업은 다음과 같다.

- Symbol table 구성: 변수, 함수, 타입 이름을 스코프별로 기록한다.
- Name resolution: 식별자가 어떤 선언을 가리키는지 결정한다.
- Type checking: 표현식과 문장의 타입 규칙을 검사한다.
- Control-flow checks: return 누락, unreachable code, break/continue 위치를 검사한다.

타입 검사는 typing rule을 AST에 재귀적으로 적용하는 과정으로 볼 수 있다. 예를 들어 정수 덧셈은 두 피연산자가 정수이고 결과도 정수라는 규칙을 갖는다.

## 구현 (Implementation)

간단한 symbol table은 스코프 stack으로 구현할 수 있다.

```python
class ScopeStack:
    def __init__(self):
        self.scopes = [{}]

    def define(self, name, typ):
        self.scopes[-1][name] = typ

    def lookup(self, name):
        for scope in reversed(self.scopes):
            if name in scope:
                return scope[name]
        raise NameError(name)
```

실제 컴파일러는 AST node에 타입 정보를 annotate하거나 별도 typed IR을 만든다.

## 복잡도 (Complexity)

기본 의미 분석은 AST 크기에 선형에 가깝다. 다만 overload resolution, trait/typeclass, generic constraint solving, 타입 추론이 들어가면 훨씬 복잡해질 수 있다.

## 응용 (Applications)

- 컴파일 오류 진단
- IDE 자동완성과 jump-to-definition
- 최적화 전 타입/스코프 정보 제공
- 안전한 IR 생성

## 흔한 오해 (Common Misunderstandings)

- 파싱이 성공해도 프로그램이 의미적으로 올바른 것은 아니다.
- 타입 검사는 런타임 테스트를 대체하지 않는다.
- 에러 메시지 품질은 의미 분석 설계의 중요한 일부다.
- 동적 타입 언어도 이름 해석과 스코프 검사는 필요하다.

## TMI

- 좋은 컴파일러는 첫 오류 이후에도 분석을 계속해 여러 오류를 한 번에 보고하려고 error recovery를 한다.
- Rust의 borrow checker는 의미 분석과 타입 시스템이 프로그램 안전성을 강하게 보장하는 사례다.
- IDE의 language server는 컴파일러 프론트엔드 일부를 계속 실행하는 셈이다.

## 연습 / 확인 문제 (Exercises)

- 파싱 오류와 타입 오류의 차이를 예로 설명하라.
- 중첩 스코프에서 shadowing을 symbol table로 처리하는 방법을 설명하라.
- 함수 호출 타입 검사에 필요한 정보를 나열하라.

## 이어서 읽기 (Reading Path)

- 이전: [AST](AST.md)
- 다음: [중간 표현](Intermediate-Representation.md)

## 참조 (References)

- [Parser.md](Parser.md)
- [AST.md](AST.md)
- [CS-Theory/Programming-Languages/Type-Systems.md](../Programming-Languages/Type-Systems.md)
- [Reference/Books.md](../../Reference/Books.md)
