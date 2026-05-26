# 복잡도 분석 (Big-O)

- Level: Beginner
- Prerequisites: [Programming/Control-Flow.md](../Programming/Control-Flow.md), [Math/Discrete/Logic.md](../Math/Discrete/Logic.md)
- Status: Draft

---

## 개념 (Concept)

복잡도 분석은 입력 크기가 커질 때 알고리즘의 시간과 공간 사용량이 어떻게 증가하는지 설명하는 방법이다. Big-O 표기법은 증가율의 상한을 간단히 나타낸다.

## 직관 (Intuition)

작은 입력에서는 대부분의 코드가 충분히 빠르다. 문제는 입력이 커질 때다. 길이 100에서는 괜찮던 알고리즘이 길이 1,000,000에서는 끝나지 않을 수 있다.

복잡도는 특정 컴퓨터에서 몇 초가 걸리는지를 직접 말하지 않는다. 대신 입력 크기 `n`이 커질 때 작업량이 어떤 모양으로 늘어나는지 말한다.

## 이론 (Theory)

자주 보는 복잡도는 다음과 같다.

| 표기 | 이름 | 전형적인 예 |
|---|---|---|
| O(1) | 상수 | 배열 인덱스 접근 |
| O(log n) | 로그 | 이진 탐색 |
| O(n) | 선형 | 전체 순회 |
| O(n log n) | 선형 로그 | 효율적인 비교 정렬 |
| O(n^2) | 이차 | 모든 쌍 비교 |
| O(2^n) | 지수 | 모든 부분집합 탐색 |

Big-O는 낮은 차수 항과 상수 계수를 생략한다.

```text
3n^2 + 10n + 5 = O(n^2)
```

하지만 실제 성능에서는 상수와 메모리 접근 패턴도 중요하다. Big-O는 알고리즘 선택의 첫 기준이지 유일한 기준은 아니다.

## 구현 (Implementation)

O(n) 예시:

```python
def contains(values, target):
    for value in values:
        if value == target:
            return True
    return False
```

O(n^2) 예시:

```python
def has_duplicate(values):
    n = len(values)
    for i in range(n):
        for j in range(i + 1, n):
            if values[i] == values[j]:
                return True
    return False
```

해시 집합을 쓰면 중복 검사를 평균 O(n)으로 바꿀 수 있다.

```python
def has_duplicate_fast(values):
    seen = set()
    for value in values:
        if value in seen:
            return True
        seen.add(value)
    return False
```

## 복잡도 (Complexity)

| 알고리즘 | 시간 | 공간 |
|---|---|---|
| `contains` | O(n) | O(1) |
| `has_duplicate` | O(n^2) | O(1) |
| `has_duplicate_fast` | 평균 O(n) | O(n) |

시간을 줄이기 위해 추가 공간을 사용하는 경우가 많다. 이를 시간-공간 트레이드오프라고 한다.

## 응용 (Applications)

- 알고리즘 선택
- 자료구조 선택
- 병목 예측
- 입력 크기에 따른 한계 판단
- 코딩 테스트와 시스템 성능 분석

## 흔한 오해 (Common Misunderstandings)

- Big-O는 항상 최악의 경우만 뜻하지 않는다. 최악, 평균, 최선 중 무엇을 말하는지 명시해야 한다.
- O(n) 알고리즘이 모든 입력에서 O(1) 알고리즘보다 느리다는 뜻은 아니다.
- 중첩 반복문이 항상 O(n^2)은 아니다. 반복 범위가 입력과 어떻게 연결되는지 봐야 한다.
- 공간 복잡도에는 보조 자료구조뿐 아니라 재귀 호출 스택도 포함된다.

## 연습 / 확인 문제 (Exercises)

- 배열의 합을 구하는 함수의 시간/공간 복잡도를 분석하라.
- 이중 반복문이지만 전체 반복 횟수가 O(n)인 예시를 만들어 보라.
- 중복 검사에서 O(n^2) 풀이와 O(n) 풀이의 장단점을 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [그래프 표현](../Data-Structures/Graph-Representation.md)
- 다음: [정렬](Sorting.md)

## 참조 (References)

- [Data-Structures/Array.md](../Data-Structures/Array.md)
- [Programming/Control-Flow.md](../Programming/Control-Flow.md)
