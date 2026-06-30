# 양자 회로 (Quantum Circuits)

- Level: Advanced
- Prerequisites: [Quantum-Gates.md](Quantum-Gates.md), [Entanglement.md](Entanglement.md), [Algorithms/Complexity.md](../../Algorithms/Complexity.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

양자 회로는 큐비트 선(wire)에 게이트와 측정을 배치해 계산을 표현하는 모델이다. **초기 상태 준비 → unitary 게이트 열 → 측정** 으로 구성되며, 양자 복잡도 이론의 표준 계산 모델이다.

## 직관 (Intuition)

고전 회로가 비트에 논리 게이트를 적용하듯, 양자 회로는 큐비트에 게이트를 순서대로 적용한다. 차이는 **중첩·위상·얽힘이 중간에 유지**되고, 알고리즘이 정답 진폭을 키우고 오답을 상쇄(간섭)시킨 뒤, **마지막 측정에서 확률적 결과**가 나온다는 점.

## 이론 (Theory)

### 1. 회로 척도

| 척도 | 의미 |
|---|---|
| width | 큐비트 수 |
| depth | 의존성을 고려한 게이트 **층** 수(병렬 적용 가능 게이트는 같은 층) |
| gate count | 전체 게이트 수 |
| measurement | 고전 결과 추출 |

depth가 핵심 — 노이즈 하드웨어에선 **depth가 깊을수록 성공 확률이 떨어진다**(decoherence 누적).

### 2. transpilation

논리 회로를 하드웨어의 **native gate set + qubit connectivity** 에 맞게 변환(분해·SWAP 삽입). 연결 안 된 큐비트 간 2-게이트는 SWAP으로 옮겨야 해 depth가 늘어난다.

### 3. Gottesman-Knill

**Clifford 게이트(H, S, CNOT)만의 회로는 고전적으로 효율 시뮬레이션 가능** — 양자 우위에는 비-Clifford(T 게이트)가 필요하다는 중요한 경계.

## 구현 (Implementation)

```text
q0: |0> ──H──●──M        # depth 분석:
             │           #  층1: H(q0)
q1: |0> ─────X──M        #  층2: CNOT(q0,q1)
                         #  층3: 측정
                         # width=2, depth=2(게이트), gate count=2
```

이 벨 회로는 두 큐비트를 얽힌 상태 $\frac{|00\rangle+|11\rangle}{\sqrt2}$ 로 만든 뒤 측정 → 결과는 항상 `00` 또는 `11`(상관).

## 복잡도 (Complexity)

| 항목 | 특성 |
|---|---|
| 회로 비용 | gate count·depth |
| 노이즈 하드웨어 | depth↑ → 성공 확률↓ |
| 고전 시뮬레이션 | 일반적으로 큐비트 수에 **지수** (Clifford는 예외) |

## 응용 (Applications)

- 양자 알고리즘 표현, 하드웨어 실행 계획.
- [오류정정](Quantum-Error-Correction.md) 회로 설계, 양자 복잡도 모델([BQP](Quantum-Complexity.md)).

## 흔한 오해 (Common Misunderstandings)

- **회로의 선은 값의 복사본이 아니라** 같은 큐비트의 시간 진행이다.
- **중간 측정은 상태를 바꾼다** — unitary 게이트와 다르다(deferred measurement 정리로 끝으로 미룰 수 있음).
- **깊은 회로가 항상 강하지 않다** — 노이즈·비용.
- **fan-out으로 임의 양자 상태 복사 불가**(no-cloning).

## TMI

- NISQ 시대엔 노이즈를 견디려 **얕은 변분 회로**(VQE·QAOA)가 많이 연구됐다.
- 회로 동치 변환(게이트 재작성)으로 depth·gate count를 줄이는 게 컴파일의 핵심.
- "deferred measurement" 정리: 중간 측정을 회로 끝으로 미뤄도 결과가 같다(이론 분석에 유용).

## 연습 / 확인 문제 (Exercises)

- 위 벨 회로의 width·depth·gate count를 구하라.
- 회로 depth와 노이즈(성공 확률)의 관계를 설명하라.
- 연결 안 된 큐비트 간 CNOT에 SWAP이 왜 필요한지(transpilation) 설명하라.
- Clifford 회로가 왜 고전 시뮬 가능한지(Gottesman-Knill) 의미를 적어라.

## 이어서 읽기 (Reading Path)

- 이전: [얽힘](Entanglement.md)
- 다음: [Grover 알고리즘](Grover.md)
- 관련: [양자 복잡도](Quantum-Complexity.md)

## 참조 (References)

- [Quantum-Gates.md](Quantum-Gates.md)
- [Entanglement.md](Entanglement.md)
- [Algorithms/Complexity.md](../../Algorithms/Complexity.md)
- [Reference/Books.md](../../Reference/Books.md)
