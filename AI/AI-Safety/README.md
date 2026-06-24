# AI 안전성 (AI Safety)

> AI 시스템이 의도대로, 안전하게 동작하도록 보장하는 이론과 기술.

**선수지식**: [AI/Deep-Learning/](../Deep-Learning/), [AI/Theoretical-ML/](../Theoretical-ML/)

**Last reviewed**: 2026-05-26

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

### 정렬 문제 (Alignment)

| 주제 | 파일 | Status |
|---|---|---|
| AI 정렬 문제 개요 — 왜 어려운가 | [Alignment-Overview.md](Alignment-Overview.md) | Draft |
| 보상 해킹과 목표 오명세 (Goal Misgeneralization) | [Reward-Hacking.md](Reward-Hacking.md) | Draft |
| RLHF와 Constitutional AI | [RLHF-Constitutional-AI.md](RLHF-Constitutional-AI.md) | Draft |
| 인간 피드백의 한계와 reward model collapse | [Feedback-Limitations.md](Feedback-Limitations.md) | Draft |
| 슈퍼정렬 (Superalignment) 연구 방향 | [Superalignment.md](Superalignment.md) | Draft |

### 해석 가능성 (Interpretability)

| 주제 | 파일 | Status |
|---|---|---|
| 기계적 해석 가능성 (Mechanistic Interpretability) | [Mechanistic-Interpretability.md](Mechanistic-Interpretability.md) | Draft |
| 활성화 패치와 인과적 개입 | [Activation-Patching.md](Activation-Patching.md) | Draft |
| Probing Classifiers | [Probing-Classifiers.md](Probing-Classifiers.md) | Draft |
| Sparse Autoencoder를 이용한 특성 분해 | [Sparse-Autoencoder.md](Sparse-Autoencoder.md) | Draft |
| Attention 시각화의 한계 | [Attention-Visualization.md](Attention-Visualization.md) | Draft |

### 강건성 (Robustness)

| 주제 | 파일 | Status |
|---|---|---|
| 적대적 예제 (Adversarial Examples) | [Adversarial-Examples.md](Adversarial-Examples.md) | Draft |
| 분포 외 일반화 (OOD Generalization) | [OOD-Generalization.md](OOD-Generalization.md) | Draft |
| 인증된 강건성 (Certified Robustness) | [Certified-Robustness.md](Certified-Robustness.md) | Draft |
| 데이터 오염 공격 (Poisoning Attacks) | [Poisoning-Attacks.md](Poisoning-Attacks.md) | Draft |

### 평가와 벤치마크

| 주제 | 파일 | Status |
|---|---|---|
| AI 역량 평가 — MMLU, BIG-Bench | [Capability-Evaluation.md](Capability-Evaluation.md) | Draft |
| 위험 역량 평가 (Dangerous Capability Evaluation) | [Dangerous-Capability-Evaluation.md](Dangerous-Capability-Evaluation.md) | Draft |
| Red-Teaming 방법론 | [Red-Teaming.md](Red-Teaming.md) | Draft |
| Scalable Oversight | [Scalable-Oversight.md](Scalable-Oversight.md) | Draft |

### 거버넌스 & 사회적 영향

| 주제 | 파일 | Status |
|---|---|---|
| AI 위험 분류 체계 | [AI-Risk-Classification.md](AI-Risk-Classification.md) | Draft |
| 규제 프레임워크 — EU AI Act 등 | [AI-Regulation.md](AI-Regulation.md) | Draft |
| 공정성과 편향 (Fairness & Bias) | [Fairness-Bias.md](Fairness-Bias.md) | Draft |

---

## 학습 순서

```text
정렬 문제 개요
       ↓
해석 가능성 ← → 강건성
       ↓
평가 방법론
       ↓
거버넌스 & 사회적 맥락
```

---

## 연관 섹션

- [AI/Theoretical-ML/](../Theoretical-ML/) — 일반화 이론, PAC 학습 (강건성 기반)
- [AI/LLMs/](../LLMs/) — RLHF, Constitutional AI의 실제 적용
- [AI/Causal-Inference/](../Causal-Inference/) — 인과적 개입 방법론
- [Engineering/Security/](../../Engineering/Security/) — 적대적 공격의 보안 관점
