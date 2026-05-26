# 기여 가이드 (Contributing)

> CS와 AI 지식을 장기적으로 축적하기 위한 문서 저장소다.

---

## 디렉토리 구조

```
BFB_of_CS/
├── Programming/        프로그래밍 기초
├── Math/               수학
├── Data-Structures/    자료구조
├── Algorithms/         알고리즘
├── Systems/            컴퓨터 시스템
├── CS-Theory/          CS 이론
├── AI/                 인공지능
├── Engineering/        엔지니어링 실무
├── Roadmaps/           학습 로드맵
├── Reference/          참조 자료
├── Maintainers/        작성자용 운영 문서와 검수 도구
│   └── Scripts/        문서 구조 검수 스크립트
└── Templates/          문서 템플릿
```

## 문서 작성 규칙

새 문서는 파일 종류에 맞는 템플릿을 기준으로 작성한다. 문서 종류별 템플릿 매핑과 각 템플릿의 구조는 [Templates/README.md](Templates/README.md) 참고.

- 상위 허브 README는 하위 디렉토리를 묶는 섹션 허브다.
- 상위 주제 인덱스 README는 루트 섹션이 직접 주제 파일 목록을 관리하는 경우다.
- 하위 주제 인덱스 README는 특정 분야 내부의 주제 목록을 관리한다.
- 상위 허브 README는 `Level`과 `Status` 대신 선수지식, 서브섹션, 학습 순서, 연관 섹션을 우선한다.
- 학습자에게 보이는 README와 로드맵은 현재 읽을 수 있는 `Draft` 이상 문서와 아직 본문이 없는 `Planned` 주제를 명확히 구분한다.

주제 목록 표의 열 구성(`파일`, `설명`, `Order`, 커버리지 항목 전용 표 등)은 [Topic-Index-README-Template.md](Templates/Topic-Index-README-Template.md)를 따른다.

## 작성 우선순위

새 주제를 추가하기보다 이미 예정된 핵심 경로를 먼저 본문으로 전환한다.
전체 작성 순서는 [Content-Backlog.md](Maintainers/Content-Backlog.md)를 따르고, 로드맵 완료 기준과 실제 문서의 연결은 [Coverage-Matrix.md](Maintainers/Coverage-Matrix.md)를 따른다. 핵심 경로 밖의 예정 주제는 [Topic-Classification.md](Maintainers/Topic-Classification.md)에서 `Optional` 또는 `Deferred`로 분류한다.

| 우선순위 | 범위 | 기준 |
|---|---|---|
| 1 | [입문자 로드맵](Roadmaps/Beginner.md) | 프로그래밍, 이산수학, 자료구조, 알고리즘 기초를 실제 학습 가능한 문서로 작성 |
| 2 | [CS 핵심 로드맵](Roadmaps/CS-Core.md) | 시스템, 계산 이론, 보안 기초까지 전공 핵심 흐름 완성 |
| 3 | [AI 핵심 로드맵](Roadmaps/AI-Core.md) | 수학, 머신러닝, 딥러닝의 최소 핵심 경로 완성 |
| 4 | 심화/응용 섹션 | LLMs, AI Safety, MLOps, 고급 알고리즘 등은 핵심 경로 이후 확장 |

각 주제 문서는 다음 조건을 만족할 때 `Review` 이상으로 올린다.

- 개념, 직관, 핵심 이론, 구현 또는 예시, 복잡도/한계, 응용, 흔한 오해, 연습 문제, 이어서 읽기, 참조가 있다.
- 선수지식과 연관 섹션이 실제 링크로 연결된다.
- 독자가 문서 하나를 읽고 최소 하나의 연습 문제나 구현 과제를 수행할 수 있다.

로드맵 완료 기준에 필요한 주제를 새로 만들거나 상태를 올릴 때는 해당 로드맵의 커버리지 표도 함께 확인한다.

## 상태(Status) 정의

| 값 | 의미 |
|---|---|
| Planned | 파일을 실제로 만들지 않고 목차에 예정 파일명만 적은 상태. 커버리지 전용 표에서는 아직 본문으로 쪼개지 않은 항목 |
| Stub | 제목과 골격만 있음 |
| Draft | 주요 내용 초안 작성 중 |
| Review | 내용 완성, 검토 필요 |
| Complete | 완성 |

## 목차 정렬 원칙

- README의 섹션과 주제 목록은 선수지식이 낮은 것에서 높은 것 순으로 배치한다.
- GitHub 파일 목록 순서를 맞추기 위한 `01-`, `02-` prefix는 사용하지 않는다.
- 파일명과 디렉토리명은 의미 중심의 영어 `Title-Kebab-Case`를 유지한다.
- 예정 주제는 파일을 만들지 않고 목차 표의 `Status` 열에 `Planned`로 표시한다.
- `Reference/Books.md`, `Reference/Courses.md`, `Reference/Papers.md`를 수정하면 `Maintainers/Reference-Coverage.md`의 Coverage 표도 함께 갱신한다.
- 참조 목록의 `Link` 열은 안정적인 원문, 공식 강의, 출판사 페이지가 명확할 때만 추가한다.

## 선수지식 표기 규칙

`**선수지식**:` 라인과 표의 선수지식 열은 다음 형식을 따른다.

- 링크 가능한 선수지식은 링크로만 표기: `[Section/](path), [Section/Subsection/](path)`
- 부연이 필요하면 링크 뒤에 괄호: `[Math/Calculus/](../Calculus/) (기초 권장)`
- 링크가 없는 선수지식은 평문으로 표기: `이진수, 기본 논리 회로`
- 한 항목당 부연은 한 괄호로 묶고, 항목들은 쉼표로 구분한다.

## 파일/디렉토리 명명 규칙

- 영어 Title-Kebab-Case 사용: `Linear-Algebra/`, `Gradient-Descent.md`
- 널리 쓰이는 약어는 표준 표기를 유지한다. 예: `AI/`, `NLP/`, `LLMs/`, `PGMs/`, `MLOps/`, `DevOps/`
- 공백 사용 금지
- 한글 제목은 문서 내부에서만 사용
- 주제 파일명은 전체 주제 README 표에서 중복되지 않게 한다. 계획 문서는 bare filename으로 분류하므로 중복 파일명은 모호성을 만든다.
- 중복 개념은 canonical 문서를 정하고, 다른 섹션에서는 도메인 한정 파일명과 교차 링크를 사용한다. 예: `Normalization-Layers.md`, `Database-Normalization.md`

## 링크 정책

| 링크 유형 | 규칙 |
|---|---|
| 섹션 디렉토리 링크 | 실제 디렉토리가 존재해야 함 |
| 주제 파일 링크 | 실제 파일이 있을 때만 링크한다. 예정 문서는 목차 표의 `파일` 열에 파일명만 적는다 |
| 외부 참조 | 원문, 공식 문서, 논문, 강의 원본 우선 |

## 검수 체크리스트

문서 구조를 수정한 뒤 다음 항목을 확인한다:

- 저장소 루트에서 `python Maintainers/Scripts/validate_docs.py` 또는 `py -3 Maintainers/Scripts/validate_docs.py`로 링크, 표, 메타데이터, README-본문 상태 동기화를 검사했는가
- Markdown 파일에 UTF-8 BOM이 없는가
- 로드맵 필수 문서라면 [Coverage-Matrix.md](Maintainers/Coverage-Matrix.md)에 반영되어 있는가
- 핵심 경로 밖의 예정 문서라면 [Topic-Classification.md](Maintainers/Topic-Classification.md)에 반영되어 있는가
- Markdown 상대 링크가 실제 파일이나 디렉토리를 가리키는가
- 표 헤더와 구분선의 열 수가 맞는가
- `Status` 값이 `Planned`, `Stub`, `Draft`, `Review`, `Complete` 중 하나인가
- 주제 문서의 `Level` 값이 `Beginner`, `Intermediate`, `Advanced` 중 하나인가
- `Draft` 이상 주제 문서의 `Prerequisites`가 비어 있지 않은가
- 예정 파일명이 영어 `Title-Kebab-Case.md` 형식인가
- 주제 파일명이 다른 섹션의 주제 파일명과 중복되지 않는가
- 예전 구조명이나 폐기된 긴 파일명이 남아 있지 않은가
- 이전 양식의 짧은 제목이나 파일 열 없는 실제 주제 표가 남아 있지 않은가
- 루트 README, 섹션 README, 로드맵의 순서가 선수지식 순서를 따르는가

## 작성 원칙

- 같은 개념을 중복 문서로 만들지 말고 기존 문서에 링크한다.
- 선수지식이 필요하면 문서 상단에 명시한다.
- 외부 자료를 참고했으면 References 섹션에 남긴다.
