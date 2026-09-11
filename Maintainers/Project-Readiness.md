# 프로젝트 준비 상태 (Project Readiness)

> 새 문서 프로젝트의 준비자료를 보강하면서 유지하는 구조와 기록 기준.

---

## 현재 판정

2026-09-11 기준, 이 저장소는 **나중에 별도 문서 프로젝트로 재구성할 준비자료**를 모은다. 학습 주제의 deep-dive 품질 목표와 기존 구조 검증은 유지하며, 재사용할 재료와 추가 조사할 내용을 [Preparation-Guide.md](Preparation-Guide.md)에 따라 기록한다.

현재 작업은 직접 출처 연결, 구체 예제 보강, 부족한 부분 기록과 전체 자료 목록 갱신이다. 사람 검토와 `Complete` 승격은 이 준비 단계의 작업이나 완료 조건에 포함하지 않는다.

## 현재 우선순위

| 순위 | 작업 | 이유 |
|---|---|---|
| 1 | 핵심 주장에 원문·공식 문서를 직접 연결한다 | 재작성 때 근거를 다시 찾는 시간을 줄인다 |
| 2 | 입력·과정·결과가 있는 계산·실행·실패 사례를 보강한다 | 새 문서의 설명과 실습으로 재사용한다 |
| 3 | 재작성 메모에 재사용할 재료와 추가 조사할 질문을 남긴다 | 같은 부족분을 다시 조사하지 않게 한다 |
| 4 | 전체 자료 목록과 JSON 출력을 최신 상태로 유지한다 | 주제별 선별·재배치를 돕는다 |
| 5 | 구조·요약 수치와 자동 목록 검증을 유지한다 | 자료가 늘어도 링크와 기록을 추적한다 |

## 운영 게이트

| 영역 | 완료 기준 | 자동 검증 |
|---|---|---|
| 시작점 | 학습자가 루트 README, Roadmaps, 섹션 README만으로 다음 문서를 찾을 수 있다 | `validate_docs.py` |
| 주제 등록 | 모든 예정 주제는 섹션 README 표에 있고, 핵심 경로 또는 `Optional`/`Deferred` 분류에 들어간다 | `validate_docs.py` |
| 본문 문서 | 실제 파일이 있는 주제는 `Level`, `Prerequisites`, `Status`, `Reviewed-by`, `Depth`와 필수 섹션을 가진다 | `validate_docs.py` |
| 상태 동기화 | 섹션 README의 `Status`와 본문 메타데이터의 `Status`가 일치한다 | `validate_docs.py` |
| 요약 수치 | Backlog, Coverage Matrix, Reference Coverage 수치가 실제 표와 일치한다 | `validate_docs.py`, `sync_summary_counts.py --check` |
| 참조 자료 | 책, 강의, 논문 항목은 분야별 커버리지에 반영된다 | `validate_docs.py` |
| 재작성 기록 | 보강한 주제에 재사용할 재료, 보충할 내용, 확인 범위를 남긴다 | 메모 제목 존재만 자동 목록으로 확인; 내용 충분성은 자동 판정하지 않음 |
| 자료 목록 | 모든 학습 주제의 직접 출처·구현 후보·메모 현황이 최신이다 | `build_preparation_inventory.py --check` |
| 저작권/보안 | 외부 자료 무단 복사, 불법 링크, 민감정보, 공격 절차를 포함하지 않는다 | 일부 링크 정책만 자동 검증; 법적 적합성을 보증하는 검사가 아님 |
| 검토 상태의 정직성 | 실제 사람 검토 기록이 있을 때만 `Reviewed-by`와 배지를 채운다. 준비 작업에서는 `-`를 유지한다 | `validate_docs.py`의 기존 상태·배지 검사 |

## 지식 문서 작성 절차

1. [Preparation-Inventory.md](Preparation-Inventory.md)와 [Content-Backlog.md](Content-Backlog.md)에서 다음 자료 보강 대상을 고른다.
2. 해당 주제가 로드맵 필수라면 [Coverage-Matrix.md](Coverage-Matrix.md)를 확인한다.
3. 핵심 경로 밖의 주제라면 [Topic-Classification.md](Topic-Classification.md)에서 분류를 확인한다.
4. deep-dive 품질 기준이나 다음 비검토 작업 순서를 고른다면 [Documentation-Depth-Plan.md](Documentation-Depth-Plan.md)를 확인한다.
5. 새 학습 주제는 원칙적으로 [Deep-Dive-Template.md](../Templates/Deep-Dive-Template.md)를 기준으로 작성한다. 가벼운 표준 문서는 예외적으로 [Topic-Template.md](../Templates/Topic-Template.md)를 쓴다.
6. 문서 상단 `Reviewed-by`는 검토 전 `-`로 둔다.
7. 상위 README에서 파일 링크와 `Status`를 갱신한다.
8. 필요하면 [Reference/](../Reference/)와 [Reference-Coverage.md](Reference-Coverage.md)를 함께 갱신한다.
9. 재작성 메모를 남기고 `python Maintainers/Scripts/build_preparation_inventory.py --write`로 목록을 갱신한 뒤 아래 검증 명령을 모두 통과시킨다.

## 검증 명령

저장소 루트에서 실행한다.

```powershell
python Maintainers/Scripts/validate_docs.py
python Maintainers/Scripts/sync_summary_counts.py --check
python Maintainers/Scripts/test_validate_docs.py
python Maintainers/Scripts/build_preparation_inventory.py --check
python Maintainers/Scripts/test_preparation_inventory.py
```

로컬에서 `python`이 없고 `uv`가 있다면 임시 캐시를 지정해 실행할 수 있다.

```powershell
uv --cache-dir "$env:TEMP\uv-cache-bfb" run python Maintainers/Scripts/validate_docs.py
uv --cache-dir "$env:TEMP\uv-cache-bfb" run python Maintainers/Scripts/sync_summary_counts.py --check
uv --cache-dir "$env:TEMP\uv-cache-bfb" run python Maintainers/Scripts/test_validate_docs.py
uv --cache-dir "$env:TEMP\uv-cache-bfb" run python Maintainers/Scripts/build_preparation_inventory.py --check
uv --cache-dir "$env:TEMP\uv-cache-bfb" run python Maintainers/Scripts/test_preparation_inventory.py
```

## 완료와 미완료의 구분

- **구조 준비 완료**: 위 운영 게이트와 검증 명령이 통과하는 상태.
- **개별 주제의 재작성 재료 확보**: 직접 출처와 그 사용 범위, 구체 예제, 추가 조사할 질문, 확인한 범위가 기록된 상태. 자동 목록의 숫자만으로 판정하지 않는다.
- **deep-dive 운영 완료**: 학습 주제 문서가 `Depth: Deep-dive`와 필수 섹션을 갖추고, README와 운영 문서가 같은 정책을 말하는 상태.
- **지식 경로 완료**: 특정 로드맵의 필수 문서가 `Review` 이상으로 작성되고, 로드맵이 산출물과 다음 학습 경로를 안내하는 상태.
- **완성 문서**: 사람이 전체 내용을 검토하고 `Reviewed-by`와 검토 배지를 채운 `Complete` 문서.

전체 목록 생성은 모든 문서의 자료 보강 완료를 뜻하지 않는다. 현재는 주제별 재작성 재료 확보를 진행하며, 사람 검토 완료는 준비 단계와 별도로 유지하는 기존 상태 정의다.
