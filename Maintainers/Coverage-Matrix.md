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

| 영역 | Draft | Review | Planned | 역할 |
|---|---:|---:|---:|---|
| Programming | 31 | 2 | 0 | 모든 로드맵의 출발점 |
| Math | 52 | 0 | 0 | CS/AI 이론의 공통 기반 |
| Data-Structures | 17 | 0 | 0 | 알고리즘과 시스템 구현 기반 |
| Algorithms | 32 | 2 | 0 | CS 핵심과 코딩 문제 해결 기반 |
| Systems | 54 | 0 | 0 | CS Core, Systems Engineer 기반 |
| CS-Theory | 30 | 0 | 0 | 이론/컴파일러/보안 기반 |
| AI | 191 | 0 | 0 | AI Core, ML Engineer, Researcher 기반 |
| Engineering | 113 | 0 | 0 | 실무 운영, 설계, 품질 기반 |

---

## Beginner

입문자 로드맵은 프로그래밍, 기초 수학, 자료구조, 알고리즘, 시스템 기본 용어까지 연결한다.

| 단계 | 필수 문서 |
|---|---|
| 프로그래밍 | [Variables-and-Types.md](../Programming/Variables-and-Types.md), [Control-Flow.md](../Programming/Control-Flow.md), [Functions-and-Recursion.md](../Programming/Functions-and-Recursion.md), [Arrays-and-Strings.md](../Programming/Arrays-and-Strings.md), [Language-Selection.md](../Programming/Language-Selection.md) |
| 이산수학 | [Logic.md](../Math/Discrete/Logic.md), [Induction.md](../Math/Discrete/Induction.md), [Graph-Theory.md](../Math/Discrete/Graph-Theory.md) |
| 자료구조 | [Array.md](../Data-Structures/Array.md), [Linked-List.md](../Data-Structures/Linked-List.md), [Stack.md](../Data-Structures/Stack.md), [Queue.md](../Data-Structures/Queue.md), [Graph-Representation.md](../Data-Structures/Graph-Representation.md), [Binary-Tree.md](../Data-Structures/Binary-Tree.md), [Hash-Table.md](../Data-Structures/Hash-Table.md) |
| 알고리즘 | [Complexity.md](../Algorithms/Complexity.md), [Sorting.md](../Algorithms/Sorting.md), [Binary-Search.md](../Algorithms/Binary-Search.md), [BFS-DFS.md](../Algorithms/BFS-DFS.md), [DP-Basics.md](../Algorithms/DP-Basics.md) |
| 시스템 맛보기 | [Data-Representation.md](../Systems/Computer-Architecture/Data-Representation.md), [Processes-and-Threads.md](../Systems/Operating-Systems/Processes-and-Threads.md), [Network-Models.md](../Systems/Networks/Network-Models.md), [Relational-Model-and-SQL.md](../Systems/Databases/Relational-Model-and-SQL.md) |

---

## CS Core

CS 핵심 로드맵은 전공 필수 흐름을 완성하는 기준이다.

| 단계 | 필수 문서 |
|---|---|
| 프로그래밍 | Beginner 필수 문서 + [Pointers-and-Memory.md](../Programming/Pointers-and-Memory.md), [OOP.md](../Programming/OOP.md), [Functional-Intro.md](../Programming/Functional-Intro.md) |
| 수학 | [Set-Theory.md](../Math/Discrete/Set-Theory.md), [Relations-and-Functions.md](../Math/Discrete/Relations-and-Functions.md), [Induction.md](../Math/Discrete/Induction.md), [Graph-Theory.md](../Math/Discrete/Graph-Theory.md), [Recurrences.md](../Math/Discrete/Recurrences.md), [Number-Theory-Basics.md](../Math/Discrete/Number-Theory-Basics.md) |
| 자료구조 | Beginner 필수 문서 + [BST.md](../Data-Structures/BST.md), [Heap.md](../Data-Structures/Heap.md), [Union-Find.md](../Data-Structures/Union-Find.md), [Hash-Function.md](../Data-Structures/Hash-Function.md) |
| 알고리즘 | Beginner 필수 문서 + [Divide-and-Conquer.md](../Algorithms/Divide-and-Conquer.md), [Greedy.md](../Algorithms/Greedy.md), [Backtracking.md](../Algorithms/Backtracking.md), [Topological-Sort.md](../Algorithms/Topological-Sort.md), [Dijkstra.md](../Algorithms/Dijkstra.md), [MST.md](../Algorithms/MST.md), [Amortized-Analysis.md](../Algorithms/Amortized-Analysis.md) |
| 컴퓨터 구조 | [Digital-Logic.md](../Systems/Computer-Architecture/Digital-Logic.md), [Data-Representation.md](../Systems/Computer-Architecture/Data-Representation.md), [CPU-and-ISA.md](../Systems/Computer-Architecture/CPU-and-ISA.md), [Pipelining.md](../Systems/Computer-Architecture/Pipelining.md), [Memory-Hierarchy.md](../Systems/Computer-Architecture/Memory-Hierarchy.md), [IO-Systems.md](../Systems/Computer-Architecture/IO-Systems.md) |
| 운영체제 | [Processes-and-Threads.md](../Systems/Operating-Systems/Processes-and-Threads.md), [Scheduling.md](../Systems/Operating-Systems/Scheduling.md), [Synchronization.md](../Systems/Operating-Systems/Synchronization.md), [Deadlock.md](../Systems/Operating-Systems/Deadlock.md), [Memory-Management.md](../Systems/Operating-Systems/Memory-Management.md), [Virtual-Memory.md](../Systems/Operating-Systems/Virtual-Memory.md), [File-Systems.md](../Systems/Operating-Systems/File-Systems.md) |
| 네트워크 | [Network-Models.md](../Systems/Networks/Network-Models.md), [IP-and-Routing.md](../Systems/Networks/IP-and-Routing.md), [TCP-UDP.md](../Systems/Networks/TCP-UDP.md), [HTTP.md](../Systems/Networks/HTTP.md), [DNS.md](../Systems/Networks/DNS.md), [Socket-Programming.md](../Systems/Networks/Socket-Programming.md) |
| 데이터베이스 | [Relational-Model-and-SQL.md](../Systems/Databases/Relational-Model-and-SQL.md), [Database-Normalization.md](../Systems/Databases/Database-Normalization.md), [Indexes-and-B-Tree.md](../Systems/Databases/Indexes-and-B-Tree.md), [Transactions-and-ACID.md](../Systems/Databases/Transactions-and-ACID.md), [Concurrency-Control.md](../Systems/Databases/Concurrency-Control.md), [Query-Optimization.md](../Systems/Databases/Query-Optimization.md) |
| 분산 시스템 | [System-Models.md](../Systems/Distributed-Systems/System-Models.md), [CAP-Theorem.md](../Systems/Distributed-Systems/CAP-Theorem.md), [Consensus.md](../Systems/Distributed-Systems/Consensus.md), [Replication.md](../Systems/Distributed-Systems/Replication.md), [Partitioning.md](../Systems/Distributed-Systems/Partitioning.md), [Time-and-Ordering.md](../Systems/Distributed-Systems/Time-and-Ordering.md) |
| 계산 이론 | [Regular-Languages.md](../CS-Theory/Computation-Theory/Regular-Languages.md), [Regular-Expressions.md](../CS-Theory/Computation-Theory/Regular-Expressions.md), [Context-Free.md](../CS-Theory/Computation-Theory/Context-Free.md), [Turing-Machine.md](../CS-Theory/Computation-Theory/Turing-Machine.md), [Undecidability.md](../CS-Theory/Computation-Theory/Undecidability.md), [Complexity-Classes.md](../CS-Theory/Computation-Theory/Complexity-Classes.md), [NP-Completeness.md](../CS-Theory/Computation-Theory/NP-Completeness.md) |
| PL/컴파일러 | [Syntax-and-Semantics.md](../CS-Theory/Programming-Languages/Syntax-and-Semantics.md), [Type-Systems.md](../CS-Theory/Programming-Languages/Type-Systems.md), [Lambda-Calculus.md](../CS-Theory/Programming-Languages/Lambda-Calculus.md), [Lexer.md](../CS-Theory/Compilers/Lexer.md), [Parser.md](../CS-Theory/Compilers/Parser.md), [AST.md](../CS-Theory/Compilers/AST.md), [Intermediate-Representation.md](../CS-Theory/Compilers/Intermediate-Representation.md), [Code-Generation.md](../CS-Theory/Compilers/Code-Generation.md) |
| 보안 | [Symmetric-Encryption.md](../Engineering/Security/Symmetric-Encryption.md), [Asymmetric-Encryption.md](../Engineering/Security/Asymmetric-Encryption.md), [Hash-Functions.md](../Engineering/Security/Hash-Functions.md), [Digital-Signatures.md](../Engineering/Security/Digital-Signatures.md), [PKI-and-TLS.md](../Engineering/Security/PKI-and-TLS.md), [Auth.md](../Engineering/Security/Auth.md), [Web-Security.md](../Engineering/Security/Web-Security.md) |

---

## AI Core

AI 핵심 로드맵은 수학 기초에서 머신러닝, 딥러닝, 주요 응용 분야까지 이어지는 기준이다.

| 단계 | 필수 문서 |
|---|---|
| 선형대수 | [Vectors.md](../Math/Linear-Algebra/Vectors.md), [Matrices.md](../Math/Linear-Algebra/Matrices.md), [Linear-Systems.md](../Math/Linear-Algebra/Linear-Systems.md), [Eigenvalues.md](../Math/Linear-Algebra/Eigenvalues.md), [SVD.md](../Math/Linear-Algebra/SVD.md), [PCA.md](../Math/Linear-Algebra/PCA.md), [Orthogonality.md](../Math/Linear-Algebra/Orthogonality.md) |
| 미적분 | [Limits.md](../Math/Calculus/Limits.md), [Differentiation.md](../Math/Calculus/Differentiation.md), [Partial-Derivatives.md](../Math/Calculus/Partial-Derivatives.md), [Chain-Rule.md](../Math/Calculus/Chain-Rule.md), [Taylor-Series.md](../Math/Calculus/Taylor-Series.md) |
| 확률/통계 | [Probability-Basics.md](../Math/Probability-Statistics/Probability-Basics.md), [Distributions.md](../Math/Probability-Statistics/Distributions.md), [Expectation.md](../Math/Probability-Statistics/Expectation.md), [Bayes-Theorem.md](../Math/Probability-Statistics/Bayes-Theorem.md), [MLE.md](../Math/Probability-Statistics/MLE.md), [CLT.md](../Math/Probability-Statistics/CLT.md), [Hypothesis-Testing.md](../Math/Probability-Statistics/Hypothesis-Testing.md), [Information-Theory.md](../Math/Probability-Statistics/Information-Theory.md) |
| 최적화 | [Convex-Optimization.md](../Math/Optimization/Convex-Optimization.md), [Gradient-Descent.md](../Math/Optimization/Gradient-Descent.md), [SGD.md](../Math/Optimization/SGD.md), [Adaptive-Methods.md](../Math/Optimization/Adaptive-Methods.md), [Lagrangian.md](../Math/Optimization/Lagrangian.md) |
| 머신러닝 | [Linear-Regression.md](../AI/Machine-Learning/Linear-Regression.md), [Logistic-Regression.md](../AI/Machine-Learning/Logistic-Regression.md), [Decision-Trees.md](../AI/Machine-Learning/Decision-Trees.md), [Ensemble.md](../AI/Machine-Learning/Ensemble.md), [KNN.md](../AI/Machine-Learning/KNN.md), [K-Means.md](../AI/Machine-Learning/K-Means.md), [Dimensionality-Reduction.md](../AI/Machine-Learning/Dimensionality-Reduction.md), [Bias-Variance.md](../AI/Machine-Learning/Bias-Variance.md), [Cross-Validation.md](../AI/Machine-Learning/Cross-Validation.md), [Regularization.md](../AI/Machine-Learning/Regularization.md), [Overfitting.md](../AI/Machine-Learning/Overfitting.md) |
| 딥러닝 | [MLP.md](../AI/Deep-Learning/MLP.md), [Backpropagation.md](../AI/Deep-Learning/Backpropagation.md), [Activation-Functions.md](../AI/Deep-Learning/Activation-Functions.md), [Loss-Functions.md](../AI/Deep-Learning/Loss-Functions.md), [Normalization-Layers.md](../AI/Deep-Learning/Normalization-Layers.md), [Dropout.md](../AI/Deep-Learning/Dropout.md), [CNN.md](../AI/Deep-Learning/CNN.md), [RNN-LSTM-GRU.md](../AI/Deep-Learning/RNN-LSTM-GRU.md), [Attention.md](../AI/Deep-Learning/Attention.md), [Transformer.md](../AI/Deep-Learning/Transformer.md), [Transfer-Learning.md](../AI/Deep-Learning/Transfer-Learning.md), [Fine-Tuning.md](../AI/Deep-Learning/Fine-Tuning.md) |
| NLP/LLM | [Text-Preprocessing.md](../AI/NLP/Text-Preprocessing.md), [Language-Model-Basics.md](../AI/NLP/Language-Model-Basics.md), [Word-Embeddings.md](../AI/NLP/Word-Embeddings.md), [Transformer-NLP.md](../AI/NLP/Transformer-NLP.md), [BERT.md](../AI/NLP/BERT.md), [GPT.md](../AI/NLP/GPT.md), [Transformer-Advanced.md](../AI/LLMs/Transformer-Advanced.md), [GPT-Family.md](../AI/LLMs/GPT-Family.md), [BERT-Family.md](../AI/LLMs/BERT-Family.md), [Encoder-Decoder.md](../AI/LLMs/Encoder-Decoder.md), [Pretraining.md](../AI/LLMs/Pretraining.md), [Instruction-Tuning.md](../AI/LLMs/Instruction-Tuning.md), [RLHF.md](../AI/LLMs/RLHF.md), [DPO.md](../AI/LLMs/DPO.md), [PEFT.md](../AI/LLMs/PEFT.md), [Prompt-Engineering.md](../AI/LLMs/Prompt-Engineering.md), [In-Context-Learning.md](../AI/LLMs/In-Context-Learning.md), [Chain-of-Thought.md](../AI/LLMs/Chain-of-Thought.md), [RAG.md](../AI/LLMs/RAG.md), [LLM-Agents.md](../AI/LLMs/LLM-Agents.md), [Efficient-Attention.md](../AI/LLMs/Efficient-Attention.md), [Quantization.md](../AI/LLMs/Quantization.md), [Distillation.md](../AI/LLMs/Distillation.md), [Inference-Optimization.md](../AI/LLMs/Inference-Optimization.md) |
| 비전/생성/RL | [Image-Basics.md](../AI/Computer-Vision/Image-Basics.md), [Classical-Vision.md](../AI/Computer-Vision/Classical-Vision.md), [CNN-Deep-Dive.md](../AI/Computer-Vision/CNN-Deep-Dive.md), [Image-Classification.md](../AI/Computer-Vision/Image-Classification.md), [Object-Detection.md](../AI/Computer-Vision/Object-Detection.md), [Semantic-Segmentation.md](../AI/Computer-Vision/Semantic-Segmentation.md), [Instance-Segmentation.md](../AI/Computer-Vision/Instance-Segmentation.md), [Image-Generation.md](../AI/Computer-Vision/Image-Generation.md), [Pose-Estimation.md](../AI/Computer-Vision/Pose-Estimation.md), [Optical-Flow.md](../AI/Computer-Vision/Optical-Flow.md), [Video-Understanding.md](../AI/Computer-Vision/Video-Understanding.md), [Vision-Language.md](../AI/Computer-Vision/Vision-Language.md), [3D-Vision.md](../AI/Computer-Vision/3D-Vision.md), [Autoencoders.md](../AI/Generative-Models/Autoencoders.md), [VAE.md](../AI/Generative-Models/VAE.md), [Beta-VAE.md](../AI/Generative-Models/Beta-VAE.md), [GAN-Basics.md](../AI/Generative-Models/GAN-Basics.md), [DCGAN.md](../AI/Generative-Models/DCGAN.md), [Conditional-GAN.md](../AI/Generative-Models/Conditional-GAN.md), [StyleGAN.md](../AI/Generative-Models/StyleGAN.md), [CycleGAN.md](../AI/Generative-Models/CycleGAN.md), [Normalizing-Flows.md](../AI/Generative-Models/Normalizing-Flows.md), [Real-NVP.md](../AI/Generative-Models/Real-NVP.md), [DDPM.md](../AI/Generative-Models/DDPM.md), [DDIM.md](../AI/Generative-Models/DDIM.md), [Score-Based.md](../AI/Generative-Models/Score-Based.md), [Latent-Diffusion.md](../AI/Generative-Models/Latent-Diffusion.md), [EBM.md](../AI/Generative-Models/EBM.md), [MDP.md](../AI/Reinforcement-Learning/MDP.md), [Value-Functions.md](../AI/Reinforcement-Learning/Value-Functions.md), [Policy.md](../AI/Reinforcement-Learning/Policy.md), [TD-Learning.md](../AI/Reinforcement-Learning/TD-Learning.md), [Policy-Gradient.md](../AI/Reinforcement-Learning/Policy-Gradient.md) |
| 운영 | [Experiment-Tracking.md](../AI/MLOps/Experiment-Tracking.md), [Hyperparameter-Tuning.md](../AI/MLOps/Hyperparameter-Tuning.md), [Reproducibility.md](../AI/MLOps/Reproducibility.md), [Data-Versioning.md](../AI/MLOps/Data-Versioning.md), [Feature-Store.md](../AI/MLOps/Feature-Store.md), [Data-Validation.md](../AI/MLOps/Data-Validation.md), [Online-vs-Batch-Serving.md](../AI/MLOps/Online-vs-Batch-Serving.md), [REST-Serving.md](../AI/MLOps/REST-Serving.md), [gRPC-Serving.md](../AI/MLOps/gRPC-Serving.md), [Model-Optimization.md](../AI/MLOps/Model-Optimization.md), [Data-Drift.md](../AI/MLOps/Data-Drift.md), [Model-Monitoring.md](../AI/MLOps/Model-Monitoring.md), [Feedback-Loop.md](../AI/MLOps/Feedback-Loop.md), [ML-Pipeline.md](../AI/MLOps/ML-Pipeline.md) |

---

## Systems Engineer

시스템 엔지니어 로드맵은 시스템 내부 동작과 운영 실무를 함께 완성하는 기준이다.

| 단계 | 필수 문서 |
|---|---|
| 시스템 기반 | CS Core의 컴퓨터 구조, 운영체제, 네트워크, 데이터베이스, 분산 시스템 필수 문서 |
| 병렬 컴퓨팅 | [Parallel-Models.md](../Systems/Parallel-Computing/Parallel-Models.md), [Multithreading.md](../Systems/Parallel-Computing/Multithreading.md), [SIMD.md](../Systems/Parallel-Computing/SIMD.md), [GPU-and-CUDA.md](../Systems/Parallel-Computing/GPU-and-CUDA.md), [OpenMP-MPI.md](../Systems/Parallel-Computing/OpenMP-MPI.md), [Parallel-Scalability.md](../Systems/Parallel-Computing/Parallel-Scalability.md) |
| 성능 공학 | [Benchmarking-Basics.md](../Engineering/Performance/Benchmarking-Basics.md), [CPU-Profiling.md](../Engineering/Performance/CPU-Profiling.md), [Memory-Profiling.md](../Engineering/Performance/Memory-Profiling.md), [IO-Profiling.md](../Engineering/Performance/IO-Profiling.md), [Flame-Graphs.md](../Engineering/Performance/Flame-Graphs.md), [Cache-Friendly-Code.md](../Engineering/Performance/Cache-Friendly-Code.md), [Branch-Prediction.md](../Engineering/Performance/Branch-Prediction.md), [SIMD-Vectorization.md](../Engineering/Performance/SIMD-Vectorization.md), [Memory-Layout.md](../Engineering/Performance/Memory-Layout.md), [False-Sharing.md](../Engineering/Performance/False-Sharing.md), [Practical-Complexity.md](../Engineering/Performance/Practical-Complexity.md), [Memoization-Caching.md](../Engineering/Performance/Memoization-Caching.md), [Lazy-Evaluation.md](../Engineering/Performance/Lazy-Evaluation.md), [Lock-Contention.md](../Engineering/Performance/Lock-Contention.md), [Thread-Pool-Tuning.md](../Engineering/Performance/Thread-Pool-Tuning.md), [Async-IO.md](../Engineering/Performance/Async-IO.md), [Database-Query-Optimization.md](../Engineering/Performance/Database-Query-Optimization.md), [Network-Performance.md](../Engineering/Performance/Network-Performance.md), [CDN-Caching.md](../Engineering/Performance/CDN-Caching.md), [JIT-Optimization.md](../Engineering/Performance/JIT-Optimization.md) |
| DevOps | [Git-Internals.md](../Engineering/DevOps/Git-Internals.md), [CICD-Principles.md](../Engineering/DevOps/CICD-Principles.md), [Jenkins-GitLab-CI.md](../Engineering/DevOps/Jenkins-GitLab-CI.md), [Deployment-Strategies.md](../Engineering/DevOps/Deployment-Strategies.md), [Docker-Basics.md](../Engineering/DevOps/Docker-Basics.md), [Docker-Compose.md](../Engineering/DevOps/Docker-Compose.md), [Container-Networking-Volumes.md](../Engineering/DevOps/Container-Networking-Volumes.md), [Kubernetes-Basics.md](../Engineering/DevOps/Kubernetes-Basics.md), [Kubernetes-Advanced.md](../Engineering/DevOps/Kubernetes-Advanced.md), [Helm.md](../Engineering/DevOps/Helm.md), [Cloud-Computing.md](../Engineering/DevOps/Cloud-Computing.md), [AWS-Core-Services.md](../Engineering/DevOps/AWS-Core-Services.md), [GCP-Azure-Overview.md](../Engineering/DevOps/GCP-Azure-Overview.md), [Serverless.md](../Engineering/DevOps/Serverless.md), [Terraform-Basics.md](../Engineering/DevOps/Terraform-Basics.md), [Ansible.md](../Engineering/DevOps/Ansible.md), [Logging-Systems.md](../Engineering/DevOps/Logging-Systems.md), [Metrics-Alerts.md](../Engineering/DevOps/Metrics-Alerts.md), [Distributed-Tracing.md](../Engineering/DevOps/Distributed-Tracing.md), [SLI-SLO-SLA.md](../Engineering/DevOps/SLI-SLO-SLA.md), [Git-Basics.md](../Engineering/DevOps/Git/Git-Basics.md), [Git-Branches-Merging-Rebasing.md](../Engineering/DevOps/Git/Git-Branches-Merging-Rebasing.md), [Git-Remotes.md](../Engineering/DevOps/Git/Git-Remotes.md), [Git-Conflict-Resolution.md](../Engineering/DevOps/Git/Git-Conflict-Resolution.md), [Git-Undoing-Changes.md](../Engineering/DevOps/Git/Git-Undoing-Changes.md), [GitHub-Repositories.md](../Engineering/DevOps/GitHub/GitHub-Repositories.md), [GitHub-Issues-and-Pull-Requests.md](../Engineering/DevOps/GitHub/GitHub-Issues-and-Pull-Requests.md), [GitHub-Flow.md](../Engineering/DevOps/GitHub/GitHub-Flow.md), [GitHub-Code-Review.md](../Engineering/DevOps/GitHub/GitHub-Code-Review.md), [GitHub-Actions.md](../Engineering/DevOps/GitHub/GitHub-Actions.md) |
| 시스템 설계 | [Approach.md](../Engineering/System-Design/Approach.md), [Scalability.md](../Engineering/System-Design/Scalability.md), [Load-Balancing.md](../Engineering/System-Design/Load-Balancing.md), [Caching.md](../Engineering/System-Design/Caching.md), [Database-Design.md](../Engineering/System-Design/Database-Design.md), [CDN.md](../Engineering/System-Design/CDN.md), [Message-Queues.md](../Engineering/System-Design/Message-Queues.md), [Microservices.md](../Engineering/System-Design/Microservices.md), [System-Design-Case-Studies.md](../Engineering/System-Design/System-Design-Case-Studies.md) |

---

## ML Engineer

ML 엔지니어 로드맵은 모델 학습, 실험 관리, 서빙, 배포를 하나의 흐름으로 연결한다.

| 단계 | 필수 문서 |
|---|---|
| 모델 기반 | AI Core의 수학, 머신러닝, 딥러닝 필수 문서 |
| 생성/LLM | [VAE.md](../AI/Generative-Models/VAE.md), [GAN-Basics.md](../AI/Generative-Models/GAN-Basics.md), [DDPM.md](../AI/Generative-Models/DDPM.md), [Latent-Diffusion.md](../AI/Generative-Models/Latent-Diffusion.md), [Transformer-Advanced.md](../AI/LLMs/Transformer-Advanced.md), [GPT-Family.md](../AI/LLMs/GPT-Family.md), [Pretraining.md](../AI/LLMs/Pretraining.md), [Instruction-Tuning.md](../AI/LLMs/Instruction-Tuning.md), [PEFT.md](../AI/LLMs/PEFT.md), [RAG.md](../AI/LLMs/RAG.md), [Inference-Optimization.md](../AI/LLMs/Inference-Optimization.md) |
| MLOps | [Experiment-Tracking.md](../AI/MLOps/Experiment-Tracking.md), [Hyperparameter-Tuning.md](../AI/MLOps/Hyperparameter-Tuning.md), [Reproducibility.md](../AI/MLOps/Reproducibility.md), [Data-Versioning.md](../AI/MLOps/Data-Versioning.md), [Feature-Store.md](../AI/MLOps/Feature-Store.md), [Data-Validation.md](../AI/MLOps/Data-Validation.md), [Streaming-vs-Batch.md](../AI/MLOps/Streaming-vs-Batch.md), [Data-Labeling.md](../AI/MLOps/Data-Labeling.md), [Online-vs-Batch-Serving.md](../AI/MLOps/Online-vs-Batch-Serving.md), [REST-Serving.md](../AI/MLOps/REST-Serving.md), [gRPC-Serving.md](../AI/MLOps/gRPC-Serving.md), [Model-Optimization.md](../AI/MLOps/Model-Optimization.md), [AB-Testing.md](../AI/MLOps/AB-Testing.md), [Data-Drift.md](../AI/MLOps/Data-Drift.md), [Model-Monitoring.md](../AI/MLOps/Model-Monitoring.md), [Feedback-Loop.md](../AI/MLOps/Feedback-Loop.md), [ML-Pipeline.md](../AI/MLOps/ML-Pipeline.md), [Distributed-Training.md](../AI/MLOps/Distributed-Training.md), [GPU-Cluster.md](../AI/MLOps/GPU-Cluster.md), [Model-Registry.md](../AI/MLOps/Model-Registry.md) |
| 운영 인프라 | [Docker-Basics.md](../Engineering/DevOps/Docker-Basics.md), [Kubernetes-Basics.md](../Engineering/DevOps/Kubernetes-Basics.md), [Cloud-Computing.md](../Engineering/DevOps/Cloud-Computing.md), [Metrics-Alerts.md](../Engineering/DevOps/Metrics-Alerts.md), [Distributed-Tracing.md](../Engineering/DevOps/Distributed-Tracing.md), [Approach.md](../Engineering/System-Design/Approach.md), [Caching.md](../Engineering/System-Design/Caching.md), [Message-Queues.md](../Engineering/System-Design/Message-Queues.md) |

---

## Researcher

연구자 로드맵은 논문 독해와 이론적 분석을 위한 기준이다.

| 단계 | 필수 문서 |
|---|---|
| 수학 이론 | [Real-Numbers.md](../Math/Real-Analysis/Real-Numbers.md), [Sequences-Series.md](../Math/Real-Analysis/Sequences-Series.md), [Continuity.md](../Math/Real-Analysis/Continuity.md), [Uniform-Continuity.md](../Math/Real-Analysis/Uniform-Continuity.md), [Measure-Theory.md](../Math/Real-Analysis/Measure-Theory.md), [Function-Spaces.md](../Math/Real-Analysis/Function-Spaces.md), [Information-Theory.md](../Math/Probability-Statistics/Information-Theory.md), [Convex-Optimization.md](../Math/Optimization/Convex-Optimization.md) |
| 계산 이론 | [Complexity-Classes.md](../CS-Theory/Computation-Theory/Complexity-Classes.md), [NP-Completeness.md](../CS-Theory/Computation-Theory/NP-Completeness.md), [Undecidability.md](../CS-Theory/Computation-Theory/Undecidability.md) |
| 이론적 ML | [PAC-Learning.md](../AI/Theoretical-ML/PAC-Learning.md), [VC-Dimension.md](../AI/Theoretical-ML/VC-Dimension.md), [Shattering.md](../AI/Theoretical-ML/Shattering.md), [No-Free-Lunch.md](../AI/Theoretical-ML/No-Free-Lunch.md), [Rademacher-Complexity.md](../AI/Theoretical-ML/Rademacher-Complexity.md), [Generalization-Bounds.md](../AI/Theoretical-ML/Generalization-Bounds.md), [Double-Descent.md](../AI/Theoretical-ML/Double-Descent.md), [Convex-Learning.md](../AI/Theoretical-ML/Convex-Learning.md), [GD-Convergence.md](../AI/Theoretical-ML/GD-Convergence.md), [Implicit-Regularization.md](../AI/Theoretical-ML/Implicit-Regularization.md), [Regret-Minimization.md](../AI/Theoretical-ML/Regret-Minimization.md), [Multi-Armed-Bandit.md](../AI/Theoretical-ML/Multi-Armed-Bandit.md) |
| PGM/인과 | [Factorization.md](../AI/PGMs/Factorization.md), [Bayesian-Networks.md](../AI/PGMs/Bayesian-Networks.md), [d-Separation.md](../AI/PGMs/d-Separation.md), [MRF.md](../AI/PGMs/MRF.md), [Variable-Elimination.md](../AI/PGMs/Variable-Elimination.md), [Belief-Propagation.md](../AI/PGMs/Belief-Propagation.md), [Variational-Inference.md](../AI/PGMs/Variational-Inference.md), [MCMC.md](../AI/PGMs/MCMC.md), [Correlation-vs-Causation.md](../AI/Causal-Inference/Correlation-vs-Causation.md), [Confounding.md](../AI/Causal-Inference/Confounding.md), [Potential-Outcomes.md](../AI/Causal-Inference/Potential-Outcomes.md), [SCM.md](../AI/Causal-Inference/SCM.md), [Causal-DAG.md](../AI/Causal-Inference/Causal-DAG.md), [Do-Calculus.md](../AI/Causal-Inference/Do-Calculus.md), [Identifiability.md](../AI/Causal-Inference/Identifiability.md), [Intervention.md](../AI/Causal-Inference/Intervention.md), [Counterfactual.md](../AI/Causal-Inference/Counterfactual.md), [Mediation.md](../AI/Causal-Inference/Mediation.md), [RCT.md](../AI/Causal-Inference/RCT.md), [Instrumental-Variables.md](../AI/Causal-Inference/Instrumental-Variables.md), [DiD.md](../AI/Causal-Inference/DiD.md), [RDD.md](../AI/Causal-Inference/RDD.md), [Causal-ML.md](../AI/Causal-Inference/Causal-ML.md), [Causal-Representation.md](../AI/Causal-Inference/Causal-Representation.md) |
| 안전성/해석 | [Alignment-Overview.md](../AI/AI-Safety/Alignment-Overview.md), [Reward-Hacking.md](../AI/AI-Safety/Reward-Hacking.md), [RLHF-Constitutional-AI.md](../AI/AI-Safety/RLHF-Constitutional-AI.md), [Feedback-Limitations.md](../AI/AI-Safety/Feedback-Limitations.md), [Superalignment.md](../AI/AI-Safety/Superalignment.md), [Mechanistic-Interpretability.md](../AI/AI-Safety/Mechanistic-Interpretability.md), [Activation-Patching.md](../AI/AI-Safety/Activation-Patching.md), [Probing-Classifiers.md](../AI/AI-Safety/Probing-Classifiers.md), [Sparse-Autoencoder.md](../AI/AI-Safety/Sparse-Autoencoder.md), [Attention-Visualization.md](../AI/AI-Safety/Attention-Visualization.md), [Adversarial-Examples.md](../AI/AI-Safety/Adversarial-Examples.md), [OOD-Generalization.md](../AI/AI-Safety/OOD-Generalization.md), [Certified-Robustness.md](../AI/AI-Safety/Certified-Robustness.md), [Poisoning-Attacks.md](../AI/AI-Safety/Poisoning-Attacks.md), [Capability-Evaluation.md](../AI/AI-Safety/Capability-Evaluation.md), [Dangerous-Capability-Evaluation.md](../AI/AI-Safety/Dangerous-Capability-Evaluation.md), [Red-Teaming.md](../AI/AI-Safety/Red-Teaming.md), [Scalable-Oversight.md](../AI/AI-Safety/Scalable-Oversight.md), [AI-Risk-Classification.md](../AI/AI-Safety/AI-Risk-Classification.md), [AI-Regulation.md](../AI/AI-Safety/AI-Regulation.md), [Fairness-Bias.md](../AI/AI-Safety/Fairness-Bias.md) |

---

## 완료 판정

프로젝트 전체가 "본문만 채우면 되는 상태"를 유지하려면 다음 조건을 만족해야 한다.

- 새 주제는 먼저 섹션 README의 `Planned` 행으로 등록한다.
- 특정 로드맵 완료 기준에 필요한 주제는 이 문서의 해당 로드맵 표에도 반영한다.
- 실제 파일을 만들면 상위 README의 `Status`와 문서 상단 `Status`를 함께 변경한다.
- `Review` 이상으로 올릴 때는 개념, 직관, 이론, 구현/예시, 복잡도/한계, 응용, 흔한 오해, 연습 문제, 이어서 읽기, 참조를 채운다.
- 빠르게 변하는 분야는 `Last reviewed` 날짜를 유지한다.
