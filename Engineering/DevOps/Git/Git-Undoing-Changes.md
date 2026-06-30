# Git 변경 되돌리기 (Undoing Changes)

- Level: Beginner
- Prerequisites: [Engineering/DevOps/Git/Git-Basics.md](Git-Basics.md), [Engineering/DevOps/Git/Git-Remotes.md](Git-Remotes.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

Git에서 변경 되돌리기는 working tree, staging area, commit history 중 어느 영역을 되돌리는지에 따라 `restore`, `revert`, `reset`을 구분해 사용한다.

## 직관 (Intuition)

책상 위 낙서를 지우는 일, 제출 바구니에서 빼는 일, 이미 제출한 기록을 취소하는 일은 서로 다르다. Git도 영역별 도구가 다르다.

## 이론 (Theory)

`git restore`는 파일 내용을 이전 상태로 되돌리거나 staged 변경을 내린다. `git revert`는 기존 commit의 반대 변경을 새 commit으로 만들어 공유 이력에 안전하다. `git reset`은 branch pointer와 index/working tree를 이동하며, 특히 `--hard`는 작업 내용을 잃게 할 수 있다.

### 되돌리기의 위험도

Undo 명령은 어떤 영역을 바꾸는지에 따라 위험도가 다르다. Working tree만 되돌리는지, index를 바꾸는지, commit history를 이동하는지 구분한다. 공유된 commit을 없애는 방식보다 새 revert commit을 만드는 방식이 협업에서는 안전하다.

작업 전 `status`와 diff를 확인하고, 애매하면 임시 commit이나 stash로 현재 상태를 보존한다. Reflog는 마지막 안전망이지만 의도한 백업 절차는 아니다.

## 구현 (Implementation)

```bash
git restore app.py
git restore --staged app.py
git revert <commit>
git reset --soft HEAD~1
```

`git reset --hard`나 force push는 지워지는 대상과 복구 계획을 설명할 수 있을 때만 사용한다.

## 복잡도 (Complexity)

되돌리기 자체는 빠르지만, 공유된 이력을 바꾸면 협업자의 로컬 이력 정리 비용이 커진다.

## 응용 (Applications)

- 실수로 수정한 파일 복원
- staging 대상 정리
- 배포된 commit 취소
- local commit 묶음 재정리

## 흔한 오해 (Common Misunderstandings)

- `revert`는 과거 commit을 삭제하지 않는다. 취소 commit을 추가한다.
- `reset --soft`, `--mixed`, `--hard`는 보존 범위가 다르다.
- 공유 branch에서 history rewrite는 팀 합의가 필요하다.
- Git이 모든 untracked file을 자동 보호하지는 않는다.

## TMI

- `git reflog`는 HEAD가 어디를 가리켰는지 기록해 많은 실수를 복구하는 단서가 된다.
- 안전한 되돌리기의 기본은 먼저 `status`, `diff`, `log`를 보는 것이다.
- 배포 사고 대응에서는 이력 미화보다 빠르고 추적 가능한 revert가 낫다.

## 연습 / 확인 문제 (Exercises)

- staged 변경을 unstaged로 되돌려 보라.
- commit 하나를 revert하고 이력이 어떻게 남는지 확인하라.
- `reset --soft`와 `reset --mixed`의 차이를 실습하라.

## 이어서 읽기 (Reading Path)

- 이전: [충돌 해결](Git-Conflict-Resolution.md)
- 다음: [GitHub 저장소와 권한](../GitHub/GitHub-Repositories.md)

## 참조 (References)

- [Engineering/Debugging/Bisect-Debugging.md](../../Debugging/Bisect-Debugging.md)
- [Engineering/DevOps/GitHub/](../GitHub/)
