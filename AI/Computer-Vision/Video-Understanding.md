# 영상 이해 (Video Understanding)

- Level: Advanced
- Prerequisites: [AI/Computer-Vision/Image-Classification.md](Image-Classification.md), [AI/Computer-Vision/Optical-Flow.md](Optical-Flow.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

영상 이해는 프레임들의 시간적 변화를 이용해 action, event, object interaction, scene transition을 인식하는 과제다. 이미지 인식에 시간 축과 motion 정보를 더한다.

## 직관 (Intuition)

한 장의 사진으로는 "공을 던지는 중"인지 "잡은 채 서 있는 중"인지 모호할 수 있다. 영상은 변화의 방향과 순서를 보여 주므로 행동과 사건을 이해할 수 있다.

## 이론 (Theory)

Video model은 2D CNN으로 프레임 feature를 뽑아 temporal pooling을 하거나, 3D CNN으로 공간·시간 convolution을 수행하거나, Transformer로 frame/patch token 사이의 장기 의존성을 학습한다. Two-stream 방식은 RGB appearance와 optical flow motion을 분리해 사용한다.

Sampling strategy가 매우 중요하다. 짧은 clip은 세부 motion을 잘 보고, 긴 clip은 context를 더 잘 본다. Label은 video-level, clip-level, frame-level로 달라질 수 있다.

## 구현 (Implementation)

```python
clip = sample_frames(video, num_frames=16, stride=4)
features = [image_encoder(frame) for frame in clip]
prediction = temporal_head(features)
```

실제 학습에서는 fps, stride, clip length, augmentation, multi-view evaluation을 명확히 기록한다.

## 복잡도 (Complexity)

비용은 frame 수와 해상도, temporal attention 범위에 따라 커진다. 긴 영상은 memory가 커서 sparse sampling, hierarchical model, feature caching을 사용한다.

## 응용 (Applications)

- action recognition
- surveillance event detection
- sports highlight detection
- video retrieval·summarization

## 흔한 오해 (Common Misunderstandings)

- 프레임별 이미지 분류 평균만으로 모든 영상 문제가 해결되지 않는다.
- Random frame sampling은 짧은 사건을 놓칠 수 있다.
- 높은 clip accuracy가 긴 영상의 event localization을 보장하지 않는다.
- Optical flow는 motion 정보를 주지만 계산 비용과 오류도 함께 온다.

## TMI

- SlowFast류 모델은 느린 semantic stream과 빠른 motion stream을 나눠 본다.
- Video transformer는 token 수가 폭발하기 쉬워 factorized attention이나 sparse attention을 쓴다.
- Audio와 subtitle은 video understanding에서 강력한 추가 modality다.

## 연습 / 확인 문제 (Exercises)

- 2D CNN+temporal pooling과 3D CNN의 차이를 설명하라.
- 3초 행동과 10분 사건 탐지의 sampling strategy를 비교하라.
- Video-level label만 있을 때 frame-level localization이 어려운 이유를 말하라.

## 이어서 읽기 (Reading Path)

- 이전: [이미지 분류](Image-Classification.md), [광류](Optical-Flow.md)
- 다음: [Vision-Language Model](Vision-Language.md)

## 참조 (References)

- [AI/Deep-Learning/Transformer.md](../Deep-Learning/Transformer.md)
- [Reference/Papers.md](../../Reference/Papers.md)
