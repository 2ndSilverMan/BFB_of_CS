# 주제 분류표 (Topic Classification)

> 모든 주제 문서를 `Required`, `Optional`, `Deferred` 중 하나로 분류한다.

---

## 분류 기준

- `Required`: 로드맵 완료 기준에 직접 필요하거나, [Content-Backlog.md](Content-Backlog.md)의 P0~P7에 포함된 문서.
- `Optional`: 섹션 확장, 심화, 실무 사례, 특정 도구/기법처럼 핵심 경로 이후에 채우는 문서.
- `Deferred`: 지금 목차에는 둘 수 있지만, 프로젝트의 현재 학습 목표에서는 보류하는 문서.

`Required` 문서는 [Coverage-Matrix.md](Coverage-Matrix.md)와 [Content-Backlog.md](Content-Backlog.md)가 관리한다. 아래 목록은 그 외 `Planned` 문서의 분류다.

---

## Optional

### AI/AI-Safety

`AI-Risk-Classification.md`, `Attention-Visualization.md`, `Certified-Robustness.md`, `Dangerous-Capability-Evaluation.md`, `Fairness-Bias.md`, `Feedback-Limitations.md`, `Poisoning-Attacks.md`, `Probing-Classifiers.md`, `Superalignment.md`

### AI/Causal-Inference

`Causal-ML.md`, `Causal-Representation.md`, `Confounding.md`, `Correlation-vs-Causation.md`, `DiD.md`, `Instrumental-Variables.md`, `Intervention.md`, `Mediation.md`, `RCT.md`, `RDD.md`

### AI/Computer-Vision

`3D-Vision.md`, `Classical-Vision.md`, `Image-Generation.md`, `Instance-Segmentation.md`, `Optical-Flow.md`, `Pose-Estimation.md`, `Semantic-Segmentation.md`, `Video-Understanding.md`, `Vision-Language.md`

### AI/Deep-Learning

`GNN.md`, `Self-Supervised.md`

### AI/Generative-Models

`Beta-VAE.md`, `Conditional-GAN.md`, `CycleGAN.md`, `DCGAN.md`, `DDIM.md`, `EBM.md`, `Normalizing-Flows.md`, `Real-NVP.md`, `Score-Based.md`, `StyleGAN.md`

### AI/LLMs

`BERT-Family.md`, `Chain-of-Thought.md`, `Distillation.md`, `DPO.md`, `Efficient-Attention.md`, `Encoder-Decoder.md`, `In-Context-Learning.md`, `LLM-Agents.md`, `Quantization.md`, `RLHF.md`

### AI/Machine-Learning

`Hierarchical-Clustering.md`, `SVM.md`

### AI/MLOps

`Data-Labeling.md`, `GPU-Cluster.md`, `gRPC-Serving.md`, `Streaming-vs-Batch.md`

### AI/NLP

`Attention-in-NLP.md`, `Machine-Translation.md`, `NER.md`, `Question-Answering.md`, `Relation-Extraction.md`, `RNN-for-NLP.md`, `Summarization.md`, `Text-Classification.md`

### AI/PGMs

`Cliques.md`, `CRF.md`, `EM-Algorithm.md`, `Graph-Review.md`, `HMM.md`, `Naive-Bayes.md`

### AI/Reinforcement-Learning

`Actor-Critic.md`, `DQN.md`, `Dynamic-Programming.md`, `Function-Approximation.md`, `Hierarchical-RL.md`, `Model-Based-DRL.md`, `Monte-Carlo.md`, `Multi-Agent-RL.md`, `Offline-RL.md`, `PPO.md`, `SAC.md`

### AI/Theoretical-ML

`Bias-Variance-Theory.md`, `Expert-Algorithms.md`, `MDL.md`, `Mutual-Information.md`, `Non-Convex-Convergence.md`

### Algorithms

`Aho-Corasick.md`, `Bellman-Ford.md`, `Bitmask-DP.md`, `Computational-Geometry.md`, `Dinic.md`, `DP-Optimization.md`, `Fast-Exponentiation.md`, `FFT.md`, `Floyd-Warshall.md`, `MCMF.md`, `Parallel-Algorithms.md`, `Rabin-Karp.md`, `SCC.md`, `Suffix-Array.md`, `Tree-DP.md`, `Z-Algorithm.md`

### CS-Theory/Compilers

`Interpreter-vs-Compiler.md`, `Optimization.md`, `Semantic-Analysis.md`

### CS-Theory/Programming-Languages

`Concurrency-Models.md`, `Memory-Models.md`, `Paradigms.md`, `Type-Inference.md`

### CS-Theory/Quantum-Computing

`Entanglement.md`, `Grover.md`, `Quantum-Circuits.md`, `Quantum-Complexity.md`, `Quantum-Error-Correction.md`, `Quantum-Gates.md`, `Shor.md`

### Data-Structures

`AVL-Tree.md`, `Deque.md`, `Fenwick-Tree.md`, `Red-Black-Tree.md`, `Segment-Tree.md`, `Trie.md`

### Engineering/Debugging

`Bisect-Debugging.md`, `Breakpoints-and-Stepping.md`, `Canary-Feature-Flags.md`, `Conditional-Breakpoints.md`, `Core-Dump-Analysis.md`, `Deadlock-Detection.md`, `Distributed-Log-Correlation.md`, `Error-Tracking.md`, `Logging-Levels.md`, `Memory-Errors.md`, `Minimal-Reproducible-Example.md`, `Postmortem.md`, `Race-Condition-Debugging.md`, `Remote-Debugging.md`, `Rubber-Duck-Debugging.md`, `Valgrind-AddressSanitizer.md`

### Engineering/DevOps

`Ansible.md`, `AWS-Core-Services.md`, `Container-Networking-Volumes.md`, `Docker-Compose.md`, `GCP-Azure-Overview.md`, `GitHub-Flow.md`, `Git-Internals.md`, `Helm.md`, `Jenkins-GitLab-CI.md`, `Kubernetes-Advanced.md`, `Logging-Systems.md`, `Serverless.md`

### Engineering/Performance

`Branch-Prediction.md`, `CDN-Caching.md`, `False-Sharing.md`, `JIT-Optimization.md`, `Lazy-Evaluation.md`, `Memoization-Caching.md`, `Memory-Layout.md`, `Practical-Complexity.md`, `SIMD-Vectorization.md`, `Thread-Pool-Tuning.md`

### Engineering/Security

`Network-Security.md`, `Zero-Knowledge-Proofs.md`

### Engineering/Software-Design

`Behavioral-Patterns.md`, `Creational-Patterns.md`, `Design-Principles.md`, `Structural-Patterns.md`

### Engineering/System-Design

`CDN.md`

### Engineering/Testing

`BDD.md`, `Boundary-Value-Analysis.md`, `Code-Coverage.md`, `Contract-Testing.md`, `Database-Testing.md`, `E2E-Testing.md`, `K6-JMeter.md`, `Load-Stress-Soak-Testing.md`, `Mutation-Testing.md`, `Static-Analysis-Linting.md`, `TDD.md`, `Testable-Design.md`, `Test-Doubles.md`, `UI-Test-Tools.md`, `Visual-Regression-Testing.md`

### Math/Calculus

`Integration.md`, `Multivariable-Integration.md`

### Math/Discrete

`Combinatorics.md`

### Math/Linear-Algebra

`Determinant.md`

### Math/Numerical-Methods

`Differentiation-Integration.md`, `Floating-Point.md`, `Interpolation.md`, `Numerical-Linear-Systems.md`, `ODE-Solvers.md`, `Root-Finding.md`

### Math/Optimization

`Linear-Programming.md`, `Quadratic-Programming.md`

### Math/Probability-Statistics

`Markov-Chains.md`

### Math/Real-Analysis

`Riemann-Integration.md`

### Systems/Computer-Architecture

`Parallel-Architecture.md`, `Virtual-Memory-Hardware.md`

### Systems/Databases

`Distributed-DB.md`, `NoSQL.md`, `Recovery.md`

### Systems/Distributed-Systems

`Distributed-System-Case-Studies.md`, `Distributed-Transactions.md`, `Message-Queues-Event-Streaming.md`

### Systems/Networks

`CDN-and-Load-Balancing.md`, `Network-Security-Basics.md`, `Physical-and-Link.md`

### Systems/Operating-Systems

`IO-and-Drivers.md`

---

## Deferred

현재 `Deferred` 문서는 없다. 목차에 유지하기 애매한 주제가 생기면 먼저 이 섹션에 넣고, 필요한 경우 섹션 README에서 제거한다.
