# 복제 (Replication)

- Level: Intermediate
- Prerequisites: [Systems/Distributed-Systems/CAP-Theorem.md](CAP-Theorem.md), [Systems/Databases/Transactions-and-ACID.md](../Databases/Transactions-and-ACID.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

복제는 같은 데이터를 **여러 노드에 중복 저장**해 가용성·내결함성·읽기 처리량을 높이는 기법이다. 한 노드가 죽어도 다른 복제본이 서비스를 이어 가고, 읽기를 여러 복제본에 분산할 수 있다. 대신 복제본 사이의 **일관성을 어떻게 유지하느냐**가 핵심 과제다.

## 직관 (Intuition)

중요한 문서를 한 곳에만 두면 그 서버가 고장 났을 때 끝이다. 여러 곳에 복사본을 두면 안전하지만, 한 곳에서 문서를 고쳤을 때 나머지 복사본에 그 변경을 어떻게·언제 전파할지가 문제다. 즉시 모두 맞추면 느리고, 나중에 맞추면 잠깐 서로 다른 값을 보게 된다.

## 이론 (Theory)

복제 구조는 쓰기를 누가 받느냐로 나뉜다.

| 구조 | 방식 | 특징 |
|---|---|---|
| 단일 리더(single-leader) | 쓰기는 리더만, 팔로워는 복제본 읽기 | 단순, 일관성 쉬움, 리더가 병목/단일 장애점 |
| 다중 리더(multi-leader) | 여러 리더가 쓰기 수용 | 지역 분산에 유리, 쓰기 충돌 해결 필요 |
| 리더리스(leaderless) | 아무 노드나 쓰기, 쿼럼으로 조율 | 고가용성, 클라이언트가 충돌 처리(Dynamo 스타일) |

전파 시점에 따라 **동기 복제**(리더가 팔로워 확인까지 대기 — 안전하지만 느림)와 **비동기 복제**(리더가 즉시 응답, 나중 전파 — 빠르지만 리더 장애 시 데이터 손실 가능)로 나뉜다. 많은 시스템이 일부는 동기, 나머지는 비동기로 두는 **준동기(semi-synchronous)** 를 택한다.

리더리스에서는 [CAP의 쿼럼](CAP-Theorem.md) 규칙 $W + R > N$으로 일관성을 조절하고, 뒤처진 복제본은 **읽기 복구(read repair)** 와 **안티 엔트로피(anti-entropy)** 로 따라잡는다.

## 구현 (Implementation)

리더리스 쿼럼 쓰기/읽기를 단순화한 모델이다.

```python
N, W, R = 3, 2, 2          # W + R > N 이면 강한 일관성

replicas = [None] * N

def write(value, version):
    acks = 0
    for i in range(N):
        replicas[i] = (value, version)   # 실제로는 일부만 즉시 성공할 수 있음
        acks += 1
        if acks >= W:                    # W개 응답이면 쓰기 성공 처리
            return True
    return False

def read():
    responses = [replicas[i] for i in range(R)]      # R개에서 읽음
    return max(responses, key=lambda x: x[1])        # 최신 버전 채택
```

## 복잡도 (Complexity)

| 선택 | 장점 | 대가 |
|---|---|---|
| 동기 복제 | 데이터 손실 없음 | 쓰기 지연 증가, 팔로워 장애 시 차단 |
| 비동기 복제 | 빠른 쓰기 | 리더 장애 시 미전파분 손실 |
| 복제본 수 ↑ | 가용성·읽기 처리량↑ | 쓰기 전파 비용·저장 공간↑ |

## 응용 (Applications)

- 데이터베이스 읽기 확장(읽기 복제본)
- 고가용성: 리더 장애 시 팔로워 승격(failover)
- 지역 분산(multi-region)으로 사용자 근접 읽기
- CDN·캐시의 콘텐츠 복제

## 흔한 오해 (Common Misunderstandings)

- 비동기 복제에서 "쓰기 성공" 응답을 받아도 데이터가 안전하다는 보장은 없다. 리더가 전파 전에 죽으면 손실될 수 있다.
- 읽기 복제본에서 읽으면 방금 쓴 값을 못 볼 수 있다(복제 지연). "자신이 쓴 것 읽기(read-your-writes)" 같은 보장은 따로 설계해야 한다.
- 복제는 백업이 아니다. 잘못된 삭제·손상도 그대로 복제되므로, 시점 복구용 백업은 별도로 필요하다.
- 복제본을 늘리면 읽기는 빨라지지만 쓰기는 더 느려질 수 있다(전파 부담).

## TMI

- 복제 지연이 사용자에게 드러나는 고전적 예: 댓글을 달자마자 새로고침했는데 자기 댓글이 안 보이는 현상(리더에 썼지만 팔로워에서 읽음).
- 다중 리더의 쓰기 충돌 해결로 CRDT(충돌 없는 복제 자료형)나 "마지막 쓰기 승리(LWW)"가 쓰이는데, LWW는 시계 오차 때문에 쓰기가 조용히 사라질 수 있다.
- Dynamo 논문(2007)의 리더리스 + 쿼럼 + 읽기 복구 설계는 Cassandra, Riak, Voldemort 등 여러 시스템의 청사진이 됐다.

## 연습 / 확인 문제 (Exercises)

- `N=3`에서 `(W=1, R=1)`과 `(W=2, R=2)`의 일관성·가용성 차이를 설명하라.
- 단일 리더에서 리더가 죽었을 때 팔로워 승격 과정에서 생길 수 있는 데이터 손실 시나리오를 들어라.
- "자신이 쓴 것 읽기" 보장을 단일 리더 복제 위에서 구현하는 방법을 제안하라.

## 이어서 읽기 (Reading Path)

- 이전: [CAP 정리와 PACELC](CAP-Theorem.md)
- 다음: [파티셔닝](Partitioning.md)
- 관련: [분산 합의](Consensus.md)

## 참조 (References)

- [Systems/Distributed-Systems/CAP-Theorem.md](CAP-Theorem.md)
- [Systems/Databases/Transactions-and-ACID.md](../Databases/Transactions-and-ACID.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Papers.md](../../Reference/Papers.md)
