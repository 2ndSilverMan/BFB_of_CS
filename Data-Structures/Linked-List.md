# 연결 리스트 (Linked List)

- Level: Beginner
- Prerequisites: [Programming/Variables-and-Types.md](../Programming/Variables-and-Types.md), [Programming/Functions-and-Recursion.md](../Programming/Functions-and-Recursion.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

연결 리스트는 각 원소가 값과 다음 원소를 가리키는 링크를 함께 가지는 선형 자료구조다. 원소들이 메모리에서 연속될 필요가 없고, 링크를 따라가며 순서가 정해진다.

## 직관 (Intuition)

배열이 번호가 붙은 연속된 칸이라면, 연결 리스트는 다음 주소가 적힌 쪽지들의 사슬이다. 첫 노드를 알면 다음 노드, 그다음 노드를 차례로 따라갈 수 있다.

중간에 새 노드를 넣을 때는 주변 링크만 바꾸면 된다. 하지만 i번째 원소를 바로 찾아갈 수 없어서 앞에서부터 따라가야 한다.

## 이론 (Theory)

가장 기본적인 단일 연결 리스트 노드는 다음 정보를 가진다.

| 필드 | 의미 |
|---|---|
| value | 저장할 값 |
| next | 다음 노드에 대한 참조 |

연결 리스트의 핵심 연산은 링크 변경이다.

```text
A -> B -> C

B 뒤에 X 삽입:
B.next = X
X.next = C

A -> B -> X -> C
```

## 구현 (Implementation)

```python
class Node:
    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node


head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

current = head
while current is not None:
    print(current.value)
    current = current.next
```

앞에 삽입하기:

```python
def push_front(head, value):
    return Node(value, head)
```

값 찾기:

```python
def contains(head, target):
    current = head
    while current is not None:
        if current.value == target:
            return True
        current = current.next
    return False
```

## 복잡도 (Complexity)

| 연산 | 시간 | 공간 |
|---|---|---|
| 첫 원소 접근 | O(1) | O(1) |
| i번째 원소 접근 | O(n) | O(1) |
| 값 검색 | O(n) | O(1) |
| 맨 앞 삽입 | O(1) | O(1) |
| 현재 노드 뒤 삽입 | O(1) | O(1) |
| 특정 값 삭제 | O(n) | O(1) |

삽입/삭제가 O(1)이라는 말은 이미 해당 위치의 노드를 알고 있을 때다. 그 위치를 찾는 비용은 별도로 든다.

## 응용 (Applications)

- 스택과 큐의 연결 기반 구현
- 빈번한 앞쪽 삽입/삭제
- 노드 단위로 구조를 바꿔야 하는 알고리즘
- 해시 테이블의 체이닝 충돌 처리

## 흔한 오해 (Common Misunderstandings)

- 연결 리스트가 배열보다 항상 빠른 것은 아니다. 캐시 지역성이 나빠 실제 성능이 불리할 수 있다.
- i번째 원소 접근은 O(1)이 아니다.
- 노드 삭제 시 이전 노드의 링크를 바꾸지 않으면 리스트가 끊기거나 삭제가 반영되지 않는다.
- 순환이 생기면 단순 순회가 끝나지 않을 수 있다.

## TMI

- Lisp라는 언어 이름은 "LISt Processor"에서 왔다. 리스트와 `cons` 셀은 초기 인공지능 연구와 함수형 프로그래밍 문화에서 매우 중요한 자료구조였다.
- 연결 리스트의 순환 여부를 찾는 대표 기법은 빠른 포인터와 느린 포인터를 함께 움직이는 Floyd cycle-finding algorithm이다.
- Linux 커널 코드에는 데이터 안에 링크 포인터를 직접 넣는 intrusive linked list 패턴이 널리 쓰인다. 자료구조가 노드를 감싸는 방식과 반대로, 사용자가 가진 구조체 안에 리스트 연결 정보가 들어간다.
- 면접에서는 연결 리스트가 자주 나오지만, 일반 애플리케이션 코드에서는 동적 배열, 해시 맵, 덱이 더 자주 쓰이는 편이다.

## 연습 / 확인 문제 (Exercises)

- 연결 리스트의 길이를 세는 함수를 작성하라.
- 연결 리스트를 뒤집는 함수를 작성하라.
- 두 포인터를 사용해 연결 리스트에 순환이 있는지 검사하라.

## 이어서 읽기 (Reading Path)

- 이전: [배열](Array.md)
- 다음: [스택](Stack.md)

## 참조 (References)

- [Data-Structures/Array.md](Array.md)
- [Programming/Functions-and-Recursion.md](../Programming/Functions-and-Recursion.md)
- [Reference/Books.md](../Reference/Books.md)
- [Reference/Courses.md](../Reference/Courses.md)
