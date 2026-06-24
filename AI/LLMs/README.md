# 대규모 언어 모델 (Large Language Models)

> 수십억 개의 파라미터로 자연어를 이해하고 생성하는 모델.

**선수지식**: [AI/NLP/](../NLP/), [AI/Deep-Learning/](../Deep-Learning/), [AI/Reinforcement-Learning/](../Reinforcement-Learning/) (RLHF 파트)

**Last reviewed**: 2026-05-26

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

### 아키텍처

| 주제 | 파일 | Status |
|---|---|---|
| Transformer 심화 (위치 인코딩, KV 캐시) | [Transformer-Advanced.md](Transformer-Advanced.md) | Draft |
| GPT 계열 (GPT-1 → GPT-4, LLaMA) | [GPT-Family.md](GPT-Family.md) | Draft |
| BERT 계열 (마스크드 언어 모델) | [BERT-Family.md](BERT-Family.md) | Draft |
| T5 / Encoder-Decoder 모델 | [Encoder-Decoder.md](Encoder-Decoder.md) | Draft |

### 학습 방법

| 주제 | 파일 | Status |
|---|---|---|
| 사전학습 (Pretraining) | [Pretraining.md](Pretraining.md) | Draft |
| 인스트럭션 파인튜닝 (Instruction Tuning) | [Instruction-Tuning.md](Instruction-Tuning.md) | Draft |
| RLHF (인간 피드백 강화학습) | [RLHF.md](RLHF.md) | Draft |
| DPO (Direct Preference Optimization) | [DPO.md](DPO.md) | Draft |
| 효율적 파인튜닝 (LoRA, QLoRA, Adapter) | [PEFT.md](PEFT.md) | Draft |

### 추론 & 활용

| 주제 | 파일 | Status |
|---|---|---|
| 프롬프트 엔지니어링 | [Prompt-Engineering.md](Prompt-Engineering.md) | Draft |
| In-context Learning과 Few-shot | [In-Context-Learning.md](In-Context-Learning.md) | Draft |
| Chain-of-Thought (사고의 연쇄) | [Chain-of-Thought.md](Chain-of-Thought.md) | Draft |
| RAG (Retrieval-Augmented Generation) | [RAG.md](RAG.md) | Draft |
| LLM 에이전트와 Tool Use | [LLM-Agents.md](LLM-Agents.md) | Draft |

### 효율화 & 배포

| 주제 | 파일 | Status |
|---|---|---|
| 어텐션 효율화 (Flash Attention, Sparse Attention) | [Efficient-Attention.md](Efficient-Attention.md) | Draft |
| 양자화 (Quantization) | [Quantization.md](Quantization.md) | Draft |
| 지식 증류 (Knowledge Distillation) | [Distillation.md](Distillation.md) | Draft |
| vLLM, 추론 최적화 | [Inference-Optimization.md](Inference-Optimization.md) | Draft |

---

## 학습 순서

```text
Transformer-Advanced
        ↓
Pretraining → GPT-Family / BERT-Family / Encoder-Decoder
        ↓
Instruction-Tuning → RLHF → DPO → PEFT
        ↓
Prompt-Engineering → In-Context-Learning → Chain-of-Thought → RAG → LLM-Agents
        ↓
Efficient-Attention → Quantization → Distillation → Inference-Optimization
```

---

## 연관 섹션

- [AI/NLP/](../NLP/) — 선수지식
- [AI/Reinforcement-Learning/](../Reinforcement-Learning/) — RLHF
- [AI/MLOps/](../MLOps/) — 모델 배포 및 서빙
