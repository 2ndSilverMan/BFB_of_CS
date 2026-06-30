# Shor 소인수 분해 알고리즘 (Shor's Algorithm)

- Level: Advanced
- Prerequisites: [Quantum-Circuits.md](Quantum-Circuits.md), [Algorithms/Number-Theory.md](../../Algorithms/Number-Theory.md), [Math/Linear-Algebra/Vectors.md](../../Math/Linear-Algebra/Vectors.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

Shor는 큰 정수의 **소인수분해와 이산 로그를 양자 컴퓨터에서 다항 시간**에 푼다. RSA·Diffie-Hellman·ECC의 안전성 가정을 장기적으로 위협하는 대표 양자 알고리즘이다.

## 직관 (Intuition)

소인수분해를 직접 풀지 않고 **함수의 주기(period) 찾기**로 환원한다. 주기 찾기는 고전적으론 어렵지만, **양자 푸리에 변환(QFT)** 이 중첩 + 간섭으로 주기를 효율적으로 드러낸다. "어려운 문제를 양자가 잘하는 문제로 번역"하는 것이 핵심.

## 이론 (Theory)

### 1. 소인수분해 → 주기 찾기

$N$ 을 인수분해하려면 $a$ 와 서로소인 $a$ 에 대해

$$f(x)=a^x \bmod N$$

의 주기 $r$(= $a^r\equiv1$ 인 최소 양수)을 찾는다. $r$ 이 짝수이고 $a^{r/2}\not\equiv-1$ 이면

$$\gcd(a^{r/2}-1,\ N),\quad \gcd(a^{r/2}+1,\ N)$$

이 $N$ 의 **비자명 인수**를 준다.

### 2. 양자 vs 고전 분담

양자 부분은 **주기 찾기**(modular exponentiation을 중첩으로 + QFT로 주기 추출). gcd·검증은 고전. QFT는 주기 $r$ 의 배수에서 진폭이 보강 간섭되도록 만들어, 측정하면 $r$ 을 알아낼 정보가 나온다.

## 구현 (Implementation)

```python
import math
def factors_from_period(a, r, n):
    if r % 2 == 1: return None                     # 홀수 주기는 실패(다른 a 재시도)
    x = pow(a, r // 2, n)
    if x == n - 1: return None                     # a^(r/2) ≡ -1 이면 실패
    return math.gcd(x - 1, n), math.gcd(x + 1, n)

print(factors_from_period(a=7, r=4, n=15))         # (3, 5)
```

**워크드 예제($N=15, a=7$).** $7^1=7,\ 7^2=49\equiv4,\ 7^3\equiv13,\ 7^4\equiv1 \pmod{15}$ → 주기 $r=4$. $7^{2}=49$, $\gcd(49-1,15)=\gcd(48,15)=3$, $\gcd(49+1,15)=\gcd(50,15)=5$ → $15=3\times5$. 양자 부분이 한 일은 *오직* $r=4$ 를 찾은 것.

## 복잡도 (Complexity)

| | 시간 |
|---|---|
| Shor(양자) | $O((\log N)^3)$ 다항 |
| 최선 고전(GNFS) | 준지수 $e^{O((\log N)^{1/3}(\log\log N)^{2/3})}$ |

이론은 다항이나, 실용 대규모 실행은 **큐비트 수·gate fidelity·[오류정정](Quantum-Error-Correction.md) overhead** 가 큰 과제다(2048비트 RSA엔 수백만 물리 큐비트 추정).

## 응용 (Applications)

- 정수 소인수분해·이산 로그, RSA/DH/ECC의 장기 위험 평가.
- **post-quantum cryptography**(양자에도 안전한 고전 알고리즘) 필요성의 근거.

## 흔한 오해 (Common Misunderstandings)

- **Shor가 모든 암호를 깨지 않는다** — 인수분해/이산로그 기반만(대칭키·해시는 [Grover](Grover.md) 수준 영향).
- **다항 시간 ≠ 지금 큰 키를 깰 수 있다** — 하드웨어가 아직 한참 부족.
- **QFT가 답을 출력하는 게 아니라** 주기 정보를 추출하게 돕는다.
- **Shor(지수 speedup)와 Grover(제곱근)의 성격이 다르다**.

## TMI

- 주기 찾기는 **hidden subgroup problem**(아벨 군)의 사례 — Shor가 그 특수 경우다.
- "Q-day"(양자가 RSA를 깨는 날)에 대비해 NIST가 2024년 post-quantum 표준(ML-KEM 등)을 확정했다(검토 날짜 주의: 빠르게 변하는 분야).
- "harvest now, decrypt later"(지금 암호문을 저장했다 미래에 복호) 위협 때문에 전환이 서둘러진다.

## 연습 / 확인 문제 (Exercises)

- $N=15, a=7, r=4$ 의 gcd 후처리로 인수 3, 5를 유도하라.
- $a=2, N=15$ 의 주기를 직접 구하고 인수분해하라.
- Shor가 인수분해를 왜 주기 찾기로 바꾸는지 설명하라.
- Shor와 Grover의 speedup 성격(지수 vs 제곱근)을 대조하라.

## 이어서 읽기 (Reading Path)

- 이전: [Grover 알고리즘](Grover.md)
- 다음: [양자 오류 수정](Quantum-Error-Correction.md)
- 관련: [정수론 & 소수](../../Algorithms/Number-Theory.md)

## 참조 (References)

- [Algorithms/Number-Theory.md](../../Algorithms/Number-Theory.md)
- [Engineering/Security/Asymmetric-Encryption.md](../../Engineering/Security/Asymmetric-Encryption.md)
- [Reference/Books.md](../../Reference/Books.md)
