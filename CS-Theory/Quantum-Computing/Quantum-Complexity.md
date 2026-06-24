# 양자 복잡도 클래스 BQP (Quantum Complexity)

- Level: Advanced
- Prerequisites: [Quantum-Circuits.md](Quantum-Circuits.md), [Grover.md](Grover.md), [Shor.md](Shor.md), [CS-Theory/Computation-Theory/Complexity-Classes.md](../Computation-Theory/Complexity-Classes.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

양자 복잡도 이론은 양자 컴퓨터가 어떤 문제를 얼마나 효율적으로 풀 수 있는지 연구한다. BQP는 bounded-error quantum polynomial time의 약자로, 다항 시간 양자 알고리즘이 높은 확률로 답할 수 있는 결정 문제들의 클래스다.

## 직관 (Intuition)

양자 컴퓨터는 모든 문제를 마법처럼 빠르게 풀지 않는다. 어떤 문제에서는 큰 speedup이 있고, 어떤 문제에서는 알려진 이점이 작거나 없다. BQP는 “양자 계산으로 효율적으로 풀 수 있는 문제”의 경계를 형식화한다.

## 이론 (Theory)

BQP는 양자 회로 family가 다항 크기이고, 정답 확률이 예를 들어 $2/3$ 이상인 문제들의 클래스다. 오류 확률은 반복과 증폭으로 줄일 수 있다.

관계는 대략 다음처럼 알려져 있다.

```text
P ⊆ BPP ⊆ BQP ⊆ PSPACE
```

하지만 BQP와 NP의 정확한 관계는 알려져 있지 않다. Shor 알고리즘은 factoring이 BQP에 있음을 보여주지만, factoring은 NP-complete로 알려져 있지 않다. Grover는 일반 탐색에서 quadratic speedup을 제공하지만 NP-complete 문제가 모두 다항 시간에 풀린다는 뜻은 아니다.

## 구현 (Implementation)

복잡도 관점에서는 특정 입력 크기 $n$에 대해 uniform circuit family가 존재하는지 본다.

```text
for each input length n:
    construct quantum circuit C_n of size poly(n)
    run C_n on input x
    accept with probability >= 2/3 for yes instances
    accept with probability <= 1/3 for no instances
```

이 정의는 하드웨어 세부보다 계산 가능성과 자원 scaling에 초점을 둔다.

## 복잡도 (Complexity)

양자 알고리즘의 자원은 큐비트 수, 게이트 수, 회로 depth, oracle query 수, 오류정정 overhead로 측정한다. 이론적 BQP 알고리즘이 실용적이라는 뜻은 아니며, fault-tolerant 구현 비용을 별도로 고려해야 한다.

## 응용 (Applications)

- 양자 알고리즘의 한계 이해
- 고전/확률/양자 계산 모델 비교
- 암호 가정의 장기 안전성 평가
- 양자 우위와 시뮬레이션 난이도 분석

## 흔한 오해 (Common Misunderstandings)

- BQP가 NP를 포함하는지는 알려져 있지 않다.
- Shor가 있다고 NP-complete 문제가 모두 효율적으로 풀리는 것은 아니다.
- 양자 컴퓨터가 비결정론적 컴퓨터와 같은 것은 아니다.
- 이론적 speedup과 실용적 speedup은 다르다.

## TMI

- QMA는 양자판 NP처럼 설명되지만 세부는 다르다.
- Quantum supremacy/advantage 실험은 특정 샘플링 작업의 고전 시뮬레이션 어려움을 보이려는 방향이 많다.
- Stabilizer circuit은 양자적이지만 고전적으로 효율 시뮬레이션 가능한 중요한 부분 클래스다.

## 연습 / 확인 문제 (Exercises)

- BQP의 bounded-error 조건을 설명하라.
- Shor 알고리즘이 BQP와 암호학에 주는 의미를 설명하라.
- “BQP = NP”라고 말할 수 없는 이유를 정리하라.

## 이어서 읽기 (Reading Path)

- 이전: [양자 오류 수정](Quantum-Error-Correction.md)
- 다음: [CS-Theory/Computation-Theory/Complexity-Classes.md](../Computation-Theory/Complexity-Classes.md)

## 참조 (References)

- [Quantum-Circuits.md](Quantum-Circuits.md)
- [Grover.md](Grover.md)
- [Shor.md](Shor.md)
- [CS-Theory/Computation-Theory/Complexity-Classes.md](../Computation-Theory/Complexity-Classes.md)
- [Reference/Books.md](../../Reference/Books.md)
