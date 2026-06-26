# 큐비트와 중첩 (Qubits and Superposition)

- Level: Advanced
- Prerequisites: [Math/Linear-Algebra/Vectors.md](../../Math/Linear-Algebra/Vectors.md), [Math/Linear-Algebra/Matrices.md](../../Math/Linear-Algebra/Matrices.md), [Math/Probability-Statistics/Probability-Basics.md](../../Math/Probability-Statistics/Probability-Basics.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

큐비트는 양자 컴퓨팅의 기본 정보 단위다. 고전 비트가 0 또는 1 중 하나의 값을 갖는다면, 큐비트의 상태는 두 기저 상태 $|0\rangle$, $|1\rangle$의 복소수 선형결합으로 표현된다.

$$
|\psi\rangle = \alpha |0\rangle + \beta |1\rangle
$$

여기서 $\alpha,\beta\in\mathbb{C}$이고 정규화 조건 $|\alpha|^2+|\beta|^2=1$을 만족한다.

## 직관 (Intuition)

큐비트는 “0과 1을 동시에 몰래 들고 있는 동전”이라기보다, 측정 결과의 확률과 간섭 가능성을 담은 복소수 벡터다. 측정하기 전에는 진폭(amplitude)이 계산에 참여하고, 측정하면 확률적으로 0 또는 1이 나온다.

## 이론 (Theory)

계산 기저에서

$$
|0\rangle=\begin{bmatrix}1\\0\end{bmatrix},\quad
|1\rangle=\begin{bmatrix}0\\1\end{bmatrix}
$$

로 쓴다. 상태 $|\psi\rangle=\alpha|0\rangle+\beta|1\rangle$를 측정하면 0이 나올 확률은 $|\alpha|^2$, 1이 나올 확률은 $|\beta|^2$다. 측정 후 상태는 관측된 기저 상태로 붕괴한다.

전역 위상(global phase)은 관측 결과를 바꾸지 않는다. 즉 $|\psi\rangle$와 $e^{i\theta}|\psi\rangle$는 물리적으로 같은 상태로 본다. 반면 상대 위상은 간섭에 영향을 주므로 계산적으로 중요하다.

$n$개의 큐비트 상태 공간은 텐서곱으로 만들어지며 차원이 $2^n$이다. 이 때문에 고전 컴퓨터로 일반 양자 상태를 그대로 시뮬레이션하면 메모리가 지수적으로 증가한다. 양자 게이트는 상태 벡터의 norm을 보존하는 unitary 변환으로 표현된다.

## 구현 (Implementation)

단일 큐비트 상태의 측정 확률은 복소수 벡터에서 바로 계산할 수 있다.

```python
def normalize(alpha, beta):
    norm = (abs(alpha) ** 2 + abs(beta) ** 2) ** 0.5
    return alpha / norm, beta / norm


def measurement_probs(alpha, beta):
    alpha, beta = normalize(alpha, beta)
    return {"0": abs(alpha) ** 2, "1": abs(beta) ** 2}


alpha = 1 / (2 ** 0.5)
beta = 1j / (2 ** 0.5)
print(measurement_probs(alpha, beta))
```

상태 벡터 시뮬레이터에서는 $n$큐비트 상태를 길이 $2^n$ 복소수 배열로 저장한다.

## 복잡도 (Complexity)

단일 큐비트 계산은 작지만, $n$큐비트 상태를 일반적으로 표현하려면 $2^n$개의 복소수 진폭이 필요하다. 따라서 고전 시뮬레이션의 메모리와 연산 비용은 큐비트 수에 지수적으로 증가한다. 실제 양자 하드웨어에서는 측정 결과가 확률적이므로 통계적 추정을 위해 반복 실행이 필요하다.

## 응용 (Applications)

- 양자 게이트와 양자 회로의 기본 상태 표현
- 중첩과 간섭을 이용한 양자 알고리즘
- 양자 암호와 양자 정보 이론
- 양자 컴퓨터 고전 시뮬레이션의 한계 이해

## 흔한 오해 (Common Misunderstandings)

- 큐비트가 0과 1을 “동시에 읽을 수 있다”는 뜻은 아니다. 측정하면 하나의 결과만 나온다.
- 중첩은 단순한 확률 혼합과 다르다. 복소수 위상과 간섭이 있다.
- 큐비트를 복사할 수 있다고 가정하면 안 된다. 임의의 미지 양자 상태는 no-cloning 정리에 의해 복제할 수 없다.
- 많은 큐비트가 있다고 해서 자동으로 모든 문제가 빨라지는 것은 아니다.

## TMI

- Bloch sphere는 단일 큐비트의 순수 상태를 구 위의 점으로 시각화한다.
- Hadamard gate는 $|0\rangle$를 $(|0\rangle+|1\rangle)/\sqrt2$ 형태의 균등 중첩으로 만든다.
- 양자 알고리즘의 힘은 가능한 답을 “모두 읽는 것”이 아니라, 잘못된 경로의 진폭을 상쇄하고 원하는 경로의 진폭을 키우는 간섭에서 나온다.

## 연습 / 확인 문제 (Exercises)

- $\alpha=3/5$, $\beta=4i/5$인 큐비트의 측정 확률을 계산하라.
- 전역 위상과 상대 위상의 차이를 예시로 설명하라.
- $n$큐비트 상태 벡터를 고전 메모리에 저장할 때 필요한 진폭 개수를 구하라.

## 이어서 읽기 (Reading Path)

- 이전: [Math/Linear-Algebra/Vectors.md](../../Math/Linear-Algebra/Vectors.md)
- 다음: [양자 게이트](Quantum-Gates.md)

## 참조 (References)

- [Math/Linear-Algebra/Vectors.md](../../Math/Linear-Algebra/Vectors.md)
- [Math/Linear-Algebra/Matrices.md](../../Math/Linear-Algebra/Matrices.md)
- [Math/Probability-Statistics/Probability-Basics.md](../../Math/Probability-Statistics/Probability-Basics.md)
- [Reference/Books.md](../../Reference/Books.md)
