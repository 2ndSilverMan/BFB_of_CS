# 배열과 문자열 (Arrays and Strings)

- Level: Beginner
- Prerequisites: [Programming/Variables-and-Types.md](Variables-and-Types.md), [Programming/Control-Flow.md](Control-Flow.md)
- Status: Draft

---

## 개념 (Concept)

배열은 여러 값을 순서대로 담는 묶음이고, 문자열은 문자들이 순서대로 나열된 값이다. 둘 다 인덱스로 특정 위치에 접근하고, 반복문으로 처음부터 끝까지 순회할 수 있다.

## 직관 (Intuition)

배열과 문자열은 "순서가 있는 데이터"를 다루는 가장 기본적인 도구다. 점수 목록, 이름 목록, 입력 텍스트, 파일 경로, 명령어 인자처럼 실제 프로그램의 많은 데이터가 이 형태로 들어온다.

배열은 보통 원소를 바꿀 수 있지만, 문자열은 많은 언어에서 불변 값으로 다룬다. 그래서 문자열을 조금씩 이어 붙이는 코드는 예상보다 비쌀 수 있다.

## 이론 (Theory)

배열과 문자열에서 자주 쓰는 연산은 다음과 같다.

| 연산 | 의미 |
|---|---|
| 인덱싱 | 특정 위치의 원소 읽기 |
| 슬라이싱 | 연속된 구간 잘라내기 |
| 순회 | 모든 원소를 차례로 방문 |
| 검색 | 조건을 만족하는 원소 찾기 |
| 변환 | 각 원소를 다른 값으로 바꾸기 |

0-based 인덱스 언어에서는 첫 위치가 `0`이다. 길이가 `n`인 배열의 마지막 인덱스는 `n - 1`이다.

문자열은 문자 배열처럼 순회할 수 있지만, 문자 인코딩 때문에 "보이는 글자 수"와 내부 코드 포인트 수가 다를 수 있다. 입문 단계에서는 ASCII나 단순한 한글 문자열을 기준으로 시작하고, 나중에 Unicode를 따로 다룬다.

## 구현 (Implementation)

배열 순회:

```python
scores = [90, 85, 100]

for score in scores:
    print(score)
```

인덱스가 필요할 때:

```python
names = ["Ada", "Grace", "Linus"]

for index in range(len(names)):
    print(index, names[index])
```

문자열 순회와 카운트:

```python
def count_char(text, target):
    count = 0
    for char in text:
        if char == target:
            count += 1
    return count
```

새 배열 만들기:

```python
def square_all(values):
    result = []
    for value in values:
        result.append(value * value)
    return result
```

## 복잡도 (Complexity)

| 연산 | 시간 | 공간 |
|---|---|---|
| 인덱스 접근 | O(1) | O(1) |
| 전체 순회 | O(n) | O(1) |
| 값 검색 | O(n) | O(1) |
| 길이 n 배열 복사 | O(n) | O(n) |
| 길이 n 문자열 생성 | O(n) | O(n) |

슬라이싱은 언어에 따라 새 배열/문자열을 만들 수 있다. 새 값을 만들면 보통 잘라낸 길이만큼 시간과 공간이 든다.

## 응용 (Applications)

- 입력 목록 처리
- 문자열 검색과 전처리
- 정렬, 이진 탐색, 투 포인터 알고리즘의 기반
- 스택, 큐, 힙 같은 자료구조의 내부 저장소
- 텍스트 처리와 파싱

## 흔한 오해 (Common Misunderstandings)

- 인덱스 접근이 O(1)이어도 원하는 값을 찾는 검색은 O(n)이다.
- 문자열은 배열과 비슷해 보여도 수정 가능성이 다를 수 있다.
- `len(values)`가 항상 비싼 것은 아니다. 많은 언어에서 길이는 별도로 저장되어 O(1)이다.
- 빈 배열과 `None`은 다르다. 빈 배열은 원소가 0개인 정상 값이다.

## 연습 / 확인 문제 (Exercises)

- 숫자 배열에서 짝수만 골라 새 배열로 반환하라.
- 문자열에서 모음 개수를 세는 함수를 작성하라.
- 배열이 오름차순으로 정렬되어 있는지 검사하라.

## 이어서 읽기 (Reading Path)

- 이전: [함수와 재귀](Functions-and-Recursion.md)
- 다음: [명제 논리와 술어 논리](../Math/Discrete/Logic.md)

## 참조 (References)

- [Programming/Variables-and-Types.md](Variables-and-Types.md)
- [Programming/Control-Flow.md](Control-Flow.md)
- [Data-Structures/Array.md](../Data-Structures/Array.md)
