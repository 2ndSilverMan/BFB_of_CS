# 전이 학습 (Transfer Learning)

- Level: Intermediate
- Prerequisites: [AI/Deep-Learning/CNN.md](CNN.md), [AI/Deep-Learning/Backpropagation.md](Backpropagation.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

transfer learning은 한 과제(source)에서 학습한 표현을 다른 과제(target)에 재사용하는 방법이다. 보통 대규모 데이터로 미리 학습한(pretrained) 모델의 가중치를 가져와, 적은 데이터의 새 과제에 맞춰 일부 또는 전체를 다시 학습한다.

## 직관 (Intuition)

밑바닥부터 학습하면 모델은 "에지·질감 같은 저수준 특징"부터 다시 배워야 한다. 그런데 이런 특징은 과제가 달라도 상당히 공통적이다. 이미 좋은 표현을 가진 모델에서 출발하면, 적은 데이터로도 빠르고 안정적으로 수렴한다. 사람도 기타를 칠 줄 알면 우쿨렐레를 더 빨리 배우는 것과 같다.

## 이론 (Theory)

신경망을 feature extractor $f_\theta$와 head $g_\phi$로 나누면 예측은 $g_\phi(f_\theta(x))$다. 전이 전략은 어디까지 고정(freeze)하고 어디부터 갱신할지로 갈린다.

- **feature extraction**: $\theta$를 freeze하고 새 head $\phi$만 학습. 데이터가 매우 적을 때.
- **fine-tuning**: $\theta$의 일부 또는 전부를 작은 learning rate로 함께 갱신. 데이터가 어느 정도 있을 때.

source와 target의 분포 차이(domain shift)가 클수록 전이 이득이 줄고, 음의 전이(negative transfer)가 날 수도 있다. 일반적으로 저수준 층일수록 과제 독립적이라 freeze하기 좋고, 고수준 층일수록 과제 특화라 갱신 대상이 된다.

## 구현 (Implementation)

```python
model = load_pretrained("resnet50")     # source 과제로 학습된 가중치

for p in model.backbone.parameters():   # feature extractor 고정
    p.requires_grad = False

model.head = NewHead(num_classes=10)    # target 과제용 head 교체
optimizer = SGD(model.head.parameters(), lr=1e-3)
# 이후 일부 backbone을 풀어(unfreeze) 작은 lr로 fine-tuning할 수 있다
```

## 복잡도 (Complexity)

학습 비용은 갱신하는 파라미터 수와 backprop 깊이에 비례한다. feature extraction은 backbone gradient가 필요 없어 가장 싸고, 전체 fine-tuning은 from-scratch와 비슷한 한 step 비용이지만 수렴이 훨씬 빨라 총 비용이 작다. 추가 비용으로 pretrained 가중치 저장 공간이 필요하다.

## 응용 (Applications)

- 의료·위성 등 라벨이 비싼 도메인에서 ImageNet pretrained 모델 활용
- NLP의 사전학습 언어 모델(BERT, GPT) 다운스트림 적용
- 음성·추천·단백질 등 대규모 사전학습 후 특화
- few-shot 환경에서 학습 안정화

## 흔한 오해 (Common Misunderstandings)

- pretrained 모델이 항상 도움이 되는 것은 아니다. domain gap이 크면 손해(negative transfer)일 수 있다.
- freeze한 backbone에도 batch norm 통계 갱신 같은 미묘한 상태가 있어 모드 설정에 주의해야 한다.
- "전이 학습 = fine-tuning"이 아니다. fine-tuning은 전이의 한 방식일 뿐이다.
- 큰 모델을 작은 데이터에 전체 fine-tuning하면 과적합·표현 붕괴가 날 수 있다.

## TMI

- 2014년 무렵 ImageNet pretrained CNN을 다른 비전 과제에 그대로 쓰는 것이 강력하다는 것이 알려지며 전이 학습이 표준이 됐다.
- NLP에서는 ULMFiT, ELMo, BERT가 "사전학습 후 fine-tuning" 패러다임을 대중화했다.
- batch norm 층을 freeze할 때 통계를 갱신할지 여부가 미세하지만 성능에 영향을 준다.

## 연습 / 확인 문제 (Exercises)

- 데이터가 100장뿐인 분류 과제에서 feature extraction과 전체 fine-tuning 중 무엇을 먼저 시도할지 근거와 함께 정하라.
- negative transfer가 발생하는 상황을 한 가지 예로 설명하라.
- 저수준 층을 freeze하고 고수준 층만 푸는 것이 합리적인 이유를 표현 계층 관점에서 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [CNN](CNN.md)
- 다음: [파인튜닝](Fine-Tuning.md), [AI/LLMs/Pretraining.md](../LLMs/Pretraining.md)

## 참조 (References)

- [AI/Deep-Learning/Fine-Tuning.md](Fine-Tuning.md)
- [AI/LLMs/Pretraining.md](../LLMs/Pretraining.md)
- [Reference/Papers.md](../../Reference/Papers.md)
- [Reference/Books.md](../../Reference/Books.md)
