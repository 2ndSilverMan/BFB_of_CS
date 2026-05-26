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
- 표 헤더, 구분선, 데이터 행의 열 수가 맞는지
- `Status` 값이 허용된 값인지
- 주제 문서 상단 메타데이터의 `Level`, `Prerequisites`, `Status` 값이 유효한지
- `Draft`, `Review`, `Complete` 주제 파일이 README 표에서 링크로 연결되어 있는지
- 주제 README의 `Status`와 실제 주제 문서 상단 메타데이터가 일치하는지
- `Draft`, `Review`, `Complete` 주제 문서가 필수 섹션과 `이어서 읽기`를 갖추었는지
- 루트 README가 `Planned`, `Stub`, `Draft`, `Review`, `Complete`의 학습자 관점 의미를 설명하는지
- 로드맵 문서가 현재 읽을 수 있는 범위와 아직 예정인 범위를 설명하는지
- 학습 영역 README가 `Draft` 이상 문서와 `Planned` 주제를 구분해서 안내하는지
- 작성자용 운영 문서(`Maintainers/Content-Backlog.md`, `Maintainers/Coverage-Matrix.md`, `Maintainers/Topic-Classification.md`, `Maintainers/Reference-Coverage.md`)가 존재하는지
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
