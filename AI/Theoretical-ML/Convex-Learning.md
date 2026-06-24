# 볼록 최적화와 학습 (Convex Learning)

- Level: Advanced
- Prerequisites: [Math/Optimization/Convex-Optimization.md](../../Math/Optimization/Convex-Optimization.md), [GD-Convergence.md](GD-Convergence.md), [AI/Machine-Learning/Logistic-Regression.md](../Machine-Learning/Logistic-Regression.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

볼록 학습은 손실 함수와 정규화 항이 볼록인 문제를 학습 이론과 최적화 관점에서 분석하는 분야다. 볼록 문제에서는 local minimum이 global minimum이므로, 최적화와 통계적 분석을 비교적 깔끔하게 연결할 수 있다.

## 직관 (Intuition)

울퉁불퉁한 산악 지형에서는 낮은 골짜기에 빠져도 전체 최저점인지 알기 어렵다. 볼록 지형은 하나의 큰 그릇처럼 생겨 있어 아래로 내려가면 전역 최저점에 가까워진다. 그래서 알고리즘 분석과 일반화 분석이 훨씬 투명해진다.

## 이론 (Theory)

전형적인 정규화 경험 위험 최소화는 다음 형태다.

$$
\min_w \frac{1}{n}\sum_{i=1}^{n}\ell(w;x_i,y_i)+\lambda R(w)
$$

손실 $\ell$과 정규화 $R$이 볼록이면 전체 목적 함수도 볼록이다. 로지스틱 회귀, SVM hinge loss, ridge/lasso regression은 대표적인 볼록 학습 문제다.

볼록성은 최적화 보장을 준다. $L$-smooth convex 함수에서는 gradient descent가 $O(1/T)$의 function gap 수렴률을 갖고, strong convexity가 있으면 선형 수렴이 가능하다. 통계적으로는 stability, Rademacher complexity, regularization path 분석이 상대적으로 잘 정리된다.

## 구현 (Implementation)

L2 정규화가 있는 로지스틱 회귀 목적의 gradient 형태는 다음처럼 계산할 수 있다.

```python
import math


def sigmoid(z):
    return 1 / (1 + math.exp(-z))


def logistic_grad(w, x, y, l2):
    p = sigmoid(sum(wi * xi for wi, xi in zip(w, x)))
    return [(p - y) * xi + l2 * wi for wi, xi in zip(w, x)]


w = [0.1, -0.2]
x = [1.0, 3.0]
y = 1
print(logistic_grad(w, x, y, l2=0.01))
```

문제는 볼록이어도 feature scaling, 조건수, 학습률 선택은 여전히 중요하다.

## 복잡도 (Complexity)

볼록 학습의 반복 복잡도는 smoothness, strong convexity, 조건수, 정확도 $\epsilon$에 따라 달라진다. 대규모 데이터에서는 full gradient보다 SGD, variance reduction, coordinate descent가 자주 쓰인다.

## 응용 (Applications)

- 로지스틱 회귀와 선형 SVM
- convex surrogate loss 설계
- 정규화 경로와 sparse 모델
- 비볼록 딥러닝 분석의 기준점

## 흔한 오해 (Common Misunderstandings)

- 볼록이면 자동으로 빠르다는 뜻은 아니다. 조건수가 나쁘면 느릴 수 있다.
- 볼록 최적해가 실제 문제의 최고 예측 성능을 보장하지는 않는다.
- 딥러닝이 비볼록이라고 해서 볼록 이론이 쓸모없는 것은 아니다.
- convex surrogate가 원래 평가 지표와 완전히 같은 것은 아니다.

## TMI

- hinge loss는 0-1 loss의 볼록 대리 손실이다.
- L1 정규화는 sparse 해를 유도하지만 목적 함수가 미분 가능하지 않을 수 있다.
- online convex optimization은 regret minimization과 자연스럽게 연결된다.

## 연습 / 확인 문제 (Exercises)

- 로지스틱 손실이 볼록인 이유를 Hessian 관점에서 설명하라.
- L2 정규화가 strong convexity를 제공하는 조건을 설명하라.
- 0-1 loss 대신 convex surrogate를 쓰는 이유를 말하라.

## 이어서 읽기 (Reading Path)

- 이전: [Double Descent](Double-Descent.md)
- 다음: [비볼록 수렴](Non-Convex-Convergence.md)

## 참조 (References)

- [Math/Optimization/Convex-Optimization.md](../../Math/Optimization/Convex-Optimization.md)
- [GD-Convergence.md](GD-Convergence.md)
- [AI/Machine-Learning/Logistic-Regression.md](../Machine-Learning/Logistic-Regression.md)
- [Reference/Books.md](../../Reference/Books.md)
