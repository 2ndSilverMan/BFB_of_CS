# 편향-분산 트레이드오프 이론 (Bias-Variance Theory)

- Level: Advanced
- Prerequisites: [AI/Machine-Learning/Bias-Variance.md](../Machine-Learning/Bias-Variance.md), [Generalization-Bounds.md](Generalization-Bounds.md), [Math/Probability-Statistics/Expectation.md](../../Math/Probability-Statistics/Expectation.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

편향-분산 분해는 예측 오차를 모델의 체계적 오류인 편향, 데이터 표본 변화에 따른 민감도인 분산, 줄일 수 없는 잡음으로 나누어 설명한다. 이론적으로는 모델 복잡도와 일반화 오차 사이의 고전적 관계를 이해하는 도구다.

## 직관 (Intuition)

너무 단순한 모델은 항상 비슷하게 틀린다. 이것이 높은 편향이다. 너무 유연한 모델은 훈련 데이터가 조금만 바뀌어도 크게 달라진다. 이것이 높은 분산이다. 좋은 모델은 문제 구조를 충분히 표현하면서도 표본 잡음에는 과하게 흔들리지 않는다.

## 이론 (Theory)

회귀에서 $Y=f^\*(X)+\epsilon$, $E[\epsilon]=0$, $Var(\epsilon)=\sigma^2$라고 하자. 학습 데이터 $S$로 얻은 예측기를 $\hat f_S$라고 하면 한 점 $x$에서 평균제곱오차는

$$
E_S[(\hat f_S(x)-Y)^2]
= Bias(x)^2 + Var(x) + \sigma^2
$$

로 분해된다. 여기서

$$
Bias(x)=E_S[\hat f_S(x)]-f^\*(x)
$$

이고

$$
Var(x)=E_S[(\hat f_S(x)-E_S[\hat f_S(x)])^2]
$$

이다.

이 분해는 모델 복잡도를 올리면 보통 bias는 줄고 variance는 늘 수 있음을 보여준다. 그러나 현대 과매개변수 모델에서는 double descent처럼 고전적 U자 곡선만으로 설명되지 않는 현상도 나타난다.

## 구현 (Implementation)

여러 bootstrap 표본으로 모델 예측의 분산을 추정하는 식의 진단을 할 수 있다.

```python
def mean(values):
    return sum(values) / len(values)


def variance(values):
    m = mean(values)
    return sum((v - m) ** 2 for v in values) / len(values)


predictions_at_x = [1.2, 1.4, 0.9, 1.1, 1.5]
true_f_x = 1.0

bias = mean(predictions_at_x) - true_f_x
var = variance(predictions_at_x)
print(round(bias ** 2, 3), round(var, 3))
```

실제 문제에서는 $f^\*$를 모르므로 bias를 직접 측정하기 어렵고, synthetic data나 validation behavior로 간접 분석한다.

## 복잡도 (Complexity)

편향-분산 분석은 여러 학습 반복이나 resampling을 요구할 수 있다. Bootstrap 기반 추정은 기본 학습 비용에 반복 횟수를 곱한 비용이 든다.

## 응용 (Applications)

- 모델 복잡도 선택
- 정규화와 early stopping 해석
- learning curve 분석
- double descent와 현대 일반화 현상 비교

## 흔한 오해 (Common Misunderstandings)

- 편향이 사회적 bias를 의미하는 것은 아니다. 여기서는 통계적 체계 오류다.
- 분산이 높다는 말은 데이터 분할에 민감하다는 뜻이지, 예측값의 관측 잡음만 뜻하지 않는다.
- 모든 손실과 문제에서 단순한 세 항 분해가 그대로 성립하는 것은 아니다.
- double descent는 bias-variance 관점을 폐기한다기보다 확장과 재해석을 요구한다.

## TMI

- bagging은 여러 모델 평균으로 variance를 줄이는 대표적 방법이다.
- ridge regression은 bias를 조금 늘려 variance를 크게 줄일 수 있다.
- “작은 모델 vs 큰 모델”보다 데이터 구조, regularization, optimizer bias가 함께 중요하다.

## 연습 / 확인 문제 (Exercises)

- MSE 분해식을 전개해 bias, variance, noise 항을 유도하라.
- high bias와 high variance의 learning curve 패턴을 비교하라.
- bagging이 variance를 줄이는 이유를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [No-Free-Lunch](No-Free-Lunch.md)
- 다음: [Rademacher 복잡도](Rademacher-Complexity.md)

## 참조 (References)

- [AI/Machine-Learning/Bias-Variance.md](../Machine-Learning/Bias-Variance.md)
- [Generalization-Bounds.md](Generalization-Bounds.md)
- [Math/Probability-Statistics/Expectation.md](../../Math/Probability-Statistics/Expectation.md)
- [Reference/Books.md](../../Reference/Books.md)
