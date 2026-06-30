# 콘텐츠 작성 백로그 (Content Backlog)

> 전체 프로젝트를 실제 지식 문서 작성 단계로 전환하기 위한 우선순위.

---

## 현재 범위

아래 표는 현재 README 주제 표를 요약한 것이다.  
이 문서는 예정 문서를 한 번에 모두 나열하기보다, 어떤 순서로 핵심 학습 경로를 열어야 하는지 관리한다.

전체 로드맵별 필수 문서 매핑은 [Coverage-Matrix.md](Coverage-Matrix.md)를 따른다.
핵심 경로 밖의 `Optional`/`Deferred` 주제 분류는 [Topic-Classification.md](Topic-Classification.md)를 따른다.
기존 문서를 더 깊게 만들거나 `Deep-dive` 후보를 고를 때는 [Documentation-Depth-Plan.md](Documentation-Depth-Plan.md)를 따른다.

| 영역 | 현재 Draft | Review | 남은 Planned | 우선 역할 |
|---|---:|---:|---:|---|
| Programming | 31 | 2 | 0 | 모든 로드맵의 출발점 |
| Math | 52 | 0 | 0 | CS/AI 공통 기반 |
| Data-Structures | 17 | 0 | 0 | 알고리즘과 시스템 구현 기반 |
| Algorithms | 32 | 2 | 0 | 문제 해결과 전공 핵심 기반 |
| Systems | 54 | 0 | 0 | CS Core, Systems Engineer 기반 |
| CS-Theory | 30 | 0 | 0 | 계산 이론, PL, 컴파일러 기반 |
| AI | 191 | 0 | 0 | AI Core, ML Engineer, Researcher 기반 |
| Engineering | 113 | 0 | 0 | 실무 설계, 운영, 품질 기반 |

---

## 우선순위 기준

여기서 `P0`-`P7`은 장애 심각도가 아니라 **작성 백로그 우선순위**다. 숫자가 낮을수록 먼저 안정화할 학습 경로다.

- `P0`: 이미 작성된 읽기 가능한 최소 경로. 새 주제 추가보다 먼저 정확성, 사람 검토, 참조를 안정화한다.
- `P1`: 입문자 최종 완료 기준 중 비시스템 기초를 채우는 문서.
- `P1.5`: 입문자 최종 완료 기준 중 시스템 맛보기를 채우는 최소 문서.
- `P2`: CS Core로 들어가기 위한 시스템/이론 최소 문서.
- `P3`: AI Core로 들어가기 위한 수학/ML 최소 문서.
- `P4`: CS Core 전공 흐름을 완성하는 문서.
- `P5`: AI Core 모델 흐름을 완성하는 문서.
- `P6`: Systems Engineer와 ML Engineer 실무 흐름을 완성하는 문서.
- `P7`: Researcher와 심화 이론 흐름을 완성하는 문서.

현재 P0-P3의 대상 파일은 모두 본문이 열려 있다. 다음 신규 작성 작업은 P4/P5 이후에서 고르고, P0-P3은 정확성 검토와 참조 보강을 통해 `Review`로 승격한다.

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

## P1: 입문자 비시스템 기초 보강 - 작성됨

| 섹션 | 파일 | 상태 | 이유 |
|---|---|---|---|
| Data-Structures | [Binary-Tree.md](../Data-Structures/Binary-Tree.md) | Draft | 트리 계열과 재귀 구조의 공통 기반 |
| Data-Structures | [Hash-Table.md](../Data-Structures/Hash-Table.md) | Draft | 평균 O(1) 탐색과 해시 기반 자료구조 |
| Algorithms | [DP-Basics.md](../Algorithms/DP-Basics.md) | Draft | 입문자 최종 완료 기준의 기본 DP |
| Math/Discrete | [Induction.md](../Math/Discrete/Induction.md) | Draft | 알고리즘 정당성 증명의 기본 |
| Math/Discrete | [Graph-Theory.md](../Math/Discrete/Graph-Theory.md) | Draft | 그래프 알고리즘 이해 보강 |

## P1.5: 입문자 시스템 맛보기 - 작성됨

이 문서들은 CS Core의 시스템 파트로도 이어지지만, 입문자 로드맵의 최종 완료 기준에 직접 들어간다. P1 비시스템 기초 문서 직후에 최소 본문을 먼저 열어 둔다.

| 섹션 | 파일 | 상태 | 이유 |
|---|---|---|---|
| Systems/Computer-Architecture | [Data-Representation.md](../Systems/Computer-Architecture/Data-Representation.md) | Draft | 이진수, 정수, 부동소수점 표현 |
| Systems/Operating-Systems | [Processes-and-Threads.md](../Systems/Operating-Systems/Processes-and-Threads.md) | Draft | 프로세스, 스레드, 메모리 용어의 시작점 |
| Systems/Networks | [Network-Models.md](../Systems/Networks/Network-Models.md) | Draft | TCP/IP 같은 네트워크 기본 용어의 뼈대 |
| Systems/Databases | [Relational-Model-and-SQL.md](../Systems/Databases/Relational-Model-and-SQL.md) | Draft | SQL과 트랜잭션 학습의 입구 |

## P2: CS Core 진입 보강 - 작성됨

| 섹션 | 파일 | 상태 | 이유 |
|---|---|---|---|
| Systems/Computer-Architecture | [CPU-and-ISA.md](../Systems/Computer-Architecture/CPU-and-ISA.md) | Draft | 프로그램이 하드웨어에서 실행되는 흐름 |
| Systems/Operating-Systems | [Memory-Management.md](../Systems/Operating-Systems/Memory-Management.md) | Draft | 메모리 추상화 이해 |
| Systems/Networks | [TCP-UDP.md](../Systems/Networks/TCP-UDP.md) | Draft | 전송 계층의 핵심 |
| Systems/Databases | [Transactions-and-ACID.md](../Systems/Databases/Transactions-and-ACID.md) | Draft | 데이터 일관성의 핵심 |
| CS-Theory/Computation-Theory | [Regular-Languages.md](../CS-Theory/Computation-Theory/Regular-Languages.md) | Draft | 계산 이론 시작점 |

## P3: AI Core 진입 보강 - 작성됨

| 섹션 | 파일 | 상태 | 이유 |
|---|---|---|---|
| Math/Calculus | [Differentiation.md](../Math/Calculus/Differentiation.md) | Draft | 역전파와 최적화의 최소 미적분 |
| Math/Calculus | [Chain-Rule.md](../Math/Calculus/Chain-Rule.md) | Draft | 역전파의 수학적 핵심 |
| Math/Linear-Algebra | [Vectors.md](../Math/Linear-Algebra/Vectors.md) | Draft | ML 입력과 파라미터 표현의 시작점 |
| Math/Linear-Algebra | [Matrices.md](../Math/Linear-Algebra/Matrices.md) | Draft | 배치 계산과 선형 변환의 기반 |
| Math/Probability-Statistics | [Probability-Basics.md](../Math/Probability-Statistics/Probability-Basics.md) | Draft | 확률 모델과 평가 지표의 기반 |
| Math/Probability-Statistics | [Expectation.md](../Math/Probability-Statistics/Expectation.md) | Draft | 손실과 기대 위험 이해 |
| Math/Optimization | [Gradient-Descent.md](../Math/Optimization/Gradient-Descent.md) | Draft | 머신러닝 학습의 핵심 절차 |
| AI/Machine-Learning | [Linear-Regression.md](../AI/Machine-Learning/Linear-Regression.md) | Draft | AI 경로의 첫 모델 문서 |
| AI/Machine-Learning | [Logistic-Regression.md](../AI/Machine-Learning/Logistic-Regression.md) | Draft | 분류 모델의 기본 |

## P4: CS Core 완성 경로

| 묶음 | 우선 문서 |
|---|---|
| 자료구조 확장 | [BST.md](../Data-Structures/BST.md), [Heap.md](../Data-Structures/Heap.md), [Union-Find.md](../Data-Structures/Union-Find.md), [Hash-Function.md](../Data-Structures/Hash-Function.md) (작성됨, Draft) |
| 알고리즘 확장 | [Divide-and-Conquer.md](../Algorithms/Divide-and-Conquer.md), [Greedy.md](../Algorithms/Greedy.md), [Backtracking.md](../Algorithms/Backtracking.md), [Topological-Sort.md](../Algorithms/Topological-Sort.md), [Dijkstra.md](../Algorithms/Dijkstra.md), [MST.md](../Algorithms/MST.md) (작성됨, Draft) |
| 운영체제 | [Scheduling.md](../Systems/Operating-Systems/Scheduling.md), [Synchronization.md](../Systems/Operating-Systems/Synchronization.md), [Deadlock.md](../Systems/Operating-Systems/Deadlock.md), [Virtual-Memory.md](../Systems/Operating-Systems/Virtual-Memory.md), [File-Systems.md](../Systems/Operating-Systems/File-Systems.md) (작성됨, Draft) |
| 데이터베이스 | [Database-Normalization.md](../Systems/Databases/Database-Normalization.md), [Indexes-and-B-Tree.md](../Systems/Databases/Indexes-and-B-Tree.md), [Concurrency-Control.md](../Systems/Databases/Concurrency-Control.md), [Query-Optimization.md](../Systems/Databases/Query-Optimization.md) (작성됨, Draft) |
| 분산 시스템 | [System-Models.md](../Systems/Distributed-Systems/System-Models.md), [CAP-Theorem.md](../Systems/Distributed-Systems/CAP-Theorem.md), [Consensus.md](../Systems/Distributed-Systems/Consensus.md), [Replication.md](../Systems/Distributed-Systems/Replication.md), [Partitioning.md](../Systems/Distributed-Systems/Partitioning.md) (작성됨, Draft) |
| 계산 이론 | [Regular-Expressions.md](../CS-Theory/Computation-Theory/Regular-Expressions.md), [Context-Free.md](../CS-Theory/Computation-Theory/Context-Free.md), [Turing-Machine.md](../CS-Theory/Computation-Theory/Turing-Machine.md), [Undecidability.md](../CS-Theory/Computation-Theory/Undecidability.md), [Complexity-Classes.md](../CS-Theory/Computation-Theory/Complexity-Classes.md), [NP-Completeness.md](../CS-Theory/Computation-Theory/NP-Completeness.md) (작성됨, Draft) |
| PL/컴파일러 | [Syntax-and-Semantics.md](../CS-Theory/Programming-Languages/Syntax-and-Semantics.md), [Type-Systems.md](../CS-Theory/Programming-Languages/Type-Systems.md), [Lambda-Calculus.md](../CS-Theory/Programming-Languages/Lambda-Calculus.md), [Lexer.md](../CS-Theory/Compilers/Lexer.md), [Parser.md](../CS-Theory/Compilers/Parser.md), [AST.md](../CS-Theory/Compilers/AST.md) (작성됨, Draft) |
| 보안 | [Symmetric-Encryption.md](../Engineering/Security/Symmetric-Encryption.md), [Asymmetric-Encryption.md](../Engineering/Security/Asymmetric-Encryption.md), [Hash-Functions.md](../Engineering/Security/Hash-Functions.md), [Digital-Signatures.md](../Engineering/Security/Digital-Signatures.md), [PKI-and-TLS.md](../Engineering/Security/PKI-and-TLS.md), [Auth.md](../Engineering/Security/Auth.md), [Web-Security.md](../Engineering/Security/Web-Security.md) (작성됨, Draft) |

## P5: AI Core 완성 경로

| 묶음 | 우선 문서 |
|---|---|
| 선형대수 | [Linear-Systems.md](../Math/Linear-Algebra/Linear-Systems.md), [Eigenvalues.md](../Math/Linear-Algebra/Eigenvalues.md), [SVD.md](../Math/Linear-Algebra/SVD.md), [PCA.md](../Math/Linear-Algebra/PCA.md), [Orthogonality.md](../Math/Linear-Algebra/Orthogonality.md) (작성됨, Draft) |
| 확률/통계 | [Distributions.md](../Math/Probability-Statistics/Distributions.md), [Bayes-Theorem.md](../Math/Probability-Statistics/Bayes-Theorem.md), [MLE.md](../Math/Probability-Statistics/MLE.md), [CLT.md](../Math/Probability-Statistics/CLT.md), [Hypothesis-Testing.md](../Math/Probability-Statistics/Hypothesis-Testing.md), [Information-Theory.md](../Math/Probability-Statistics/Information-Theory.md) (작성됨, Draft) |
| 최적화 | [Convex-Optimization.md](../Math/Optimization/Convex-Optimization.md), [SGD.md](../Math/Optimization/SGD.md), [Adaptive-Methods.md](../Math/Optimization/Adaptive-Methods.md), [Lagrangian.md](../Math/Optimization/Lagrangian.md) (작성됨, Draft) |
| 머신러닝 | [Decision-Trees.md](../AI/Machine-Learning/Decision-Trees.md), [Ensemble.md](../AI/Machine-Learning/Ensemble.md), [KNN.md](../AI/Machine-Learning/KNN.md), [K-Means.md](../AI/Machine-Learning/K-Means.md), [Dimensionality-Reduction.md](../AI/Machine-Learning/Dimensionality-Reduction.md), [Bias-Variance.md](../AI/Machine-Learning/Bias-Variance.md), [Cross-Validation.md](../AI/Machine-Learning/Cross-Validation.md), [Regularization.md](../AI/Machine-Learning/Regularization.md), [Overfitting.md](../AI/Machine-Learning/Overfitting.md) (작성됨, Draft) |
| 딥러닝 | [MLP.md](../AI/Deep-Learning/MLP.md), [Backpropagation.md](../AI/Deep-Learning/Backpropagation.md), [Activation-Functions.md](../AI/Deep-Learning/Activation-Functions.md), [Loss-Functions.md](../AI/Deep-Learning/Loss-Functions.md), [Normalization-Layers.md](../AI/Deep-Learning/Normalization-Layers.md), [Dropout.md](../AI/Deep-Learning/Dropout.md), [CNN.md](../AI/Deep-Learning/CNN.md), [Attention.md](../AI/Deep-Learning/Attention.md), [Transformer.md](../AI/Deep-Learning/Transformer.md) (작성됨, Draft) |
| 응용 AI | [Language-Model-Basics.md](../AI/NLP/Language-Model-Basics.md), [Word-Embeddings.md](../AI/NLP/Word-Embeddings.md), [BERT.md](../AI/NLP/BERT.md), [GPT.md](../AI/NLP/GPT.md), [Image-Basics.md](../AI/Computer-Vision/Image-Basics.md), [Classical-Vision.md](../AI/Computer-Vision/Classical-Vision.md), [CNN-Deep-Dive.md](../AI/Computer-Vision/CNN-Deep-Dive.md), [Image-Classification.md](../AI/Computer-Vision/Image-Classification.md), [Object-Detection.md](../AI/Computer-Vision/Object-Detection.md), [Semantic-Segmentation.md](../AI/Computer-Vision/Semantic-Segmentation.md), [Instance-Segmentation.md](../AI/Computer-Vision/Instance-Segmentation.md), [Image-Generation.md](../AI/Computer-Vision/Image-Generation.md), [Pose-Estimation.md](../AI/Computer-Vision/Pose-Estimation.md), [Optical-Flow.md](../AI/Computer-Vision/Optical-Flow.md), [Video-Understanding.md](../AI/Computer-Vision/Video-Understanding.md), [Vision-Language.md](../AI/Computer-Vision/Vision-Language.md), [3D-Vision.md](../AI/Computer-Vision/3D-Vision.md), [MDP.md](../AI/Reinforcement-Learning/MDP.md), [TD-Learning.md](../AI/Reinforcement-Learning/TD-Learning.md), [Autoencoders.md](../AI/Generative-Models/Autoencoders.md), [VAE.md](../AI/Generative-Models/VAE.md), [Beta-VAE.md](../AI/Generative-Models/Beta-VAE.md), [GAN-Basics.md](../AI/Generative-Models/GAN-Basics.md), [DCGAN.md](../AI/Generative-Models/DCGAN.md), [Conditional-GAN.md](../AI/Generative-Models/Conditional-GAN.md), [StyleGAN.md](../AI/Generative-Models/StyleGAN.md), [CycleGAN.md](../AI/Generative-Models/CycleGAN.md), [Normalizing-Flows.md](../AI/Generative-Models/Normalizing-Flows.md), [Real-NVP.md](../AI/Generative-Models/Real-NVP.md), [DDPM.md](../AI/Generative-Models/DDPM.md), [DDIM.md](../AI/Generative-Models/DDIM.md), [Score-Based.md](../AI/Generative-Models/Score-Based.md), [Latent-Diffusion.md](../AI/Generative-Models/Latent-Diffusion.md), [EBM.md](../AI/Generative-Models/EBM.md) (작성됨, Draft) |

## P6: 실무/운영 경로

| 로드맵 | 우선 문서 |
|---|---|
| Systems Engineer | [Parallel-Models.md](../Systems/Parallel-Computing/Parallel-Models.md), [Multithreading.md](../Systems/Parallel-Computing/Multithreading.md), [Benchmarking-Basics.md](../Engineering/Performance/Benchmarking-Basics.md), [CPU-Profiling.md](../Engineering/Performance/CPU-Profiling.md), [Memory-Profiling.md](../Engineering/Performance/Memory-Profiling.md), [IO-Profiling.md](../Engineering/Performance/IO-Profiling.md), [Flame-Graphs.md](../Engineering/Performance/Flame-Graphs.md), [Cache-Friendly-Code.md](../Engineering/Performance/Cache-Friendly-Code.md), [Branch-Prediction.md](../Engineering/Performance/Branch-Prediction.md), [SIMD-Vectorization.md](../Engineering/Performance/SIMD-Vectorization.md), [Memory-Layout.md](../Engineering/Performance/Memory-Layout.md), [False-Sharing.md](../Engineering/Performance/False-Sharing.md), [Practical-Complexity.md](../Engineering/Performance/Practical-Complexity.md), [Memoization-Caching.md](../Engineering/Performance/Memoization-Caching.md), [Lazy-Evaluation.md](../Engineering/Performance/Lazy-Evaluation.md), [Lock-Contention.md](../Engineering/Performance/Lock-Contention.md), [Thread-Pool-Tuning.md](../Engineering/Performance/Thread-Pool-Tuning.md), [Async-IO.md](../Engineering/Performance/Async-IO.md), [Database-Query-Optimization.md](../Engineering/Performance/Database-Query-Optimization.md), [Network-Performance.md](../Engineering/Performance/Network-Performance.md), [CDN-Caching.md](../Engineering/Performance/CDN-Caching.md), [JIT-Optimization.md](../Engineering/Performance/JIT-Optimization.md), [Git-Internals.md](../Engineering/DevOps/Git-Internals.md), [CICD-Principles.md](../Engineering/DevOps/CICD-Principles.md), [Jenkins-GitLab-CI.md](../Engineering/DevOps/Jenkins-GitLab-CI.md), [Deployment-Strategies.md](../Engineering/DevOps/Deployment-Strategies.md), [Docker-Basics.md](../Engineering/DevOps/Docker-Basics.md), [Docker-Compose.md](../Engineering/DevOps/Docker-Compose.md), [Container-Networking-Volumes.md](../Engineering/DevOps/Container-Networking-Volumes.md), [Kubernetes-Basics.md](../Engineering/DevOps/Kubernetes-Basics.md), [Kubernetes-Advanced.md](../Engineering/DevOps/Kubernetes-Advanced.md), [Helm.md](../Engineering/DevOps/Helm.md), [Cloud-Computing.md](../Engineering/DevOps/Cloud-Computing.md), [AWS-Core-Services.md](../Engineering/DevOps/AWS-Core-Services.md), [GCP-Azure-Overview.md](../Engineering/DevOps/GCP-Azure-Overview.md), [Serverless.md](../Engineering/DevOps/Serverless.md), [Terraform-Basics.md](../Engineering/DevOps/Terraform-Basics.md), [Ansible.md](../Engineering/DevOps/Ansible.md), [Logging-Systems.md](../Engineering/DevOps/Logging-Systems.md), [Metrics-Alerts.md](../Engineering/DevOps/Metrics-Alerts.md), [Distributed-Tracing.md](../Engineering/DevOps/Distributed-Tracing.md), [SLI-SLO-SLA.md](../Engineering/DevOps/SLI-SLO-SLA.md), [Git-Basics.md](../Engineering/DevOps/Git/Git-Basics.md), [Git-Branches-Merging-Rebasing.md](../Engineering/DevOps/Git/Git-Branches-Merging-Rebasing.md), [Git-Remotes.md](../Engineering/DevOps/Git/Git-Remotes.md), [Git-Conflict-Resolution.md](../Engineering/DevOps/Git/Git-Conflict-Resolution.md), [Git-Undoing-Changes.md](../Engineering/DevOps/Git/Git-Undoing-Changes.md), [GitHub-Repositories.md](../Engineering/DevOps/GitHub/GitHub-Repositories.md), [GitHub-Issues-and-Pull-Requests.md](../Engineering/DevOps/GitHub/GitHub-Issues-and-Pull-Requests.md), [GitHub-Flow.md](../Engineering/DevOps/GitHub/GitHub-Flow.md), [GitHub-Code-Review.md](../Engineering/DevOps/GitHub/GitHub-Code-Review.md), [GitHub-Actions.md](../Engineering/DevOps/GitHub/GitHub-Actions.md), [Approach.md](../Engineering/System-Design/Approach.md), [Scalability.md](../Engineering/System-Design/Scalability.md), [Load-Balancing.md](../Engineering/System-Design/Load-Balancing.md), [Caching.md](../Engineering/System-Design/Caching.md), [Database-Design.md](../Engineering/System-Design/Database-Design.md), [CDN.md](../Engineering/System-Design/CDN.md), [Message-Queues.md](../Engineering/System-Design/Message-Queues.md), [Microservices.md](../Engineering/System-Design/Microservices.md), [System-Design-Case-Studies.md](../Engineering/System-Design/System-Design-Case-Studies.md) (작성됨, Draft) |
| ML Engineer | [Experiment-Tracking.md](../AI/MLOps/Experiment-Tracking.md), [Hyperparameter-Tuning.md](../AI/MLOps/Hyperparameter-Tuning.md), [Reproducibility.md](../AI/MLOps/Reproducibility.md), [Data-Versioning.md](../AI/MLOps/Data-Versioning.md), [Feature-Store.md](../AI/MLOps/Feature-Store.md), [Data-Validation.md](../AI/MLOps/Data-Validation.md), [Streaming-vs-Batch.md](../AI/MLOps/Streaming-vs-Batch.md), [Data-Labeling.md](../AI/MLOps/Data-Labeling.md), [Online-vs-Batch-Serving.md](../AI/MLOps/Online-vs-Batch-Serving.md), [REST-Serving.md](../AI/MLOps/REST-Serving.md), [gRPC-Serving.md](../AI/MLOps/gRPC-Serving.md), [Model-Optimization.md](../AI/MLOps/Model-Optimization.md), [AB-Testing.md](../AI/MLOps/AB-Testing.md), [Data-Drift.md](../AI/MLOps/Data-Drift.md), [Model-Monitoring.md](../AI/MLOps/Model-Monitoring.md), [Feedback-Loop.md](../AI/MLOps/Feedback-Loop.md), [ML-Pipeline.md](../AI/MLOps/ML-Pipeline.md), [Distributed-Training.md](../AI/MLOps/Distributed-Training.md), [GPU-Cluster.md](../AI/MLOps/GPU-Cluster.md), [Model-Registry.md](../AI/MLOps/Model-Registry.md) (작성됨, Draft) |
| Software Engineering | [SOLID.md](../Engineering/Software-Design/SOLID.md), [Clean-Code.md](../Engineering/Software-Design/Clean-Code.md), [Refactoring.md](../Engineering/Software-Design/Refactoring.md), [Testing-Pyramid.md](../Engineering/Testing/Testing-Pyramid.md), [Test-Doubles.md](../Engineering/Testing/Test-Doubles.md), [Boundary-Value-Analysis.md](../Engineering/Testing/Boundary-Value-Analysis.md), [Unit-Test-Principles.md](../Engineering/Testing/Unit-Test-Principles.md), [TDD.md](../Engineering/Testing/TDD.md), [BDD.md](../Engineering/Testing/BDD.md), [Testable-Design.md](../Engineering/Testing/Testable-Design.md), [Integration-Test-Strategy.md](../Engineering/Testing/Integration-Test-Strategy.md), [Contract-Testing.md](../Engineering/Testing/Contract-Testing.md), [Database-Testing.md](../Engineering/Testing/Database-Testing.md), [E2E-Testing.md](../Engineering/Testing/E2E-Testing.md), [UI-Test-Tools.md](../Engineering/Testing/UI-Test-Tools.md), [Visual-Regression-Testing.md](../Engineering/Testing/Visual-Regression-Testing.md), [Load-Stress-Soak-Testing.md](../Engineering/Testing/Load-Stress-Soak-Testing.md), [K6-JMeter.md](../Engineering/Testing/K6-JMeter.md), [Code-Coverage.md](../Engineering/Testing/Code-Coverage.md), [Mutation-Testing.md](../Engineering/Testing/Mutation-Testing.md), [Static-Analysis-Linting.md](../Engineering/Testing/Static-Analysis-Linting.md), [Scientific-Debugging.md](../Engineering/Debugging/Scientific-Debugging.md), [Minimal-Reproducible-Example.md](../Engineering/Debugging/Minimal-Reproducible-Example.md), [Bisect-Debugging.md](../Engineering/Debugging/Bisect-Debugging.md), [Rubber-Duck-Debugging.md](../Engineering/Debugging/Rubber-Duck-Debugging.md), [Stack-Traces.md](../Engineering/Debugging/Stack-Traces.md), [Breakpoints-and-Stepping.md](../Engineering/Debugging/Breakpoints-and-Stepping.md), [Conditional-Breakpoints.md](../Engineering/Debugging/Conditional-Breakpoints.md), [Remote-Debugging.md](../Engineering/Debugging/Remote-Debugging.md), [Core-Dump-Analysis.md](../Engineering/Debugging/Core-Dump-Analysis.md), [Structured-Logging.md](../Engineering/Debugging/Structured-Logging.md), [Logging-Levels.md](../Engineering/Debugging/Logging-Levels.md), [Distributed-Log-Correlation.md](../Engineering/Debugging/Distributed-Log-Correlation.md), [Memory-Errors.md](../Engineering/Debugging/Memory-Errors.md), [Valgrind-AddressSanitizer.md](../Engineering/Debugging/Valgrind-AddressSanitizer.md), [Race-Condition-Debugging.md](../Engineering/Debugging/Race-Condition-Debugging.md), [Deadlock-Detection.md](../Engineering/Debugging/Deadlock-Detection.md), [Canary-Feature-Flags.md](../Engineering/Debugging/Canary-Feature-Flags.md), [Error-Tracking.md](../Engineering/Debugging/Error-Tracking.md), [Postmortem.md](../Engineering/Debugging/Postmortem.md) (작성됨, Draft) |

## P7: 연구/심화 경로

| 묶음 | 우선 문서 |
|---|---|
| 수학 심화 | [Real-Numbers.md](../Math/Real-Analysis/Real-Numbers.md), [Sequences-Series.md](../Math/Real-Analysis/Sequences-Series.md), [Continuity.md](../Math/Real-Analysis/Continuity.md), [Measure-Theory.md](../Math/Real-Analysis/Measure-Theory.md), [Function-Spaces.md](../Math/Real-Analysis/Function-Spaces.md) (작성됨, Draft) |
| 이론적 ML | [PAC-Learning.md](../AI/Theoretical-ML/PAC-Learning.md), [VC-Dimension.md](../AI/Theoretical-ML/VC-Dimension.md), [Rademacher-Complexity.md](../AI/Theoretical-ML/Rademacher-Complexity.md), [Generalization-Bounds.md](../AI/Theoretical-ML/Generalization-Bounds.md), [Double-Descent.md](../AI/Theoretical-ML/Double-Descent.md), [GD-Convergence.md](../AI/Theoretical-ML/GD-Convergence.md), [Regret-Minimization.md](../AI/Theoretical-ML/Regret-Minimization.md) (작성됨, Draft) |
| PGM/인과 | [Bayesian-Networks.md](../AI/PGMs/Bayesian-Networks.md), [d-Separation.md](../AI/PGMs/d-Separation.md), [Variable-Elimination.md](../AI/PGMs/Variable-Elimination.md), [Belief-Propagation.md](../AI/PGMs/Belief-Propagation.md), [MCMC.md](../AI/PGMs/MCMC.md), [Correlation-vs-Causation.md](../AI/Causal-Inference/Correlation-vs-Causation.md), [Confounding.md](../AI/Causal-Inference/Confounding.md), [Potential-Outcomes.md](../AI/Causal-Inference/Potential-Outcomes.md), [SCM.md](../AI/Causal-Inference/SCM.md), [Causal-DAG.md](../AI/Causal-Inference/Causal-DAG.md), [Do-Calculus.md](../AI/Causal-Inference/Do-Calculus.md), [Identifiability.md](../AI/Causal-Inference/Identifiability.md), [Intervention.md](../AI/Causal-Inference/Intervention.md), [Counterfactual.md](../AI/Causal-Inference/Counterfactual.md), [Mediation.md](../AI/Causal-Inference/Mediation.md), [RCT.md](../AI/Causal-Inference/RCT.md), [Instrumental-Variables.md](../AI/Causal-Inference/Instrumental-Variables.md), [DiD.md](../AI/Causal-Inference/DiD.md), [RDD.md](../AI/Causal-Inference/RDD.md), [Causal-ML.md](../AI/Causal-Inference/Causal-ML.md), [Causal-Representation.md](../AI/Causal-Inference/Causal-Representation.md) (작성됨, Draft) |
| AI Safety | [Alignment-Overview.md](../AI/AI-Safety/Alignment-Overview.md), [Reward-Hacking.md](../AI/AI-Safety/Reward-Hacking.md), [RLHF-Constitutional-AI.md](../AI/AI-Safety/RLHF-Constitutional-AI.md), [Feedback-Limitations.md](../AI/AI-Safety/Feedback-Limitations.md), [Superalignment.md](../AI/AI-Safety/Superalignment.md), [Mechanistic-Interpretability.md](../AI/AI-Safety/Mechanistic-Interpretability.md), [Activation-Patching.md](../AI/AI-Safety/Activation-Patching.md), [Probing-Classifiers.md](../AI/AI-Safety/Probing-Classifiers.md), [Sparse-Autoencoder.md](../AI/AI-Safety/Sparse-Autoencoder.md), [Attention-Visualization.md](../AI/AI-Safety/Attention-Visualization.md), [Adversarial-Examples.md](../AI/AI-Safety/Adversarial-Examples.md), [OOD-Generalization.md](../AI/AI-Safety/OOD-Generalization.md), [Certified-Robustness.md](../AI/AI-Safety/Certified-Robustness.md), [Poisoning-Attacks.md](../AI/AI-Safety/Poisoning-Attacks.md), [Capability-Evaluation.md](../AI/AI-Safety/Capability-Evaluation.md), [Dangerous-Capability-Evaluation.md](../AI/AI-Safety/Dangerous-Capability-Evaluation.md), [Red-Teaming.md](../AI/AI-Safety/Red-Teaming.md), [Scalable-Oversight.md](../AI/AI-Safety/Scalable-Oversight.md), [AI-Risk-Classification.md](../AI/AI-Safety/AI-Risk-Classification.md), [AI-Regulation.md](../AI/AI-Safety/AI-Regulation.md), [Fairness-Bias.md](../AI/AI-Safety/Fairness-Bias.md) (작성됨, Draft) |
| 고급 알고리즘/이론 | [Max-Flow.md](../Algorithms/Max-Flow.md), [Bipartite-Matching.md](../Algorithms/Bipartite-Matching.md), [KMP.md](../Algorithms/KMP.md), [Number-Theory.md](../Algorithms/Number-Theory.md), [Approximation-Algorithms.md](../Algorithms/Approximation-Algorithms.md), [Randomized-Algorithms.md](../Algorithms/Randomized-Algorithms.md), [Qubits.md](../CS-Theory/Quantum-Computing/Qubits.md) (작성됨, Draft) |

---

## 승격 순서

1. 이 백로그 또는 [Coverage-Matrix.md](Coverage-Matrix.md)에서 다음 작성 대상을 고른다.
2. 상위 README의 `Planned` 행을 확인한다.
3. 실제 파일을 만들고 `Status: Draft`를 둔다.
4. 상위 README의 해당 행을 `Draft`로 바꾼다.
5. `python Maintainers/Scripts/sync_summary_counts.py`로 요약 수치를 맞춘 뒤 `python Maintainers/Scripts/validate_docs.py`를 실행한다.
6. 개념, 직관, 이론, 구현/예시, 복잡도/한계, 응용, 흔한 오해, 연습 문제, 이어서 읽기, 참조가 충분하면 `Review`로 올린다.
7. 핵심 경로 밖의 주제는 [Topic-Classification.md](Topic-Classification.md)의 `Optional` 또는 `Deferred` 분류를 확인한다.
