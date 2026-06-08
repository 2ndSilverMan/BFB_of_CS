# Git 학습 트랙 (Git)

> 커밋, 브랜치, 원격 저장소, 충돌 해결, 되돌리기를 익히는 버전 관리 트랙.

**선수지식**: [Programming/](../../../Programming/)

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

| Order | 주제 | 파일 | 설명 | Status |
|---|---|---|---|---|
| 1 | Git 기초 | Git-Basics.md | 저장소, 커밋, 상태 확인, staging area | Planned |
| 2 | 브랜치, 머지, 리베이스 | Git-Branches-Merging-Rebasing.md | branch, merge, rebase의 차이와 사용 기준 | Planned |
| 3 | 원격 저장소 | Git-Remotes.md | remote, fetch, pull, push, upstream | Planned |
| 4 | 충돌 해결 | Git-Conflict-Resolution.md | merge conflict 읽기, 해결, 재검증 | Planned |
| 5 | 변경 되돌리기 | Git-Undoing-Changes.md | restore, revert, reset의 차이와 위험도 | Planned |

---

## 학습 순서

```text
Git-Basics -> Git-Branches-Merging-Rebasing -> Git-Remotes
        ↓
Git-Conflict-Resolution -> Git-Undoing-Changes
```

---

## TMI

- Git은 Linux 커널 개발 흐름을 감당하기 위해 만들어졌다. 그래서 작은 프로젝트보다 대규모 분산 협업을 염두에 둔 설계가 많다.
- Git에서 branch는 생각보다 가볍다. 내부적으로는 특정 커밋을 가리키는 이름에 가깝기 때문에, 브랜치를 자주 만드는 문화가 자연스럽다.
- `git reset --hard`는 작업 내용을 날릴 수 있다. 팀 문서에서는 보통 "무엇이 지워지는지 설명할 수 있을 때만 사용" 같은 규칙을 둔다.
- Git은 파일의 변경분만 저장한다고 흔히 설명하지만, 내부 모델은 스냅샷에 더 가깝다. 이 차이를 알면 `commit`, `tree`, `blob` 개념이 덜 낯설어진다.

---

## 연관 섹션

- [Engineering/DevOps/](../) - CI/CD와 배포 자동화의 출발점
- [Engineering/Software-Design/](../../Software-Design/) - 코드 변경을 작게 나누는 설계 습관
- [GitHub 학습 트랙](../GitHub/) - Git 기반 협업 플랫폼
