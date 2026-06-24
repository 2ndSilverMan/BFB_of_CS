# 최대 우도 추정 (Maximum Likelihood Estimation)

- Level: Intermediate
- Prerequisites: [Math/Probability-Statistics/Distributions.md](Distributions.md), [Math/Calculus/Differentiation.md](../Calculus/Differentiation.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

최대 우도 추정(MLE)은 관측한 데이터를 가장 그럴듯하게 만드는 모델 매개변수를 선택한다. 확률 모형 $p(x\mid\theta)$와 데이터 $D=\{x_i\}_{i=1}^n$에 대해 우도를 최대화한다.

$$
\hat\theta_{\text{MLE}}=\arg\max_\theta\prod_{i=1}^n p(x_i\mid\theta)
$$

## 직관 (Intuition)

동전을 여러 번 던져 앞면이 70% 나왔다면, 관측 결과를 가장 잘 설명하는 앞면 확률은 대략 0.7이다. MLE는 가능한 매개변수마다 "이 데이터가 나올 가능성"을 비교해 가장 큰 값을 고른다.

## 이론 (Theory)

독립 표본에서는 우도가 확률의 곱이다. 수치 안정성과 미분 편의를 위해 로그우도

$$
\ell(\theta)=\sum_{i=1}^n\log p(x_i\mid\theta)
$$

를 최대화한다. 로그는 단조 증가하므로 최적점은 같고 곱이 합으로 바뀐다. Bernoulli 데이터 $x_i\in\{0,1\}$의 경우

$$
\ell(p)=\sum_i x_i\log p+(1-x_i)\log(1-p)
$$

이고 미분하면 $\hat p=\frac{1}{n}\sum_i x_i$를 얻는다. 음의 로그우도는 머신러닝 손실로 자주 쓰이며, 분류의 cross-entropy와 회귀의 제곱오차도 특정 확률 가정의 MLE로 해석할 수 있다.

## 구현 (Implementation)

```python
import math


def bernoulli_mle(samples):
    return sum(samples) / len(samples)


def log_likelihood(samples, p):
    return sum(x * math.log(p) + (1 - x) * math.log(1 - p) for x in samples)


data = [1, 0, 1, 1, 0, 1, 1]
p_hat = bernoulli_mle(data)
print(p_hat)
print(log_likelihood(data, p_hat))
```

복잡한 모델은 닫힌 해가 없어 gradient descent 같은 수치 최적화를 사용한다.

## 복잡도 (Complexity)

한 번의 로그우도 평가는 표본 수 $n$에 대해 보통 `O(n)`이다. 반복 최적화는 반복 횟수 $T$에 대해 `O(Tn)`이 기본이며, 미니배치로 한 단계 비용을 줄인다.

## 응용 (Applications)

- 확률분포 매개변수 추정
- 선형·로지스틱 회귀 학습
- 혼합모형과 잠재변수 모델
- 신경망의 cross-entropy와 Gaussian 음의 로그우도

## 흔한 오해 (Common Misunderstandings)

- 우도는 매개변수의 확률분포가 아니다. 데이터를 고정하고 매개변수의 함수로 본 값이다.
- MLE가 유한 표본에서 항상 불편추정량인 것은 아니다.
- 높은 훈련 우도가 좋은 일반화를 자동으로 보장하지 않는다.
- 로그우도 최대화는 확률 최대화와 최적점은 같지만 계산 안정성은 훨씬 좋다.

## TMI

- MAP 추정은 로그우도에 로그 사전확률을 더하며, 정규화 관점에서 규제와 연결된다.
- Gaussian 잡음을 가정한 선형 회귀의 MLE는 제곱오차 최소화와 같다.
- 혼합모형에서는 직접 최적화 대신 EM 알고리즘을 자주 사용한다.

## 연습 / 확인 문제 (Exercises)

- Bernoulli 로그우도를 미분해 표본평균이 MLE임을 유도하라.
- 데이터에 성공 하나를 추가했을 때 $\hat p$가 어떻게 변하는지 계산하라.
- Gaussian 평균의 MLE가 표본평균임을 유도하라.

## 이어서 읽기 (Reading Path)

- 이전: [베이즈 정리](Bayes-Theorem.md)
- 다음: [중심 극한 정리](CLT.md)
- 관련: [경사 하강법](../Optimization/Gradient-Descent.md)

## 참조 (References)

- [Math/Probability-Statistics/Distributions.md](Distributions.md)
- [Math/Calculus/Differentiation.md](../Calculus/Differentiation.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
