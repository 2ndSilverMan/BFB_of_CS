# 행렬 연산 (Matrix Operations)

- Level: Intermediate
- Prerequisites: [Math/Linear-Algebra/Vectors.md](Vectors.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

행렬은 수를 2차원 격자로 배열한 것이다. $m \times n$ 행렬은 $m$개의 행과 $n$개의 열을 가진다. 행렬은 단순한 표가 아니라 **선형 변환**(회전·확대·투영 등)을 나타내는 도구이며, 머신러닝의 거의 모든 연산이 행렬 곱으로 표현된다.

## 직관 (Intuition)

벡터가 "점"이라면, 행렬은 "점을 다른 점으로 옮기는 규칙"이다. 행렬을 벡터에 곱하면 그 벡터가 회전·확대·반사된다. 여러 데이터를 한꺼번에 변환할 때, 행렬 한 번의 곱으로 전부 처리할 수 있어 효율적이다.

## 이론 (Theory)

행렬 곱 $C = AB$는 $A$가 $m \times k$, $B$가 $k \times n$일 때 정의되며,

$$C_{ij} = \sum_{l=1}^{k} A_{il}\,B_{lj}$$

주요 연산과 성질:

| 개념 | 설명 |
|---|---|
| 전치 $A^\top$ | 행과 열을 뒤바꿈 |
| 항등 행렬 $I$ | $AI = IA = A$ |
| 역행렬 $A^{-1}$ | $AA^{-1} = I$ (정칙 행렬일 때만 존재) |
| 비가환성 | 일반적으로 $AB \ne BA$ |

행렬 곱은 두 선형 변환의 합성에 대응한다. 먼저 $B$로, 그다음 $A$로 변환하는 것이 $AB$다.

## 구현 (Implementation)

```python
import numpy as np

A = np.array([[1, 2],
              [3, 4]])
B = np.array([[5, 6],
              [7, 8]])

print(A @ B)        # 행렬 곱
# [[19 22]
#  [43 50]]
print(A.T)          # 전치
print(np.linalg.inv(A))   # 역행렬
```

## 복잡도 (Complexity)

| 연산 | 시간 (정사각 `n×n`) |
|---|---|
| 덧셈, 전치 | `O(n^2)` |
| 곱셈(소박한 방법) | `O(n^3)` |
| 역행렬 | `O(n^3)` |

행렬 곱은 빠른 알고리즘(Strassen 등)으로 더 줄일 수 있지만, 실무에서는 고도로 최적화된 라이브러리(BLAS)와 GPU가 처리한다.

## 응용 (Applications)

- 신경망의 각 층: 입력 벡터에 가중치 행렬을 곱함
- 배치 처리: 여러 샘플을 행렬 한 번으로 변환
- 그래픽스의 변환·투영, 물리 시뮬레이션
- 선형 연립방정식, 최소제곱, 차원 축소(PCA)

## 흔한 오해 (Common Misunderstandings)

- 행렬 곱은 교환법칙이 성립하지 않는다. $AB$와 $BA$는 다르고, $BA$는 정의조차 안 될 수 있다.
- 모든 행렬에 역행렬이 있는 것은 아니다. 정사각이면서 정칙(행렬식 ≠ 0)일 때만 존재한다.
- 행렬 곱은 성분별 곱(`*`, Hadamard)과 다르다. numpy에서 `@`와 `*`를 혼동하기 쉽다.
- 차원이 맞아야 곱이 정의된다. $A$의 열 수 = $B$의 행 수.

## TMI

- 딥러닝 학습 시간의 대부분은 사실상 거대한 행렬 곱이다. GPU·TPU가 AI에 필수가 된 이유가 바로 행렬 곱 병렬화다.
- 두 행렬을 곱할 수 있는지 빠르게 점검하려면 "안쪽 차원이 같은가"만 보면 된다: $(m \times k)(k \times n)$.

## 연습 / 확인 문제 (Exercises)

- $2 \times 3$ 행렬과 $3 \times 2$ 행렬을 곱하면 결과의 크기는 얼마인가?
- $AB \ne BA$인 구체적인 $2 \times 2$ 예를 만들어 보라.
- 항등 행렬을 곱해도 원래 행렬이 변하지 않음을 코드로 확인하라.

## 이어서 읽기 (Reading Path)

- 이전: [벡터와 벡터 공간](Vectors.md)
- 다음: 선형 연립방정식 (예정 `Linear-Systems.md`), 고유값과 고유벡터 (예정 `Eigenvalues.md`)

## 참조 (References)

- [Math/Linear-Algebra/Vectors.md](Vectors.md)
- [AI/Deep-Learning/](../../AI/Deep-Learning/)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
