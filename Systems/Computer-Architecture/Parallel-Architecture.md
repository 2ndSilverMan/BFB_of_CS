# 병렬 아키텍처 (멀티코어, GPU) (Parallel Architecture)

- Level: Advanced
- Prerequisites: [Systems/Computer-Architecture/Memory-Hierarchy.md](Memory-Hierarchy.md), [Systems/Computer-Architecture/Pipelining.md](Pipelining.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

병렬 아키텍처는 여러 처리 장치가 동시에 연산하는 하드웨어다. 멀티코어 CPU, SIMD 벡터 유닛, GPU의 대규모 스레드, 그리고 이들을 잇는 메모리·캐시 일관성 구조를 다룬다.

## 직관 (Intuition)

한 코어의 클록을 계속 높이는 것은 전력·발열 한계(파워 월)에 부딪혔다. 그래서 "더 빠른 하나" 대신 "여러 개"로 방향을 틀었다. 작업을 잘게 나눠 여러 코어/스레드가 동시에 처리하면 같은 시간에 더 많은 일을 한다 — 단, 데이터를 공유하면 일관성과 동기화 문제가 따라온다.

## 이론 (Theory)

**플린 분류**: SISD, **SIMD**(한 명령 다중 데이터, 벡터), **MIMD**(독립 명령·데이터, 멀티코어), SPMD(GPU 모델).

**멀티코어**: 코어마다 L1/L2, 공유 L3. **캐시 일관성(coherence)**을 MESI 같은 프로토콜로 유지한다. 메모리 일관성(consistency) 모델이 재배열 규칙을 정한다.

**GPU**: 수천 개의 경량 코어가 SIMT(single instruction multiple threads)로 동작. 높은 처리량·메모리 대역폭에 최적화, 분기 발산(warp divergence)에 취약. 공유 메모리·코얼레싱이 성능 열쇠다.

## 구현 (Implementation)

```text
SIMD: 한 명령이 벡터 레인 여러 개를 동시 연산
  [a0 a1 a2 a3] + [b0 b1 b2 b3] = [a0+b0 a1+b1 a2+b2 a3+b3]

GPU(SIMT): 수천 스레드가 같은 커널을 다른 데이터에 실행
  thread i: C[i] = A[i] + B[i]    # 인덱스만 다름, 동시에 수천 개
```

## 복잡도 (Complexity)

이론적 속도 향상은 코어/레인 수에 비례하지만, 암달의 법칙(순차 부분), 메모리 대역폭, 동기화·일관성 트래픽이 한계를 만든다. GPU는 처리량은 높지만 지연이 크고, 데이터 전송(PCIe)이 병목이 되기도 한다.

## 응용 (Applications)

- 딥러닝 학습·추론(GPU/TPU)
- 과학 시뮬레이션·렌더링
- 멀티스레드 서버·데이터 처리
- 미디어 코덱·신호 처리(SIMD)

## 흔한 오해 (Common Misunderstandings)

- 코어가 2배라고 2배 빨라지지 않는다(암달·동기화·대역폭).
- GPU가 항상 CPU보다 빠르지 않다 — 데이터 병렬성이 크고 분기가 적을 때 유리하다.
- 캐시 일관성은 자동이지만 공짜가 아니다(일관성 트래픽, false sharing).
- SIMD는 분기·불규칙 접근에 약하다.

## TMI

- "파워 월"과 "메모리 월"이 단일 코어 클록 경쟁을 끝내고 멀티코어 시대를 열었다(2000년대 중반).
- GPU는 그래픽용으로 태어났지만 CUDA(2007) 이후 범용 계산(GPGPU)의 주역이 됐다.
- warp divergence: 같은 워프의 스레드들이 서로 다른 분기를 타면 직렬화되어 성능이 떨어진다.

## 연습 / 확인 문제 (Exercises)

- 플린 분류로 멀티코어 CPU와 GPU를 분류하라.
- SIMD가 유리한 연산과 불리한 연산을 각각 들어라.
- false sharing이 멀티코어 성능을 해치는 시나리오를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [입출력 (I/O) 시스템](IO-Systems.md)
- 다음: [Systems/Parallel-Computing/Parallel-Models.md](../Parallel-Computing/Parallel-Models.md), [Systems/Parallel-Computing/GPU-and-CUDA.md](../Parallel-Computing/GPU-and-CUDA.md)

## 참조 (References)

- [Systems/Parallel-Computing/Parallel-Models.md](../Parallel-Computing/Parallel-Models.md)
- [Algorithms/Parallel-Algorithms.md](../../Algorithms/Parallel-Algorithms.md)
- [Reference/Books.md](../../Reference/Books.md)
