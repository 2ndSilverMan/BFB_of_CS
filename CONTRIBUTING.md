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
└── Templates/          문서 템플릿
```

## 문서 작성 규칙

새 주제 문서는 [Templates/Topic-Template.md](Templates/Topic-Template.md)을 기준으로 작성한다.

각 문서 상단에 다음 정보를 포함한다:

```
- Level: Beginner / Intermediate / Advanced
- Prerequisites: 선수지식 링크
- Status: Stub / Draft / Review / Complete
```

## 상태(Status) 정의

| 값 | 의미 |
|---|---|
| Planned | 목차에만 있고 아직 파일이 없음 |
| Stub | 제목과 골격만 있음 |
| Draft | 주요 내용 초안 작성 중 |
| Review | 내용 완성, 검토 필요 |
| Complete | 완성 |

## 목차 정렬 원칙

- README의 섹션과 주제 목록은 선수지식이 낮은 것에서 높은 것 순으로 배치한다.
- GitHub 파일 목록 순서를 맞추기 위한 `01-`, `02-` prefix는 사용하지 않는다.
- 파일명과 디렉토리명은 의미 중심의 영어 `Title-Kebab-Case`를 유지한다.
- 예정 주제는 파일을 만들지 않고 목차 표의 `Status` 열에 `Planned`로 표시한다.

## 파일/디렉토리 명명 규칙

- 영어 Title-Kebab-Case 사용: `Linear-Algebra/`, `Gradient-Descent.md`
- 공백 사용 금지
- 한글 제목은 문서 내부에서만 사용

## 링크 정책

| 링크 유형 | 규칙 |
|---|---|
| 섹션 디렉토리 링크 | 실제 디렉토리가 존재해야 함 |
| 주제 파일 링크 | 목차 단계에서는 예정 링크 허용 |
| 외부 참조 | 원문, 공식 문서, 논문, 강의 원본 우선 |

## 작성 원칙

- 같은 개념을 중복 문서로 만들지 말고 기존 문서에 링크한다.
- 선수지식이 필요하면 문서 상단에 명시한다.
- 외부 자료를 참고했으면 References 섹션에 남긴다.
