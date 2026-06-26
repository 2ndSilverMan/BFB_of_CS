# 해시 테이블 (Hash Table)

- Level: Beginner
- Prerequisites: [Data-Structures/Array.md](Array.md), [Data-Structures/Linked-List.md](Linked-List.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

해시 테이블은 **키(key)를 값(value)에 평균 `O(1)`로 대응**시키는 자료구조다. 키를 해시 함수에 넣어 배열의 인덱스(버킷)를 계산하고, 그 자리에 값을 저장한다. Python의 `dict`, `set`이 대표적인 구현이다.

## 직관 (Intuition)

이름으로 전화번호를 찾을 때, 책 전체를 처음부터 읽는 대신 "ㄱ으로 시작하면 몇 쪽"처럼 바로 위치를 계산할 수 있다면 훨씬 빠르다. 해시 함수가 바로 그 "키 → 위치" 계산기다. 잘 만든 해시 함수는 키들을 버킷에 고르게 흩뿌려, 어떤 키든 거의 한 번에 찾게 해 준다.

## 이론 (Theory)

핵심은 해시 함수 $h(\text{key}) \rightarrow [0, m)$ 와 **충돌(collision)** 처리다. 서로 다른 키가 같은 버킷으로 가는 충돌은 비둘기집 원리상 피할 수 없다. 두 가지 대표 전략이 있다.

| 전략 | 방법 |
|---|---|
| 체이닝(chaining) | 각 버킷에 연결 리스트(또는 동적 배열)를 두고 충돌한 항목을 이어 붙임 |
| 개방 주소법(open addressing) | 충돌 시 정해진 규칙(선형·이차 탐사 등)으로 다른 빈 버킷을 찾아감 |

성능은 **부하율(load factor)** $\alpha = n/m$(항목 수 / 버킷 수)에 좌우된다. $\alpha$가 커지면 충돌이 늘어 느려지므로, 보통 임계치를 넘으면 버킷을 늘리고 전체를 다시 배치하는 **리해싱(rehashing)** 을 한다. 균등 해싱 가정에서 한 연산의 평균 비용은 $O(1 + \alpha)$이고, $\alpha$를 상수로 유지하면 평균 `O(1)`이다.

## 구현 (Implementation)

체이닝 방식의 최소 구현이다.

```python
class HashTable:
    def __init__(self, capacity=8):
        self.buckets = [[] for _ in range(capacity)]

    def _index(self, key):
        return hash(key) % len(self.buckets)

    def put(self, key, value):
        bucket = self.buckets[self._index(key)]
        for i, (k, _) in enumerate(bucket):
            if k == key:
                bucket[i] = (key, value)   # 갱신
                return
        bucket.append((key, value))        # 새 키

    def get(self, key):
        for k, v in self.buckets[self._index(key)]:
            if k == key:
                return v
        raise KeyError(key)


table = HashTable()
table.put("apple", 3)
print(table.get("apple"))   # 3
```

실무에서는 직접 구현하기보다 언어의 `dict`/`set`을 쓴다.

```python
counts = {}
for word in ["a", "b", "a"]:
    counts[word] = counts.get(word, 0) + 1
print(counts)   # {'a': 2, 'b': 1}
```

## 복잡도 (Complexity)

| 연산 | 평균 | 최악 |
|---|---|---|
| 탐색 | `O(1)` | `O(n)` |
| 삽입 | `O(1)` | `O(n)` |
| 삭제 | `O(1)` | `O(n)` |

최악의 경우는 모든 키가 한 버킷에 몰릴 때다(나쁜 해시 함수나 의도적 공격). 공간은 `O(n + m)`이다.

## 응용 (Applications)

- 사전·집합 자료형(`dict`, `set`)
- 빈도 세기, 중복 제거, 그룹화
- 캐시·메모이제이션의 저장소
- 데이터베이스 인덱스, 심볼 테이블

## 흔한 오해 (Common Misunderstandings)

- `O(1)`은 **평균**이다. 최악은 `O(n)`이며, 나쁜 해시나 적대적 입력에서 실제로 나타날 수 있다.
- 모든 값을 키로 쓸 수 있는 것은 아니다. 키는 해시 가능(hashable)해야 하며, 보통 불변(immutable) 객체여야 한다.
- 해시 테이블은 기본적으로 정렬을 보장하지 않는다. (Python `dict`는 3.7+부터 **삽입 순서**를 보존하지만, 이는 "정렬"이 아니다.)
- 부하율을 무시하면 안 된다. 리해싱 없이 항목만 계속 넣으면 충돌이 누적돼 `O(1)`이 깨진다.

## TMI

- 한 번의 리해싱은 `O(n)`이지만, 버킷을 2배씩 키우면 분할 상환(amortized) 비용은 삽입당 `O(1)`로 유지된다.
- 많은 언어 런타임은 해시 충돌을 악용한 DoS(HashDoS)를 막기 위해 실행마다 해시에 무작위 시드를 섞는다. 그래서 `hash("같은 문자열")` 값이 실행마다 달라질 수 있다.
- "생일 문제"가 알려주듯, 버킷이 많아도 충돌은 생각보다 빨리 발생한다. 충돌 처리가 선택이 아니라 필수인 이유다.

## 연습 / 확인 문제 (Exercises)

- 위 `HashTable`에 `remove(key)`와 부하율 기반 리해싱을 추가하라.
- 두 리스트에서 공통 원소를 `O(n)` 평균 시간에 찾는 함수를 해시 집합으로 작성하라.
- 개방 주소법(선형 탐사)으로 같은 인터페이스를 구현하고 체이닝과 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [배열](Array.md)
- 다음: [해시 함수와 충돌 처리](Hash-Function.md)
- 관련: [트라이](Trie.md)

## 참조 (References)

- [Data-Structures/Array.md](Array.md)
- [Data-Structures/Linked-List.md](Linked-List.md)
- [Reference/Books.md](../Reference/Books.md)
- [Reference/Courses.md](../Reference/Courses.md)
