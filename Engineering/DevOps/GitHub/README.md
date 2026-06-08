# GitHub 학습 트랙 (GitHub)

> 원격 저장소, 이슈, Pull Request, 코드 리뷰, GitHub Actions를 사용하는 협업 트랙.

**선수지식**: [Engineering/DevOps/Git/](../Git/)

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

| Order | 주제 | 파일 | 설명 | Status |
|---|---|---|---|---|
| 1 | 저장소와 권한 | GitHub-Repositories.md | repository, visibility, collaborator, permission | Planned |
| 2 | 이슈와 Pull Request | GitHub-Issues-and-Pull-Requests.md | issue, PR, review, merge 흐름 | Planned |
| 3 | GitHub Flow | GitHub-Flow.md | 브랜치 기반 협업과 trunk-based 개발 비교 | Planned |
| 4 | 코드 리뷰 | GitHub-Code-Review.md | 리뷰 관점, 코멘트, 승인, 변경 요청 | Planned |
| 5 | GitHub Actions | GitHub-Actions.md | workflow, job, step, runner, secret | Planned |

---

## 학습 순서

```text
GitHub-Repositories -> GitHub-Issues-and-Pull-Requests -> GitHub-Flow
        ↓
GitHub-Code-Review -> GitHub-Actions
```

---

## TMI

- Git과 GitHub는 같은 것이 아니다. Git은 버전 관리 도구이고, GitHub는 Git 저장소를 중심으로 협업 기능을 제공하는 플랫폼이다.
- Pull Request는 Git 자체 기능이 아니라 GitHub 같은 플랫폼이 제공하는 협업 단위다.
- GitHub Actions의 `secret`은 로그에 그대로 찍히지 않도록 마스킹되지만, 잘못된 스크립트나 외부 전송까지 자동으로 막아 주지는 않는다.
- README의 배지, PR 템플릿, issue 템플릿은 기능보다 작은 장치처럼 보이지만, 오픈소스 프로젝트에서는 기여 품질을 꽤 많이 좌우한다.

---

## 연관 섹션

- [Git 학습 트랙](../Git/) - GitHub 사용 전 필요한 버전 관리 기초
- [Engineering/Testing/](../../Testing/) - PR에서 자동화 테스트를 돌리는 흐름
- [Engineering/DevOps/](../) - CI/CD, 배포, 운영 자동화
