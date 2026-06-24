# GitHub 저장소와 권한 (GitHub Repositories)

- Level: Beginner
- Prerequisites: [Engineering/DevOps/Git/Git-Remotes.md](../Git/Git-Remotes.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

GitHub 저장소는 Git remote에 issue, Pull Request, 권한, branch protection, release, automation 기능을 더한 협업 공간이다.

## 직관 (Intuition)

Git이 이력 엔진이라면 GitHub 저장소는 팀이 그 이력을 검토하고 배포 준비를 하는 작업실이다.

## 이론 (Theory)

Visibility는 public/private/internal로 접근 범위를 정한다. Collaborator, team, role은 누가 읽고 쓰고 관리할 수 있는지 제어한다. Branch protection은 main branch에 직접 push를 막고 PR review, status check, signed commit 같은 조건을 요구할 수 있다. CODEOWNERS는 특정 경로 review 책임자를 지정한다.

## 구현 (Implementation)

```text
recommended repository baseline:
- protected main branch
- required status checks
- at least one review for production code
- CODEOWNERS for critical paths
- issue/PR templates
```

## 복잡도 (Complexity)

권한 모델이 세밀할수록 운영 비용이 늘지만, 큰 조직에서는 최소 권한 원칙과 감사 가능성이 중요해진다.

## 응용 (Applications)

- 팀 repository 운영
- 오픈소스 contribution 관리
- branch protection 정책
- release artifact 배포

## 흔한 오해 (Common Misunderstandings)

- private repository가 secret 보관소는 아니다.
- admin 권한을 많이 주면 사고 반경도 커진다.
- branch protection 없이 CI만 있어도 main 안정성이 보장되지는 않는다.
- Fork 권한과 원본 repository 권한은 다르다.

## TMI

- Repository의 README, license, contributing guide는 협업 진입장벽을 크게 낮춘다.
- Security advisory와 Dependabot은 운영 측면의 GitHub 기능이다.
- “누가 merge할 수 있는가”는 기술보다 팀 신뢰와 책임 경계에 가깝다.

## 연습 / 확인 문제 (Exercises)

- main branch protection에 필요한 조건을 설계하라.
- CODEOWNERS가 필요한 경로를 예시로 정하라.
- public repository에 올리면 안 되는 정보 목록을 작성하라.

## 이어서 읽기 (Reading Path)

- 이전: [Git 변경 되돌리기](../Git/Git-Undoing-Changes.md)
- 다음: [이슈와 Pull Request](GitHub-Issues-and-Pull-Requests.md)

## 참조 (References)

- [Engineering/DevOps/Git/](../Git/)
- [Engineering/Security/Auth.md](../../Security/Auth.md)

