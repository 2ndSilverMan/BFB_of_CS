# 이진 탐색 (Binary Search)

- Level: Beginner
- Prerequisites: [Programming/Arrays-and-Strings.md](../Programming/Arrays-and-Strings.md), [Algorithms/Complexity.md](Complexity.md), [Algorithms/Sorting.md](Sorting.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

이진 탐색은 정렬된 배열에서 탐색 범위를 절반씩 줄이며 원하는 값을 찾는 알고리즘이다. 매 단계마다 가운데 값을 보고 왼쪽 절반 또는 오른쪽 절반을 버린다.

## 직관 (Intuition)

사전에서 단어를 찾을 때 처음부터 한 장씩 넘기지 않는다. 중간쯤을 펴 보고 찾는 단어가 앞쪽인지 뒤쪽인지 판단한 뒤 절반을 버린다. 이진 탐색도 같은 방식이다.

핵심 조건은 데이터가 정렬되어 있어야 한다는 점이다.

## 이론 (Theory)

이진 탐색은 항상 다음 불변식을 유지한다.

```text
target이 있다면 left와 right 사이에 있다.
```

중간 인덱스 `mid`를 확인한 뒤 다음 중 하나를 수행한다.

| 비교 | 행동 |
|---|---|
| `values[mid] == target` | 찾음 |
| `values[mid] < target` | 왼쪽 절반을 버림 |
| `values[mid] > target` | 오른쪽 절반을 버림 |

탐색 범위가 매번 절반으로 줄기 때문에 시간 복잡도는 O(log n)이다.

## 구현 (Implementation)

반복문 버전:

```python
def binary_search(values, target):
    left = 0
    right = len(values) - 1

    while left <= right:
        mid = (left + right) // 2

        if values[mid] == target:
            return mid
        if values[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
```

삽입 위치 찾기:

```python
def lower_bound(values, target):
    left = 0
    right = len(values)

    while left < right:
        mid = (left + right) // 2
        if values[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left
```

`lower_bound`는 `target` 이상인 첫 위치를 반환한다. 같은 값이 여러 개 있을 때 첫 위치를 찾는 데 유용하다.

## 복잡도 (Complexity)

| 연산 | 시간 | 공간 |
|---|---|---|
| 반복문 이진 탐색 | O(log n) | O(1) |
| 재귀 이진 탐색 | O(log n) | O(log n) |
| 정렬 후 한 번 탐색 | O(n log n) | 정렬 구현에 따름 |

데이터가 이미 정렬되어 있지 않다면 정렬 비용도 함께 고려해야 한다.

## 응용 (Applications)

- 정렬된 배열에서 값 찾기
- 첫 위치/마지막 위치 찾기
- 조건을 만족하는 최소/최대 값 찾기
- 답을 정해 놓고 가능 여부를 검사하는 파라메트릭 서치

## 흔한 오해 (Common Misunderstandings)

- 정렬되지 않은 배열에는 이진 탐색을 사용할 수 없다.
- `left <= right`와 `left < right`는 서로 다른 형태다. 불변식에 맞춰 경계를 정해야 한다.
- 중복 값이 있을 때 일반 이진 탐색은 아무 위치나 반환할 수 있다.
- 정렬 비용이 탐색 비용보다 클 수 있다. 한 번만 찾을 거면 선형 탐색이 더 나을 수도 있다.

## TMI

- 이진 탐색은 아이디어는 단순하지만 경계 조건 버그가 자주 나는 알고리즘으로 유명하다. `left`, `right`, `mid`의 의미를 먼저 정해야 구현이 흔들리지 않는다.
- 예전에는 `mid = (left + right) // 2`가 매우 큰 정수에서 오버플로를 일으킬 수 있었다. 그래서 `left + (right - left) // 2` 형태를 권장하는 언어도 많다.
- Python의 `bisect` 모듈은 값을 찾았는지 직접 알려 주기보다 "어디에 끼워 넣으면 정렬이 유지되는지"를 알려 준다.
- Java의 `Arrays.binarySearch`는 값을 못 찾으면 음수를 반환하는데, 그 값은 삽입 위치를 인코딩한 것이다. 처음 보면 에러 코드처럼 보인다.

## 연습 / 확인 문제 (Exercises)

- 정렬된 배열에서 특정 값의 인덱스를 반환하라. 없으면 `-1`을 반환하라.
- 정렬된 배열에서 target 이상인 첫 위치를 구하라.
- 정렬된 배열에서 특정 값이 몇 번 등장하는지 이진 탐색으로 구하라.

## 이어서 읽기 (Reading Path)

- 이전: [정렬](Sorting.md)
- 다음: [BFS / DFS](BFS-DFS.md)

## 참조 (References)

- [Algorithms/Sorting.md](Sorting.md)
- [Algorithms/Complexity.md](Complexity.md)
- [Reference/Books.md](../Reference/Books.md)
- [Reference/Courses.md](../Reference/Courses.md)
