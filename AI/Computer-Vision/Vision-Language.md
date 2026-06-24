# Vision-Language Model

- Level: Advanced
- Prerequisites: [AI/Deep-Learning/Transformer.md](../Deep-Learning/Transformer.md), [AI/NLP/Language-Model-Basics.md](../NLP/Language-Model-Basics.md), [AI/Computer-Vision/Image-Classification.md](Image-Classification.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

Vision-Language Model(VLM)은 이미지·영상과 텍스트를 같은 문제 안에서 다루는 모델이다. Image-text retrieval, captioning, visual question answering, grounding, multimodal chat 등이 대표 과제다.

## 직관 (Intuition)

이미지 모델이 "무엇이 보이는가"를 알고 언어 모델이 "어떻게 말하는가"를 안다면, VLM은 둘 사이에 다리를 놓는다. 고양이 사진과 "소파 위의 고양이"라는 문장을 가까운 표현으로 맞춘다.

## 이론 (Theory)

Contrastive image-text pretraining은 matching되는 이미지와 문장의 embedding을 가깝게, 다른 pair는 멀게 만든다. Captioning과 VQA는 visual token을 language model의 context로 넣거나 cross-attention으로 결합한다.

ViT는 이미지를 patch token sequence로 바꾸어 Transformer에 넣는다. Grounding 과제에서는 텍스트 span과 image region의 alignment가 중요하다. Multimodal 모델은 modality별 encoder, projection layer, fusion module의 설계가 핵심이다.

## 구현 (Implementation)

```python
def contrastive_score(image_embedding, text_embedding):
    dot = sum(i * t for i, t in zip(image_embedding, text_embedding))
    return dot / (norm(image_embedding) * norm(text_embedding))
```

Embedding은 보통 normalize한 뒤 cosine similarity나 scaled dot product로 비교한다.

## 복잡도 (Complexity)

Contrastive training은 batch 안의 negative 수가 중요해 큰 batch와 memory가 필요하다. Cross-attention 기반 fusion은 image token과 text token 수가 늘수록 비용이 증가한다.

## 응용 (Applications)

- text-image retrieval
- image captioning
- visual question answering
- OCR·document understanding
- referring expression grounding

## 흔한 오해 (Common Misunderstandings)

- 이미지와 텍스트를 함께 학습했다고 세밀한 공간 관계를 항상 이해하는 것은 아니다.
- Caption이 그럴듯해도 이미지에 없는 내용을 hallucinate할 수 있다.
- Contrastive pretraining은 negative 구성과 데이터 품질에 민감하다.
- VLM의 안전성 문제는 텍스트 모델과 이미지 모델의 문제가 함께 섞인다.

## TMI

- Zero-shot classification은 class 이름을 prompt text로 만들어 image embedding과 비교하는 식으로 가능하다.
- Fine-grained grounding은 이미지-문장 pair보다 더 촘촘한 annotation이 필요할 수 있다.
- Video-language model은 시간 축 때문에 token budget 문제가 더 커진다.

## 연습 / 확인 문제 (Exercises)

- Contrastive image-text 학습의 positive/negative pair를 정의하라.
- Captioning과 VQA의 입력·출력 차이를 비교하라.
- VLM hallucination을 평가하는 테스트셋 설계를 제안하라.

## 이어서 읽기 (Reading Path)

- 이전: [Transformer](../Deep-Learning/Transformer.md), [영상 이해](Video-Understanding.md)
- 다음: [이미지 생성](Image-Generation.md), [3D 비전](3D-Vision.md)

## 참조 (References)

- [AI/Deep-Learning/Transformer.md](../Deep-Learning/Transformer.md)
- [AI/NLP/Language-Model-Basics.md](../NLP/Language-Model-Basics.md)
- [Reference/Papers.md](../../Reference/Papers.md)
