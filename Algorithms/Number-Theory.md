# 정수론 & 소수 (Number Theory Algorithms)

- Level: Advanced
- Prerequisites: [Math/Discrete/Number-Theory-Basics.md](../Math/Discrete/Number-Theory-Basics.md), [Algorithms/Complexity.md](Complexity.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

정수론 알고리즘은 소수 판정·생성, 소인수분해, GCD, 모듈러 역원, 합동식을 효율적으로 계산한다. **암호(RSA/DH)·해싱·경쟁 프로그래밍**의 수학 도구 모음이다.

## 직관 (Intuition)

"소수인가", "어떻게 인수분해되나", "모듈러 세계의 나눗셈은?"은 단순해 보여도 큰 수에선 영리한 알고리즘이 필요하다. **작은 수는 체로 한꺼번에**, **큰 수는 확률적 판정**으로 빠르게. 그리고 인수분해의 어려움이 곧 RSA의 안전성이다.

## 이론 (Theory)

### 1. 소수 생성과 판정

- **에라토스테네스 체**: $n$ 까지 모든 소수를 $O(n\log\log n)$. 각 합성수를 최소 소인수로 한 번만 지우는 **선형 체**는 $O(n)$.
- **밀러-라빈**: 페르마 소정리 $a^{n-1}\equiv1$ + "1의 자명하지 않은 제곱근 없음"을 결합한 확률적 판정. $n-1=2^r d$ 로 쓰고 증인 $a$ 로 검사. $2^{64}$ 미만은 고정 증인 12개로 **결정적**.

### 2. 소인수분해와 GCD

- **폴라드 로**: $f(x)=x^2+c$ 의 사이클을 Floyd(거북이·토끼)로 찾아 $\gcd$ 로 인수 추출, 기댓값 $O(n^{1/4})$. 소수엔 무력(먼저 판정).
- **확장 유클리드**: $ax+by=\gcd(a,b)$ 의 $x,y$ 를 구해 **모듈러 역원**($\gcd=1$ 일 때만 존재) 계산.
- **CRT**: 서로소 모듈러 합동식 연립을 유일해로 합친다.

### 3. 오일러 정리

$\varphi(n)$(서로소 개수)에 대해 $a^{\varphi(n)}\equiv1\pmod n$ ($\gcd(a,n)=1$) — 모듈러 지수의 주기를 주고, $a^{-1}\equiv a^{\varphi(n)-1}$ 로 역원도 준다(소수면 페르마 $a^{p-2}$).

## 구현 (Implementation)

```python
def sieve(n):
    p = [True]*(n+1); p[0:2] = [False, False]
    for i in range(2, int(n**0.5)+1):
        if p[i]:
            for j in range(i*i, n+1, i): p[j] = False
    return [i for i in range(2, n+1) if p[i]]

def is_prime(n):                            # 결정적 밀러-라빈 (n < 3.3e24)
    if n < 2: return False
    for q in (2,3,5,7,11,13,17,19,23,29,31,37):
        if n % q == 0: return n == q
    d, r = n-1, 0
    while d % 2 == 0: d //= 2; r += 1
    for a in (2,3,5,7,11,13,17,19,23,29,31,37):
        x = pow(a, d, n)
        if x in (1, n-1): continue
        for _ in range(r-1):
            x = x*x % n
            if x == n-1: break
        else: return False
    return True

def ext_gcd(a, b):
    if b == 0: return a, 1, 0
    g, x, y = ext_gcd(b, a % b)
    return g, y, x - (a // b) * y           # 역원: x mod m (g==1일 때)
```

## 복잡도 (Complexity)

| 연산 | 시간 |
|---|---|
| 에라토스테네스 / 선형 체 | $O(n\log\log n)$ / $O(n)$ |
| 밀러-라빈 | $O(k\log^3 n)$ |
| 폴라드 로 | 기댓값 $O(n^{1/4})$ |
| 확장 유클리드 / 모듈러 역원 | $O(\log n)$ |

**워크드 예제(역원).** $\bmod 13$ 에서 $7^{-1}$: 확장 유클리드 $7\cdot2-13\cdot1=1$ → $7^{-1}\equiv2$. 확인 $7\cdot2=14\equiv1$. **CRT** $x\equiv2(3),\,x\equiv3(5)$: $x=8$ ($8\bmod3=2,\,8\bmod5=3$).

## 응용 (Applications)

- 공개키 암호([RSA·Diffie-Hellman](../Engineering/Security/Asymmetric-Encryption.md)).
- 해시·모듈러 산술(경쟁 프로그래밍), 체크섬·부호 이론.
- 의사난수 생성, 조합론 모듈러 계산.

## 흔한 오해 (Common Misunderstandings)

- **시험 나눗셈 $O(\sqrt n)$ 은 큰 수엔 비현실적** — 밀러-라빈 필요.
- **밀러-라빈은 확률적이지만 작은 범위는 고정 증인으로 결정적**.
- **모듈러 나눗셈 = 역원 곱**, 역원은 $\gcd=1$ 일 때만 존재.
- **폴라드 로는 소수엔 무력** — 먼저 소수 판정.

## TMI

- AKS(2002)는 최초의 다항 시간 *결정적* 소수 판정으로 이론적 이정표지만, 실전은 밀러-라빈이 훨씬 빠르다.
- 폴라드 로의 "거북이와 토끼"는 [연결 리스트 사이클 탐지](../Data-Structures/Linked-List.md)의 Floyd 알고리즘을 인수분해에 응용한 것.
- RSA-250(2020) 인수분해에 약 2700 CPU-코어-년이 들었다 — 인수분해의 어려움이 암호의 토대.

## 연습 / 확인 문제 (Exercises)

- 체로 50 이하 소수를 구하고 선형 체와 비교하라.
- 확장 유클리드로 $\bmod 13$ 에서 $7$ 의 역원을 구하라.
- CRT로 $x\equiv2(3),\,x\equiv3(5)$ 를 풀어라.
- 밀러-라빈이 페르마 판정보다 강한 이유(카마이클 수)를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [서픽스 배열](Suffix-Array.md)
- 다음: [고속 거듭제곱 / 행렬 거듭제곱](Fast-Exponentiation.md)
- 관련: [비대칭 암호](../Engineering/Security/Asymmetric-Encryption.md)

## 참조 (References)

- [Math/Discrete/Number-Theory-Basics.md](../Math/Discrete/Number-Theory-Basics.md)
- [Engineering/Security/Asymmetric-Encryption.md](../Engineering/Security/Asymmetric-Encryption.md)
- [Reference/Books.md](../Reference/Books.md)
