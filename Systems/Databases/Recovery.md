# 복구: WAL, REDO/UNDO (Database Recovery)

- Level: Advanced
- Prerequisites: [Transactions-and-ACID.md](Transactions-and-ACID.md), [Concurrency-Control.md](Concurrency-Control.md), [Systems/Operating-Systems/File-Systems.md](../Operating-Systems/File-Systems.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

데이터베이스 복구는 장애가 나도 커밋된 트랜잭션의 결과는 보존하고, 커밋되지 않은 트랜잭션의 부분 변경은 되돌리는 기술이다. WAL(Write-Ahead Logging), REDO, UNDO가 핵심 도구다.

## 직관 (Intuition)

은행 장부를 고치기 전에 “무엇을 바꿀 예정인지”를 별도 기록장에 먼저 써둔다고 생각하면 된다. 서버가 중간에 꺼져도 기록장을 보고 끝낸 일은 다시 적용하고, 끝내지 못한 일은 되돌릴 수 있다.

## 이론 (Theory)

WAL 원칙은 데이터 페이지를 디스크에 쓰기 전에 해당 변경 로그가 먼저 안정 저장소에 기록되어야 한다는 규칙이다. 로그 레코드는 보통 트랜잭션 ID, page ID, before image, after image, LSN 같은 정보를 포함한다.

- REDO: 커밋됐지만 데이터 페이지에 반영되지 않았을 수 있는 변경을 다시 적용한다.
- UNDO: 커밋되지 않은 트랜잭션의 변경을 before image로 되돌린다.
- Checkpoint: 복구 시 처음부터 모든 로그를 스캔하지 않도록 기준점을 만든다.

ARIES류 복구는 analysis, redo, undo 단계를 거쳐 crash recovery를 수행한다.

## 구현 (Implementation)

복구 판단의 핵심은 로그의 커밋 여부와 페이지 반영 여부를 비교하는 것이다.

```python
log = [
    {"tx": 1, "op": "update", "key": "x", "before": 10, "after": 20},
    {"tx": 1, "op": "commit"},
    {"tx": 2, "op": "update", "key": "y", "before": 5, "after": 9},
]

committed = {r["tx"] for r in log if r["op"] == "commit"}
redo = [r for r in log if r["op"] == "update" and r["tx"] in committed]
undo = [r for r in reversed(log) if r["op"] == "update" and r["tx"] not in committed]
print(redo, undo)
```

실제 DBMS는 pageLSN, dirty page table, compensation log record를 사용해 중복 복구를 안전하게 만든다.

## 복잡도 (Complexity)

복구 시간은 마지막 checkpoint 이후 로그 길이에 크게 좌우된다. WAL은 정상 처리 경로에 로그 쓰기 비용을 추가하지만, group commit과 sequential write로 비용을 완화한다.

## 응용 (Applications)

- DBMS crash recovery
- 트랜잭션 원자성과 지속성 보장
- replication log와 change data capture의 기반
- storage engine 설계

## 흔한 오해 (Common Misunderstandings)

- 데이터 페이지를 썼다고 트랜잭션이 커밋된 것은 아니다.
- 로그만 있으면 백업이 필요 없는 것은 아니다.
- checkpoint는 모든 로그를 삭제한다는 뜻이 아니라 복구 시작점을 줄이는 장치다.
- REDO와 UNDO는 서로 반대 방향의 역할을 하지만 둘 다 필요할 수 있다.

## TMI

- steal/no-force buffer 정책은 복구 메커니즘을 필요하게 만드는 대표적 배경이다.
- group commit은 여러 트랜잭션의 로그 flush를 묶어 fsync 비용을 줄인다.
- LSM-tree 기반 저장소도 WAL을 사용해 memtable 손실을 복구한다.

## 연습 / 확인 문제 (Exercises)

- WAL 원칙을 한 문장으로 설명하라.
- steal/no-force 정책에서 왜 UNDO와 REDO가 필요한지 설명하라.
- checkpoint가 복구 시간을 줄이는 이유를 말하라.

## 이어서 읽기 (Reading Path)

- 이전: [동시성 제어](Concurrency-Control.md)
- 다음: [쿼리 최적화](Query-Optimization.md)

## 참조 (References)

- [Transactions-and-ACID.md](Transactions-and-ACID.md)
- [Concurrency-Control.md](Concurrency-Control.md)
- [Systems/Operating-Systems/File-Systems.md](../Operating-Systems/File-Systems.md)
- [Reference/Books.md](../../Reference/Books.md)
