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

## 법적/저작권 안전 규칙

모든 문서는 [Legal-and-Copyright-Policy.md](Maintainers/Legal-and-Copyright-Policy.md)를 따라야 한다. 법적 문제, 저작권 침해, 라이선스 위반, 개인정보 노출 가능성이 있는 내용은 저장소에 넣지 않는다.

금지되는 대표 사례:

- 책, 강의 노트, 블로그, 논문, 유료 자료 본문을 길게 복사한 내용
- 교재 문제, 시험 문제, 유료 문제, 답안지의 무단 복제
- 불법 PDF, 크랙, 토렌트, paywall 우회 링크
- 출처와 라이선스가 불명확한 코드, 이미지, 표, 다이어그램
- API 키, 토큰, 비밀번호, 내부 URL, 개인정보
- 실제 대상 침해를 돕는 보안 공격 절차

허용되는 방식:

- 직접 작성한 설명과 직접 만든 예제를 사용한다.
- 외부 자료는 짧게 요약하고 원문, 공식 문서, 출판사, 저자, 학회, 대학 강의 링크를 남긴다.
- 짧은 인용이 꼭 필요하면 필요한 최소 문장만 인용하고 출처를 명확히 적는다.
- 불확실한 자료는 넣지 말고 관리자 검토를 받는다.

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

- 개념, 직관, 핵심 이론, 구현 또는 예시, 복잡도/한계, 응용, 흔한 오해, TMI, 연습 문제, 이어서 읽기, 참조가 있다.
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

## 사람 검토 표시 (Reviewed-by)

초안은 상당수 AI가 작성하므로, 사람이 문서 전체를 직접 검토했는지는 내용 성숙도(`Status`)와 **별개의 축**으로 표시한다. 문서 상단 메타데이터에 `Reviewed-by`를 둔다.

- 검토 전: `- Reviewed-by: -`
- 검토 후: `- Reviewed-by: 이름 (YYYY-MM-DD)`
- `Status: Complete`는 사람 검토를 마친 문서에만 붙인다. 검토 표식이 없으면 검증에서 막힌다(`MissingReview`).
- 검토를 마치면 본문 맨 위(`---` 아래)에 학습자용 배지 한 줄을 추가한다. 이름과 날짜는 `Reviewed-by`와 같아야 한다.

  > ✅ **사람 검토 완료** — 이름, YYYY-MM-DD

- 검토하지 않은 문서에는 배지를 넣지 않는다. 배지와 `Reviewed-by`가 어긋나면 검증에서 막힌다.

## 문서 깊이(Depth) tier

같은 주제라도 다루는 깊이를 두 tier로 구분한다. `Depth`는 `Status`(성숙도), `Level`(학습 경로상 위치/전제), `Reviewed-by`(사람 검토)와 **독립된 축**이다.

| tier | 의미 | 분량 감각 | 템플릿 |
|---|---|---|---|
| Standard | 잘 정리된 개념 지도/강의노트. 절대다수의 기본값 | 섹션당 1~3문장 | [Topic-Template.md](Templates/Topic-Template.md) |
| Deep-dive | 선언한 선수지식 위에서 자기완결적인 심화 | 메커니즘·워크드 예제까지 | [Deep-Dive-Template.md](Templates/Deep-Dive-Template.md) |

- `Depth`는 **선택 필드**다. 없으면 Standard로 본다. 값은 `Standard` 또는 `Deep-dive`이며, 뒤에 괄호 메모를 붙일 수 있다(예: `- Depth: Deep-dive (자기완결)`). 허용 값 밖이면 검증에서 막힌다(`BadMetadataDepth`).
- **Deep-dive 품질 바** (Draft 이상으로 올리기 전 자가 점검): ① 선수지식 위에서 자기완결 ② 이론·구현·복잡도가 "왜·어떻게"(메커니즘)를 담음 ③ 워크드 예제(수치/구체) 최소 1개 ④ 실행 가능한 명령·코드·설정 ⑤ 실전 실패 모드 ⑥ 구조는 Mermaid ⑦ 비자명한 주장엔 참조.
- **운영 원칙**: deep-dive는 전 문서로 확대하지 않는다. roadmap의 핵심·길목 주제 등 **소수에만 선별 적용**한다. 깊어질수록 검증할 사실이 늘어 사람 검토 부담이 커지므로, `Complete` 승격 시 검토를 특히 꼼꼼히 한다(`Complete`는 tier와 무관하게 사람 검토 필수).
- 어떤 문서를 deep-dive 후보로 삼을지는 [Documentation-Depth-Plan.md](Maintainers/Documentation-Depth-Plan.md)의 선정 루브릭과 작업 순서를 따른다.

## 수식과 다이어그램 표기

- **수식**: 하이브리드. 의미 있는 수식은 GitHub LaTeX로 쓴다. 인라인은 `$ ... $`, 블록은 `$$ ... $$`. 복잡도 표기(`O(n log n)`)와 코드 식별자는 백틱을 유지한다.
- 표 안에서 `$ ... $`를 쓸 수 있다. 검증기가 표 셀을 나눌 때 `$ ... $` 구간의 세로줄을 보호하지만, 조건부 확률 등은 `$P(A \mid B)$`처럼 `\mid`를 쓰는 편이 안전하다.
- **다이어그램**: ` ```mermaid ` 블록을 우선 쓴다. 텍스트라 diff와 검토가 쉽고 GitHub가 바로 렌더한다.
- 이미지가 꼭 필요할 때만 `assets/<Section>/`에 두고, 파일명은 의미 중심 `Title-Kebab-Case`로, 출처와 라이선스를 [Legal-and-Copyright-Policy.md](Maintainers/Legal-and-Copyright-Policy.md)에 따라 남긴다.

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
- 상태를 추가하거나 올렸다면 `python Maintainers/Scripts/sync_summary_counts.py`로 운영 문서의 요약 수치를 자동으로 맞췄는가
- 구조 준비 완료 기준이 필요한 변경이라면 [Project-Readiness.md](Maintainers/Project-Readiness.md)에 어긋나지 않는가
- Markdown 파일에 UTF-8 BOM이 없는가
- 로드맵 필수 문서라면 [Coverage-Matrix.md](Maintainers/Coverage-Matrix.md)에 반영되어 있는가
- 핵심 경로 밖의 예정 문서라면 [Topic-Classification.md](Maintainers/Topic-Classification.md)에 반영되어 있는가
- [Legal-and-Copyright-Policy.md](Maintainers/Legal-and-Copyright-Policy.md)에 어긋나는 내용이 없는가
- 외부 본문, 코드, 이미지, 표, 문제, 답안을 무단 복사하지 않았는가
- API 키, 토큰, 비밀번호, 개인정보, 내부 URL이 포함되지 않았는가
- Markdown 상대 링크가 실제 파일이나 디렉토리를 가리키는가
- 표 헤더와 구분선의 열 수가 맞는가
- 수식은 의미 단위로 LaTeX(`$ ... $` / `$$ ... $$`)를 쓰고, 다이어그램은 Mermaid를 우선했는가
- `Status` 값이 `Planned`, `Stub`, `Draft`, `Review`, `Complete` 중 하나인가
- 주제 문서의 `Level` 값이 `Beginner`, `Intermediate`, `Advanced` 중 하나인가
- `Depth` 필드가 있다면 값이 `Standard` 또는 `Deep-dive`인가
- `Draft` 이상 주제 문서의 `Prerequisites`가 비어 있지 않은가
- 주제 문서에 `Reviewed-by`가 있으며, 검토 전이면 `-`, 검토 후이면 `이름 (YYYY-MM-DD)` 형식인가
- `Complete` 문서에는 검토 표식이 있는가
- 사람 검토를 마친 문서에 `> ✅ 사람 검토 완료` 배지가 있고 `Reviewed-by`와 일치하는가
- 예정 파일명이 영어 `Title-Kebab-Case.md` 형식인가
- 주제 파일명이 다른 섹션의 주제 파일명과 중복되지 않는가
- 예전 구조명이나 폐기된 긴 파일명이 남아 있지 않은가
- 이전 양식의 짧은 제목이나 파일 열 없는 실제 주제 표가 남아 있지 않은가
- 루트 README, 섹션 README, 로드맵의 순서가 선수지식 순서를 따르는가

## 작성 원칙

- 같은 개념을 중복 문서로 만들지 말고 기존 문서에 링크한다.
- 선수지식이 필요하면 문서 상단에 명시한다.
- 외부 자료를 참고했으면 References 섹션에 남긴다.
- 외부 자료의 본문을 옮기지 말고, 직접 작성한 설명과 링크로 대체한다.
