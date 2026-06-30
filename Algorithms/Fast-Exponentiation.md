# 고속 거듭제곱 / 행렬 거듭제곱 (Fast Exponentiation)

- Level: Intermediate
- Prerequisites: [Algorithms/Divide-and-Conquer.md](Divide-and-Conquer.md), [Math/Discrete/Number-Theory-Basics.md](../Math/Discrete/Number-Theory-Basics.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

고속 거듭제곱(이진 지수법)은 $a^n$ 을 곱셈 **$O(\log n)$** 번으로 계산한다. 지수를 이진수로 쪼개 제곱을 반복하며, 모듈러·행렬로 일반화돼 RSA·선형 점화식 가속의 핵심이 된다.

## 직관 (Intuition)

$a^{16}$ 을 16번 곱하지 않고 제곱 반복으로 $a\to a^2\to a^4\to a^8\to a^{16}$ 4번. 지수가 16이 아니어도 이진 표현($13=1101_2$)을 보고 필요한 제곱들만 골라 곱하면 $O(\log n)$. 같은 원리가 **행렬**에도 통해 선형 점화식을 로그 시간에 푼다.

## 이론 (Theory)

### 1. 이진 지수법

$n=\sum b_i 2^i$ 일 때 $a^n=\prod_{b_i=1} a^{2^i}$, $a^{2^i}$ 는 제곱 반복으로. 비트를 낮은 자리부터 보며 "현재 누적 제곱 $a^{2^i}$ 를, 비트가 1이면 결과에 곱한다". 모듈러 버전은 매 곱마다 $\bmod m$ 으로 수 크기를 제한.

### 2. 행렬 거듭제곱으로 점화식

선형 점화식 $f_n$ 을 전이 행렬 $M$ 로 표현하면 $M^n$ 을 $O(k^3\log n)$ ($k$=행렬 크기)에 계산해 $f_n$ 을 얻는다. 피보나치:

$$\begin{pmatrix}f_{n+1}\\f_n\end{pmatrix}=\begin{pmatrix}1&1\\1&0\end{pmatrix}\begin{pmatrix}f_n\\f_{n-1}\end{pmatrix}\;\Rightarrow\;\begin{pmatrix}1&1\\1&0\end{pmatrix}^{n}$$

### 3. 부수 효과 주의 (보안)

데이터 의존 분기(비트가 1일 때만 곱)는 **타이밍/전력 부채널**을 노출한다. 암호 구현은 **Montgomery ladder** 처럼 비트와 무관하게 같은 연산 수를 하는 상수 시간 변형을 쓴다.

## 구현 (Implementation)

```python
def power(a, n, mod=None):                  # a^n (mod)
    result = 1
    while n > 0:
        if n & 1:
            result = result * a % mod if mod else result * a
        a = a * a % mod if mod else a * a   # 제곱
        n >>= 1
    return result

def fib(n):                                 # 행렬 거듭제곱 O(log n)
    def mul(A, B):
        return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    R, M = [[1,0],[0,1]], [[1,1],[1,0]]     # R=단위행렬
    while n:
        if n & 1: R = mul(R, M)
        M = mul(M, M); n >>= 1
    return R[0][1]
```

## 복잡도 (Complexity)

| 연산 | 시간 |
|---|---|
| 스칼라 거듭제곱 | $O(\log n)$ 곱셈 |
| 모듈러 거듭제곱 | $O(\log n)$ 곱(각 곱은 자릿수 비용 별도) |
| 행렬 거듭제곱 | $O(k^3\log n)$ |

**워크드 예제($3^{13}\bmod7$).** $13=1101_2$. $3^1=3,\ 3^2=2,\ 3^4=2^2=4,\ 3^8=4^2=2\pmod7$. 비트 1,2,8 → $3\cdot4\cdot2=24\equiv3\pmod7$. (검산: $3^{13}=3^{6\cdot2+1}\equiv3$.)

## 응용 (Applications)

- 모듈러 지수(RSA 복호, 페르마 소정리 역원).
- 선형 점화식의 $n$ 번째 항(피보나치·트리보나치) $O(\log n)$.
- 그래프 경로 수($A^n$), 마르코프 체인 전이($P^n$).

## 흔한 오해 (Common Misunderstandings)

- **큰 지수에서 `a**n` 직접 계산은 수 폭발** — 모듈러 거듭제곱 필요.
- **곱셈 횟수는 $O(\log n)$ 이지만 큰 정수 곱 비용은 자릿수에 별도로 의존**.
- **행렬 거듭제곱은 점화식이 선형일 때만** 적용.
- **지수가 음수면 모듈러 역원과 결합**해야 한다.

## TMI

- 이진 지수법은 고대 인도 *찬다흐샤스트라*(핑갈라)까지 거슬러 올라가는 유서 깊은 기법이다.
- RSA 복호의 핵심이 모듈러 거듭제곱이라 하드웨어 가속·부채널 방어의 주 대상이다.
- 행렬 거듭제곱 피보나치는 면접 단골이지만, 큰 $n$ 의 정확한 값엔 빅정수 비용이 더 크다.

## 연습 / 확인 문제 (Exercises)

- $3^{13}\bmod7$ 을 이진 지수법으로 손으로 계산하라(위 예제 재현).
- 피보나치 전이 행렬을 유도하고 $f_{10}$ 을 행렬 거듭제곱으로 구하라.
- 큰 지수에서 모듈러 없이 계산할 때의 문제를 설명하라.
- 인접 행렬 $A$ 에서 $A^k$ 의 의미(길이 $k$ 경로 수)를 작은 그래프로 확인하라.

## 이어서 읽기 (Reading Path)

- 이전: [정수론 & 소수](Number-Theory.md)
- 다음: [FFT / NTT](FFT.md)
- 관련: [분할 정복](Divide-and-Conquer.md), [행렬](../Math/Linear-Algebra/Matrices.md)

## 참조 (References)

- [Algorithms/Divide-and-Conquer.md](Divide-and-Conquer.md)
- [Math/Linear-Algebra/Matrices.md](../Math/Linear-Algebra/Matrices.md)
- [Reference/Books.md](../Reference/Books.md)
