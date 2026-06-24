# 락 경합과 Lock-Free 접근 (Lock Contention)

- Level: Advanced
- Prerequisites: [Systems/Operating-Systems/Synchronization.md](../../Systems/Operating-Systems/Synchronization.md), [Systems/Parallel-Computing/Multithreading.md](../../Systems/Parallel-Computing/Multithreading.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

락 경합은 여러 thread가 같은 lock을 기다리며 병렬성이 줄어드는 현상이다. Lock-free 접근은 일부 작업이 전체 lock 없이 진행되도록 설계한다.

## 직관 (Intuition)

계산대가 하나뿐이면 손님이 많아도 처리량은 늘지 않는다. 줄을 줄이려면 계산대를 나누거나 계산 자체를 줄여야 한다.

## 이론 (Theory)

Critical section 길이, lock acquisition 빈도, thread 수, scheduler preemption이 경합을 만든다. 완화 방법은 lock splitting, sharding, read-write lock, batching, immutable snapshot, atomic operation, queue 기반 설계가 있다. Lock-free는 deadlock을 줄일 수 있지만 ABA 문제, memory ordering, starvation 같은 난도가 높다.

## 구현 (Implementation)

```python
from collections import Counter

def aggregate(shards):
    total = Counter()
    for shard in shards:
        total.update(shard)
    return total
```

각 thread가 local shard에 기록하고 마지막에 합치면 공유 lock 빈도를 줄일 수 있다.

## 복잡도 (Complexity)

작업 자체는 `O(n)`이어도 lock wait time이 thread 수에 따라 증가할 수 있다. Sharding은 merge 비용과 memory를 추가한다.

## 응용 (Applications)

- shared cache·counter
- logging queue
- connection pool
- in-memory index

## 흔한 오해 (Common Misunderstandings)

- lock-free가 wait-free를 뜻하지 않는다.
- lock을 없애면 자동으로 안전해지는 것이 아니다.
- critical section이 짧아도 매우 자주 잡으면 병목이 된다.
- CPU 사용률이 높아도 spin wait일 수 있다.

## TMI

- Convoying은 lock 보유 thread가 지연되며 뒤 thread가 줄줄이 밀리는 현상이다.
- Atomic increment도 한 cache line을 두고 싸우면 느려진다.
- 단순한 mutex가 복잡한 lock-free 구조보다 빠른 경우도 많다.

## 연습 / 확인 문제 (Exercises)

- global counter와 sharded counter를 benchmark하라.
- critical section 길이를 늘려 throughput 변화를 관찰하라.
- deadlock, livelock, starvation을 구분하라.

## 이어서 읽기 (Reading Path)

- 이전: [지연 계산](Lazy-Evaluation.md)
- 다음: [스레드 풀 튜닝](Thread-Pool-Tuning.md)

## 참조 (References)

- [Systems/Operating-Systems/Synchronization.md](../../Systems/Operating-Systems/Synchronization.md)
- [Systems/Operating-Systems/Deadlock.md](../../Systems/Operating-Systems/Deadlock.md)

