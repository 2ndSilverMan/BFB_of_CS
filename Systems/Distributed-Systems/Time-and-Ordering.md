# 시간과 순서: 논리적 시계와 벡터 시계

- Level: Advanced
- Prerequisites: [System-Models.md](System-Models.md), [Replication.md](Replication.md), [Consensus.md](Consensus.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

분산 시스템에서 시간과 순서는 여러 노드에서 발생한 이벤트의 전후 관계를 판단하는 문제다. 물리 시계는 완벽히 동기화되지 않으므로, 논리적 시계와 벡터 시계가 causal ordering을 표현하는 데 사용된다.

## 직관 (Intuition)

서로 다른 도시의 사람들이 각자 시계를 보고 일을 기록하면, 시계 오차 때문에 실제 순서를 헷갈릴 수 있다. 분산 시스템도 마찬가지다. 메시지를 주고받은 관계를 이용해 “이 일은 저 일보다 먼저 영향을 줄 수 있었다”를 추적한다.

## 이론 (Theory)

Lamport의 happened-before 관계는 다음으로 정의된다.

- 같은 프로세스 안에서 앞선 이벤트는 뒤 이벤트보다 먼저 발생했다.
- 메시지 send는 해당 receive보다 먼저 발생했다.
- 관계는 transitive하다.

Lamport clock은 이벤트마다 counter를 증가시키고, 메시지에 clock을 실어 보내 receive 시 더 큰 값으로 갱신한다. 이는 happened-before이면 clock도 작다는 성질을 주지만, clock이 작다고 반드시 causal order가 있는 것은 아니다.

Vector clock은 노드별 counter 벡터를 사용해 두 이벤트가 causal하게 비교 가능한지 또는 concurrent인지 판정할 수 있다.

## 구현 (Implementation)

벡터 시계 비교는 모든 성분이 작거나 같고 하나 이상 작으면 선행 관계다.

```python
def happens_before(a, b):
    le_all = all(a[k] <= b[k] for k in a)
    lt_any = any(a[k] < b[k] for k in a)
    return le_all and lt_any


v1 = {"A": 2, "B": 1}
v2 = {"A": 3, "B": 1}
v3 = {"A": 1, "B": 3}

print(happens_before(v1, v2))
print(happens_before(v2, v3))
```

두 방향 모두 선행하지 않으면 concurrent로 본다.

## 복잡도 (Complexity)

Lamport clock은 노드당 정수 하나면 충분하다. Vector clock은 노드 수 $N$에 비례하는 메타데이터가 필요하므로 대규모 동적 membership에서는 부담이 된다.

## 응용 (Applications)

- causal consistency
- conflict detection in replicated systems
- distributed debugging과 trace ordering
- event sourcing과 메시지 순서 분석

## 흔한 오해 (Common Misunderstandings)

- 물리 timestamp가 항상 실제 인과 순서를 알려주지는 않는다.
- Lamport clock 값이 다르다고 두 이벤트가 causal하게 연결된 것은 아니다.
- vector clock은 동시성을 감지할 수 있지만 conflict를 자동 해결하지는 않는다.
- total order와 causal order는 다르다.

## TMI

- Hybrid logical clock은 물리 시간과 논리 시간을 결합해 실용적인 ordering을 제공한다.
- Consensus log는 이벤트에 total order를 부여하는 강한 방식이다.
- “시간이 어렵다”는 분산 시스템 농담은 대부분 시계 오차와 메시지 지연에서 나온다.

## 연습 / 확인 문제 (Exercises)

- happened-before 관계의 세 규칙을 써라.
- Lamport clock과 vector clock의 차이를 설명하라.
- concurrent event를 vector clock으로 판정하는 예를 만들어라.

## 이어서 읽기 (Reading Path)

- 이전: [System Models](System-Models.md)
- 다음: [분산 트랜잭션](Distributed-Transactions.md), [메시지 큐와 이벤트 스트리밍](Message-Queues-Event-Streaming.md)

## 참조 (References)

- [System-Models.md](System-Models.md)
- [Replication.md](Replication.md)
- [Consensus.md](Consensus.md)
- [Reference/Papers.md](../../Reference/Papers.md)
