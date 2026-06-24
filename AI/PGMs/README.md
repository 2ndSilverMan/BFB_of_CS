# 확률 그래프 모델 (Probabilistic Graphical Models)

> 확률 변수 간의 의존 구조를 그래프로 표현하고 추론하는 방법.

**선수지식**: [Math/Probability-Statistics/](../../Math/Probability-Statistics/), [Math/Discrete/](../../Math/Discrete/) (그래프 이론)

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

### 기초

| 주제 | 파일 | Status |
|---|---|---|
| 그래프 이론 복습 (방향/무방향 그래프) | [Graph-Review.md](Graph-Review.md) | Draft |
| 인수 분해와 조건부 독립 | [Factorization.md](Factorization.md) | Draft |

### 방향성 그래프 모델 (Bayesian Networks)

| 주제 | 파일 | Status |
|---|---|---|
| 베이지안 네트워크 구조와 파라미터 | [Bayesian-Networks.md](Bayesian-Networks.md) | Draft |
| d-분리 (d-separation) | [d-Separation.md](d-Separation.md) | Draft |
| 나이브 베이즈 | [Naive-Bayes.md](Naive-Bayes.md) | Draft |
| Hidden Markov Model (HMM) | [HMM.md](HMM.md) | Draft |

### 무방향성 그래프 모델 (MRF)

| 주제 | 파일 | Status |
|---|---|---|
| 마르코프 랜덤 필드 (MRF) | [MRF.md](MRF.md) | Draft |
| 클리크와 포텐셜 함수 | [Cliques.md](Cliques.md) | Draft |
| 조건부 랜덤 필드 (CRF) | [CRF.md](CRF.md) | Draft |

### 추론 알고리즘

| 주제 | 파일 | Status |
|---|---|---|
| 변수 소거 (Variable Elimination) | [Variable-Elimination.md](Variable-Elimination.md) | Draft |
| 신뢰 전파 (Belief Propagation) | [Belief-Propagation.md](Belief-Propagation.md) | Draft |
| 변분 추론 (Variational Inference) | [Variational-Inference.md](Variational-Inference.md) | Draft |
| MCMC 샘플링 | [MCMC.md](MCMC.md) | Draft |
| EM 알고리즘 | [EM-Algorithm.md](EM-Algorithm.md) | Draft |

---

## 학습 순서

```text
Graph-Review → Factorization → Bayesian-Networks → d-Separation
       ↓
Naive-Bayes / HMM / MRF / CRF
       ↓
Variable-Elimination → Belief-Propagation → Variational-Inference / MCMC
       ↓
EM-Algorithm
```

---

## 연관 섹션

- [AI/Causal-Inference/](../Causal-Inference/) — PGM에서 인과 관계로
- [AI/Machine-Learning/](../Machine-Learning/) — 나이브 베이즈, GMM
- [Math/Probability-Statistics/](../../Math/Probability-Statistics/) — 선수지식
