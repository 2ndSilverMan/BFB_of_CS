# 고유값과 고유벡터 (Eigenvalues and Eigenvectors)

- Level: Intermediate
- Prerequisites: [Math/Linear-Algebra/Matrices.md](Matrices.md), [Math/Linear-Algebra/Linear-Systems.md](Linear-Systems.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

정사각 행렬 $A$가 어떤 0이 아닌 벡터 $\mathbf{v}$의 방향은 바꾸지 않고 크기만 $\lambda$배 한다면, $\mathbf{v}$를 고유벡터, $\lambda$를 고유값이라 한다.

$$
A\mathbf{v}=\lambda\mathbf{v}
$$

고유값은 선형 변환이 특별한 방향을 얼마나 늘이거나 줄이고, 반복 적용했을 때 어떤 거동이 지배적인지 보여 준다.

## 직관 (Intuition)

대부분의 벡터는 행렬을 곱하면 방향까지 바뀐다. 하지만 변환의 축에 놓인 벡터는 같은 직선 위에 남는다. 그 축이 고유벡터이고 배율이 고유값이다. 큰 절댓값의 고유값에 대응하는 방향은 변환을 반복할수록 두드러진다.

## 이론 (Theory)

고유벡터가 존재하려면

$$
(A-\lambda I)\mathbf{v}=0
$$

이 0이 아닌 해를 가져야 한다. 따라서 $A-\lambda I$가 특이해야 하고 특성방정식

$$
\det(A-\lambda I)=0
$$

의 근이 고유값이다. 서로 독립인 고유벡터를 충분히 모을 수 있으면

$$
A=V\Lambda V^{-1}, \qquad A^k=V\Lambda^kV^{-1}
$$

로 대각화할 수 있다. 모든 행렬이 실수 고유값을 가지거나 대각화되는 것은 아니다. 실대칭 행렬은 특히 좋은 성질을 가지며, 실수 고유값과 서로 직교하는 고유벡터를 가져 $A=Q\Lambda Q^\top$로 분해된다.

## 구현 (Implementation)

```python
import numpy as np

A = np.array([[2.0, 1.0],
              [1.0, 2.0]])

# 대칭 행렬에는 eig보다 eigh가 더 안정적이고 결과도 실수다.
values, vectors = np.linalg.eigh(A)
for i, value in enumerate(values):
    v = vectors[:, i]
    print(value, np.allclose(A @ v, value * v))
```

수치 계산에서는 특성다항식을 직접 만들기보다 QR 알고리즘, power iteration, Lanczos 같은 방법을 사용한다.

## 복잡도 (Complexity)

조밀한 $n\times n$ 행렬의 전체 고유값 분해는 보통 `O(n^3)` 시간과 `O(n^2)` 공간이 필요하다. 희소 행렬의 일부 극단 고유값만 필요하면 행렬-벡터 곱을 반복하는 방법으로 비용을 크게 줄일 수 있다.

## 응용 (Applications)

- 동적 시스템의 안정성 분석
- 그래프 인접·라플라시안 행렬의 스펙트럴 분석
- 공분산 행렬의 주성분 방향 계산
- Markov chain의 장기 상태와 수렴률 분석

## 흔한 오해 (Common Misunderstandings)

- 고유벡터는 0벡터가 될 수 없다.
- 고유값과 고유벡터는 정사각 행렬에 대해 정의하며, 직사각 행렬에는 SVD를 사용한다.
- 서로 다른 고유값의 고유벡터가 항상 직교하는 것은 아니다. 실대칭 행렬에서는 직교하게 고를 수 있다.
- 수치 출력의 고유벡터 부호가 달라도 오류가 아니다. $\mathbf{v}$와 $-\mathbf{v}$는 같은 고유방향이다.

## TMI

- Google의 초기 PageRank는 링크 행렬의 지배적 고유벡터를 찾는 문제로 볼 수 있다.
- spectral radius는 고유값 절댓값의 최댓값이며 반복법과 동적 시스템의 수렴에 관여한다.
- 고유값이 반복된다고 항상 고유벡터가 부족한 것은 아니지만, 부족하면 행렬은 대각화되지 않는다.

## 연습 / 확인 문제 (Exercises)

- 대각 행렬의 고유값과 고유벡터를 계산하고 기하학적으로 설명하라.
- 회전 행렬이 실수 고유벡터를 갖지 않을 수 있는 예를 찾아라.
- power iteration을 구현해 가장 큰 절댓값의 고유값을 근사하라.

## 이어서 읽기 (Reading Path)

- 이전: [선형 연립방정식](Linear-Systems.md)
- 다음: [특이값 분해](SVD.md)
- 관련: [행렬 연산](Matrices.md)

## 참조 (References)

- [Math/Linear-Algebra/Matrices.md](Matrices.md)
- [Math/Linear-Algebra/Linear-Systems.md](Linear-Systems.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
