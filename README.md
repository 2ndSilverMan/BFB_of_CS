# Big Book of Computer Science & AI

> BFB_of_CS: CS & AI 공개 지식 저장고

---

## 바로 시작하기

처음이라면 [입문자 로드맵](Roadmaps/Beginner.md)부터 읽는다. 현재 실제 본문이 있는 최소 경로는 다음 순서다.

1. [변수와 타입](Programming/Variables-and-Types.md) → [조건문과 반복문](Programming/Control-Flow.md) → [함수와 재귀](Programming/Functions-and-Recursion.md) → [배열과 문자열](Programming/Arrays-and-Strings.md)
2. [명제 논리와 술어 논리](Math/Discrete/Logic.md)
3. [배열](Data-Structures/Array.md) → [연결 리스트](Data-Structures/Linked-List.md) → [스택](Data-Structures/Stack.md) / [큐](Data-Structures/Queue.md) → [그래프 표현](Data-Structures/Graph-Representation.md)
4. [복잡도 분석](Algorithms/Complexity.md) → [정렬](Algorithms/Sorting.md) → [이진 탐색](Algorithms/Binary-Search.md) → [BFS / DFS](Algorithms/BFS-DFS.md)

특정 언어를 골라 배우려면 공통 프로그래밍 기초 뒤에 [언어 선택 가이드](Programming/Language-Selection.md)와 [언어별 학습 트랙](Programming/Languages/)을 읽는다.

목적이 분명하다면 [학습 로드맵](Roadmaps/)에서 바로 맞는 경로를 고른다.

---

## 현재 읽기 상태

이 저장소는 현재 핵심 학습 경로의 일부 본문을 먼저 열어 둔 상태다. 나머지 주제는 목차와 로드맵으로 준비되어 있으며, 본문이 채워지는 순서는 다음 흐름을 따른다.

1. [입문자 로드맵](Roadmaps/Beginner.md)에 필요한 프로그래밍, 이산수학, 자료구조, 알고리즘 기초
2. [CS 핵심 로드맵](Roadmaps/CS-Core.md)의 시스템, 계산 이론, 보안 기초
3. [AI 핵심 로드맵](Roadmaps/AI-Core.md)의 수학, 머신러닝, 딥러닝 기초

학습할 때는 링크가 걸린 `Draft` 이상 문서를 먼저 읽는다. `Planned`는 아직 본문 파일이 없는 예정 주제다.

| 상태 | 학습자에게 의미 |
|---|---|
| Planned | 목차에만 있는 예정 주제. 아직 읽을 본문은 없다 |
| Stub | 파일은 있지만 골격만 있다 |
| Draft | 지금 읽을 수 있는 초안이다 |
| Review | 본문 작성은 끝났고 검토 중이다 |
| Complete | 완성 문서다 |

---

## 섹션 구성

문서와 목차는 선수지식이 낮은 것에서 높은 것 순으로 배치한다. 학습 시작점은 [Roadmaps/](Roadmaps/)에서 관리한다.

| 섹션 | 내용 |
|---|---|
| [Programming/](Programming/) | 프로그래밍 기초 - 변수, 함수, 재귀, 추상화, Python/JavaScript/C/Java/C++ 언어 입문 |
| [Math/](Math/) | CS와 AI의 수학적 기반 — 이산수학, 선형대수, 확률/통계, 미적분, 최적화 |
| [Data-Structures/](Data-Structures/) | 배열, 연결 리스트, 트리, 그래프, 해시 등 자료 표현 방법 |
| [Algorithms/](Algorithms/) | 정렬, 탐색, DP, 그래프 알고리즘, 알고리즘 설계 기법 |
| [Systems/](Systems/) | 컴퓨터 구조, 운영체제, 네트워크, 데이터베이스, 분산 시스템 |
| [CS-Theory/](CS-Theory/) | 계산 이론, 프로그래밍 언어론, 컴파일러, 양자 컴퓨팅 |
| [AI/](AI/) | 머신러닝, 딥러닝, NLP, 비전, 강화학습, 생성 모델, LLM |
| [Engineering/](Engineering/) | 소프트웨어 설계, 시스템 설계, 테스트, DevOps, 보안, 성능 |

---

## 학습 로드맵

전체 목록은 [Roadmaps/](Roadmaps/)에서 관리한다.

| 로드맵 | 대상 |
|---|---|
| [입문자 (Beginner)](Roadmaps/Beginner.md) | 프로그래밍과 CS를 처음 시작하는 사람 |
| [CS 핵심 (CS Core)](Roadmaps/CS-Core.md) | 컴퓨터공학 전공 핵심을 체계적으로 공부하려는 사람 |
| [AI 핵심 (AI Core)](Roadmaps/AI-Core.md) | AI/ML 전공 지식을 순서대로 공부하려는 사람 |
| [시스템 엔지니어](Roadmaps/Systems-Engineer.md) | OS, 네트워크, DB, 분산 시스템 중심 학습자 |
| [ML 엔지니어](Roadmaps/ML-Engineer.md) | 모델 학습부터 배포까지 다루려는 학습자 |
| [연구자 (Researcher)](Roadmaps/Researcher.md) | 논문과 이론 중심으로 깊게 들어가려는 학습자 |

---

## 참조 자료

용어, 책, 논문, 강의 목록은 [Reference/](Reference/)에서 관리한다.

---

## 작성자용 문서

본문 작성 우선순위, 로드맵 커버리지, 참조 자료 보강, 템플릿, 검수 스크립트는 [Maintainers/](Maintainers/)에서 관리한다.
저작권, 라이선스, 개인정보, 법적 리스크 방지 규칙은 [Legal and Copyright Policy](Maintainers/Legal-and-Copyright-Policy.md)를 따른다.
현재 루트 `LICENSE`는 아직 없으므로 저장소 밖 재사용 조건은 별도로 정해지지 않았다.

---

## 기여

[CONTRIBUTING.md](CONTRIBUTING.md) 참고.
