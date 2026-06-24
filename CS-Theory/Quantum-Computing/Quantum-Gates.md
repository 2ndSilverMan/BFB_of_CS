# 양자 게이트 (Quantum Gates)

- Level: Advanced
- Prerequisites: [Qubits.md](Qubits.md), [Math/Linear-Algebra/Matrices.md](../../Math/Linear-Algebra/Matrices.md), [Math/Linear-Algebra/Orthogonality.md](../../Math/Linear-Algebra/Orthogonality.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

양자 게이트는 큐비트 상태에 적용되는 unitary 변환이다. 고전 논리 게이트가 비트를 바꾸듯, 양자 게이트는 복소수 상태 벡터의 진폭과 위상을 바꾼다.

## 직관 (Intuition)

큐비트 상태가 벡터라면 양자 게이트는 길이를 보존하는 회전이나 반사 같은 행렬 변환이다. 측정 확률의 총합이 1로 유지되어야 하므로, 게이트는 정보를 잃지 않는 가역 변환이어야 한다.

## 이론 (Theory)

단일 큐비트 게이트는 $2\times2$ unitary 행렬이다. 대표 게이트는 다음과 같다.

$$
X=\begin{bmatrix}0&1\\1&0\end{bmatrix},\quad
H=\frac{1}{\sqrt2}\begin{bmatrix}1&1\\1&-1\end{bmatrix}
$$

$X$는 고전 NOT처럼 $|0\rangle$와 $|1\rangle$를 바꾸고, Hadamard $H$는 계산 기저 상태를 중첩으로 만든다. 다중 큐비트 게이트인 CNOT은 control 큐비트가 1일 때 target 큐비트를 뒤집는다.

임의의 양자 회로는 보편 게이트 집합으로 근사할 수 있다. 예를 들어 단일 큐비트 회전과 CNOT을 조합하면 넓은 회로를 구성할 수 있다.

## 구현 (Implementation)

행렬-벡터 곱으로 단일 큐비트 게이트를 시뮬레이션할 수 있다.

```python
import math


def matvec(m, v):
    return [
        sum(m[i][j] * v[j] for j in range(len(v)))
        for i in range(len(m))
    ]


H = [[1 / math.sqrt(2), 1 / math.sqrt(2)],
     [1 / math.sqrt(2), -1 / math.sqrt(2)]]
zero = [1, 0]
print(matvec(H, zero))
```

다중 큐비트 게이트는 텐서곱 공간에서 작동하므로 상태 벡터 차원이 $2^n$으로 증가한다.

## 복잡도 (Complexity)

단일 큐비트 게이트는 $2$차원 변환이지만, $n$큐비트 전체 상태를 고전적으로 시뮬레이션하면 길이 $2^n$ 벡터를 다뤄야 한다. 실제 양자 하드웨어에서는 gate depth, error rate, connectivity가 중요하다.

## 응용 (Applications)

- 양자 회로 구성
- 중첩과 간섭 생성
- Grover, Shor 같은 알고리즘의 building block
- 양자 오류정정의 syndrome 측정 회로

## 흔한 오해 (Common Misunderstandings)

- 양자 게이트는 일반적으로 가역이어야 한다.
- Hadamard는 단순 랜덤 동전 던지기가 아니라 위상을 가진 중첩을 만든다.
- 측정은 unitary gate가 아니다.
- CNOT만으로는 모든 양자 계산을 만들 수 없다. 단일 큐비트 게이트와 조합해야 한다.

## TMI

- Pauli X, Y, Z는 Bloch sphere에서 축 회전과 연결된다.
- Toffoli gate는 고전 reversible computation에서 중요한 역할을 한다.
- 실제 하드웨어의 native gate set은 이론 교재의 게이트와 다를 수 있어 transpilation이 필요하다.

## 연습 / 확인 문제 (Exercises)

- $H|0\rangle$와 $H|1\rangle$를 계산하라.
- $X$ 게이트가 unitary임을 확인하라.
- CNOT이 얽힘 생성에 어떻게 사용될 수 있는지 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [큐비트](Qubits.md)
- 다음: [얽힘](Entanglement.md)

## 참조 (References)

- [Qubits.md](Qubits.md)
- [Math/Linear-Algebra/Matrices.md](../../Math/Linear-Algebra/Matrices.md)
- [Math/Linear-Algebra/Orthogonality.md](../../Math/Linear-Algebra/Orthogonality.md)
- [Reference/Books.md](../../Reference/Books.md)
