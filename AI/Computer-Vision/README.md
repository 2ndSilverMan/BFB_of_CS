# 컴퓨터 비전 (Computer Vision)

> 이미지와 영상을 이해하는 방법.

**선수지식**: [AI/Deep-Learning/](../Deep-Learning/), [Math/Linear-Algebra/](../../Math/Linear-Algebra/)

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

### 기초

| 주제 | 파일 | Status |
|---|---|---|
| 이미지 표현 (픽셀, 컬러 스페이스) | Image-Basics.md | Planned |
| 고전 비전 (에지 검출, HOG, SIFT) | Classical-Vision.md | Planned |
| 합성곱 신경망 (CNN) 심화 | CNN-Deep-Dive.md | Planned |

### 주요 태스크

| 주제 | 파일 | Status |
|---|---|---|
| 이미지 분류 | Image-Classification.md | Planned |
| 객체 탐지 (YOLO, Faster R-CNN, DETR) | Object-Detection.md | Planned |
| 시맨틱 세그멘테이션 | Semantic-Segmentation.md | Planned |
| 인스턴스 세그멘테이션 | Instance-Segmentation.md | Planned |
| 이미지 생성 (GAN, Diffusion) | Image-Generation.md | Planned |

### 심화

| 주제 | 파일 | Status |
|---|---|---|
| 포즈 추정 | Pose-Estimation.md | Planned |
| 광류 (Optical Flow) | Optical-Flow.md | Planned |
| 영상 이해 (Video Understanding) | Video-Understanding.md | Planned |
| Vision-Language Model (CLIP, ViT) | Vision-Language.md | Planned |
| 3D 비전 (NeRF, 포인트 클라우드) | 3D-Vision.md | Planned |

---

## 학습 순서

```text
Image-Basics → Classical-Vision → CNN-Deep-Dive
        ↓
Image-Classification → Object-Detection
        ↓
Semantic-Segmentation / Instance-Segmentation
        ↓
Image-Generation / Pose-Estimation / Optical-Flow / Video-Understanding / Vision-Language / 3D-Vision
```

---

## 연관 섹션

- [AI/Deep-Learning/](../Deep-Learning/) — CNN, 어텐션 선수지식
- [AI/Generative-Models/](../Generative-Models/) — 이미지 생성
