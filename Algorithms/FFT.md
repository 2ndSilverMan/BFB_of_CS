# FFT / NTT (Fast Fourier Transform)

- Level: Advanced
- Prerequisites: [Algorithms/Divide-and-Conquer.md](Divide-and-Conquer.md), [Algorithms/Fast-Exponentiation.md](Fast-Exponentiation.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

FFT는 다항식·수열을 점값 표현으로 빠르게 변환하는 분할 정복 알고리즘으로, 다항식 곱셈(합성곱)을 `O(n log n)`에 수행한다. NTT는 같은 아이디어를 모듈러 정수 위에서 수행해 부동소수점 오차를 없앤다.

## 직관 (Intuition)

두 다항식을 계수끼리 곱하면 `O(n^2)`다. 하지만 다항식을 여러 점에서의 값으로 표현하면, 곱은 점마다의 단순 곱(`O(n)`)이 된다. FFT는 계수↔점값 변환을 `O(n log n)`에 해 주는 마법이다. 핵심은 1의 거듭제곱근(roots of unity)의 대칭성을 이용한 분할 정복이다.

## 이론 (Theory)

이산 푸리에 변환(DFT)은 다항식을 $n$개의 1의 거듭제곱근 $\omega^k$에서 평가한다. FFT는 다항식을 짝수·홀수 차수로 분할해

$$A(x)=A_{\text{even}}(x^2)+x\,A_{\text{odd}}(x^2)$$

$\omega$의 대칭성($\omega^{k+n/2}=-\omega^k$)으로 절반의 계산을 재사용해 `O(n log n)`을 얻는다. 합성곱 정리: 시간 영역의 합성곱 = 주파수 영역의 점별 곱. 역변환(IFFT)으로 계수를 복원한다.

**NTT**는 복소수 대신 소수 모듈러의 원시근을 1의 거듭제곱근으로 써, 정수 합성곱을 오차 없이 계산한다.

## 구현 (Implementation)

```python
import cmath
def fft(a, invert=False):
    n = len(a)
    if n == 1: return a
    even = fft(a[0::2], invert)
    odd  = fft(a[1::2], invert)
    ang = (2 if invert else -2) * cmath.pi / n
    res = [0]*n
    for k in range(n//2):
        w = cmath.exp(1j * ang * k)
        res[k]        = even[k] + w*odd[k]
        res[k + n//2] = even[k] - w*odd[k]   # 대칭성 활용
    return res
```

## 복잡도 (Complexity)

| 연산 | 시간 |
|---|---|
| FFT/IFFT | `O(n log n)` |
| 다항식 곱셈 | `O(n log n)` |

소박한 곱셈 `O(n^2)`을 크게 앞선다. NTT는 같은 복잡도에 정수 정확성을 보장하지만 모듈러 제약이 있다.

## 응용 (Applications)

- 큰 정수·다항식 곱셈
- 신호·오디오·이미지 처리(주파수 분석, 필터)
- 합성곱(상관, 패턴 매칭, 확률 분포 합)
- 압축(JPEG의 DCT는 사촌)

## 흔한 오해 (Common Misunderstandings)

- FFT는 곱셈을 빠르게 하지만, 입력을 2의 거듭제곱 길이로 패딩해야 한다.
- 부동소수점 FFT는 반올림 오차가 있어 큰 정수엔 NTT가 안전하다.
- DFT와 FFT는 다른 변환이 아니다 — FFT는 DFT의 빠른 계산법이다.
- NTT는 아무 소수나 쓸 수 없다(적절한 형태의 소수와 원시근 필요).

## TMI

- Cooley-Tukey FFT(1965)는 20세기 가장 영향력 있는 알고리즘으로 꼽히며, 사실 가우스가 먼저 발견했다는 설도 있다.
- 거대 정수 곱셈(원주율 수조 자리 계산)은 FFT/NTT 기반이다.
- JPEG·MP3 같은 압축은 푸리에 계열 변환으로 사람이 덜 민감한 성분을 버린다.

## 연습 / 확인 문제 (Exercises)

- 길이 4 수열의 DFT를 1의 4제곱근으로 손으로 계산하라.
- 두 작은 다항식을 FFT로 곱하는 과정을 단계별로 보여라.
- NTT가 부동소수점 오차를 어떻게 피하는지 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [고속 거듭제곱 / 행렬 거듭제곱](Fast-Exponentiation.md)
- 다음: [분할 상환 분석](Amortized-Analysis.md)

## 참조 (References)

- [Algorithms/Divide-and-Conquer.md](Divide-and-Conquer.md)
- [Math/Linear-Algebra/Vectors.md](../Math/Linear-Algebra/Vectors.md)
- [Reference/Books.md](../Reference/Books.md)
