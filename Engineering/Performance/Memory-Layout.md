# 메모리 레이아웃 (Memory Layout)

- Level: Advanced
- Prerequisites: [Systems/Computer-Architecture/Memory-Hierarchy.md](../../Systems/Computer-Architecture/Memory-Hierarchy.md), [Engineering/Performance/Cache-Friendly-Code.md](Cache-Friendly-Code.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

메모리 레이아웃은 데이터가 주소 공간에 배치되는 방식이다. Array of Structs(AoS)와 Struct of Arrays(SoA)는 대표적인 배치 선택이다.

## 직관 (Intuition)

CPU cache는 근처 데이터를 한 번에 가져온다. 실제로 같이 쓰는 값을 붙여 두면 좋고, 안 쓰는 값을 함께 끌고 오면 낭비가 된다.

## 이론 (Theory)

AoS는 객체 단위 접근이 쉽고 locality가 좋다. SoA는 특정 field만 대량 처리할 때 cache 효율과 SIMD 가능성이 높다. Padding, alignment, pointer chasing, indirection, object header도 성능에 영향을 준다. Layout 변경은 API·readability·mutation pattern과 함께 평가해야 한다.

### Layout이 성능이 되는 이유

메모리 성능은 데이터가 cache line에 어떻게 배치되는지에 크게 좌우된다. Array of Structs는 객체 단위 접근에 좋고, Struct of Arrays는 특정 필드만 대량 처리할 때 SIMD와 cache locality에 유리하다.

Padding과 alignment는 크기를 늘릴 수 있지만 misaligned access나 false sharing을 줄일 수 있다. 구조체 크기와 hot field 위치는 profile을 보고 조정한다.

## 구현 (Implementation)

```text
AoS: [{x,y,z}, {x,y,z}, {x,y,z}]
SoA: {x:[...], y:[...], z:[...]}
```

위치의 x좌표만 모두 더한다면 SoA가 필요한 데이터만 연속으로 읽는다. 한 객체의 모든 field를 자주 쓰면 AoS가 자연스럽다.

## 복잡도 (Complexity)

연산 복잡도는 같아도 cache miss와 memory bandwidth 비용이 달라진다. Pointer chasing은 prefetch가 어렵고 latency가 누적된다.

## 응용 (Applications)

- game entity component system
- columnar database
- vectorized analytics
- simulation·graphics

## 흔한 오해 (Common Misunderstandings)

- SoA가 항상 AoS보다 빠른 것은 아니다.
- 작은 데이터셋은 cache 안에 들어가 차이가 작다.
- Layout 최적화는 측정 없이 적용하면 유지보수 비용만 늘 수 있다.
- 언어 런타임 object layout도 고려해야 한다.

## TMI

- Columnar storage는 query가 필요한 column만 읽게 해 analytics에 유리하다.
- Packed struct는 메모리를 줄이지만 misaligned access 비용을 만들 수 있다.
- Data-oriented design은 객체보다 access pattern을 먼저 본다.

## 연습 / 확인 문제 (Exercises)

- AoS와 SoA로 좌표 배열 합산 benchmark를 작성하라.
- Padding 때문에 struct 크기가 커지는 예를 계산하라.
- Pointer 기반 linked list와 array scan을 cache 관점에서 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [SIMD / 벡터화](SIMD-Vectorization.md)
- 다음: [False Sharing](False-Sharing.md)

## 참조 (References)

- [Systems/Computer-Architecture/Memory-Hierarchy.md](../../Systems/Computer-Architecture/Memory-Hierarchy.md)
- [Systems/Computer-Architecture/Data-Representation.md](../../Systems/Computer-Architecture/Data-Representation.md)
