# CS 이론 (CS Theory)

> 계산이란 무엇인가, 언어는 어떻게 설계되는가, 컴파일러는 어떻게 동작하는가.

**선수지식**: [Math/Discrete/](../Math/Discrete/), [Algorithms/](../Algorithms/)

---

## 현재 가용성

현재 이 섹션은 계산 이론, 프로그래밍 언어론, 컴파일러, 양자 컴퓨팅의 학습 범위를 보여주는 주제 지도다. 개별 본문은 대부분 `Planned` 상태이므로, 각 하위 README에서 `Draft` 이상으로 열린 항목부터 읽는다.

---

## 서브섹션

| 서브섹션 | 내용 | 선수지식 |
|---|---|---|
| [Computation-Theory/](Computation-Theory/) | 오토마타, 튜링 머신, 결정 불가능성, P vs NP | [Math/Discrete/](../Math/Discrete/), [Algorithms/](../Algorithms/) |
| [Programming-Languages/](Programming-Languages/) | 타입 시스템, 람다 대수, 의미론, 패러다임 | [CS-Theory/Computation-Theory/](Computation-Theory/) |
| [Compilers/](Compilers/) | 렉서, 파서, 중간 표현, 코드 생성, 최적화 | [CS-Theory/Programming-Languages/](Programming-Languages/) |
| [Quantum-Computing/](Quantum-Computing/) | 양자 게이트, 양자 알고리즘, 양자 복잡도 | [Math/Linear-Algebra/](../Math/Linear-Algebra/), [Math/Probability-Statistics/](../Math/Probability-Statistics/) |

---

## 학습 순서

```text
Computation-Theory → Programming-Languages → Compilers
                   ↘
                    Quantum-Computing (독립 가능)
```

---

## 연관 섹션

- [Algorithms/](../Algorithms/) — 복잡도 클래스, NP-완전 문제
- [Math/Discrete/](../Math/Discrete/) — 논리, 집합론, 형식 언어의 수학적 기반
- [Engineering/Security/](../Engineering/Security/) — 암호학의 계산 복잡도 기반
