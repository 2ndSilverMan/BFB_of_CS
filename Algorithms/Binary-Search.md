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

사전에서 단어를 처음부터 넘기지 않고, 중간을 펴 앞/뒤를 판단해 절반을 버린다. 매 비교가 후보를 절반으로 줄여 $\lfloor\log_2 n\rfloor+1$ 번이면 끝난다. 필요한 단 하나의 조건: **"왼쪽은 전부 아니오, 오른쪽은 전부 예"** 처럼 경계가 한 번만 바뀌는 단조성.

## 이론 (Theory)

### 1. 불변식과 종료

전 과정에서 **불변식** "답이 있다면 `[left, right]` 안에 있다"를 유지한다. 매 반복마다 구간이 strictly 줄어드니 반드시 종료한다. 핵심 설계는 *경계와 종료조건을 불변식에 맞추는 것*이다.

| 형태 | 종료 | mid 갱신 | 쓰임 |
|---|---|---|---|
| `left <= right` (닫힌 구간) | `left > right` | `left=mid+1` / `right=mid-1` | 정확한 값 찾기 |
| `left < right` (반열린) | `left == right` | `left=mid+1` / `right=mid` | 경계(lower/upper bound) |

### 2. lower/upper bound

`lower_bound`는 `target` **이상인 첫 위치**, `upper_bound`는 **초과하는 첫 위치**. 둘의 차가 등장 횟수다. Python `bisect_left/right`가 이것이며, "찾았는지"가 아니라 "어디 끼울지"를 답한다.

### 3. 파라메트릭 서치 — 답을 이분하기

"최솟값 $x$ 를 직접 구하기"가 어려워도, **"$x$ 가 가능한가?"** 라는 술어 $P(x)$ 가 단조($P$ 가 어느 지점부터 계속 참)면 답을 이분할 수 있다.

$$P(x):\ \underbrace{\text{F F F F}}_{x<\text{답}}\ \underbrace{\text{T T T T}}_{x\ge\text{답}} \;\Rightarrow\; \text{경계 = 답}$$

예: "택배를 $D$ 일 안에 나르는 최소 적재량" → "적재량 $c$ 면 $D$ 일 안에 되나?"는 $c$ 에 단조 → 적재량을 이분. 정수뿐 아니라 실수(에 $\varepsilon$ 또는 고정 반복)로도 한다.

## 구현 (Implementation)

```python
def binary_search(a, target):              # 정확한 위치, 없으면 -1
    lo, hi = 0, len(a) - 1
    while lo <= hi:
        mid = lo + (hi - lo) // 2          # 오버플로 안전
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
    while lo < hi:
        mid = lo + (hi - lo) // 2
        if ok(mid): hi = mid               # 가능 → 더 작게
        else:       lo = mid + 1
    return lo
```

## 복잡도 (Complexity)

| 형태 | 시간 | 공간 |
|---|---|---|
| 반복 이진 탐색 | $O(\log n)$ (정확히 $\lfloor\log_2 n\rfloor+1$ 비교) | $O(1)$ |
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
- **`mid=(lo+hi)//2` 는 큰 정수에서 오버플로** 가능 → `lo+(hi-lo)//2`.

## TMI

- "아이디어는 쉬운데 구현 버그가 잦은 알고리즘"의 대명사 — Bentley는 *Programming Pearls*에서 "직접 짠 이진 탐색의 90%가 틀렸다"고 했다.
- Java `Arrays.binarySearch`는 못 찾으면 음수를 반환하는데, 그 값은 `-(삽입위치)-1` 로 **삽입 위치를 인코딩**한 것이다.
- JDK의 이진 탐색 `mid` 오버플로 버그가 2006년에야 공개 수정된 것은 유명한 일화다.

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

- [Algorithms/Sorting.md](Sorting.md)
- [Algorithms/Complexity.md](Complexity.md)
- [Reference/Books.md](../Reference/Books.md)
- [Reference/Courses.md](../Reference/Courses.md)
