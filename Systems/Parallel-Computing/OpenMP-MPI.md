# OpenMP / MPI

- Level: Advanced
- Prerequisites: [Multithreading.md](Multithreading.md), [Parallel-Models.md](Parallel-Models.md), [Systems/Distributed-Systems/System-Models.md](../Distributed-Systems/System-Models.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

OpenMP와 MPI는 병렬 프로그램을 작성하는 대표적 모델이다. OpenMP는 공유 메모리 환경에서 thread 병렬화를 쉽게 표현하고, MPI는 분산 메모리 환경에서 프로세스들이 메시지를 주고받아 협력하게 한다.

## 직관 (Intuition)

OpenMP는 한 사무실 안에서 여러 사람이 같은 화이트보드를 보며 일하는 것과 비슷하다. MPI는 서로 다른 사무실의 사람들이 우편으로 메시지를 주고받으며 일하는 것에 가깝다. 공유 메모리와 분산 메모리의 차이가 핵심이다.

## 이론 (Theory)

OpenMP는 compiler directive로 loop parallelism, reduction, critical section 등을 표현한다. 같은 주소 공간을 공유하므로 데이터 race와 false sharing을 조심해야 한다.

MPI는 rank를 가진 프로세스들이 send/receive, broadcast, scatter/gather, reduce 같은 collective operation을 사용한다. 각 프로세스는 독립 메모리를 가지므로 데이터 분할과 통신 패턴 설계가 중요하다.

하이브리드 HPC 프로그램은 노드 내부에서는 OpenMP, 노드 간에는 MPI를 함께 쓰기도 한다.

## 구현 (Implementation)

OpenMP 스타일의 병렬 루프는 다음처럼 directive로 표현한다.

```c
#pragma omp parallel for reduction(+:sum)
for (int i = 0; i < n; i++) {
    sum += a[i];
}
```

MPI 스타일에서는 각 rank가 자기 chunk를 처리하고 reduce로 합친다. 실제 코드는 초기화, rank 확인, 통신 호출, 종료 처리가 필요하다.

## 복잡도 (Complexity)

OpenMP는 thread 수가 늘수록 lock contention, memory bandwidth, scheduling overhead가 병목이 된다. MPI는 통신 latency와 bandwidth, collective operation 비용이 지배적일 수 있다.

## 응용 (Applications)

- 과학 계산과 HPC
- 대규모 시뮬레이션
- 병렬 선형대수
- 클러스터 기반 수치 계산

## 흔한 오해 (Common Misunderstandings)

- OpenMP는 분산 클러스터 전체 메모리를 자동 공유하지 않는다.
- MPI는 어렵지만 명시적 통신 덕분에 성능 예측이 쉬운 경우가 많다.
- 병렬화 directive를 붙이면 항상 빠른 것은 아니다.
- reduction 변수와 shared variable을 구분하지 않으면 race가 생긴다.

## TMI

- embarrassingly parallel 문제는 MPI로도 매우 쉽게 확장된다.
- collective operation은 직접 send/receive를 짜는 것보다 최적화된 구현을 제공할 수 있다.
- NUMA 환경에서는 OpenMP도 메모리 배치가 성능에 큰 영향을 준다.

## 연습 / 확인 문제 (Exercises)

- OpenMP와 MPI의 메모리 모델 차이를 설명하라.
- reduction이 필요한 병렬 합산 예를 들어라.
- MPI 프로그램에서 통신 비용을 줄이는 전략을 세 가지 말하라.

## 이어서 읽기 (Reading Path)

- 이전: [GPU와 CUDA](GPU-and-CUDA.md)
- 다음: [병렬 확장성](Parallel-Scalability.md)

## 참조 (References)

- [Multithreading.md](Multithreading.md)
- [Parallel-Models.md](Parallel-Models.md)
- [Systems/Distributed-Systems/System-Models.md](../Distributed-Systems/System-Models.md)
- [Reference/Books.md](../../Reference/Books.md)
