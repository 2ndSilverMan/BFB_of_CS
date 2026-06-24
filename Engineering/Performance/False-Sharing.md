# False Sharing과 캐시 라인 (False Sharing)

- Level: Advanced
- Prerequisites: [Systems/Computer-Architecture/Memory-Hierarchy.md](../../Systems/Computer-Architecture/Memory-Hierarchy.md), [Systems/Operating-Systems/Synchronization.md](../../Systems/Operating-Systems/Synchronization.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

False sharing은 서로 다른 thread가 다른 변수를 갱신하지만 그 변수들이 같은 cache line에 있어 불필요한 cache coherence traffic이 발생하는 현상이다.

## 직관 (Intuition)

각자 다른 종이에 쓰는 줄 알았는데 실제로는 같은 종이 한 장을 번갈아 빼앗는 꼴이다. 데이터는 공유하지 않아도 cache line은 공유할 수 있다.

## 이론 (Theory)

CPU cache coherence protocol은 cache line 단위로 ownership을 관리한다. 한 core가 line을 write하면 다른 core의 line copy가 invalidation된다. 같은 line 안의 독립 counter를 여러 core가 자주 쓰면 line bouncing이 발생한다. Padding, per-thread shard, batching으로 줄일 수 있다.

## 구현 (Implementation)

```text
bad:  counter[0] counter[1] counter[2] counter[3]  # 같은 cache line 가능
good: counter[0] padding ... counter[1] padding ... # line 분리
```

실제 padding 크기는 CPU cache line size와 언어의 object layout을 확인해야 한다.

## 복잡도 (Complexity)

알고리즘 복잡도는 변하지 않지만 core 수가 늘수록 coherence 비용이 증가해 scaling이 꺾인다.

## 응용 (Applications)

- multi-threaded counter
- work queue statistic
- lock-free data structure
- high-throughput telemetry

## 흔한 오해 (Common Misunderstandings)

- lock이 없어도 공유 cache line은 병목이 될 수 있다.
- 읽기만 하는 데이터는 보통 문제가 작고, 빈번한 write가 핵심이다.
- padding은 memory footprint를 늘린다.
- profiler에 함수 hotspot보다 hardware counter로 먼저 보일 수 있다.

## TMI

- “false”라는 이름은 논리적으로 공유하지 않는데 하드웨어 단위에서는 공유한다는 뜻이다.
- Per-CPU/per-thread counter는 합산 비용과 write locality를 교환한다.
- Cache line size는 흔히 64 bytes지만 가정으로 박아 두면 이식성이 떨어진다.

## 연습 / 확인 문제 (Exercises)

- adjacent counter와 padded counter의 throughput을 비교하라.
- core 수를 늘리며 scaling curve를 그려라.
- false sharing과 true sharing의 차이를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [메모리 레이아웃](Memory-Layout.md)
- 다음: [실전 복잡도](Practical-Complexity.md)

## 참조 (References)

- [Systems/Computer-Architecture/Memory-Hierarchy.md](../../Systems/Computer-Architecture/Memory-Hierarchy.md)
- [Systems/Parallel-Computing/Multithreading.md](../../Systems/Parallel-Computing/Multithreading.md)

