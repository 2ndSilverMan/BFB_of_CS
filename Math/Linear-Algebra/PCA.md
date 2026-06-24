# 주성분 분석 (Principal Component Analysis)

- Level: Intermediate
- Prerequisites: [Math/Linear-Algebra/SVD.md](SVD.md), [Math/Probability-Statistics/Expectation.md](../Probability-Statistics/Expectation.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

주성분 분석(PCA)은 데이터의 분산을 가장 많이 보존하는 서로 직교한 방향을 찾아 저차원으로 투영하는 비지도 선형 차원 축소 방법이다. 첫 주성분은 분산이 가장 큰 방향이고, 다음 성분은 앞선 성분과 직교하면서 남은 분산을 가장 많이 설명한다.

## 직관 (Intuition)

비스듬히 길게 늘어진 점 구름을 생각해 보자. 원래 좌표축 대신 점 구름의 긴 방향과 짧은 방향을 새 축으로 잡으면, 긴 축 하나만으로도 데이터의 큰 변화를 설명할 수 있다. PCA는 이 회전된 축을 찾고 정보가 적은 축을 버린다.

## 이론 (Theory)

$N$개 샘플을 행으로 가진 $X\in\mathbb{R}^{N\times d}$에서 각 열의 평균을 빼 $X_c$를 만든다. 단위벡터 $\mathbf{w}$ 방향의 투영 분산은

$$
\operatorname{Var}(X_c\mathbf{w})=\mathbf{w}^\top S\mathbf{w},
\qquad S=\frac{1}{N-1}X_c^\top X_c
$$

다. $\|\mathbf{w}\|_2=1$ 제약 아래 이를 최대화하면 공분산 행렬 $S$의 가장 큰 고유값에 대응하는 고유벡터를 얻는다. 중심화된 데이터의 SVD

$$
X_c=U\Sigma V^\top
$$

를 쓰면 $V$의 열이 주성분 방향이고, 설명 분산은 $\sigma_i^2/(N-1)$이다. 상위 $k$개 방향 $V_k$로 투영한 점수는 $Z=X_cV_k$다.

특징 스케일이 크게 다르면 분산이 큰 단위가 결과를 지배한다. 문제 의미에 따라 표준화 여부를 정해야 하며, 학습 데이터에서 구한 평균·스케일·주성분을 검증/테스트 데이터에 그대로 적용해 데이터 누출을 막는다.

## 구현 (Implementation)

```python
import numpy as np

X = np.array([[2.0, 0.0], [0.0, 1.0], [3.0, 1.0], [4.0, 2.0]])
mean = X.mean(axis=0)
X_centered = X - mean

_, singular_values, Vt = np.linalg.svd(X_centered, full_matrices=False)
k = 1
components = Vt[:k].T
Z = X_centered @ components
X_approx = Z @ components.T + mean

explained_variance = singular_values**2 / (len(X) - 1)
ratio = explained_variance / explained_variance.sum()
print(Z)
print(ratio)
```

실무에서는 학습/변환 API가 분리된 검증된 라이브러리를 사용해 전처리 상태를 파이프라인에 포함한다.

## 복잡도 (Complexity)

$N\ge d$인 조밀한 데이터의 전체 SVD 기반 PCA는 대략 `O(Nd^2)` 시간과 `O(Nd)` 저장 공간이 필요하다. $k\ll d$이면 randomized·incremental PCA로 상위 성분만 구해 비용을 줄일 수 있다.

## 응용 (Applications)

- 고차원 데이터의 2D·3D 시각화
- 압축, 잡음 제거, 중복 특징 축소
- 모델 학습 전 선형 전처리
- 공정·센서 데이터의 주요 변화 방향 탐색

## 흔한 오해 (Common Misunderstandings)

- PCA는 레이블을 사용하지 않으므로 분류에 중요한 저분산 방향을 버릴 수 있다.
- 주성분의 부호는 고유하지 않다. 같은 축의 반대 방향은 동일한 해석을 나타낸다.
- 중심화를 생략하면 원점과의 거리 때문에 의도와 다른 축을 얻을 수 있다.
- 설명 분산이 높다는 사실이 의미 있는 정보나 인과 관계를 보존한다는 뜻은 아니다.

## TMI

- PCA는 투영 분산 최대화와 제곱 재구성 오차 최소화라는 두 관점이 동치다.
- 주성분은 원래 특징의 선형 결합이라, 성능은 좋아져도 특징별 해석은 어려워질 수 있다.
- 희소 원-핫 데이터는 평균을 빼면 조밀해질 수 있어 Truncated SVD 같은 대안을 쓰기도 한다.

## 연습 / 확인 문제 (Exercises)

- 2차원 점을 직접 그려 첫 주성분 방향과 투영 결과를 비교하라.
- 중심화를 생략한 PCA와 포함한 PCA의 주성분을 비교하라.
- 누적 설명 분산이 90% 이상이 되는 최소 $k$를 선택하는 코드를 작성하라.

## 이어서 읽기 (Reading Path)

- 이전: [특이값 분해](SVD.md)
- 다음: 차원 축소 (예정 `Dimensionality-Reduction.md`, AI/Machine-Learning)
- 관련: [기댓값](../Probability-Statistics/Expectation.md)

## 참조 (References)

- [Math/Linear-Algebra/SVD.md](SVD.md)
- [Math/Probability-Statistics/Expectation.md](../Probability-Statistics/Expectation.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
