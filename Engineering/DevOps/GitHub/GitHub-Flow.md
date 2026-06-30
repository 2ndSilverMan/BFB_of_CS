# GitHub Flow

- Level: Beginner
- Prerequisites: [Engineering/DevOps/Git/Git-Branches-Merging-Rebasing.md](../Git/Git-Branches-Merging-Rebasing.md), [Engineering/DevOps/GitHub/GitHub-Issues-and-Pull-Requests.md](GitHub-Issues-and-Pull-Requests.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

GitHub Flow는 main을 항상 배포 가능한 상태로 유지하고, 짧은 feature branch에서 PR을 열어 review와 CI를 통과한 뒤 병합하는 협업 흐름이다.

## 직관 (Intuition)

큰 공사장을 오래 막아 두지 않고, 작은 작업 구역을 열었다가 검사 후 바로 본선에 합류시킨다.

## 이론 (Theory)

흐름은 branch 생성, commit, PR, review, automated check, merge, deploy로 이어진다. Trunk-based 개발과 마찬가지로 branch 수명을 짧게 유지하는 것이 핵심이다. 아직 사용자에게 노출하면 안 되는 코드는 feature flag로 감춘다. Git Flow처럼 장기 develop/release branch를 두는 방식보다 단순하지만, 배포 자동화와 test 신뢰도가 중요하다.

### Flow와 배포 능력

GitHub Flow는 main이 항상 배포 가능하다는 전제를 가진다. 이 전제가 없으면 작은 PR과 빠른 merge가 오히려 불안정해진다. CI gate, preview environment, feature flag, rollback이 함께 있어야 flow가 작동한다.

Long-lived branch가 필요한 경우도 있지만, branch가 오래 살수록 merge risk와 feedback delay가 커진다. 가능한 한 작은 변경으로 자주 통합한다.

## 구현 (Implementation)

```text
main
  └─ feature/small-change
       └─ pull request
            ├─ review
            ├─ CI checks
            └─ merge to main
```

## 복잡도 (Complexity)

프로세스는 단순하지만 main 안정성을 유지하려면 test suite, rollback, monitoring, branch protection이 필요하다.

## 응용 (Applications)

- 웹 서비스 지속 배포
- 작은 팀의 빠른 협업
- 오픈소스 contribution
- feature flag 기반 개발

## 흔한 오해 (Common Misunderstandings)

- GitHub Flow는 테스트 없이 main에 빨리 넣자는 뜻이 아니다.
- 작은 PR은 설계 없이 쪼개라는 뜻이 아니다.
- main이 깨져도 나중에 고치면 된다는 문화와 맞지 않는다.
- 배포와 merge가 항상 같은 순간일 필요는 없다.

## TMI

- Git Flow는 release cadence가 느리거나 버전 유지가 많은 제품에서 여전히 유용할 수 있다.
- Short-lived branch는 conflict와 review 부담을 줄인다.
- Feature flag는 code integration과 feature release를 분리한다.

## 연습 / 확인 문제 (Exercises)

- 한 기능을 GitHub Flow 단계로 나눠 계획하라.
- main 보호 규칙과 CI check를 연결하라.
- Git Flow가 더 적합한 상황을 하나 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [이슈와 Pull Request](GitHub-Issues-and-Pull-Requests.md)
- 다음: [코드 리뷰](GitHub-Code-Review.md)

## 참조 (References)

- [Engineering/DevOps/Git/Git-Branches-Merging-Rebasing.md](../Git/Git-Branches-Merging-Rebasing.md)
- [Engineering/Debugging/Canary-Feature-Flags.md](../../Debugging/Canary-Feature-Flags.md)
