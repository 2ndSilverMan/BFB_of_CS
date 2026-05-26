# 자연어 처리 (Natural Language Processing)

> 텍스트를 이해하고 생성하는 방법.

**선수지식**: [AI/Deep-Learning/](../Deep-Learning/), [Math/Probability-Statistics/](../../Math/Probability-Statistics/)

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

### 기초

| 주제 | 파일 | Status |
|---|---|---|
| 텍스트 전처리 (토크나이제이션, 정규화) | Text-Preprocessing.md | Planned |
| 언어 모델 기초 (N-gram, 퍼플렉서티) | Language-Model-Basics.md | Planned |
| 단어 임베딩 (Word2Vec, GloVe, FastText) | Word-Embeddings.md | Planned |

### 신경망 기반 NLP

| 주제 | 파일 | Status |
|---|---|---|
| RNN / LSTM / GRU for NLP | RNN-for-NLP.md | Planned |
| 어텐션 메커니즘 | Attention-in-NLP.md | Planned |
| Transformer for NLP | Transformer-NLP.md | Planned |
| BERT와 사전학습 언어 모델 | BERT.md | Planned |
| GPT 계열과 인과적 언어 모델 | GPT.md | Planned |

### 태스크별 응용

| 주제 | 파일 | Status |
|---|---|---|
| 텍스트 분류 (감성 분석 포함) | Text-Classification.md | Planned |
| 개체명 인식 (NER) | NER.md | Planned |
| 관계 추출 | Relation-Extraction.md | Planned |
| 기계 번역 | Machine-Translation.md | Planned |
| 질문 응답 (QA) | Question-Answering.md | Planned |
| 텍스트 요약 | Summarization.md | Planned |

---

## 학습 순서

```text
Text-Preprocessing → Language-Model-Basics → Word-Embeddings
        ↓
RNN-for-NLP → Attention-in-NLP → Transformer-NLP
        ↓
BERT / GPT
        ↓
Text-Classification / NER / Relation-Extraction / Machine-Translation / Question-Answering / Summarization
```

---

## 연관 섹션

- [AI/Deep-Learning/](../Deep-Learning/) — 선수지식
- [AI/LLMs/](../LLMs/) — NLP의 심화: 대규모 언어 모델
- [AI/Generative-Models/](../Generative-Models/) — 텍스트 생성
