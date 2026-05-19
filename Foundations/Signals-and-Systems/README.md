# 신호 및 시스템 (Signals & Systems)

> 선수 지식 → 난이도 순 정렬.
> 디지털 신호 처리, 통신, 제어 이론, 오디오/영상 AI의 기반.

## 1. 신호 (선수 지식: 미적분, 복소해석)

| # | 주제 | 파일 |
|---|------|------|
| 1 | 신호의 정의 & 분류 (Signals: CT vs DT, Periodic, Energy/Power) | [Signal-Classification.md](Signal-Classification.md) |
| 2 | 기본 신호 (Unit Step, Impulse, Exponential, Sinusoid) | [Basic-Signals.md](Basic-Signals.md) |
| 3 | 신호 연산 (Time Shift, Scaling, Reversal) | [Signal-Operations.md](Signal-Operations.md) |

## 2. 시스템 (선수 지식: 신호 기초)

| # | 주제 | 파일 |
|---|------|------|
| 4 | 시스템의 성질 (Linearity, Time-Invariance, Causality, Stability) | [System-Properties.md](System-Properties.md) |
| 5 | LTI 시스템 (Linear Time-Invariant Systems) | [LTI-Systems.md](LTI-Systems.md) |
| 6 | 임펄스 응답 (Impulse Response) | [Impulse-Response.md](Impulse-Response.md) |

## 3. 합성곱 (선수 지식: LTI 시스템)

| # | 주제 | 파일 |
|---|------|------|
| 7 | 연속시간 합성곱 (CT Convolution) | [CT-Convolution.md](CT-Convolution.md) |
| 8 | 이산시간 합성곱 (DT Convolution) | [DT-Convolution.md](DT-Convolution.md) |
| 9 | 합성곱의 성질 (Properties of Convolution) | [Convolution-Properties.md](Convolution-Properties.md) |

## 4. 푸리에 해석 (선수 지식: 합성곱)

| # | 주제 | 파일 |
|---|------|------|
| 10 | 연속시간 푸리에 급수 (CT Fourier Series) | [CT-Fourier-Series.md](CT-Fourier-Series.md) |
| 11 | 연속시간 푸리에 변환 (CTFT) | [CTFT.md](CTFT.md) |
| 12 | CTFT 성질 (Linearity, Shift, Convolution, Parseval) | [CTFT-Properties.md](CTFT-Properties.md) |
| 13 | 이산시간 푸리에 변환 (DTFT) | [DTFT.md](DTFT.md) |
| 14 | 이산 푸리에 변환 (DFT) | [DFT.md](DFT.md) |
| 15 | 고속 푸리에 변환 (FFT) | [FFT.md](FFT.md) |

## 5. 라플라스 변환 (선수 지식: CTFT)

| # | 주제 | 파일 |
|---|------|------|
| 16 | 라플라스 변환 정의 & 수렴 영역 (ROC) | [Laplace-Transform.md](Laplace-Transform.md) |
| 17 | 라플라스 변환 성질 | [Laplace-Properties.md](Laplace-Properties.md) |
| 18 | 역 라플라스 변환 (부분 분수 분해) | [Inverse-Laplace.md](Inverse-Laplace.md) |
| 19 | 전달 함수 (Transfer Function) | [Transfer-Function.md](Transfer-Function.md) |
| 20 | 극점 & 영점 (Poles & Zeros) | [Poles-Zeros.md](Poles-Zeros.md) |
| 21 | 블록 다이어그램 & 신호 흐름 그래프 | [Block-Diagram.md](Block-Diagram.md) |

## 6. z-변환 (선수 지식: 라플라스 변환, DTFT)

| # | 주제 | 파일 |
|---|------|------|
| 22 | z-변환 정의 & ROC | [Z-Transform.md](Z-Transform.md) |
| 23 | z-변환 성질 | [Z-Properties.md](Z-Properties.md) |
| 24 | 역 z-변환 (Inverse Z-Transform) | [Inverse-Z.md](Inverse-Z.md) |
| 25 | z-도메인 LTI 시스템 분석 | [Z-LTI-Analysis.md](Z-LTI-Analysis.md) |

## 7. 주파수 응답 & 필터 (선수 지식: 푸리에 해석, 전달 함수)

| # | 주제 | 파일 |
|---|------|------|
| 26 | 주파수 응답 (Frequency Response) | [Frequency-Response.md](Frequency-Response.md) |
| 27 | 보드 선도 (Bode Plot) | [Bode-Plot.md](Bode-Plot.md) |
| 28 | 이상적 필터 (Low-pass, High-pass, Band-pass, Notch) | [Ideal-Filters.md](Ideal-Filters.md) |
| 29 | 필터 구현 기초 (Filter Realization) | [Filter-Realization.md](Filter-Realization.md) |

## 8. 샘플링 이론 (선수 지식: 푸리에 변환)

| # | 주제 | 파일 |
|---|------|------|
| 30 | 샘플링 정리 (Nyquist-Shannon Sampling Theorem) | [Sampling-Theorem.md](Sampling-Theorem.md) |
| 31 | 에일리어싱 (Aliasing) | [Aliasing.md](Aliasing.md) |
| 32 | 양자화 (Quantization) | [Quantization.md](Quantization.md) |
| 33 | 복원 & 보간 (Reconstruction & Interpolation) | [Reconstruction.md](Reconstruction.md) |
