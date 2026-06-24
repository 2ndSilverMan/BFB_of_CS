# 특이값 분해 (Singular Value Decomposition)

- Level: Advanced
- Prerequisites: [Math/Linear-Algebra/Eigenvalues.md](Eigenvalues.md), [Math/Linear-Algebra/Orthogonality.md](Orthogonality.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

특이값 분해(SVD)는 임의의 $m\times n$ 실수 행렬 $A$를 두 직교 변환과 축별 크기 조절로 분해한다.

$$
A=U\Sigma V^\top
$$

$U$와 $V$의 열은 각각 왼쪽·오른쪽 특이벡터이고, $\Sigma$의 음이 아닌 대각 원소가 특이값이다. 고유값 분해와 달리 정사각이 아니거나 랭크가 부족한 행렬에도 항상 존재한다.

## 직관 (Intuition)

행렬 변환은 단위 구를 회전하고, 서로 직교하는 축 방향으로 늘이거나 줄인 뒤 다시 회전해 타원체로 만드는 과정으로 볼 수 있다. $V^\top$가 입력 좌표축을 맞추고, $\Sigma$가 각 축을 특이값만큼 조절하며, $U$가 출력 공간의 방향을 정한다.

## 이론 (Theory)

특이값을 $\sigma_1\ge\sigma_2\ge\cdots\ge0$으로 정렬하면

$$
A=\sum_{i=1}^{r}\sigma_i\mathbf{u}_i\mathbf{v}_i^\top
$$

이며 $r=\operatorname{rank}(A)$다. $\mathbf{v}_i$는 $A^\top A$의 고유벡터, $\mathbf{u}_i$는 $AA^\top$의 고유벡터이고, 대응 고유값은 $\sigma_i^2$다.

상위 $k$개 항만 남긴

$$
A_k=\sum_{i=1}^{k}\sigma_i\mathbf{u}_i\mathbf{v}_i^\top
$$

는 Frobenius norm과 spectral norm에서 가장 좋은 랭크-$k$ 근사다. 작은 특이값을 버리면 압축과 잡음 제거가 가능하지만 중요한 작은 신호도 잃을 수 있다. 유사역행렬은 0이 아닌 특이값을 뒤집어 $A^+=V\Sigma^+U^\top$로 만든다.

## 구현 (Implementation)

```python
import numpy as np

A = np.array([[3.0, 1.0, 1.0],
              [-1.0, 3.0, 1.0]])

U, singular_values, Vt = np.linalg.svd(A, full_matrices=False)
reconstructed = U @ np.diag(singular_values) @ Vt
print(np.allclose(A, reconstructed))

k = 1
A_rank1 = U[:, :k] @ np.diag(singular_values[:k]) @ Vt[:k, :]
print(A_rank1)
```

큰 희소 행렬에서 일부 특이값만 필요하면 전체 SVD 대신 truncated/randomized SVD를 사용한다.

## 복잡도 (Complexity)

$m\ge n$인 조밀한 $m\times n$ 행렬의 전체 SVD는 대략 `O(mn^2)` 시간과 `O(mn)` 이상의 저장 공간이 필요하다. 상위 $k$개 성분만 구하는 반복·무작위 방법은 행렬-벡터 곱과 $k$에 비례해 더 큰 데이터에 적합하다.

## 응용 (Applications)

- 저랭크 행렬 압축과 잡음 제거
- 최소제곱과 유사역행렬 계산
- PCA와 잠재 의미 분석
- 조건수, 유효 랭크, 역문제 안정성 분석

## 흔한 오해 (Common Misunderstandings)

- 특이값은 음수가 아니다. 부호와 방향은 특이벡터에 흡수된다.
- SVD는 대칭·정사각 행렬에만 쓰는 분해가 아니다.
- 작은 특이값을 버리는 것이 항상 좋은 정규화는 아니다. 문제에서 그 방향이 중요한지 확인해야 한다.
- `full_matrices=True`의 전체 크기 $U,V$가 항상 필요한 것은 아니다. 축소 SVD가 메모리를 아낀다.

## TMI

- 2-norm 조건수는 가장 큰 특이값을 가장 작은 0이 아닌 특이값으로 나눈 값이다.
- Eckart–Young–Mirsky 정리가 truncated SVD의 최적 저랭크 근사를 보장한다.
- 추천 시스템에서 사용자-아이템 행렬을 저랭크 요인으로 근사하는 생각도 SVD와 밀접하다.

## 연습 / 확인 문제 (Exercises)

- 랭크 1 행렬의 특이값 중 0이 아닌 값이 몇 개인지 확인하라.
- $k$를 바꾸며 근사 오차 $\|A-A_k\|_F$를 비교하라.
- SVD로 특이한 선형 시스템의 최소 노름 해를 구하라.

## 이어서 읽기 (Reading Path)

- 이전: [직교성과 최소제곱](Orthogonality.md), [고유값과 고유벡터](Eigenvalues.md)
- 다음: [주성분 분석](PCA.md)
- 관련: [행렬 연산](Matrices.md)

## 참조 (References)

- [Math/Linear-Algebra/Eigenvalues.md](Eigenvalues.md)
- [Math/Linear-Algebra/Orthogonality.md](Orthogonality.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
