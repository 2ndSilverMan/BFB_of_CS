# 코드 생성 (Code Generation)

- Level: Advanced
- Prerequisites: [Optimization.md](Optimization.md), [Intermediate-Representation.md](Intermediate-Representation.md), [Systems/Computer-Architecture/CPU-and-ISA.md](../../Systems/Computer-Architecture/CPU-and-ISA.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

코드 생성은 IR을 대상 아키텍처의 기계어, 어셈블리, 바이트코드로 변환하는 컴파일러 단계다. 명령 선택, 레지스터 할당, 명령 스케줄링, calling convention 적용이 주요 작업이다.

## 직관 (Intuition)

IR은 “무엇을 계산할지”를 비교적 중립적으로 말한다. 코드 생성은 이를 “이 CPU의 어떤 명령과 레지스터로 계산할지”로 바꾼다. 같은 프로그램도 x86, ARM, WebAssembly에 따라 다른 코드가 나온다.

## 이론 (Theory)

코드 생성의 핵심 하위 문제는 다음과 같다.

- Instruction selection: IR 연산을 대상 ISA 명령으로 매핑한다.
- Register allocation: 무한에 가까운 임시 변수를 제한된 물리 레지스터에 배치한다.
- Spilling: 레지스터가 부족하면 일부 값을 메모리에 저장한다.
- Instruction scheduling: pipeline과 latency를 고려해 명령 순서를 조정한다.
- ABI/calling convention: 함수 호출, 인자 전달, stack frame 규칙을 따른다.

레지스터 할당은 graph coloring 문제와 연결되며, 실용 컴파일러는 heuristic을 사용한다.

## 구현 (Implementation)

단순한 stack machine bytecode 생성은 AST 후위 순회와 비슷하다.

```python
def gen_expr(expr):
    if isinstance(expr, int):
        return [("PUSH", expr)]
    op, left, right = expr
    return gen_expr(left) + gen_expr(right) + [(op.upper(),)]


print(gen_expr(("add", 2, ("mul", 3, 4))))
```

실제 native code generation은 target ISA, register, memory addressing mode를 고려한다.

## 복잡도 (Complexity)

명령 선택과 스케줄링은 실용적으로 빠른 heuristic을 사용한다. 레지스터 할당은 큰 함수에서 컴파일 시간과 코드 품질에 큰 영향을 준다. 최적 코드 생성은 일반적으로 어려운 조합 최적화 문제다.

## 응용 (Applications)

- native compiler backend
- VM bytecode compiler
- JIT compiler
- WebAssembly와 cross-compilation

## 흔한 오해 (Common Misunderstandings)

- 코드 생성은 단순 번역이 아니라 많은 최적화 판단을 포함한다.
- 레지스터가 부족하면 성능이 크게 떨어질 수 있다.
- 같은 IR이라도 target별 성능 차이가 크다.
- ABI를 무시하면 다른 함수나 라이브러리와 연결할 수 없다.

## TMI

- JIT은 실행 중 profiling 정보를 이용해 hot path를 더 공격적으로 최적화할 수 있다.
- Tree pattern matching은 instruction selection의 고전적 접근이다.
- SSA를 기계 코드로 내릴 때 phi node 제거가 필요하다.

## 연습 / 확인 문제 (Exercises)

- instruction selection과 register allocation의 차이를 설명하라.
- spilling이 왜 성능을 낮추는지 말하라.
- calling convention이 필요한 이유를 함수 호출 예로 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [코드 최적화](Optimization.md)
- 다음: [인터프리터 vs 컴파일러](Interpreter-vs-Compiler.md)

## 참조 (References)

- [Optimization.md](Optimization.md)
- [Intermediate-Representation.md](Intermediate-Representation.md)
- [Systems/Computer-Architecture/CPU-and-ISA.md](../../Systems/Computer-Architecture/CPU-and-ISA.md)
- [Reference/Books.md](../../Reference/Books.md)
