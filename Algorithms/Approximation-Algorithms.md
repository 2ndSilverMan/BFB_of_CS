# 근사 알고리즘 (Approximation Algorithms)

- Level: Advanced
- Prerequisites: [Algorithms/Greedy.md](Greedy.md), [CS-Theory/Computation-Theory/NP-Completeness.md](../CS-Theory/Computation-Theory/NP-Completeness.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

근사 알고리즘은 NP-난해 최적화 문제에 대해 다항 시간에 "최적에 가까운" 해를 보장과 함께 내는 알고리즘이다. 근사 비율(approximation ratio)로 품질을 정량화한다.

## 직관 (Intuition)

많은 중요한 문제(외판원, 정점 덮개)는 정확한 최적해를 다항 시간에 구할 수 없다고 여겨진다. 그렇다고 포기하는 대신, "최적의 2배 이내"처럼 보장된 품질의 해를 빠르게 얻는다. 휴리스틱과 달리 근사 알고리즘은 그 품질을 수학적으로 증명한다.

## 이론 (Theory)

근사 비율 $\rho$: 최소화 문제에서 알고리즘 해 $\le \rho\cdot \text{OPT}$. 등급:

- **상수 근사**: 정점 덮개 2-근사(간선을 골라 양 끝 포함), 메트릭 TSP 2-근사(MST 기반)·1.5-근사(Christofides).
- **PTAS**: 임의의 $\epsilon$에 대해 $(1+\epsilon)$ 근사를 다항 시간에(예: 배낭).
- **로그 근사**: 집합 덮개의 그리디 $\ln n$-근사 — 이보다 좋은 근사는 불가능(하한 존재).

일부 문제는 $P\ne NP$ 가정에서 일정 비율 이하 근사가 불가능함이 증명된다(근사 하한, PCP 정리).

## 구현 (Implementation)

```python
def vertex_cover_2approx(edges):
    cover = set()
    used = set()
    for u, v in edges:
        if u in used or v in used:        # 이미 덮인 간선은 건너뜀
            if u in cover or v in cover: continue
        if u not in cover and v not in cover:
            cover.add(u); cover.add(v)    # 간선의 양 끝을 모두 추가
            used.add(u); used.add(v)
    return cover                          # |cover| <= 2 * OPT
```

## 복잡도 (Complexity)

근사 알고리즘은 다항 시간이 핵심 제약이다. 정점 덮개 2-근사·메트릭 TSP MST 근사는 간선 수에 거의 선형이다. PTAS는 $\epsilon$이 작아질수록 비용이 커지며, FPTAS는 $1/\epsilon$의 다항식으로 제한된다.

## 응용 (Applications)

- 시설 배치·네트워크 설계
- 스케줄링·부하 분산
- 클러스터링(k-center, k-means++)
- 라우팅·배낭형 자원 배분

## 흔한 오해 (Common Misunderstandings)

- 근사 비율은 보장이지 평균 성능이 아니다 — 실제로는 더 좋을 때가 많다.
- 휴리스틱(보장 없음)과 근사 알고리즘(증명된 보장)은 다르다.
- 모든 NP-난해 문제가 좋은 근사를 갖지 않는다(일반 TSP는 상수 근사 불가).
- 메트릭(삼각 부등식) 가정 유무가 근사 가능성을 크게 바꾼다.

## TMI

- Christofides 알고리즘(1976)의 1.5-근사는 40여 년간 메트릭 TSP 최고 기록이었다가 2020년에야 미세하게 개선됐다.
- PCP 정리는 "근사조차 어렵다"를 증명하는 강력한 도구로 근사 하한의 토대다.
- k-means++의 영리한 초기화는 기대 $O(\log k)$ 근사를 보장하는 실용적 사례다.

## 연습 / 확인 문제 (Exercises)

- 정점 덮개 2-근사가 왜 최적의 2배 이내인지 증명하라.
- MST 기반 메트릭 TSP 2-근사의 아이디어를 설명하라.
- 집합 덮개 그리디가 $\ln n$-근사임을 직관적으로 논하라.

## 이어서 읽기 (Reading Path)

- 이전: [분할 상환 분석](Amortized-Analysis.md)
- 다음: [랜덤 알고리즘](Randomized-Algorithms.md)

## 참조 (References)

- [CS-Theory/Computation-Theory/NP-Completeness.md](../CS-Theory/Computation-Theory/NP-Completeness.md)
- [Algorithms/Greedy.md](Greedy.md)
- [Reference/Books.md](../Reference/Books.md)
