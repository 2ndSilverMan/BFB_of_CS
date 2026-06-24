# 트라이 (Trie, Prefix Tree)

- Level: Intermediate
- Prerequisites: [Data-Structures/Binary-Tree.md](Binary-Tree.md), [Data-Structures/Hash-Table.md](Hash-Table.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

트라이는 문자열 집합을 공통 접두사를 공유하는 트리로 저장하는 자료구조다. 각 경로가 하나의 문자열을 나타내며, 접두사 탐색·자동완성·사전 검색에 특화돼 있다.

## 직관 (Intuition)

"car", "card", "care"는 모두 "car"로 시작한다. 트라이는 이 공통 접두사를 한 번만 저장하고 그 뒤만 가지를 친다. 그래서 "ca로 시작하는 단어"를 찾을 때 전체를 훑지 않고 해당 가지만 따라가면 된다. 문자열 길이에만 비례하는 탐색이 핵심 강점이다.

## 이론 (Theory)

루트에서 시작해 각 간선이 한 문자를 나타낸다. 노드는 자식 맵(배열 또는 해시)과 "여기서 단어가 끝남" 표시를 가진다. 길이 $m$ 문자열의 삽입·탐색은 $m$개 노드를 따라가 `O(m)`이며, 사전 크기 $n$과 무관하다.

변형:
- **압축 트라이(radix/Patricia)**: 외자식 경로를 하나로 합쳐 공간 절약.
- **접미사 트라이/트리**: 한 문자열의 모든 접미사 저장 → 부분문자열 검색.
- **DAWG**: 공통 접미사까지 공유해 더 압축.

## 구현 (Implementation)

```python
class Trie:
    def __init__(self):
        self.children = {}
        self.is_end = False

    def insert(self, word):
        node = self
        for ch in word:
            node = node.children.setdefault(ch, Trie())  # 없으면 새 노드
            node = node if False else node
        node.is_end = True

    def starts_with(self, prefix):
        node = self
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True            # 접두사 경로 존재
```

## 복잡도 (Complexity)

| 연산 | 시간 |
|---|---|
| 삽입 | `O(m)` |
| 탐색 | `O(m)` |
| 접두사 질의 | `O(m)` |

$m$은 문자열 길이. 공간은 최악의 경우 노드 수 × 알파벳 크기까지 커질 수 있어, 배열 자식은 빠르지만 메모리를 많이 쓰고 해시 자식은 그 반대다. 압축 트라이로 공간을 줄인다.

## 응용 (Applications)

- 자동완성·검색어 추천
- 사전·맞춤법 검사
- IP 라우팅 테이블(최장 접두사 매칭)
- 문자열 알고리즘(접미사 트리, Aho-Corasick)의 토대

## 흔한 오해 (Common Misunderstandings)

- 트라이 탐색은 사전 크기 $n$이 아니라 키 길이 $m$에 의존한다.
- 해시 테이블보다 항상 빠르지 않다. 접두사 질의가 필요 없으면 해시가 더 메모리 효율적일 수 있다.
- 노드마다 알파벳 크기 배열을 두면 메모리가 폭증한다(희소하면 맵 사용).
- "단어 끝" 표시가 없으면 접두사와 완전한 단어를 구분할 수 없다.

## TMI

- "trie"는 retrieval에서 따온 이름이며, 발음은 "트라이"가 흔하지만 "트리"라고도 한다.
- 라우터의 최장 접두사 매칭은 압축 트라이(또는 그 하드웨어 변형)로 초고속 패킷 포워딩을 한다.
- Aho-Corasick은 트라이에 실패 링크를 더해 여러 패턴을 한 번에 검색한다.

## 연습 / 확인 문제 (Exercises)

- "to", "tea", "ted", "ten"을 삽입한 트라이를 그려라.
- 트라이로 자동완성(주어진 접두사로 시작하는 모든 단어)을 구현하라.
- 같은 사전을 해시 셋과 트라이로 저장할 때의 장단점을 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [해시 테이블](Hash-Table.md)
- 다음: 문자열 매칭 (예정 `KMP.md`), 다중 패턴 매칭 (예정 `Aho-Corasick.md`)

## 참조 (References)

- [Data-Structures/Hash-Table.md](Hash-Table.md)
- [Data-Structures/Binary-Tree.md](Binary-Tree.md)
- [Reference/Books.md](../Reference/Books.md)
