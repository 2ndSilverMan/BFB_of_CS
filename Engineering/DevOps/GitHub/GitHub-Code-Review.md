# GitHub 코드 리뷰 (Code Review)

- Level: Intermediate
- Prerequisites: [Engineering/DevOps/GitHub/GitHub-Issues-and-Pull-Requests.md](GitHub-Issues-and-Pull-Requests.md), [Engineering/Testing/Unit-Test-Principles.md](../../Testing/Unit-Test-Principles.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

코드 리뷰는 Pull Request의 변경이 의도, 설계, 안정성, 테스트, 보안, 운영성을 만족하는지 동료가 검토하는 과정이다.

## 직관 (Intuition)

리뷰는 흠집 찾기가 아니라 사고를 나누는 안전장치다. 작성자는 맥락을 제공하고, 리뷰어는 사용자가 될 시스템을 상상한다.

## 이론 (Theory)

좋은 리뷰는 blocking issue와 suggestion을 구분한다. Correctness, edge case, backward compatibility, observability, test coverage, security를 우선 보고, style은 자동화 도구에 최대한 맡긴다. 큰 설계 논쟁은 PR comment보다 design note나 sync로 분리하는 편이 낫다.

### 리뷰의 초점

좋은 리뷰는 취향보다 위험에 집중한다. Correctness, security, data migration, observability, test coverage, rollback 가능성을 먼저 보고, 스타일은 자동화 도구에 맡긴다.

리뷰어는 변경 의도와 테스트 증거를 요구하고, 작성자는 PR 크기와 설명을 리뷰 가능한 단위로 유지한다. 논쟁이 길어지면 원칙, benchmark, 작은 실험으로 수렴시킨다.

## 구현 (Implementation)

```text
review checklist:
- 요구사항을 만족하는가?
- 실패 경로와 경계값이 테스트되었는가?
- 운영 중 관찰할 로그/메트릭이 있는가?
- 보안·권한 경계가 안전한가?
- 더 작은 변경으로 나눌 수 있는가?
```

## 복잡도 (Complexity)

리뷰 시간은 diff 크기, 도메인 난도, 테스트 신뢰도, 설명 품질에 비례한다. PR이 작고 설명이 좋으면 reviewer throughput이 올라간다.

## 응용 (Applications)

- 결함 조기 발견
- 지식 공유
- 코드 스타일과 설계 일관성 유지
- 보안·운영 위험 검토

## 흔한 오해 (Common Misunderstandings)

- 리뷰는 모든 버그를 잡는 보증 장치가 아니다.
- 취향과 요구사항을 구분하지 않으면 리뷰가 소모전이 된다.
- Approve 후에도 작성자는 최종 책임을 가진다.
- 자동화 가능한 지적을 사람이 반복하면 팀 피로도가 커진다.

## TMI

- “question”, “nit”, “blocking” 같은 접두어는 comment의 강도를 명확히 한다.
- Self-review로 불필요한 diff와 로그를 먼저 제거하면 리뷰 품질이 올라간다.
- 좋은 리뷰 문화는 속도를 늦추는 장치가 아니라 되돌림 비용을 줄이는 장치다.

## 연습 / 확인 문제 (Exercises)

- 하나의 PR 설명에서 reviewer가 놓칠 수 있는 맥락을 보강하라.
- blocking comment와 optional suggestion을 구분해 작성하라.
- 테스트가 없는 변경에 어떤 질문을 해야 하는지 정리하라.

## 이어서 읽기 (Reading Path)

- 이전: [GitHub Flow](GitHub-Flow.md)
- 다음: [GitHub Actions](GitHub-Actions.md)

## 참조 (References)

- [Engineering/Testing/Unit-Test-Principles.md](../../Testing/Unit-Test-Principles.md)
- [Engineering/Software-Design/Clean-Code.md](../../Software-Design/Clean-Code.md)
