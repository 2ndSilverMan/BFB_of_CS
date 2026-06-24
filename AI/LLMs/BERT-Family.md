# BERT 계열 (BERT Family)

- Level: Advanced
- Prerequisites: [AI/LLMs/Pretraining.md](Pretraining.md), [AI/NLP/BERT.md](../NLP/BERT.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

BERT 계열은 encoder-only Transformer를 masked language modeling으로 사전학습한 언어 모델 계열이다. 양방향 문맥 표현을 얻어 분류, 추출형 QA, NER, retrieval reranking 등에 강하다.

## 직관 (Intuition)

GPT가 왼쪽에서 오른쪽으로 이어 쓰는 모델이라면, BERT는 문장 중간의 빈칸을 양쪽 문맥을 보고 맞히는 모델이다. 그래서 생성보다는 입력 문장을 깊게 이해해 표현하는 데 적합하다.

## 이론 (Theory)

Masked LM은 일부 토큰을 `[MASK]`로 가리고 원래 토큰을 예측한다. Encoder self-attention은 모든 위치가 서로를 볼 수 있어 bidirectional context를 사용한다.

Sentence pair classification, token classification, span extraction 같은 downstream task는 `[CLS]` representation이나 token representation 위에 head를 얹어 fine-tuning한다.

## 구현 (Implementation)

```python
task_heads = {
    "classification": "use CLS embedding",
    "token_classification": "use each token embedding",
    "span_qa": "predict start and end positions",
}
```

Encoder-only 모델은 autoregressive generation에는 직접 맞지 않다.

## 복잡도 (Complexity)

Attention 비용은 sequence length의 제곱에 비례한다. Fine-tuning 비용은 decoder LLM보다 작을 수 있지만 task별 labeled data와 calibration이 중요하다.

## 응용 (Applications)

- 문서 분류·감성 분석
- NER·정보 추출
- 추출형 질문응답
- 검색 reranking과 embedding 모델의 기반

## 흔한 오해 (Common Misunderstandings)

- BERT는 GPT보다 낡았다기보다 목적이 다르다.
- `[MASK]` pretraining과 실제 입력 사이에는 mismatch가 있다.
- 문장 embedding은 pooling 방식에 따라 품질이 크게 달라진다.
- Encoder-only 모델이 긴 생성에 자연스럽게 맞는 것은 아니다.

## TMI

- RoBERTa류는 pretraining recipe가 모델 성능에 얼마나 중요한지 보여 준다.
- DistilBERT류는 encoder 모델 distillation의 대표 사례다.
- Cross-encoder reranker는 느리지만 query-document 상호작용을 세밀하게 본다.

## 연습 / 확인 문제 (Exercises)

- Causal LM과 masked LM의 attention mask 차이를 설명하라.
- BERT가 NER에 잘 맞는 이유를 말하라.
- Cross-encoder와 bi-encoder retrieval의 tradeoff를 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [BERT](../NLP/BERT.md), [사전학습](Pretraining.md)
- 다음: [Encoder-Decoder](Encoder-Decoder.md), [Distillation](Distillation.md)

## 참조 (References)

- [AI/NLP/BERT.md](../NLP/BERT.md)
- [Reference/Papers.md](../../Reference/Papers.md)
