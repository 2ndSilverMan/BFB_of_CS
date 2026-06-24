# Python 컬렉션 (Collections)

- Level: Beginner
- Prerequisites: [Python 실행 환경과 기본 문법](Python-Setup-and-Syntax.md), [Programming/Arrays-and-Strings.md](../../Arrays-and-Strings.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

Python의 대표 컬렉션은 `list`, `tuple`, `dict`, `set`이다. 여러 값을 묶고 순회하고 검색하는 기본 도구이며, 알고리즘과 데이터 처리의 출발점이다.

## 직관 (Intuition)

`list`는 순서 있는 가변 목록, `tuple`은 고정된 묶음, `dict`는 이름표가 붙은 사전, `set`은 중복 없는 집합으로 보면 된다.

## 이론 (Theory)

Python 컬렉션은 동적 객체 reference를 담는 고수준 자료구조다. `list`는 동적 배열, `dict`와 `set`은 hash table에 가깝고, mutation과 aliasing이 동작 이해의 핵심이다.

## 구현 (Implementation)

구현할 때는 access pattern에 맞춰 기본 컬렉션을 고른다. 순서와 중복이 중요하면 `list`, key lookup이 중요하면 `dict`, membership과 중복 제거가 중요하면 `set`을 먼저 고려한다.

## 핵심 문법 (Core Syntax)

```python
numbers = [3, 1, 4]
point = (10, 20)
user = {"name": "Ada", "age": 20}
tags = {"python", "cs", "python"}

numbers.append(2)
print(user["name"])
print("cs" in tags)

for n in numbers:
    print(n)
```

List comprehension은 짧은 변환에 유용하다.

```python
squares = [x * x for x in range(5)]
```

## 복잡도 (Complexity)

`list` 끝 삽입은 평균 O(1), 중간 삽입은 O(n)이다. `dict`와 `set`의 lookup은 평균 O(1)이지만 해시 가능한 값만 key로 쓸 수 있다.

## 응용 (Applications)

- 데이터 목록 처리
- 빈도수 세기와 그룹화
- 중복 제거
- JSON 같은 중첩 데이터 표현

## 흔한 오해 (Common Misunderstandings)

- `list`를 복사하지 않고 대입하면 같은 객체를 가리킨다.
- `dict` key에는 보통 mutable 객체를 쓸 수 없다.
- `set`은 순서에 의존하는 자료구조가 아니다.
- 중첩 리스트를 만들 때 `[[0] * 3] * 3`은 같은 내부 리스트를 공유한다.

## TMI

- Python 3.7 이후 일반 `dict`도 삽입 순서를 보존하는 언어 보장이 있다.
- `collections.Counter`, `defaultdict`, `deque`는 자주 쓰는 확장 컬렉션이다.
- Slicing은 새 리스트를 만들 수 있어 큰 데이터에서는 비용을 의식해야 한다.

## 연습 / 확인 문제 (Exercises)

- 문자열 목록에서 각 단어의 등장 횟수를 `dict`로 세어라.
- 리스트에서 중복을 제거하되 원래 순서를 유지해 보라.
- `list`, `tuple`, `set`을 어떤 상황에 쓸지 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [Python 기본 문법](Python-Setup-and-Syntax.md)
- 다음: [Python 함수와 모듈](Python-Functions-and-Modules.md)

## 참조 (References)

- [Programming/Arrays-and-Strings.md](../../Arrays-and-Strings.md)
- [Data-Structures/Hash-Table.md](../../../Data-Structures/Hash-Table.md)
