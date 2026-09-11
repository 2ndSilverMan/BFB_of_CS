# 문서 심화 계획 (Documentation Depth Plan)

> 프로젝트 전체 학습 주제를 `Deep-dive` 품질로 유지하고, 사람 검토 없이 먼저 처리할 수 있는 운영 작업을 정하기 위한 기준.

---

## 목적

이 저장소는 이미 많은 주제 파일이 열려 있다. 다음 단계의 핵심은 새 파일을 계속 늘리는 것이 아니라, 열린 학습 주제들이 같은 deep-dive 품질 기준과 운영 규칙을 따르게 만드는 것이다.

심화 작업은 두 축을 분리해서 본다.

| 축 | 의미 | 판단 기준 |
|---|---|---|
| `Status` 승격 | 문서 성숙도를 `Draft`에서 `Review` 또는 `Complete`로 올리는 일 | 내용 완성도, 참조, 검증, 최종 사람 검토 |
| `Depth` 유지 | 학습 주제를 `Deep-dive` 품질로 다루는 일 | 자기완결성, 메커니즘 설명, 워크드 예제, 실패 모드, 참조 |

`Deep-dive`는 더 긴 문서를 뜻하지 않는다. 독자가 선언된 선수지식만 가지고 메커니즘, 구현, 한계, 실패 모드까지 스스로 연결할 수 있어야 한다.

## 현재 방향 (2026-09-11)

2026-07-02에 정한 전 주제 deep-dive 품질 목표는 유지한다. 현재는 이 자료를 나중에 별도 문서 프로젝트로 재작성하기 위해 직접 출처, 구체 예제, 보충할 질문을 확보한다. [Preparation-Guide.md](Preparation-Guide.md)의 기록 기준과 [Preparation-Inventory.md](Preparation-Inventory.md)의 전체 목록을 사용하며, 사람 검토와 `Complete` 승격은 현재 작업에 포함하지 않는다.

## 현재 판단

- 학습 주제 본문은 전 섹션에서 deep-dive 품질 기준을 공유한다.
- `README`, `Roadmaps`, `Reference`, `Maintainers`, `Templates`는 학습 주제 본문이 아니므로 `Depth` 정책을 그대로 강제하지 않는다. 대신 각 문서 종류별 완료 기준을 명확히 둔다.
- `Review`는 내용과 구조가 학습 가능한 상태라는 뜻으로 사용하고, `Complete`는 사람이 전체 내용을 검토한 뒤에만 붙인다.
- 준비자료의 유용성은 재사용할 설명·예제, 직접 출처, 추가 조사할 질문으로 확인한다. 출처 접근과 코드 실행은 확인 범위를 남기며, 사람 검토로 표시하지 않는다.

## 프로젝트 전체 적용 범위

심화 체계는 모든 학습 섹션에 적용하지만, 섹션마다 점검해야 하는 품질 축이 다르다.

| 섹션 | deep-dive 품질 축 | 우선 점검할 것 |
|---|---|---|
| [Programming/](../Programming/) | 언어 개념이 실제 실행 모델과 연결되어야 한다 | 값/참조, 메모리, OOP, 함수형 추상화, 언어별 함정 |
| [Math/](../Math/) | 정의, 직관, 계산 절차, 사용 맥락이 이어져야 한다 | 선형대수, 확률, 최적화의 워크드 계산과 AI/CS 연결 |
| [Data-Structures/](../Data-Structures/) | 내부 표현과 연산 불변식이 보여야 한다 | amortized/균형 조건, edge case, 구현 함정 |
| [Algorithms/](../Algorithms/) | 정당성, 복잡도, 구현 세부, 반례가 함께 있어야 한다 | 증명 직관, 상태 전이 trace, 실패하는 탐욕/DP 설계 |
| [Systems/](../Systems/) | 추상화 계층과 장애 모드가 연결되어야 한다 | 동시성, 일관성, 메모리, 네트워크, 데이터베이스 trade-off |
| [CS-Theory/](../CS-Theory/) | 형식 정의와 실제 계산/도구 감각이 이어져야 한다 | 증명 직관, 작은 예제, 컴파일러/PL/계산 모델 연결 |
| [AI/](../AI/) | 수식, 계산 그래프, 실험 실패 모드, 실무 참조가 함께 있어야 한다 | 학습 절차, 평가, 재현성, 데이터/서빙 경계 |
| [Engineering/](../Engineering/) | 운영 절차와 설계 trade-off가 실제 예로 보여야 한다 | 설정, 명령, 장애 대응, 성능·보안·품질 비용 |

## Rollout waves

아래는 deep-dive 확장의 작업 영역이다. 현재 실행 순서는 [Preparation-Guide.md](Preparation-Guide.md)의 출처·예제·메모 보강을 우선한다.

| Wave | 범위 | 목표 | 현재 처리 |
|---|---|---|---|
| 0 | 학습 주제 본문 | 전 주제에 `Depth: Deep-dive`와 필수 섹션을 갖춘다 | 완료된 상태로 검증 유지 |
| 1 | 운영 문서와 템플릿 | 문서들이 같은 deep-dive 정책과 사람 검토 우선순위를 말한다 | 우선 처리 |
| 2 | README/index 정책 | 허브 문서와 주제 본문 문서의 메타데이터 기준을 분리한다 | 다음 처리 |
| 3 | Roadmaps | 학습 산출물, 체크포인트, 복습 루프를 추가한다 | 다음 처리 |
| 4 | Reference | 책, 강의, 논문, 용어 사전의 분야별 공백을 줄인다 | 다음 처리 |
| 5 | 검증 스크립트 | 새 정책을 자동으로 더 많이 잡는다 | 필요 시 처리 |
| 별도 | 사람 검토 | 기존 `Complete`와 `Reviewed-by`의 의미 유지 | 현재 준비 작업 범위 밖 |

## 품질 점검 루브릭

문서가 deep-dive 품질을 실제로 갖추었는지는 아래 질문으로 판단한다. 태그 존재보다 중요한 것은 이 질문들에 답할 수 있는 본문이다.

| 기준 | 질문 |
|---|---|
| 로드맵 병목 | Beginner, CS Core, AI Core, Systems Engineer, ML Engineer 중 둘 이상에서 반복해서 쓰이는가 |
| 개념 전이 | 이 문서를 이해하면 여러 후속 문서의 이해 비용이 크게 줄어드는가 |
| 메커니즘 필요 | 정의만으로 부족하고 내부 동작, 증명, 실행 흐름, 실패 원리를 설명해야 하는가 |
| 실전 함정 | 잘못 이해하면 구현 오류, 성능 문제, 보안 문제, 운영 장애로 이어지는가 |
| 실행 가능성 | 실제 코드, 명령, 설정, 수치 워크드 예제가 있는가 |
| 참조 안정성 | 공식 문서, 교과서, 논문, 공개 강의 등 검증 가능한 참조가 있는가 |

## 작업 순서

1. [Project-Readiness.md](Project-Readiness.md)의 현재 우선순위에서 사람 검토가 아닌 작업을 먼저 고른다.
2. 기존 `Status`, `Depth`, 상위 README의 상태 표를 확인한다.
3. 새 학습 주제는 [Deep-Dive-Template.md](../Templates/Deep-Dive-Template.md)를 기준으로 작성한다.
4. 기존 주제는 품질 점검 루브릭에서 부족한 항목을 먼저 보강한다.
5. 비자명한 주장과 빠르게 변하는 기술 내용은 직접 참조를 붙이고, 재작성 메모에 확인 날짜·범위와 보충할 질문을 남긴다.
6. 상위 README의 `Status`와 본문 메타데이터를 동기화한다.
7. `Review` 승격은 내용 준비 상태로만 사용한다. 현재는 `Reviewed-by: -`를 유지한다.
8. `python Maintainers/Scripts/build_preparation_inventory.py --write`로 자료 목록을 갱신하고 검증 명령을 실행한다.

```powershell
python Maintainers/Scripts/validate_docs.py
python Maintainers/Scripts/sync_summary_counts.py --check
python Maintainers/Scripts/test_validate_docs.py
python Maintainers/Scripts/build_preparation_inventory.py --check
python Maintainers/Scripts/test_preparation_inventory.py
```

## 다음 비검토 작업

아래 작업은 사람 검토 없이 이어서 처리할 수 있는 프로젝트 전체 작업이다.

| 영역 | 작업 | 목적 |
|---|---|---|
| 운영 문서 | [Project-Readiness.md](Project-Readiness.md), [Content-Backlog.md](Content-Backlog.md), [Maintainers/README.md](README.md) 정책 동기화 | 다음 작업자가 같은 우선순위를 보게 한다 |
| 템플릿 | [Templates/](../Templates/)의 deep-dive 기본값과 사람 검토 설명 정리 | 새 문서가 현재 정책을 따르게 한다 |
| README/index | `Depth` 없는 허브 문서를 예외로 둘지, 별도 메타데이터를 둘지 결정 | topic docs와 hub docs의 기준 충돌을 막는다 |
| Roadmaps | 체크포인트, 산출물, 복습 루프 추가 | 학습 경로를 실제 실행 계획으로 만든다 |
| Reference | [Reference-Coverage.md](Reference-Coverage.md)의 공백 보강 | deep-dive 주장의 출처와 후속 학습 경로를 강화한다 |
| 검증 스크립트 | 새 정책을 자동 검사로 옮길지 검토 | 사람이 반복 확인할 일을 줄인다 |

## 문서 하나를 깊게 만드는 체크리스트

- 개념의 경계를 명확히 썼는가. "무엇이 아닌지"가 보이는가.
- 직관이 단순 비유에서 멈추지 않고 실제 메커니즘으로 이어지는가.
- Mermaid 다이어그램이 구조나 흐름을 설명하는가.
- 워크드 예제가 최소 하나 있는가. 수치 계산, 상태 변화, 실행 trace 중 하나는 있어야 한다.
- 구현 예시는 실제로 실행 가능한 코드, 명령, 설정인가.
- 시간/공간 복잡도 또는 운영 비용, 실패 특성, 한계를 분리해 썼는가.
- 흔한 오해와 실전 실패 모드가 짝지어 설명되어 있는가.
- 연습 문제는 본문을 다시 읽게 만드는 수준인가.
- 이어서 읽기가 실제 선수지식 순서를 유지하는가.
- 비자명한 사실, 역사, 기술 사양, 빠르게 변하는 내용에는 참조가 있는가.

## 승격 기준

| 목표 | 필요한 상태 |
|---|---|
| `Draft` 유지 | 골격과 주요 설명은 있으나 참조, 워크드 예제, 검증이 부족하다 |
| `Review` 승격 | 필수 섹션을 채웠고, 독자가 문서 하나로 연습 문제나 구현 과제를 수행할 수 있다. 사람 검토는 아직 끝나지 않아도 된다 |
| `Complete` 승격 | 사람이 전체 내용을 직접 검토했고 `Reviewed-by`와 검토 배지가 일치한다 |
| `Deep-dive` 유지 | 자기완결성, 메커니즘, 워크드 예제, 실행 가능한 구현, 실패 모드, 참조를 모두 갖춘다 |

## 하지 않을 일

- 품질 바를 만족하지 못한 문서에 `Depth: Deep-dive` 태그만 붙이지 않는다(태그와 내용이 일치해야 한다).
- 길이를 늘리기 위해 배경 설명만 덧붙이지 않는다.
- 외부 자료의 본문, 코드, 표, 문제를 옮겨 깊이를 만든 것처럼 보이게 하지 않는다.
- 빠르게 변하는 제품 사양이나 벤치마크를 검토 날짜 없이 단정하지 않는다.
- 상위 README와 본문 `Status`가 어긋난 채로 남기지 않는다.
- 사람 검토를 자동화 가능한 정리 작업의 선행 조건으로 두지 않는다.
- 사람이 직접 읽지 않은 문서에 `Reviewed-by`나 검토 배지를 채우지 않는다.
