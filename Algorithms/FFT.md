# FFT / NTT (Fast Fourier Transform)

- Level: Advanced
- Prerequisites: [Algorithms/Divide-and-Conquer.md](Divide-and-Conquer.md), [Algorithms/Fast-Exponentiation.md](Fast-Exponentiation.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

FFT는 다항식·수열의 **계수 표현 ↔ 점값 표현** 변환을 $O(n\log n)$ 에 하는 분할 정복이다. 이로써 다항식 곱셈(합성곱)이 $O(n\log n)$. **NTT**는 같은 아이디어를 모듈러 정수 위에서 해 부동소수점 오차를 없앤다.

## 직관 (Intuition)

두 다항식을 계수끼리 곱하면 $O(n^2)$. 하지만 **점값 표현**(여러 점에서의 값)이면 곱이 점마다 단순 곱 $O(n)$. FFT는 계수↔점값 변환을 $O(n\log n)$ 에 해 주는 마법이고, 비밀은 **1의 거듭제곱근(roots of unity)의 대칭성**이다.

## 이론 (Theory)

### 1. DFT와 분할

DFT는 다항식을 $n$ 개의 1의 거듭제곱근 $\omega^k$ ($\omega=e^{-2\pi i/n}$)에서 평가한다. 짝수·홀수 차수로 분할:

$$A(x)=A_{\text{even}}(x^2)+x\,A_{\text{odd}}(x^2)$$

$\omega$ 의 대칭성 $\omega^{k+n/2}=-\omega^k$ 로 절반의 계산을 재사용 → $T(n)=2T(n/2)+O(n)=O(n\log n)$. 이 결합 단계가 **butterfly** 연산.

### 2. 합성곱 정리

시간 영역 합성곱 = 주파수 영역 점별 곱: $\text{conv}(a,b)=\text{IDFT}(\text{DFT}(a)\cdot\text{DFT}(b))$. 두 다항식을 각각 FFT → 점별 곱 → IFFT로 계수 복원.

### 3. NTT

복소수 대신 **소수 모듈러의 원시근**을 1의 거듭제곱근으로 쓴다. $p=c\cdot2^k+1$ 꼴 소수(예: $998244353$)와 원시근 $g$ 가 있어야 길이 $2^k$ 변환이 정확히 닫힌다 — 정수 합성곱을 오차 0으로.

## 구현 (Implementation)

```python
import cmath
def fft(a, invert=False):
    n = len(a)
    if n == 1: return a[:]
    even = fft(a[0::2], invert)
    odd  = fft(a[1::2], invert)
    ang = (2 if invert else -2) * cmath.pi / n
    res = [0]*n
    for k in range(n//2):
        w = cmath.exp(1j*ang*k) * odd[k]
        res[k]        = even[k] + w
        res[k + n//2] = even[k] - w        # 대칭성: -ω^k
    if invert:
        for k in range(n): res[k] /= 2     # IFFT 정규화(재귀 누적)
    return res

def multiply(a, b):
    n = 1
    while n < len(a)+len(b): n <<= 1        # 2의 거듭제곱으로 패딩
    fa = fft(a + [0]*(n-len(a))); fb = fft(b + [0]*(n-len(b)))
    fc = [x*y for x, y in zip(fa, fb)]      # 점별 곱
    return [round(x.real) for x in fft(fc, invert=True)]
```

## 복잡도 (Complexity)

| 연산 | 시간 |
|---|---|
| FFT/IFFT | $O(n\log n)$ |
| 다항식·정수 곱셈 | $O(n\log n)$ |

소박한 $O(n^2)$ 을 크게 앞선다. **워크드 예제.** $(1+2x)\cdot(3+4x)$: 길이 4로 패딩, 1의 4제곱근 $\{1,i,-1,-i\}$ 에서 평가·점별 곱·역변환 → $3+10x+8x^2$.

## 응용 (Applications)

- 큰 정수·다항식 곱셈(원주율 수조 자리, 빅정수 라이브러리).
- 신호·오디오·이미지 처리(주파수 분석·필터), 합성곱(상관·확률분포 합).
- 압축(JPEG의 DCT는 사촌), 문자열 매칭(와일드카드).

## 흔한 오해 (Common Misunderstandings)

- **입력을 2의 거듭제곱 길이로 패딩**해야 한다(기본 Cooley-Tukey).
- **부동소수점 FFT는 반올림 오차** — 큰 정수엔 NTT.
- **DFT와 FFT는 다른 변환이 아니다** — FFT는 DFT의 빠른 계산법.
- **NTT는 아무 소수나 못 쓴다** — $c\cdot2^k+1$ 꼴 소수와 원시근 필요.

## TMI

- Cooley-Tukey(1965)는 20세기 가장 영향력 있는 알고리즘으로 꼽히며, 가우스가 1805년 먼저 발견했다는 설이 있다.
- 반복(iterative) FFT는 비트 반전(bit-reversal) 순열로 재귀 없이 in-place 계산해 더 빠르다.
- MP3·JPEG는 푸리에 계열 변환으로 사람이 덜 민감한 주파수 성분을 버려 압축한다.

## 연습 / 확인 문제 (Exercises)

- 길이 4 수열의 DFT를 1의 4제곱근으로 손으로 계산하라.
- 두 작은 다항식을 FFT로 곱하는 과정을 단계별로 보여라.
- $\omega^{k+n/2}=-\omega^k$ 가 왜 절반의 계산을 아끼는지 설명하라.
- NTT가 부동소수점 오차를 어떻게 피하는지 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [고속 거듭제곱 / 행렬 거듭제곱](Fast-Exponentiation.md)
- 다음: [분할 상환 분석](Amortized-Analysis.md)
- 관련: [분할 정복](Divide-and-Conquer.md)

## 참조 (References)

- [Algorithms/Divide-and-Conquer.md](Divide-and-Conquer.md)
- [Math/Linear-Algebra/Vectors.md](../Math/Linear-Algebra/Vectors.md)
- [Reference/Books.md](../Reference/Books.md)
