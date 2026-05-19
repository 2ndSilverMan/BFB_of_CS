# 작성 상태판 (Status Board)

> **역할:** 상태값의 정의를 관리하고, 영역(폴더) 단위 진행 상황을 집계한다.
> 각 문서의 현재 상태는 문서 상단 `Status:` 필드에 기록한다. Area Status 표는 영역 단위 집계다.
> **업데이트 시점:** 영역 전체가 새 단계로 전환됐을 때만 Area Status 표를 갱신한다.
>
> 현재 레포의 작성 상태를 한눈에 보기 위한 문서.

## Status Values

| 상태 | 의미 |
|---|---|
| Structure Ready | 디렉터리와 README 목차가 잡힌 상태 |
| Stub | 문서 파일은 있지만 본문이 거의 없는 상태 |
| Draft | 초안이 작성된 상태 |
| Review | 내용 검토가 필요한 상태 |
| Complete | 현재 기준으로 충분히 정리된 상태 |

## Area Status

| 영역 | 상태 | 비고 |
|---|---|---|
| [Foundations](../Foundations/) | Structure Ready | 기초 수학/프로그래밍/계산 기반 목차 구축 |
| [CS](../CS/) | Structure Ready | 전공 핵심과 고급 CS 영역 분리 |
| [AI](../AI/) | Structure Ready | AI 핵심, 생성 모델, LLM, Safety, MLOps 분리 |
| [Engineering](../Engineering/) | Structure Ready | 실무 공학 계층 구축 |
| [Roadmaps](../Roadmaps/) | Structure Ready | 목적별 학습 경로 구축 |
| [Reference](../Reference/) | Structure Ready | 색인/참조 계층 구축 |

## Link Policy

| 링크 종류 | 정책 |
|---|---|
| 상위 디렉터리 링크 | 반드시 실제 경로가 존재해야 한다 |
| 로드맵 링크 | 반드시 실제 파일이 존재해야 한다 |
| 세부 주제 `.md` 링크 | 목차 단계에서는 작성 예정 링크를 허용한다 |
| 외부 자료 링크 | 신뢰 가능한 원문 또는 공식 자료를 우선한다 |

## Current Phase

현재 단계는 **구조 설계 및 목차 구축 단계**다. 세부 주제 문서는 이후 우선순위에 따라 `Stub -> Draft -> Review -> Complete` 순서로 채운다.
