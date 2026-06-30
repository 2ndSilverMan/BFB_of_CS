# 시스템 설계 접근 방법 (System Design Approach)

- Level: Intermediate
- Prerequisites: [Systems/Networks/README.md](../../Systems/Networks/README.md), [Systems/Databases/README.md](../../Systems/Databases/README.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

시스템 설계는 요구사항·규모·제약을 명확히 하고 component, data flow, interface, failure mode와 tradeoff를 단계적으로 결정하는 과정이다.

## 직관 (Intuition)

상자를 먼저 그리기보다 누가 무엇을 얼마나 자주 요청하며 무엇이 실패해도 되는지 묻는다. 숫자와 invariant가 architecture 선택을 이끈다.

## 이론 (Theory)

1. Functional/non-functional requirement와 범위
2. Traffic·storage·bandwidth·latency 추정
3. API와 data model
4. High-level component와 data flow
5. Bottleneck, consistency, failure, security
6. 관찰 가능성·배포·비용과 tradeoff

Availability, consistency, latency, durability, cost는 동시에 최대화되지 않는다. 중요한 invariant와 SLO를 먼저 정한다.

## 구현 (Implementation)

```text
요구: URL 생성/조회, 10k read/s, 1k write/s
핵심 경로: Client → API → Cache → Database
불변식: short key는 하나의 destination만 가리킨다
실패 질문: cache miss, DB failover, hot key, abuse
```

## 복잡도 (Complexity)

Back-of-envelope 계산은 peak QPS, 평균 object size, retention을 곱해 order of magnitude를 얻는다. 설계 복잡도는 component 수보다 coupling과 failure state 조합에서 커진다.

## 응용 (Applications)

- interview·design review
- 신규 service architecture
- capacity planning·migration
- incident 후 구조 개선

## 흔한 오해 (Common Misunderstandings)

- 유명 architecture를 요구사항 없이 복사하면 안 된다.
- 평균 traffic만 보고 peak와 burst를 무시하면 안 된다.
- happy path diagram만으로 설계가 끝나지 않는다.
- microservice 수가 scalability의 척도는 아니다.

## TMI

- 간단한 single-node design에서 시작해 bottleneck 증거가 생길 때 확장하는 설명이 명확하다.
- decision record는 선택뿐 아니라 버린 대안과 이유를 남긴다.
- operational simplicity도 중요한 quality attribute다.

## 연습 / 확인 문제 (Exercises)

- URL shortener 요구와 규모를 추정하라.
- 핵심 invariant 3개를 작성하라.
- 한 component failure와 recovery flow를 그려라.

## 이어서 읽기 (Reading Path)

- 이전: [데이터베이스](../../Systems/Databases/)
- 다음: [확장성](Scalability.md)

## 참조 (References)

- [Systems/Distributed-Systems/System-Models.md](../../Systems/Distributed-Systems/System-Models.md)
- [Reference/Books.md](../../Reference/Books.md)
