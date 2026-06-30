# 이슈와 Pull Request (Issues and Pull Requests)

- Level: Beginner
- Prerequisites: [Engineering/DevOps/GitHub/GitHub-Repositories.md](GitHub-Repositories.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

Issue는 논의·작업 추적 단위이고 Pull Request는 코드 변경을 제안하고 검토하고 병합하는 단위다.

## 직관 (Intuition)

Issue는 “무엇을 왜 할 것인가”를 잡고, PR은 “어떻게 바꿨는가”를 보여 준다. 둘이 연결되면 맥락과 구현이 이어진다.

## 이론 (Theory)

좋은 issue는 문제, 기대 결과, 재현 방법, 완료 조건을 담는다. 좋은 PR은 작은 범위, 명확한 설명, 관련 issue, 테스트 결과를 포함한다. Review는 correctness, design, maintainability, security, test coverage를 확인한다. Merge 방식은 merge commit, squash merge, rebase merge 중 팀 이력 정책에 맞춘다.

### Issue와 PR의 연결

Issue는 문제 정의와 결정 기록이고, PR은 해결 구현과 검증 증거다. 좋은 issue에는 배경, 기대 결과, 범위 밖, acceptance criteria가 있고, 좋은 PR에는 변경 요약, 테스트, 위험, rollout/rollback 메모가 있다.

템플릿은 팀의 사고 방식을 고정하는 장치다. 너무 길면 무시되고, 너무 짧으면 중요한 운영 정보가 빠진다.

## 구현 (Implementation)

```markdown
## What
- 변경 내용

## Why
- 문제와 의도

## Test
- 실행한 검증
```

PR 본문은 reviewer가 코드를 읽기 전에 방향을 잡도록 돕는다.

## 복잡도 (Complexity)

PR 크기가 커질수록 review latency와 누락 위험이 증가한다. 작은 PR은 병합은 쉽지만 cross-cutting 변경에서는 순서 관리가 필요하다.

## 응용 (Applications)

- 버그 리포트와 기능 요청 관리
- 코드 리뷰 workflow
- release note 자동화
- 작업 추적과 audit trail

## 흔한 오해 (Common Misunderstandings)

- PR은 코드만 보는 화면이 아니라 의사결정 기록이다.
- Issue 없이 PR을 만들면 맥락이 사라질 수 있다.
- Approve는 책임 없는 도장이 아니다.
- Draft PR은 미완성 공유와 조기 피드백에 유용하다.

## TMI

- “Closes #123” 같은 키워드는 merge 시 issue를 자동으로 닫을 수 있다.
- PR template은 팀이 원하는 정보를 빠뜨리지 않게 해 준다.
- Review comment는 사람보다 코드와 위험에 초점을 맞출수록 효과적이다.

## 연습 / 확인 문제 (Exercises)

- 버그 issue template에 필요한 항목을 작성하라.
- 큰 변경을 3개의 작은 PR로 나누는 계획을 세워라.
- PR 설명만 보고 reviewer가 알 수 있어야 하는 정보를 정리하라.

## 이어서 읽기 (Reading Path)

- 이전: [GitHub 저장소와 권한](GitHub-Repositories.md)
- 다음: [GitHub Flow](GitHub-Flow.md)

## 참조 (References)

- [Engineering/Testing/](../../Testing/)
- [Engineering/Debugging/Minimal-Reproducible-Example.md](../../Debugging/Minimal-Reproducible-Example.md)
