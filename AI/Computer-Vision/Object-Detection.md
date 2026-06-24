# 객체 탐지 (Object Detection)

- Level: Advanced
- Prerequisites: [AI/Computer-Vision/CNN-Deep-Dive.md](CNN-Deep-Dive.md), [AI/Computer-Vision/Image-Classification.md](Image-Classification.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

object detection은 이미지에서 객체의 위치(bounding box)와 종류(class)를 동시에 찾는 과제다. 분류와 달리 "무엇이 어디에 몇 개 있는가"를 답해야 하므로, 위치 회귀와 다중 객체 처리가 핵심이다.

## 직관 (Intuition)

분류는 이미지 전체에 라벨 하나를 단다. 탐지는 한 이미지에 객체가 몇 개일지 모르고, 각각 위치까지 찾아야 한다. 그래서 "후보 영역을 만들고 각각 분류·정밀화"하거나(2-stage), "격자마다 박스를 직접 예측"한다(1-stage). 겹치는 예측을 정리하는 후처리(NMS)가 마무리를 맡는다.

## 이론 (Theory)

**계열.**
- **2-stage(R-CNN, Faster R-CNN)**: region proposal → 각 영역 분류·박스 회귀. 정확하지만 느리다.
- **1-stage(YOLO, SSD, RetinaNet)**: 격자/anchor마다 박스·클래스를 한 번에 예측. 빠르다.
- **DETR**: Transformer로 집합 예측(set prediction)을 직접 수행, anchor·NMS 제거.

**핵심 요소.** anchor box는 다양한 크기·비율의 기준 박스다. 예측 박스와 정답의 겹침은 IoU로 측정한다.

$$\text{IoU}=\frac{|A\cap B|}{|A\cup B|}$$

손실은 보통 분류 손실 + 박스 회귀 손실(예: smooth L1, GIoU)의 합이다. 1-stage의 클래스 불균형(배경 과다)은 focal loss로 완화한다. **NMS(non-maximum suppression)**는 같은 객체에 대한 중복 박스를 IoU 임계로 제거한다. 평가는 여러 IoU·클래스에 대한 **mAP**로 한다.

## 구현 (Implementation)

```python
def nms(boxes, scores, iou_thresh):
    keep = []
    order = argsort(scores, descending=True)
    while order:
        i = order.pop(0)
        keep.append(i)                        # 가장 점수 높은 박스 채택
        order = [j for j in order
                 if iou(boxes[i], boxes[j]) < iou_thresh]  # 겹치면 제거
    return keep
```

## 복잡도 (Complexity)

비용은 backbone 추론 + head 예측 + NMS로 나뉜다. 2-stage는 proposal 수에 비례해 느리고, 1-stage는 한 번의 forward로 끝나 실시간에 유리하다. NMS는 박스 수 $n$에 대해 보통 `O(n^2)`이며 박스가 많으면 병목이 될 수 있다. DETR류는 NMS를 없애지만 학습 수렴이 느린 편이다.

## 응용 (Applications)

- 자율주행의 보행자·차량 탐지
- CCTV·드론 감시, 재고·결함 검사
- 의료 영상의 병변 위치 검출
- AR, 로봇 비전, 스포츠 분석

## 흔한 오해 (Common Misunderstandings)

- 1-stage가 항상 2-stage보다 부정확하지 않다. focal loss 이후 격차가 크게 줄었다.
- mAP가 높다고 모든 클래스·크기에서 고르게 좋은 것은 아니다(작은 객체는 흔히 어렵다).
- NMS 임계값은 정밀도/재현율 균형을 바꾸는 중요한 하이퍼파라미터다.
- anchor가 필수는 아니다. anchor-free·set prediction 방식도 있다.

## TMI

- YOLO("You Only Look Once")는 탐지를 단일 회귀 문제로 본 발상으로 실시간 탐지를 대중화했다.
- DETR은 NMS·anchor 같은 손수 설계한 후처리를 학습으로 흡수하려는 흐름의 대표 사례다.
- mAP의 정의(IoU 임계, 보간 방식)는 데이터셋(COCO vs VOC)마다 달라 수치 비교에 주의해야 한다.

## 연습 / 확인 문제 (Exercises)

- 두 박스 좌표가 주어졌을 때 IoU를 직접 계산하라.
- 1-stage와 2-stage 탐지기의 속도·정확도 트레이드오프를 구조와 연결해 설명하라.
- NMS 임계값을 높이거나 낮출 때 중복/누락이 어떻게 변하는지 논하라.

## 이어서 읽기 (Reading Path)

- 이전: [CNN 심화](CNN-Deep-Dive.md)
- 다음: [시맨틱 세그멘테이션](Semantic-Segmentation.md), [Vision-Language Model](Vision-Language.md)

## 참조 (References)

- [AI/Computer-Vision/CNN-Deep-Dive.md](CNN-Deep-Dive.md)
- [AI/Computer-Vision/Image-Classification.md](Image-Classification.md)
- [Reference/Papers.md](../../Reference/Papers.md)
