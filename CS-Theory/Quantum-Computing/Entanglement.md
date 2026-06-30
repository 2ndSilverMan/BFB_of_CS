# 얽힘 (Entanglement)

- Level: Advanced
- Prerequisites: [Qubits.md](Qubits.md), [Quantum-Gates.md](Quantum-Gates.md), [Math/Linear-Algebra/Vectors.md](../../Math/Linear-Algebra/Vectors.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

얽힘은 여러 큐비트의 합동 상태가 **각 큐비트 상태의 텐서곱으로 분해되지 않는** 현상이다. 얽힌 상태는 국소 상태들의 단순 조합보다 강한 상관을 가져, 양자 통신·QEC·알고리즘의 핵심 **자원**이 된다.

## 직관 (Intuition)

두 큐비트가 각각 따로 상태를 갖는 게 아니라, **둘을 함께 봐야만** 완전히 설명되는 상태가 있다. 측정 결과는 확률적이지만 두 결과 사이에 고전적 독립으로 설명 안 되는 상관이 나타난다.

## 이론 (Theory)

### 1. Bell 상태와 분해 불가 증명

$$|\Phi^+\rangle=\frac{|00\rangle+|11\rangle}{\sqrt2}$$

이게 product state $(a|0\rangle+b|1\rangle)\otimes(c|0\rangle+d|1\rangle)=ac|00\rangle+ad|01\rangle+bc|10\rangle+bd|11\rangle$ 라면 $ac=bd=\frac{1}{\sqrt2}$ 이고 $ad=bc=0$ 이어야 한다. 그런데 $ad=0$ 이면 $a=0$ 또는 $d=0$ → $ac$ 또는 $bd$ 가 0 → 모순. **분해 불가 = 얽힘**. 첫 큐비트 측정이 0이면 둘째도 0, 1이면 둘째도 1.

### 2. Bell 부등식과 비국소성

CHSH 부등식에서 고전 local hidden variable는 상관값 $\le 2$ 인데, 얽힘은 $2\sqrt2$ 까지(Tsirelson) 위반한다. 이 **위반**이 양자 상관이 고전 국소 이론으로 설명 안 됨을 실험으로 보인다(2022 노벨물리).

### 3. no-signaling

얽힘은 **초광속 통신 불가** — 한쪽 측정의 *국소* 통계는 상대 행동과 무관하다(no-signaling). 상관은 둘의 결과를 *나중에 비교*해야 드러난다.

## 구현 (Implementation)

H + CNOT으로 벨 상태 생성:

```text
|00⟩
  ├─ H on q0   → (|00⟩ + |10⟩)/√2
  └─ CNOT(q0→q1) → (|00⟩ + |11⟩)/√2   # q0=1일 때만 q1 플립 → 얽힘
```

상태 벡터 시뮬레이션에선 네 진폭 중 $|00\rangle,|11\rangle$ 만 $1/\sqrt2$, $|01\rangle,|10\rangle$ 은 0.

## 복잡도 (Complexity)

| 항목 | 특성 |
|---|---|
| 일반 $n$ 큐비트 얽힘 표현 | $2^n$ 진폭(고전적으로 어려움) |
| 제한된 얽힘 구조 | tensor network로 효율 표현 가능 |
| 얽힘 entropy | 부분계-나머지 얽힘 정도 척도 |

## 응용 (Applications)

- **양자 teleportation**(얽힘 + 고전 2비트로 미지 상태 전송), **superdense coding**(1큐비트로 2고전비트).
- [QEC](Quantum-Error-Correction.md)(정보 분산), 양자 알고리즘 상태 준비, 양자 정보 이론.

## 흔한 오해 (Common Misunderstandings)

- **얽힘 ≠ 단순 강한 상관** — 고전 상관으로 재현 불가(Bell 위반).
- **얽힘으로 정보를 빛보다 빠르게 못 보낸다** — no-signaling.
- **중첩이 있어도 얽힘이 없을 수 있다** — 단일 큐비트 중첩($|+\rangle$)은 얽힘 아님.
- **측정 전/후 상태를 구분**해야 한다(측정이 붕괴).

## TMI

- 텔레포테이션은 상태를 "복사"가 아니라 "이동"한다 — no-cloning과 모순되지 않게 원본이 파괴된다.
- entanglement entropy는 many-body 물리와 양자 컴퓨팅이 만나는 지점이다(area law).
- "spooky action at a distance"는 아인슈타인이 얽힘을 불편해하며 쓴 표현(EPR 역설)이다.

## 연습 / 확인 문제 (Exercises)

- $|\Phi^+\rangle$ 가 product state가 아님을 위 모순 논법으로 보여라.
- 벨 상태를 만드는 H+CNOT 회로를 단계별로 계산하라.
- 얽힘과 초광속 통신의 차이를 no-signaling으로 설명하라.
- 텔레포테이션이 no-cloning을 어기지 않는 이유를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [양자 게이트](Quantum-Gates.md)
- 다음: [양자 회로](Quantum-Circuits.md)
- 관련: [큐비트](Qubits.md)

## 참조 (References)

- [Qubits.md](Qubits.md)
- [Quantum-Gates.md](Quantum-Gates.md)
- [Math/Linear-Algebra/Vectors.md](../../Math/Linear-Algebra/Vectors.md)
- [Reference/Books.md](../../Reference/Books.md)
