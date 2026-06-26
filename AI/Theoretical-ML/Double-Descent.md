# 이중 강하 현상 (Double Descent)

- Level: Advanced
- Prerequisites: [Generalization-Bounds.md](Generalization-Bounds.md), [AI/Machine-Learning/Bias-Variance.md](../Machine-Learning/Bias-Variance.md), [AI/Machine-Learning/Regularization.md](../Machine-Learning/Regularization.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

Double descent는 모델 복잡도가 증가할 때 테스트 오차가 한 번 내려갔다가 보간(interpolation) 임계점 근처에서 치솟고, 그 이후 과매개변수 영역에서 다시 내려가는 현상이다. 고전적인 U자형 bias-variance 곡선을 현대 대형 모델 스케일링에서 확장해 보는 관점이다.

## 직관 (Intuition)

작은 모델은 너무 단순해서 underfitting한다. 중간 크기의 모델은 훈련 데이터를 겨우 외울 수 있는 경계에 있어 잡음까지 불안정하게 맞추며 테스트 오차가 커질 수 있다. 더 큰 모델은 해가 많아지고, 최적화 알고리즘의 암묵적 선호가 더 매끄럽거나 낮은 norm의 해를 선택하면서 다시 일반화가 좋아질 수 있다.

## 이론 (Theory)

고전적 bias-variance 관점에서는 모델 복잡도가 커질수록 bias는 줄고 variance는 늘어 U자형 테스트 오차가 나타난다. 그러나 파라미터 수가 표본 수를 넘는 overparameterized 영역에서는 훈련 오차가 0인 해가 많아지고, 그중 어떤 해를 선택하는지가 중요해진다.

선형 회귀의 minimum-norm interpolator, kernel ridgeless regression, 일부 random feature 모델에서는 double descent가 비교적 명확히 분석된다. 일반화는 단순히 파라미터 수가 아니라 데이터 구조, 노이즈, feature spectrum, 최적화 알고리즘의 implicit bias, regularization에 좌우된다.

현대 딥러닝에서 double descent는 모델 크기뿐 아니라 학습 epoch 수, 데이터 크기, regularization 강도에 대해서도 관찰될 수 있다. 다만 모든 문제에서 뚜렷하게 나타나는 법칙은 아니며, 실험 조건에 민감하다.

## 구현 (Implementation)

다항 회귀의 차수를 바꾸며 train/test MSE를 그리면 작은 예제로 double descent와 비슷한 패턴을 관찰할 수 있다.

```python
import numpy as np


def mse(y, pred):
    return np.mean((y - pred) ** 2)


rng = np.random.default_rng(0)
x_train = np.linspace(-1, 1, 25)
y_train = np.sin(3 * x_train) + 0.2 * rng.normal(size=len(x_train))
x_test = np.linspace(-1, 1, 200)
y_test = np.sin(3 * x_test)

for degree in [1, 3, 8, 20, 35]:
    coef = np.polyfit(x_train, y_train, degree)
    train_error = mse(y_train, np.polyval(coef, x_train))
    test_error = mse(y_test, np.polyval(coef, x_test))
    print(degree, round(train_error, 4), round(test_error, 4))
```

수치적으로 고차 다항식은 불안정할 수 있으므로 실제 분석에서는 정규화, orthogonal basis, 반복 평균을 함께 사용한다.

## 복잡도 (Complexity)

Double descent를 실험적으로 확인하려면 모델 크기나 학습 시간을 여러 단계로 sweep해야 하므로 기본 학습 비용의 배수가 든다. 이론 분석은 feature spectrum과 noise model에 의존해 문제별로 복잡해진다.

## 응용 (Applications)

- 대형 모델 scaling behavior 해석
- overparameterization이 항상 해롭지 않은 이유 설명
- regularization과 early stopping의 역할 분석
- benchmark에서 모델 크기 sweep을 설계할 때 참고

## 흔한 오해 (Common Misunderstandings)

- 파라미터가 데이터보다 많으면 반드시 과적합한다는 주장은 현대 모델에서는 너무 단순하다.
- Double descent가 regularization이 필요 없다는 뜻은 아니다.
- 현상이 관찰된다고 해서 원인이 하나로 고정되는 것은 아니다.
- 테스트 오차 peak가 항상 정확히 파라미터 수와 표본 수가 같은 지점에 생기지는 않는다.

## TMI

- benign overfitting은 훈련 데이터를 보간하면서도 테스트 오차가 낮을 수 있는 조건을 연구한다.
- epoch-wise double descent는 학습 시간이 길어지며 훈련 오차가 0에 가까워지는 주변에서 테스트 오차가 다시 변하는 현상이다.
- 딥러닝에서 “큰 모델이 더 잘 일반화한다”는 경험 법칙은 데이터 품질과 최적화 안정성이 받쳐줄 때 훨씬 강하다.

## 연습 / 확인 문제 (Exercises)

- 고전적 bias-variance 곡선과 double descent 곡선을 한 문단으로 비교하라.
- 보간 임계점 근처에서 variance가 커질 수 있는 이유를 설명하라.
- ridge regularization을 추가하면 double descent peak가 어떻게 변할지 예측하라.

## 이어서 읽기 (Reading Path)

- 이전: [일반화 경계](Generalization-Bounds.md)
- 다음: [경사 하강법 수렴 분석](GD-Convergence.md)
- 관련: [볼록 최적화와 학습](Convex-Learning.md)

## 참조 (References)

- [Generalization-Bounds.md](Generalization-Bounds.md)
- [AI/Machine-Learning/Bias-Variance.md](../Machine-Learning/Bias-Variance.md)
- [AI/Machine-Learning/Regularization.md](../Machine-Learning/Regularization.md)
- [Reference/Books.md](../../Reference/Books.md)
