# 양자 오류 수정 (Quantum Error Correction)

- Level: Advanced
- Prerequisites: [Qubits.md](Qubits.md), [Entanglement.md](Entanglement.md), [Quantum-Circuits.md](Quantum-Circuits.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

양자 오류 수정은 노이즈와 decoherence로부터 양자 정보를 보호하기 위해 논리 큐비트를 여러 물리 큐비트에 인코딩하는 기술이다. 측정으로 상태를 망가뜨리지 않으면서 오류 syndrome을 얻는 것이 핵심이다.

## 직관 (Intuition)

고전 컴퓨터는 비트를 여러 번 복사해 다수결로 오류를 잡을 수 있다. 양자 상태는 임의로 복사할 수 없으므로, 정보를 얽힌 다중 큐비트 상태에 분산하고 오류 종류만 간접 측정해 고친다.

## 이론 (Theory)

양자 오류는 bit flip, phase flip, 또는 그 조합으로 생각할 수 있다. 오류정정 코드는 논리 상태를 더 큰 Hilbert space에 넣고, stabilizer 측정을 통해 어떤 오류가 발생했는지 syndrome을 얻는다.

중요한 제약은 다음과 같다.

- no-cloning: 미지 양자 상태를 단순 복사할 수 없다.
- 측정 문제: 상태 자체를 측정하면 중첩이 붕괴할 수 있다.
- 연속 오류: 작은 회전 오류도 basis error 조합으로 다룬다.

Surface code는 물리적으로 인접한 큐비트 격자에서 오류정정을 수행하는 대표적 코드다.

## 구현 (Implementation)

오류정정의 추상 흐름은 다음과 같다.

```text
encode logical qubit into many physical qubits
repeat:
    measure stabilizer syndromes
    infer likely error pattern
    apply correction or update Pauli frame
decode or continue computation
```

실제 구현은 하드웨어 noise model과 measurement fidelity에 크게 의존한다.

## 복잡도 (Complexity)

논리 큐비트 하나를 안정적으로 유지하려면 여러 물리 큐비트와 반복 syndrome 측정이 필요하다. fault-tolerant computation의 overhead는 매우 크며, threshold 이하 오류율을 달성해야 확장 가능성이 생긴다.

## 응용 (Applications)

- 대규모 fault-tolerant 양자 컴퓨터
- Shor 같은 깊은 회로 실행
- 양자 메모리
- 하드웨어 오류율 요구사항 분석

## 흔한 오해 (Common Misunderstandings)

- 양자 오류정정은 단순 복사와 다르다.
- 오류정정이 있으면 노이즈가 완전히 사라지는 것이 아니다. overhead와 threshold가 중요하다.
- 작은 NISQ 회로와 fault-tolerant 회로의 요구사항은 다르다.
- syndrome은 논리 정보를 직접 측정하지 않고 오류 정보만 얻도록 설계된다.

## TMI

- Stabilizer formalism은 많은 오류정정 코드를 효율적으로 설명한다.
- Magic state distillation은 fault-tolerant universal computation에서 중요한 비용 요소다.
- 오류정정은 양자 컴퓨팅의 이론과 공학이 가장 강하게 만나는 지점이다.

## 연습 / 확인 문제 (Exercises)

- no-cloning 때문에 고전 반복 부호를 그대로 쓸 수 없는 이유를 설명하라.
- bit flip과 phase flip 오류의 차이를 말하라.
- syndrome 측정이 논리 상태 측정과 달라야 하는 이유를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [Shor 알고리즘](Shor.md)
- 다음: [양자 복잡도](Quantum-Complexity.md)

## 참조 (References)

- [Qubits.md](Qubits.md)
- [Entanglement.md](Entanglement.md)
- [Quantum-Circuits.md](Quantum-Circuits.md)
- [Reference/Books.md](../../Reference/Books.md)
