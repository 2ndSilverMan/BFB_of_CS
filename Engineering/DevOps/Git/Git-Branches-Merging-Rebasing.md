# 브랜치, 머지, 리베이스 (Branches, Merging, Rebasing)

- Level: Beginner
- Prerequisites: [Engineering/DevOps/Git/Git-Basics.md](Git-Basics.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

브랜치는 특정 커밋을 가리키는 이름이고, 머지는 두 이력 줄기를 합치며, 리베이스는 내 커밋을 다른 기준점 위에 다시 얹는 작업이다.

## 직관 (Intuition)

브랜치는 책갈피, 머지는 두 초안을 합치는 일, 리베이스는 내 초안의 작성 순서를 최신 원고 뒤로 다시 정렬하는 일에 가깝다.

## 이론 (Theory)

Merge commit은 두 부모를 가진 새 커밋으로 이력의 분기와 합류를 보존한다. Fast-forward merge는 대상 브랜치가 단순히 앞으로 이동한다. Rebase는 새 커밋 ID를 만들기 때문에 이미 공유한 커밋에 무심코 적용하면 협업자가 혼란을 겪는다.

## 구현 (Implementation)

```bash
git switch -c feature/login
git commit -m "Add login form"
git switch main
git merge feature/login
```

```bash
git switch feature/login
git fetch origin
git rebase origin/main
```

공유 브랜치에는 팀 규칙 없이 강제 push를 하지 않는다.

## 복잡도 (Complexity)

충돌 가능성은 변경 파일 수, 같은 줄 수정 여부, 브랜치가 갈라진 기간에 따라 커진다. 작은 브랜치와 잦은 동기화가 비용을 줄인다.

## 응용 (Applications)

- 기능별 독립 작업
- release branch 관리
- hotfix 분리
- Pull Request 단위 구성

## 흔한 오해 (Common Misunderstandings)

- rebase가 merge보다 항상 “깨끗한” 것은 아니다.
- conflict가 없다고 semantic conflict가 없는 것은 아니다.
- 브랜치는 무겁지 않다. 오래 방치한 브랜치가 비싸다.
- merge commit을 없애는 것이 항상 좋은 이력은 아니다.

## TMI

- `git switch`는 branch 이동을 더 명확하게 하기 위해 도입된 명령이다.
- Squash merge는 여러 commit을 하나로 합쳐 main 이력을 단순하게 만든다.
- Trunk-based 개발은 짧은 브랜치와 feature flag를 선호한다.

## 연습 / 확인 문제 (Exercises)

- 브랜치를 만들고 fast-forward merge와 merge commit을 각각 만들어 보라.
- rebase 후 commit hash가 바뀌는지 확인하라.
- 긴 브랜치에서 conflict가 커지는 이유를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [Git 기초](Git-Basics.md)
- 다음: [원격 저장소](Git-Remotes.md)

## 참조 (References)

- [GitHub Flow](../GitHub/GitHub-Flow.md)
- [Engineering/Software-Design/Refactoring.md](../../Software-Design/Refactoring.md)

