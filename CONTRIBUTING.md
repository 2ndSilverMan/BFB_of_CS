# 기여 가이드 (Contributing)

> 이 레포는 CS와 AI 지식을 장기적으로 축적하기 위한 문서 저장소다.

## Document Rules

새 주제 문서는 [Templates/Topic-Template.md](Templates/Topic-Template.md)를 기준으로 작성한다.

각 문서는 가능한 한 다음 정보를 가진다.

- Level
- Prerequisites
- Related Topics
- Tags
- Status

## Status Values

각 상태값의 정의는 [작성 상태판 (Status Board)](Reference/Status-Board.md)에서 관리한다.

개별 주제 문서는 `Stub`, `Draft`, `Review`, `Complete` 중 하나를 사용한다.
`Structure Ready`는 영역(폴더) 단위에서만 사용하며, 개별 문서에는 쓰지 않는다.

각 문서의 현재 상태는 문서 상단 `Status:` 필드가 기준이다.
영역 전체가 새 단계로 전환됐을 때만 [Reference/Status-Board.md](Reference/Status-Board.md)의 Area Status 표를 갱신한다. 문서 하나를 작성할 때마다 갱신하지 않는다.

## Link Policy

| Link Type | Rule |
|---|---|
| Area directory links | 실제 디렉터리가 존재해야 한다 |
| Roadmap links | 실제 문서 파일이 존재해야 한다 |
| Planned topic `.md` links | 목차 단계에서는 작성 예정 링크를 허용한다 |
| External references | 가능하면 원문, 공식 문서, 논문, 강의 원본을 연결한다 |

## Writing Principles

- 개념, 직관, 이론, 구현, 복잡도, 응용을 구분한다.
- 선수지식이 필요한 경우 문서 상단에 명시한다.
- 같은 개념을 중복 문서로 만들기보다 기존 문서에 연결한다.
- 외부 자료를 참고한 경우 References에 남긴다.

## File Naming

- 디렉터리와 파일명은 영어 Title-Kebab-Case를 사용한다. 예: `Data-Structures/`, `Gradient-Descent.md`, `CS-Core.md`
- 공백은 사용하지 않는다.
- 한글 제목은 문서 내부 제목에서 사용한다.
