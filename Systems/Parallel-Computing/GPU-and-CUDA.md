# GPU 아키텍처와 CUDA (GPU Architecture and CUDA)

- Level: Advanced
- Prerequisites: [SIMD.md](SIMD.md), [Parallel-Models.md](Parallel-Models.md), [AI/MLOps/Distributed-Training.md](../../AI/MLOps/Distributed-Training.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

GPU는 많은 수의 단순한 연산 유닛으로 대규모 데이터 병렬 작업을 처리하는 하드웨어다. CUDA는 NVIDIA GPU에서 kernel을 작성하고 thread/block/grid 구조로 병렬 실행을 제어하는 프로그래밍 모델이다.

## 직관 (Intuition)

CPU가 소수의 똑똑한 작업자라면, GPU는 많은 단순 작업자가 같은 종류의 일을 한꺼번에 처리하는 공장에 가깝다. 작업을 작은 독립 조각으로 잘게 나눌 수 있을수록 GPU가 강해진다.

## 이론 (Theory)

CUDA 실행 모델은 다음 계층을 사용한다.

- Thread: 실제 작업 단위
- Block: thread들의 묶음, shared memory를 공유
- Grid: block들의 전체 실행 집합
- Warp: 보통 같은 명령을 함께 실행하는 thread 묶음

성능은 occupancy, memory coalescing, shared memory 사용, warp divergence, host-device transfer 비용에 영향을 받는다. GPU는 연산량이 많아도 데이터 전송과 동기화가 많으면 기대한 성능이 나오지 않는다.

## 구현 (Implementation)

CUDA kernel의 개념적 형태는 각 thread가 자기 index의 데이터를 처리하는 것이다.

```c
__global__ void add(float* a, float* b, float* c, int n) {
    int i = blockIdx.x * blockDim.x + threadIdx.x;
    if (i < n) {
        c[i] = a[i] + b[i];
    }
}
```

실무에서는 직접 CUDA를 쓰기보다 PyTorch, CUDA libraries, vendor-optimized kernel을 사용하는 경우가 많다.

## 복잡도 (Complexity)

연산 복잡도는 같아도 병렬 처리량이 높아 wall-clock 시간이 줄 수 있다. 하지만 작은 입력, 잦은 CPU-GPU 전송, 분기 많은 코드, 낮은 arithmetic intensity는 GPU 이점을 줄인다.

## 응용 (Applications)

- 딥러닝 학습과 추론
- 행렬 곱과 선형대수
- 물리 시뮬레이션
- 이미지/비디오 처리

## 흔한 오해 (Common Misunderstandings)

- GPU가 CPU보다 모든 작업에서 빠른 것은 아니다.
- GPU 메모리는 CPU 메모리와 별도일 수 있어 전송 비용을 고려해야 한다.
- thread를 많이 만들면 자동으로 빠른 것이 아니다. memory bottleneck이 흔하다.
- CUDA는 NVIDIA 생태계에 특화되어 있으며, 다른 GPU에는 다른 API가 필요할 수 있다.

## TMI

- Tensor Core는 행렬 연산을 특화해 딥러닝 성능을 크게 높인다.
- mixed precision은 메모리와 연산량을 줄이지만 numerical stability를 확인해야 한다.
- GPU 성능 최적화는 알고리즘보다 메모리 계층 이해가 더 중요할 때가 많다.

## 연습 / 확인 문제 (Exercises)

- thread, block, grid의 관계를 설명하라.
- warp divergence가 성능을 낮추는 이유를 말하라.
- GPU를 쓰면 오히려 느릴 수 있는 작업 예를 들어라.

## 이어서 읽기 (Reading Path)

- 이전: [SIMD](SIMD.md)
- 다음: [OpenMP / MPI](OpenMP-MPI.md)

## 참조 (References)

- [SIMD.md](SIMD.md)
- [Parallel-Models.md](Parallel-Models.md)
- [AI/MLOps/Distributed-Training.md](../../AI/MLOps/Distributed-Training.md)
- [Reference/Books.md](../../Reference/Books.md)
