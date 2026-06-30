# 정렬 (Sorting)

- Level: Beginner
- Prerequisites: [Programming/Arrays-and-Strings.md](../Programming/Arrays-and-Strings.md), [Algorithms/Complexity.md](Complexity.md)
- Status: Review
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

정렬은 원소를 정해진 기준으로 순서대로 배치한다. 단순해 보이지만 **비교 정렬의 이론적 하한, 안정성, 제자리 여부, 키 분포 활용**이 얽힌 풍부한 주제이며, 이진 탐색·그룹화·탐욕 등 수많은 알고리즘의 전처리다.

## 직관 (Intuition)

정렬된 데이터는 다루기 쉽다 — 이진 탐색이 가능하고, 인접한 중복이 모이며, 순위·구간 질의가 단순해진다. 핵심 질문 둘: **"비교만으로 얼마나 빠를 수 있나?"**(→ $\Omega(n\log n)$ 하한)와 **"키에 구조가 있으면 그 벽을 넘을 수 있나?"**(→ 계수/기수 정렬).

## 이론 (Theory)

### 1. 비교 정렬의 하한 $\Omega(n\log n)$

비교 정렬은 "두 원소 비교"의 결과로 분기하는 **이진 결정 트리**로 모델링된다. $n$ 개의 가능한 순열 $n!$ 개가 각각 다른 잎이어야 하므로 트리 높이(최악 비교 수)는

$$h \ge \lceil \log_2(n!)\rceil = \Theta(n\log n)\quad(\text{스털링})$$

즉 **어떤 비교 정렬도 최악 $\Omega(n\log n)$** — 병합·힙 정렬이 이 하한을 만난다.

### 2. 비교 기준 4가지

| 기준 | 의미 |
|---|---|
| 시간 | 비교·이동 비용 |
| 공간 | 추가 메모리(제자리=in-place는 $O(1)$~$O(\log n)$) |
| 안정성 | 같은 키의 상대 순서 보존 |
| 적응성 | 거의 정렬된 입력에서 빨라짐 |

| 알고리즘 | 평균 | 최악 | 공간 | 안정 |
|---|---|---|---|---|
| 삽입 | $O(n^2)$ | $O(n^2)$ | $O(1)$ | ✅ (적응적, 최선 $O(n)$) |
| 병합 | $O(n\log n)$ | $O(n\log n)$ | $O(n)$ | ✅ |
| 퀵 | $O(n\log n)$ | $O(n^2)$ | $O(\log n)$ | ❌ |
| 힙 | $O(n\log n)$ | $O(n\log n)$ | $O(1)$ | ❌ |

### 3. 퀵 정렬: 분할과 피벗

피벗 기준으로 분할(Lomuto/Hoare) 후 양쪽 재귀. 균형 분할이면 $T(n)=2T(n/2)+n=O(n\log n)$ 이지만, **정렬된 입력 + 끝값 피벗**이면 한쪽이 비어 $O(n^2)$. 방어: **랜덤 피벗** 또는 **median-of-three**, 그리고 깊이가 깊어지면 힙 정렬로 전환하는 **introsort**(C++ `std::sort`).

### 4. 비교의 벽을 넘기: 계수·기수 정렬

키 범위 $k$ 가 작으면 비교를 아예 안 한다.

- **계수 정렬(counting)**: 각 키 빈도를 세어 위치 계산 → $O(n+k)$, 안정.
- **기수 정렬(radix, LSD)**: 자릿수마다 계수 정렬 $d$ 번 → $O(d(n+k))$.
- **버킷 정렬**: 균등 분포 가정 시 평균 $O(n)$.

## 구현 (Implementation)

```python
def merge_sort(a):                       # 안정, O(n log n)
    if len(a) <= 1: return a
    mid = len(a) // 2
    L, R = merge_sort(a[:mid]), merge_sort(a[mid:])
    out, i, j = [], 0, 0
    while i < len(L) and j < len(R):
        if L[i] <= R[j]: out.append(L[i]); i += 1   # <= 라서 안정
        else:            out.append(R[j]); j += 1
    return out + L[i:] + R[j:]

def counting_sort(a, k):                 # 키 0..k-1, O(n+k), 안정
    cnt = [0] * k
    for x in a: cnt[x] += 1
    for i in range(1, k): cnt[i] += cnt[i-1]    # 누적 → 끝 위치
    out = [0] * len(a)
    for x in reversed(a):                # 뒤에서: 안정성 보존
        cnt[x] -= 1; out[cnt[x]] = x
    return out
```

다중 기준 정렬은 **안정 정렬을 약한 키부터** 적용하거나 튜플 키를 쓴다: `sorted(people, key=lambda p: (-p.score, p.name))`.

## 복잡도 (Complexity)

| 알고리즘 | 시간 | 공간 | 비고 |
|---|---|---|---|
| 삽입 | 최선 $O(n)$ / 최악 $O(n^2)$ | $O(1)$ | 작은/거의정렬 배열 |
| 병합 | $O(n\log n)$ | $O(n)$ | 안정, 외부정렬 |
| 퀵(introsort) | 평균 $O(n\log n)$ | $O(\log n)$ | 실측 빠름 |
| 계수/기수 | $O(n+k)$/$O(d(n+k))$ | $O(n+k)$ | 키 범위 제한 시 |

**워크드 예제.** `[3,1,2,1]` 계수 정렬($k=4$): 빈도 `[0,2,1,1]` → 누적 `[0,2,3,4]`. 뒤에서 `1→cnt[1]=1` 위치1, `2→cnt[2]=2` 위치2, `1→cnt[1]=0` 위치0, `3→cnt[3]=3` 위치3 → `[1,1,2,3]`, 두 `1`의 원래 순서 보존(안정).

## 응용 (Applications)

- 이진 탐색·중복 제거·그룹화·순위 계산의 전처리.
- 스케줄링·탐욕 알고리즘(구간 정렬 후 처리).
- 외부 정렬(메모리 초과 데이터, 병합 정렬 기반), DB `ORDER BY`.

## 흔한 오해 (Common Misunderstandings)

- **모든 정렬이 $O(n\log n)$ 은 아니다** — 단순 정렬은 $O(n^2)$, 계수/기수는 비교가 아니라 $O(n+k)$.
- **퀵 정렬은 평균 빠르지만 최악 $O(n^2)$** — 방어(랜덤/중앙값/introsort) 없이는 적대적 입력에 취약.
- **안정성은 다중 기준 정렬에서 중요** — 불안정 정렬을 약한 키부터 적용하면 깨진다.
- **계수/기수가 항상 빠르지 않다** — 키 범위 $k$ 가 크면 $O(n+k)$ 가 손해.

## TMI

- Python·Java의 표준 정렬은 **Timsort**(Tim Peters) — 자연스러운 정렬 run을 찾아 병합하고 galloping으로 가속, 거의 정렬된 데이터에서 $O(n)$ 에 가깝다.
- Python `list.sort()`/`sorted()`는 안정 → "약한 키부터 차례로 정렬" 테크닉이 성립.
- 문자열 정렬은 사람이 기대하는 순서와 다를 수 있다(대소문자·한글·악센트·유니코드 정규화·locale).
- 2002년경 발견된 Timsort의 병합 불변식 버그가 2015년 형식 검증(KeY)으로 재발견·수정된 일은 유명하다.

## 연습 / 확인 문제 (Exercises)

- 결정 트리 논증으로 비교 정렬 하한 $\lceil\log_2(n!)\rceil$ 을 설명하라.
- 삽입 정렬이 거의 정렬된 배열에서 $O(n)$ 인 이유를 적응성으로 설명하라.
- 계수 정렬이 안정이 되도록 "뒤에서부터" 배치하는 이유를 보여라.
- 학생을 점수 내림차순·이름 오름차순으로 안정 정렬하라.

## 이어서 읽기 (Reading Path)

- 이전: [복잡도 분석](Complexity.md)
- 다음: [이진 탐색](Binary-Search.md)
- 관련: [분할 정복](Divide-and-Conquer.md), [힙](../Data-Structures/Heap.md)

## 참조 (References)

- [Algorithms/Complexity.md](Complexity.md)
- [Algorithms/Binary-Search.md](Binary-Search.md)
- [Data-Structures/Heap.md](../Data-Structures/Heap.md)
- [Reference/Books.md](../Reference/Books.md)
- [Reference/Courses.md](../Reference/Courses.md)
