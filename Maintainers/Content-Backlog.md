# 콘텐츠 작성 백로그 (Content Backlog)

> 전체 프로젝트를 실제 지식 문서 작성 단계로 전환하기 위한 우선순위.

---

## 현재 범위

아래 표는 현재 README 주제 표를 요약한 것이다.  
이 문서는 예정 문서를 한 번에 모두 나열하기보다, 어떤 순서로 핵심 학습 경로를 열어야 하는지 관리한다.

전체 로드맵별 필수 문서 매핑은 [Coverage-Matrix.md](Coverage-Matrix.md)를 따른다.
핵심 경로 밖의 `Optional`/`Deferred` 주제 분류는 [Topic-Classification.md](Topic-Classification.md)를 따른다.

| 영역 | 현재 Draft | Review | 남은 Planned | 우선 역할 |
|---|---:|---:|---:|---|
| Programming | 3 | 2 | 28 | 모든 로드맵의 출발점 |
| Math | 1 | 0 | 51 | CS/AI 공통 기반 |
| Data-Structures | 5 | 0 | 12 | 알고리즘과 시스템 구현 기반 |
| Algorithms | 2 | 2 | 30 | 문제 해결과 전공 핵심 기반 |
| Systems | 0 | 0 | 54 | CS Core, Systems Engineer 기반 |
| CS-Theory | 0 | 0 | 30 | 계산 이론, PL, 컴파일러 기반 |
| AI | 0 | 0 | 191 | AI Core, ML Engineer, Researcher 기반 |
| Engineering | 0 | 0 | 112 | 실무 설계, 운영, 품질 기반 |

---

## 우선순위 기준

- `P0`: 이미 작성된 읽기 가능한 최소 경로.
- `P1`: 입문자 최종 완료 기준 중 비시스템 기초를 채우는 문서.
- `P1.5`: 입문자 최종 완료 기준 중 시스템 맛보기를 채우는 최소 문서.
- `P2`: CS Core로 들어가기 위한 시스템/이론 최소 문서.
- `P3`: AI Core로 들어가기 위한 수학/ML 최소 문서.
- `P4`: CS Core 전공 흐름을 완성하는 문서.
- `P5`: AI Core 모델 흐름을 완성하는 문서.
- `P6`: Systems Engineer와 ML Engineer 실무 흐름을 완성하는 문서.
- `P7`: Researcher와 심화 이론 흐름을 완성하는 문서.

---

## P0: 작성됨

| 섹션 | 파일 | 상태 |
|---|---|---|
| Programming | [Variables-and-Types.md](../Programming/Variables-and-Types.md) | Review |
| Programming | [Control-Flow.md](../Programming/Control-Flow.md) | Draft |
| Programming | [Functions-and-Recursion.md](../Programming/Functions-and-Recursion.md) | Draft |
| Programming | [Arrays-and-Strings.md](../Programming/Arrays-and-Strings.md) | Draft |
| Programming | [Language-Selection.md](../Programming/Language-Selection.md) | Review |
| Math/Discrete | [Logic.md](../Math/Discrete/Logic.md) | Draft |
| Data-Structures | [Array.md](../Data-Structures/Array.md) | Draft |
| Data-Structures | [Linked-List.md](../Data-Structures/Linked-List.md) | Draft |
| Data-Structures | [Stack.md](../Data-Structures/Stack.md) | Draft |
| Data-Structures | [Queue.md](../Data-Structures/Queue.md) | Draft |
| Data-Structures | [Graph-Representation.md](../Data-Structures/Graph-Representation.md) | Draft |
| Algorithms | [Complexity.md](../Algorithms/Complexity.md) | Draft |
| Algorithms | [Sorting.md](../Algorithms/Sorting.md) | Review |
| Algorithms | [Binary-Search.md](../Algorithms/Binary-Search.md) | Draft |
| Algorithms | [BFS-DFS.md](../Algorithms/BFS-DFS.md) | Review |

## P1: 입문자 비시스템 기초 보강

| 섹션 | 파일 | 이유 |
|---|---|---|
| Data-Structures | `Binary-Tree.md` | 트리 계열과 재귀 구조의 공통 기반 |
| Data-Structures | `Hash-Table.md` | 평균 O(1) 탐색과 해시 기반 자료구조 |
| Algorithms | `DP-Basics.md` | 입문자 최종 완료 기준의 기본 DP |
| Math/Discrete | `Induction.md` | 알고리즘 정당성 증명의 기본 |
| Math/Discrete | `Graph-Theory.md` | 그래프 알고리즘 이해 보강 |

## P1.5: 입문자 시스템 맛보기

이 문서들은 CS Core의 시스템 파트로도 이어지지만, 입문자 로드맵의 최종 완료 기준에 직접 들어간다. P1 비시스템 기초 문서 직후에 최소 본문을 먼저 열어 둔다.

| 섹션 | 파일 | 이유 |
|---|---|---|
| Systems/Computer-Architecture | `Data-Representation.md` | 이진수, 정수, 부동소수점 표현 |
| Systems/Operating-Systems | `Processes-and-Threads.md` | 프로세스, 스레드, 메모리 용어의 시작점 |
| Systems/Networks | `Network-Models.md` | TCP/IP 같은 네트워크 기본 용어의 뼈대 |
| Systems/Databases | `Relational-Model-and-SQL.md` | SQL과 트랜잭션 학습의 입구 |

## P2: CS Core 진입 보강

| 섹션 | 파일 | 이유 |
|---|---|---|
| Systems/Computer-Architecture | `CPU-and-ISA.md` | 프로그램이 하드웨어에서 실행되는 흐름 |
| Systems/Operating-Systems | `Memory-Management.md` | 메모리 추상화 이해 |
| Systems/Networks | `TCP-UDP.md` | 전송 계층의 핵심 |
| Systems/Databases | `Transactions-and-ACID.md` | 데이터 일관성의 핵심 |
| CS-Theory/Computation-Theory | `Regular-Languages.md` | 계산 이론 시작점 |

## P3: AI Core 진입 보강

| 섹션 | 파일 | 이유 |
|---|---|---|
| Math/Calculus | `Differentiation.md` | 역전파와 최적화의 최소 미적분 |
| Math/Calculus | `Chain-Rule.md` | 역전파의 수학적 핵심 |
| Math/Linear-Algebra | `Vectors.md` | ML 입력과 파라미터 표현의 시작점 |
| Math/Linear-Algebra | `Matrices.md` | 배치 계산과 선형 변환의 기반 |
| Math/Probability-Statistics | `Probability-Basics.md` | 확률 모델과 평가 지표의 기반 |
| Math/Probability-Statistics | `Expectation.md` | 손실과 기대 위험 이해 |
| Math/Optimization | `Gradient-Descent.md` | 머신러닝 학습의 핵심 절차 |
| AI/Machine-Learning | `Linear-Regression.md` | AI 경로의 첫 모델 문서 |
| AI/Machine-Learning | `Logistic-Regression.md` | 분류 모델의 기본 |

## P4: CS Core 완성 경로

| 묶음 | 우선 문서 |
|---|---|
| 자료구조 확장 | `BST.md`, `Heap.md`, `Union-Find.md`, `Hash-Function.md` |
| 알고리즘 확장 | `Divide-and-Conquer.md`, `Greedy.md`, `Backtracking.md`, `Topological-Sort.md`, `Dijkstra.md`, `MST.md` |
| 운영체제 | `Scheduling.md`, `Synchronization.md`, `Deadlock.md`, `Virtual-Memory.md`, `File-Systems.md` |
| 데이터베이스 | `Database-Normalization.md`, `Indexes-and-B-Tree.md`, `Concurrency-Control.md`, `Query-Optimization.md` |
| 분산 시스템 | `System-Models.md`, `CAP-Theorem.md`, `Consensus.md`, `Replication.md`, `Partitioning.md` |
| 계산 이론 | `Regular-Expressions.md`, `Context-Free.md`, `Turing-Machine.md`, `Undecidability.md`, `Complexity-Classes.md`, `NP-Completeness.md` |
| PL/컴파일러 | `Syntax-and-Semantics.md`, `Type-Systems.md`, `Lambda-Calculus.md`, `Lexer.md`, `Parser.md`, `AST.md` |
| 보안 | `Symmetric-Encryption.md`, `Asymmetric-Encryption.md`, `Hash-Functions.md`, `Digital-Signatures.md`, `PKI-and-TLS.md`, `Auth.md`, `Web-Security.md` |

## P5: AI Core 완성 경로

| 묶음 | 우선 문서 |
|---|---|
| 선형대수 | `Linear-Systems.md`, `Eigenvalues.md`, `SVD.md`, `PCA.md`, `Orthogonality.md` |
| 확률/통계 | `Distributions.md`, `Bayes-Theorem.md`, `MLE.md`, `CLT.md`, `Hypothesis-Testing.md`, `Information-Theory.md` |
| 최적화 | `Convex-Optimization.md`, `SGD.md`, `Adaptive-Methods.md`, `Lagrangian.md` |
| 머신러닝 | `Decision-Trees.md`, `Ensemble.md`, `KNN.md`, `K-Means.md`, `Dimensionality-Reduction.md`, `Bias-Variance.md`, `Cross-Validation.md`, `Regularization.md`, `Overfitting.md` |
| 딥러닝 | `MLP.md`, `Backpropagation.md`, `Activation-Functions.md`, `Loss-Functions.md`, `Normalization-Layers.md`, `Dropout.md`, `CNN.md`, `Attention.md`, `Transformer.md` |
| 응용 AI | `Language-Model-Basics.md`, `Word-Embeddings.md`, `BERT.md`, `GPT.md`, `Image-Basics.md`, `Image-Classification.md`, `MDP.md`, `TD-Learning.md`, `VAE.md`, `GAN-Basics.md`, `DDPM.md` |

## P6: 실무/운영 경로

| 로드맵 | 우선 문서 |
|---|---|
| Systems Engineer | `Parallel-Models.md`, `Multithreading.md`, `Benchmarking-Basics.md`, `CPU-Profiling.md`, `Cache-Friendly-Code.md`, `Docker-Basics.md`, `Kubernetes-Basics.md`, `Metrics-Alerts.md`, `Approach.md`, `Scalability.md`, `Caching.md` |
| ML Engineer | `Experiment-Tracking.md`, `Reproducibility.md`, `Data-Versioning.md`, `REST-Serving.md`, `Model-Optimization.md`, `AB-Testing.md`, `Data-Drift.md`, `Model-Monitoring.md`, `ML-Pipeline.md`, `Distributed-Training.md`, `Model-Registry.md` |
| Software Engineering | `SOLID.md`, `Clean-Code.md`, `Refactoring.md`, `Testing-Pyramid.md`, `Unit-Test-Principles.md`, `Integration-Test-Strategy.md`, `Scientific-Debugging.md`, `Stack-Traces.md`, `Structured-Logging.md` |

## P7: 연구/심화 경로

| 묶음 | 우선 문서 |
|---|---|
| 수학 심화 | `Real-Numbers.md`, `Sequences-Series.md`, `Continuity.md`, `Measure-Theory.md`, `Function-Spaces.md` |
| 이론적 ML | `PAC-Learning.md`, `VC-Dimension.md`, `Rademacher-Complexity.md`, `Generalization-Bounds.md`, `Double-Descent.md`, `GD-Convergence.md`, `Regret-Minimization.md` |
| PGM/인과 | `Bayesian-Networks.md`, `d-Separation.md`, `Variable-Elimination.md`, `Belief-Propagation.md`, `MCMC.md`, `Potential-Outcomes.md`, `SCM.md`, `Do-Calculus.md`, `Identifiability.md` |
| AI Safety | `Alignment-Overview.md`, `Reward-Hacking.md`, `RLHF-Constitutional-AI.md`, `Mechanistic-Interpretability.md`, `Sparse-Autoencoder.md`, `Adversarial-Examples.md`, `Capability-Evaluation.md`, `Red-Teaming.md` |
| 고급 알고리즘/이론 | `Max-Flow.md`, `Bipartite-Matching.md`, `KMP.md`, `Number-Theory.md`, `Approximation-Algorithms.md`, `Randomized-Algorithms.md`, `Qubits.md` |

---

## 승격 순서

1. 이 백로그 또는 [Coverage-Matrix.md](Coverage-Matrix.md)에서 다음 작성 대상을 고른다.
2. 상위 README의 `Planned` 행을 확인한다.
3. 실제 파일을 만들고 `Status: Draft`를 둔다.
4. 상위 README의 해당 행을 `Draft`로 바꾼다.
5. `python Maintainers/Scripts/sync_summary_counts.py`로 요약 수치를 맞춘 뒤 `python Maintainers/Scripts/validate_docs.py`를 실행한다.
6. 개념, 직관, 이론, 구현/예시, 복잡도/한계, 응용, 흔한 오해, 연습 문제, 이어서 읽기, 참조가 충분하면 `Review`로 올린다.
7. 핵심 경로 밖의 주제는 [Topic-Classification.md](Topic-Classification.md)의 `Optional` 또는 `Deferred` 분류를 확인한다.
