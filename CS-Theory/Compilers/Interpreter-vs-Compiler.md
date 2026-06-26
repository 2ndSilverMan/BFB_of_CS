# 인터프리터 vs 컴파일러 (Interpreter vs Compiler)

- Level: Intermediate
- Prerequisites: [Lexer.md](Lexer.md), [Parser.md](Parser.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

컴파일러는 프로그램을 실행 전에 다른 표현으로 번역하고, 인터프리터는 프로그램 표현을 직접 읽으며 실행한다. 실제 언어 구현은 둘을 섞어 bytecode, JIT, VM 형태로 구성되는 경우가 많다.

## 직관 (Intuition)

컴파일은 책 전체를 번역해 출판한 뒤 읽는 것과 비슷하고, 인터프리트는 통역사가 문장을 읽는 즉시 옆에서 설명하는 것과 비슷하다. 전자는 실행이 빠를 수 있고, 후자는 실행 전 준비와 동적 상호작용이 유연할 수 있다.

## 이론 (Theory)

실행 방식은 스펙트럼이다.

- Ahead-of-time compiler: 소스 코드를 미리 native code로 번역한다.
- Tree-walking interpreter: AST를 직접 순회하며 실행한다.
- Bytecode VM: 소스를 bytecode로 컴파일한 뒤 VM이 실행한다.
- JIT compiler: 실행 중 hot code를 native code로 컴파일한다.

인터프리터도 내부적으로 파싱과 분석을 거치며, 컴파일러도 runtime system을 필요로 할 수 있다.

## 구현 (Implementation)

작은 expression interpreter는 AST를 재귀적으로 평가한다.

```python
def eval_expr(expr, env):
    if isinstance(expr, int):
        return expr
    if isinstance(expr, str):
        return env[expr]
    op, left, right = expr
    if op == "add":
        return eval_expr(left, env) + eval_expr(right, env)
    if op == "mul":
        return eval_expr(left, env) * eval_expr(right, env)
    raise ValueError(op)


print(eval_expr(("add", "x", ("mul", 2, 3)), {"x": 4}))
```

컴파일러라면 이 AST를 bytecode나 machine code로 변환해 실행한다.

## 복잡도 (Complexity)

인터프리터는 실행 중 dispatch overhead가 크지만 구현이 단순하고 동적 기능을 지원하기 쉽다. AOT 컴파일러는 최적화 시간이 들지만 실행 성능이 좋을 수 있다. JIT은 warmup 비용과 runtime complexity를 감수하고 hot path 성능을 노린다.

## 응용 (Applications)

- 스크립트 언어 구현
- VM과 bytecode runtime
- JIT 기반 고성능 동적 언어
- DSL과 설정 언어 실행기

## 흔한 오해 (Common Misunderstandings)

- “컴파일 언어”와 “인터프리터 언어”는 언어 자체보다 구현 방식에 가깝다.
- 인터프리터가 반드시 느린 것은 아니다. JIT과 최적화 VM이 있다.
- 컴파일러가 있으면 런타임이 필요 없는 것은 아니다.
- bytecode는 소스도 기계어도 아닌 중간 실행 표현이다.

## TMI

- Python의 대표 구현은 소스를 bytecode로 컴파일한 뒤 VM이 실행한다.
- Java는 bytecode와 JIT을 결합한 대표 사례다.
- 많은 DB query engine도 해석 실행과 JIT 컴파일 사이에서 선택한다.

## 연습 / 확인 문제 (Exercises)

- AOT, bytecode VM, JIT의 차이를 비교하라.
- tree-walking interpreter가 느릴 수 있는 이유를 설명하라.
- 언어와 구현 방식을 구분해야 하는 이유를 예로 들어라.

## 이어서 읽기 (Reading Path)

- 이전: [코드 생성](Code-Generation.md)
- 다음: [CS-Theory/Programming-Languages/](../Programming-Languages/)

## 참조 (References)

- [Lexer.md](Lexer.md)
- [Parser.md](Parser.md)
- [Intermediate-Representation.md](Intermediate-Representation.md)
- [Reference/Books.md](../../Reference/Books.md)
