# 작성자용 스크립트 (Maintainer Scripts)

> 문서 저장소를 검수하기 위한 보조 스크립트.

## validate_docs.py

Markdown 문서의 기본 구조를 검사한다.

필요한 런타임은 Python 3.10 이상이며, 별도 패키지는 필요 없다.

로컬에서 `python`이나 `py` 명령을 찾지 못하면 Python 3.10 이상을 설치하고 터미널을 새로 연 뒤 실행한다. GitHub Actions에서는 CI가 Python을 설치한다.

저장소 루트에서 실행한다.

```powershell
python Maintainers/Scripts/validate_docs.py
```

Windows Python 런처를 사용하는 환경에서는 다음 명령도 가능하다.

```powershell
py -3 Maintainers/Scripts/validate_docs.py
```

검사 항목:

- Markdown 파일에 UTF-8 BOM이 없는지
- Markdown 상대 링크가 실제 파일이나 디렉토리와 앵커를 가리키는지
- 표 헤더, 구분선, 데이터 행의 열 수가 맞는지 (셀 안의 `` `코드` ``와 `$...$` / `$$...$$` 수식 구간의 세로줄은 구분자로 보지 않음)
- `Status` 값이 허용된 값인지
- 주제 문서 상단 메타데이터의 `Level`, `Prerequisites`, `Status`, `Reviewed-by` 값이 유효한지
- `Reviewed-by`가 검토 완료 값이면 `이름 (YYYY-MM-DD)` 형식인지, `Status: Complete`에 검토 표식이 있는지
- 사람 검토 배지(`> ✅ **사람 검토 완료** — 이름, 날짜`)가 `Reviewed-by`와 일치하는지(없거나 어긋나면 보고)
- 주제 템플릿이 필수 메타데이터와 필수 섹션을 계속 포함하는지
- `Draft`, `Review`, `Complete` 주제 파일이 README 표에서 링크로 연결되어 있는지
- 주제 README의 `Status`와 실제 주제 문서 상단 메타데이터가 일치하는지
- `Draft`, `Review`, `Complete` 주제 문서가 필수 섹션과 `이어서 읽기`를 갖추었는지
- 루트 README가 `Planned`, `Stub`, `Draft`, `Review`, `Complete`의 학습자 관점 의미를 설명하는지
- 로드맵 문서가 현재 읽을 수 있는 범위와 아직 예정인 범위를 설명하는지
- 학습 영역 README가 `Draft` 이상 문서와 `Planned` 주제를 구분해서 안내하는지
- 작성자용 운영 문서(`Maintainers/Content-Backlog.md`, `Maintainers/Coverage-Matrix.md`, `Maintainers/Topic-Classification.md`, `Maintainers/Reference-Coverage.md`, `Maintainers/Project-Readiness.md`)가 존재하는지
- CI, 기여 가이드, 템플릿, 줄바꿈 설정 같은 필수 지원 파일이 존재하는지
- 학습자 루트에 `Scripts/` 디렉토리가 다시 생기지 않았는지
- 모든 학습 영역 디렉토리와 하위 디렉토리에 `README.md`가 있는지
- 작성자용 운영 문서의 `Draft`/`Planned` 요약 수치가 실제 README 주제 표와 일치하는지
- 작성자용 운영 문서의 요약 표에 현재 최상위 섹션이 아닌 행이 남아 있지 않은지
- `Reference/Books.md`, `Reference/Courses.md`, `Reference/Papers.md`의 커버리지 수치가 `Maintainers/Reference-Coverage.md`와 일치하는지
- `Maintainers/Reference-Coverage.md`에 현재 최상위 섹션이 아닌 행이 남아 있지 않은지
- 작성자용 운영 문서에 적힌 `.md` 파일명이 실제 주제 README 표에 존재하는지
- `Required` 주제가 `Optional`/`Deferred`로 중복 분류되지 않았는지
- 주제 README 표의 파일명이 중복되어 계획 문서 참조가 모호해지지 않는지
- 모든 `Planned` 주제가 핵심 경로 또는 `Optional`/`Deferred` 분류에 포함되는지

요약 표 검사는 `Draft`/`Planned`뿐 아니라 표에 `Review`, `Complete`, `Stub` 열이 있으면 그 수치도 실제 README 주제 표와 비교한다.

## sync_summary_counts.py

`Maintainers/Content-Backlog.md`와 `Maintainers/Coverage-Matrix.md`의 영역별 상태 수치 요약 표를 실제 README 주제 표 기준으로 다시 계산해 자동으로 맞춘다. `validate_docs.py`는 수치 불일치를 검사만 하고, 이 스크립트는 고쳐 준다. 상태 열(`Draft`, `Review`, `Planned` 등)의 숫자 칸만 바꾸고 `역할` 같은 다른 열은 그대로 둔다.

```powershell
python Maintainers/Scripts/sync_summary_counts.py          # 실제로 수정
python Maintainers/Scripts/sync_summary_counts.py --check   # 수정 없이 불일치만 보고 (CI용)
```

문서를 추가하거나 상태를 올린 뒤 이 스크립트를 실행하면 요약 수치를 손으로 맞출 필요가 없다.

## test_validate_docs.py

`validate_docs.py`와 `sync_summary_counts.py`의 핵심 함수에 대한 단위 테스트다. 표준 라이브러리 `unittest`만 쓰므로 별도 패키지가 필요 없다.

```powershell
python Maintainers/Scripts/test_validate_docs.py
```

CI(`.github/workflows/docs.yml`)는 매 PR과 설정된 브랜치 push에서 기존 구조·요약 검사와 이 테스트, 아래 준비자료 목록 검사·테스트를 실행한다.

## build_preparation_inventory.py

전체 학습 주제를 스캔해 [Preparation-Inventory.md](../Preparation-Inventory.md)를 생성한다. 참조 섹션의 직접 HTTP(S) 출처 링크, 언어가 있는 구현 후보 블록, 재작성 메모 유무를 기록한다. 코드·주석 안의 링크와 예시용 예약 도메인은 출처 수에 넣지 않는다.

```powershell
python Maintainers/Scripts/build_preparation_inventory.py               # Markdown을 표준 출력으로 보기
python Maintainers/Scripts/build_preparation_inventory.py --write       # 자동 목록 갱신
python Maintainers/Scripts/build_preparation_inventory.py --check       # 누락/오래된 목록이면 실패
python Maintainers/Scripts/build_preparation_inventory.py --format json # 이관·분류용 JSON 출력
```

`--format json`은 `--write`, `--check`와 함께 사용하지 않는다. 기본 루트는 스크립트가 있는 저장소이며, 테스트 자료 등에는 `--root`를 지정할 수 있다. Python 3.10 이상과 표준 라이브러리만 사용한다.

JSON은 주제별 경로·내용 해시, 직접 출처 URL과 줄 번호, 코드 언어와 범위, 메모 위치를 포함한다. 목록에 날짜를 자동으로 넣지 않아 같은 내용에서는 같은 출력이 나온다. 실행 시 네트워크에 접근하거나 문서의 코드를 실행하지 않는다.

링크 수는 근거의 충분성, 코드 블록 수는 실행 성공, 메모 존재는 재작성 완료를 뜻하지 않는다. 실제 확인 범위는 주제별 메모에 기록한다. Markdown `--check`는 표에 표시되는 관측값의 변경을 검사한다. 줄 위치와 내용 해시가 필요한 경우에는 JSON을 다시 내보내 최신 본문과 함께 사용한다.

## test_preparation_inventory.py

출처 파싱, 코드·주석의 가짜 링크 제외, 재작성 메모 탐지, 안정적인 출력, 파일 누락·변경 감지와 JSON CLI를 검사한다.

```powershell
python Maintainers/Scripts/test_preparation_inventory.py
```
