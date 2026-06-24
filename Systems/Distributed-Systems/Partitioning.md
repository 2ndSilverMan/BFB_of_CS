# 파티셔닝 (Partitioning / Sharding)

- Level: Intermediate
- Prerequisites: [Systems/Distributed-Systems/Replication.md](Replication.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

파티셔닝(샤딩)은 큰 데이터셋을 **여러 노드에 나눠 저장**해, 한 노드의 용량·처리량 한계를 넘어 수평 확장(scale-out)하는 기법이다. 각 데이터 조각(파티션/샤드)은 서로 다른 노드가 맡고, 보통 [복제](Replication.md)와 함께 쓰여 각 파티션도 여러 복제본을 둔다.

## 직관 (Intuition)

도서관 책이 한 서가에 다 안 들어가면 A–G, H–N, O–Z처럼 나눠 여러 서가에 둔다. 그러면 각 서가가 일부만 담당해 부담이 분산된다. 핵심 질문은 "어떤 기준으로 나눠야 한 서가에만 사람이 몰리지(핫스팟) 않을까"이다.

## 이론 (Theory)

파티션을 정하는 두 대표 방식이 있다.

| 방식 | 방법 | 장점 / 단점 |
|---|---|---|
| 키 범위(range) | 키 구간으로 분할(A–G, H–N…) | 범위 조회 효율적 / 핫스팟 위험(편향된 키) |
| 해시(hash) | 키의 해시로 분할 | 고른 분산 / 범위 조회 비효율 |

해시 파티셔닝은 고르게 분산되지만, 노드를 추가·제거할 때 거의 모든 키가 재배치되는 문제가 있다. 이를 **일관 해싱(consistent hashing)** 이 해결한다 — 노드와 키를 같은 해시 링 위에 놓아, 노드 변경 시 인접 구간의 키만 옮긴다.

핫스팟을 막기 위한 보조 기법도 있다 — 인기 키에 무작위 접두사를 붙이거나(salting), 가상 노드(virtual node)로 부하를 잘게 흩뿌린다.

보조 인덱스가 있으면 파티셔닝이 복잡해진다 — **로컬 인덱스**(각 파티션이 자기 데이터만 색인, 쓰기 빠름·읽기 시 모든 파티션 조회)와 **글로벌 인덱스**(인덱스 자체를 별도 파티셔닝, 읽기 빠름·쓰기 시 여러 파티션 갱신)의 트레이드오프가 있다.

## 구현 (Implementation)

해시 파티셔닝과 일관 해싱의 핵심 차이를 보인다.

```python
import hashlib

def h(key):
    return int(hashlib.md5(key.encode()).hexdigest(), 16)

# 단순 해시: 노드 수가 바뀌면 거의 모든 키가 재배치됨
def naive_partition(key, num_nodes):
    return h(key) % num_nodes

# 일관 해싱: 링 위에서 키보다 큰 첫 노드에 배정 → 변경 영향 최소
def consistent_partition(key, ring):       # ring: 정렬된 (해시, 노드) 목록
    point = h(key)
    for node_hash, node in ring:
        if point <= node_hash:
            return node
    return ring[0][1]                       # 링을 한 바퀴 돌면 첫 노드
```

## 복잡도 (Complexity)

| 항목 | 영향 |
|---|---|
| 균등 분산 실패 | 핫스팟 → 한 노드만 과부하 |
| 노드 추가/제거(단순 해시) | 거의 전체 키 재배치 — `O(n)` 이동 |
| 노드 추가/제거(일관 해싱) | 평균 `O(K/N)` 키만 이동 |
| 크로스 파티션 조인/트랜잭션 | 비싸짐(여러 노드 협력 필요) |

## 응용 (Applications)

- 대규모 데이터베이스 수평 확장(Cassandra, MongoDB, Vitess)
- 분산 캐시의 키 분배(memcached, Redis Cluster)
- 메시지 큐의 파티션(Kafka 토픽 파티션)
- 로드 밸런서의 요청 분배

## 흔한 오해 (Common Misunderstandings)

- 파티셔닝과 복제는 다른 개념이다. 파티셔닝은 데이터를 **나누고**, 복제는 **중복**한다. 보통 둘을 함께 쓴다.
- 해시 파티셔닝이 항상 좋은 건 아니다. 범위 조회(`BETWEEN`, 정렬)가 비효율적이다.
- 균등 해시도 핫스팟을 완전히 막지 못한다. 특정 키 하나에 트래픽이 몰리면(인기 사용자) 그 파티션이 과부하된다.
- 파티션을 가로지르는 트랜잭션·조인은 비싸다. 좋은 파티션 키 설계로 크로스 파티션 연산을 줄이는 것이 핵심이다.

## TMI

- 일관 해싱은 1997년 MIT에서 웹 캐시 부하 분산을 위해 고안됐고, 이후 Dynamo·Cassandra의 핵심 기술이 됐다.
- 가상 노드(virtual node)는 물리 노드 하나를 링 위 여러 지점에 배치해, 노드 간 부하를 더 고르게 만들고 장애 시 재분배를 매끄럽게 한다.
- "셀러브리티 문제(celebrity problem)": 팔로워가 수천만인 계정 하나가 특정 파티션을 마비시키는 핫스팟의 대표 사례다.

## 연습 / 확인 문제 (Exercises)

- 단순 해시(`% N`)에서 노드를 3개→4개로 늘릴 때 재배치되는 키 비율을 추정하라.
- 일관 해싱 링에 가상 노드를 도입하면 부하 분산이 왜 개선되는지 설명하라.
- 범위 파티셔닝이 핫스팟을 만드는 키 분포의 예를 하나 제시하라.

## 이어서 읽기 (Reading Path)

- 이전: [복제](Replication.md)
- 다음: [분산 트랜잭션](Distributed-Transactions.md), [사례 연구](Distributed-System-Case-Studies.md)
- 관련: [해시 함수](../../Data-Structures/Hash-Function.md)

## 참조 (References)

- [Systems/Distributed-Systems/Replication.md](Replication.md)
- [Data-Structures/Hash-Function.md](../../Data-Structures/Hash-Function.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Papers.md](../../Reference/Papers.md)
