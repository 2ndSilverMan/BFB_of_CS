# 시맨틱 세그멘테이션 (Semantic Segmentation)

- Level: Advanced
- Prerequisites: [AI/Computer-Vision/CNN-Deep-Dive.md](CNN-Deep-Dive.md), [AI/Computer-Vision/Image-Classification.md](Image-Classification.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

시맨틱 세그멘테이션은 이미지의 각 픽셀에 의미 class를 할당하는 과제다. "이 픽셀은 도로", "이 픽셀은 사람"처럼 위치와 범주를 dense하게 예측하지만, 같은 class의 개별 객체는 구분하지 않는다.

## 직관 (Intuition)

분류가 이미지 전체에 라벨 하나를 붙이고, 탐지가 박스를 그린다면, 세그멘테이션은 색칠 공부처럼 모든 픽셀을 class별로 칠한다. 경계가 정확해야 하고 작은 물체도 놓치면 안 된다.

## 이론 (Theory)

Fully convolutional network는 dense feature map에서 픽셀별 logit을 만든다. Encoder는 context를 추출하고 decoder는 해상도를 복원한다. U-Net의 skip connection은 저수준 위치 정보와 고수준 의미 정보를 결합한다.

Loss는 pixel-wise cross entropy, Dice loss, focal loss 등을 사용한다. 평가는 class별 IoU와 평균 mIoU가 대표적이다. Class imbalance와 boundary ambiguity가 핵심 난점이다.

## 구현 (Implementation)

```python
def pixel_accuracy(pred_mask, true_mask):
    total = len(true_mask)
    correct = sum(p == y for p, y in zip(pred_mask, true_mask))
    return correct / total
```

실제 구현은 2D mask를 flatten해 계산하거나 class별 confusion matrix에서 IoU를 구한다.

## 복잡도 (Complexity)

출력 해상도가 높아 메모리와 연산량이 커진다. Decoder, multi-scale feature, high-resolution crop은 정확도를 올리지만 training batch size를 줄일 수 있다.

## 응용 (Applications)

- 자율주행 도로·차선·보행자 영역 인식
- 의료 영상 장기·병변 분할
- 위성 영상 토지 피복 분류
- 이미지 편집용 mask 생성

## 흔한 오해 (Common Misunderstandings)

- 높은 pixel accuracy는 배경이 많은 데이터에서 착시를 만들 수 있다.
- Semantic segmentation은 같은 class의 두 객체를 분리하지 않는다.
- Upsampling만 잘하면 경계가 정확해지는 것은 아니다.
- Annotation boundary 자체가 모호하면 모델 평가도 흔들린다.

## TMI

- Dilated convolution은 해상도를 덜 줄이면서 receptive field를 키운다.
- CRF 같은 후처리는 경계를 다듬는 데 쓰였지만 end-to-end 모델로 대체되는 경우가 많다.
- Sliding window inference는 큰 이미지를 GPU 메모리에 맞춰 처리할 때 유용하다.

## 연습 / 확인 문제 (Exercises)

- Pixel accuracy와 mIoU가 다르게 해석되는 예시를 만들어라.
- U-Net skip connection의 역할을 설명하라.
- Class imbalance가 심한 segmentation loss를 설계하라.

## 이어서 읽기 (Reading Path)

- 이전: [이미지 분류](Image-Classification.md), [객체 탐지](Object-Detection.md)
- 다음: [인스턴스 세그멘테이션](Instance-Segmentation.md)

## 참조 (References)

- [AI/Deep-Learning/CNN.md](../Deep-Learning/CNN.md)
- [Reference/Papers.md](../../Reference/Papers.md)
