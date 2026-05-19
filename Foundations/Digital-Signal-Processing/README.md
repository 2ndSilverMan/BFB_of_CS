# 디지털 신호 처리 (Digital Signal Processing)

> **레벨:** 학부~대학원
> **선수 지식:** [신호와 시스템 (Signals and Systems)](../Signals-and-Systems/) — DFT, z-변환, 샘플링 이론
>
> 신호와 시스템에서 다룬 이론을 디지털 영역에서 실제로 설계하고 구현하는 방법을 다룬다.
> 오디오, 영상, 통신, 음성 AI의 전처리 기반.

---

## 1. 이산시간 신호 & 시스템 복습 (선수 지식: 신호와 시스템)

| # | 주제 | 파일 |
|---|------|------|
| 1 | 이산시간 신호 & LTI 시스템 복습 | [DT-Review.md](DT-Review.md) |
| 2 | 차분 방정식 (Difference Equations) | [Difference-Equations.md](Difference-Equations.md) |
| 3 | z-변환과 시스템 함수 | [Z-Transform-Systems.md](Z-Transform-Systems.md) |

## 2. DFT & FFT (선수 지식: 이산 푸리에 변환)

| # | 주제 | 파일 |
|---|------|------|
| 4 | DFT 성질 & 스펙트럼 해석 | [DFT-Properties.md](DFT-Properties.md) |
| 5 | FFT 알고리즘 (Cooley-Tukey, Radix-2) | [FFT-Algorithms.md](FFT-Algorithms.md) |
| 6 | IFFT & 원형 합성곱 (Circular Convolution) | [IFFT-Circular.md](IFFT-Circular.md) |
| 7 | 주파수 해상도 & 영 삽입 (Zero-Padding) | [Frequency-Resolution.md](Frequency-Resolution.md) |
| 8 | 단시간 푸리에 변환 (STFT) | [STFT.md](STFT.md) |

## 3. 디지털 필터 설계 (선수 지식: DFT, z-변환)

| # | 주제 | 파일 |
|---|------|------|
| 9 | FIR 필터 (Finite Impulse Response) | [FIR-Filter.md](FIR-Filter.md) |
| 10 | IIR 필터 (Infinite Impulse Response) | [IIR-Filter.md](IIR-Filter.md) |
| 11 | 윈도우 함수 (Window Functions) | [Window-Functions.md](Window-Functions.md) |
| 12 | 필터 설계 방법 (Butterworth, Chebyshev, Elliptic) | [Filter-Design.md](Filter-Design.md) |
| 13 | 쌍선형 변환 (Bilinear Transform) | [Bilinear-Transform.md](Bilinear-Transform.md) |
| 14 | 위상 특성 & 선형 위상 FIR | [Phase-Response.md](Phase-Response.md) |

## 4. 스펙트럼 분석 (선수 지식: DFT)

| # | 주제 | 파일 |
|---|------|------|
| 15 | 전력 스펙트럼 밀도 (Power Spectral Density) | [PSD.md](PSD.md) |
| 16 | 스펙트로그램 (Spectrogram) | [Spectrogram.md](Spectrogram.md) |
| 17 | 멜 스펙트로그램 & MFCC | [Mel-MFCC.md](Mel-MFCC.md) |
| 18 | 파라메트릭 스펙트럼 추정 (AR, ARMA) | [Parametric-Spectral.md](Parametric-Spectral.md) |

## 5. 다중 레이트 신호 처리 (선수 지식: 필터 설계)

| # | 주제 | 파일 |
|---|------|------|
| 19 | 업샘플링 & 다운샘플링 (Upsampling & Downsampling) | [Resampling.md](Resampling.md) |
| 20 | 폴리페이즈 필터 (Polyphase Filters) | [Polyphase.md](Polyphase.md) |
| 21 | 필터 뱅크 (Filter Banks) | [Filter-Banks.md](Filter-Banks.md) |

## 6. 웨이블릿 변환 (선수 지식: 필터 뱅크)

| # | 주제 | 파일 |
|---|------|------|
| 22 | 연속 웨이블릿 변환 (CWT) | [CWT.md](CWT.md) |
| 23 | 이산 웨이블릿 변환 (DWT) | [DWT.md](DWT.md) |
| 24 | 다중 해상도 분석 (Multiresolution Analysis) | [MRA.md](MRA.md) |

## 7. 적응 필터링 (선수 지식: 확률론, 필터 설계)

| # | 주제 | 파일 |
|---|------|------|
| 25 | LMS 알고리즘 (Least Mean Squares) | [LMS.md](LMS.md) |
| 26 | RLS 알고리즘 (Recursive Least Squares) | [RLS.md](RLS.md) |
| 27 | 적응 잡음 제거 (Adaptive Noise Cancellation) | [ANC.md](ANC.md) |

## 8. 응용 (선수 지식: 전 섹션)

| # | 주제 | 파일 |
|---|------|------|
| 28 | 오디오 신호 처리 (Audio Processing) | [Audio-Processing.md](Audio-Processing.md) |
| 29 | 음성 인식 전처리 (Speech Preprocessing) | [Speech-Preprocessing.md](Speech-Preprocessing.md) |
| 30 | 이미지 주파수 분석 (Image Frequency Analysis) | [Image-Frequency.md](Image-Frequency.md) |
| 31 | 통신 시스템 기초 (Communications Basics) | [Communications.md](Communications.md) |
| 32 | 압축 센싱 (Compressed Sensing) | [Compressed-Sensing.md](Compressed-Sensing.md) |
