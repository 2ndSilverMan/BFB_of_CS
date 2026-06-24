# CI/CD 원칙 (CI/CD Principles)

- Level: Intermediate
- Prerequisites: [Engineering/DevOps/GitHub/GitHub-Actions.md](GitHub/GitHub-Actions.md), [Engineering/Testing/Testing-Pyramid.md](../Testing/Testing-Pyramid.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

CI/CD는 변경을 자주 통합하고 자동 검증하며, 검증된 artifact를 안전하게 배포하는 개발·운영 원칙이다.

## 직관 (Intuition)

작은 변경을 자주 검사대에 올려 불량을 빨리 찾고, 같은 포장물을 개발·스테이징·운영으로 이동시킨다.

## 이론 (Theory)

CI는 main에 통합하기 전 build, test, lint, security check를 자동 실행한다. CD는 continuous delivery와 continuous deployment로 나뉜다. Delivery는 언제든 배포 가능한 상태를 만들고 사람이 승인하며, deployment는 검증 후 자동 배포까지 한다. 핵심은 immutable artifact, reproducible pipeline, fast feedback, rollback path다.

## 구현 (Implementation)

```text
commit -> build -> unit test -> integration test -> package
       -> deploy to staging -> smoke test -> production approval/deploy
```

Pipeline은 실패하면 멈추고, 같은 artifact를 환경별로 재빌드하지 않는 편이 좋다.

## 복잡도 (Complexity)

검증이 많을수록 신뢰도는 오르지만 feedback 시간이 길어진다. 빠른 test는 PR 단계에, 느린 test는 nightly나 pre-release 단계에 배치한다.

## 응용 (Applications)

- PR 자동 검증
- release artifact 생성
- staging 배포 자동화
- production 배포 승인 흐름

## 흔한 오해 (Common Misunderstandings)

- CI/CD는 YAML 파일이 아니라 변경 흐름의 품질 시스템이다.
- 자동 배포가 없더라도 continuous delivery는 가능하다.
- 테스트가 느리면 개발자는 pipeline을 우회하게 된다.
- 환경별로 artifact를 다시 만들면 “검증한 것”과 “배포한 것”이 달라진다.

## TMI

- Trunk-based 개발은 CI의 효과를 크게 만든다.
- Flaky test는 pipeline 신뢰를 빠르게 갉아먹는다.
- 배포 자동화는 rollback·monitoring·alert와 함께 설계되어야 한다.

## 연습 / 확인 문제 (Exercises)

- 현재 프로젝트에 필요한 PR 단계와 release 단계를 나누어라.
- flaky test를 발견했을 때의 팀 정책을 작성하라.
- artifact immutability가 중요한 이유를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [GitHub Actions](GitHub/GitHub-Actions.md)
- 다음: [Jenkins / GitLab CI](Jenkins-GitLab-CI.md)

## 참조 (References)

- [Engineering/Testing/Testing-Pyramid.md](../Testing/Testing-Pyramid.md)
- [Engineering/DevOps/GitHub/GitHub-Actions.md](GitHub/GitHub-Actions.md)

