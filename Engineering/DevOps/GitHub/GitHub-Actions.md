# GitHub Actions

- Level: Intermediate
- Prerequisites: [Engineering/DevOps/GitHub/GitHub-Code-Review.md](GitHub-Code-Review.md), [Engineering/Testing/Static-Analysis-Linting.md](../../Testing/Static-Analysis-Linting.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

GitHub Actions는 repository event에 반응해 workflow를 실행하는 자동화 플랫폼이다. CI, release, deployment, scheduled job에 사용한다.

## 직관 (Intuition)

PR이 올라오면 사람이 매번 검사하지 않고, 정해 둔 로봇 작업자가 checkout, build, test, packaging을 수행한다.

## 이론 (Theory)

Workflow는 YAML 파일이며 event, job, step, action, runner로 구성된다. Job은 기본적으로 병렬 실행될 수 있고, `needs`로 의존성을 건다. Secret과 token 권한은 최소화해야 하며, 외부 action은 version pinning과 신뢰성 검토가 필요하다. Cache는 build 시간을 줄이지만 key 설계가 중요하다.

## 구현 (Implementation)

```yaml
name: ci
on:
  pull_request:
  push:
    branches: [main]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm test
```

## 복잡도 (Complexity)

CI 시간은 dependency install, build, test 수, runner queue, cache hit에 좌우된다. Matrix build는 coverage를 늘리지만 비용도 곱해진다.

## 응용 (Applications)

- PR test와 lint
- release artifact 생성
- container image build
- scheduled maintenance

## 흔한 오해 (Common Misunderstandings)

- secret masking은 의도치 않은 외부 전송을 막지 못한다.
- `pull_request_target`은 권한이 커서 신중히 써야 한다.
- CI가 통과해도 production readiness가 자동 보장되지는 않는다.
- Cache key가 넓으면 오래된 dependency를 재사용할 수 있다.

## TMI

- `permissions`를 workflow나 job 수준에서 줄이면 token 피해 범위를 줄일 수 있다.
- Self-hosted runner는 강력하지만 격리와 secret 관리 책임이 커진다.
- Required check와 branch protection을 연결해야 CI 실패가 merge를 막는다.

## 연습 / 확인 문제 (Exercises)

- lint와 test job을 분리하고 `needs` 관계를 설정하라.
- dependency cache key에 lockfile hash를 포함하라.
- workflow token 권한을 read-only로 줄여 보라.

## 이어서 읽기 (Reading Path)

- 이전: [코드 리뷰](GitHub-Code-Review.md)
- 다음: [CI/CD 원칙](../CICD-Principles.md)

## 참조 (References)

- [Engineering/Testing/Static-Analysis-Linting.md](../../Testing/Static-Analysis-Linting.md)
- [Engineering/DevOps/](../)

