# 3D 비전 (3D Vision)

- Level: Advanced
- Prerequisites: [Math/Linear-Algebra/Matrices.md](../../Math/Linear-Algebra/Matrices.md), [AI/Computer-Vision/Classical-Vision.md](Classical-Vision.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

3D 비전은 2D 이미지, depth, point cloud, multi-view 관측에서 장면의 3차원 구조와 카메라·객체의 기하를 추정하는 분야다. Reconstruction, pose, depth estimation, NeRF, point cloud understanding 등이 포함된다.

## 직관 (Intuition)

사진은 3D 세계가 평면에 투영된 그림자다. 3D 비전은 여러 시점, 움직임, 깊이 센서, 기하 제약을 이용해 그림자 뒤의 공간 구조를 되살린다.

## 이론 (Theory)

Pinhole camera model은 3D 점을 camera intrinsic·extrinsic matrix로 2D image plane에 투영한다. Stereo vision은 두 카메라의 disparity로 depth를 추정한다. Structure from Motion은 여러 이미지의 feature correspondence로 camera pose와 sparse 3D point를 함께 복원한다.

3D representation은 point cloud, voxel, mesh, signed distance field, neural radiance field처럼 다양하다. Point cloud는 sparse하고 순서가 없으며, voxel은 regular grid지만 resolution 비용이 크다. NeRF류는 위치와 시점 방향에서 색과 density를 예측해 novel view를 합성한다.

## 구현 (Implementation)

```python
point3d = [x, y, z, 1.0]
pixel_homogeneous = camera_matrix @ point3d
pixel = pixel_homogeneous[:2] / pixel_homogeneous[2]
```

실제 구현은 calibration, distortion, coordinate convention, scale ambiguity를 명확히 관리해야 한다.

## 복잡도 (Complexity)

Multi-view matching은 image 수와 feature 수가 늘수록 비용이 커진다. Voxel은 해상도를 두 배 올리면 3D grid cell이 대략 8배 증가한다. NeRF 학습·렌더링은 ray sample 수와 network 평가 횟수에 민감하다.

## 응용 (Applications)

- AR/VR 공간 인식
- 로봇 navigation·grasping
- 자율주행 perception
- 3D reconstruction·digital twin

## 흔한 오해 (Common Misunderstandings)

- 단일 2D 이미지에서 절대 scale을 항상 알 수 있는 것은 아니다.
- Depth map과 3D reconstruction은 관련 있지만 같은 결과물이 아니다.
- Point cloud는 순서가 없으므로 일반 이미지 convolution을 그대로 적용하기 어렵다.
- NeRF가 mesh를 직접 주는 것은 아니며 별도 추출 과정이 필요할 수 있다.

## TMI

- Epipolar geometry는 stereo matching의 검색 공간을 선으로 줄인다.
- SLAM은 localization과 mapping을 동시에 푸는 문제다.
- Differentiable rendering은 렌더링 오차를 통해 3D 표현을 학습하게 해 준다.

## 연습 / 확인 문제 (Exercises)

- Camera intrinsic과 extrinsic의 차이를 설명하라.
- Stereo disparity가 작아질 때 depth가 어떻게 변하는지 말하라.
- Point cloud, voxel, mesh, NeRF representation을 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [고전 비전](Classical-Vision.md), [광류](Optical-Flow.md)
- 다음: [Vision-Language Model](Vision-Language.md)

## 참조 (References)

- [Math/Linear-Algebra/Matrices.md](../../Math/Linear-Algebra/Matrices.md)
- [Reference/Books.md](../../Reference/Books.md)
