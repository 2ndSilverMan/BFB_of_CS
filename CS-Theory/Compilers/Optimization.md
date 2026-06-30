# 코드 최적화 (Compiler Optimization)

- Level: Advanced
- Prerequisites: [Intermediate-Representation.md](Intermediate-Representation.md), [Algorithms/Complexity.md](../../Algorithms/Complexity.md), [Systems/Computer-Architecture/Memory-Hierarchy.md](../../Systems/Computer-Architecture/Memory-Hierarchy.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

컴파일러 최적화는 **프로그램의 관찰 가능한 의미를 보존**하면서 실행 시간·코드 크기·메모리 접근·전력을 개선하는 변환이다. 보통 [IR](Intermediate-Representation.md) 위에서 여러 **pass**를 반복 적용하며, 각 pass는 **분석(analysis)** 결과에 의존한다.

## 직관 (Intuition)

사람이 쓴 코드는 *읽기 좋은* 형태이고, 기계가 *빠르게 실행하는* 형태와 다르다. 컴파일러는 불필요한 계산을 지우고, 반복문을 다듬고, 메모리 접근을 줄인다. 핵심 제약은 단 하나 — **의미 보존**. 단, "정의되지 않은 동작(UB)"은 컴파일러가 마음대로 가정할 수 있어 놀라운 결과가 나오기도 한다.

## 이론 (Theory)

### 1. 대표 최적화

| 최적화 | 내용 |
|---|---|
| Constant folding | 상수식을 컴파일 시간에 계산 |
| Dead code elimination | 결과가 안 쓰이는 코드 제거 |
| Common subexpression elim | 같은 계산 재사용 |
| Loop invariant code motion | 루프 안 불변식을 밖으로 |
| Inlining | 호출을 본문으로 → 추가 최적화 기회 |

### 2. 분석이 변환을 가능케 한다

- **control-flow analysis**: 기본 블록·CFG.
- **data-flow analysis**: reaching definitions, liveness(어떤 변수가 이후 쓰이나).
- **alias analysis**: 두 포인터가 같은 메모리를 가리킬 수 있나 — **포인터 aliasing이 불확실하면 메모리 최적화가 막힌다**.

**SSA(정적 단일 대입) 형식**(각 변수가 한 번만 정의)이 현대 최적화의 표준 IR — def-use 관계가 명시돼 분석이 쉬워진다.

## 구현 (Implementation)

```python
# constant folding + dead code: IR(튜플 트리)를 재귀 단순화
def fold(node):
    if isinstance(node, int): return node
    op, *args = node
    a, b = (fold(x) for x in args)
    if op == "add" and isinstance(a, int) and isinstance(b, int):
        return a + b                       # 상수 폴딩
    if op == "mul" and (a == 0 or b == 0):
        return 0                            # 대수적 단순화
    return (op, a, b)

print(fold(("add", ("mul", 2, 3), "x")))   # ('add', 6, 'x')
```

**워크드 예제(before→after).**
```text
t1 = 2 * 3      ; constant fold → t1 = 6
t2 = t1 + x
t3 = t1 + x      ; CSE → t3 = t2 (재계산 제거)
y  = t2          ; t3는 dead → 제거
```
실제 pass는 side effect·overflow semantics 같은 언어 규칙을 반드시 지켜야 한다.

## 복잡도 (Complexity)

| 항목 | 특성 |
|---|---|
| 개별 pass | 보통 IR 크기에 선형~준선형 |
| pass 반복 | 컴파일 시간 ↑(고정점까지) |
| 고급 분석(alias·interproc) | 비용 큼 |
| JIT | 최적화 비용 ↔ 실행 이득 균형 |

## 응용 (Applications)

- 실행 시간 단축·바이너리 축소·에너지 효율, zero-cost abstraction 지원.
- PGO(프로파일 기반)·auto-vectorization(SIMD)·escape analysis(스택 할당).

## 흔한 오해 (Common Misunderstandings)

- **최적화가 항상 빠르게 만들지 않는다** — 코드 크기·캐시 동작이 나빠질 수 있다.
- **의미 보존이 최우선** — UB가 있으면 결과가 놀랍게 보일 수 있다(컴파일러가 "안 일어난다"고 가정).
- **컴파일러가 모든 비효율을 잡지 않는다** — 알고리즘 선택은 사람 몫.
- **`-O2`/`-O3` 는 디버깅을 어렵게** 한다(변수 제거·인라인으로 소스 매핑 흐려짐).

## TMI

- LLVM은 SSA 기반 IR에 수백 개 pass를 적용하며, `opt -O2 -print-after-all` 로 각 pass 효과를 볼 수 있다.
- `restrict`(C)·`noalias` 는 "이 포인터는 다른 것과 안 겹친다"고 컴파일러에 약속해 메모리 최적화를 푼다.
- escape analysis 덕에 JVM은 짧게 사는 객체를 힙 대신 스택/레지스터에 두거나 아예 제거한다(scalar replacement).

## 연습 / 확인 문제 (Exercises)

- dead code와 unreachable code의 차이를 설명하라.
- 위 before→after 예제에 LICM을 적용할 수 있는 루프를 추가하라.
- alias가 불확실하면 어떤 메모리 최적화가 막히는지 예로 설명하라.
- SSA 형식이 왜 data-flow 분석을 단순화하는지 def-use로 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [중간 표현](Intermediate-Representation.md)
- 다음: [코드 생성](Code-Generation.md)
- 관련: [메모리 계층](../../Systems/Computer-Architecture/Memory-Hierarchy.md)

## 참조 (References)

- [Intermediate-Representation.md](Intermediate-Representation.md)
- [Systems/Computer-Architecture/Memory-Hierarchy.md](../../Systems/Computer-Architecture/Memory-Hierarchy.md)
- [Reference/Books.md](../../Reference/Books.md)
