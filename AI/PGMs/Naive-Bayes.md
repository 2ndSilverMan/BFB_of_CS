# 나이브 베이즈 (Naive Bayes)

- Level: Intermediate
- Prerequisites: [Math/Probability-Statistics/Bayes-Theorem.md](../../Math/Probability-Statistics/Bayes-Theorem.md), [AI/Machine-Learning/Logistic-Regression.md](../Machine-Learning/Logistic-Regression.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

나이브 베이즈는 클래스가 주어지면 feature들이 서로 조건부 독립이라고 가정하는 확률 분류기다. 가정은 단순하지만, 텍스트 분류처럼 고차원 희소 feature에서 강력한 baseline이 된다.

## 직관 (Intuition)

문서가 스팸인지 판단할 때 각 단어의 등장 여부를 모두 복잡하게 연결해 모델링하면 어렵다. 나이브 베이즈는 “스팸 여부를 알면 단어들은 독립적으로 나타난다”고 단순화해 계산을 작게 만든다.

## 이론 (Theory)

클래스 $Y$와 feature $X_1,\dots,X_d$에 대해

$$
P(Y\mid X_1,\dots,X_d)\propto P(Y)\prod_{j=1}^{d}P(X_j\mid Y)
$$

로 분류한다. 이산 count feature에는 multinomial naive Bayes, binary feature에는 Bernoulli naive Bayes, 연속 feature에는 Gaussian naive Bayes를 사용할 수 있다.

확률이 0이 되는 문제를 피하려면 Laplace smoothing을 자주 사용한다.

$$
P(w\mid y)=\frac{count(w,y)+\alpha}{\sum_{w'}count(w',y)+\alpha |V|}
$$

```mermaid
flowchart LR
    Text["features"] --> Counts["class-conditional counts"]
    Counts --> Smooth["smoothing"]
    Smooth --> LogProb["log probabilities"]
    LogProb --> Class["argmax class"]
```

### 변형 선택

| 변형 | Feature | 사용 예 |
| --- | --- | --- |
| Multinomial NB | count/frequency | 문서 단어 count |
| Bernoulli NB | binary presence | 짧은 문서, 등장 여부 |
| Gaussian NB | continuous value | 단순 연속 feature |
| Complement NB | class complement count | 불균형 텍스트 |

텍스트에서는 multinomial NB가 강한 baseline이고, feature를 TF-IDF로 바꿀 때는 확률적 해석이 조금 약해질 수 있지만 실용적으로 잘 작동하기도 한다.

### 독립 가정과 결정 경계

단어들은 실제로 독립이 아니지만, log probability를 더하면 선형 score가 되어 고차원 희소 텍스트에서 강력하다. 독립 가정이 틀려도 argmax 분류가 괜찮을 수 있지만, posterior probability는 과신되는 경향이 있다.

### OOV와 vocabulary pruning

희귀 단어를 모두 vocabulary에 넣으면 noise와 메모리가 늘고, 너무 많이 제거하면 의미 단서를 잃는다. `<UNK>` 처리, min frequency, class별 informative token 검토가 필요하다.

## 구현 (Implementation)

로그 확률을 쓰면 underflow를 피할 수 있다.

```python
import math


def score(words, class_log_prior, word_log_probs):
    total = class_log_prior
    for w in words:
        total += word_log_probs.get(w, word_log_probs["<UNK>"])
    return total


spam = score(["free", "prize"], -0.7, {"free": -0.2, "prize": -0.4, "<UNK>": -3.0})
ham = score(["free", "prize"], -0.6, {"free": -1.5, "prize": -2.0, "<UNK>": -3.0})
print("spam" if spam > ham else "ham")
```

실무에서는 tokenization, vocabulary pruning, smoothing 값이 성능에 영향을 준다.

```python
def laplace(count, total, vocab_size, alpha=1.0):
    return (count + alpha) / (total + alpha * vocab_size)
```

## 복잡도 (Complexity)

학습은 feature count를 세면 되므로 데이터 크기에 거의 선형이다. 예측도 문서의 nonzero feature 수에 비례한다. 메모리는 클래스 수와 vocabulary 크기의 곱에 비례한다.

## 응용 (Applications)

- 스팸 필터링
- 감성 분석 baseline
- 문서 분류와 토픽 분류
- 확률 모델링 교육용 예시

## 흔한 오해 (Common Misunderstandings)

- feature 독립 가정이 현실에서 정확해야만 잘 작동하는 것은 아니다.
- 확률 calibration은 좋지 않을 수 있다. 분류는 잘해도 확률값은 과신할 수 있다.
- smoothing 없이 드문 단어를 처리하면 확률이 0이 되어 문제가 생긴다.
- feature engineering이 여전히 중요하다.

## TMI

- 텍스트에서는 단어들이 독립이 아니지만, log-count 기반 선형 결정 경계가 강력한 baseline을 만든다.
- 나이브 베이즈는 생성 모델이고 로지스틱 회귀는 판별 모델로 비교된다.
- Complement Naive Bayes는 불균형 텍스트 분류에서 도움이 될 수 있다.

## 연습 / 확인 문제 (Exercises)

- 나이브 베이즈의 조건부 독립 가정을 확률식으로 써라.
- Laplace smoothing이 없는 경우 어떤 단어가 문제를 만들 수 있는지 설명하라.
- 나이브 베이즈와 로지스틱 회귀의 차이를 생성/판별 관점에서 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [베이지안 네트워크](Bayesian-Networks.md)
- 다음: [HMM](HMM.md)

## 참조 (References)

- [Bayesian-Networks.md](Bayesian-Networks.md)
- [Math/Probability-Statistics/Bayes-Theorem.md](../../Math/Probability-Statistics/Bayes-Theorem.md)
- [AI/Machine-Learning/Logistic-Regression.md](../Machine-Learning/Logistic-Regression.md)
- [Reference/Books.md](../../Reference/Books.md)
