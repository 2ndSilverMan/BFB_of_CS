# 멀티스레딩 (Multithreading)

- Level: Intermediate
- Prerequisites: [Systems/Parallel-Computing/Parallel-Models.md](Parallel-Models.md), [Systems/Operating-Systems/Synchronization.md](../Operating-Systems/Synchronization.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

멀티스레딩은 한 process의 address space를 공유하는 여러 thread가 동시에 작업하도록 구성하는 방법이다. 낮은 공유 비용 대신 race condition, deadlock, visibility 문제를 제어해야 한다.

## 직관 (Intuition)

한 문서를 여러 사람이 동시에 편집하면 빠르지만 같은 문단을 덮어쓸 수 있다. 작업 영역을 분리하거나 수정 순서를 lock·message로 조정해야 한다.

## 이론 (Theory)

정확성의 핵심은 shared mutable state 접근에 happens-before 관계를 세우는 것이다. mutex는 mutual exclusion, condition variable은 상태 변화 대기, semaphore는 동시 사용량, atomic은 제한된 lock-free update를 제공한다.

Thread pool은 task마다 thread를 만들지 않고 worker를 재사용한다. CPU-bound는 core 수와 oversubscription을, I/O-bound는 blocking 시간과 queue를 고려한다.

## 구현 (Implementation)

```python
from concurrent.futures import ThreadPoolExecutor
from threading import Lock

total = 0
lock = Lock()


def add(value):
    global total
    with lock:
        total += value


with ThreadPoolExecutor(max_workers=4) as pool:
    list(pool.map(add, range(100)))
```

## 복잡도 (Complexity)

Lock operation은 보통 낮은 비용이지만 contention 시 queueing과 context switch가 발생한다. Thread 수가 core보다 지나치게 많으면 scheduling·cache 비용이 증가한다.

## 응용 (Applications)

- server request 처리
- UI와 background 작업 분리
- parallel pipeline
- I/O overlap과 multicore computation

## 흔한 오해 (Common Misunderstandings)

- 한 번 잘 실행됐다고 race가 없는 것은 아니다.
- atomic 여러 개를 조합한 전체 연산은 자동으로 atomic하지 않다.
- lock을 많이 쓰면 안전할 수 있어도 deadlock·contention이 생긴다.
- 언어 runtime에 따라 CPU parallelism 제약이 다르다.

## TMI

- false sharing은 다른 변수라도 같은 cache line이면 성능을 떨어뜨린다.
- work stealing scheduler는 idle worker가 다른 queue의 task를 가져온다.
- structured concurrency는 child task lifetime을 lexical scope에 묶는다.

## 연습 / 확인 문제 (Exercises)

- lost update race를 재현하고 lock으로 고쳐라.
- lock ordering으로 deadlock을 예방하라.
- CPU-bound와 I/O-bound pool 크기 기준을 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [병렬 컴퓨팅 모델](Parallel-Models.md)
- 다음: [SIMD](SIMD.md)

## 참조 (References)

- [Systems/Operating-Systems/Synchronization.md](../Operating-Systems/Synchronization.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
