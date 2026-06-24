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
| 오토인코더 (AE, DAE, Sparse AE) | [Autoencoders.md](Autoencoders.md) | Draft |
| 변분 오토인코더 (VAE) | [VAE.md](VAE.md) | Draft |
| β-VAE와 분리 표현 학습 | [Beta-VAE.md](Beta-VAE.md) | Draft |

### GAN 계열

| 주제 | 파일 | Status |
|---|---|---|
| GAN 기초와 학습 안정성 | [GAN-Basics.md](GAN-Basics.md) | Draft |
| DCGAN | [DCGAN.md](DCGAN.md) | Draft |
| Conditional GAN | [Conditional-GAN.md](Conditional-GAN.md) | Draft |
| StyleGAN | [StyleGAN.md](StyleGAN.md) | Draft |
| CycleGAN (비짝지은 변환) | [CycleGAN.md](CycleGAN.md) | Draft |

### Flow 기반 모델

| 주제 | 파일 | Status |
|---|---|---|
| Normalizing Flows | [Normalizing-Flows.md](Normalizing-Flows.md) | Draft |
| RealNVP, Glow | [Real-NVP.md](Real-NVP.md) | Draft |

### Diffusion 모델

| 주제 | 파일 | Status |
|---|---|---|
| DDPM (Denoising Diffusion Probabilistic Models) | [DDPM.md](DDPM.md) | Draft |
| DDIM (가속 샘플링) | [DDIM.md](DDIM.md) | Draft |
| Score-based 생성 모델 | [Score-Based.md](Score-Based.md) | Draft |
| Latent Diffusion / Stable Diffusion | [Latent-Diffusion.md](Latent-Diffusion.md) | Draft |

### 에너지 기반 모델

| 주제 | 파일 | Status |
|---|---|---|
| 에너지 기반 모델 (EBM) | [EBM.md](EBM.md) | Draft |

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
