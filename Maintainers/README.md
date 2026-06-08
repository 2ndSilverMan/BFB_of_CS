# 작성자용 운영 문서 (Maintainers)

> 작성자와 관리자를 위한 문서 영역.

학습자는 보통 [Roadmaps/](../Roadmaps/)와 각 섹션 README만 보면 된다. 이 디렉토리는 문서를 새로 쓰거나, 상태를 올리거나, 전체 범위를 관리할 때 사용한다.

## 문서

| 문서 | 용도 |
|---|---|
| [Content-Backlog.md](Content-Backlog.md) | 전체 프로젝트의 본문 작성 우선순위 |
| [Coverage-Matrix.md](Coverage-Matrix.md) | 로드맵별 필수 문서와 완료 기준 연결 |
| [Topic-Classification.md](Topic-Classification.md) | 모든 예정 주제의 Required/Optional/Deferred 분류 |
| [Reference-Coverage.md](Reference-Coverage.md) | 책, 강의, 논문, 용어 사전의 분야별 보강 상태 |
| [Legal-and-Copyright-Policy.md](Legal-and-Copyright-Policy.md) | 저작권, 라이선스, 개인정보, 법적 리스크 방지 규칙 |
| [CONTRIBUTING.md](../CONTRIBUTING.md) | 작성 규칙과 검수 체크리스트 |
| [Templates/](../Templates/) | 문서 종류별 템플릿 |
| [Scripts/](Scripts/) | 문서 구조 검수 스크립트 |

## 준비 완료 기준

이 프로젝트가 "실제 지식 문서만 채우면 되는 상태"가 되려면 다음 조건을 유지한다.

- 학습자는 루트 README, [Roadmaps/](../Roadmaps/), 각 섹션 README만으로 시작점과 다음 주제를 찾을 수 있다.
- 모든 예정 주제는 섹션 README의 주제 표에 있고, 핵심 경로 또는 `Optional`/`Deferred` 분류에 포함된다.
- 실제 파일이 있는 주제는 [Topic-Template.md](../Templates/Topic-Template.md)의 필수 섹션을 갖추고, 상위 README의 `Status`와 문서 상단 `Status`가 일치한다.
- 로드맵 완료 기준에 필요한 문서는 [Coverage-Matrix.md](Coverage-Matrix.md)에 연결된다.
- 본문 작성 우선순위는 [Content-Backlog.md](Content-Backlog.md)에서 결정하고, 참조 자료 보강은 [Reference-Coverage.md](Reference-Coverage.md)에 반영한다.
- 모든 본문, 예제, 참조 링크는 [Legal-and-Copyright-Policy.md](Legal-and-Copyright-Policy.md)를 통과해야 한다.
- 구조 변경 뒤에는 `python Maintainers/Scripts/validate_docs.py` 또는 `py -3 Maintainers/Scripts/validate_docs.py`가 통과해야 한다.

## 작업 흐름

1. [Content-Backlog.md](Content-Backlog.md)에서 다음 작성 대상을 고른다.
2. 해당 주제가 로드맵 필수 문서라면 [Coverage-Matrix.md](Coverage-Matrix.md)를 확인한다.
3. 핵심 경로 밖의 주제라면 [Topic-Classification.md](Topic-Classification.md)의 분류를 확인한다.
4. 참조 자료를 보강한다면 [Reference-Coverage.md](Reference-Coverage.md)를 함께 갱신한다.
5. [Legal-and-Copyright-Policy.md](Legal-and-Copyright-Policy.md)에 맞게 저작권, 라이선스, 개인정보, 보안 리스크를 확인한다.
6. 템플릿에 맞춰 주제 문서를 작성하고 상위 README의 `Status`를 갱신한다.
7. 저장소 루트에서 `python Maintainers/Scripts/validate_docs.py` 또는 `py -3 Maintainers/Scripts/validate_docs.py`로 구조를 검수한다.
