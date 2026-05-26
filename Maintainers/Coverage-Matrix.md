# 로드맵 커버리지 매트릭스 (Coverage Matrix)

> 목적별 로드맵의 완료 기준을 실제 작성해야 할 문서 단위로 연결한다.

---

## 읽는 법

- 이미 존재하는 `Draft` 이상 문서는 링크로 표시한다.
- 아직 만들지 않은 `Planned` 문서는 파일명만 `code`로 표시한다.
- 이 문서는 "어떤 지식 문서를 채워야 로드맵이 완성되는가"를 판단하기 위한 기준이다.
- 전체 주제 목록은 각 섹션 README가 관리하고, 작성 우선순위는 [Content-Backlog.md](Content-Backlog.md)가 관리한다.
- 핵심 경로 밖의 `Optional`/`Deferred` 주제는 [Topic-Classification.md](Topic-Classification.md)가 관리한다.

---

## 현재 커버리지 요약

아래 표는 현재 README 주제 표 기준이다.

| 영역 | Draft | Planned | 역할 |
|---|---:|---:|---|
| Programming | 4 | 3 | 모든 로드맵의 출발점 |
| Math | 1 | 51 | CS/AI 이론의 공통 기반 |
| Data-Structures | 5 | 12 | 알고리즘과 시스템 구현 기반 |
| Algorithms | 4 | 30 | CS 핵심과 코딩 문제 해결 기반 |
| Systems | 0 | 49 | CS Core, Systems Engineer 기반 |
| CS-Theory | 0 | 30 | 이론/컴파일러/보안 기반 |
| AI | 0 | 191 | AI Core, ML Engineer, Researcher 기반 |
| Engineering | 0 | 105 | 실무 운영, 설계, 품질 기반 |

---

## Beginner

입문자 로드맵은 프로그래밍, 기초 수학, 자료구조, 알고리즘, 시스템 기본 용어까지 연결한다.

| 단계 | 필수 문서 |
|---|---|
| 프로그래밍 | [Variables-and-Types.md](../Programming/Variables-and-Types.md), [Control-Flow.md](../Programming/Control-Flow.md), [Functions-and-Recursion.md](../Programming/Functions-and-Recursion.md), [Arrays-and-Strings.md](../Programming/Arrays-and-Strings.md) |
| 이산수학 | [Logic.md](../Math/Discrete/Logic.md), `Induction.md`, `Graph-Theory.md` |
| 자료구조 | [Array.md](../Data-Structures/Array.md), [Linked-List.md](../Data-Structures/Linked-List.md), [Stack.md](../Data-Structures/Stack.md), [Queue.md](../Data-Structures/Queue.md), [Graph-Representation.md](../Data-Structures/Graph-Representation.md), `Binary-Tree.md`, `Hash-Table.md` |
| 알고리즘 | [Complexity.md](../Algorithms/Complexity.md), [Sorting.md](../Algorithms/Sorting.md), [Binary-Search.md](../Algorithms/Binary-Search.md), [BFS-DFS.md](../Algorithms/BFS-DFS.md), `DP-Basics.md` |
| 시스템 맛보기 | `Data-Representation.md`, `Processes-and-Threads.md`, `Network-Models.md`, `Relational-Model-and-SQL.md` |

---

## CS Core

CS 핵심 로드맵은 전공 필수 흐름을 완성하는 기준이다.

| 단계 | 필수 문서 |
|---|---|
| 프로그래밍 | Beginner 필수 문서 + `Pointers-and-Memory.md`, `OOP.md`, `Functional-Intro.md` |
| 수학 | `Set-Theory.md`, `Relations-and-Functions.md`, `Induction.md`, `Graph-Theory.md`, `Recurrences.md`, `Number-Theory-Basics.md` |
| 자료구조 | Beginner 필수 문서 + `BST.md`, `Heap.md`, `Union-Find.md`, `Hash-Function.md` |
| 알고리즘 | Beginner 필수 문서 + `Divide-and-Conquer.md`, `Greedy.md`, `Backtracking.md`, `Topological-Sort.md`, `Dijkstra.md`, `MST.md`, `Amortized-Analysis.md` |
| 컴퓨터 구조 | `Digital-Logic.md`, `Data-Representation.md`, `CPU-and-ISA.md`, `Pipelining.md`, `Memory-Hierarchy.md`, `IO-Systems.md` |
| 운영체제 | `Processes-and-Threads.md`, `Scheduling.md`, `Synchronization.md`, `Deadlock.md`, `Memory-Management.md`, `Virtual-Memory.md`, `File-Systems.md` |
| 네트워크 | `Network-Models.md`, `IP-and-Routing.md`, `TCP-UDP.md`, `HTTP.md`, `DNS.md`, `Socket-Programming.md` |
| 데이터베이스 | `Relational-Model-and-SQL.md`, `Database-Normalization.md`, `Indexes-and-B-Tree.md`, `Transactions-and-ACID.md`, `Concurrency-Control.md`, `Query-Optimization.md` |
| 분산 시스템 | `System-Models.md`, `CAP-Theorem.md`, `Consensus.md`, `Replication.md`, `Partitioning.md`, `Time-and-Ordering.md` |
| 계산 이론 | `Regular-Languages.md`, `Regular-Expressions.md`, `Context-Free.md`, `Turing-Machine.md`, `Undecidability.md`, `Complexity-Classes.md`, `NP-Completeness.md` |
| PL/컴파일러 | `Syntax-and-Semantics.md`, `Type-Systems.md`, `Lambda-Calculus.md`, `Lexer.md`, `Parser.md`, `AST.md`, `Intermediate-Representation.md`, `Code-Generation.md` |
| 보안 | `Symmetric-Encryption.md`, `Asymmetric-Encryption.md`, `Hash-Functions.md`, `Digital-Signatures.md`, `PKI-and-TLS.md`, `Auth.md`, `Web-Security.md` |

---

## AI Core

AI 핵심 로드맵은 수학 기초에서 머신러닝, 딥러닝, 주요 응용 분야까지 이어지는 기준이다.

| 단계 | 필수 문서 |
|---|---|
| 선형대수 | `Vectors.md`, `Matrices.md`, `Linear-Systems.md`, `Eigenvalues.md`, `SVD.md`, `PCA.md`, `Orthogonality.md` |
| 미적분 | `Limits.md`, `Differentiation.md`, `Partial-Derivatives.md`, `Chain-Rule.md`, `Taylor-Series.md` |
| 확률/통계 | `Probability-Basics.md`, `Distributions.md`, `Expectation.md`, `Bayes-Theorem.md`, `MLE.md`, `CLT.md`, `Hypothesis-Testing.md`, `Information-Theory.md` |
| 최적화 | `Convex-Optimization.md`, `Gradient-Descent.md`, `SGD.md`, `Adaptive-Methods.md`, `Lagrangian.md` |
| 머신러닝 | `Linear-Regression.md`, `Logistic-Regression.md`, `Decision-Trees.md`, `Ensemble.md`, `KNN.md`, `K-Means.md`, `Dimensionality-Reduction.md`, `Bias-Variance.md`, `Cross-Validation.md`, `Regularization.md`, `Overfitting.md` |
| 딥러닝 | `MLP.md`, `Backpropagation.md`, `Activation-Functions.md`, `Loss-Functions.md`, `Normalization-Layers.md`, `Dropout.md`, `CNN.md`, `RNN-LSTM-GRU.md`, `Attention.md`, `Transformer.md`, `Transfer-Learning.md`, `Fine-Tuning.md` |
| NLP/LLM | `Text-Preprocessing.md`, `Language-Model-Basics.md`, `Word-Embeddings.md`, `Transformer-NLP.md`, `BERT.md`, `GPT.md`, `Transformer-Advanced.md`, `Pretraining.md`, `Instruction-Tuning.md`, `Prompt-Engineering.md`, `RAG.md` |
| 비전/생성/RL | `Image-Basics.md`, `CNN-Deep-Dive.md`, `Image-Classification.md`, `Object-Detection.md`, `Autoencoders.md`, `VAE.md`, `GAN-Basics.md`, `DDPM.md`, `MDP.md`, `Value-Functions.md`, `Policy.md`, `TD-Learning.md`, `Policy-Gradient.md` |
| 운영 | `Experiment-Tracking.md`, `Reproducibility.md`, `Data-Versioning.md`, `Online-vs-Batch-Serving.md`, `REST-Serving.md`, `Model-Optimization.md`, `Data-Drift.md`, `Model-Monitoring.md`, `ML-Pipeline.md` |

---

## Systems Engineer

시스템 엔지니어 로드맵은 시스템 내부 동작과 운영 실무를 함께 완성하는 기준이다.

| 단계 | 필수 문서 |
|---|---|
| 시스템 기반 | CS Core의 컴퓨터 구조, 운영체제, 네트워크, 데이터베이스, 분산 시스템 필수 문서 |
| 병렬 컴퓨팅 | `Parallel-Models.md`, `Multithreading.md`, `SIMD.md`, `GPU-and-CUDA.md`, `OpenMP-MPI.md`, `Parallel-Scalability.md` |
| 성능 공학 | `Benchmarking-Basics.md`, `CPU-Profiling.md`, `Memory-Profiling.md`, `IO-Profiling.md`, `Flame-Graphs.md`, `Cache-Friendly-Code.md`, `Lock-Contention.md`, `Async-IO.md`, `Database-Query-Optimization.md`, `Network-Performance.md` |
| DevOps | `Git-Basics.md`, `CICD-Principles.md`, `GitHub-Actions.md`, `Deployment-Strategies.md`, `Docker-Basics.md`, `Kubernetes-Basics.md`, `Cloud-Computing.md`, `Terraform-Basics.md`, `Metrics-Alerts.md`, `Distributed-Tracing.md`, `SLI-SLO-SLA.md` |
| 시스템 설계 | `Approach.md`, `Scalability.md`, `Load-Balancing.md`, `Caching.md`, `Database-Design.md`, `Message-Queues.md`, `Microservices.md`, `System-Design-Case-Studies.md` |

---

## ML Engineer

ML 엔지니어 로드맵은 모델 학습, 실험 관리, 서빙, 배포를 하나의 흐름으로 연결한다.

| 단계 | 필수 문서 |
|---|---|
| 모델 기반 | AI Core의 수학, 머신러닝, 딥러닝 필수 문서 |
| 생성/LLM | `VAE.md`, `GAN-Basics.md`, `DDPM.md`, `Latent-Diffusion.md`, `Transformer-Advanced.md`, `GPT-Family.md`, `Pretraining.md`, `Instruction-Tuning.md`, `PEFT.md`, `RAG.md`, `Inference-Optimization.md` |
| MLOps | `Experiment-Tracking.md`, `Hyperparameter-Tuning.md`, `Reproducibility.md`, `Data-Versioning.md`, `Feature-Store.md`, `Data-Validation.md`, `Online-vs-Batch-Serving.md`, `REST-Serving.md`, `Model-Optimization.md`, `AB-Testing.md`, `Data-Drift.md`, `Model-Monitoring.md`, `Feedback-Loop.md`, `ML-Pipeline.md`, `Distributed-Training.md`, `Model-Registry.md` |
| 운영 인프라 | `Docker-Basics.md`, `Kubernetes-Basics.md`, `Cloud-Computing.md`, `Metrics-Alerts.md`, `Distributed-Tracing.md`, `Approach.md`, `Caching.md`, `Message-Queues.md` |

---

## Researcher

연구자 로드맵은 논문 독해와 이론적 분석을 위한 기준이다.

| 단계 | 필수 문서 |
|---|---|
| 수학 이론 | `Real-Numbers.md`, `Sequences-Series.md`, `Continuity.md`, `Uniform-Continuity.md`, `Measure-Theory.md`, `Function-Spaces.md`, `Information-Theory.md`, `Convex-Optimization.md` |
| 계산 이론 | `Complexity-Classes.md`, `NP-Completeness.md`, `Undecidability.md` |
| 이론적 ML | `PAC-Learning.md`, `VC-Dimension.md`, `Shattering.md`, `No-Free-Lunch.md`, `Rademacher-Complexity.md`, `Generalization-Bounds.md`, `Double-Descent.md`, `Convex-Learning.md`, `GD-Convergence.md`, `Implicit-Regularization.md`, `Regret-Minimization.md`, `Multi-Armed-Bandit.md` |
| PGM/인과 | `Factorization.md`, `Bayesian-Networks.md`, `d-Separation.md`, `MRF.md`, `Variable-Elimination.md`, `Belief-Propagation.md`, `Variational-Inference.md`, `MCMC.md`, `Potential-Outcomes.md`, `SCM.md`, `Causal-DAG.md`, `Do-Calculus.md`, `Identifiability.md`, `Counterfactual.md` |
| 안전성/해석 | `Alignment-Overview.md`, `Reward-Hacking.md`, `RLHF-Constitutional-AI.md`, `Mechanistic-Interpretability.md`, `Activation-Patching.md`, `Sparse-Autoencoder.md`, `Adversarial-Examples.md`, `OOD-Generalization.md`, `Capability-Evaluation.md`, `Red-Teaming.md`, `Scalable-Oversight.md`, `AI-Regulation.md` |

---

## 완료 판정

프로젝트 전체가 "본문만 채우면 되는 상태"를 유지하려면 다음 조건을 만족해야 한다.

- 새 주제는 먼저 섹션 README의 `Planned` 행으로 등록한다.
- 특정 로드맵 완료 기준에 필요한 주제는 이 문서의 해당 로드맵 표에도 반영한다.
- 실제 파일을 만들면 상위 README의 `Status`와 문서 상단 `Status`를 함께 변경한다.
- `Review` 이상으로 올릴 때는 개념, 직관, 이론, 구현/예시, 복잡도/한계, 응용, 흔한 오해, 연습 문제, 이어서 읽기, 참조를 채운다.
- 빠르게 변하는 분야는 `Last reviewed` 날짜를 유지한다.
