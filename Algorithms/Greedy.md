# 그리디 알고리즘 (Greedy Algorithm)

- Level: Intermediate
- Prerequisites: [Algorithms/Complexity.md](Complexity.md), [Algorithms/Sorting.md](Sorting.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

그리디는 매 단계 **그 순간 최선(지역 최적)** 을 고르고 되돌리지 않는다. 이 지역 선택의 연속이 **전체 최적**과 일치함이 *증명될 때만* 옳다 — 그래서 그리디의 본질은 코드가 아니라 **정당성 증명**이다.

## 직관 (Intuition)

거스름돈을 큰 동전부터 내미는 게 그리디다. 사람의 "지금 가장 큰 걸 집자" 직관을 옮긴 것. 핵심 함정은 이 직관이 **항상 맞지는 않는다**는 것 — 반례 하나면 전략이 무너진다.

## 이론 (Theory)

### 1. 두 필요 성질

| 성질 | 의미 |
|---|---|
| 탐욕적 선택 속성 | 지역 최적 선택이 어떤 전체 최적해에 포함됨 |
| 최적 부분 구조 | 부분 문제의 최적해가 전체 최적해를 구성 |

### 2. 증명 도구 둘

- **교환 논법(exchange argument)**: 임의 최적해 $O$ 가 그리디 선택과 다르면, $O$ 의 한 요소를 그리디 선택으로 **바꿔도 더 나빠지지 않음**을 보여 그리디 해가 최적임을 논증.
- **greedy-stays-ahead**: 매 단계 그리디의 부분 해가 어떤 최적해보다 "뒤지지 않음"을 귀납으로.

예: **활동 선택**에서 "끝나는 시각이 가장 빠른 활동 먼저"는 교환 논법으로 최적 — 가장 빨리 끝나는 활동을 고르면 남은 시간이 최대가 된다. 반면 0/1 배낭의 "가치/무게 비율 큰 것부터"는 **쪼갤 수 없어** 최적이 아니다(분할 가능 배낭은 최적).

### 3. 그리디가 *항상* 통하는 구조: 매트로이드

**매트로이드(matroid)** 이론은 "어떤 독립 집합 구조에서 그리디가 항상 최적해를 주는가"를 정확히 규정한다(가중 매트로이드 → 그리디 최적). 크루스칼 MST가 그래픽 매트로이드의 그리디다.

## 구현 (Implementation)

```python
def select_activities(activities):           # (start, end) 목록
    activities.sort(key=lambda x: x[1])      # 끝나는 시각 오름차순이 핵심
    chosen, last_end = [], float("-inf")
    for s, e in activities:
        if s >= last_end:                    # 직전과 안 겹치면 선택
            chosen.append((s, e)); last_end = e
    return chosen

print(select_activities([(1,4),(3,5),(0,6),(5,7),(5,9),(8,9)]))
# [(1, 4), (5, 7), (8, 9)]
```

## 복잡도 (Complexity)

| 단계 | 시간 |
|---|---|
| 기준 정렬 | $O(n\log n)$ |
| 한 번 순회 선택 | $O(n)$ |
| 전체 | $O(n\log n)$ |

보조 공간 $O(1)$~$O(n)$. 그리디는 [DP](DP-Basics.md)보다 빠르고 단순하지만 정당성 증명이 까다롭다. **워크드 예제(활동 선택).** 정렬 후 끝시각 `4,5,6,7,9,9`. `(1,4)` 선택(last=4) → `(3,5)` `(0,6)` 겹침 스킵 → `(5,7)` 선택(last=7) → `(5,9)` 겹침 → `(8,9)` 선택. 답 3개, 최적.

## 응용 (Applications)

- 활동/회의실 배정, 작업 스케줄링(마감/지연 최소화).
- 허프만 코딩(최소 빈도 둘을 반복 병합).
- [MST](MST.md)(크루스칼·프림, cut property), [다익스트라](Dijkstra.md)(가장 가까운 정점 확정).
- 거스름돈(동전 체계가 canonical일 때).

## 흔한 오해 (Common Misunderstandings)

- **그리디가 항상 최적은 아니다** — 동전 `[1,3,4]` 로 6원: 그리디 `4+1+1`(3개) vs 최적 `3+3`(2개).
- **"좋아 보이는 기준" ≠ "증명된 기준"** — 활동 선택에서 시작 시각·소요 시간 기준은 틀리고 *끝 시각*만 옳다.
- **그리디 ≠ DP** — 그리디는 한 번 고르면 불변, DP는 모든 경우를 표로.
- **증명 없는 그리디는 위험** — 반례 하나로 무너진다.

## TMI

- "그리디 같은데 증명이 안 되면 DP를 의심하라, DP가 너무 느리면 그리디 성질을 찾아라"는 경쟁 프로그래밍 격언.
- 다익스트라와 프림은 사실상 같은 그리디 골격(우선순위 큐로 다음 최적 확정)을 공유한다.
- 허프만 코딩의 최적성은 교환 논법의 교과서적 사례다(가장 드문 두 심볼이 최하단 형제가 됨).

## 연습 / 확인 문제 (Exercises)

- 동전 `[1,5,10,50]` 에서 그리디가 최적인 이유를 설명하고, 최적이 깨지는 동전 집합을 만들어라.
- 회의 `(시작,끝)` 에서 최대 개수를 잡는 코드를 작성하고 끝시각 기준의 최적성을 교환 논법으로 논증하라.
- 분할 가능 배낭을 그리디로 풀고, 0/1 배낭에서 왜 깨지는지 반례를 들어라.
- 허프만 코딩을 구현하고 평균 부호 길이가 최소임을 작은 예로 확인하라.

## 이어서 읽기 (Reading Path)

- 이전: [정렬](Sorting.md)
- 다음: [최소 신장 트리](MST.md)
- 관련: [다익스트라](Dijkstra.md), [DP 기초](DP-Basics.md)

## 참조 (References)

- [Algorithms/Complexity.md](Complexity.md)
- [Algorithms/Sorting.md](Sorting.md)
- [Algorithms/MST.md](MST.md)
- [Reference/Books.md](../Reference/Books.md)
- [Reference/Courses.md](../Reference/Courses.md)
