# 병렬 컴퓨팅 (Parallel Computing)

> 여러 연산을 동시에 수행하여 성능을 높이는 방법.

**선수지식**: [Systems/Operating-Systems/](../Operating-Systems/), [Systems/Computer-Architecture/](../Computer-Architecture/)

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

| 주제 | 파일 | Status |
|---|---|---|
| 병렬 컴퓨팅 모델 (공유 메모리, 분산 메모리) | Parallel-Models.md | Planned |
| 멀티스레딩과 동기화 | Multithreading.md | Planned |
| SIMD와 벡터 연산 | SIMD.md | Planned |
| GPU 아키텍처와 CUDA | GPU-and-CUDA.md | Planned |
| OpenMP / MPI | OpenMP-MPI.md | Planned |
| Amdahl의 법칙과 확장성 | Parallel-Scalability.md | Planned |

---

## 학습 순서

```text
Parallel-Models → Multithreading
       ↓
SIMD → GPU-and-CUDA
       ↓
OpenMP-MPI → Parallel-Scalability
```

---

## 연관 섹션

- [Systems/Computer-Architecture/](../Computer-Architecture/) — 멀티코어, 캐시, SIMD 하드웨어 기반
- [Systems/Operating-Systems/](../Operating-Systems/) — 스레드, 스케줄링, 동기화 기반
- [Engineering/Performance/](../../Engineering/Performance/) — 병렬 성능 측정과 병목 분석
- [AI/MLOps/](../../AI/MLOps/) — 분산 학습과 GPU 인프라 운영
