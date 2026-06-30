# 프로젝트 준비 상태 (Project Readiness)

> 지식 본문 작성 단계로 들어가기 전에 유지해야 하는 구조적 완료 기준.

---

## 현재 판정

2026-06-08 기준, 이 저장소는 **지식 문서를 채우는 단계로 진입 가능한 구조**를 목표로 관리한다. 새 지식 문서를 추가할 때는 아래 운영 게이트를 통과해야 한다.

현재 남은 핵심 작업은 본문 작성과 사람 검토다. 디렉토리 구조, 로드맵, 주제 분류, 템플릿, 참조 커버리지, 법적 정책, 검증 스크립트는 계속 동기화되어야 한다.

## 운영 게이트

| 영역 | 완료 기준 | 자동 검증 |
|---|---|---|
| 시작점 | 학습자가 루트 README, Roadmaps, 섹션 README만으로 다음 문서를 찾을 수 있다 | `validate_docs.py` |
| 주제 등록 | 모든 예정 주제는 섹션 README 표에 있고, 핵심 경로 또는 `Optional`/`Deferred` 분류에 들어간다 | `validate_docs.py` |
| 본문 문서 | 실제 파일이 있는 주제는 `Level`, `Prerequisites`, `Status`, `Reviewed-by`와 필수 섹션을 가진다 | `validate_docs.py` |
| 상태 동기화 | 섹션 README의 `Status`와 본문 메타데이터의 `Status`가 일치한다 | `validate_docs.py` |
| 요약 수치 | Backlog, Coverage Matrix, Reference Coverage 수치가 실제 표와 일치한다 | `validate_docs.py`, `sync_summary_counts.py --check` |
| 참조 자료 | 책, 강의, 논문 항목은 분야별 커버리지에 반영된다 | `validate_docs.py` |
| 저작권/보안 | 외부 자료 무단 복사, 불법 링크, 민감정보, 공격 절차를 포함하지 않는다 | 일부 자동 검증 + 사람 검토 |
| 사람 검토 | 검토 완료 문서는 `Reviewed-by`와 학습자 배지가 일치한다 | `validate_docs.py` |

## 지식 문서 작성 절차

1. [Content-Backlog.md](Content-Backlog.md)에서 다음 작성 대상을 고른다.
2. 해당 주제가 로드맵 필수라면 [Coverage-Matrix.md](Coverage-Matrix.md)를 확인한다.
3. 핵심 경로 밖의 주제라면 [Topic-Classification.md](Topic-Classification.md)에서 분류를 확인한다.
4. 기존 문서를 깊게 만들거나 `Depth: Deep-dive` 후보를 고른다면 [Documentation-Depth-Plan.md](Documentation-Depth-Plan.md)를 확인한다.
5. Standard 문서는 [Topic-Template.md](../Templates/Topic-Template.md), deep-dive 문서는 [Deep-Dive-Template.md](../Templates/Deep-Dive-Template.md)를 기준으로 본문을 작성한다.
6. 문서 상단 `Reviewed-by`는 검토 전 `-`로 둔다.
7. 상위 README에서 파일 링크와 `Status`를 갱신한다.
8. 필요하면 [Reference/](../Reference/)와 [Reference-Coverage.md](Reference-Coverage.md)를 함께 갱신한다.
9. 아래 검증 명령을 모두 통과시킨다.

## 검증 명령

저장소 루트에서 실행한다.

```powershell
python Maintainers/Scripts/validate_docs.py
python Maintainers/Scripts/sync_summary_counts.py --check
python Maintainers/Scripts/test_validate_docs.py
```

로컬에서 `python`이 없고 `uv`가 있다면 임시 캐시를 지정해 실행할 수 있다.

```powershell
uv --cache-dir "$env:TEMP\uv-cache-bfb" run python Maintainers/Scripts/validate_docs.py
uv --cache-dir "$env:TEMP\uv-cache-bfb" run python Maintainers/Scripts/sync_summary_counts.py --check
uv --cache-dir "$env:TEMP\uv-cache-bfb" run python Maintainers/Scripts/test_validate_docs.py
```

## 완료와 미완료의 구분

- **구조 준비 완료**: 위 운영 게이트와 검증 명령이 통과하는 상태.
- **지식 경로 완료**: 특정 로드맵의 필수 문서가 `Review` 이상으로 작성된 상태.
- **완성 문서**: 사람이 전체 내용을 검토하고 `Reviewed-by`와 검토 배지를 채운 `Complete` 문서.

이 저장소는 구조 준비 완료와 지식 경로 완료를 분리해서 관리한다. 새 주제 파일을 많이 만드는 것보다, 백로그 순서대로 실제 학습 가능한 문서를 채우고 검토하는 것을 우선한다.
