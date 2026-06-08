# 스택 (Stack)

- Level: Beginner
- Prerequisites: [Data-Structures/Array.md](Array.md), [Data-Structures/Linked-List.md](Linked-List.md)
- Status: Draft

---

## 개념 (Concept)

스택은 가장 나중에 넣은 값이 가장 먼저 나오는 LIFO(Last In, First Out) 자료구조다. 핵심 연산은 값을 넣는 `push`, 가장 위 값을 꺼내는 `pop`, 가장 위 값을 확인하는 `peek`이다.

## 직관 (Intuition)

스택은 접시 더미와 비슷하다. 새 접시는 맨 위에 올리고, 꺼낼 때도 맨 위 접시부터 꺼낸다. 중간에 있는 접시를 바로 꺼내는 구조가 아니다.

프로그램 실행의 함수 호출도 스택처럼 이해할 수 있다. 함수가 호출되면 호출 정보가 쌓이고, 함수가 끝나면 가장 최근 호출부터 돌아간다.

## 이론 (Theory)

스택 ADT(Abstract Data Type)는 구현 방식보다 연산 규칙이 중요하다.

| 연산 | 의미 |
|---|---|
| `push(x)` | x를 맨 위에 넣음 |
| `pop()` | 맨 위 값을 제거하고 반환 |
| `peek()` | 맨 위 값을 제거하지 않고 확인 |
| `is_empty()` | 비어 있는지 확인 |

스택은 배열이나 연결 리스트로 구현할 수 있다. 동적 배열을 쓰면 끝에 추가/삭제를 평균 O(1)로 처리할 수 있어 실용적이다.

## 구현 (Implementation)

Python 리스트로 구현:

```python
class Stack:
    def __init__(self):
        self._items = []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        if self.is_empty():
            return None
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0
```

괄호 검사:

```python
def is_balanced(text):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}

    for char in text:
        if char in "([{":
            stack.append(char)
        elif char in pairs:
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0
```

## 복잡도 (Complexity)

| 연산 | 시간 | 공간 |
|---|---|---|
| `push` | 평균 O(1) | O(1) |
| `pop` | O(1) | O(1) |
| `peek` | O(1) | O(1) |
| n개 원소 저장 | O(n) | O(n) |

동적 배열 기반 `push`는 용량 확장 순간 최악 O(n)이지만, 여러 번의 평균으로는 O(1)이다.

## 응용 (Applications)

- 함수 호출 스택
- 괄호 짝 검사
- DFS의 명시적 스택 구현
- 실행 취소(undo)
- 후위 표기식 계산

## 흔한 오해 (Common Misunderstandings)

- 스택은 정렬된 자료구조가 아니다.
- `pop`은 보통 값을 확인하는 동시에 제거한다. 확인만 하려면 `peek`을 쓴다.
- 재귀는 내부적으로 호출 스택을 사용하므로 깊이가 커지면 스택 오버플로가 날 수 있다.
- 배열의 앞쪽을 스택의 top으로 쓰면 삽입/삭제가 O(n)이 될 수 있다. 끝쪽을 top으로 쓰는 편이 일반적이다.

## TMI

- 스택의 LIFO는 "Last In, First Out"의 약자다. 접시를 쌓아 두면 나중에 올린 접시를 먼저 꺼내는 것과 같다.
- 프로그램 오류 메시지에서 자주 보는 "stack trace"는 함수 호출이 어떤 순서로 쌓였는지 보여 주는 기록이다.
- 웹 브라우저의 뒤로 가기/앞으로 가기, 편집기의 undo/redo는 스택 두 개로 설명하기 좋은 대표 사례다.
- "stack overflow"는 호출 스택이 너무 깊어져서 더 쌓을 공간이 없을 때 나는 오류 이름이기도 하다.

## 연습 / 확인 문제 (Exercises)

- 문자열의 괄호 `()[]{}` 짝이 맞는지 검사하라.
- 스택 두 개로 큐를 구현하는 방법을 설명하라.
- 재귀 DFS를 명시적 스택 DFS로 바꿔 보라.

## 이어서 읽기 (Reading Path)

- 이전: [연결 리스트](Linked-List.md)
- 다음: [큐](Queue.md)

## 참조 (References)

- [Data-Structures/Array.md](Array.md)
- [Algorithms/BFS-DFS.md](../Algorithms/BFS-DFS.md)
- [Reference/Books.md](../Reference/Books.md)
- [Reference/Courses.md](../Reference/Courses.md)
