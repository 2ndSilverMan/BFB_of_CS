# 손실 함수 (Loss Functions)

- Level: Intermediate
- Prerequisites: [AI/Deep-Learning/MLP.md](MLP.md), [Math/Probability-Statistics/MLE.md](../../Math/Probability-Statistics/MLE.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

손실 함수는 모델 예측과 목표의 불일치를 스칼라로 측정해 학습 방향을 정한다. 회귀에는 MSE·MAE, 분류에는 cross-entropy가 대표적이며 평가 지표와 같은 목적일 수도, 미분 가능한 surrogate일 수도 있다.

## 직관 (Intuition)

모델이 무엇을 잘해야 하는지 숫자로 정의한 채점표다. 채점표가 실제 목표와 어긋나면 optimizer는 손실을 잘 줄여도 원하는 행동을 배우지 못한다.

## 이론 (Theory)

$$\operatorname{MSE}=\frac1n\sum_i(\hat y_i-y_i)^2,qquad
\operatorname{MAE}=\frac1n\sum_i|\hat y_i-y_i|$$

다중분류 cross-entropy는 $L=-\sum_k y_k\log p_k$다. one-hot target이면 정답 클래스의 음의 로그확률이다. Gaussian noise MLE는 MSE, Laplace noise는 MAE와 연결된다.

class imbalance에서는 weighting·sampling·focal loss 등을 고려하되 precision/recall tradeoff와 calibration에 미치는 영향을 검증한다. loss reduction(sum/mean) 방식은 gradient scale을 바꾼다.

## 구현 (Implementation)

```python
import math


def mse(targets, predictions):
    return sum((y - p) ** 2 for y, p in zip(targets, predictions)) / len(targets)


def cross_entropy(class_index, probabilities):
    return -math.log(max(probabilities[class_index], 1e-12))
```

실전에는 log-softmax와 cross-entropy를 합친 안정적 API를 사용한다.

## 복잡도 (Complexity)

배치 원소·클래스 총수 $N$에 대해 계산과 gradient는 `O(N)`이다. 거대한 vocabulary에서는 sampled/approximate softmax로 비용을 줄이기도 한다.

## 응용 (Applications)

- 회귀·분류·랭킹 학습
- metric learning과 contrastive learning
- 생성 모델의 likelihood·reconstruction objective
- 다중 과제의 weighted objective

## 흔한 오해 (Common Misunderstandings)

- 훈련 loss가 낮다고 실제 비즈니스 지표가 반드시 높지는 않다.
- MSE는 이상치에 민감하고 MAE는 0에서 매끄럽지 않다.
- class weight는 데이터 자체의 평가 분포를 바꾸지는 않는다.
- 확률에 직접 log를 취하기보다 안정적인 logits API를 써야 한다.

## TMI

- Huber loss는 작은 오차에서 제곱, 큰 오차에서 선형으로 동작한다.
- label smoothing은 target을 완전한 one-hot에서 조금 완화한다.
- surrogate loss는 정확도처럼 미분 불가능한 목표를 간접 최적화한다.

## 연습 / 확인 문제 (Exercises)

- 같은 오차에 MSE와 MAE가 주는 penalty를 비교하라.
- cross-entropy와 MLE의 연결을 설명하라.
- 불균형 분류에서 loss와 평가 metric 조합을 설계하라.

## 이어서 읽기 (Reading Path)

- 이전: [역전파](Backpropagation.md)
- 다음: [정규화 층](Normalization-Layers.md)

## 참조 (References)

- [Math/Probability-Statistics/MLE.md](../../Math/Probability-Statistics/MLE.md)
- [Math/Probability-Statistics/Information-Theory.md](../../Math/Probability-Statistics/Information-Theory.md)
- [Reference/Books.md](../../Reference/Books.md)
