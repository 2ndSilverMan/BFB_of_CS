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
| AI 정렬 문제 개요 — 왜 어려운가 | Alignment-Overview.md | Planned |
| 보상 해킹과 목표 오명세 (Goal Misgeneralization) | Reward-Hacking.md | Planned |
| RLHF와 Constitutional AI | RLHF-Constitutional-AI.md | Planned |
| 인간 피드백의 한계와 reward model collapse | Feedback-Limitations.md | Planned |
| 슈퍼정렬 (Superalignment) 연구 방향 | Superalignment.md | Planned |

### 해석 가능성 (Interpretability)

| 주제 | 파일 | Status |
|---|---|---|
| 기계적 해석 가능성 (Mechanistic Interpretability) | Mechanistic-Interpretability.md | Planned |
| 활성화 패치와 인과적 개입 | Activation-Patching.md | Planned |
| Probing Classifiers | Probing-Classifiers.md | Planned |
| Sparse Autoencoder를 이용한 특성 분해 | Sparse-Autoencoder.md | Planned |
| Attention 시각화의 한계 | Attention-Visualization.md | Planned |

### 강건성 (Robustness)

| 주제 | 파일 | Status |
|---|---|---|
| 적대적 예제 (Adversarial Examples) | Adversarial-Examples.md | Planned |
| 분포 외 일반화 (OOD Generalization) | OOD-Generalization.md | Planned |
| 인증된 강건성 (Certified Robustness) | Certified-Robustness.md | Planned |
| 데이터 오염 공격 (Poisoning Attacks) | Poisoning-Attacks.md | Planned |

### 평가와 벤치마크

| 주제 | 파일 | Status |
|---|---|---|
| AI 역량 평가 — MMLU, BIG-Bench | Capability-Evaluation.md | Planned |
| 위험 역량 평가 (Dangerous Capability Evaluation) | Dangerous-Capability-Evaluation.md | Planned |
| Red-Teaming 방법론 | Red-Teaming.md | Planned |
| Scalable Oversight | Scalable-Oversight.md | Planned |

### 거버넌스 & 사회적 영향

| 주제 | 파일 | Status |
|---|---|---|
| AI 위험 분류 체계 | AI-Risk-Classification.md | Planned |
| 규제 프레임워크 — EU AI Act 등 | AI-Regulation.md | Planned |
| 공정성과 편향 (Fairness & Bias) | Fairness-Bias.md | Planned |

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
