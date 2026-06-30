# 근사 알고리즘 (Approximation Algorithms)

- Level: Advanced
- Prerequisites: [Algorithms/Greedy.md](Greedy.md), [CS-Theory/Computation-Theory/NP-Completeness.md](../CS-Theory/Computation-Theory/NP-Completeness.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

근사 알고리즘은 NP-난해 최적화 문제에 **다항 시간으로 "최적에 가까운" 해를 보장과 함께** 낸다. 품질은 **근사 비율(approximation ratio)** 로 정량화한다 — 휴리스틱과 달리 그 품질을 *증명*한다.

## 직관 (Intuition)

외판원·정점 덮개 같은 중요한 문제는 정확한 최적해를 다항 시간에 못 구한다고 여겨진다([NP-완전성](../CS-Theory/Computation-Theory/NP-Completeness.md)). 포기 대신 "최적의 2배 이내"처럼 **보장된 품질**의 해를 빠르게 얻는다.

## 이론 (Theory)

### 1. 근사 비율과 등급

최소화 문제에서 비율 $\rho$: 알고리즘 해 $\le\rho\cdot\text{OPT}$.

- **상수 근사**: 정점 덮개 2-근사, 메트릭 TSP 2-근사(MST)·1.5-근사(Christofides).
- **PTAS**: 임의 $\varepsilon$ 에 $(1+\varepsilon)$ 근사를 다항 시간에(배낭). **FPTAS**는 비용이 $1/\varepsilon$ 의 다항식.
- **로그 근사**: 집합 덮개 그리디 $\ln n$-근사 — $P\ne NP$ 면 이보다 못 줄인다(하한).

### 2. 정점 덮개 2-근사 증명

알고리즘이 "양 끝을 모두 넣은" 간선들은 서로 끝점을 공유 안 함 → **매칭** $M$. OPT는 $M$ 의 각 간선을 끝점 하나 이상으로 덮어야 하므로 $\text{OPT}\ge|M|$. 우리 덮개 $=2|M|\le2\,\text{OPT}$. ∎

### 3. 근사 하한 (PCP)

일부 문제는 $P\ne NP$ 가정에서 **일정 비율 이하 근사조차 불가능**함이 증명된다(PCP 정리). 일반 TSP는 상수 근사 불가, 집합 덮개는 $(1-o(1))\ln n$ 이 하한.

## 구현 (Implementation)

```python
def vertex_cover_2approx(edges):
    cover = set()
    for u, v in edges:
        if u not in cover and v not in cover:    # 아직 안 덮인 간선
            cover.add(u); cover.add(v)           # 양 끝을 모두 추가(매칭)
    return cover                                  # |cover| <= 2 * OPT

def metric_tsp_2approx(mst_preorder):
    # MST를 DFS preorder로 순회 → 메트릭(삼각 부등식)이면 <= 2*OPT
    return mst_preorder + [mst_preorder[0]]
```

## 복잡도 (Complexity)

| 기법 | 비율 | 비용 |
|---|---|---|
| 정점 덮개 2-근사 | 2 | $O(E)$ |
| 메트릭 TSP (MST) | 2 | $O(E\log V)$ |
| Christofides | 1.5 | $O(V^3)$ (매칭) |
| 집합 덮개 그리디 | $\ln n$ | 다항 |
| FPTAS(배낭) | $1+\varepsilon$ | $O(n^3/\varepsilon)$ |

근사 비율은 **보장**이지 평균이 아니다 — 실측은 보통 더 좋다.

## 응용 (Applications)

- 시설 배치·네트워크 설계, 스케줄링·부하 분산.
- 클러스터링(k-center 2-근사, k-means++), 라우팅·배낭형 자원 배분.

## 흔한 오해 (Common Misunderstandings)

- **근사 비율은 최악 보장**이지 평균 성능이 아니다.
- **휴리스틱(보장 없음) ≠ 근사 알고리즘(증명된 보장)**.
- **모든 NP-난해가 좋은 근사를 갖지 않는다** — 일반 TSP는 상수 근사 불가.
- **메트릭(삼각 부등식) 가정 유무가 근사 가능성을 크게 바꾼다**.

## TMI

- Christofides(1976)의 1.5-근사는 40여 년 메트릭 TSP 최고 기록이었다가 2020년에야 미세하게 깨졌다($1.5-\epsilon$).
- PCP 정리(1990년대)는 "근사조차 어렵다"를 증명하는 도구로 근사 하한의 토대다.
- k-means++의 영리한 초기화는 기대 $O(\log k)$ 근사를 보장하는 실용 사례다.

## 연습 / 확인 문제 (Exercises)

- 정점 덮개 2-근사가 최적의 2배 이내임을 매칭 논증으로 증명하라.
- MST 기반 메트릭 TSP 2-근사의 아이디어(MST 비용 ≤ OPT, 순회 ≤ 2 MST)를 설명하라.
- 집합 덮개 그리디가 $\ln n$-근사임을 직관적으로 논하라.
- 배낭 FPTAS가 값을 어떻게 반올림해 $(1+\varepsilon)$ 를 얻는지 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [분할 상환 분석](Amortized-Analysis.md)
- 다음: [랜덤 알고리즘](Randomized-Algorithms.md)
- 관련: [그리디](Greedy.md), [NP-완전성](../CS-Theory/Computation-Theory/NP-Completeness.md)

## 참조 (References)

- [CS-Theory/Computation-Theory/NP-Completeness.md](../CS-Theory/Computation-Theory/NP-Completeness.md)
- [Algorithms/Greedy.md](Greedy.md)
- [Reference/Books.md](../Reference/Books.md)
