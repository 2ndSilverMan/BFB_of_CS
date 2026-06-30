# 덱 (Deque, Double-Ended Queue)

- Level: Beginner
- Prerequisites: [Data-Structures/Queue.md](Queue.md), [Data-Structures/Linked-List.md](Linked-List.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

덱은 **양쪽 끝 모두에서 삽입·삭제가 $O(1)$** 인 선형 자료구조다. `push_front`, `push_back`, `pop_front`, `pop_back`. [스택](Stack.md)(한쪽 끝)과 [큐](Queue.md)(뒤로 넣고 앞으로 빼기)를 **특수 경우로 포함**하는 일반화다.

## 직관 (Intuition)

"양쪽이 열린 줄". 최근 항목을 앞에서 빠르게 꺼내거나, 윈도우가 미끄러질 때 한쪽 끝의 오래된 값을 버리고 다른 끝에 새 값을 넣는 일이 모두 상수 시간이다. 이 양방향성 덕에 **슬라이딩 윈도우 극값**과 **0-1 BFS** 같은, 큐만으로는 어색한 패턴이 깔끔해진다.

## 이론 (Theory)

### 1. 두 가지 구현과 트레이드오프

| 구현 | 양 끝 연산 | 임의 접근 | 메모리 | 비고 |
|---|---|---|---|---|
| 이중 연결 리스트 | $O(1)$ | $O(n)$ | 노드 오버헤드 | 크기 제한 없음 |
| 블록 이중 연결 리스트 | $O(1)$ | $O(n)$ | 블록 단위 | CPython `deque` 방식 |
| 원형 동적 배열(ring buffer) | amortized $O(1)$ | $O(1)$ | 조밀 | C++ `std::deque`는 블록 배열 |

CPython `collections.deque`는 **고정 크기 블록들의 이중 연결 리스트**라, 양 끝 push/pop은 빠르지만 가운데 인덱싱은 $O(n)$이다.

### 2. monotonic deque — 핵심 알고리즘

윈도우 최댓값을 매번 다시 스캔하면 $O(nk)$. 덱에 **값이 단조 감소하도록 인덱스를 유지**하면, 새 값이 들어올 때 그보다 작은 꼬리들을 버리고(어차피 답이 될 일 없음), 윈도우를 벗어난 머리를 버린다. 각 원소가 **정확히 한 번 push·한 번 pop** 되므로 전체 $O(n)$ (amortized $O(1)$/원소). 덱 머리가 항상 현재 윈도우의 최댓값 인덱스다.

### 3. 0-1 BFS

간선 가중치가 0 또는 1뿐인 그래프에서, 가중치 0 간선은 `push_front`, 1 간선은 `push_back` 하면 덱이 거리 순 정렬을 유지해 다익스트라($O(E\log V)$) 대신 **$O(V+E)$** 로 최단 거리를 구한다.

## 구현 (Implementation)

```python
from collections import deque

dq = deque()
dq.append(1)       # 뒤로
dq.appendleft(0)   # 앞으로
dq.pop()           # 뒤에서 → 1
dq.popleft()       # 앞에서 → 0

def max_window(nums, k):                 # 슬라이딩 윈도우 최댓값, 전체 O(n)
    dq, out = deque(), []                # dq: 인덱스, 대응 값은 단조 감소
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] <= x:
            dq.pop()                     # 더 작은 꼬리는 버림(단조 유지)
        dq.append(i)
        if dq[0] == i - k:               # 윈도우를 벗어난 머리 제거
            dq.popleft()
        if i >= k - 1:
            out.append(nums[dq[0]])      # 머리 = 윈도우 최댓값
    return out
```

## 복잡도 (Complexity)

| 연산 | 시간 |
|---|---|
| 양 끝 삽입/삭제 | $O(1)$ (ring buffer는 amortized) |
| 임의 접근(배열 기반) | $O(1)$ |
| 임의 접근(링크 기반) | $O(n)$ |
| 임의 위치 삽입/삭제 | $O(n)$ |

공간 $O(n)$. **워크드 예제** `max_window([1,3,-1,-3,5], k=3)`: i0 dq=[0]; i1 `1≤3`→pop0, dq=[1]; i2 dq=[1,2]→윈도우 첫 출력 `nums[1]=3`; i3 dq=[1,2,3]→출력 `3`; i4 x=5 pop3,pop2 그리고 머리 `1`이 `i-k=1`이라 popleft, dq=[4]→출력 `5`. 결과 `[3,3,5]`. 각 인덱스 한 번 push/pop.

## 응용 (Applications)

- 슬라이딩 윈도우 최대/최소(단조 덱).
- 0-1 BFS 최단 경로.
- **work-stealing 스케줄러**: 각 워커가 자기 덱의 한쪽에서 작업을 꺼내고, 노는 워커가 반대쪽에서 훔친다(Chase–Lev 덱).
- 최근 항목 버퍼, undo/redo, palindrome 검사(양 끝 비교).

## 흔한 오해 (Common Misunderstandings)

- **덱이 항상 더 낫지 않다** — 필요 없는 일반성은 오버헤드다. 한쪽만 쓰면 스택/큐가 더 단순·빠르다.
- **링크 기반 덱은 임의 인덱스 접근이 $O(n)$**.
- Python `list`의 `insert(0)`/`pop(0)`은 $O(n)$ — 앞쪽 연산엔 `deque`.
- 링 버퍼 덱은 가득 차면 재할당이 필요해 **개별 연산이 가끔 느릴 수 있다**(amortized는 $O(1)$).

## TMI

- C++ `std::deque`는 단일 연속 메모리가 아니라 **고정 크기 블록들의 배열**이다. 그래서 `&dq[0]`로 전체를 연속 버퍼로 넘길 수 없다(이게 `vector`와의 큰 차이).
- work-stealing 덱(Chase–Lev)은 Java `ForkJoinPool`, Go 런타임, Rust `rayon` 등 현대 병렬 런타임의 심장부다.
- 덱은 deque로 쓰지만 "deck"으로 읽는 사람도 많다 — 표기는 double-ended queue.

## 연습 / 확인 문제 (Exercises)

- 덱으로 스택과 큐를 각각 흉내 내고, 어떤 연산만 쓰면 되는지 적어라.
- 슬라이딩 윈도우 최댓값을 단조 덱으로 구현하고 왜 전체 $O(n)$ 인지(각 원소 1 push/1 pop) 논증하라.
- 0-1 BFS에서 가중치 0/1 간선을 각각 어느 끝에 넣어야 거리 순서가 유지되는지 설명하라.
- 링 버퍼 덱에서 앞/뒤 인덱스가 모듈러로 어떻게 도는지 가득참 판정과 함께 그려라.

## 이어서 읽기 (Reading Path)

- 이전: [큐](Queue.md)
- 다음: [힙](Heap.md)
- 관련: [BFS·DFS](../Algorithms/BFS-DFS.md), [스택](Stack.md)

## 참조 (References)

- [Data-Structures/Queue.md](Queue.md)
- [Data-Structures/Linked-List.md](Linked-List.md)
- [Reference/Books.md](../Reference/Books.md)
