# 큐 (Queue)

- Level: Beginner
- Prerequisites: [Data-Structures/Array.md](Array.md), [Data-Structures/Linked-List.md](Linked-List.md)
- Status: Draft

---

## 개념 (Concept)

큐는 먼저 넣은 값이 먼저 나오는 FIFO(First In, First Out) 자료구조다. 핵심 연산은 뒤에 값을 넣는 `enqueue`, 앞에서 값을 꺼내는 `dequeue`, 맨 앞 값을 확인하는 `front`이다.

## 직관 (Intuition)

큐는 줄 서기와 같다. 먼저 줄 선 사람이 먼저 처리된다. 새로 온 사람은 뒤에 서고, 처리할 때는 앞에서부터 처리한다.

BFS는 큐를 사용해 가까운 노드부터 차례대로 탐색한다. 그래서 큐는 그래프 탐색과 작업 스케줄링에서 자주 등장한다.

## 이론 (Theory)

큐 ADT의 기본 연산은 다음과 같다.

| 연산 | 의미 |
|---|---|
| `enqueue(x)` | x를 뒤에 넣음 |
| `dequeue()` | 앞 값을 제거하고 반환 |
| `front()` | 앞 값을 제거하지 않고 확인 |
| `is_empty()` | 비어 있는지 확인 |

배열의 앞에서 값을 삭제하면 남은 원소를 당겨야 해서 O(n)이 될 수 있다. 그래서 실전에서는 원형 버퍼나 양쪽 끝 연산이 빠른 deque를 많이 쓴다.

## 구현 (Implementation)

Python의 `collections.deque` 사용:

```python
from collections import deque

queue = deque()
queue.append("A")
queue.append("B")
queue.append("C")

print(queue.popleft())  # A
print(queue.popleft())  # B
```

간단한 큐 래퍼:

```python
from collections import deque


class Queue:
    def __init__(self):
        self._items = deque()

    def enqueue(self, value):
        self._items.append(value)

    def dequeue(self):
        if self.is_empty():
            return None
        return self._items.popleft()

    def front(self):
        if self.is_empty():
            return None
        return self._items[0]

    def is_empty(self):
        return len(self._items) == 0
```

## 복잡도 (Complexity)

| 연산 | 시간 | 공간 |
|---|---|---|
| `enqueue` | O(1) | O(1) |
| `dequeue` | O(1) | O(1) |
| `front` | O(1) | O(1) |
| n개 원소 저장 | O(n) | O(n) |

위 복잡도는 deque나 원형 버퍼처럼 앞/뒤 연산이 빠른 구현을 기준으로 한다.

## 응용 (Applications)

- BFS
- 작업 대기열
- 프린터 큐
- 이벤트 처리
- 생산자-소비자 패턴

## 흔한 오해 (Common Misunderstandings)

- Python 리스트에서 `pop(0)`을 큐처럼 쓰면 O(n)이 될 수 있다.
- 큐는 우선순위가 없다. 우선순위가 필요하면 우선순위 큐/힙을 사용한다.
- 큐가 비어 있을 때 `dequeue`를 어떻게 처리할지 정해야 한다. 예외를 던질 수도 있고 `None`을 반환할 수도 있다.
- BFS에서 큐에 넣을 때 방문 처리하지 않으면 같은 노드가 여러 번 들어갈 수 있다.

## 연습 / 확인 문제 (Exercises)

- deque를 사용해 큐 클래스를 구현하라.
- 큐를 사용해 숫자 1부터 n까지 차례대로 처리하는 시뮬레이션을 작성하라.
- BFS 코드에서 큐가 어떤 순서로 변하는지 작은 그래프로 추적하라.

## 이어서 읽기 (Reading Path)

- 이전: [스택](Stack.md)
- 다음: [그래프 표현](Graph-Representation.md)

## 참조 (References)

- [Data-Structures/Array.md](Array.md)
- [Algorithms/BFS-DFS.md](../Algorithms/BFS-DFS.md)
