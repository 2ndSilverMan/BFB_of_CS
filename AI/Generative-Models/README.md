# 생성 모델 (Generative Models)

> 데이터 분포를 학습하여 새로운 샘플을 생성하는 모델.

**선수지식**: [AI/Deep-Learning/](../Deep-Learning/), [Math/Probability-Statistics/](../../Math/Probability-Statistics/)

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

### 오토인코더 계열

| 주제 | 파일 | Status |
|---|---|---|
| 오토인코더 (AE, DAE, Sparse AE) | Autoencoders.md | Planned |
| 변분 오토인코더 (VAE) | VAE.md | Planned |
| β-VAE와 분리 표현 학습 | Beta-VAE.md | Planned |

### GAN 계열

| 주제 | 파일 | Status |
|---|---|---|
| GAN 기초와 학습 안정성 | GAN-Basics.md | Planned |
| DCGAN | DCGAN.md | Planned |
| Conditional GAN | Conditional-GAN.md | Planned |
| StyleGAN | StyleGAN.md | Planned |
| CycleGAN (비짝지은 변환) | CycleGAN.md | Planned |

### Flow 기반 모델

| 주제 | 파일 | Status |
|---|---|---|
| Normalizing Flows | Normalizing-Flows.md | Planned |
| RealNVP, Glow | Real-NVP.md | Planned |

### Diffusion 모델

| 주제 | 파일 | Status |
|---|---|---|
| DDPM (Denoising Diffusion Probabilistic Models) | DDPM.md | Planned |
| DDIM (가속 샘플링) | DDIM.md | Planned |
| Score-based 생성 모델 | Score-Based.md | Planned |
| Latent Diffusion / Stable Diffusion | Latent-Diffusion.md | Planned |

### 에너지 기반 모델

| 주제 | 파일 | Status |
|---|---|---|
| 에너지 기반 모델 (EBM) | EBM.md | Planned |

---

## 학습 순서

```text
Autoencoders → VAE → Beta-VAE
       ↓
GAN-Basics → DCGAN / Conditional-GAN / StyleGAN / CycleGAN
       ↓
Normalizing-Flows → Real-NVP
       ↓
DDPM → DDIM → Score-Based → Latent-Diffusion
       ↓
EBM
```

---

## 연관 섹션

- [AI/Deep-Learning/](../Deep-Learning/) — 선수지식
- [AI/Computer-Vision/](../Computer-Vision/) — 이미지 생성 응용
- [AI/LLMs/](../LLMs/) — 텍스트 생성 모델
