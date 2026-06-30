# Python 컬렉션 (Collections)

- Level: Beginner
- Prerequisites: [Python 실행 환경과 기본 문법](Python-Setup-and-Syntax.md), [Programming/Arrays-and-Strings.md](../../Arrays-and-Strings.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

Python의 대표 컬렉션 `list`·`tuple`·`dict`·`set` 은 각각 **동적 배열·불변 배열·해시 테이블·해시 집합**이다. 겉보기 문법보다 **내부 표현과 aliasing(참조 공유)** 을 이해하는 것이 버그 없는 코드의 핵심이다.

## 직관 (Intuition)

`list`=순서 있는 가변 목록, `tuple`=고정 묶음, `dict`=이름표 붙은 사전, `set`=중복 없는 집합. 단, Python 컬렉션은 **값이 아니라 객체 참조**를 담는다 — 이 사실이 복사·변경·중첩의 모든 함정을 만든다.

## 핵심 문법 (Core Syntax)

```python
nums = [3, 1, 4]; nums.append(2)        # 동적 배열
point = (10, 20)                         # 불변
user = {"name": "Ada", "age": 20}        # 해시 테이블
tags = {"py", "cs", "py"}                # 중복 제거 → {"py","cs"}
squares = [x*x for x in range(5)]        # comprehension
```

## 이론 (Theory)

### 1. 내부 표현

- **`list`**: [동적 배열](../../../Data-Structures/Array.md) — 끝 추가는 over-allocation으로 amortized $O(1)$, 중간 삽입/삭제는 $O(n)$(밀기).
- **`dict`/`set`**: [open-addressing 해시 테이블](../../../Data-Structures/Hash-Table.md). 키는 **hashable**(불변 + `__hash__`)이어야. CPython 3.6+ 의 **compact dict**는 삽입 순서를 보존(언어 보장은 3.7+).
- **`tuple`**: 불변이라 hashable → dict 키·set 원소로 사용 가능.

### 2. aliasing과 mutation

대입은 **복사가 아니라 참조 공유**다. `b = a` 후 `a.append(x)` 면 `b` 도 바뀐다. 얕은 복사 `a[:]`/`list(a)` vs 깊은 복사 `copy.deepcopy` 의 차이가 중첩 구조에서 결정적이다.

## 구현 (Implementation)

```python
words = ["a", "b", "a", "c", "a", "b"]
freq = {}
for w in words:
    freq[w] = freq.get(w, 0) + 1          # dict 집계
unique_in_order = list(dict.fromkeys(words))   # 순서 보존 중복 제거
print(freq["a"], unique_in_order)          # 3 ['a','b','c']

from collections import Counter, defaultdict, deque
Counter(words)                             # {'a':3,'b':2,'c':1}
```

## 복잡도 (Complexity)

| 연산 | list | dict/set |
|---|---|---|
| 인덱스 접근 | $O(1)$ | — |
| 끝 추가 | amortized $O(1)$ | — |
| 중간 삽입/삭제 | $O(n)$ | — |
| 멤버십 `in` | $O(n)$ | 평균 $O(1)$ |
| 키 조회/삽입 | — | 평균 $O(1)$, 최악 $O(n)$ |

`x in list` 가 $O(n)$ 인데 `x in set` 이 $O(1)$ 임을 모르면 흔한 성능 버그가 난다.

**워크드 예제(aliasing 함정).** `grid = [[0]*3]*3` 은 **같은 내부 리스트 3개**를 참조 → `grid[0][0]=1` 이면 `grid[1][0]`, `grid[2][0]` 도 1이 된다. 올바른 방법: `[[0]*3 for _ in range(3)]`.

## 응용 (Applications)

- 데이터 목록 처리, 빈도 세기·그룹화(`Counter`/`defaultdict`), 중복 제거.
- JSON 같은 중첩 구조 표현, 큐/스택(`deque`).

## 흔한 오해 (Common Misunderstandings)

- **`b = a` 는 복사가 아니다** — 같은 객체 참조(aliasing).
- **`[[0]*n]*m` 은 행을 공유한다** — comprehension으로 만들어야 독립.
- **dict 키는 hashable만** — 리스트는 키로 못 쓴다(tuple은 가능).
- **`set` 은 순서 의존 구조가 아니다** — 반복 순서에 기대지 말 것.
- **슬라이싱은 새 리스트를 만든다** — 큰 데이터에서 메모리 비용 의식.

## TMI

- 3.6 compact dict는 메모리를 ~20-25% 줄이면서 삽입 순서 보존을 "우연히" 얻었고, 3.7에서 언어 보장이 됐다.
- `Counter`·`defaultdict`·`deque`·`OrderedDict` 는 `collections` 의 단골 확장.
- `frozenset` 은 불변 집합이라 dict 키·다른 set의 원소가 될 수 있다.

## 연습 / 확인 문제 (Exercises)

- 문자열 목록의 단어 빈도를 `dict.get` 과 `Counter` 두 방식으로 세라.
- 순서를 유지하며 중복을 제거하라(`dict.fromkeys` 활용).
- `[[0]*3]*3` 의 aliasing 버그를 재현하고 comprehension으로 고쳐라.
- 큰 리스트에서 `in` 검색을 `set` 으로 바꿔 시간을 측정하라.

## 이어서 읽기 (Reading Path)

- 이전: [Python 기본 문법](Python-Setup-and-Syntax.md)
- 다음: [Python 함수와 모듈](Python-Functions-and-Modules.md)
- 관련: [배열](../../../Data-Structures/Array.md), [해시 테이블](../../../Data-Structures/Hash-Table.md)

## 참조 (References)

- [Programming/Arrays-and-Strings.md](../../Arrays-and-Strings.md)
- [Data-Structures/Hash-Table.md](../../../Data-Structures/Hash-Table.md)
