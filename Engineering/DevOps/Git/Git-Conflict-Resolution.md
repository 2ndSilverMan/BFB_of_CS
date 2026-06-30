# Git 충돌 해결 (Git Conflict Resolution)

- Level: Beginner
- Prerequisites: [Engineering/DevOps/Git/Git-Remotes.md](Git-Remotes.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

Git 충돌은 두 이력에서 같은 파일의 같은 영역을 서로 다르게 바꿔 Git이 자동으로 합칠 수 없을 때 발생한다.

## 직관 (Intuition)

두 사람이 같은 문장의 결말을 다르게 고쳤다면, 도구는 어느 쪽이 맞는지 모른다. 사람이 의도를 읽고 하나의 결과로 다시 써야 한다.

## 이론 (Theory)

Merge conflict는 conflict marker로 표시된다. `<<<<<<<`, `=======`, `>>>>>>>` 사이를 읽고 최종 파일을 직접 만든 뒤 `git add`로 해결 표시를 한다. Rebase 중 충돌은 각 commit을 재적용하는 과정에서 반복적으로 나타날 수 있으며, 해결 후 `git rebase --continue`를 실행한다.

### 충돌 해결의 검증

충돌은 텍스트 병합 실패일 뿐 의미 병합 성공을 보장하지 않는다. 충돌 마커를 제거한 뒤에는 관련 테스트, 빌드, 가능하면 변경 영역의 동작 확인을 해야 한다. 특히 양쪽 변경이 같은 API contract를 다르게 바꿨다면 semantic conflict가 남을 수 있다.

큰 충돌은 파일별로 해결하고, resolution commit을 작게 유지한다. 자동 포매팅은 충돌 해결과 분리하면 리뷰가 쉬워진다.

## 구현 (Implementation)

```text
<<<<<<< HEAD
현재 브랜치 내용
=======
합치려는 브랜치 내용
>>>>>>> feature
```

최종 파일에는 marker가 남으면 안 된다. 해결 후에는 build와 test를 실행해 문법 충돌뿐 아니라 의미 충돌도 확인한다.

## 복잡도 (Complexity)

충돌 비용은 충돌 영역 수보다 변경 의도를 이해하는 비용에 더 좌우된다. 오래 갈라진 branch일수록 semantic conflict 위험이 커진다.

## 응용 (Applications)

- merge conflict 수동 해결
- rebase conflict 처리
- lockfile conflict 재생성
- generated file 충돌 정책 수립

## 흔한 오해 (Common Misunderstandings)

- conflict marker를 지우는 것만으로 해결이 끝난 것은 아니다.
- “ours/theirs”는 merge와 rebase 상황에서 직관과 다르게 느껴질 수 있다.
- 자동 merge 성공이 동작 성공을 보장하지 않는다.
- lockfile은 손으로 섞기보다 재생성이 안전한 경우가 많다.

## TMI

- `git rerere`는 이전 충돌 해결 방법을 기억해 반복 conflict를 줄인다.
- 작은 PR과 잦은 main 동기화가 conflict를 줄인다.
- 충돌 해결 commit message에는 왜 그 결과를 택했는지 남기면 좋다.

## 연습 / 확인 문제 (Exercises)

- 같은 줄을 두 브랜치에서 다르게 고쳐 conflict를 만들어 보라.
- conflict 해결 후 test를 실행하는 이유를 설명하라.
- rebase 중 conflict와 merge 중 conflict의 흐름을 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [원격 저장소](Git-Remotes.md)
- 다음: [변경 되돌리기](Git-Undoing-Changes.md)

## 참조 (References)

- [Engineering/Testing/](../../Testing/)
- [GitHub 코드 리뷰](../GitHub/GitHub-Code-Review.md)
