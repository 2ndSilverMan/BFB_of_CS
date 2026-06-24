# SIMD와 벡터화 (SIMD Vectorization)

- Level: Advanced
- Prerequisites: [Systems/Parallel-Computing/SIMD.md](../../Systems/Parallel-Computing/SIMD.md), [Systems/Computer-Architecture/Parallel-Architecture.md](../../Systems/Computer-Architecture/Parallel-Architecture.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

SIMD는 하나의 instruction으로 여러 data lane을 동시에 처리하는 방식이다. 벡터화는 scalar loop를 SIMD instruction을 활용하도록 바꾸는 최적화다.

## 직관 (Intuition)

숫자 하나씩 계산하지 않고 같은 연산을 여러 숫자 묶음에 한 번에 적용한다. 반복문이 단순하고 데이터가 연속적일수록 유리하다.

## 이론 (Theory)

Compiler auto-vectorization은 dependency가 없고 memory access가 규칙적인 loop에서 잘 동작한다. Alignment, stride, branch, aliasing, gather/scatter 비용이 성능을 좌우한다. SIMD 폭이 커도 memory bandwidth가 병목이면 속도가 선형으로 늘지 않는다.

## 구현 (Implementation)

```python
import numpy as np

a = np.arange(1_000_000, dtype=np.float32)
b = np.arange(1_000_000, dtype=np.float32)
c = a * 0.5 + b
```

NumPy 같은 array library는 내부에서 vectorized native loop를 사용한다. Python loop보다 빠른 이유는 interpreter overhead 감소와 SIMD 활용이다.

## 복잡도 (Complexity)

연산 수 Big-O는 같지만 lane 수만큼 instruction 수가 줄 수 있다. 실제 speedup은 memory bandwidth, alignment, branch, vector width에 제한된다.

## 응용 (Applications)

- numerical computing
- image·audio processing
- cryptography primitive
- search·filter·scan workload

## 흔한 오해 (Common Misunderstandings)

- vectorized API가 항상 SIMD를 쓴다는 보장은 없다.
- SIMD는 multi-threading과 다른 병렬성이다.
- 작은 데이터에서는 setup cost가 이득을 먹을 수 있다.
- precision·overflow 차이를 확인해야 한다.

## TMI

- AVX 같은 넓은 SIMD instruction은 CPU frequency를 낮출 수 있다.
- GPU는 SIMD와 비슷한 데이터 병렬성을 훨씬 큰 규모로 사용한다.
- Compiler report를 보면 왜 loop가 vectorize되지 않았는지 알 수 있다.

## 연습 / 확인 문제 (Exercises)

- Python loop와 NumPy vectorized 연산을 비교하라.
- branch가 있는 loop를 mask 기반 처리로 바꿔 보라.
- memory bandwidth가 speedup을 제한하는 예를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [분기 예측](Branch-Prediction.md)
- 다음: [메모리 레이아웃](Memory-Layout.md)

## 참조 (References)

- [Systems/Parallel-Computing/SIMD.md](../../Systems/Parallel-Computing/SIMD.md)
- [Systems/Computer-Architecture/Parallel-Architecture.md](../../Systems/Computer-Architecture/Parallel-Architecture.md)

