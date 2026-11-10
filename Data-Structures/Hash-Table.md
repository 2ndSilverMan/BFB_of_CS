# 해시 테이블 (Hash Table)

- Level: Beginner
- Prerequisites: [Data-Structures/Array.md](Array.md), [Data-Structures/Linked-List.md](Linked-List.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

해시 테이블은 해시·동등성 비교 비용이 상수이고 키가 충분히 고르게 분산되며 부하율을 관리할 때 **기대 $O(1)$** 조회를 제공한다. 키를 [해시 함수](Hash-Function.md)에 넣어 배열 인덱스(버킷)를 계산하고 그 자리에 저장한다. Python `dict`/`set`, Java `HashMap`이 대표 구현이다.

## 직관 (Intuition)

전화번호부를 처음부터 읽는 대신 "키 → 위치"를 *계산*해 바로 점프한다. 잘 만든 해시 함수가 키를 버킷에 고르게 흩뿌리면 어떤 키든 거의 한 번에 닿는다. 모든 어려움은 단 하나 — **충돌**(서로 다른 키가 같은 버킷)을 어떻게 다루느냐다.

## 이론 (Theory)

### 1. 충돌은 불가피 — 두 전략

키 공간 > 버킷 수이므로 비둘기집 원리상 충돌은 피할 수 없다.

| 전략 | 방법 | 부하율 | 특징 |
|---|---|---|---|
| 체이닝(chaining) | 버킷마다 리스트/동적 배열 | $\alpha>1$ 허용 | 단순, 삭제 쉬움, 포인터 오버헤드 |
| 개방 주소법(open addressing) | 충돌 시 정해진 규칙으로 다른 빈 칸 탐사 | 일반적으로 $\alpha<1$ 유지 | 캐시 친화, 삭제 후 탐사 경로 보존 필요 |

개방 주소법의 탐사(probe) 방식:

- **선형 탐사**: `+1, +2, …` → primary clustering(덩어리짐).
- **이차 탐사**: 초기 위치에서 `+1², +2², …`만큼 이동 → 연속 구간에 뭉치는 primary clustering을 줄이지만, 초기 위치가 같은 키는 여전히 같은 탐사열을 따르는 secondary clustering이 남는다. 테이블 크기와 계수에 따라 모든 칸을 방문하지 못할 수도 있다. ([Virginia Tech 이차 탐사 설명](https://research.cs.vt.edu/AVresearch/hashing/quadratic.php))
- **이중 해싱**: 보폭을 두 번째 해시로 결정해 키별 탐사열을 더 다양하게 만든다. 모든 칸을 방문하려면 보폭과 테이블 크기가 서로소여야 한다.

### 2. 부하율과 기대 탐사 횟수

성능은 **부하율** $\alpha=n/m$와 충돌 분포에 영향을 받는다. 해시 계산·키 비교를 상수 시간으로 가정하면:

- **체이닝**: 단순 균등 해싱에서 탐색 기대 시간은 $\Theta(1+\alpha)$이므로 $\alpha$가 상수면 $O(1)$이다. $1+\alpha$를 모든 검색의 정확한 비교 횟수로 읽으면 안 된다.
- **개방 주소법(균등한 무작위 탐사열 모델)**: 삭제가 없고 $\alpha<1$이면 실패 탐색의 기대 탐사 횟수는 최대 $\dfrac{1}{1-\alpha}$다. 저장된 키를 같은 확률로 찾는 성공 탐색은 최대 $\dfrac{1}{\alpha}\ln\dfrac{1}{1-\alpha}$다. 이는 해당 가정 아래의 상한이며, 선형 탐사나 tombstone이 쌓인 테이블의 실측값이 아니다. ([Stanford CS161, §1.1·§3.2](https://web.stanford.edu/class/archive/cs/cs161/cs161.1168/lecture9.pdf))

$\alpha=0.9$를 위 실패 탐색 상한에 대입하면 10회다. 임계값은 충돌 처리·삭제 방식과 메모리 목표에 따라 선택하며, 모든 해시 테이블에 공통인 0.7 기준은 없다. 아래 체이닝 예제는 0.75를 **초과할 때** 두 배로 확장한다. 리해싱 비용을 분산한 삽입당 추가 비용은 amortized $O(1)$이지만, 충돌이 심할 때의 키 탐색 비용까지 사라지는 것은 아니다.

### 3. 진보된 변형

Robin Hood(탐사 거리 균등화), **Cuckoo 해싱**(두 해시·최악 조회 $O(1)$), hopscotch 같은 변형이 있다. OpenJDK `jdk-21+35`의 `HashMap`은 `TREEIFY_THRESHOLD=8`, `MIN_TREEIFY_CAPACITY=64`를 둔다. 충돌 버킷의 트리화 조건에 도달해도 전체 테이블 용량이 64보다 작으면 먼저 확장한다. 트리화가 곧 모든 키에 대한 최악 $O(\log n)$ 보장이라는 뜻도 아니다. 구현 주석의 로그 시간 설명은 서로 다른 해시값이나 비교 가능한 키처럼 트리에서 탐색 방향을 정할 수 있는 경우를 전제로 한다. ([해당 버전의 `HashMap` 구현·`treeifyBin`](https://raw.githubusercontent.com/openjdk/jdk/jdk-21%2B35/src/java.base/share/classes/java/util/HashMap.java))

## 구현 (Implementation)

체이닝 최소 구현이다. Python 3 표준 기능만 사용하며 삭제·동시 접근은 구현하지 않는다. 기존 키의 값을 갱신할 때는 원소 수를 늘리지 않고, 리해싱은 이미 중복이 없는 항목을 새 버킷에 직접 배치한다.

```python
class HashTable:
    def __init__(self, capacity=8):
        if type(capacity) is not int or capacity <= 0:
            raise ValueError("capacity must be a positive integer")
        self.buckets = [[] for _ in range(capacity)]
        self.n = 0

    def _idx(self, key):
        return hash(key) % len(self.buckets)

    def put(self, key, value):
        b = self.buckets[self._idx(key)]
        for i, (k, _) in enumerate(b):
            if k == key:
                b[i] = (key, value)
                return                       # 갱신은 원소 수 유지
        b.append((key, value))
        self.n += 1
        if self.n / len(self.buckets) > 0.75:  # 0.75와 같을 때는 유지
            self._rehash()

    def get(self, key):
        for k, v in self.buckets[self._idx(key)]:
            if k == key:
                return v
        raise KeyError(key)

    def _rehash(self):
        old_buckets = self.buckets
        self.buckets = [[] for _ in range(2 * len(old_buckets))]
        for bucket in old_buckets:
            for key, value in bucket:
                self.buckets[self._idx(key)].append((key, value))
```

### 부하율 경계와 충돌 확인

버킷 8개에서 서로 다른 키 6개를 넣으면 $6/8=0.75$이므로 그대로다. 기존 키의 값을 바꿔도 원소 수는 6이다. 일곱 번째 키를 추가하면 $7/8=0.875$로 임계값을 초과해 16버킷으로 확장하고, 최종 부하율은 $7/16=0.4375$다.

다음 블록을 클래스 정의 뒤에 이어서 실행한다. 출력은 차례로 `6 8`, `7 16`, `hash table checks passed`다.

```python
table = HashTable()
for key in range(6):
    table.put(key, key * 10)
assert (table.n, len(table.buckets)) == (6, 8)
print(table.n, len(table.buckets))

table.put(2, 200)
assert table.get(2) == 200
assert (table.n, len(table.buckets)) == (6, 8)
table.put(6, 60)
assert (table.n, len(table.buckets)) == (7, 16)
assert [table.get(key) for key in range(7)] == [0, 10, 200, 30, 40, 50, 60]
print(table.n, len(table.buckets))

# 이 입력의 키들은 초기 8버킷에서 같은 버킷에 들어간다.
collisions = HashTable()
collision_keys = [0, 8, 16]
assert len({collisions._idx(key) for key in collision_keys}) == 1
for key in collision_keys:
    collisions.put(key, str(key))
assert [collisions.get(key) for key in collision_keys] == ["0", "8", "16"]
try:
    collisions.get(24)
except KeyError:
    pass
else:
    raise AssertionError("missing key was accepted")

try:
    HashTable(0)
except ValueError:
    pass
else:
    raise AssertionError("zero capacity was accepted")
print("hash table checks passed")
```

## 복잡도 (Complexity)

아래는 위 체이닝 코드의 비용이며 해시 계산·동등성 비교를 $O(1)$로 가정한다.

| 연산 | 기대 또는 분할 상환 비용 | 최악 |
|---|---|---|
| 조회·기존 키 갱신 | 균등 해싱·상수 부하율에서 $O(1)$ | $O(n)$, 하나의 체인에 몰릴 때 |
| 새 키 삽입 | 같은 가정에서 리해싱 포함 expected amortized $O(1)$ | $O(n)$, 충돌 탐색 또는 리해싱 |
| 리해싱만 | 여러 삽입에 분산하면 amortized $O(1)$/삽입 | $O(n+m)$, 자동 확장 시점에는 $m=\Theta(n)$ |

공간은 $O(n+m)$이다. `_rehash`는 새 버킷 초기화와 각 항목의 이동만 수행한다. 여기에 중복 검사까지 하는 `put`을 다시 호출하면 충돌한 키들을 반복 탐색해 불필요한 비용을 만들 수 있다. 긴 문자열의 해시 계산이나 사용자 정의 동등성 비교 비용이 크면 위 상수 시간 가정도 별도로 수정해야 한다.

## 응용 (Applications)

- 사전·집합(`dict`, `set`), 빈도 세기·중복 제거·그룹화.
- 캐시·메모이제이션 저장소, DB 인덱스·심볼 테이블.
- 조인(hash join), 집합 연산(교집합/차집합).

## 흔한 오해 (Common Misunderstandings)

- **$O(1)$ 은 평균** — 최악은 $O(n)$, 나쁜 해시·적대적 입력에서 실제로 발생.
- **키는 hashable이어야 한다** — 저장 중 해시값과 동등성 관계가 안정적이어야 하고, 같은 것으로 비교되는 키는 같은 해시값을 가져야 한다. 객체에 가변 필드가 있다는 이유만으로 항상 사용할 수 없는 것은 아니다. Python의 사용자 정의 객체는 기본적으로 식별성에 기반한 해시와 비교를 사용한다. ([Python `hashable` 정의](https://docs.python.org/3/glossary.html#term-hashable))
- **정렬을 보장하지 않는다** — Python `dict`의 삽입 순서 보존은 "정렬"이 아니다.
- **부하율을 무시하면 안 된다** — 리해싱 없이 넣기만 하면 충돌 누적으로 $O(1)$ 이 깨진다.
- **개방 주소법 삭제 후 탐사 경로를 보존해야 한다** — 빈 칸을 만나면 탐색을 종료하는 방식에서 중간 칸만 비우면 뒤의 키를 놓친다. tombstone은 한 해결책이고, 선형 탐사에서는 같은 군집의 키들을 다시 삽입하는 방법도 있다. [Sedgewick·Wayne의 `LinearProbingHashST.delete`](https://algs4.cs.princeton.edu/34hash/LinearProbingHashST.java.html)는 후자를 보여 준다. 삭제 전략은 탐사 방식에 맞춰 선택해야 한다.

## TMI

- 두 배 확장의 이동 비용을 여러 삽입에 나누는 논리는 [동적 배열](Array.md)과 같다. 다만 해시 테이블의 충돌 탐색은 별도 분석 대상이다.
- 많은 런타임이 **HashDoS**(충돌을 악용한 DoS)를 막으려 실행마다 해시에 무작위 시드를 섞는다 → `hash("같은 문자열")` 이 실행마다 달라질 수 있다.
- **생일 문제**가 알려주듯 버킷이 많아도 충돌은 의외로 빨리 생긴다($\sqrt m$ 개만 넣어도) — 충돌 처리가 필수인 이유.
- 실제 구현의 속도를 비교할 때는 부하율·키 크기·해시 함수·삭제 비율·참조 안정성 요구를 함께 기록해야 한다. 체이닝과 개방 주소법이라는 분류만으로 일률적인 속도 순서를 정할 수는 없다.

## 연습 / 확인 문제 (Exercises)

- 위 `HashTable`에 `remove(key)` 를 추가하라(체이닝).
- 개방 주소법(선형 탐사)으로 같은 인터페이스를 구현하고 삭제 시 tombstone을 다뤄라.
- 두 리스트의 공통 원소를 평균 $O(n)$ 에 찾는 함수를 해시 셋으로 작성하라.
- $\alpha=0.5, 0.7, 0.9$에서 균등한 무작위 탐사열 모델의 실패 탐색 기대 횟수 **상한** $\frac{1}{1-\alpha}$를 계산하고, 이것이 선형 탐사의 실측값과 같다고 보장할 수 없는 이유를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [배열](Array.md)
- 다음: [해시 함수와 충돌 처리](Hash-Function.md)
- 관련: [트라이](Trie.md), [연결 리스트](Linked-List.md)

## 참조 (References)

- [Stanford CS161 — Lecture 9: Hashing, Jessica Su](https://web.stanford.edu/class/archive/cs/cs161/cs161.1168/lecture9.pdf): §1.1의 체이닝 기대 비용, §3.1.3의 이중 해싱 보폭 조건, §3.2의 삭제 없는 균등 탐사열 가정과 성공·실패 탐색 상한.
- [Virginia Tech — Hashing Tutorial, §6.3 Quadratic Probing](https://research.cs.vt.edu/AVresearch/hashing/quadratic.php): 이차 탐사열의 정의와 일부 칸을 방문하지 못하는 사례. 동일 초기 위치의 키가 같은 탐사열을 갖는다는 설명은 그 식에서 따른다.
- [OpenJDK `jdk-21+35` — `HashMap.java`](https://raw.githubusercontent.com/openjdk/jdk/jdk-21%2B35/src/java.base/share/classes/java/util/HashMap.java): `TREEIFY_THRESHOLD`, `MIN_TREEIFY_CAPACITY`, `treeifyBin`과 트리 버킷의 로그 시간 전제. 특정 버전의 구현이며 Java API 전체의 성능 보장으로 일반화하지 않는다.
- [Sedgewick·Wayne — `LinearProbingHashST.java`](https://algs4.cs.princeton.edu/34hash/LinearProbingHashST.java.html): `delete`의 군집 재삽입 방식. tombstone이 삭제의 유일한 방법이 아님을 보여 주는 저자 공개 코드.
- [Python — Glossary, hashable](https://docs.python.org/3/glossary.html#term-hashable): 해시값의 안정성, 동등한 객체의 해시 계약과 사용자 정의 객체의 기본 동작.
- [Data-Structures/Array.md](Array.md)
- [Data-Structures/Linked-List.md](Linked-List.md)
- [Reference/Books.md](../Reference/Books.md)
- [Reference/Courses.md](../Reference/Courses.md)

## 재작성 메모 (Rewrite Notes)

- 재사용할 재료: 충돌 전략 비교, 가정을 적은 기대 탐사 상한, 체이닝 구현, 8버킷에서 6개 유지·7개 확장 경계와 갱신·충돌·미존재 조회 assert.
- 보충할 내용: tombstone과 군집 재삽입의 삭제 trace 비교, 반복 삭제 후 부하율과 탐사 횟수 측정, Cuckoo·Robin Hood의 원문 및 실패 조건, 키 해시·비교 비용을 포함한 실제 워크로드 벤치마크.
- 확인 상태: 2026-09-16 위 5개 직접 출처에서 참조에 적은 절·상수·삭제 방식·해시 계약을 확인했다. Python 3.12.10에서 본문 코드 블록 2개를 순서대로 실행해 부하율 경계·갱신·리해싱 후 조회·충돌·미존재 키·0용량 거부 assert가 통과했고 예상 출력과 일치했다. OpenJDK 코드는 읽었지만 Java의 트리화 동작을 실행하지 않았다.
