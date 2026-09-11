# 템플릿 (Templates)

> 문서 형식을 통일하기 위한 템플릿 모음.

## 문서 종류별 템플릿

| 템플릿 | 용도 | 대상 |
|---|---|---|
| [섹션 README 템플릿](Section-README-Template.md) | 상위 지식 영역의 허브 | `Math/README.md`, `Systems/README.md`, `CS-Theory/README.md`, `AI/README.md`, `Engineering/README.md` |
| [주제 인덱스 README 템플릿](Topic-Index-README-Template.md) | 상위/하위 주제 목록과 커버리지 관리 | `Programming/README.md`, `Programming/Languages/README.md`, `Programming/Languages/Python/README.md`, `Data-Structures/README.md`, `Algorithms/README.md`, `Systems/Operating-Systems/Linux/README.md`, `AI/MLOps/README.md`, `Engineering/DevOps/README.md`, `Engineering/DevOps/Git/README.md`, `Engineering/DevOps/GitHub/README.md` |
| [개별 주제 문서 템플릿](Topic-Template.md) | 가벼운 표준 주제 문서 또는 운영상 예외 문서 | `Linear-Regression.md`, `BFS-DFS.md` |
| [Deep-dive 주제 문서 템플릿](Deep-Dive-Template.md) | 새 학습 주제의 기본 템플릿. 자기완결 심화(deep-dive) 품질 기준 | `Server-Images-and-Snapshots.md` |
| [로드맵 템플릿](Roadmap-Template.md) | 목적별 학습 순서 | `Roadmaps/*.md` |
| [참조 목록 템플릿](Reference-List-Template.md) | 책, 강의, 논문 목록 | `Reference/Books.md`, `Reference/Courses.md`, `Reference/Papers.md` |
| [용어 사전 템플릿](Glossary-Template.md) | 용어 정의와 관련 섹션 연결 | `Reference/Glossary.md` |

학습 섹션의 새 개별 주제 문서는 원칙적으로 deep-dive 템플릿을 쓰고, 메타데이터에 `Depth: Deep-dive (자기완결)`를 둔다. `Topic-Template.md`는 가벼운 표준 문서나 운영상 예외가 필요할 때 쓴다. 두 tier의 정의·품질 바·운영 원칙은 [CONTRIBUTING.md](../CONTRIBUTING.md)의 "문서 깊이(Depth) tier"를 따른다.

문서 구조 검수는 [Maintainers/Scripts/validate_docs.py](../Maintainers/Scripts/validate_docs.py)로 수행한다.

두 주제 템플릿 모두 참조 뒤에 `재작성 메모 (Rewrite Notes)`를 둔다. 새로 작성하거나 보강하는 문서는 안내 문구를 실제 재사용할 재료, 보충할 질문, 확인 범위로 교체한다. [Preparation-Guide.md](../Maintainers/Preparation-Guide.md)를 따르며, 사람 검토와 상태 승격은 현재 준비 작업의 조건이 아니다.

학습자에게 보이는 README와 로드맵은 현재 읽을 수 있는 `Draft` 이상 문서와 아직 본문이 없는 `Planned` 주제를 명확히 구분해야 한다.
