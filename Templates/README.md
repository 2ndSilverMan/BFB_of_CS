# 템플릿 (Templates)

> 문서 형식을 통일하기 위한 템플릿 모음.

## 문서 종류별 템플릿

| 템플릿 | 용도 | 대상 |
|---|---|---|
| [섹션 README 템플릿](Section-README-Template.md) | 상위 지식 영역의 허브 | `Math/README.md`, `Systems/README.md`, `CS-Theory/README.md`, `AI/README.md`, `Engineering/README.md` |
| [주제 인덱스 README 템플릿](Topic-Index-README-Template.md) | 상위/하위 주제 목록과 커버리지 관리 | `Programming/README.md`, `Programming/Languages/README.md`, `Programming/Languages/Python/README.md`, `Data-Structures/README.md`, `Algorithms/README.md`, `Systems/Operating-Systems/Linux/README.md`, `AI/MLOps/README.md`, `Engineering/DevOps/README.md`, `Engineering/DevOps/Git/README.md`, `Engineering/DevOps/GitHub/README.md` |
| [개별 주제 문서 템플릿](Topic-Template.md) | 개별 개념, 알고리즘, 이론, 기술 문서 작성 | `Linear-Regression.md`, `BFS-DFS.md` |
| [로드맵 템플릿](Roadmap-Template.md) | 목적별 학습 순서 | `Roadmaps/*.md` |
| [참조 목록 템플릿](Reference-List-Template.md) | 책, 강의, 논문 목록 | `Reference/Books.md`, `Reference/Courses.md`, `Reference/Papers.md` |
| [용어 사전 템플릿](Glossary-Template.md) | 용어 정의와 관련 섹션 연결 | `Reference/Glossary.md` |

문서 구조 검수는 [Maintainers/Scripts/validate_docs.py](../Maintainers/Scripts/validate_docs.py)로 수행한다.

학습자에게 보이는 README와 로드맵은 현재 읽을 수 있는 `Draft` 이상 문서와 아직 본문이 없는 `Planned` 주제를 명확히 구분해야 한다.
