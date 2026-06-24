# Shor 소인수 분해 알고리즘 (Shor's Algorithm)

- Level: Advanced
- Prerequisites: [Quantum-Circuits.md](Quantum-Circuits.md), [Algorithms/Number-Theory.md](../../Algorithms/Number-Theory.md), [Math/Linear-Algebra/Vectors.md](../../Math/Linear-Algebra/Vectors.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

Shor 알고리즘은 큰 정수의 소인수분해와 이산 로그 문제를 양자 컴퓨터에서 다항 시간에 풀 수 있음을 보여준 알고리즘이다. 현대 공개키 암호의 일부 기반 가정에 큰 영향을 주는 대표 양자 알고리즘이다.

## 직관 (Intuition)

소인수분해 문제를 직접 푸는 대신, 특정 함수의 주기(period)를 찾는 문제로 바꾼다. 양자 Fourier transform은 중첩과 간섭을 이용해 이 주기 정보를 효율적으로 드러낸다.

## 이론 (Theory)

정수 $N$을 인수분해하려면 임의의 $a$에 대해 함수

$$
f(x)=a^x \bmod N
$$

의 주기 $r$을 찾는 문제가 중요하다. 적절한 조건에서 $r$을 알면

$$
\gcd(a^{r/2}-1,N),\quad \gcd(a^{r/2}+1,N)
$$

으로 비자명 인수를 얻을 수 있다.

양자 부분은 주기 찾기이며, modular exponentiation과 quantum Fourier transform을 사용한다. 나머지 gcd 계산 등은 고전 알고리즘으로 처리한다.

## 구현 (Implementation)

Shor 알고리즘의 고전 후처리 직관은 다음과 같다.

```python
import math


def factors_from_period(a, r, n):
    if r % 2 == 1:
        return None
    x = pow(a, r // 2, n)
    return math.gcd(x - 1, n), math.gcd(x + 1, n)


print(factors_from_period(a=2, r=4, n=15))
```

실제 양자 회로에서 큰 수를 인수분해하려면 오류정정된 대규모 양자 컴퓨터가 필요하다.

## 복잡도 (Complexity)

Shor 알고리즘은 이론적으로 다항 시간 양자 알고리즘이다. 하지만 실용적 대규모 실행은 큐비트 수, gate fidelity, 오류정정 overhead가 큰 과제다. 현재 암호 전환 논의는 이런 장기적 위협을 고려한다.

## 응용 (Applications)

- 정수 소인수분해
- 이산 로그 문제
- RSA, Diffie-Hellman, ECC 기반 암호의 장기 위험 평가
- post-quantum cryptography 필요성 설명

## 흔한 오해 (Common Misunderstandings)

- Shor가 모든 암호를 깨는 것은 아니다. 특정 수학 문제 기반 공개키 암호가 영향권이다.
- 알고리즘이 다항 시간이라고 해서 현재 임의의 큰 키를 쉽게 깰 수 있다는 뜻은 아니다.
- 양자 Fourier transform 자체가 답을 출력하는 것이 아니라 주기 정보를 추출하게 돕는다.
- Grover와 Shor의 speedup 성격은 다르다.

## TMI

- Shor 알고리즘은 양자 계산의 잠재력을 대중적으로 알린 가장 유명한 결과 중 하나다.
- Post-quantum cryptography는 양자 컴퓨터에도 안전하다고 믿는 고전 알고리즘을 연구한다.
- 주기 찾기 문제는 hidden subgroup problem의 중요한 사례로 볼 수 있다.

## 연습 / 확인 문제 (Exercises)

- $N=15$, $a=2$, 주기 $r=4$일 때 gcd 후처리를 계산하라.
- Shor 알고리즘이 소인수분해를 주기 찾기로 바꾸는 이유를 설명하라.
- Shor와 Grover의 speedup 차이를 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [Grover 알고리즘](Grover.md)
- 다음: [양자 오류 수정](Quantum-Error-Correction.md)

## 참조 (References)

- [Algorithms/Number-Theory.md](../../Algorithms/Number-Theory.md)
- [Engineering/Security/Asymmetric-Encryption.md](../../Engineering/Security/Asymmetric-Encryption.md)
- [Reference/Books.md](../../Reference/Books.md)
