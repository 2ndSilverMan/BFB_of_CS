# 코드 생성 (Code Generation)

- Level: Advanced
- Prerequisites: [Optimization.md](Optimization.md), [Intermediate-Representation.md](Intermediate-Representation.md), [Systems/Computer-Architecture/CPU-and-ISA.md](../../Systems/Computer-Architecture/CPU-and-ISA.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

코드 생성은 [IR](Intermediate-Representation.md)을 대상 아키텍처의 기계어·어셈블리·바이트코드로 바꾼다. **명령 선택 · 레지스터 할당 · 명령 스케줄링 · calling convention(ABI)** 이 네 하위 문제다.

## 직관 (Intuition)

IR은 "무엇을 계산할지"를 중립적으로 말한다. 코드 생성은 "**이 CPU의 어떤 명령·레지스터로**"로 바꾼다. 같은 프로그램도 x86·ARM·WASM에 따라 다른 코드가 나오고, 같은 IR이라도 레지스터를 잘 쓰면 수 배 빨라진다.

## 이론 (Theory)

### 1. 네 하위 문제

- **명령 선택**: IR 연산 → 타깃 ISA 명령(tree pattern matching).
- **레지스터 할당**: 무한에 가까운 임시 변수를 제한된 물리 레지스터에.
- **spilling**: 레지스터 부족 시 일부 값을 메모리로(느려짐).
- **스케줄링**: 파이프라인·latency 고려한 명령 순서.
- **ABI/calling convention**: 인자 전달·스택 프레임·호출 규칙(이걸 어기면 라이브러리와 연결 불가).

### 2. 레지스터 할당 = 그래프 색칠

동시에 살아 있는(겹치는 생존 구간) 변수를 간선으로 잇는 **간섭 그래프(interference graph)** 를 만들고, $k$ 개 레지스터로 **$k$-색칠**한다. 색칠 불가 노드는 spill. 그래프 색칠은 NP-난해라 실용 컴파일러는 휴리스틱(Chaitin-Briggs)을 쓴다.

## 구현 (Implementation)

```python
def gen_stack(expr):                          # 스택 머신 바이트코드: AST 후위 순회
    if isinstance(expr, int):
        return [("PUSH", expr)]
    op, l, r = expr
    return gen_stack(l) + gen_stack(r) + [(op.upper(),)]

print(gen_stack(("add", 2, ("mul", 3, 4))))
# [('PUSH', 2), ('PUSH', 3), ('PUSH', 4), ('MUL',), ('ADD',)]
```

**워크드 예제(실행).** 위 바이트코드를 스택 머신이 실행: PUSH 2→[2], PUSH 3→[2,3], PUSH 4→[2,3,4], MUL→[2,12], ADD→[14]. 결과 14 = `2 + 3*4`. 후위 순회가 곧 스택 머신 코드인 이유.

## 복잡도 (Complexity)

| 항목 | 특성 |
|---|---|
| 명령 선택·스케줄링 | 실용적 휴리스틱 |
| 레지스터 할당 | 그래프 색칠(NP-난해) → 휴리스틱, 큰 함수에서 컴파일 시간 지배 |
| 최적 코드 생성 | 일반적으로 어려운 조합 최적화 |

## 응용 (Applications)

- 네이티브 컴파일러 백엔드, VM 바이트코드 컴파일러.
- JIT, WebAssembly·크로스 컴파일.

## 흔한 오해 (Common Misunderstandings)

- **코드 생성은 단순 번역이 아니다** — 많은 최적화 판단 포함.
- **레지스터 부족(spill)은 성능을 크게 떨어뜨린다**(메모리 왕복).
- **같은 IR이라도 타깃별 성능 차이가 크다**.
- **ABI를 어기면** 다른 함수·라이브러리와 링크 불가.

## TMI

- JIT은 실행 중 프로파일로 hot path를 더 공격적으로 최적화한다(역최적화/deopt도 함께).
- SSA를 기계 코드로 내릴 때 **phi node 제거**(이동 명령 삽입)가 필요하다.
- x86은 레지스터가 적고(범용 16개) ARM·RISC-V는 많아, 레지스터 할당 압박이 ISA마다 다르다.

## 연습 / 확인 문제 (Exercises)

- 명령 선택과 레지스터 할당의 차이를 설명하라.
- 위 바이트코드의 스택 변화를 손으로 추적하라(14 도출).
- 간섭 그래프를 그려 3개 레지스터로 색칠 가능/불가 예를 만들어라.
- calling convention이 필요한 이유를 함수 호출 예로 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [코드 최적화](Optimization.md)
- 다음: [인터프리터 vs 컴파일러](Interpreter-vs-Compiler.md)
- 관련: [CPU와 ISA](../../Systems/Computer-Architecture/CPU-and-ISA.md)

## 참조 (References)

- [Optimization.md](Optimization.md)
- [Intermediate-Representation.md](Intermediate-Representation.md)
- [Systems/Computer-Architecture/CPU-and-ISA.md](../../Systems/Computer-Architecture/CPU-and-ISA.md)
- [Reference/Books.md](../../Reference/Books.md)
