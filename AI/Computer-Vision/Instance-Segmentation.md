# 인스턴스 세그멘테이션 (Instance Segmentation)

- Level: Advanced
- Prerequisites: [AI/Computer-Vision/Object-Detection.md](Object-Detection.md), [AI/Computer-Vision/Semantic-Segmentation.md](Semantic-Segmentation.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

인스턴스 세그멘테이션은 각 객체의 class, 위치, 픽셀 mask를 동시에 예측한다. Semantic segmentation과 달리 같은 class의 개별 객체를 서로 다른 instance로 분리한다.

## 직관 (Intuition)

"사람 픽셀"을 모두 하나로 칠하는 데서 멈추지 않고, 첫 번째 사람과 두 번째 사람의 영역을 따로 잘라낸다. 그래서 탐지의 객체 단위 사고와 segmentation의 픽셀 정밀도가 함께 필요하다.

## 이론 (Theory)

Top-down 방식은 먼저 객체 후보나 box를 찾고 각 후보에 mask head를 적용한다. Mask R-CNN은 detection branch에 parallel mask branch를 추가한 대표 구조다. Bottom-up 방식은 픽셀 embedding이나 center/keypoint를 예측한 뒤 instance로 그룹화한다.

평가는 mask IoU 기반 AP를 사용한다. Crowded scene에서는 overlap, occlusion, small object가 어렵고, mask quality와 box quality가 함께 결과를 좌우한다.

## 구현 (Implementation)

```python
prediction = {
    "class": "person",
    "score": 0.93,
    "box": [12, 20, 160, 240],
    "mask": "binary_mask_for_this_instance",
}
```

후처리는 score threshold, mask resize, NMS 또는 mask-aware 중복 제거를 포함한다.

## 복잡도 (Complexity)

Detection backbone과 proposal 수, mask resolution이 비용을 결정한다. Instance가 많고 mask가 고해상도일수록 memory와 post-processing 비용이 증가한다.

## 응용 (Applications)

- 로봇 grasping 대상 분리
- 의료 영상의 병변 개별 개수 측정
- 이미지 편집·배경 제거
- 제조 결함 위치와 개수 분석

## 흔한 오해 (Common Misunderstandings)

- Instance segmentation은 semantic segmentation보다 항상 정답 annotation이 더 쉽지 않다.
- Box가 틀리면 mask가 좋아도 평가가 나빠질 수 있다.
- 같은 class 객체가 붙어 있으면 mask boundary가 특히 어렵다.
- Panoptic segmentation은 semantic과 instance를 결합한 별도 설정이다.

## TMI

- COCO-style mask AP는 여러 IoU threshold를 평균해 mask 품질을 더 엄격하게 본다.
- Polygon annotation과 bitmap mask annotation은 비용과 정밀도 트레이드오프가 있다.
- 객체 수를 세는 문제에서는 detection false positive/negative가 바로 count error가 된다.

## 연습 / 확인 문제 (Exercises)

- Semantic과 instance segmentation의 출력 차이를 예시로 설명하라.
- Mask AP가 box AP와 달라지는 상황을 만들라.
- 서로 겹친 객체의 annotation 정책을 설계하라.

## 이어서 읽기 (Reading Path)

- 이전: [객체 탐지](Object-Detection.md), [시맨틱 세그멘테이션](Semantic-Segmentation.md)
- 다음: [포즈 추정](Pose-Estimation.md), [Vision-Language Model](Vision-Language.md)

## 참조 (References)

- [AI/Computer-Vision/Object-Detection.md](Object-Detection.md)
- [Reference/Papers.md](../../Reference/Papers.md)
