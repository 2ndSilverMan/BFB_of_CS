# 특이값 분해 (Singular Value Decomposition)

- Level: Intermediate
- Prerequisites: [Math/Linear-Algebra/Eigenvalues.md](Eigenvalues.md), [Math/Linear-Algebra/Orthogonality.md](Orthogonality.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

특이값 분해(SVD)는 임의의 $m\times n$ 실수 행렬 $A$를 두 직교 변환과 축별 크기 조절로 분해한다.

$$
A=U\Sigma V^\top
$$

$U$와 $V$의 열은 각각 왼쪽·오른쪽 특이벡터이고, $\Sigma$의 음이 아닌 대각 원소가 특이값이다. 고유값 분해와 달리 정사각이 아니거나 랭크가 부족한 행렬에도 항상 존재한다.

## 직관 (Intuition)

행렬 변환은 단위 구를 회전하고, 서로 직교하는 축 방향으로 늘이거나 줄인 뒤 다시 회전해 타원체로 만드는 과정으로 볼 수 있다. $V^\top$가 입력 좌표축을 맞추고, $\Sigma$가 각 축을 특이값만큼 조절하며, $U$가 출력 공간의 방향을 정한다.

```mermaid
flowchart LR
    X["입력 공간"] --> VT["V^T<br/>입력 축 정렬"]
    VT --> S["Sigma<br/>축별 스케일"]
    S --> U["U<br/>출력 축 회전"]
    U --> Y["출력 공간"]
```

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

### shape로 보는 축소 SVD

$A$가 $m\times n$, 랭크가 $r$이면 축소 SVD는 다음 모양을 갖는다.

| 항 | 모양 | 의미 |
|---|---|---|
| $U_r$ | $m\times r$ | 출력 공간의 직교 축 |
| $\Sigma_r$ | $r\times r$ | 0이 아닌 특이값 |
| $V_r^\top$ | $r\times n$ | 입력 공간의 직교 축 |

`full_matrices=False`는 보통 이 축소 형태를 반환한다. 실제 데이터 분석에서는 0이 아닌 특이값 전부가 아니라 상위 $k$개만 쓰는 경우가 많아 $U_k\Sigma_kV_k^\top$가 압축된 표현이 된다.

### 특이값 간격과 해석

특이값이 급격히 떨어지면 상위 몇 개 방향만으로 행렬의 대부분 구조를 설명할 수 있다. 반대로 완만하게 떨어지면 명확한 저차원 구조가 약하다는 뜻일 수 있다. 작은 특이값을 뒤집는 유사역행렬은 잡음을 크게 증폭할 수 있으므로, 실제 구현에서는 임계값 아래 특이값을 0처럼 처리하는 truncated SVD나 Tikhonov 정규화를 사용한다.

손계산으로는 대각 행렬이 가장 쉽다. $A=\operatorname{diag}(3,1)$이면 입력 축과 출력 축이 이미 맞춰져 있으므로 $U=I$, $V=I$, 특이값은 $3,1$이다. 상위 1개만 남기면 두 번째 축 정보를 버린 $\operatorname{diag}(3,0)$이 되어, 랭크 1 근사로는 첫 축의 변화만 보존한다.

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
print(np.linalg.norm(A - A_rank1, ord="fro"))
```

큰 희소 행렬에서 일부 특이값만 필요하면 전체 SVD 대신 truncated/randomized SVD를 사용한다.

유사역행렬은 작은 특이값 처리 기준을 명시해야 안정적이다.

```python
tol = 1e-10
sigma_inv = np.array([1 / s if s > tol else 0.0 for s in singular_values])
A_pinv = Vt.T @ np.diag(sigma_inv) @ U.T
print(np.allclose(A_pinv, np.linalg.pinv(A)))
```

## 복잡도 (Complexity)

$m\ge n$인 조밀한 $m\times n$ 행렬의 전체 SVD는 대략 `O(mn^2)` 시간과 `O(mn)` 이상의 저장 공간이 필요하다. 상위 $k$개 성분만 구하는 반복·무작위 방법은 행렬-벡터 곱과 $k$에 비례해 더 큰 데이터에 적합하다.

저장 관점에서 원래 행렬은 `mn`개 숫자가 필요하지만, 랭크-$k$ 근사는 $mk + k + nk$개 정도면 된다. $k \ll \min(m,n)$이면 압축 이득이 크다.

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
- 고유값과 특이값은 다르다. 대칭 양의 준정부호 행렬에서는 연결이 강하지만, 일반 행렬에서는 해석이 달라진다.
- 설명력이 큰 특이값 방향이 항상 예측에 중요한 방향이라는 보장은 없다. PCA와 마찬가지로 레이블을 보지 않는 구조다.

## TMI

- 2-norm 조건수는 가장 큰 특이값을 가장 작은 0이 아닌 특이값으로 나눈 값이다.
- Eckart–Young–Mirsky 정리가 truncated SVD의 최적 저랭크 근사를 보장한다.
- 추천 시스템에서 사용자-아이템 행렬을 저랭크 요인으로 근사하는 생각도 SVD와 밀접하다.

## 연습 / 확인 문제 (Exercises)

- 랭크 1 행렬의 특이값 중 0이 아닌 값이 몇 개인지 확인하라.
- $k$를 바꾸며 근사 오차 $\|A-A_k\|_F$를 비교하라.
- SVD로 특이한 선형 시스템의 최소 노름 해를 구하라.
- `full_matrices=True/False` 결과의 shape를 비교하고, 언제 축소 SVD가 충분한지 설명하라.
- 작은 특이값 하나를 인위적으로 만든 행렬에서 유사역행렬이 잡음을 어떻게 증폭하는지 실험하라.

## 이어서 읽기 (Reading Path)

- 이전: [직교성과 최소제곱](Orthogonality.md), [고유값과 고유벡터](Eigenvalues.md)
- 다음: [주성분 분석](PCA.md)
- 관련: [행렬 연산](Matrices.md)

## 참조 (References)

- [Math/Linear-Algebra/Eigenvalues.md](Eigenvalues.md)
- [Math/Linear-Algebra/Orthogonality.md](Orthogonality.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
