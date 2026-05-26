# 정렬 (Sorting)

- Level: Beginner
- Prerequisites: [Programming/Arrays-and-Strings.md](../Programming/Arrays-and-Strings.md), [Algorithms/Complexity.md](Complexity.md)
- Status: Draft

---

## 개념 (Concept)

정렬은 원소들을 정해진 기준에 따라 순서대로 배치하는 작업이다. 숫자는 오름차순/내림차순으로, 문자열은 사전순으로, 객체는 특정 필드 기준으로 정렬할 수 있다.

## 직관 (Intuition)

정렬된 데이터는 다루기 쉽다. 사전이 정렬되어 있어 단어를 빨리 찾을 수 있고, 정렬된 숫자 배열에서는 이진 탐색을 사용할 수 있다. 많은 알고리즘은 정렬을 먼저 해 두면 문제가 단순해진다.

## 이론 (Theory)

정렬 알고리즘을 비교할 때는 다음 기준을 본다.

| 기준 | 의미 |
|---|---|
| 시간 복잡도 | 입력 크기에 따른 비교/이동 비용 |
| 공간 복잡도 | 추가 메모리 사용량 |
| 안정성 | 같은 키의 원소 순서가 유지되는지 |
| 제자리 정렬 | 입력 배열 내부에서 대부분 처리하는지 |

대표 알고리즘:

| 알고리즘 | 평균 시간 | 최악 시간 | 특징 |
|---|---|---|---|
| 버블 정렬 | O(n^2) | O(n^2) | 단순하지만 느림 |
| 선택 정렬 | O(n^2) | O(n^2) | 교환 횟수가 적음 |
| 삽입 정렬 | O(n^2) | O(n^2) | 거의 정렬된 데이터에 강함 |
| 병합 정렬 | O(n log n) | O(n log n) | 안정적, 추가 공간 필요 |
| 퀵 정렬 | O(n log n) | O(n^2) | 실전에서 빠른 편, 피벗 선택 중요 |

## 구현 (Implementation)

삽입 정렬:

```python
def insertion_sort(values):
    result = values[:]

    for i in range(1, len(result)):
        key = result[i]
        j = i - 1

        while j >= 0 and result[j] > key:
            result[j + 1] = result[j]
            j -= 1

        result[j + 1] = key

    return result
```

Python 내장 정렬:

```python
numbers = [5, 1, 4, 2, 3]
print(sorted(numbers))

people = [
    {"name": "Ada", "age": 36},
    {"name": "Grace", "age": 30},
]
print(sorted(people, key=lambda person: person["age"]))
```

## 복잡도 (Complexity)

| 알고리즘 | 시간 | 공간 |
|---|---|---|
| 삽입 정렬 | 평균/최악 O(n^2), 최선 O(n) | O(n) 또는 O(1) |
| 병합 정렬 | O(n log n) | O(n) |
| 퀵 정렬 | 평균 O(n log n), 최악 O(n^2) | O(log n) 평균 |
| Python `sorted` | O(n log n) | O(n) |

위 삽입 정렬 구현은 입력을 복사하므로 O(n) 공간을 쓴다. 제자리 구현이면 보조 공간은 O(1)이다.

## 응용 (Applications)

- 이진 탐색 전처리
- 중복 제거와 그룹화
- 순위 계산
- 스케줄링
- 탐욕 알고리즘의 전처리

## 흔한 오해 (Common Misunderstandings)

- 모든 정렬이 O(n log n)은 아니다. 단순 정렬은 보통 O(n^2)이다.
- 퀵 정렬은 평균적으로 빠르지만 최악의 경우 O(n^2)가 될 수 있다.
- 안정 정렬 여부는 객체를 여러 기준으로 정렬할 때 중요하다.
- 실무에서는 직접 정렬 알고리즘을 구현하기보다 언어의 표준 정렬을 쓰는 경우가 많다.

## 연습 / 확인 문제 (Exercises)

- 삽입 정렬이 거의 정렬된 배열에서 빠른 이유를 설명하라.
- 학생 목록을 점수 기준 내림차순으로 정렬하라.
- 정렬된 배열에서 중복 값을 제거하는 함수를 작성하라.

## 이어서 읽기 (Reading Path)

- 이전: [복잡도 분석](Complexity.md)
- 다음: [이진 탐색](Binary-Search.md)

## 참조 (References)

- [Algorithms/Complexity.md](Complexity.md)
- [Algorithms/Binary-Search.md](Binary-Search.md)
