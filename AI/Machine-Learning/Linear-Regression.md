# 선형 회귀 (Linear Regression)

- Level: Intermediate
- Prerequisites: [Math/Linear-Algebra/Vectors.md](../../Math/Linear-Algebra/Vectors.md), [Math/Optimization/Gradient-Descent.md](../../Math/Optimization/Gradient-Descent.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

선형 회귀는 입력 특징의 **가중합**으로 연속적인 출력값을 예측하는 가장 기본적인 지도학습 모델이다. "공부 시간으로 점수를 예측"하듯, 입력과 출력 사이의 직선(고차원에서는 초평면) 관계를 학습한다.

## 직관 (Intuition)

산점도에 점들이 흩어져 있을 때, 그 점들을 가장 잘 지나는 직선 하나를 긋는 것이 선형 회귀다. "가장 잘"의 기준은 보통 예측값과 실제값의 차이(오차)를 제곱해 합한 것을 최소화하는 것이다.

## 이론 (Theory)

예측은 파라미터 $\theta$와 입력 $x$의 내적이다(편향은 $x_0 = 1$로 흡수).

$$\hat{y} = \theta^\top x = \theta_0 + \theta_1 x_1 + \dots + \theta_d x_d$$

손실은 평균제곱오차(MSE)다.

$$J(\theta) = \frac{1}{2m}\sum_{i=1}^{m}\left(\theta^\top x_i - y_i\right)^2$$

해를 구하는 두 방법:

- **정규 방정식(closed form)**: $\theta = (X^\top X)^{-1} X^\top y$. 단, $X^\top X$가 가역이고 수치적으로 안정적일 때 직접 쓸 수 있다.
- **경사 하강법**: $\theta \leftarrow \theta - \eta\,\nabla_\theta J(\theta)$ ([경사 하강법](../../Math/Optimization/Gradient-Descent.md) 참고)

특징 수 $d$가 작으면 정규 방정식이 간단하고, 매우 크면 경사 하강법이 효율적이다.

## 구현 (Implementation)

작은 예제에서는 정규 방정식과 같은 해를 주는 최소제곱 solver로 직선을 적합한다.

```python
import numpy as np

X = np.array([[1, 1], [1, 2], [1, 3], [1, 4]])   # 첫 열은 편향(1)
y = np.array([2, 4, 6, 8])                        # y = 2x

theta, *_ = np.linalg.lstsq(X, y, rcond=None)
print(theta)              # [~0, ~2]  ->  y_hat = 0 + 2*x
print(X @ theta)          # [2 4 6 8]
```

## 복잡도 (Complexity)

`m`은 표본 수, `d`는 특징 수다.

| 방법 | 시간 |
|---|---|
| 정규 방정식 | `O(m·d^2 + d^3)` (행렬 역연산) |
| 경사 하강법(반복 `T`회) | `O(T·m·d)` |

`d`가 크면 $d^3$의 역행렬 비용 때문에 경사 하강법이 유리하다.

## 응용 (Applications)

- 수요·가격·매출 예측
- 특징과 결과의 관계 해석(계수의 부호·크기)
- 더 복잡한 모델의 기준선(baseline)
- 다른 모델의 출력 보정

## 흔한 오해 (Common Misunderstandings)

- "선형"은 입력이 아니라 **파라미터**에 대한 선형이다. $x^2$ 같은 특징을 넣어 곡선도 적합할 수 있다(다항 회귀).
- MSE는 이상치(outlier)에 민감하다. 큰 오차가 제곱되어 과대 반영된다.
- 정규 방정식의 $X^\top X$가 비가역이면(특징이 중복·과다) 해가 불안정하다. 정규화가 필요하다.
- 상관관계를 인과로 해석하면 안 된다.

## TMI

- 최소제곱법은 19세기 초 가우스와 르장드르가 천체 궤도 예측에 사용하면서 정립됐다. 머신러닝보다 200년 앞선 기법이다.
- $X^\top X$의 역행렬을 직접 구하는 대신, 수치적으로 안정적인 QR 분해나 의사역행렬(`np.linalg.lstsq`)을 쓰는 것이 실무 권장 사항이다.

## 연습 / 확인 문제 (Exercises)

- 위 데이터에 이상치 $(1, 5) \to 100$을 추가하면 적합 직선이 어떻게 흔들리는지 관찰하라.
- MSE 손실 $J(\theta)$의 기울기 $\nabla_\theta J$를 직접 유도하라.
- 같은 데이터를 경사 하강법으로 학습해 정규 방정식 해와 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: 없음
- 다음: [로지스틱 회귀](Logistic-Regression.md)
- 관련: [경사 하강법](../../Math/Optimization/Gradient-Descent.md)

## 참조 (References)

- [Math/Linear-Algebra/Vectors.md](../../Math/Linear-Algebra/Vectors.md)
- [Math/Optimization/Gradient-Descent.md](../../Math/Optimization/Gradient-Descent.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
