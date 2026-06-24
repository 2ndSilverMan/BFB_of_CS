# 고속 거듭제곱 / 행렬 거듭제곱 (Fast Exponentiation)

- Level: Intermediate
- Prerequisites: [Algorithms/Divide-and-Conquer.md](Divide-and-Conquer.md), [Math/Discrete/Number-Theory-Basics.md](../Math/Discrete/Number-Theory-Basics.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

고속 거듭제곱(이진 지수법)은 $a^n$을 곱셈 `O(log n)`번으로 계산하는 기법이다. 지수를 이진수로 쪼개 제곱을 반복하며, 모듈러 산술·행렬 거듭제곱으로 자연스럽게 일반화된다.

## 직관 (Intuition)

$a^{16}$을 16번 곱하지 않고, 제곱을 반복하면 $a\to a^2\to a^4\to a^8\to a^{16}$로 4번이면 된다. 지수가 16이 아니어도 이진 표현(예: $13=1101_2$)을 보고 필요한 제곱들만 골라 곱하면 `O(log n)`이다. 같은 원리가 행렬에도 통해 점화식을 빠르게 계산한다.

## 이론 (Theory)

지수 $n=\sum b_i 2^i$일 때

$$a^n=\prod_{b_i=1} a^{2^i}$$

$a^{2^i}$는 제곱을 반복해 얻는다. 모듈러 버전은 매 곱마다 $\bmod m$을 취해 수 크기를 제한한다.

**행렬 거듭제곱**: 선형 점화식 $f_n$을 행렬 $M$의 거듭제곱으로 표현하면 $M^n$을 `O(k^3 log n)`($k$는 행렬 크기)에 계산해 $f_n$을 구한다. 예: 피보나치는 $\begin{pmatrix}1&1\\1&0\end{pmatrix}^n$.

## 구현 (Implementation)

```python
def power(a, n, mod=None):
    result = 1
    while n > 0:
        if n & 1:                          # 현재 비트가 1이면 곱
            result = result * a
            if mod: result %= mod
        a = a * a                          # 제곱
        if mod: a %= mod
        n >>= 1
    return result

# 행렬 거듭제곱으로 피보나치
def fib(n):
    def mul(A, B):
        return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)] for i in range(2)]
    R, M = [[1,0],[0,1]], [[1,1],[1,0]]
    while n:
        if n & 1: R = mul(R, M)
        M = mul(M, M); n >>= 1
    return R[0][1]
```

## 복잡도 (Complexity)

| 연산 | 시간 |
|---|---|
| 스칼라 거듭제곱 | `O(log n)` 곱셈 |
| 행렬 거듭제곱 | `O(k^3 log n)` |

지수가 아무리 커도 로그 시간이다. 모듈러를 함께 쓰면 큰 수 연산도 일정 크기로 유지된다.

## 응용 (Applications)

- 모듈러 지수(RSA, 페르마 소정리, 역원)
- 선형 점화식의 $n$번째 항 빠른 계산
- 그래프의 경로 수($A^n$)
- 확률 전이(마르코프 체인 $P^n$)

## 흔한 오해 (Common Misunderstandings)

- 큰 지수에서 `a**n`을 그대로 계산하면 수가 폭발한다 — 모듈러 거듭제곱이 필요하다.
- 곱셈 횟수는 `O(log n)`이지만, 큰 정수 곱 비용은 자릿수에 따라 별도다.
- 행렬 거듭제곱은 점화식이 선형일 때만 적용된다.
- 지수가 음수면 모듈러 역원과 결합해야 한다.

## TMI

- 이진 지수법은 고대 인도의 수학(찬다흐샤스트라)까지 거슬러 올라가는 유서 깊은 기법이다.
- 행렬 거듭제곱으로 피보나치를 `O(log n)`에 구하는 것은 면접 단골 문제다.
- RSA 복호화의 핵심 연산이 바로 모듈러 거듭제곱이라, 하드웨어 가속의 대상이 된다.

## 연습 / 확인 문제 (Exercises)

- $3^{13} \bmod 7$을 이진 지수법으로 손으로 계산하라.
- 피보나치 행렬 거듭제곱 공식을 유도하라.
- 큰 지수에서 모듈러 없이 계산할 때의 문제를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [정수론 & 소수](Number-Theory.md)
- 다음: [FFT / NTT](FFT.md)

## 참조 (References)

- [Algorithms/Divide-and-Conquer.md](Divide-and-Conquer.md)
- [Math/Linear-Algebra/Matrices.md](../Math/Linear-Algebra/Matrices.md)
- [Reference/Books.md](../Reference/Books.md)
