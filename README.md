# Big F**king Book of Computer Science

> CS와 AI에 대한 모든 전공 지식을 담은 레포지토리.
> 학부 입문부터 대학원·연구자 수준까지, 이 레포 하나로 컴퓨터공학과 AI 전공 지식 전체를 습득하는 것이 목표다.
>
> **읽는 순서:** 선수 지식 의존 관계 → 같은 레벨 내에서 난이도 순으로 정렬되어 있다.
>
> 각 문서는 **개념 → 원리 → 복잡도 분석 → 구현(Python/C++/Java) → 응용 사례** 형식으로 작성된다.

---

## Computer Science

> 위에서 아래로 읽을수록 선수 지식이 쌓인다.

| # | 주제 | 핵심 선수 지식 | 내용 |
|---|------|--------------|------|
| 1 | [자료구조 (Data Structures)](CS/Data-Structures/) | 없음 | 배열, 연결리스트, 트리, 그래프, 고급 자료구조 등 |
| 2 | [알고리즘 (Algorithms)](CS/Algorithms/) | 자료구조 | 정렬, DP, 그래프, 네트워크 플로우, 근사/랜덤 알고리즘 등 |
| 3 | [컴퓨터 구조 (Computer Architecture)](CS/Computer-Architecture/) | 없음 | CPU, 파이프라이닝, 메모리 계층, SIMD, GPU 아키텍처 등 |
| 4 | [운영체제 (Operating Systems)](CS/Operating-Systems/) | 컴퓨터 구조 | 프로세스, 스레드, 메모리 관리, 가상화, 실시간 OS 등 |
| 5 | [컴퓨터 네트워크 (Computer Networks)](CS/Computer-Networks/) | 운영체제 | OSI, TCP/IP, HTTP, DNS, 라우팅, 혼잡 제어 등 |
| 6 | [데이터베이스 (Databases)](CS/Databases/) | 알고리즘, 운영체제 | SQL, 트랜잭션, 인덱싱, 쿼리 최적화, NoSQL 등 |
| 7 | [계산이론 (Theory of Computation)](CS/Theory-of-Computation/) | 이산수학 | 오토마타, 튜링 기계, 계산 가능성, 복잡도, P vs NP 등 |
| 8 | [프로그래밍 언어론 (Programming Languages)](CS/Programming-Languages/) | 계산이론 | 타입 이론, 람다 계산법, 형식 의미론, 의존 타입 등 |
| 9 | [컴파일러 (Compilers)](CS/Compilers/) | 계산이론, 언어론, 알고리즘 | 어휘/구문/의미 분석, IR, 최적화, JIT 등 |
| 10 | [소프트웨어 공학 (Software Engineering)](CS/Software-Engineering/) | 1~9 전반 | 디자인 패턴, SOLID, 아키텍처, 형식 검증, 테스팅 등 |
| 11 | [수치해석 (Numerical Methods)](CS/Numerical-Methods/) | 선형대수, 미적분 | 부동소수점, 선형계, 고유값, ODE/PDE, 최적화 등 |
| 12 | [병렬 컴퓨팅 (Parallel Computing)](CS/Parallel-Computing/) | 컴퓨터 구조, 운영체제, 알고리즘 | PRAM, OpenMP, MPI, CUDA, 병렬 알고리즘 등 |
| 13 | [분산 시스템 (Distributed Systems)](CS/Distributed-Systems/) | 운영체제, 네트워크, 데이터베이스 | CAP, Paxos, Raft, 분산 DB, 합의 알고리즘 등 |
| 14 | [암호학 & 보안 (Cryptography & Security)](CS/Cryptography-and-Security/) | 알고리즘, 네트워크, 계산이론 | 대칭/공개키 암호, 영지식 증명, 동형암호, 양자 후 암호화 등 |
| 15 | [양자 컴퓨팅 (Quantum Computing)](CS/Quantum-Computing/) | 선형대수, 계산이론, 물리학 기초 | 큐비트, 양자 게이트, Shor/Grover 알고리즘, 오류 정정 등 |

---

## Artificial Intelligence

> 위에서 아래로 읽을수록 선수 지식이 쌓인다.

| # | 주제 | 핵심 선수 지식 | 내용 |
|---|------|--------------|------|
| 1 | [수학 기초 (Math Foundations)](AI/Math-Foundations/) | 없음 | 선형대수, 확률통계, 미적분, 측도론, 정보이론 등 |
| 2 | [최적화 이론 (Optimization Theory)](AI/Optimization-Theory/) | 수학 기초 | 볼록 최적화, KKT, 경사하강법, SGD 변형, 비볼록 최적화 등 |
| 3 | [머신러닝 (Machine Learning)](AI/Machine-Learning/) | 수학 기초, 최적화 | 지도/비지도학습, SVM, 트리, 앙상블, 차원 축소 등 |
| 4 | [확률적 그래피컬 모델 (PGM)](AI/Probabilistic-Graphical-Models/) | 확률론, 머신러닝 | 베이지안 네트워크, MRF, HMM, 변분 추론, MCMC 등 |
| 5 | [이론적 머신러닝 (Theoretical ML)](AI/Theoretical-ML/) | 확률론, 머신러닝 | PAC 학습, VC 차원, Rademacher, 온라인 학습, 밴딧 등 |
| 6 | [딥러닝 (Deep Learning)](AI/Deep-Learning/) | 머신러닝, 최적화, 선형대수 | 신경망, CNN, RNN, Transformer, GAN, Diffusion 등 |
| 7 | [자연어처리 (NLP)](AI/NLP/) | 딥러닝 (특히 Transformer) | 임베딩, BERT, GPT, 기계 번역, 정보 추출 등 |
| 8 | [컴퓨터 비전 (Computer Vision)](AI/Computer-Vision/) | 딥러닝 (특히 CNN) | 합성곱, 객체 탐지, 세그멘테이션, 3D 비전 등 |
| 9 | [강화학습 (Reinforcement Learning)](AI/Reinforcement-Learning/) | 머신러닝, 최적화, 확률론 | MDP, Q-Learning, PPO, Actor-Critic, MARL 등 |
| 10 | [인과 추론 (Causal Inference)](AI/Causal-Inference/) | 확률론, 통계, 머신러닝 | 잠재적 결과, DAG, do-계산법, 처치 효과 추정 등 |
| 11 | [최신 연구 동향 (Advanced Topics)](AI/Advanced-Topics/) | 딥러닝, NLP/CV/RL | LLM, Diffusion, 멀티모달, 메타 학습, AI 안전성 등 |

---

## 문서 구성 형식

```
# 주제명

## 개념 (Concept)
## 원리 및 동작 방식 (How It Works)
## 복잡도 분석 (Complexity)
## 구현 (Implementation) — Python / C++ / Java
## 응용 사례 (Applications)
```
