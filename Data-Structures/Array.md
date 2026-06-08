# 배열 (Array)

- Level: Beginner
- Prerequisites: [Programming/Variables-and-Types.md](../Programming/Variables-and-Types.md), [Programming/Control-Flow.md](../Programming/Control-Flow.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

배열은 같은 종류의 값을 연속된 위치에 저장하고, 인덱스로 접근하는 선형 자료구조다. 많은 언어에서 배열 또는 리스트는 가장 기본적인 데이터 묶음으로 쓰인다.

## 직관 (Intuition)

배열은 번호가 붙은 칸들의 줄이다. `0`번 칸, `1`번 칸, `2`번 칸처럼 위치가 정해져 있으므로 특정 위치의 값을 빠르게 읽을 수 있다.

반대로 중간에 값을 끼워 넣거나 삭제하면 뒤의 원소들을 밀거나 당겨야 해서 비용이 든다.

## 이론 (Theory)

배열의 핵심은 인덱스 기반 접근이다.

| 연산 | 설명 |
|---|---|
| 접근 | `array[i]`로 i번째 원소 읽기 |
| 갱신 | `array[i] = value`로 i번째 원소 바꾸기 |
| 순회 | 처음부터 끝까지 차례로 방문 |
| 삽입 | 특정 위치에 새 원소 추가 |
| 삭제 | 특정 위치의 원소 제거 |

고정 크기 배열은 크기가 정해져 있고, 동적 배열은 내부 용량을 늘려 가며 원소를 추가한다. Python의 `list`, Java의 `ArrayList`, C++의 `vector`는 동적 배열에 가깝다.

## 구현 (Implementation)

```python
numbers = [10, 20, 30]

print(numbers[0])  # 10
numbers[1] = 25
numbers.append(40)

for number in numbers:
    print(number)
```

최댓값 찾기:

```python
def max_value(values):
    if len(values) == 0:
        return None

    best = values[0]
    for index in range(1, len(values)):
        if values[index] > best:
            best = values[index]
    return best
```

## 복잡도 (Complexity)

| 연산 | 시간 | 공간 |
|---|---|---|
| 인덱스 접근 | O(1) | O(1) |
| 인덱스 갱신 | O(1) | O(1) |
| 끝에 추가 | 평균 O(1), 최악 O(n) | O(1) 또는 O(n) |
| 중간 삽입 | O(n) | O(1) |
| 중간 삭제 | O(n) | O(1) |
| 전체 순회 | O(n) | O(1) |

동적 배열은 용량이 부족할 때 더 큰 공간을 새로 잡고 기존 원소를 복사한다. 그래서 끝에 추가는 최악 O(n)이지만 여러 번의 평균으로 보면 O(1)로 분석한다.

## 응용 (Applications)

- 순서가 중요한 데이터 저장
- 테이블, 벡터, 행렬의 기초 표현
- 정렬과 탐색 알고리즘의 입력
- 스택, 힙, 해시 테이블 같은 다른 자료구조의 내부 구현

## 흔한 오해 (Common Misunderstandings)

- 배열 접근이 O(1)이라는 말은 어떤 값이든 바로 "찾는다"는 뜻이 아니다. 위치를 알 때만 O(1)이다.
- 값으로 검색하는 것은 보통 O(n)이다.
- 동적 배열의 `append`는 항상 O(1)이 아니라 평균 O(1)이다.
- 배열과 연결 리스트는 둘 다 선형 구조지만 성능 특성이 크게 다르다.

## TMI

- 많은 언어가 0부터 인덱스를 세는 이유 중 하나는 배열의 시작 주소에서 얼마나 떨어져 있는지를 바로 오프셋으로 볼 수 있기 때문이다.
- Python의 `list`는 이름은 리스트지만 내부적으로는 연결 리스트가 아니라 동적 배열에 가깝다.
- 동적 배열은 보통 실제 길이보다 큰 용량을 미리 잡아 둔다. 그래서 원소를 하나 추가할 때마다 매번 새 배열을 만들지는 않는다.
- 배열은 단순해 보여도 CPU 캐시와 잘 맞아서 실제 성능이 좋을 때가 많다. 연결 리스트가 이론상 삽입/삭제에 유리해도 실전에서 배열이 이기는 이유 중 하나다.

## 연습 / 확인 문제 (Exercises)

- 숫자 배열에서 최솟값과 최댓값을 동시에 찾는 함수를 작성하라.
- 배열을 뒤집는 함수를 새 배열을 만드는 방식과 제자리 방식으로 각각 작성하라.
- 배열에서 특정 값이 처음 등장하는 인덱스를 반환하라. 없으면 `-1`을 반환하라.

## 이어서 읽기 (Reading Path)

- 이전: [명제 논리와 술어 논리](../Math/Discrete/Logic.md)
- 다음: [연결 리스트](Linked-List.md)

## 참조 (References)

- [Programming/Control-Flow.md](../Programming/Control-Flow.md)
- [Data-Structures/Linked-List.md](Linked-List.md)
- [Algorithms/Complexity.md](../Algorithms/Complexity.md)
- [Reference/Books.md](../Reference/Books.md)
- [Reference/Courses.md](../Reference/Courses.md)
