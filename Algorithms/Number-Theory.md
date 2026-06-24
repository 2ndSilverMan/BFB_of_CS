# 정수론 & 소수 (Number Theory Algorithms)

- Level: Advanced
- Prerequisites: [Math/Discrete/Number-Theory-Basics.md](../Math/Discrete/Number-Theory-Basics.md), [Algorithms/Complexity.md](Complexity.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

정수론 알고리즘은 소수 판정·생성, 소인수분해, 최대공약수, 모듈러 역원, 합동식 풀이 등을 효율적으로 계산한다. 암호·해싱·경쟁 프로그래밍의 수학적 도구 모음이다.

## 직관 (Intuition)

"소수인가", "어떻게 인수분해되나", "모듈러 세계에서 나눗셈은?" 같은 질문은 단순해 보여도 큰 수에서는 영리한 알고리즘이 필요하다. 작은 수는 체로 한꺼번에, 큰 수는 확률적 판정으로 빠르게 다룬다.

## 이론 (Theory)

- **에라토스테네스의 체**: $n$까지 소수를 `O(n log log n)`에 모두 찾는다. 선형 체는 `O(n)`.
- **밀러-라빈 소수 판정**: 확률적(또는 결정적 증인 집합)으로 큰 수의 소수 여부를 `O(k log^3 n)`에 판정.
- **폴라드 로(Pollard's rho)**: 소인수분해를 기댓값 `O(n^{1/4})`에 시도.
- **확장 유클리드**: $ax+by=\gcd$, 모듈러 역원 계산.
- **중국인의 나머지 정리(CRT)**: 서로소 모듈러 합동식 연립을 유일해로 합친다.

오일러 피 함수 $\varphi(n)$와 오일러 정리 $a^{\varphi(n)}\equiv 1$은 모듈러 지수의 주기를 준다.

## 구현 (Implementation)

```python
def sieve(n):                              # 에라토스테네스의 체
    is_prime = [True]*(n+1); is_prime[0:2] = [False, False]
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            for j in range(i*i, n+1, i):
                is_prime[j] = False
    return [i for i in range(2, n+1) if is_prime[i]]

def is_prime(n):                           # 밀러-라빈 (결정적 증인)
    if n < 2: return False
    for p in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n % p == 0: return n == p
    d = n-1; r = 0
    while d % 2 == 0: d //= 2; r += 1
    for a in (2,3,5,7,11,13,17,19,23,29,31,37):
        x = pow(a, d, n)
        if x in (1, n-1): continue
        for _ in range(r-1):
            x = x*x % n
            if x == n-1: break
        else: return False
    return True
```

## 복잡도 (Complexity)

| 연산 | 시간 |
|---|---|
| 에라토스테네스 체 | `O(n log log n)` |
| 밀러-라빈 | `O(k log^3 n)` |
| 폴라드 로 | 기댓값 `O(n^{1/4})` |
| 확장 유클리드 | `O(log n)` |

큰 수 소인수분해는 일반적으로 어려운 문제로 남아 있어 RSA 안전성의 근거가 된다.

## 응용 (Applications)

- 공개키 암호(RSA, Diffie-Hellman)
- 해시·모듈러 산술(경쟁 프로그래밍)
- 난수·의사난수 생성
- 부호 이론·체크섬

## 흔한 오해 (Common Misunderstandings)

- 단순 시험 나눗셈 `O(√n)`은 큰 수엔 비현실적이다(밀러-라빈 필요).
- 밀러-라빈은 확률적이지만, 작은 범위는 고정 증인으로 결정적이다.
- 모듈러 나눗셈은 역원 곱이며, 역원은 $\gcd=1$일 때만 존재한다.
- 폴라드 로는 소수에는 무력하다(먼저 소수 판정).

## TMI

- 밀러-라빈의 결정적 버전은 $2^{64}$ 미만에서 12개 증인이면 충분하다고 알려져 있다.
- AKS 소수 판정(2002)은 최초의 다항 시간 결정적 소수 판정으로 이론적 이정표지만 실전은 밀러-라빈이 빠르다.
- 폴라드 로의 "거북이와 토끼" 사이클 탐지는 Floyd의 알고리즘을 인수분해에 응용한 것이다.

## 연습 / 확인 문제 (Exercises)

- 체로 50 이하 소수를 구하라.
- 확장 유클리드로 $\bmod 13$에서 7의 역원을 구하라.
- CRT로 $x\equiv2\ (\bmod\,3),\ x\equiv3\ (\bmod\,5)$를 풀어라.

## 이어서 읽기 (Reading Path)

- 이전: [서픽스 배열](Suffix-Array.md)
- 다음: [고속 거듭제곱 / 행렬 거듭제곱](Fast-Exponentiation.md)

## 참조 (References)

- [Math/Discrete/Number-Theory-Basics.md](../Math/Discrete/Number-Theory-Basics.md)
- [Engineering/Security/Asymmetric-Encryption.md](../Engineering/Security/Asymmetric-Encryption.md)
- [Reference/Books.md](../Reference/Books.md)
