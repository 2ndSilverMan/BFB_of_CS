# 해시 테이블 (Hash Table)

- Level: Beginner
- Prerequisites: [Data-Structures/Array.md](Array.md), [Data-Structures/Linked-List.md](Linked-List.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

해시 테이블은 키를 **평균 $O(1)$** 로 값에 대응시킨다. 키를 [해시 함수](Hash-Function.md)에 넣어 배열 인덱스(버킷)를 계산하고 그 자리에 저장한다. Python `dict`/`set`, Java `HashMap`이 대표 구현.

## 직관 (Intuition)

전화번호부를 처음부터 읽는 대신 "키 → 위치"를 *계산*해 바로 점프한다. 잘 만든 해시 함수가 키를 버킷에 고르게 흩뿌리면 어떤 키든 거의 한 번에 닿는다. 모든 어려움은 단 하나 — **충돌**(서로 다른 키가 같은 버킷)을 어떻게 다루느냐다.

## 이론 (Theory)

### 1. 충돌은 불가피 — 두 전략

키 공간 > 버킷 수이므로 비둘기집 원리상 충돌은 피할 수 없다.

| 전략 | 방법 | 부하율 | 특징 |
|---|---|---|---|
| 체이닝(chaining) | 버킷마다 리스트/동적 배열 | $\alpha>1$ 허용 | 단순, 삭제 쉬움, 포인터 오버헤드 |
| 개방 주소법(open addressing) | 충돌 시 정해진 규칙으로 다른 빈 칸 탐사 | $\alpha<1$ 필수 | 캐시 친화, 삭제는 tombstone 필요 |

개방 주소법의 탐사(probe) 방식:

- **선형 탐사**: `+1, +2, …` → primary clustering(덩어리짐).
- **이차 탐사**: `+1², +2², …` → secondary clustering 완화.
- **이중 해싱**: 보폭을 두 번째 해시로 → 군집 최소.

### 2. 부하율과 기대 탐사 횟수

성능은 **부하율** $\alpha=n/m$ 가 좌우한다. 균등 해싱 가정에서:

- **체이닝**: 평균 탐사 $\approx 1+\alpha$ → $\alpha$ 상수면 $O(1)$.
- **개방 주소법(랜덤 탐사 모델)**: 실패 탐색 $\approx \dfrac{1}{1-\alpha}$, 성공 $\approx \dfrac{1}{\alpha}\ln\dfrac{1}{1-\alpha}$.

$\alpha\to1$ 에서 개방 주소법은 폭발($\alpha=0.9$ 면 실패 탐색이 평균 10회) → 보통 **0.7 근처에서 리해싱**. 리해싱은 버킷을 2배로 늘려 전체 재배치($O(n)$)하지만, 기하급수 확장이라 **삽입당 amortized $O(1)$**.

### 3. 진보된 변형

Robin Hood(탐사 거리 균등화), **Cuckoo 해싱**(두 해시·최악 조회 $O(1)$), hopscotch. Java `HashMap`은 한 버킷 체인이 8을 넘으면 **레드-블랙 트리로 변환(treeify)** 해 최악을 $O(\log n)$ 으로 낮춘다.

## 구현 (Implementation)

체이닝 최소 구현:

```python
class HashTable:
    def __init__(self, capacity=8):
        self.buckets = [[] for _ in range(capacity)]
        self.n = 0

    def _idx(self, key):
        return hash(key) % len(self.buckets)

    def put(self, key, value):
        b = self.buckets[self._idx(key)]
        for i, (k, _) in enumerate(b):
            if k == key:
                b[i] = (key, value); return     # 갱신
        b.append((key, value)); self.n += 1
        if self.n / len(self.buckets) > 0.75:   # 부하율 임계 → 리해싱
            self._rehash()

    def get(self, key):
        for k, v in self.buckets[self._idx(key)]:
            if k == key:
                return v
        raise KeyError(key)

    def _rehash(self):
        old = [kv for b in self.buckets for kv in b]
        self.buckets = [[] for _ in range(2 * len(self.buckets))]
        self.n = 0
        for k, v in old:
            self.put(k, v)
```

## 복잡도 (Complexity)

| 연산 | 평균 | 최악 |
|---|---|---|
| 탐색/삽입/삭제 | $O(1)$ | $O(n)$ (체인 몰림), treeify면 $O(\log n)$ |
| 리해싱 | amortized $O(1)$/삽입 | $O(n)$ 순간 |

공간 $O(n+m)$. **워크드 예제(부하율).** 버킷 8개에 6개 삽입 → $\alpha=0.75$ 임계 → 16개로 리해싱, $\alpha=0.375$. 균등 해싱이면 체이닝 평균 탐사 $1+\alpha\approx1.4$ 로 유지. 최악은 모든 키가 한 버킷에 몰릴 때(나쁜 해시 또는 적대적 입력) $O(n)$.

## 응용 (Applications)

- 사전·집합(`dict`, `set`), 빈도 세기·중복 제거·그룹화.
- 캐시·메모이제이션 저장소, DB 인덱스·심볼 테이블.
- 조인(hash join), 집합 연산(교집합/차집합).

## 흔한 오해 (Common Misunderstandings)

- **$O(1)$ 은 평균** — 최악은 $O(n)$, 나쁜 해시·적대적 입력에서 실제로 발생.
- **키는 hashable(보통 immutable)** 이어야 한다 — 가변 객체를 키로 쓰면 위치가 어긋난다.
- **정렬을 보장하지 않는다** — Python `dict`의 삽입 순서 보존은 "정렬"이 아니다.
- **부하율을 무시하면 안 된다** — 리해싱 없이 넣기만 하면 충돌 누적으로 $O(1)$ 이 깨진다.
- **개방 주소법 삭제는 그냥 비우면 안 된다** — 탐사 사슬이 끊겨, tombstone(삭제 표식)이 필요하다.

## TMI

- 한 번의 리해싱은 $O(n)$ 이지만 2배 확장이라 amortized 삽입은 $O(1)$ — [동적 배열](Array.md) 분석과 같은 논리.
- 많은 런타임이 **HashDoS**(충돌을 악용한 DoS)를 막으려 실행마다 해시에 무작위 시드를 섞는다 → `hash("같은 문자열")` 이 실행마다 달라질 수 있다.
- **생일 문제**가 알려주듯 버킷이 많아도 충돌은 의외로 빨리 생긴다($\sqrt m$ 개만 넣어도) — 충돌 처리가 필수인 이유.
- C++ `std::unordered_map`은 표준이 체이닝을 사실상 강제(버킷 인터페이스·참조 안정성 때문)해, 개방 주소법 구현보다 느린 편이다.

## 연습 / 확인 문제 (Exercises)

- 위 `HashTable`에 `remove(key)` 를 추가하라(체이닝).
- 개방 주소법(선형 탐사)으로 같은 인터페이스를 구현하고 삭제 시 tombstone을 다뤄라.
- 두 리스트의 공통 원소를 평균 $O(n)$ 에 찾는 함수를 해시 셋으로 작성하라.
- $\alpha=0.5, 0.7, 0.9$ 에서 개방 주소법 실패 탐색 기대 횟수 $\frac{1}{1-\alpha}$ 를 계산하고 리해싱 임계의 근거를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [배열](Array.md)
- 다음: [해시 함수와 충돌 처리](Hash-Function.md)
- 관련: [트라이](Trie.md), [연결 리스트](Linked-List.md)

## 참조 (References)

- [Data-Structures/Array.md](Array.md)
- [Data-Structures/Linked-List.md](Linked-List.md)
- [Reference/Books.md](../Reference/Books.md)
- [Reference/Courses.md](../Reference/Courses.md)
