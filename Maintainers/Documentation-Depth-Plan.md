# 문서 심화 계획 (Documentation Depth Plan)

> 넓게 열린 `Draft` 문서를 실제 학습 가능한 `Review` 문서와 선별된 `Deep-dive` 문서로 끌어올리기 위한 운영 기준.

---

## 목적

이 저장소는 이미 많은 주제 파일이 열려 있다. 다음 단계의 핵심은 새 파일을 계속 늘리는 것이 아니라, 핵심 학습 경로의 문서를 더 정확하고 자기완결적으로 만드는 것이다.

심화 작업은 두 축을 분리해서 본다.

| 축 | 의미 | 판단 기준 |
|---|---|---|
| `Status` 승격 | 문서 성숙도를 `Draft`에서 `Review` 또는 `Complete`로 올리는 일 | 내용 완성도, 참조, 검증, 사람 검토 |
| `Depth` 지정 | 일부 문서를 `Deep-dive`로 다루는 일 | 길목 주제인지, 메커니즘 설명이 필요한지, 검토 비용을 감당할 수 있는지 |

`Deep-dive`는 더 긴 문서를 뜻하지 않는다. 독자가 선언된 선수지식만 가지고 메커니즘, 구현, 한계, 실패 모드까지 스스로 연결할 수 있어야 한다.

## 현재 방향 (2026-06-29 결정)

> 메인테이너 결정으로 **모든 학습 섹션의 주제 문서를 deep-dive 품질로 확대**한다. 아래 "선정 루브릭"은 *우선순위*를 정하는 용도로 유지하되, 최종 목표는 전 주제 deep-dive다. 단 **품질 바와 `Complete` 사람 검토 요건은 그대로 적용**한다 — 길이를 늘리는 것이 아니라 메커니즘·워크드 예제·실패 모드·참조를 채우는 것이 기준이다.

## 현재 판단

- P0-P3 경로는 먼저 정확성, 참조, 연습 문제, 사람 검토 준비를 통해 `Review`로 안정화한다.
- 알고리즘 문서 다수는 이미 `Depth: Deep-dive`로 지정되어 있으므로, 새 태그를 늘리기보다 [Deep-Dive-Template.md](../Templates/Deep-Dive-Template.md)의 품질 바를 실제로 만족하는지 점검한다.
- Data-Structures는 알고리즘의 실질적 선수지식이므로 deep-dive 후보를 넓게 잡되, 구현·복잡도·실전 함정이 부족한 문서를 우선 보강한다.
- Programming, Math, Systems, CS-Theory, AI, Engineering은 대부분 Standard 초안으로 유지하되, 여러 로드맵이 공통으로 밟는 길목 주제만 deep-dive 후보로 올린다.
- `Complete`는 depth와 무관하게 사람이 전체 내용을 검토한 뒤에만 붙인다.

## 프로젝트 전체 적용 범위

심화 체계는 모든 학습 섹션에 적용하지만, 섹션마다 깊게 만들 이유가 다르다.

| 섹션 | 기본 전략 | deep-dive를 고르는 기준 |
|---|---|---|
| [Programming/](../Programming/) | 대부분 Standard. 입문자가 막히는 메모리·추상화 주제만 깊게 다룬다 | 값/참조, 메모리, OOP, 함수형 추상화처럼 이후 모든 섹션의 언어가 되는 주제 |
| [Math/](../Math/) | AI/CS 공통 수학은 Review 승격을 우선하고, 계산 절차가 있는 주제만 deep-dive 후보로 둔다 | 증명보다 사용 메커니즘이 중요한 선형대수, 확률, 최적화 주제 |
| [Data-Structures/](../Data-Structures/) | 알고리즘 구현의 기반이므로 많은 문서를 deep-dive 후보로 관리한다 | 내부 표현, 연산 불변식, amortized/균형 조건, 실전 구현 함정이 있는 구조 |
| [Algorithms/](../Algorithms/) | 핵심·길목 알고리즘은 deep-dive로 관리한다 | 정당성 증명, 복잡도 분석, 구현 세부, 반례가 학습 성패를 가르는 알고리즘 |
| [Systems/](../Systems/) | CS Core와 Systems Engineer 경로의 병목 주제를 선별한다 | 추상화 계층, 일관성, 동시성, 장애 모드처럼 단순 정의로 부족한 주제 |
| [CS-Theory/](../CS-Theory/) | 계산 이론·PL·컴파일러의 연결부를 선별한다 | 형식 정의, 증명 직관, 실제 도구와의 연결이 필요한 이론 주제 |
| [AI/](../AI/) | AI Core의 수학-모델-학습-서빙 연결부를 선별한다 | 수식, 계산 그래프, 실험 실패 모드, 최신 실무 참조가 함께 필요한 주제 |
| [Engineering/](../Engineering/) | 운영 장애와 설계 trade-off가 큰 실무 주제를 선별한다 | 설정, 명령, 장애 대응, 성능·보안 trade-off를 실제 예로 보여야 하는 주제 |

## Rollout waves

프로젝트 전체로 확장할 때는 섹션을 한 번에 모두 바꾸지 않는다. 검토 가능한 단위로 끊는다.

| Wave | 범위 | 목표 |
|---|---|---|
| 0 | 템플릿, 검증기, 운영 문서 | `Depth` 메타데이터와 deep-dive 품질 바를 저장소 규칙으로 고정 |
| 1 | P0-P3 핵심 경로 | 입문자/CS Core/AI Core 진입 문서를 `Review` 가능한 품질로 안정화 |
| 2 | Data-Structures + Algorithms | 이미 deep-dive로 지정된 문서가 실제 품질 바를 만족하는지 보강 |
| 3 | Systems + CS-Theory | 시스템·이론의 길목 주제를 deep-dive 후보로 선별하고 첫 문서를 작성 |
| 4 | Math + AI | 수학-모델-학습 흐름의 병목 문서를 선별하고 참조·검토 날짜를 보강 |
| 5 | Engineering | 운영·설계·테스트·보안·성능 문서 중 실전 실패 모드가 큰 주제를 선별 |

## 선정 루브릭

문서를 deep-dive 후보로 올릴지는 아래 질문으로 판단한다. 강한 근거가 4개 이상이면 후보로 삼고, 아니면 Standard 문서를 먼저 탄탄하게 만든다.

| 기준 | 질문 |
|---|---|
| 로드맵 병목 | Beginner, CS Core, AI Core, Systems Engineer, ML Engineer 중 둘 이상에서 반복해서 쓰이는가 |
| 개념 전이 | 이 문서를 이해하면 여러 후속 문서의 이해 비용이 크게 줄어드는가 |
| 메커니즘 필요 | 정의만으로 부족하고 내부 동작, 증명, 실행 흐름, 실패 원리를 설명해야 하는가 |
| 실전 함정 | 잘못 이해하면 구현 오류, 성능 문제, 보안 문제, 운영 장애로 이어지는가 |
| 실행 가능성 | 실제 코드, 명령, 설정, 수치 워크드 예제를 넣을 수 있는가 |
| 참조 안정성 | 공식 문서, 교과서, 논문, 공개 강의 등 검증 가능한 참조가 있는가 |

## 작업 순서

1. [Content-Backlog.md](Content-Backlog.md)와 [Coverage-Matrix.md](Coverage-Matrix.md)에서 현재 로드맵 병목을 고른다.
2. 기존 `Status`, `Depth`, 상위 README의 상태 표를 확인한다.
3. Standard로 충분한 문서는 `Review` 승격에 집중한다.
4. deep-dive 후보는 [Deep-Dive-Template.md](../Templates/Deep-Dive-Template.md)의 품질 바를 체크하고, 부족한 항목을 먼저 보강한다.
5. 비자명한 주장과 빠르게 변하는 기술 내용은 참조를 붙이고, 필요하면 `Last reviewed` 날짜를 둔다.
6. 상위 README의 `Status`와 본문 메타데이터를 동기화한다.
7. 검증 명령을 실행한다.

```powershell
python Maintainers/Scripts/validate_docs.py
python Maintainers/Scripts/sync_summary_counts.py --check
python Maintainers/Scripts/test_validate_docs.py
```

## 첫 심화 후보

아래 목록은 태그를 즉시 바꾸라는 뜻이 아니라, 다음 작성 사이클에서 먼저 살펴볼 후보군이다.

| 영역 | 후보 문서 | 심화 이유 |
|---|---|---|
| Programming | [Pointers-and-Memory.md](../Programming/Pointers-and-Memory.md), [OOP.md](../Programming/OOP.md), [Functional-Intro.md](../Programming/Functional-Intro.md) | 이후 시스템·언어론·소프트웨어 설계 문서의 공통 언어를 만든다 |
| Math | [Logic.md](../Math/Discrete/Logic.md), [Matrices.md](../Math/Linear-Algebra/Matrices.md), [Bayes-Theorem.md](../Math/Probability-Statistics/Bayes-Theorem.md), [Gradient-Descent.md](../Math/Optimization/Gradient-Descent.md) | 증명, 계산, 모델 학습의 연결부라 후속 문서 이해 비용을 크게 낮춘다 |
| Data-Structures | [Array.md](../Data-Structures/Array.md), [Hash-Table.md](../Data-Structures/Hash-Table.md), [Heap.md](../Data-Structures/Heap.md), [Union-Find.md](../Data-Structures/Union-Find.md) | 내부 표현과 연산 불변식이 알고리즘 구현 품질을 좌우한다 |
| Algorithms | [Complexity.md](../Algorithms/Complexity.md), [DP-Basics.md](../Algorithms/DP-Basics.md), [Dijkstra.md](../Algorithms/Dijkstra.md), [Max-Flow.md](../Algorithms/Max-Flow.md) | 많은 후속 알고리즘 문서의 언어, 증명, 분석 기준을 만든다 |
| Systems | [Virtual-Memory.md](../Systems/Operating-Systems/Virtual-Memory.md), [Transactions-and-ACID.md](../Systems/Databases/Transactions-and-ACID.md), [Consensus.md](../Systems/Distributed-Systems/Consensus.md), [TCP-UDP.md](../Systems/Networks/TCP-UDP.md) | 추상화와 실제 구현 사이의 간극이 크고 오해가 잦다 |
| CS-Theory | [NP-Completeness.md](../CS-Theory/Computation-Theory/NP-Completeness.md), [Type-Systems.md](../CS-Theory/Programming-Languages/Type-Systems.md), [Parser.md](../CS-Theory/Compilers/Parser.md), [Qubits.md](../CS-Theory/Quantum-Computing/Qubits.md) | 형식 정의와 실제 계산/도구 감각을 함께 잡아야 한다 |
| AI | [Backpropagation.md](../AI/Deep-Learning/Backpropagation.md), [Transformer.md](../AI/Deep-Learning/Transformer.md), [RAG.md](../AI/LLMs/RAG.md), [Reproducibility.md](../AI/MLOps/Reproducibility.md) | 수식, 계산 그래프, 실험 실패 모드, 최신 실무 참조가 함께 필요하다 |
| Engineering | [Caching.md](../Engineering/System-Design/Caching.md), [Kubernetes-Basics.md](../Engineering/DevOps/Kubernetes-Basics.md), [Distributed-Tracing.md](../Engineering/DevOps/Distributed-Tracing.md), [Test-Doubles.md](../Engineering/Testing/Test-Doubles.md) | 운영 실패 모드, 설정 예시, 성능·품질 trade-off가 핵심이다 |

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
| `Review` 승격 | 필수 섹션을 채웠고, 독자가 문서 하나로 연습 문제나 구현 과제를 수행할 수 있다 |
| `Complete` 승격 | 사람이 전체 내용을 직접 검토했고 `Reviewed-by`와 검토 배지가 일치한다 |
| `Deep-dive` 유지 | 자기완결성, 메커니즘, 워크드 예제, 실행 가능한 구현, 실패 모드, 참조를 모두 갖춘다 |

## 하지 않을 일

- 품질 바를 만족하지 못한 문서에 `Depth: Deep-dive` 태그만 붙이지 않는다(태그와 내용이 일치해야 한다).
- 길이를 늘리기 위해 배경 설명만 덧붙이지 않는다.
- 외부 자료의 본문, 코드, 표, 문제를 옮겨 깊이를 만든 것처럼 보이게 하지 않는다.
- 빠르게 변하는 제품 사양이나 벤치마크를 검토 날짜 없이 단정하지 않는다.
- 상위 README와 본문 `Status`가 어긋난 채로 남기지 않는다.
