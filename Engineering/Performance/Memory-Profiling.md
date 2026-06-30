# 메모리 프로파일링 (Memory Profiling)

- Level: Intermediate
- Prerequisites: [Systems/Operating-Systems/Memory-Management.md](../../Systems/Operating-Systems/Memory-Management.md), [Engineering/Performance/Benchmarking-Basics.md](Benchmarking-Basics.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

메모리 프로파일링은 프로그램의 allocation, heap 사용량, object lifetime, leak, fragmentation을 측정해 메모리 병목을 찾는 절차다.

## 직관 (Intuition)

CPU 시간이 빠져나가는 곳을 찾듯이 메모리가 오래 붙잡히는 곳을 찾는다. “많이 할당한다”와 “많이 살아남는다”는 다른 문제다.

## 이론 (Theory)

Peak RSS, heap size, allocation rate, retained size, GC pause를 구분한다. Leak은 더 이상 필요하지 않은 object가 reference 때문에 해제되지 않는 상태이고, fragmentation은 빈 공간 총량은 충분하지만 연속 공간이 부족한 상태다. Snapshot 비교, allocation tracing, sampling heap profile을 함께 사용하면 누가 만들었고 누가 붙잡는지 추적할 수 있다.

### Heap과 lifetime

메모리 프로파일링은 allocation rate, retained size, object lifetime, reference path를 분리해 본다. 많은 allocation이 문제인지, 해제되지 않아 retained heap이 커지는지, GC pause가 문제인지에 따라 해결책이 다르다.

Leak은 반드시 객체 수가 무한히 증가하는 형태만은 아니다. Cache key 증가, listener 미해제, thread-local, global registry, queue backlog처럼 의도한 참조가 lifetime을 과하게 늘릴 수 있다.

## 구현 (Implementation)

```python
import tracemalloc

tracemalloc.start()

data = [bytearray(1024) for _ in range(10_000)]
snapshot = tracemalloc.take_snapshot()

for stat in snapshot.statistics("lineno")[:5]:
    print(stat)
```

## 복잡도 (Complexity)

정밀 tracing은 allocation event 수에 비례해 overhead가 커진다. Sampling 방식은 부담이 작지만 작은 allocation hotspot을 놓칠 수 있다.

## 응용 (Applications)

- memory leak 원인 추적
- GC pressure 감소
- cache 크기 조정
- container memory limit 산정

## 흔한 오해 (Common Misunderstandings)

- RSS 증가는 항상 leak이 아니다. allocator arena나 page cache일 수 있다.
- free를 호출해도 OS에 즉시 반환되지 않을 수 있다.
- 평균 메모리보다 peak가 장애를 만든다.
- 작은 object를 많이 만드는 비용은 CPU와 memory 양쪽에 나타난다.

## TMI

- GC 언어에서도 leak은 발생한다. reference가 살아 있으면 collector가 지울 수 없다.
- Native extension이 있으면 언어 런타임 profiler만으로 부족할 수 있다.
- 메모리 최적화는 cache locality 개선으로 CPU 성능도 같이 좋아지는 경우가 많다.

## 연습 / 확인 문제 (Exercises)

- heap snapshot 두 개를 비교해 증가한 object type을 찾으라.
- cache의 최대 크기를 바꿔 peak RSS와 hit rate를 비교하라.
- allocation rate가 높은 loop를 재사용 buffer로 고쳐 보라.

## 이어서 읽기 (Reading Path)

- 이전: [CPU 프로파일링](CPU-Profiling.md)
- 다음: [I/O 프로파일링](IO-Profiling.md)

## 참조 (References)

- [Systems/Operating-Systems/Memory-Management.md](../../Systems/Operating-Systems/Memory-Management.md)
- [Systems/Computer-Architecture/Memory-Hierarchy.md](../../Systems/Computer-Architecture/Memory-Hierarchy.md)
