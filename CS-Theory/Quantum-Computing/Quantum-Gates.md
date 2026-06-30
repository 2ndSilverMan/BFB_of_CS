# 양자 게이트 (Quantum Gates)

- Level: Advanced
- Prerequisites: [Qubits.md](Qubits.md), [Math/Linear-Algebra/Matrices.md](../../Math/Linear-Algebra/Matrices.md), [Math/Linear-Algebra/Orthogonality.md](../../Math/Linear-Algebra/Orthogonality.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

양자 게이트는 큐비트 상태에 적용되는 **unitary 변환**이다. 고전 게이트가 비트를 바꾸듯, 양자 게이트는 복소 상태 벡터의 **진폭과 위상**을 바꾼다. unitary($U^\dagger U = I$)라서 가역이고 확률 합(노름)을 보존한다.

## 직관 (Intuition)

큐비트 상태가 단위 벡터라면 게이트는 **길이를 보존하는 회전·반사**다. 측정 확률 합이 1로 유지돼야 하므로 게이트는 정보를 잃지 않는 가역 변환이어야 한다(측정은 예외 — 게이트가 아니다).

## 이론 (Theory)

### 1. 대표 게이트

$$X=\begin{bmatrix}0&1\\1&0\end{bmatrix},\quad Z=\begin{bmatrix}1&0\\0&-1\end{bmatrix},\quad H=\frac{1}{\sqrt2}\begin{bmatrix}1&1\\1&-1\end{bmatrix}$$

$X$=고전 NOT($|0\rangle\leftrightarrow|1\rangle$), $Z$=위상 플립, $H$=계산 기저를 중첩으로. **CNOT**(2큐비트)은 control이 1일 때 target을 뒤집어 **얽힘**을 만든다.

### 2. 보편 게이트 집합

임의 회로는 **{단일 큐비트 회전 + CNOT}** 또는 **{Clifford + T}** 로 임의 정밀도 근사 가능(Solovay-Kitaev). CNOT만으론 부족하고 단일 큐비트 게이트와 조합해야 한다.

### 3. no-cloning은 선형성의 귀결

게이트가 선형이라 미지 상태를 복사하는 unitary는 존재할 수 없다 — QEC가 고전 반복 부호를 못 쓰는 근본 이유.

## 구현 (Implementation)

```python
import math
def matvec(m, v):
    return [sum(m[i][j]*v[j] for j in range(len(v))) for i in range(len(m))]

H = [[1/math.sqrt(2), 1/math.sqrt(2)], [1/math.sqrt(2), -1/math.sqrt(2)]]
print(matvec(H, [1, 0]))   # [0.707, 0.707] = (|0>+|1>)/√2 = |+>
print(matvec(H, [0, 1]))   # [0.707, -0.707] = |->
```

**워크드 예제.** $H|0\rangle = \frac{1}{\sqrt2}(|0\rangle+|1\rangle)=|+\rangle$ — 측정 시 0/1이 각 50%. 다시 $H|+\rangle=|0\rangle$ (간섭으로 복원! 단순 동전 던지기가 아닌 이유). CNOT을 $H|0\rangle\otimes|0\rangle$ 에 적용하면 **벨 상태** $\frac{1}{\sqrt2}(|00\rangle+|11\rangle)$ — 최대 얽힘.

## 복잡도 (Complexity)

| 항목 | 특성 |
|---|---|
| 단일 큐비트 게이트 | $2\times2$ 변환 |
| $n$ 큐비트 고전 시뮬 | 길이 $2^n$ 벡터 → 지수 |
| 실하드웨어 | gate depth·error rate·connectivity가 관건 |

## 응용 (Applications)

- 양자 회로 구성, 중첩·간섭 생성.
- [Grover](Grover.md)·[Shor](Shor.md)의 building block, [QEC](Quantum-Error-Correction.md) syndrome 회로.

## 흔한 오해 (Common Misunderstandings)

- **게이트는 가역(unitary)** 이어야 한다 — 측정은 게이트가 아니다.
- **Hadamard는 랜덤 동전이 아니다** — 위상을 가진 중첩(그래서 $H^2=I$ 로 복원).
- **CNOT만으론 모든 계산 불가** — 단일 큐비트 게이트 필요.
- **임의 상태 복사 불가**(no-cloning) — 선형성의 귀결.

## TMI

- Pauli $X,Y,Z$ 는 Bloch sphere의 축 회전과 대응한다.
- Toffoli(CCNOT)는 고전 가역 계산의 보편 게이트로, 양자에서도 중요하다.
- 실하드웨어의 native gate set은 교재 게이트와 달라 **transpilation**(분해·매핑)이 필요하다.

## 연습 / 확인 문제 (Exercises)

- $H|0\rangle$, $H|1\rangle$ 을 계산하고 $H^2=I$ 를 확인하라.
- $X$ 가 unitary임을($X^\dagger X=I$) 확인하라.
- CNOT으로 벨 상태를 만드는 회로를 적고 얽힘을 설명하라.
- $Z$ 가 $|+\rangle$ 을 $|-\rangle$ 로 바꿈을 보여라(위상 플립).

## 이어서 읽기 (Reading Path)

- 이전: [큐비트](Qubits.md)
- 다음: [얽힘](Entanglement.md)
- 관련: [양자 회로](Quantum-Circuits.md)

## 참조 (References)

- [Qubits.md](Qubits.md)
- [Math/Linear-Algebra/Matrices.md](../../Math/Linear-Algebra/Matrices.md)
- [Math/Linear-Algebra/Orthogonality.md](../../Math/Linear-Algebra/Orthogonality.md)
- [Reference/Books.md](../../Reference/Books.md)
