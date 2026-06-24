# JIT 컴파일과 런타임 최적화 (JIT Optimization)

- Level: Advanced
- Prerequisites: [Engineering/Performance/Benchmarking-Basics.md](Benchmarking-Basics.md), [Systems/Computer-Architecture/CPU-and-ISA.md](../../Systems/Computer-Architecture/CPU-and-ISA.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

JIT(Just-In-Time) 컴파일은 프로그램 실행 중 hot code를 기계어로 컴파일하고, runtime profile을 이용해 최적화하는 방식이다.

## 직관 (Intuition)

처음에는 빠르게 시작하고, 자주 지나가는 길은 나중에 포장한다. 하지만 길의 모양이 바뀌면 포장을 걷어내야 할 수도 있다.

## 이론 (Theory)

JIT runtime은 interpreter, baseline compiler, optimizing compiler를 계층적으로 사용한다. Inline cache, type feedback, escape analysis, devirtualization, inlining으로 hot path를 빠르게 만든다. 가정이 깨지면 deoptimization이 발생한다. Warmup 전 benchmark는 steady-state 성능을 대표하지 않는다.

## 구현 (Implementation)

```javascript
function add(a, b) {
  return a + b;
}

for (let i = 0; i < 1_000_000; i++) {
  add(i, 1);
}
```

같은 type pattern이 반복되면 runtime이 더 공격적으로 최적화할 수 있다. 중간에 문자열을 섞으면 최적화 가정이 깨질 수 있다.

## 복잡도 (Complexity)

최적화 후 실행은 빨라질 수 있지만 warmup, compile time, deoptimization 비용이 있다. 짧게 실행되는 CLI는 JIT 이득이 작을 수 있다.

## 응용 (Applications)

- JavaScript VM 성능 이해
- JVM·CLR service warmup
- benchmark 설계
- hot loop type stability 개선

## 흔한 오해 (Common Misunderstandings)

- 한 번 실행한 측정은 JIT 성능을 설명하지 못한다.
- Dynamic language가 항상 느린 것은 아니다.
- Micro-optimization이 JIT 최적화를 방해할 수 있다.
- Runtime flag와 version 차이가 결과를 바꿀 수 있다.

## TMI

- Hidden class와 inline cache는 JavaScript object access 최적화의 핵심 개념이다.
- JVM에서는 tiered compilation과 GC가 성능 측정에 함께 영향을 준다.
- Ahead-of-time compilation은 startup과 예측 가능성을 얻는 대신 runtime profile 최적화 일부를 잃을 수 있다.

## 연습 / 확인 문제 (Exercises)

- warmup 포함/제외 benchmark 결과를 비교하라.
- type이 안정적인 loop와 불안정한 loop를 측정하라.
- deoptimization이 발생할 수 있는 코드를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [CDN 캐싱](CDN-Caching.md)
- 다음: [DevOps](../DevOps/)

## 참조 (References)

- [Engineering/Performance/Benchmarking-Basics.md](Benchmarking-Basics.md)
- [Systems/Computer-Architecture/CPU-and-ISA.md](../../Systems/Computer-Architecture/CPU-and-ISA.md)

