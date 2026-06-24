# 그리디 알고리즘 (Greedy Algorithm)

- Level: Intermediate
- Prerequisites: [Algorithms/Complexity.md](Complexity.md), [Algorithms/Sorting.md](Sorting.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

그리디 알고리즘은 매 단계에서 **그 순간 가장 좋아 보이는 선택(지역 최적, local optimum)** 을 하고 절대 되돌리지 않는 방식으로 답을 만든다. 이 지역 최적의 연속이 **전체 최적(global optimum)** 과 일치한다는 것이 증명될 때만 올바르게 동작한다.

## 직관 (Intuition)

거스름돈을 줄 때 큰 동전부터 최대한 많이 내미는 것이 그리디다. 사람은 자연스럽게 "지금 가장 큰 걸 집자"라고 생각하는데, 그리디는 이 직관을 알고리즘으로 옮긴 것이다. 다만 이 직관이 **항상 맞지는 않는다**는 점이 그리디의 핵심 함정이다.

## 이론 (Theory)

그리디가 정당하려면 두 성질이 필요하다.

| 성질 | 의미 |
|---|---|
| 탐욕적 선택 속성 (greedy choice property) | 지역 최적 선택이 전체 최적해의 일부가 됨 |
| 최적 부분 구조 (optimal substructure) | 부분 문제의 최적해가 전체 최적해를 구성함 |

증명 기법으로는 **교환 논법(exchange argument)** 이 자주 쓰인다. "어떤 최적해가 그리디 선택과 다르다면, 그 부분을 그리디 선택으로 바꿔도 답이 나빠지지 않는다"를 보여 그리디 해가 최적임을 논증한다.

예: 활동 선택 문제(activity selection)에서 "**끝나는 시각이 가장 빠른** 활동을 먼저 고르기"는 교환 논법으로 최적임이 증명된다. 반면 0/1 배낭 문제에서 "가치/무게 비율이 큰 것부터"는 최적이 아니다(쪼갤 수 없으므로).

## 구현 (Implementation)

끝나는 시각 기준 활동 선택 문제다.

```python
def select_activities(activities):
    # activities: (start, end) 목록
    activities.sort(key=lambda x: x[1])    # 끝나는 시각 오름차순
    chosen, last_end = [], float("-inf")
    for start, end in activities:
        if start >= last_end:              # 겹치지 않으면 선택
            chosen.append((start, end))
            last_end = end
    return chosen


acts = [(1, 4), (3, 5), (0, 6), (5, 7), (5, 9), (8, 9)]
print(select_activities(acts))   # [(1, 4), (5, 7), (8, 9)]
```

## 복잡도 (Complexity)

대개 정렬이 지배적이다.

| 단계 | 시간 |
|---|---|
| 기준에 따른 정렬 | `O(n log n)` |
| 한 번 순회하며 선택 | `O(n)` |
| 전체 | `O(n log n)` |

추가 공간은 보통 `O(1)`~`O(n)`이다. 그리디는 DP보다 빠르고 단순하지만, 정당성 증명이 더 까다롭다.

## 응용 (Applications)

- 활동 선택, 회의실 배정
- 허프만 코딩(빈도 낮은 것부터 합치기)
- 최소 신장 트리(크루스칼·프림)
- 다익스트라 최단 경로(가장 가까운 정점 확정)
- 거스름돈(동전 체계가 정준일 때)

## 흔한 오해 (Common Misunderstandings)

- 그리디가 항상 최적은 아니다. 거스름돈도 동전 체계가 `[1, 3, 4]`라면 6원에 그리디(`4+1+1`)는 3개지만 최적(`3+3`)은 2개다.
- "직관적으로 좋아 보이는 기준"과 "증명된 올바른 기준"은 다르다. 활동 선택에서 시작 시각이나 소요 시간 기준은 틀리고, 끝나는 시각 기준만 맞다.
- 그리디와 DP를 혼동하기 쉽다. 그리디는 한 번 고르면 되돌리지 않고, DP는 모든 경우를 표로 따진다.
- 반례 하나면 그리디 전략은 무너진다. 증명 없이 그리디를 제출하면 틀리기 쉽다.

## TMI

- 매트로이드(matroid) 이론은 "어떤 문제에서 그리디가 항상 최적인가"를 대수적으로 규정한다. 그리디가 통하는 구조의 일반화다.
- 다익스트라와 프림은 사실상 같은 그리디 골격(우선순위 큐로 다음 최적을 확정)을 공유한다.
- 경쟁 프로그래밍에서 "그리디 같은데 증명이 안 되면 DP를 의심하라"는 격언이 흔하다. 반대로 DP가 너무 느리면 그리디 성질을 찾는다.

## 연습 / 확인 문제 (Exercises)

- 동전 `[1, 5, 10, 50]`에서 그리디가 최적인 이유를 설명하고, 최적이 깨지는 동전 집합을 하나 만들어라.
- 회의 `(시작, 끝)` 목록에서 최대 개수의 회의를 잡는 코드를 작성하라.
- 분할 가능한(fractional) 배낭 문제를 그리디로 풀고, 0/1 배낭에서는 왜 안 되는지 반례로 보여라.

## 이어서 읽기 (Reading Path)

- 이전: [정렬](Sorting.md)
- 다음: [최소 신장 트리](MST.md), [다익스트라](Dijkstra.md)
- 관련: [DP 기초](DP-Basics.md) (그리디가 안 될 때의 대안)

## 참조 (References)

- [Algorithms/Complexity.md](Complexity.md)
- [Algorithms/Sorting.md](Sorting.md)
- [Reference/Books.md](../Reference/Books.md)
- [Reference/Courses.md](../Reference/Courses.md)
