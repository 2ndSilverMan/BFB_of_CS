# 선형 회귀 (Linear Regression)

- Level: Intermediate
- Prerequisites: [Math/Linear-Algebra/Vectors.md](../../Math/Linear-Algebra/Vectors.md), [Math/Optimization/Gradient-Descent.md](../../Math/Optimization/Gradient-Descent.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

선형 회귀는 입력 특징의 **가중합**으로 연속적인 출력값을 예측하는 가장 기본적인 지도학습 모델이다. "공부 시간으로 점수를 예측"하듯, 입력과 출력 사이의 직선(고차원에서는 초평면) 관계를 학습한다.

## 직관 (Intuition)

산점도에 점들이 흩어져 있을 때, 그 점들을 가장 잘 지나는 직선 하나를 긋는 것이 선형 회귀다. "가장 잘"의 기준은 보통 예측값과 실제값의 차이(오차)를 제곱해 합한 것을 최소화하는 것이다.

```mermaid
flowchart LR
    X["특징 행렬 X"] --> MODEL["예측 y_hat = X theta"]
    MODEL --> RES["잔차 r = y_hat - y"]
    RES --> LOSS["MSE 최소화"]
    LOSS --> THETA["theta 학습"]
    THETA --> EVAL["검증 데이터로 일반화 평가"]
```

## 이론 (Theory)

예측은 파라미터 $\theta$와 입력 $x$의 내적이다(편향은 $x_0 = 1$로 흡수).

$$\hat{y} = \theta^\top x = \theta_0 + \theta_1 x_1 + \dots + \theta_d x_d$$

손실은 평균제곱오차(MSE)다.

$$J(\theta) = \frac{1}{2m}\sum_{i=1}^{m}\left(\theta^\top x_i - y_i\right)^2$$

해를 구하는 두 방법:

- **정규 방정식(closed form)**: $\theta = (X^\top X)^{-1} X^\top y$. 단, $X^\top X$가 가역이고 수치적으로 안정적일 때 직접 쓸 수 있다.
- **경사 하강법**: $\theta \leftarrow \theta - \eta\,\nabla_\theta J(\theta)$ ([경사 하강법](../../Math/Optimization/Gradient-Descent.md) 참고)

특징 수 $d$가 작으면 정규 방정식이 간단하고, 매우 크면 경사 하강법이 효율적이다.

### 행렬 형태와 해석

표본을 행으로 쌓으면 $X\in\mathbb{R}^{m\times(d+1)}$, 파라미터는 $\theta\in\mathbb{R}^{d+1}$, 예측은 $\hat y=X\theta$다. 잔차 벡터는 $r=X\theta-y$이고 손실은

$$
J(\theta)=\frac{1}{2m}\|X\theta-y\|_2^2
$$

로 쓸 수 있다. 이때 gradient는

$$
\nabla_\theta J=\frac{1}{m}X^\top(X\theta-y)
$$

다. $X^\top X$가 잘 조건화되어 있으면 최소제곱 해가 안정적이지만, 특징이 거의 중복되면 계수가 크게 흔들릴 수 있다.

### 계수 해석의 조건

선형 회귀 계수 $\theta_j$는 다른 특징을 고정했을 때 $x_j$가 1 증가하면 예측이 얼마나 변하는지를 뜻한다. 하지만 특징 간 상관이 크거나 누락 변수가 있으면 계수 해석이 불안정하고 인과 해석도 불가능하다. 예측 모델과 설명 모델의 목표를 분리해야 한다.

### 진단 체크리스트

| 점검 | 이유 |
|---|---|
| 잔차 vs 예측값 플롯 | 비선형 패턴과 이분산성 탐지 |
| 이상치 영향 | MSE는 큰 오차를 제곱해 민감 |
| feature scaling | GD 수렴 속도 개선 |
| train/validation 성능 | 과적합/과소적합 구분 |
| 조건수 | 다중공선성과 수치 불안정성 확인 |

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

잔차와 조건수를 함께 확인하면 해의 신뢰도를 더 잘 볼 수 있다.

```python
pred = X @ theta
residual = y - pred
print(np.linalg.norm(residual))
print(np.linalg.cond(X))
```

## 복잡도 (Complexity)

`m`은 표본 수, `d`는 특징 수다.

| 방법 | 시간 |
|---|---|
| 정규 방정식 | `O(m·d^2 + d^3)` (행렬 역연산) |
| 경사 하강법(반복 `T`회) | `O(T·m·d)` |

`d`가 크면 $d^3$의 역행렬 비용 때문에 경사 하강법이 유리하다.

실무에서는 역행렬을 명시적으로 만들기보다 QR/SVD 기반 `lstsq`를 쓴다. 같은 데이터에서 여러 target을 학습할 때는 분해를 재사용할 수 있어 비용 구조가 달라진다.

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
- 높은 $R^2$가 배포 성능을 보장하지 않는다. 시간 누출, 중복 데이터, 분포 이동을 별도로 점검해야 한다.
- 특징 스케일이 계수 크기에 영향을 주므로, 계수 크기만 보고 중요도를 비교하면 위험하다.

## TMI

- 최소제곱법은 19세기 초 가우스와 르장드르가 천체 궤도 예측에 사용하면서 정립됐다. 머신러닝보다 200년 앞선 기법이다.
- $X^\top X$의 역행렬을 직접 구하는 대신, 수치적으로 안정적인 QR 분해나 의사역행렬(`np.linalg.lstsq`)을 쓰는 것이 실무 권장 사항이다.

## 연습 / 확인 문제 (Exercises)

- 위 데이터에 이상치 $(1, 5) \to 100$을 추가하면 적합 직선이 어떻게 흔들리는지 관찰하라.
- MSE 손실 $J(\theta)$의 기울기 $\nabla_\theta J$를 직접 유도하라.
- 같은 데이터를 경사 하강법으로 학습해 정규 방정식 해와 비교하라.
- 두 특징이 거의 같은 데이터를 만들고 조건수와 계수 안정성을 관찰하라.
- 잔차 플롯에서 U자 패턴이 보일 때 어떤 feature engineering을 시도할 수 있는지 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: 없음
- 다음: [로지스틱 회귀](Logistic-Regression.md)
- 관련: [경사 하강법](../../Math/Optimization/Gradient-Descent.md)

## 참조 (References)

- [Math/Linear-Algebra/Vectors.md](../../Math/Linear-Algebra/Vectors.md)
- [Math/Optimization/Gradient-Descent.md](../../Math/Optimization/Gradient-Descent.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
