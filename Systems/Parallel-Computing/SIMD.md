# SIMD와 벡터 연산 (SIMD and Vector Operations)

- Level: Intermediate
- Prerequisites: [Parallel-Models.md](Parallel-Models.md), [Systems/Computer-Architecture/CPU-and-ISA.md](../Computer-Architecture/CPU-and-ISA.md), [Math/Linear-Algebra/Vectors.md](../../Math/Linear-Algebra/Vectors.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

SIMD(Single Instruction, Multiple Data)는 하나의 명령으로 여러 데이터 요소에 같은 연산을 동시에 적용하는 병렬 처리 방식이다. CPU의 벡터 명령어와 GPU의 대규모 데이터 병렬 실행 모두 SIMD/SIMT적 사고와 연결된다.

## 직관 (Intuition)

숫자 하나씩 더하는 대신 숫자 4개, 8개, 16개를 한 묶음으로 집어 한 번에 더한다고 생각하면 된다. 이미지 처리, 행렬 연산, 오디오 처리처럼 같은 연산을 많은 데이터에 반복할 때 특히 유리하다.

## 이론 (Theory)

SIMD는 데이터 병렬성(data parallelism)을 활용한다. 예를 들어 벡터 덧셈

$$
c_i=a_i+b_i
$$

는 각 $i$에 대한 연산이 독립이므로 SIMD로 쉽게 병렬화된다. 성능은 vector width, memory alignment, cache locality, branch divergence, compiler auto-vectorization에 영향을 받는다.

조건 분기가 데이터마다 달라지면 같은 명령을 동시에 적용하기 어렵다. 또한 메모리가 연속적이지 않으면 gather/scatter 비용이 커질 수 있다.

## 구현 (Implementation)

Python 수준에서는 직접 SIMD 명령을 쓰지 않지만, 배열 라이브러리는 내부에서 벡터화된 연산을 활용할 수 있다.

```python
def vector_add(a, b):
    return [x + y for x, y in zip(a, b)]


a = [1, 2, 3, 4]
b = [10, 20, 30, 40]
print(vector_add(a, b))
```

C/C++에서는 compiler auto-vectorization, intrinsic, 또는 BLAS 같은 라이브러리를 통해 SIMD를 활용한다.

## 복잡도 (Complexity)

알고리즘의 Big-O는 그대로일 수 있지만, 한 명령이 처리하는 데이터 수가 늘어 상수 인자가 크게 줄어든다. 실제 speedup은 memory bandwidth와 alignment에 막힐 수 있다.

## 응용 (Applications)

- 행렬/벡터 연산
- 이미지 필터와 비디오 처리
- 암호·압축·해시 연산
- 딥러닝 inference kernel

## 흔한 오해 (Common Misunderstandings)

- SIMD를 쓰면 모든 코드가 자동으로 빨라지는 것은 아니다.
- 메모리 접근 패턴이 나쁘면 연산 병렬성이 있어도 성능이 안 나온다.
- branch가 많은 코드는 SIMD 효율이 낮을 수 있다.
- 고수준 언어의 “벡터화”와 하드웨어 SIMD는 관련 있지만 완전히 같은 말은 아니다.

## TMI

- AVX, NEON 같은 ISA 확장이 CPU SIMD 예시다.
- Structure of Arrays(SoA)는 Array of Structures(AoS)보다 SIMD에 유리한 경우가 많다.
- GPU의 SIMT는 여러 thread가 같은 instruction stream을 따라가는 방식으로 SIMD와 닮았다.

## 연습 / 확인 문제 (Exercises)

- 벡터 덧셈이 SIMD에 적합한 이유를 설명하라.
- 분기와 비연속 메모리 접근이 SIMD 성능을 낮추는 이유를 말하라.
- SoA와 AoS가 SIMD에 미치는 영향을 예로 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [병렬 모델](Parallel-Models.md)
- 다음: [GPU와 CUDA](GPU-and-CUDA.md)

## 참조 (References)

- [Parallel-Models.md](Parallel-Models.md)
- [Systems/Computer-Architecture/CPU-and-ISA.md](../Computer-Architecture/CPU-and-ISA.md)
- [Math/Linear-Algebra/Vectors.md](../../Math/Linear-Algebra/Vectors.md)
- [Reference/Books.md](../../Reference/Books.md)
