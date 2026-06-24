# 인과 추론 (Causal Inference)

> 상관관계를 넘어 인과 관계를 식별하고 추론하는 방법.

**선수지식**: [AI/PGMs/](../PGMs/), [Math/Probability-Statistics/](../../Math/Probability-Statistics/)

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

### 기초 개념

| 주제 | 파일 | Status |
|---|---|---|
| 상관 vs 인과 | [Correlation-vs-Causation.md](Correlation-vs-Causation.md) | Draft |
| 교란 변수 (Confounding) | [Confounding.md](Confounding.md) | Draft |
| 잠재 결과 프레임워크 (Potential Outcomes) | [Potential-Outcomes.md](Potential-Outcomes.md) | Draft |

### 구조적 인과 모델 (SCM)

| 주제 | 파일 | Status |
|---|---|---|
| 구조적 인과 모델 (SCM) | [SCM.md](SCM.md) | Draft |
| 인과 DAG와 d-분리 | [Causal-DAG.md](Causal-DAG.md) | Draft |
| do-calculus | [Do-Calculus.md](Do-Calculus.md) | Draft |
| 식별가능성 (Identifiability) | [Identifiability.md](Identifiability.md) | Draft |

### 인과 효과 추정

| 주제 | 파일 | Status |
|---|---|---|
| 개입 (Intervention)과 ATE | [Intervention.md](Intervention.md) | Draft |
| 반사실 (Counterfactual) | [Counterfactual.md](Counterfactual.md) | Draft |
| 매개 분석 (Mediation Analysis) | [Mediation.md](Mediation.md) | Draft |

### 실증적 방법

| 주제 | 파일 | Status |
|---|---|---|
| 무작위 실험 (RCT) | [RCT.md](RCT.md) | Draft |
| 자연 실험과 도구 변수 (IV) | [Instrumental-Variables.md](Instrumental-Variables.md) | Draft |
| 이중 차분법 (Difference-in-Differences) | [DiD.md](DiD.md) | Draft |
| 회귀 불연속 설계 (RDD) | [RDD.md](RDD.md) | Draft |

### ML과의 결합

| 주제 | 파일 | Status |
|---|---|---|
| 인과적 머신러닝 | [Causal-ML.md](Causal-ML.md) | Draft |
| 인과적 표현 학습 | [Causal-Representation.md](Causal-Representation.md) | Draft |

---

## 학습 순서

```text
Correlation-vs-Causation → Confounding
        ↓
Potential-Outcomes / SCM → Causal-DAG → Do-Calculus → Identifiability
        ↓
Intervention → Counterfactual → Mediation
        ↓
RCT → Instrumental-Variables → DiD → RDD
        ↓
Causal-ML → Causal-Representation
```

---

## 연관 섹션

- [AI/PGMs/](../PGMs/) — 선수지식
- [AI/AI-Safety/](../AI-Safety/) — 인과 추론과 AI 정렬
- [Math/Probability-Statistics/](../../Math/Probability-Statistics/) — 통계적 기반
