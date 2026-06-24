# 덱 (Deque, Double-Ended Queue)

- Level: Beginner
- Prerequisites: [Data-Structures/Queue.md](Queue.md), [Data-Structures/Linked-List.md](Linked-List.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

덱(deque)은 양쪽 끝에서 모두 삽입·삭제가 가능한 선형 자료구조다. 스택(한쪽 끝)과 큐(양 끝 분담)를 일반화하며, 슬라이딩 윈도우·양방향 처리에 쓰인다.

## 직관 (Intuition)

큐는 뒤로 넣고 앞에서 빼지만, 덱은 앞뒤 어디서든 넣고 뺄 수 있다. "양쪽이 열린 줄"이라고 보면 된다. 덕분에 최근 항목을 앞에서 빠르게 꺼내거나, 윈도우가 미끄러질 때 한쪽 끝의 오래된 값을 버리고 다른 끝에 새 값을 넣는 작업이 모두 상수 시간에 된다.

## 이론 (Theory)

덱은 네 가지 연산을 모두 `O(1)`에 지원한다: `push_front`, `push_back`, `pop_front`, `pop_back`. 구현은 두 가지가 흔하다.

- **이중 연결 리스트**: 양 끝 포인터로 상수 시간 삽입·삭제. 임의 접근은 안 됨.
- **원형 동적 배열(ring buffer)**: 앞뒤 인덱스를 모듈러로 관리. 임의 접근 `O(1)`, 가끔 재할당 비용.

스택과 큐는 덱의 제한된 사용으로 볼 수 있다. 단조 덱(monotonic deque)은 값을 단조 순서로 유지해 슬라이딩 윈도우 최댓값을 분할상환 `O(1)`에 구한다.

## 구현 (Implementation)

```python
from collections import deque

dq = deque()
dq.append(1)        # 뒤에 삽입
dq.appendleft(0)    # 앞에 삽입
dq.pop()            # 뒤에서 제거 -> 1
dq.popleft()        # 앞에서 제거 -> 0

# 슬라이딩 윈도우 최댓값 (단조 덱)
def max_window(nums, k):
    dq, out = deque(), []
    for i, x in enumerate(nums):
        while dq and nums[dq[-1]] <= x:
            dq.pop()                 # 작은 값 제거(단조 유지)
        dq.append(i)
        if dq[0] == i - k:
            dq.popleft()             # 윈도우 벗어난 인덱스 제거
        if i >= k - 1:
            out.append(nums[dq[0]])
    return out
```

## 복잡도 (Complexity)

| 연산 | 시간 |
|---|---|
| 양 끝 삽입/삭제 | `O(1)` |
| 임의 접근(배열 기반) | `O(1)` |
| 임의 위치 삽입/삭제 | `O(n)` |

공간은 `O(n)`이다. 단조 덱을 쓴 슬라이딩 윈도우 최댓값은 각 원소가 한 번씩 들어가고 나가므로 전체 `O(n)`이다.

## 응용 (Applications)

- 슬라이딩 윈도우 최대/최소(단조 덱)
- 작업 훔치기(work-stealing) 스케줄러
- 실행 취소/다시 실행, 최근 항목 버퍼
- BFS의 0-1 변형(0-1 BFS)

## 흔한 오해 (Common Misunderstandings)

- 덱은 스택이나 큐보다 항상 낫지 않다. 필요 없는 일반성은 오버헤드일 뿐이다.
- 연결 리스트 기반 덱은 임의 인덱스 접근이 `O(n)`이다.
- 파이썬 `list`의 `pop(0)`/`insert(0)`은 `O(n)`이라, 앞쪽 연산엔 `deque`를 써야 한다.
- 링 버퍼는 가득 차면 재할당이 필요해 개별 연산이 가끔 느릴 수 있다(분할상환은 `O(1)`).

## TMI

- 파이썬 `collections.deque`는 블록 이중 연결 리스트로 구현돼 양 끝 연산이 빠르다.
- 덱은 "deck"이 아니라 "deque"로 쓰고 보통 "덱"으로 읽는다.
- 0-1 BFS는 가중치가 0/1인 그래프에서 덱으로 다익스트라보다 빠르게 최단 경로를 구한다.

## 연습 / 확인 문제 (Exercises)

- 덱으로 스택과 큐를 각각 흉내 내는 코드를 작성하라.
- 슬라이딩 윈도우 최댓값을 단조 덱으로 구현하고 `O(n)`임을 설명하라.
- 링 버퍼 기반 덱에서 인덱스가 어떻게 모듈러로 관리되는지 그려라.

## 이어서 읽기 (Reading Path)

- 이전: [큐](Queue.md)
- 다음: [힙](Heap.md), [Algorithms/BFS-DFS.md](../Algorithms/BFS-DFS.md)

## 참조 (References)

- [Data-Structures/Queue.md](Queue.md)
- [Data-Structures/Linked-List.md](Linked-List.md)
- [Reference/Books.md](../Reference/Books.md)
