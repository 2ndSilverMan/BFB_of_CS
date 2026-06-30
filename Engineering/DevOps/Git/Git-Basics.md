# Git 기초 (Git Basics)

- Level: Beginner
- Prerequisites: [Programming/](../../../Programming/)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

Git은 파일 변화의 스냅샷을 커밋으로 저장하고, 커밋 그래프를 통해 프로젝트의 이력을 관리하는 분산 버전 관리 도구다.

## 직관 (Intuition)

작업 폴더는 책상, staging area는 이번에 제출할 묶음, commit은 이름 붙인 저장 지점에 가깝다. Git은 “현재 파일”보다 “어떤 변경을 어떤 이유로 남겼는가”를 관리한다.

## 이론 (Theory)

기본 영역은 working tree, index, repository다. `git status`는 세 영역의 차이를 보여 주고, `git add`는 변경을 index에 올리며, `git commit`은 index를 새 커밋으로 기록한다. 커밋은 부모 커밋을 가리켜 이력 그래프를 만든다.

### 세 영역

Git 초보 실수의 대부분은 working tree, index, repository를 구분하지 못해서 생긴다. 파일을 수정한 상태, stage한 상태, commit된 상태는 서로 다르다. `status`와 `diff`, `diff --staged`를 습관적으로 확인하면 사고가 줄어든다.

Commit은 작고 설명 가능한 단위가 좋다. 빌드 가능성, 테스트 가능성, 리뷰 가능성을 기준으로 나누면 이후 revert와 bisect가 쉬워진다.

## 구현 (Implementation)

```bash
git init
git status
git add README.md
git commit -m "Add project README"
git log --oneline
```

작업 전후에는 `git status`와 `git diff`로 무엇이 바뀌었는지 확인하는 습관을 둔다.

## 복잡도 (Complexity)

대부분의 일상 명령은 변경된 파일 수와 이력 크기에 좌우된다. 큰 binary file을 자주 커밋하면 저장소 크기와 clone 시간이 빠르게 커진다.

## 응용 (Applications)

- 개인 작업 이력 보존
- 팀 코드 리뷰 단위 만들기
- 릴리스 시점 추적
- 장애 원인 commit 탐색

## 흔한 오해 (Common Misunderstandings)

- `git add`는 서버에 올리는 명령이 아니라 commit 대상에 포함하는 명령이다.
- commit은 “완성본”만이 아니라 검토 가능한 논리 단위여야 한다.
- Git은 백업 도구가 아니다. 원격 저장소와 정책이 함께 있어야 안전하다.
- binary artifact를 저장소에 계속 넣으면 이력이 무거워진다.

## TMI

- Git commit hash는 내용 기반 식별자라 같은 내용·메타데이터 조합은 같은 ID를 만든다.
- 작은 commit은 review와 revert를 쉽게 만든다.
- `.gitignore`는 아직 추적하지 않는 파일을 무시한다. 이미 추적 중인 파일에는 별도 조치가 필요하다.

## 연습 / 확인 문제 (Exercises)

- 새 저장소를 만들고 파일 하나를 커밋하라.
- `git diff`와 `git diff --staged`의 차이를 확인하라.
- `.gitignore`를 추가하고 build artifact가 status에 나오지 않게 하라.

## 이어서 읽기 (Reading Path)

- 이전: [DevOps 개요](../)
- 다음: [브랜치, 머지, 리베이스](Git-Branches-Merging-Rebasing.md)
- 관련: [Git 내부 구조](../Git-Internals.md)

## 참조 (References)

- [Engineering/DevOps/](../)
- [Engineering/Software-Design/](../../Software-Design/)
