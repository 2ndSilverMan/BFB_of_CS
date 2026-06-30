# 계약 테스트 (Contract Testing)

- Level: Intermediate
- Prerequisites: [Engineering/Testing/Integration-Test-Strategy.md](Integration-Test-Strategy.md), [Engineering/System-Design/Microservices.md](../System-Design/Microservices.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

계약 테스트는 provider와 consumer 사이 API 계약이 깨지지 않는지 검증하는 테스트다. 마이크로서비스 환경에서 전체 E2E보다 빠르게 통합 안정성을 확인한다.

## 직관 (Intuition)

두 팀이 약속한 주문서 형식이 바뀌면 한쪽이 바로 깨질 수 있다. 계약 테스트는 실제 배포 전에 "내가 기대하는 요청/응답이 아직 유효한가"를 확인한다.

## 이론 (Theory)

Consumer-driven contract는 consumer가 기대하는 요청과 응답 예시를 계약으로 만들고 provider가 이를 만족하는지 검증한다. Schema validation은 구조를 확인하지만 의미 있는 사례까지 포함해야 안전하다.

### Consumer와 provider의 책임

Contract test는 consumer가 실제로 의존하는 요청/응답 형태를 명시하고 provider가 그 contract를 깨지 않는지 검증한다. OpenAPI schema validation만으로 충분하지 않을 수 있다. 상태 전이, 에러 코드, optional field 의미, backward compatibility도 contract에 포함된다.

Versioning 정책은 contract test와 함께 설계해야 한다. Provider는 새 필드를 추가할 수 있어도 기존 필드 의미를 바꾸면 consumer를 깨뜨릴 수 있다. Consumer-driven contract는 이 위험을 PR 단계에서 발견하게 해 준다.

## 구현 (Implementation)

```json
{
  "request": {"method": "GET", "path": "/users/123"},
  "response": {"status": 200, "body": {"id": "123", "name": "Ada"}}
}
```

## 복잡도 (Complexity)

서비스와 consumer 수가 많아지면 계약 versioning과 publishing workflow가 필요하다. 계약이 실제 사용 사례를 대표하지 않으면 빈틈이 남는다.

## 응용 (Applications)

- 마이크로서비스 API 변경 검증
- SDK와 서버 호환성 확인
- producer/consumer 독립 배포
- breaking change 방지

## 흔한 오해 (Common Misunderstandings)

- 계약 테스트는 E2E 테스트를 완전히 대체하지 않는다.
- OpenAPI schema만 있으면 의미 있는 계약이 보장되는 것은 아니다.
- Consumer 기대가 오래되면 provider 발전을 막을 수 있다.
- Mock server가 실제 provider와 drift되면 위험하다.

## TMI

- Pact는 consumer-driven contract testing 도구로 잘 알려져 있다.
- Backward compatibility 정책이 있어야 계약 테스트가 팀 간 협업 도구가 된다.
- 계약 테스트는 CI에서 provider 변경을 빠르게 막는 gate로 유용하다.

## 연습 / 확인 문제 (Exercises)

- 사용자 조회 API의 consumer contract를 작성하라.
- Breaking change와 non-breaking change를 구분하라.
- 계약 테스트와 통합 테스트의 차이를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [통합 테스트 전략](Integration-Test-Strategy.md)
- 다음: [데이터베이스 테스트](Database-Testing.md), [E2E 테스트](E2E-Testing.md)

## 참조 (References)

- [Engineering/System-Design/Microservices.md](../System-Design/Microservices.md)
- [Reference/Books.md](../../Reference/Books.md)
