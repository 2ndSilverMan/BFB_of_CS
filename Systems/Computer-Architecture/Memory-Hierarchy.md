# 메모리 계층 (Memory Hierarchy)

- Level: Intermediate
- Prerequisites: [Systems/Computer-Architecture/Data-Representation.md](Data-Representation.md), [Systems/Computer-Architecture/CPU-and-ISA.md](CPU-and-ISA.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

메모리 계층은 속도·용량·비용이 다른 저장 장치를 계층적으로 배치한 구조다. 레지스터→캐시(L1/L2/L3)→주기억장치(RAM)→보조기억장치(SSD/HDD) 순으로 느려지고 커진다. 캐싱과 지역성으로 빠른 계층의 이점을 살린다.

## 직관 (Intuition)

빠른 메모리는 비싸고 작고, 큰 메모리는 싸고 느리다. 둘 다 갖고 싶다면 "자주 쓰는 것은 빠른 곳에, 나머지는 느린 곳에" 두면 된다. 프로그램이 같은 데이터를 반복하거나(시간 지역성) 가까운 데이터를 잇따라 쓰는(공간 지역성) 경향 덕분에 이 전략이 잘 통한다.

## 이론 (Theory)

**지역성(locality)**: 시간 지역성(최근 쓴 것 다시 씀), 공간 지역성(인접한 것 곧 씀).

**캐시**: 블록(라인) 단위로 데이터를 담는다. 매핑 방식은 직접/집합 연관/완전 연관. 교체 정책 LRU 등. 평균 메모리 접근 시간

$$\text{AMAT}=\text{hit time}+\text{miss rate}\times\text{miss penalty}$$

미스 종류: compulsory(최초), capacity(용량 부족), conflict(매핑 충돌). 쓰기 정책은 write-through/write-back. 계층마다 이 원리가 반복된다.

## 구현 (Implementation)

```python
# 공간 지역성: 행 우선 배열은 연속 접근이 캐시 친화적
def row_major_sum(matrix):
    total = 0
    for row in matrix:            # 연속된 메모리를 순회 → 캐시 히트↑
        for x in row:
            total += x
    return total
# 같은 행렬을 열 우선으로 접근하면 캐시 미스가 급증한다.
```

## 복잡도 (Complexity)

접근 시간은 레지스터(<1ns), L1(~1ns), L3(~10ns), RAM(~100ns), SSD(~100µs)로 계층마다 수십~수천 배 차이가 난다. 알고리즘의 빅오가 같아도 캐시 친화성에 따라 실제 속도가 수 배 차이 날 수 있어, 메모리 접근 패턴이 성능의 핵심이다.

## 응용 (Applications)

- 캐시 친화적 자료구조·알고리즘 설계
- 행렬 연산의 블로킹(타일링)
- 데이터베이스·파일 시스템 버퍼 캐시
- GPU의 메모리 계층 최적화

## 흔한 오해 (Common Misunderstandings)

- 캐시는 프로그래머가 명시적으로 관리하지 않는다(하드웨어 자동). 단, 접근 패턴으로 영향을 준다.
- 빅오가 작아도 캐시 미스가 많으면 느릴 수 있다.
- "메모리는 균일하게 빠르다"는 가정은 틀리다 — 계층마다 큰 차이.
- write-back이 항상 빠르지 않다(일관성·복구 비용 트레이드오프).

## TMI

- "메모리 장벽(memory wall)"은 CPU 속도가 메모리 속도보다 훨씬 빠르게 발전해 생긴 격차를 가리킨다.
- 행렬 곱의 캐시 블로킹은 같은 빅오에서 수 배 빠른 대표적 최적화다.
- false sharing은 서로 다른 코어가 같은 캐시 라인을 다퉈 성능이 급락하는 미묘한 문제다.

## 연습 / 확인 문제 (Exercises)

- 행 우선과 열 우선 배열 순회의 캐시 미스 차이를 설명하라.
- AMAT 공식으로 hit/miss 시나리오의 평균 접근 시간을 계산하라.
- 시간 지역성과 공간 지역성의 예를 각각 들어라.

## 이어서 읽기 (Reading Path)

- 이전: [파이프라이닝](Pipelining.md)
- 다음: [가상 메모리](Virtual-Memory-Hardware.md), [Engineering/Performance/Cache-Friendly-Code.md](../../Engineering/Performance/Cache-Friendly-Code.md)

## 참조 (References)

- [Engineering/Performance/Cache-Friendly-Code.md](../../Engineering/Performance/Cache-Friendly-Code.md)
- [Systems/Operating-Systems/Memory-Management.md](../Operating-Systems/Memory-Management.md)
- [Reference/Books.md](../../Reference/Books.md)
