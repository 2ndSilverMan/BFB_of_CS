# 양자 회로 (Quantum Circuits)

- Level: Advanced
- Prerequisites: [Quantum-Gates.md](Quantum-Gates.md), [Entanglement.md](Entanglement.md), [Algorithms/Complexity.md](../../Algorithms/Complexity.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

양자 회로는 큐비트 선(wire)에 양자 게이트와 측정을 배치해 계산을 표현하는 모델이다. 회로는 초기 상태 준비, unitary gate sequence, 측정으로 구성된다.

## 직관 (Intuition)

고전 회로가 비트에 논리 게이트를 적용하듯, 양자 회로는 큐비트에 양자 게이트를 순서대로 적용한다. 차이는 중첩, 위상, 얽힘이 계산 중간에 유지되고, 마지막 측정에서 확률적 결과가 나온다는 점이다.

## 이론 (Theory)

회로의 중요한 척도는 다음과 같다.

- width: 사용하는 큐비트 수
- depth: 의존성을 고려한 게이트 층 수
- gate count: 전체 게이트 수
- measurement: 고전 결과를 얻는 단계

양자 알고리즘은 좋은 회로를 설계해 원하는 답의 진폭을 키우고, 틀린 답의 진폭을 상쇄시키는 방식으로 작동한다. 실제 하드웨어에서는 qubit connectivity와 noise 때문에 논리 회로를 native gate로 변환하는 transpilation이 필요하다.

## 구현 (Implementation)

간단한 Bell 회로는 텍스트로도 표현할 수 있다.

```text
q0: |0> ──H──●──M
             │
q1: |0> ─────X──M
```

이 회로는 두 큐비트를 얽힌 상태로 만든 뒤 측정한다.

## 복잡도 (Complexity)

회로 복잡도는 게이트 수와 depth로 측정한다. 오류가 있는 하드웨어에서는 depth가 깊을수록 성공 확률이 낮아질 수 있다. 고전 시뮬레이션은 일반적으로 큐비트 수에 지수적으로 어려워진다.

## 응용 (Applications)

- 양자 알고리즘 표현
- 하드웨어 실행 계획
- 오류정정 회로 설계
- 양자 복잡도 이론의 계산 모델

## 흔한 오해 (Common Misunderstandings)

- 회로 그림의 선은 값이 흐르는 복사본이 아니라 같은 큐비트의 시간 진행이다.
- 중간 측정은 상태를 바꾸므로 unitary gate와 다르다.
- 깊은 회로가 항상 더 강한 것은 아니다. 노이즈와 비용이 있다.
- 고전 회로처럼 fan-out으로 임의 양자 상태를 복사할 수 없다.

## TMI

- NISQ 시대에는 얕은 변분 회로가 많이 연구되었다.
- 회로 동치 변환은 게이트 수와 depth를 줄이는 데 중요하다.
- Clifford 회로는 특정 조건에서 고전적으로 효율적으로 시뮬레이션될 수 있다.

## 연습 / 확인 문제 (Exercises)

- Bell 회로의 width와 depth를 추정하라.
- 회로 depth와 noise의 관계를 설명하라.
- 측정이 회로 중간에 들어가면 어떤 점이 달라지는지 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [얽힘](Entanglement.md)
- 다음: [Grover 알고리즘](Grover.md), [Shor 알고리즘](Shor.md)

## 참조 (References)

- [Quantum-Gates.md](Quantum-Gates.md)
- [Entanglement.md](Entanglement.md)
- [Algorithms/Complexity.md](../../Algorithms/Complexity.md)
- [Reference/Books.md](../../Reference/Books.md)
