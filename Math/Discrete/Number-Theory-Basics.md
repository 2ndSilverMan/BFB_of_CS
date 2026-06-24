# 정수론 기초 (Number Theory Basics)

- Level: Intermediate
- Prerequisites: [Math/Discrete/Induction.md](Induction.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

정수론 기초는 정수의 나눗셈, 소수, 최대공약수, 합동(모듈러 산술)을 다룬다. 암호학, 해싱, 알고리즘 설계의 수학적 토대다.

## 직관 (Intuition)

"나누어떨어짐"과 "나머지"는 단순하지만 깊은 구조를 만든다. 시계가 12를 넘으면 다시 1로 돌아가듯, 모듈러 산술은 정수를 유한한 순환 세계로 접는다. 이 순환 구조가 RSA 같은 현대 암호와 해시 함수의 핵심이다.

## 이론 (Theory)

**나눗셈 정리**: 임의의 $a$와 양의 $b$에 대해 $a=bq+r,\ 0\le r<b$가 유일하게 존재한다.

**최대공약수**와 유클리드 호제법: $\gcd(a,b)=\gcd(b,\ a\bmod b)$. 확장 유클리드는 $ax+by=\gcd(a,b)$의 해를 준다.

**소수와 산술의 기본정리**: 1보다 큰 모든 정수는 소수의 곱으로 유일하게 분해된다.

**합동**: $a\equiv b\pmod m$은 $m\mid(a-b)$. 덧셈·곱셈이 보존된다. $\gcd(a,m)=1$이면 모듈러 역원 $a^{-1}$이 존재한다. **페르마 소정리**: 소수 $p$와 $\gcd(a,p)=1$에서

$$a^{p-1}\equiv 1 \pmod p$$

이는 빠른 거듭제곱과 함께 소수 판정·암호의 기반이 된다.

## 구현 (Implementation)

```python
def gcd(a, b):
    while b:
        a, b = b, a % b      # 유클리드 호제법
    return a

def modpow(base, exp, mod):  # 빠른 거듭제곱: O(log exp)
    result = 1
    base %= mod
    while exp:
        if exp & 1:
            result = result * base % mod
        base = base * base % mod
        exp >>= 1
    return result
```

## 복잡도 (Complexity)

유클리드 호제법은 `O(log min(a,b))`로 매우 빠르다(피보나치가 최악). 빠른 거듭제곱은 `O(log exp)` 곱셈. 시험 나눗셈 소수 판정은 `O(√n)`, 에라토스테네스의 체는 `O(n log log n)`에 $n$까지의 소수를 모두 찾는다. 큰 수 소인수분해는 어려운 문제로 여겨져 암호의 안전성 근거가 된다.

## 응용 (Applications)

- RSA·Diffie-Hellman 등 공개키 암호
- 해시 함수와 해시 테이블의 모듈러 연산
- 체크섬·오류 검출(모듈러 합)
- 경쟁 프로그래밍의 모듈러 산술

## 흔한 오해 (Common Misunderstandings)

- 모듈러 나눗셈은 역원 곱이다. 그냥 나누면 안 된다(역원은 $\gcd=1$일 때만 존재).
- 페르마 소정리의 역은 항상 참이 아니다(카마이클 수 같은 반례).
- 음수의 나머지는 언어마다 부호 규약이 달라 주의해야 한다.
- 소수는 무한히 많다(유클리드의 고전적 증명).

## TMI

- "큰 수의 소인수분해는 어렵다"는 가정이 깨지면 RSA가 무너진다 — 양자 컴퓨터의 쇼어 알고리즘이 그 위협이다.
- 메르센 소수 탐색(GIMPS)은 분산 컴퓨팅으로 거대 소수를 찾는 대표적 시민 과학 프로젝트다.
- 모듈러 역원 계산에 확장 유클리드 또는 페르마 소정리($a^{p-2}$)를 쓴다.

## 연습 / 확인 문제 (Exercises)

- $\gcd(252, 105)$를 유클리드 호제법으로 구하라.
- $3^{100} \bmod 7$을 페르마 소정리와 빠른 거듭제곱으로 구하라.
- 에라토스테네스의 체로 30 이하 소수를 모두 나열하라.

## 이어서 읽기 (Reading Path)

- 이전: [수학적 귀납법](Induction.md)
- 다음: [Engineering/Security/Asymmetric-Encryption.md](../../Engineering/Security/Asymmetric-Encryption.md), [수론 알고리즘](../../Algorithms/Number-Theory.md)

## 참조 (References)

- [Engineering/Security/Asymmetric-Encryption.md](../../Engineering/Security/Asymmetric-Encryption.md)
- [Math/Discrete/Induction.md](Induction.md)
- [Reference/Books.md](../../Reference/Books.md)
