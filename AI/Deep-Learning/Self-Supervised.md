# 자기 지도 학습 (Self-Supervised Learning)

- Level: Advanced
- Prerequisites: [AI/Deep-Learning/Transformer.md](Transformer.md), [AI/Deep-Learning/CNN.md](CNN.md), [AI/Machine-Learning/Dimensionality-Reduction.md](../Machine-Learning/Dimensionality-Reduction.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

자기 지도 학습은 사람이 직접 붙인 라벨 없이 데이터 자체에서 학습 신호를 만들어 표현을 학습하는 방법이다. 입력의 일부를 가리고 맞히거나, 서로 다른 augmentation view가 같은 의미를 갖도록 가깝게 만드는 식으로 pretext task를 만든다.

## 직관 (Intuition)

교사가 정답을 붙여주지 않아도, 문장의 빈칸을 맞히거나 이미지의 두 변형이 같은 물체라는 사실을 이용하면 유용한 표현을 배울 수 있다. 핵심은 “라벨은 없지만 데이터 안에 구조는 있다”는 점이다.

## 이론 (Theory)

대표 방식은 세 부류로 볼 수 있다.

- predictive: 입력 일부나 미래를 예측한다. 예: masked language modeling, next-token prediction
- contrastive: positive pair는 가깝게, negative pair는 멀게 만든다. 예: InfoNCE
- non-contrastive/distillation: negative 없이 teacher/student 또는 stop-gradient 구조로 collapse를 피한다.

학습된 encoder $f_\theta(x)$는 downstream task에서 linear probing, fine-tuning, retrieval, generation 등에 사용된다. 좋은 pretext task는 downstream에 필요한 불변성과 정보를 표현에 남겨야 한다.

## 구현 (Implementation)

contrastive 학습의 장난감 목적은 positive similarity를 negative보다 크게 만드는 것이다.

```python
import math


def softmax(xs):
    exps = [math.exp(x) for x in xs]
    z = sum(exps)
    return [e / z for e in exps]


def contrastive_loss(pos_score, neg_scores, temperature=0.1):
    logits = [pos_score / temperature] + [s / temperature for s in neg_scores]
    p_pos = softmax(logits)[0]
    return -math.log(p_pos)


print(round(contrastive_loss(0.8, [0.2, 0.1, 0.4]), 3))
```

실제 구현에서는 augmentation, batch construction, projection head, normalization이 성능에 큰 영향을 준다.

## 복잡도 (Complexity)

자기 지도 학습은 대규모 unlabeled data를 사용하므로 사전학습 비용이 크다. contrastive 방식은 batch 내 negative 수에 따라 메모리와 통신 비용이 커질 수 있고, masked/predictive 방식은 모델 크기와 sequence length에 민감하다.

## 응용 (Applications)

- 언어 모델 사전학습
- 이미지 표현 학습과 transfer learning
- 음성·영상·멀티모달 representation learning
- 라벨이 적은 downstream task의 성능 개선

## 흔한 오해 (Common Misunderstandings)

- 라벨이 전혀 필요 없다는 뜻은 아니다. downstream 평가나 alignment에는 라벨/피드백이 필요할 수 있다.
- pretext task 성능이 높다고 downstream 성능이 항상 좋은 것은 아니다.
- augmentation 선택은 데이터 의미를 바꿀 수 있어 신중해야 한다.
- negative sample이 항상 필요한 것은 아니다. non-contrastive 방법도 있다.

## TMI

- BERT의 masked language modeling과 GPT의 next-token prediction은 대표적인 자기 지도 학습 신호다.
- SimCLR류 방법은 큰 batch와 강한 augmentation의 중요성을 보여줬다.
- collapse는 모든 입력이 같은 representation으로 가는 실패 모드이며, 많은 SSL 방법이 이를 피하는 장치를 둔다.

## 연습 / 확인 문제 (Exercises)

- masked prediction과 contrastive learning의 학습 신호 차이를 설명하라.
- 이미지 augmentation이 semantic label을 바꿀 수 있는 예를 들어라.
- linear probing과 fine-tuning의 평가 의미를 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [전이 학습](Transfer-Learning.md), [파인튜닝](Fine-Tuning.md)
- 다음: [AI/Generative-Models/](../Generative-Models/)

## 참조 (References)

- [AI/Deep-Learning/Transformer.md](Transformer.md)
- [AI/Deep-Learning/CNN.md](CNN.md)
- [AI/Machine-Learning/Dimensionality-Reduction.md](../Machine-Learning/Dimensionality-Reduction.md)
- [Reference/Books.md](../../Reference/Books.md)
