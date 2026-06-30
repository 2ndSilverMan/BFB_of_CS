# MDL: 최소 기술 길이 (Minimum Description Length)

- Level: Advanced
- Prerequisites: [Math/Probability-Statistics/Information-Theory.md](../../Math/Probability-Statistics/Information-Theory.md), [Generalization-Bounds.md](Generalization-Bounds.md), [Bias-Variance-Theory.md](Bias-Variance-Theory.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

MDL 원리는 좋은 모델이란 데이터와 모델 자체를 합쳐 가장 짧게 설명하는 모델이라는 관점이다. 단순한 모델은 모델 설명 길이가 짧고, 복잡한 모델은 데이터 적합이 좋을 수 있지만 모델 설명 길이가 길다. MDL은 이 둘의 균형을 정보 이론적으로 표현한다.

## 직관 (Intuition)

데이터를 친구에게 보내야 한다고 하자. 규칙이 단순하면 “이 규칙과 예외 몇 개”만 보내면 된다. 규칙이 너무 복잡해 데이터 자체를 외운 것과 다르지 않다면 설명 길이가 길어진다. 좋은 일반화는 짧고 의미 있는 압축과 관련된다.

## 이론 (Theory)

모델 $M$과 데이터 $D$에 대해 MDL은 대략

$$
L(M)+L(D\mid M)
$$

을 최소화한다. 여기서 $L(M)$은 모델을 설명하는 길이이고, $L(D\mid M)$은 모델이 주어졌을 때 데이터를 설명하는 길이다. 확률 모델에서는 음의 로그우도 $-\log P(D\mid M)$가 데이터 설명 길이와 연결된다.

따라서 MDL은 likelihood와 complexity penalty의 균형으로 볼 수 있다. AIC, BIC 같은 기준도 모델 적합도와 복잡도 penalty를 결합한다는 점에서 비슷한 정신을 공유한다.

### Two-part code와 refined MDL

가장 단순한 MDL은 모델 설명 길이와 데이터 설명 길이를 더하는 two-part code다. 먼저 모델을 보내고, 그 모델이 설명하지 못한 잔차나 예외를 보낸다. 더 정교한 MDL은 normalized maximum likelihood나 stochastic complexity처럼 모델 class 전체의 부호화 비용을 다룬다.

Two-part code는 직관이 좋지만, 실제 길이는 모델을 어떻게 부호화하는지에 의존한다. 그래서 MDL 분석에서는 code choice가 중요하다.

### Likelihood와 압축

확률 모델이 데이터에 높은 확률을 주면 $-\log P(D\mid M)$이 작아지고, 이는 짧은 코드 길이에 해당한다. 따라서 maximum likelihood는 데이터 설명 길이를 줄이는 과정으로 볼 수 있다. 하지만 likelihood만 줄이면 데이터 자체를 외우는 복잡한 모델이 선택될 수 있으므로 $L(M)$이 필요하다.

### Bayesian 관점과의 연결

Bayesian evidence는 likelihood를 prior로 평균낸다. MDL의 description length와 Bayesian의 negative log evidence는 모두 fit과 complexity를 함께 벌주는 효과가 있다. 다만 철학과 세부 formalism은 다르다.

Prior를 짧은 코드에 대응시키면, 단순한 모델에 더 짧은 설명을 주는 관점과 연결된다.

### 딥러닝에서의 압축 관점

딥러닝에서는 파라미터 수가 매우 커도 pruning, quantization, low-rank factorization, weight sharing으로 잘 압축되는 모델이 일반화가 좋다는 가설이 연구된다. 중요한 것은 raw parameter count보다 훈련 후 해가 얼마나 간결하게 기술될 수 있는가다.

## 구현 (Implementation)

단순한 scoring 함수는 음의 로그우도와 모델 복잡도 penalty를 더한다.

```python
def mdl_score(neg_log_likelihood, num_params, n, penalty="bic"):
    if penalty == "bic":
        import math
        return neg_log_likelihood + 0.5 * num_params * math.log(n)
    if penalty == "aic":
        return neg_log_likelihood + num_params
    raise ValueError(penalty)


print(round(mdl_score(120.0, num_params=5, n=1000), 3))
```

실제 MDL에서는 모델을 어떻게 부호화할지 정하는 세부 선택이 중요하다.

```python
def two_part_code_length(model_bits, residual_bits):
    return model_bits + residual_bits
```

좋은 모델은 잔차를 줄이지만, 잔차 감소보다 모델 설명 길이 증가가 더 크면 MDL 점수는 나빠질 수 있다.

## 복잡도 (Complexity)

MDL 점수 계산 자체는 단순할 수 있지만, 후보 모델 공간을 탐색하는 비용이 크다. 구조 학습, feature selection, clustering처럼 가능한 모델이 많으면 최적 MDL 모델 찾기가 어려워진다.

## 응용 (Applications)

- 모델 선택과 구조 학습
- 과적합 방지의 정보 이론적 해석
- 압축 기반 일반화 설명
- 통계 모델 비교

## 흔한 오해 (Common Misunderstandings)

- 가장 짧은 설명이 항상 사람이 이해하기 쉬운 설명은 아니다.
- MDL은 단순히 파라미터 수만 세는 방법이 아니다. 부호화 방식이 중요하다.
- 훈련 데이터를 가장 짧게 압축한다고 모든 테스트 분포에 강한 것은 아니다.
- MDL과 Bayesian evidence는 관련이 있지만 완전히 같은 개념은 아니다.

## TMI

- Kolmogorov complexity는 가장 짧은 프로그램 길이로 복잡도를 정의하지만 일반적으로 계산 불가능하다.
- MDL은 “압축할 수 있는 구조가 일반화 가능하다”는 강한 직관을 제공한다.
- 딥러닝에서는 explicit parameter count보다 weight compression, flat minima, description length 관점이 더 미묘하다.

## 연습 / 확인 문제 (Exercises)

- $L(M)$과 $L(D\mid M)$이 각각 과소적합/과적합과 어떻게 연결되는지 설명하라.
- 음의 로그우도가 코드 길이와 연결되는 이유를 정보 이론 관점에서 말하라.
- BIC penalty가 표본 수 $n$에 따라 커지는 이유를 해석하라.

## 이어서 읽기 (Reading Path)

- 이전: [멀티암드 밴딧](Multi-Armed-Bandit.md)
- 다음: [상호 정보량과 학습](Mutual-Information.md)

## 참조 (References)

- [Math/Probability-Statistics/Information-Theory.md](../../Math/Probability-Statistics/Information-Theory.md)
- [Generalization-Bounds.md](Generalization-Bounds.md)
- [Bias-Variance-Theory.md](Bias-Variance-Theory.md)
- [Reference/Books.md](../../Reference/Books.md)
