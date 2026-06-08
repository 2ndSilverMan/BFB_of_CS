# 함수와 재귀 (Functions and Recursion)

- Level: Beginner
- Prerequisites: [Programming/Variables-and-Types.md](Variables-and-Types.md), [Programming/Control-Flow.md](Control-Flow.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

함수는 입력을 받아 정해진 작업을 수행하고 결과를 반환하는 코드 묶음이다. 재귀는 함수가 자기 자신을 호출해서 문제를 더 작은 문제로 나누는 기법이다.

## 직관 (Intuition)

함수는 프로그램의 이름 붙은 부품이다. 같은 코드를 반복해서 쓰지 않고, 의미 있는 단위로 나누며, 테스트하기 쉬운 경계를 만든다.

재귀는 "큰 문제를 같은 형태의 작은 문제로 줄일 수 있을 때" 자연스럽다. 예를 들어 리스트의 합은 첫 원소와 나머지 리스트의 합으로 나눌 수 있다.

## 이론 (Theory)

좋은 함수는 보통 다음 성질을 가진다.

| 성질 | 의미 |
|---|---|
| 단일 책임 | 하나의 분명한 일을 한다 |
| 명확한 입력 | 필요한 값을 매개변수로 받는다 |
| 명확한 출력 | 결과를 반환하거나 부작용을 분명히 한다 |
| 작은 범위 | 읽고 테스트하기 쉬운 크기다 |

재귀 함수에는 두 부분이 필요하다.

- 기본 조건: 더 이상 자기 자신을 호출하지 않고 끝나는 경우
- 재귀 단계: 문제를 더 작은 같은 형태의 문제로 줄이는 경우

기본 조건이 없거나 문제 크기가 줄지 않으면 재귀는 끝나지 않는다.

## 구현 (Implementation)

함수 예시:

```python
def average(values):
    if len(values) == 0:
        return 0
    return sum(values) / len(values)

print(average([90, 85, 100]))
```

재귀 예시:

```python
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120
```

리스트 합도 재귀로 표현할 수 있다.

```python
def recursive_sum(values):
    if len(values) == 0:
        return 0
    return values[0] + recursive_sum(values[1:])
```

다만 위 구현은 슬라이싱 때문에 매 호출마다 새 리스트를 만들 수 있다. 실제 코드에서는 인덱스를 넘기거나 반복문을 쓰는 편이 더 효율적일 수 있다.

## 복잡도 (Complexity)

| 함수 | 시간 | 공간 |
|---|---|---|
| `average(values)` | O(n) | O(1) |
| `factorial(n)` | O(n) | O(n) |
| 슬라이싱을 쓰는 재귀 합 | O(n^2) | O(n^2) |

재귀의 공간 복잡도에는 호출 스택이 포함된다.

## 응용 (Applications)

- 중복 로직 제거
- 입력 검증과 계산 로직 분리
- 트리와 그래프 탐색
- 분할 정복 알고리즘
- 수학적 정의를 코드로 옮기기

## 흔한 오해 (Common Misunderstandings)

- 함수가 짧다고 항상 좋은 것은 아니다. 의미 있는 단위로 나뉘어야 한다.
- 재귀가 반복문보다 항상 우아하거나 빠른 것은 아니다.
- 반환값과 출력은 다르다. `print`는 화면에 보여 주는 부작용이고, `return`은 호출한 코드에 값을 돌려준다.
- 기본 조건이 있어도 재귀 단계에서 문제 크기가 줄지 않으면 종료되지 않는다.

## TMI

- 재귀 예제로 factorial과 Fibonacci가 자주 나오지만, 실무에서는 트리, 파일 시스템, 파서처럼 "안에 같은 구조가 다시 들어 있는" 문제에서 특히 자연스럽다.
- Python은 기본 재귀 깊이에 제한이 있다. 재귀가 너무 깊어질 수 있는 문제는 반복문이나 명시적 스택으로 바꾸는 편이 안전하다.
- Python의 기본 인자 값은 함수가 호출될 때마다 새로 만들어지는 것이 아니라 함수가 정의될 때 한 번 만들어진다. 그래서 `def f(x=[]): ...` 같은 코드는 의도치 않게 리스트를 공유할 수 있다.
- Java는 객체를 넘길 때도 "참조값을 값으로 복사"한다. 그래서 Java를 pass-by-reference라고 부르면 엄밀히는 틀린 설명이다.

## 연습 / 확인 문제 (Exercises)

- 숫자 목록을 받아 최댓값을 반환하는 함수를 작성하라.
- `factorial`을 반복문 버전과 재귀 버전으로 각각 작성하라.
- 문자열이 팰린드롬인지 검사하는 재귀 함수를 작성하라.

## 이어서 읽기 (Reading Path)

- 이전: [조건문과 반복문](Control-Flow.md)
- 다음: [배열과 문자열](Arrays-and-Strings.md)

## 참조 (References)

- [Programming/Control-Flow.md](Control-Flow.md)
- [Algorithms/](../Algorithms/)
- [Reference/Books.md](../Reference/Books.md)
- [Reference/Courses.md](../Reference/Courses.md)
