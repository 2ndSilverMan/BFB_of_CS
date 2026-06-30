# 캐시 친화적 코드 (Cache-Friendly Code)

- Level: Intermediate
- Prerequisites: [Systems/Computer-Architecture/CPU-and-ISA.md](../../Systems/Computer-Architecture/CPU-and-ISA.md), [Data-Structures/Array.md](../../Data-Structures/Array.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

캐시 친화적 코드는 spatial·temporal locality를 높여 느린 main memory 접근을 줄인다. 연속 memory 순회, compact data layout, blocking이 핵심 기법이다.

## 직관 (Intuition)

책을 한 권씩 먼 창고에서 가져오기보다 가까운 책상에 필요한 묶음을 올려두고 순서대로 읽는다. CPU cache도 주변 byte를 cache line 단위로 가져온다.

## 이론 (Theory)

Row-major 행렬은 행을 연속 순회할 때 cache line을 잘 활용한다. Working set이 cache보다 크면 capacity miss, 나쁜 mapping은 conflict miss가 난다. Blocking은 큰 문제를 cache에 맞는 tile로 나눈다. Pointer-heavy structure는 locality와 prefetch가 불리하다.

### Locality의 종류

Temporal locality는 같은 데이터를 곧 다시 쓰는 성질이고, spatial locality는 가까운 주소의 데이터를 함께 쓰는 성질이다. CPU cache는 이 두 성질을 기대하므로 연속 배열 순회, loop tiling, 데이터 압축이 성능에 큰 영향을 줄 수 있다.

Cache-friendly 최적화는 알고리즘을 복잡하게 만들 수 있으므로 hot path에만 적용한다. 데이터 구조 변경은 correctness와 동시성 영향도 함께 검토한다.

## 구현 (Implementation)

```python
def row_major_sum(matrix):
    total = 0
    for row in matrix:
        for value in row:
            total += value
    return total
```

실제 효과는 contiguous numeric array와 compiler·hardware counter로 측정한다.

## 복잡도 (Complexity)

두 순회 모두 점근적으로 `O(n^2)`여도 cache miss 수가 크게 달라 실제 시간이 달라진다. 성능 모델에는 memory bandwidth와 arithmetic intensity가 중요하다.

## 응용 (Applications)

- matrix·image·simulation kernel
- database columnar processing
- game ECS와 batch processing
- high-throughput server data structure

## 흔한 오해 (Common Misunderstandings)

- 같은 Big-O면 실제 성능도 같다는 뜻이 아니다.
- 작은 object를 무조건 연속화하면 mutation·ownership 비용이 커질 수 있다.
- cache 크기 하나만 보면 안 되고 여러 level과 associativity를 고려한다.
- microbenchmark 효과가 end-to-end 병목이 아닐 수 있다.

## TMI

- structure of arrays는 한 field만 대량 처리할 때 array of structures보다 유리할 수 있다.
- hardware prefetcher는 규칙적 접근에 강하다.
- false sharing은 thread별 데이터라도 같은 cache line을 수정할 때 생긴다.

## 연습 / 확인 문제 (Exercises)

- row/column 순회 시간을 큰 numeric matrix에서 비교하라.
- AoS와 SoA layout의 장단점을 설명하라.
- tiled matrix multiplication의 tile 크기 역할을 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [CPU 프로파일링](CPU-Profiling.md)
- 다음: [메모리 레이아웃](Memory-Layout.md)

## 참조 (References)

- [Systems/Computer-Architecture/CPU-and-ISA.md](../../Systems/Computer-Architecture/CPU-and-ISA.md)
- [Reference/Books.md](../../Reference/Books.md)
