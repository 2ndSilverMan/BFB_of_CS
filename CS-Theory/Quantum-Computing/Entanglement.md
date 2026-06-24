# 얽힘 (Entanglement)

- Level: Advanced
- Prerequisites: [Qubits.md](Qubits.md), [Quantum-Gates.md](Quantum-Gates.md), [Math/Linear-Algebra/Vectors.md](../../Math/Linear-Algebra/Vectors.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

얽힘은 여러 큐비트의 상태가 각 큐비트의 독립 상태들의 텐서곱으로 분해되지 않는 현상이다. 얽힌 상태에서는 전체 상태가 국소 상태들의 단순 조합보다 더 강한 상관 구조를 가진다.

## 직관 (Intuition)

두 큐비트가 각각 따로 상태를 갖는 것이 아니라, 둘을 함께 봐야만 완전히 설명되는 상태가 있다. 측정하면 결과는 확률적이지만, 두 결과 사이에는 고전적 독립으로 설명하기 어려운 상관이 나타난다.

## 이론 (Theory)

대표적인 Bell 상태는 다음과 같다.

$$
|\Phi^+\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2}
$$

이 상태는 $|\psi\rangle\otimes|\phi\rangle$ 형태로 분해되지 않는다. 첫 번째 큐비트를 측정해 0이 나오면 두 번째도 0이고, 1이 나오면 두 번째도 1이다.

얽힘은 양자 teleportation, superdense coding, 양자 오류정정, 일부 양자 알고리즘의 핵심 자원으로 여겨진다. 다만 얽힘만으로 초광속 통신이 가능한 것은 아니다.

## 구현 (Implementation)

Bell 상태는 $|00\rangle$에 Hadamard와 CNOT을 적용해 만들 수 있다.

```text
|00⟩
  ├─ H on first qubit  → (|00⟩ + |10⟩)/√2
  └─ CNOT             → (|00⟩ + |11⟩)/√2
```

상태 벡터 시뮬레이션에서는 네 개 basis amplitude 중 $|00\rangle$와 $|11\rangle$만 1/√2를 갖는다.

## 복잡도 (Complexity)

얽힌 $n$큐비트 상태를 일반적으로 표현하려면 $2^n$개의 진폭이 필요하다. 얽힘 구조가 제한적이면 tensor network로 효율적 표현이 가능할 수 있지만, 일반 상태는 고전적으로 다루기 어렵다.

## 응용 (Applications)

- Bell pair와 양자 통신 프로토콜
- 양자 오류정정 코드
- 양자 알고리즘의 상태 준비
- 양자 정보 이론

## 흔한 오해 (Common Misunderstandings)

- 얽힘은 단순한 강한 상관관계와 다르다.
- 얽힘으로 정보를 빛보다 빠르게 보낼 수 없다.
- 중첩이 있으면 항상 얽힘이 있는 것은 아니다. 단일 큐비트 중첩은 얽힘이 아니다.
- 측정 전 상태와 측정 후 상태를 구분해야 한다.

## TMI

- Bell inequality violation은 양자 상관이 고전적 local hidden variable 이론으로 설명되기 어렵다는 신호다.
- Entanglement entropy는 부분계가 나머지와 얼마나 얽혀 있는지 재는 척도다.
- 많은-body physics와 quantum computing은 얽힘 구조 분석에서 만난다.

## 연습 / 확인 문제 (Exercises)

- $|\Phi^+\rangle$가 product state가 아님을 보이라.
- Bell 상태를 만드는 H+CNOT 회로를 단계별로 계산하라.
- 얽힘과 초광속 통신의 차이를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [양자 게이트](Quantum-Gates.md)
- 다음: [양자 회로](Quantum-Circuits.md)

## 참조 (References)

- [Qubits.md](Qubits.md)
- [Quantum-Gates.md](Quantum-Gates.md)
- [Math/Linear-Algebra/Vectors.md](../../Math/Linear-Algebra/Vectors.md)
- [Reference/Books.md](../../Reference/Books.md)
