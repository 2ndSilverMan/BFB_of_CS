# 이진 탐색 (Binary Search)

- Level: Beginner
- Prerequisites: [Programming/Arrays-and-Strings.md](../Programming/Arrays-and-Strings.md), [Algorithms/Complexity.md](Complexity.md), [Algorithms/Sorting.md](Sorting.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

이진 탐색은 **단조(monotone)한 탐색 공간**에서 가운데를 보고 절반을 버리며 답을 좁히는 알고리즘이다. 정렬 배열의 값 찾기가 대표지만, 본질은 "정렬"이 아니라 **단조 술어(predicate)** — 이 일반화가 파라메트릭 서치의 위력이다.

## 직관 (Intuition)

사전에서 단어를 처음부터 넘기지 않고, 중간을 펴 앞/뒤를 판단해 절반을 버린다. 닫힌 구간에서 값을 찾는 아래 구현은 $n\ge1$일 때 최대 $\lfloor\log_2 n\rfloor+1$회 반복하고, 빈 배열에서는 반복하지 않는다. 한 반복에서 값 비교는 두 번 일어날 수 있으므로 반복 횟수와 개별 비교 횟수를 구분한다. 핵심 조건은 **"왼쪽은 전부 아니오, 오른쪽은 전부 예"** 처럼 경계가 한 번만 바뀌는 단조성이다.

## 이론 (Theory)

### 1. 불변식과 종료

전 과정에서 **불변식** "답이 있다면 `[left, right]` 안에 있다"를 유지한다. 매 반복마다 구간이 strictly 줄어드니 반드시 종료한다. 핵심 설계는 *경계와 종료조건을 불변식에 맞추는 것*이다.

| 형태 | 종료 | mid 갱신 | 쓰임 |
|---|---|---|---|
| `left <= right` (닫힌 구간) | `left > right` | `left=mid+1` / `right=mid-1` | 정확한 값 찾기 |
| `left < right` (반열린) | `left == right` | `left=mid+1` / `right=mid` | 경계(lower/upper bound) |

표의 반열린 구간은 아직 살펴볼 배열 원소 `[left, right)`를 뜻한다. `lower_bound`의 반환 후보는 끝 삽입 위치까지 포함한 `[left, right]`에 있다. 불변식은 `a[:left]`의 모든 값이 target보다 작고 `a[right:]`의 모든 값이 target 이상이라는 것이다. 따라서 원소를 못 찾아도 `len(a)`라는 정상적인 삽입 위치를 반환할 수 있다.

### 2. lower/upper bound

`lower_bound`는 `target` **이상인 첫 위치**, `upper_bound`는 **초과하는 첫 위치**. 그런 원소가 없으면 둘 다 배열 끝 위치를 반환한다. 둘의 차가 등장 횟수다. Python `bisect_left/right`가 이것이며, "찾았는지"가 아니라 "어디 끼울지"를 답한다. ([Python `bisect`의 삽입 위치 계약](https://docs.python.org/3/library/bisect.html))

### 3. 파라메트릭 서치 — 답을 이분하기

"최솟값 $x$ 를 직접 구하기"가 어려워도, **"$x$ 가 가능한가?"** 라는 술어 $P(x)$ 가 단조($P$ 가 어느 지점부터 계속 참)면 답을 이분할 수 있다.

$$P(x):\ \underbrace{\text{F F F F}}_{x<\text{답}}\ \underbrace{\text{T T T T}}_{x\ge\text{답}} \;\Rightarrow\; \text{경계 = 답}$$

예: "택배를 $D$ 일 안에 나르는 최소 적재량" → "적재량 $c$ 면 $D$ 일 안에 되나?"는 $c$ 에 단조 → 적재량을 이분. 정수뿐 아니라 실수(에 $\varepsilon$ 또는 고정 반복)로도 한다.

## 구현 (Implementation)

```python
def binary_search(a, target):              # 정확한 위치, 없으면 -1
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2          # 고정 폭 정수로 옮길 때 합의 오버플로 회피
        if a[mid] == target: return mid
        if a[mid] < target:  lo = mid + 1
        else:                hi = mid - 1
    return -1

def lower_bound(a, target):                # target 이상인 첫 인덱스
    lo, hi = 0, len(a)                     # 반열린 [lo, hi)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if a[mid] < target: lo = mid + 1
        else:               hi = mid
    return lo

def smallest_feasible(lo, hi, ok):         # 파라메트릭: ok가 단조 F..FT..T
    if lo > hi or not ok(hi):
        raise ValueError("a nonempty range with a feasible upper bound is required")
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if ok(mid): hi = mid               # 가능 → 더 작게
        else:       lo = mid + 1
    return lo
```

`smallest_feasible`는 정수 구간 `[lo, hi]` 안의 답을 반환한다. `ok`는 호출 중 결과가 변하지 않는 단조 술어여야 하며, 상한 `hi`는 실제로 가능해야 한다. 위 코드는 빈 구간과 불가능한 상한을 거부하지만 단조성 자체를 검사하지는 않는다.

### 경계 입력과 기대 결과

| 배열 `a` | target | `binary_search` | `lower_bound` | `bisect_right` |
|---|---|---|---|---|
| `[]` | 2 | -1 | 0 | 0 |
| `[2]` | 2 | 0 | 0 | 1 |
| `[2]` | 1 | -1 | 0 | 0 |
| `[2]` | 3 | -1 | 1 | 1 |
| `[1, 2, 2, 4]` | 2 | 1 또는 2 | 1 | 3 |
| `[1, 2, 2, 4]` | 3 | -1 | 3 | 3 |
| `[1, 2, 2, 4]` | 5 | -1 | 4 | 4 |

아래 코드는 앞의 함수 정의 뒤에 이어서 실행한다. 중복값의 정확한 검색 위치는 하나로 고정하지 않고 반환 인덱스가 목표 값을 가리키는지 검사한다.

```python
from bisect import bisect_left, bisect_right

cases = [
    ([], 2, 0, 0),
    ([2], 2, 0, 1),
    ([2], 1, 0, 0),
    ([2], 3, 1, 1),
    ([1, 2, 2, 4], 2, 1, 3),
    ([1, 2, 2, 4], 3, 3, 3),
    ([1, 2, 2, 4], 5, 4, 4),
]
for a, target, expected_left, expected_right in cases:
    index = binary_search(a, target)
    if target in a:
        assert 0 <= index < len(a) and a[index] == target
    else:
        assert index == -1
    assert lower_bound(a, target) == bisect_left(a, target) == expected_left
    assert bisect_right(a, target) == expected_right
    assert expected_right - expected_left == a.count(target)

assert smallest_feasible(0, 10, lambda x: x >= 7) == 7
assert smallest_feasible(0, 10, lambda x: True) == 0
assert smallest_feasible(7, 7, lambda x: x >= 7) == 7
for lo, hi in [(0, 10), (3, 2)]:
    try:
        smallest_feasible(lo, hi, lambda x: False)
    except ValueError:
        pass
    else:
        raise AssertionError("an invalid search range was accepted")
print("7 boundary cases and 5 predicate cases passed")
```

## 복잡도 (Complexity)

| 형태 | 시간 | 공간 |
|---|---|---|
| 반복 이진 탐색 | $O(\log n)$, 값 찾기 구현은 $n\ge1$에서 최대 $\lfloor\log_2 n\rfloor+1$회 반복 | $O(1)$ |
| 재귀 이진 탐색 | $O(\log n)$ | $O(\log n)$ 스택 |
| 파라메트릭(값 범위 $R$) | $O(\log R \times C_{\text{check}})$ | 술어 비용에 의존 |
| 미정렬 → 정렬 후 1회 탐색 | $O(n\log n)$ | 정렬에 의존 |

한 번만 찾을 거면 정렬 비용($O(n\log n)$)이 선형 탐색($O(n)$)보다 비싸다 — **반복 질의일 때** 정렬+이분이 이득.

## 응용 (Applications)

- 정렬 배열 값/경계 찾기, 등장 횟수(`upper-lower`).
- **파라메트릭 서치**: 최소 최대화/최대 최소화, 자원 할당, 시간 제한 하 최소 용량.
- 회전 정렬 배열 탐색, 실수 방정식 근(이분법), `√x`·단조 함수 역.

## 흔한 오해 (Common Misunderstandings)

- **미정렬(또는 비단조)엔 못 쓴다** — 전제는 단조성.
- **`<=` 와 `<` 는 다른 템플릿** — 불변식에 맞춰 경계·종료를 정하지 않으면 off-by-one/무한 루프.
- **중복이 있으면 일반 이진 탐색은 아무 위치나** 반환 — 첫/마지막은 lower/upper bound로.
- **`mid=(lo+hi)//2`는 고정 폭 정수의 합에서 오버플로** 가능 → 유효한 비음수 인덱스 범위에서는 `lo+(hi-lo)//2`로 피한다. Python의 기본 `int`는 임의 정밀도이므로 같은 정수 오버플로가 발생하지 않는다. ([Joshua Bloch의 JDK 버그 설명](https://research.google/blog/extra-extra-read-all-about-it-nearly-all-binary-searches-and-mergesorts-are-broken/), [Python 숫자 타입](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex))

## TMI

- Joshua Bloch는 2006년 글에서 Bentley의 이진 탐색 설명과 자신이 작성한 JDK 구현에 같은 오버플로 문제가 있었다고 회고했다. 불변식뿐 아니라 실행 언어의 정수 범위도 확인해야 하는 사례다.
- Java `Arrays.binarySearch`는 못 찾으면 음수를 반환하는데, 그 값은 `-(삽입위치)-1` 로 **삽입 위치를 인코딩**한 것이다.
- 위 글은 2006년 공개된 작성자의 버그 설명이다. 공개 설명 날짜와 실제 수정 버전·배포 날짜는 별도로 구분해야 한다.

## 연습 / 확인 문제 (Exercises)

- 정렬 배열에서 값의 인덱스를, 없으면 `-1` 을 반환하라.
- `target` 의 첫/마지막 위치를 lower/upper bound로 구하고 등장 횟수를 계산하라.
- "$D$ 일 안에 나르는 최소 적재량"을 파라메트릭 서치로 풀고 술어의 단조성을 보여라.
- 회전 정렬 배열(`[4,5,6,0,1,2]`)에서 값 찾기를 $O(\log n)$ 에 구현하라.

## 이어서 읽기 (Reading Path)

- 이전: [정렬](Sorting.md)
- 다음: [BFS / DFS](BFS-DFS.md)
- 관련: [복잡도 분석](Complexity.md), [분할 정복](Divide-and-Conquer.md)

## 참조 (References)

- [Python — `bisect`](https://docs.python.org/3/library/bisect.html): `bisect_left/right`의 삽입 위치, 중복값 경계와 검색·삽입 비용을 확인할 직접 출처.
- [Joshua Bloch — Nearly All Binary Searches and Mergesorts are Broken (2006)](https://research.google/blog/extra-extra-read-all-about-it-nearly-all-binary-searches-and-mergesorts-are-broken/): JDK 구현 작성자가 설명한 중간값 오버플로 사례와 수정 식.
- [Python — Numeric Types](https://docs.python.org/3/library/stdtypes.html#numeric-types-int-float-complex): Python 기본 정수의 임의 정밀도를 확인하는 공식 출처.
- [Algorithms/Sorting.md](Sorting.md)
- [Algorithms/Complexity.md](Complexity.md)
- [Reference/Books.md](../Reference/Books.md)
- [Reference/Courses.md](../Reference/Courses.md)

## 재작성 메모 (Rewrite Notes)

- 재사용할 재료: 닫힌 검색 구간과 삽입 위치 불변식, 7개 경계 입력의 기대 결과, 표준 `bisect`와 대조하는 assert, 불가능한 파라메트릭 검색 상한을 거부하는 예제.
- 보충할 내용: 택배 적재량 문제의 구체 입력과 단조성 증명, 두 원소 구간에서 잘못된 갱신이 무한 반복되는 추적, 고정 폭 정수 언어로 옮길 때의 경계 테스트.
- 확인 상태: 2026-09-11 Python `bisect`·숫자 타입 문서와 Bloch의 원문에서 참조에 적은 계약과 사례를 대조했다. Python 3.12.10에서 본문의 코드 블록을 순서대로 실행해 배열 경계 7개와 술어 검색 5개 사례의 assert가 통과했다. 회전 배열·실수 이분법 구현은 이번 실행 범위에 포함하지 않았다.
