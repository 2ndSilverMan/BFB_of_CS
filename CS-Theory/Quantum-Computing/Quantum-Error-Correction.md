# 양자 오류 수정 (Quantum Error Correction)

- Level: Advanced
- Prerequisites: [Qubits.md](Qubits.md), [Entanglement.md](Entanglement.md), [Quantum-Circuits.md](Quantum-Circuits.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

양자 오류 수정(QEC)은 노이즈·decoherence로부터 양자 정보를 지키려 **논리 큐비트 하나를 여러 물리 큐비트에 인코딩**한다. 핵심 묘기는 **상태를 측정해 망가뜨리지 않으면서 오류 정보(syndrome)만** 얻는 것이다.

## 직관 (Intuition)

고전 컴퓨터는 비트를 복사해 다수결로 오류를 잡는다. 양자 상태는 **복사 불가(no-cloning)** 라 그럴 수 없다. 대신 정보를 **얽힌 다중 큐비트**에 분산하고, "값"이 아니라 "이웃 간 패리티(어디가 어긋났나)"만 측정해 고친다.

## 이론 (Theory)

### 1. 3큐비트 비트플립 부호 (worked)

논리 상태를 분산:

$$|\psi\rangle = \alpha|0\rangle + \beta|1\rangle \;\to\; \alpha|000\rangle + \beta|111\rangle$$

(복사가 아니라 얽힘 — $\alpha|0\rangle$ 을 3개로 복사한 게 아니다.) **stabilizer 측정** $Z_1Z_2,\ Z_2Z_3$ 는 인접 큐비트의 패리티만 보고 $\alpha,\beta$ 를 노출하지 않는다:

| syndrome ($Z_1Z_2, Z_2Z_3$) | 해석 |
|---|---|
| $(+,+)$ | 오류 없음 |
| $(-,+)$ | 큐비트 1 플립 |
| $(-,-)$ | 큐비트 2 플립 |
| $(+,-)$ | 큐비트 3 플립 |

syndrome으로 어느 큐비트가 뒤집혔는지 알아 X로 되돌린다. **위상 플립**(phase flip)은 Hadamard 기저에서 같은 방식, **Shor 9큐비트 부호**가 둘 다 잡는다.

### 2. 세 가지 제약

- **no-cloning**: 미지 상태 복사 불가 → 고전 반복 부호 직접 사용 불가.
- **측정 붕괴**: 상태를 직접 측정하면 중첩이 무너짐 → syndrome만.
- **연속 오류 이산화**: 임의의 작은 회전 오류도 측정하면 {I, X, Y, Z} 조합으로 **이산화**된다(QEC가 가능한 이유).

### 3. threshold 정리와 surface code

물리 오류율이 **임계값(threshold) 이하**면, 부호를 키워 논리 오류율을 임의로 낮출 수 있다(fault-tolerant). **Surface code** 는 2D 격자에서 인접 큐비트만 측정해 ~1% 임계값으로 실현성이 높아 주류다.

## 구현 (Implementation)

```text
encode:  |ψ⟩ → α|000⟩ + β|111⟩      (CNOT 2개로 얽힘)
repeat (매 cycle):
    measure stabilizers Z1Z2, Z2Z3   # syndrome (논리값 보존)
    decode: syndrome → 가장 그럴듯한 오류
    apply X correction 또는 Pauli frame 업데이트
```

실제 구현은 하드웨어 noise model·측정 충실도(fidelity)에 크게 좌우되며, decoder(예: minimum-weight perfect matching)가 syndrome → 오류 추정을 한다.

## 복잡도 (Complexity)

| 항목 | 특성 |
|---|---|
| 논리 큐비트 1개 | 물리 큐비트 수백~수천(surface code) |
| 매 cycle | 반복 syndrome 측정 |
| fault-tolerant overhead | 매우 큼(현재 한계) |
| 확장 조건 | 물리 오류율 < threshold |

## 응용 (Applications)

- 대규모 fault-tolerant 양자 컴퓨터, [Shor](Shor.md) 같은 깊은 회로.
- 양자 메모리, 하드웨어 오류율 요구사항 분석(자원 추정).

## 흔한 오해 (Common Misunderstandings)

- **QEC ≠ 단순 복사** — no-cloning 때문에 고전 반복 부호를 그대로 못 쓴다.
- **오류율이 0이 되는 게 아니다** — threshold 이하 + overhead로 *낮출* 뿐.
- **NISQ(작은 잡음 회로)와 fault-tolerant 요구사항이 다르다**.
- **syndrome은 논리 정보를 직접 측정하지 않는다** — 그래야 중첩이 보존된다.

## TMI

- Stabilizer formalism은 다수 부호를 효율적으로 기술하는 대수 틀(Pauli 군의 부분군).
- **Magic state distillation** 은 fault-tolerant 범용 계산에서 비-Clifford 게이트를 얻는 핵심·고비용 단계다.
- 2023~2024년 여러 하드웨어가 "부호를 키울수록 논리 오류율이 내려가는" 임계값 돌파를 처음 시연했다(검토 날짜: 빠르게 변하는 분야).

## 연습 / 확인 문제 (Exercises)

- no-cloning 때문에 고전 반복 부호를 그대로 못 쓰는 이유를 설명하라.
- 3큐비트 부호에서 syndrome $(-,-)$ 이 어느 오류를 뜻하는지 표로 유도하라.
- bit flip과 phase flip의 차이와, 왜 둘 다 잡으려면 9큐비트가 필요한지 설명하라.
- threshold 정리가 "확장 가능성"에 왜 결정적인지 논하라.

## 이어서 읽기 (Reading Path)

- 이전: [Shor 알고리즘](Shor.md)
- 다음: [양자 복잡도](Quantum-Complexity.md)
- 관련: [얽힘](Entanglement.md)

## 참조 (References)

- [Qubits.md](Qubits.md)
- [Entanglement.md](Entanglement.md)
- [Quantum-Circuits.md](Quantum-Circuits.md)
- [Reference/Books.md](../../Reference/Books.md)
