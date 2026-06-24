# 코드 최적화 (Compiler Optimization)

- Level: Advanced
- Prerequisites: [Intermediate-Representation.md](Intermediate-Representation.md), [Algorithms/Complexity.md](../../Algorithms/Complexity.md), [Systems/Computer-Architecture/Memory-Hierarchy.md](../../Systems/Computer-Architecture/Memory-Hierarchy.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

컴파일러 최적화는 프로그램의 의미를 유지하면서 실행 시간, 코드 크기, 메모리 접근, 전력 사용 등을 개선하는 변환이다. 보통 IR 위에서 여러 optimization pass를 반복 적용한다.

## 직관 (Intuition)

사람이 쓴 코드는 이해하기 좋은 형태이고, 기계가 빠르게 실행하기 좋은 형태와 다를 수 있다. 컴파일러는 불필요한 계산을 지우고, 반복문을 개선하고, 메모리 접근을 줄여 더 효율적인 형태로 바꾼다.

## 이론 (Theory)

대표 최적화는 다음과 같다.

- Constant folding: 상수식을 컴파일 시간에 계산한다.
- Dead code elimination: 결과가 쓰이지 않는 코드를 제거한다.
- Common subexpression elimination: 같은 계산을 재사용한다.
- Loop invariant code motion: 반복문 안에서 변하지 않는 계산을 밖으로 뺀다.
- Inlining: 함수 호출을 함수 본문으로 대체해 호출 비용과 추가 최적화 기회를 만든다.

정확한 최적화는 control-flow analysis, data-flow analysis, alias analysis에 의존한다. 특히 포인터 aliasing이 있으면 메모리 최적화가 어려워진다.

## 구현 (Implementation)

constant folding은 AST나 IR node를 재귀적으로 단순화한다.

```python
def fold_add(left, right):
    if isinstance(left, int) and isinstance(right, int):
        return left + right
    return ("add", left, right)


print(fold_add(2, 3))
print(fold_add("x", 3))
```

실제 pass는 side effect와 overflow semantics 같은 언어 규칙을 반드시 고려해야 한다.

## 복잡도 (Complexity)

개별 pass는 보통 IR 크기에 선형 또는 거의 선형으로 설계하지만, pass를 여러 번 반복하면 컴파일 시간이 증가한다. 고급 최적화는 분석 비용이 크고, JIT에서는 최적화 비용과 실행 이득을 균형 잡아야 한다.

## 응용 (Applications)

- 실행 시간 단축
- 바이너리 크기 감소
- 에너지 효율 개선
- 고수준 언어의 zero-cost abstraction 지원

## 흔한 오해 (Common Misunderstandings)

- 최적화는 항상 코드를 빠르게 만드는 것이 아니다. 코드 크기나 cache behavior가 나빠질 수 있다.
- 의미 보존이 최우선이다. 정의되지 않은 동작이 있으면 결과가 놀랍게 보일 수 있다.
- 컴파일러가 모든 비효율을 알아서 해결하지는 않는다.
- 최적화 수준을 올리면 디버깅이 어려워질 수 있다.

## TMI

- profile-guided optimization은 실제 실행 프로파일을 사용해 더 나은 결정을 한다.
- auto-vectorization은 반복문을 SIMD 명령으로 바꾸려는 최적화다.
- escape analysis는 객체가 함수 밖으로 탈출하지 않으면 stack allocation이나 제거를 가능하게 한다.

## 연습 / 확인 문제 (Exercises)

- dead code와 unreachable code의 차이를 설명하라.
- loop invariant code motion 예를 하나 만들어라.
- alias analysis가 어려우면 어떤 최적화가 막히는지 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [중간 표현](Intermediate-Representation.md)
- 다음: [코드 생성](Code-Generation.md)

## 참조 (References)

- [Intermediate-Representation.md](Intermediate-Representation.md)
- [Systems/Computer-Architecture/Memory-Hierarchy.md](../../Systems/Computer-Architecture/Memory-Hierarchy.md)
- [Reference/Books.md](../../Reference/Books.md)
