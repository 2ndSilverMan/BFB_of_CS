# 광류 (Optical Flow)

- Level: Advanced
- Prerequisites: [AI/Computer-Vision/Image-Basics.md](Image-Basics.md), [Math/Linear-Algebra/Vectors.md](../../Math/Linear-Algebra/Vectors.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

광류는 연속된 프레임 사이에서 각 픽셀이 어디로 움직였는지 나타내는 2D motion field다. 영상의 apparent motion을 dense vector로 표현한다.

## 직관 (Intuition)

두 장의 사진을 겹쳐 보며 "이 픽셀 무늬가 다음 프레임에서 어디로 갔나"를 추적하는 일이다. 카메라가 움직여도, 물체가 움직여도 화면 위 픽셀은 이동한다.

## 이론 (Theory)

고전적 optical flow는 brightness constancy를 가정한다. 즉 짧은 시간 동안 같은 물체 점의 밝기는 크게 변하지 않는다고 본다. 작은 움직임에서는 이미지 gradient와 속도 사이에 optical flow constraint가 생긴다.

하지만 aperture problem 때문에 한 픽셀 주변 정보만으로는 motion이 모호하다. Smoothness prior, multi-scale pyramid, feature matching, deep network를 사용해 모호성을 줄인다.

## 구현 (Implementation)

```python
flow_vector = {
    "pixel": (x, y),
    "motion": (u, v),  # next frame position is approximately (x + u, y + v)
}
```

실제 flow map은 `H × W × 2` tensor로 저장하고, occlusion이나 invalid region mask를 함께 둘 수 있다.

## 복잡도 (Complexity)

Dense flow는 모든 픽셀에 motion을 예측하므로 해상도에 민감하다. Multi-scale 방법은 큰 움직임을 잡지만 여러 scale 계산이 필요하다. Deep flow model은 정확도를 올리지만 training data와 GPU 비용이 크다.

## 응용 (Applications)

- 영상 안정화
- action recognition 보조 feature
- object tracking
- frame interpolation·video editing

## 흔한 오해 (Common Misunderstandings)

- Optical flow는 실제 3D 움직임이 아니라 화면상의 apparent motion이다.
- 조명 변화와 반사 물체는 brightness constancy를 깨뜨린다.
- Occlusion이 생기면 이전 프레임의 픽셀이 다음 프레임에 대응되지 않을 수 있다.
- 카메라 움직임과 물체 움직임을 자동으로 분리해 주지는 않는다.

## TMI

- Forward flow와 backward flow의 일관성은 occlusion 탐지에 쓰인다.
- Flow visualization은 방향을 hue, 크기를 saturation/value로 표현하는 경우가 많다.
- Video model에서 optical flow는 motion stream의 입력으로 오래 사용되었다.

## 연습 / 확인 문제 (Exercises)

- Brightness constancy 가정이 깨지는 사례 3가지를 들어라.
- Aperture problem을 그림 없이 설명하라.
- Optical flow와 object tracking의 차이를 말하라.

## 이어서 읽기 (Reading Path)

- 이전: [이미지 표현 기초](Image-Basics.md)
- 다음: [영상 이해](Video-Understanding.md)

## 참조 (References)

- [Math/Linear-Algebra/Vectors.md](../../Math/Linear-Algebra/Vectors.md)
- [Reference/Books.md](../../Reference/Books.md)
