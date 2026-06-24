# 질문 응답 (Question Answering, QA)

- Level: Advanced
- Prerequisites: [BERT.md](BERT.md), [GPT.md](GPT.md), [Relation-Extraction.md](Relation-Extraction.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

질문 응답은 자연어 질문에 대해 정답을 찾거나 생성하는 NLP 작업이다. 문서에서 span을 추출하는 extractive QA, 여러 문서를 검색해 답하는 open-domain QA, 답변을 생성하는 generative QA가 있다.

## 직관 (Intuition)

사람이 질문을 받으면 먼저 관련 자료를 찾고, 그 안에서 근거 문장을 읽고, 필요한 경우 답을 요약해 말한다. QA 시스템도 retrieval, reading, generation, grounding이 결합되는 경우가 많다.

## 이론 (Theory)

대표 설정은 다음과 같다.

- Extractive QA: passage와 question이 주어지고 answer span의 시작/끝 위치를 예측한다.
- Multiple-choice QA: 후보 답 중 하나를 고른다.
- Open-domain QA: corpus에서 관련 문서를 검색한 뒤 답한다.
- Generative QA: 모델이 자연어 답변을 생성한다.

평가에는 exact match, token-level F1, answer faithfulness, citation correctness가 쓰인다. 생성형 QA에서는 hallucination과 근거 불일치가 핵심 위험이다.

## 구현 (Implementation)

Extractive QA는 시작/끝 위치 점수를 고르는 문제로 볼 수 있다.

```python
def best_span(start_scores, end_scores, max_len=10):
    best = None
    best_score = float("-inf")
    for i, s in enumerate(start_scores):
        for j in range(i, min(len(end_scores), i + max_len)):
            score = s + end_scores[j]
            if score > best_score:
                best = (i, j)
                best_score = score
    return best
```

Open-domain QA에서는 retrieval 품질이 reader/generator 성능만큼 중요하다.

## 복잡도 (Complexity)

Extractive QA는 passage 길이에 따라 transformer 비용이 증가한다. Open-domain QA는 검색 인덱스 구축, top-k retrieval, reranking, generation 비용이 추가된다. 긴 문서 QA는 chunking과 context selection이 병목이다.

## 응용 (Applications)

- 문서 검색 기반 질의응답
- 고객지원 챗봇
- 법률/의료 문서 QA
- RAG 시스템의 reader/generator

## 흔한 오해 (Common Misunderstandings)

- 답변이 자연스럽다고 근거가 맞는 것은 아니다.
- Retriever가 관련 문서를 못 찾으면 generator가 맞히기 어렵다.
- Exact match는 표현이 다른 정답을 과소평가할 수 있다.
- QA 모델은 질문의 전제를 검증하지 않으면 잘못된 질문에도 답을 만들어낼 수 있다.

## TMI

- SQuAD는 extractive QA의 대표 benchmark다.
- Open-domain QA는 dense retrieval 발전과 함께 크게 발전했다.
- RAG에서는 답변 품질뿐 아니라 citation과 abstention 정책이 중요하다.

## 연습 / 확인 문제 (Exercises)

- Extractive QA와 generative QA의 차이를 설명하라.
- Open-domain QA에서 retriever와 reader의 역할을 구분하라.
- QA 평가에서 exact match의 한계를 말하라.

## 이어서 읽기 (Reading Path)

- 이전: [기계 번역](Machine-Translation.md)
- 다음: [텍스트 요약](Summarization.md)

## 참조 (References)

- [BERT.md](BERT.md)
- [GPT.md](GPT.md)
- [Relation-Extraction.md](Relation-Extraction.md)
- [Reference/Books.md](../../Reference/Books.md)
