# 행렬식 (Determinant)

- Level: Intermediate
- Prerequisites: [Math/Linear-Algebra/Matrices.md](Matrices.md), [Math/Linear-Algebra/Linear-Systems.md](Linear-Systems.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

행렬식은 정사각 행렬에 대응하는 스칼라로, 선형 변환이 부피를 얼마나 늘리거나 줄이는지를 나타낸다. 0이면 변환이 차원을 무너뜨려 역행렬이 없음을 뜻한다.

## 직관 (Intuition)

행렬을 "공간을 늘리고 비트는 변환"으로 보면, 행렬식은 그 변환이 단위 부피(정사각형/정육면체)를 몇 배로 만드는가다. 부호는 방향(반전 여부)을 담는다. 행렬식이 0이라는 것은 변환이 공간을 더 낮은 차원으로 납작하게 눌러, 정보를 잃고 되돌릴 수 없다는 신호다.

## 이론 (Theory)

$2\times2$ 행렬 $\begin{pmatrix}a&b\\c&d\end{pmatrix}$의 행렬식은 $ad-bc$다. 일반적으로 라플라스 전개(여인수)나 치환의 부호 합(라이프니츠 공식)으로 정의된다.

핵심 성질:
- $\det(AB)=\det(A)\det(B)$, $\det(A^\top)=\det(A)$.
- 행 교환은 부호를 바꾸고, 한 행에 스칼라를 곱하면 그만큼 곱해진다.
- $A$가 가역 $\iff \det(A)\ne 0$, 이때 $\det(A^{-1})=1/\det(A)$.
- 고윳값의 곱이 행렬식과 같다.

기하적으로 $|\det|$는 열벡터가 만드는 평행육면체의 부피다. 크라메르 공식은 행렬식으로 선형 시스템 해를 표현한다(이론적, 비효율적).

## 구현 (Implementation)

```python
def determinant_lu(A):
    import numpy as np
    from scipy.linalg import lu
    P, L, U = lu(A)
    sign = np.linalg.det(P)        # 행 교환 부호
    diag = 1.0
    for i in range(len(U)):
        diag *= U[i][i]            # 삼각행렬 대각의 곱
    return sign * diag
```

## 복잡도 (Complexity)

여인수 전개로 직접 계산하면 `O(n!)`로 폭발한다. 실무에서는 LU 분해로 삼각화한 뒤 대각 원소를 곱해 `O(n^3)`에 구한다. 큰 행렬에서는 행렬식 자체가 오버플로/언더플로하기 쉬워, 로그 행렬식(log-determinant)을 쓰는 경우가 많다.

## 응용 (Applications)

- 역행렬 존재·선형 독립 판정
- 변수 변환의 야코비안(다변수 적분)
- 고윳값·특성다항식 $\det(A-\lambda I)=0$
- 다변량 정규분포의 정규화 상수(공분산 행렬식)

## 흔한 오해 (Common Misunderstandings)

- 행렬식이 작다고 "거의 특이"인 것은 아니다(스케일에 민감). 조건수가 더 신뢰할 척도다.
- 행렬식은 정사각 행렬에만 정의된다.
- $\det(A+B)\ne\det(A)+\det(B)$ 일반적으로.
- 큰 행렬에서 행렬식을 그대로 다루면 수치적으로 위험하다(로그 사용).

## TMI

- 행렬식은 행렬 개념보다 먼저 등장했다 — 선형 시스템 풀이(크라메르, 18세기)에서 비롯됐다.
- 다변량 가우시안의 밀도에 공분산 행렬식이 정규화 상수로 들어가, ML에서 log-det이 자주 등장한다.
- 야코비안 행렬식이 0이면 그 점에서 변수 변환이 국소적으로 가역이 아니다.

## 연습 / 확인 문제 (Exercises)

- $3\times3$ 행렬의 행렬식을 여인수 전개로 구하라.
- 두 행을 교환하면 부호가 바뀜을 $2\times2$로 확인하라.
- $\det(A)=0$인 행렬을 만들고 열벡터가 선형 종속임을 보여라.

## 이어서 읽기 (Reading Path)

- 이전: [행렬](Matrices.md)
- 다음: [고윳값과 고유벡터](Eigenvalues.md), [Math/Calculus/Multivariable-Integration.md](../Calculus/Multivariable-Integration.md)

## 참조 (References)

- [Math/Linear-Algebra/Eigenvalues.md](Eigenvalues.md)
- [Math/Linear-Algebra/Linear-Systems.md](Linear-Systems.md)
- [Reference/Books.md](../../Reference/Books.md)
