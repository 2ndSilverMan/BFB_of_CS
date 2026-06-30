# 코드 커버리지 (Code Coverage)

- Level: Intermediate
- Prerequisites: [Engineering/Testing/Testing-Pyramid.md](Testing-Pyramid.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

코드 커버리지는 테스트가 실행한 코드의 비율을 측정하는 지표다. 라인, 브랜치, 조건, 함수 커버리지 등이 있으며 테스트 누락 영역을 찾는 데 도움을 준다.

## 직관 (Intuition)

커버리지는 지도에서 지나간 길을 색칠하는 것과 같다. 색칠된 길이 많다고 여행이 목적지에 잘 도착했다는 뜻은 아니지만, 한 번도 가보지 않은 곳은 알 수 있다.

## 이론 (Theory)

라인 커버리지는 실행된 줄, 브랜치 커버리지는 조건 분기의 양쪽 경로, 조건 커버리지는 복합 조건의 각 부분을 본다. 높은 커버리지는 필요조건에 가깝지만 충분조건은 아니다.

### Coverage의 해석

Coverage는 테스트가 실행한 코드의 양을 말하지, assertion이 의미 있는지를 말하지 않는다. Line coverage가 높아도 결과를 검증하지 않으면 결함을 놓친다. Branch coverage, condition coverage, mutation score를 함께 보면 "실행했다"와 "검증했다"의 간극을 줄일 수 있다.

실무에서는 전체 coverage 숫자보다 위험한 변경 영역의 diff coverage와 critical module coverage를 더 중요하게 본다. Coverage gate는 테스트 작성을 유도하는 guardrail이지 품질의 최종 증명이 아니다.

## 구현 (Implementation)

```text
coverage report:
  lines: 85%
  branches: 72%
  uncovered: payment/refund.py:42
```

Threshold는 전체 숫자보다 핵심 모듈과 변경 코드 기준으로 잡는 편이 실용적이다.

## 복잡도 (Complexity)

커버리지 측정은 실행을 계측하므로 테스트가 약간 느려질 수 있다. 커버리지 목표를 무리하게 높이면 의미 없는 테스트가 늘 수 있다.

## 응용 (Applications)

- 테스트 사각지대 탐색
- PR 품질 gate
- 레거시 코드 개선 추적
- 위험 모듈 우선순위화

## 흔한 오해 (Common Misunderstandings)

- 100% 커버리지가 버그 0개를 의미하지 않는다.
- 실행만 하고 assertion이 없으면 커버리지만 올라간다.
- 전체 평균이 높아도 중요한 모듈이 비어 있을 수 있다.
- 커버리지 숫자를 목표로 삼으면 테스트 품질이 왜곡될 수 있다.

## TMI

- Branch coverage는 line coverage보다 조건문 누락을 잘 드러낸다.
- Diff coverage는 변경된 코드에 집중한다.
- Mutation testing은 커버리지보다 assertion 강도를 더 잘 보여 줄 수 있다.

## 연습 / 확인 문제 (Exercises)

- 라인 커버리지와 브랜치 커버리지 차이를 예제로 설명하라.
- Assertion 없는 테스트가 왜 위험한지 말하라.
- 변경 코드 기준 coverage gate를 설계하라.

## 이어서 읽기 (Reading Path)

- 이전: [테스트 피라미드](Testing-Pyramid.md)
- 다음: [뮤테이션 테스트](Mutation-Testing.md), [정적 분석과 린터](Static-Analysis-Linting.md)

## 참조 (References)

- [Engineering/Testing/Testing-Pyramid.md](Testing-Pyramid.md)
- [Reference/Books.md](../../Reference/Books.md)
