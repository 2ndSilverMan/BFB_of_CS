# 분산 데이터베이스 (Distributed Databases)

- Level: Advanced
- Prerequisites: [NoSQL.md](NoSQL.md), [Systems/Distributed-Systems/Replication.md](../Distributed-Systems/Replication.md), [Systems/Distributed-Systems/Partitioning.md](../Distributed-Systems/Partitioning.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

분산 데이터베이스는 데이터를 여러 노드에 나누어 저장하고, 복제와 파티셔닝을 통해 확장성·가용성·내결함성을 제공하는 데이터베이스다. 핵심 문제는 데이터 일관성, 장애 처리, 질의 라우팅, 재분산이다.

## 직관 (Intuition)

한 창고에 모든 물건을 두면 찾기 쉽지만 창고가 터지면 끝이다. 여러 창고에 나누어 두면 규모와 가용성은 좋아지지만, 어느 창고에 무엇이 있는지, 복사본들이 같은지, 동시에 수정하면 어떻게 할지 관리해야 한다.

## 이론 (Theory)

분산 DB 설계의 주요 축은 다음과 같다.

- Partitioning/sharding: 데이터를 key range, hash, tenant 등 기준으로 나눈다.
- Replication: 같은 데이터를 여러 노드에 복제한다.
- Consistency: strong, eventual, causal, read-your-writes 등 모델을 선택한다.
- Transaction scope: 단일 파티션 트랜잭션인지, 다중 파티션 트랜잭션인지 구분한다.

CAP 정리는 네트워크 파티션 상황에서 consistency와 availability 사이 trade-off가 생긴다는 점을 강조한다. 실제 시스템은 PACELC처럼 평상시 latency와 consistency 사이의 선택도 함께 고려한다.

## 구현 (Implementation)

간단한 hash sharding은 key를 shard 수로 나누어 라우팅한다.

```python
def choose_shard(key, shard_count):
    return hash(key) % shard_count


for user_id in ["u1", "u2", "u3"]:
    print(user_id, choose_shard(user_id, 4))
```

실제 시스템은 consistent hashing, shard map, rebalancing, replica placement, failure detection을 함께 사용한다.

## 복잡도 (Complexity)

단일 key 조회는 shard routing 후 한 노드 또는 replica quorum 접근으로 처리할 수 있다. cross-shard query와 transaction은 네트워크 round trip과 coordination 비용이 커진다. rebalancing은 운영 중 성능과 안정성에 큰 영향을 준다.

## 응용 (Applications)

- 글로벌 사용자 데이터 저장
- 대규모 로그와 이벤트 저장
- 고가용성 OLTP 시스템
- multi-region read/write 서비스

## 흔한 오해 (Common Misunderstandings)

- 분산 DB가 단일 DB보다 항상 빠른 것은 아니다. coordination이 비싸다.
- replication은 backup과 다르다. 잘못된 삭제도 빠르게 복제될 수 있다.
- sharding key를 잘못 고르면 hot partition이 생긴다.
- eventual consistency를 쓰면 애플리케이션 로직이 더 단순해지는 것이 아니라 보상 로직이 필요할 수 있다.

## TMI

- quorum read/write는 $R+W>N$ 조건으로 최신성 가능성을 높인다.
- Spanner류 시스템은 시계 동기화와 consensus를 결합해 강한 트랜잭션 모델을 제공한다.
- 분산 DB의 어려움은 쿼리 엔진보다 장애 상황의 상태 전이에서 드러나는 경우가 많다.

## 연습 / 확인 문제 (Exercises)

- hash sharding과 range sharding의 장단점을 비교하라.
- replication factor가 3일 때 quorum read/write 예를 들어라.
- cross-shard transaction이 단일 shard transaction보다 어려운 이유를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [NoSQL](NoSQL.md)
- 다음: [Systems/Distributed-Systems/Distributed-Transactions.md](../Distributed-Systems/Distributed-Transactions.md)

## 참조 (References)

- [Systems/Distributed-Systems/Replication.md](../Distributed-Systems/Replication.md)
- [Systems/Distributed-Systems/Partitioning.md](../Distributed-Systems/Partitioning.md)
- [Systems/Distributed-Systems/CAP-Theorem.md](../Distributed-Systems/CAP-Theorem.md)
- [Reference/Books.md](../../Reference/Books.md)
