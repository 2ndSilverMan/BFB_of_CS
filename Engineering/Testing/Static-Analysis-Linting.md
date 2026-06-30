# 정적 분석과 린터 (Static Analysis and Linting)

- Level: Intermediate
- Prerequisites: [Engineering/Testing/Code-Coverage.md](Code-Coverage.md), [Engineering/Software-Design/Clean-Code.md](../Software-Design/Clean-Code.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

정적 분석은 코드를 실행하지 않고 버그, 스타일, 보안, 타입, 복잡도 문제를 찾는 기법이다. 린터는 코드 스타일과 잠재 오류를 빠르게 알려 주는 정적 분석 도구다.

## 직관 (Intuition)

테스트가 프로그램을 달려 보며 확인한다면, 정적 분석은 출발 전에 차량 점검표를 보는 일이다. 실행하지 않아도 잡을 수 있는 문제는 빨리 잡는 편이 싸다.

## 이론 (Theory)

분석은 syntax tree, type information, data flow, control flow를 사용할 수 있다. 강한 분석일수록 더 많은 버그를 찾지만 false positive와 실행 시간이 늘 수 있다.

### 정적 분석의 계층

Lint는 style과 단순 bug pattern을 빠르게 잡고, type checker는 interface와 data shape 오류를 줄이며, SAST는 security-sensitive pattern을 탐지한다. 각 도구의 false positive 비용과 발견 가능한 결함 종류가 다르므로 같은 gate로 취급하지 않는다.

좋은 정적 분석 운영은 baseline을 만들고 새 위반을 막는 방식으로 시작한다. 기존 legacy 전체를 한 번에 고치려 하면 도구가 꺼지기 쉽다. Rule은 팀의 실제 사고 사례와 코드베이스 특성에 맞춰 조정한다.

## 구현 (Implementation)

```text
CI:
  - format check
  - lint
  - type check
  - security scan
  - tests
```

자동 수정 가능한 formatting과 사람이 판단해야 하는 lint rule을 구분한다.

## 복잡도 (Complexity)

프로젝트가 커질수록 분석 시간이 늘어난다. Rule이 너무 많거나 팀 합의가 없으면 개발자가 경고를 무시하게 된다.

## 응용 (Applications)

- 코드 스타일 통일
- 잠재 null/타입 오류 탐지
- 보안 취약 패턴 탐지
- CI 품질 gate

## 흔한 오해 (Common Misunderstandings)

- 린터는 테스트를 대체하지 않는다.
- 경고를 모두 끄면 도구 도입 의미가 없다.
- Formatting 논쟁은 자동 포맷터로 줄이는 편이 좋다.
- False positive를 관리하지 않으면 신뢰가 떨어진다.

## TMI

- Type checker는 동적 언어에서도 큰 프로젝트 안정성을 높인다.
- Pre-commit hook은 문제를 CI 전에 잡게 해 준다.
- Security linter는 취약점 가능성을 알려 주지만 exploit 가능성을 항상 증명하지는 않는다.

## 연습 / 확인 문제 (Exercises)

- 프로젝트 CI에 lint/type/test 단계를 배치하라.
- 자동 포맷터와 린터의 역할 차이를 설명하라.
- False positive rule을 처리하는 팀 정책을 설계하라.

## 이어서 읽기 (Reading Path)

- 이전: [코드 커버리지](Code-Coverage.md), [Clean Code](../Software-Design/Clean-Code.md)
- 다음: [DevOps CI/CD](../DevOps/)

## 참조 (References)

- [Engineering/Software-Design/Clean-Code.md](../Software-Design/Clean-Code.md)
- [Reference/Books.md](../../Reference/Books.md)
