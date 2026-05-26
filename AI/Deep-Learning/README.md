# 딥러닝 (Deep Learning)

> 다층 신경망으로 복잡한 패턴을 학습하는 방법.

**선수지식**: [AI/Machine-Learning/](../Machine-Learning/), [Math/Linear-Algebra/](../../Math/Linear-Algebra/), [Math/Calculus/](../../Math/Calculus/)

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

### 기초

| 주제 | 파일 | Status |
|---|---|---|
| 퍼셉트론과 다층 신경망 (MLP) | MLP.md | Planned |
| 역전파 (Backpropagation) | Backpropagation.md | Planned |
| 활성화 함수 | Activation-Functions.md | Planned |
| 손실 함수 | Loss-Functions.md | Planned |
| 배치 정규화 / 레이어 정규화 | Normalization-Layers.md | Planned |
| 드롭아웃 | Dropout.md | Planned |

### 아키텍처

| 주제 | 파일 | Status |
|---|---|---|
| CNN (합성곱 신경망) | CNN.md | Planned |
| RNN / LSTM / GRU | RNN-LSTM-GRU.md | Planned |
| Transformer | Transformer.md | Planned |
| 어텐션 메커니즘 | Attention.md | Planned |
| 그래프 신경망 (GNN) | GNN.md | Planned |

### 학습 기법

| 주제 | 파일 | Status |
|---|---|---|
| 전이 학습 (Transfer Learning) | Transfer-Learning.md | Planned |
| 파인튜닝 | Fine-Tuning.md | Planned |
| 자기 지도 학습 (Self-supervised) | Self-Supervised.md | Planned |

---

## 학습 순서

```text
MLP → Backpropagation → Activation-Functions / Loss-Functions
       ↓
Normalization-Layers → Dropout
       ↓
CNN / RNN-LSTM-GRU → Attention → Transformer
       ↓
Transfer-Learning → Fine-Tuning → Self-Supervised / GNN
```

---

## 연관 섹션

- [AI/NLP/](../NLP/), [AI/Computer-Vision/](../Computer-Vision/) — 응용
- [AI/Generative-Models/](../Generative-Models/) — 심화
