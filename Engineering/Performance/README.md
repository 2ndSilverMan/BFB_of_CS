# 성능 공학 (Performance Engineering)

> 소프트웨어 시스템의 병목을 찾고, 측정하고, 개선하는 방법론.

**선수지식**: [Programming/](../../Programming/), [Systems/Computer-Architecture/](../../Systems/Computer-Architecture/), [Systems/Operating-Systems/](../../Systems/Operating-Systems/)

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

### 측정과 프로파일링

| 주제 | 파일 | Status |
|---|---|---|
| 벤치마킹 기초 — 마이크로/매크로 벤치마크, 워밍업 | Benchmarking-Basics.md | Planned |
| CPU 프로파일링 — 샘플링 vs 인스트루멘테이션 | CPU-Profiling.md | Planned |
| 메모리 프로파일링 — 힙 분석, 누수 탐지 | Memory-Profiling.md | Planned |
| I/O 프로파일링 — 디스크/네트워크 병목 분석 | IO-Profiling.md | Planned |
| 플레임 그래프 읽기 | Flame-Graphs.md | Planned |

### 하드웨어 기반 최적화

| 주제 | 파일 | Status |
|---|---|---|
| 캐시 친화적 코드 — 공간적/시간적 지역성 | Cache-Friendly-Code.md | Planned |
| 분기 예측과 파이프라인 최적화 | Branch-Prediction.md | Planned |
| SIMD / 벡터화 | SIMD-Vectorization.md | Planned |
| 메모리 레이아웃 — SoA vs AoS | Memory-Layout.md | Planned |
| False Sharing과 캐시 라인 | False-Sharing.md | Planned |

### 알고리즘 & 자료구조 최적화

| 주제 | 파일 | Status |
|---|---|---|
| 복잡도 분석 재검토 — 상수 인자와 실제 성능 | Practical-Complexity.md | Planned |
| 메모이제이션과 캐싱 전략 | Memoization-Caching.md | Planned |
| 지연 계산 (Lazy Evaluation) | Lazy-Evaluation.md | Planned |

### 동시성 성능

| 주제 | 파일 | Status |
|---|---|---|
| 락 경합 최소화 — Lock-Free 자료구조 | Lock-Contention.md | Planned |
| 스레드 풀 튜닝 | Thread-Pool-Tuning.md | Planned |
| 비동기 I/O — Event Loop, io_uring | Async-IO.md | Planned |

### 시스템 수준 최적화

| 주제 | 파일 | Status |
|---|---|---|
| 데이터베이스 쿼리 최적화 — 인덱스, 실행 계획 | Database-Query-Optimization.md | Planned |
| 네트워크 성능 — 커넥션 풀링, 직렬화 포맷 | Network-Performance.md | Planned |
| CDN과 캐싱 계층 설계 | CDN-Caching.md | Planned |
| JIT 컴파일과 런타임 최적화 | JIT-Optimization.md | Planned |

---

## 학습 순서

```text
벤치마킹 & 프로파일링
           ↓
하드웨어 기반 최적화
(캐시, 분기 예측, SIMD)
           ↓
알고리즘 & 자료구조 최적화
           ↓
동시성 성능 / 시스템 수준 최적화
```

---

## 연관 섹션

- [Systems/Computer-Architecture/](../../Systems/Computer-Architecture/) — 캐시 계층, 파이프라이닝 원리
- [Systems/Operating-Systems/](../../Systems/Operating-Systems/) — 스케줄링, 메모리 관리
- [Systems/Parallel-Computing/](../../Systems/Parallel-Computing/) — SIMD, 동시성 모델
- [Algorithms/](../../Algorithms/) — 알고리즘 복잡도와 실제 성능의 관계
- [Engineering/Testing/](../Testing/) — 성능 회귀를 잡는 부하 테스트
