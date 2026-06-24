# Grover 탐색 알고리즘 (Grover Search)

- Level: Advanced
- Prerequisites: [Quantum-Circuits.md](Quantum-Circuits.md), [Quantum-Gates.md](Quantum-Gates.md), [Algorithms/Randomized-Algorithms.md](../../Algorithms/Randomized-Algorithms.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

Grover 알고리즘은 정렬되지 않은 $N$개 후보 중 marked item을 찾는 양자 알고리즘이다. 고전적으로 $O(N)$ 질의가 필요한 black-box 탐색을 양자적으로 $O(\sqrt{N})$ 질의로 줄인다.

## 직관 (Intuition)

모든 후보를 균등 중첩으로 놓고, 정답 상태의 진폭은 키우고 나머지는 줄이는 과정을 반복한다. 정답을 직접 읽는 것이 아니라, 간섭을 이용해 측정 시 정답이 나올 확률을 높인다.

## 이론 (Theory)

Grover iteration은 두 단계로 구성된다.

1. Oracle: marked state의 위상을 뒤집는다.
2. Diffusion operator: 평균에 대한 반사를 수행해 marked amplitude를 증폭한다.

반복 횟수는 대략

$$
O(\sqrt{N})
$$

이며, 너무 많이 반복하면 진폭이 다시 줄어들 수 있다. Grover speedup은 quadratic이며, 일반 black-box search에서는 최적에 가깝다.

## 구현 (Implementation)

개념적으로는 amplitude amplification loop로 볼 수 있다.

```text
initialize uniform superposition
repeat about sqrt(N) times:
    apply oracle phase flip
    apply diffusion reflection
measure
```

실제 회로 구현에서는 oracle을 문제별로 구성해야 한다. oracle 비용까지 포함해야 전체 알고리즘 비용을 제대로 평가할 수 있다.

## 복잡도 (Complexity)

질의 복잡도는 $O(\sqrt{N})$이지만, oracle 구현 비용과 회로 depth가 중요하다. 고전 대비 지수 속도 향상은 아니며, quadratic speedup이다.

## 응용 (Applications)

- 비구조화 탐색
- amplitude amplification
- 일부 조합 문제의 search subroutine
- 대칭키 exhaustive search 비용 평가

## 흔한 오해 (Common Misunderstandings)

- Grover가 모든 검색 문제를 즉시 빠르게 만드는 것은 아니다. oracle 구성 비용이 중요하다.
- 속도 향상은 지수적이 아니라 제곱근 수준이다.
- 한 번의 중첩 측정으로 모든 후보를 읽는 것이 아니다.
- 반복을 무작정 많이 하면 성공 확률이 계속 증가하지 않는다.

## TMI

- Amplitude amplification은 Grover의 아이디어를 더 일반화한 틀이다.
- 암호 키 길이를 평가할 때 Grover를 고려하면 양자 공격에 대해 보안 비트가 대략 절반으로 줄어드는 식의 논의가 나온다.
- 여러 marked item이 있으면 반복 횟수는 marked item 수에 따라 달라진다.

## 연습 / 확인 문제 (Exercises)

- Grover의 두 반사 단계가 무엇인지 설명하라.
- $N=1,000,000$일 때 질의 수가 대략 어느 정도로 줄어드는지 계산하라.
- oracle 비용을 무시하면 안 되는 이유를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [양자 회로](Quantum-Circuits.md)
- 다음: [Shor 알고리즘](Shor.md)

## 참조 (References)

- [Quantum-Circuits.md](Quantum-Circuits.md)
- [Algorithms/Randomized-Algorithms.md](../../Algorithms/Randomized-Algorithms.md)
- [Reference/Books.md](../../Reference/Books.md)
