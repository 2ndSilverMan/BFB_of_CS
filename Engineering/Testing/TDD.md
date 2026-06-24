# TDD (Test-Driven Development)

- Level: Intermediate
- Prerequisites: [Engineering/Testing/Unit-Test-Principles.md](Unit-Test-Principles.md), [Engineering/Testing/Boundary-Value-Analysis.md](Boundary-Value-Analysis.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

TDD는 실패하는 테스트를 먼저 쓰고(Red), 최소 구현으로 통과시키고(Green), 설계를 개선하는(Refactor) 짧은 사이클로 개발하는 방식이다.

## 직관 (Intuition)

먼저 작은 계약을 적고, 그 계약을 만족하는 코드를 만들고, 코드 냄새를 정리한다. 테스트가 안전망이 되어 리팩터링을 허락한다.

## 이론 (Theory)

TDD의 핵심은 테스트가 설계 피드백을 준다는 점이다. 테스트하기 어렵다면 의존성이 강하거나 책임이 너무 큰 설계일 수 있다. 단, 모든 작업을 TDD로 해야 한다는 규칙은 아니다.

## 구현 (Implementation)

```text
1. 실패하는 테스트 작성
2. 가장 단순한 구현
3. 중복 제거와 이름 개선
4. 다음 작은 요구사항으로 반복
```

## 복잡도 (Complexity)

초기 속도는 느려 보일 수 있지만 regression 비용과 디버깅 시간을 줄일 수 있다. UI, 동시성, 외부 시스템 작업은 더 넓은 테스트 전략과 섞어야 한다.

## 응용 (Applications)

- 순수 도메인 로직
- 버그 수정의 재현 테스트
- 리팩터링 안전망
- API 계약 설계

## 흔한 오해 (Common Misunderstandings)

- TDD는 테스트를 많이 쓰는 것과 같지 않다. 테스트가 설계를 이끄는 방식이다.
- 테스트가 구현 세부사항에 묶이면 리팩터링이 어려워진다.
- 모든 코드를 단위 테스트만으로 검증할 수는 없다.
- Red 단계를 건너뛰면 테스트가 실제로 실패를 잡는지 모른다.

## TMI

- Triangulation은 여러 테스트로 일반화를 유도하는 TDD 기법이다.
- Fake it till you make it은 처음엔 상수로 통과시킨 뒤 일반화하는 방식이다.
- Legacy code에는 characterization test가 먼저 필요할 수 있다.

## 연습 / 확인 문제 (Exercises)

- 문자열 계산기 kata를 Red-Green-Refactor로 진행하라.
- 버그 하나를 실패 테스트로 먼저 고정하라.
- 테스트가 설계 개선을 요구한 사례를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [경계값 분석](Boundary-Value-Analysis.md)
- 다음: [BDD](BDD.md), [테스트 가능한 설계](Testable-Design.md)

## 참조 (References)

- [Engineering/Testing/Unit-Test-Principles.md](Unit-Test-Principles.md)
- [Reference/Books.md](../../Reference/Books.md)
