# 상호 정보량과 학습 (Mutual Information and Learning)

- Level: Advanced
- Prerequisites: [Math/Probability-Statistics/Information-Theory.md](../../Math/Probability-Statistics/Information-Theory.md), [MDL.md](MDL.md), [Generalization-Bounds.md](Generalization-Bounds.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

상호 정보량은 두 확률 변수 사이에 공유되는 정보의 양을 측정한다. 학습 이론에서는 표현이 라벨에 대해 얼마나 정보를 담는지, 학습 알고리즘의 출력이 훈련 데이터에 얼마나 의존하는지, 일반화와 압축을 어떻게 연결할지 분석하는 데 사용된다.

## 직관 (Intuition)

어떤 표현 $Z$가 입력 $X$의 모든 세부사항을 외우면 정보량은 크지만 일반화에 불필요한 잡음도 담을 수 있다. 반대로 $Y$를 예측하는 데 필요한 정보만 간결하게 담으면 더 좋은 표현일 수 있다. 상호 정보량은 이 “얼마나 공유하는가”를 수치화한다.

## 이론 (Theory)

상호 정보량은

$$
I(X;Y)=E\left[\log\frac{p(X,Y)}{p(X)p(Y)}\right]
$$

로 정의한다. $X$와 $Y$가 독립이면 $I(X;Y)=0$이다.

표현 학습에서는 information bottleneck 원리가 자주 등장한다.

$$
\min I(X;Z)-\beta I(Z;Y)
$$

이는 입력 정보는 압축하면서 라벨 관련 정보는 보존하려는 목적이다. 일반화 분석에서는 학습 알고리즘 출력 $W$와 훈련 데이터 $S$의 상호 정보량 $I(W;S)$가 작으면 일반화 gap을 제어할 수 있다는 형태의 경계도 연구된다.

### 데이터 처리 부등식

데이터 처리 부등식은 $X\to Z\to T$처럼 후처리된 변수 $T$가 원래 표현 $Z$보다 $X$에 대한 정보를 더 많이 가질 수 없다는 원리다.

$$
I(X;T)\le I(X;Z)
$$

표현 학습에서는 layer를 거치며 어떤 정보가 보존되고 어떤 정보가 버려지는지 해석할 때 이 원리가 자주 쓰인다. 단, deterministic neural network와 연속 변수에서는 정보량이 무한대가 되거나 측정이 민감해질 수 있다.

### Information bottleneck의 tradeoff

$I(X;Z)$를 줄이면 입력의 불필요한 세부사항을 버리는 압축이 되고, $I(Z;Y)$를 키우면 라벨 예측에 필요한 정보가 보존된다. $\beta$는 이 둘의 균형을 조절한다.

하지만 실제 딥러닝에서 bottleneck을 직접 최적화하려면 상호 정보량 추정이 어렵다. Variational approximation, noise injection, contrastive bound 같은 우회가 필요하다.

### 알고리즘 안정성과 정보량

학습된 가중치 $W$가 훈련 데이터 $S$에 너무 많은 정보를 담으면 특정 샘플을 외웠을 가능성이 커진다. $I(W;S)$ 기반 일반화 경계는 학습 알고리즘의 data dependence를 측정하려는 시도다.

이 관점은 compression과도 연결된다. 훈련 결과를 짧게 기술할 수 있으면 데이터에 대한 의존이 제한되고 일반화 gap을 제어하기 쉬워진다.

### 추정의 함정

고차원 연속 변수의 상호 정보량 추정은 estimator choice에 매우 민감하다. InfoNCE 같은 contrastive bound는 유용하지만, batch size와 negative sampling에 의존하는 하한이다. 따라서 "MI가 커졌다/작아졌다"는 실험 주장은 추정 방법과 함께 읽어야 한다.

## 구현 (Implementation)

이산 변수의 상호 정보량은 빈도표에서 추정할 수 있다.

```python
import math
from collections import Counter


def mutual_information(xs, ys):
    n = len(xs)
    cx = Counter(xs)
    cy = Counter(ys)
    cxy = Counter(zip(xs, ys))
    mi = 0.0
    for (x, y), count in cxy.items():
        pxy = count / n
        px = cx[x] / n
        py = cy[y] / n
        mi += pxy * math.log(pxy / (px * py))
    return mi


print(round(mutual_information([0, 0, 1, 1], [0, 0, 1, 1]), 3))
```

연속 고차원 변수의 상호 정보량 추정은 어렵고, variational bound나 contrastive objective가 자주 쓰인다.

```python
def pointwise_mutual_information(pxy, px, py):
    import math
    return math.log(pxy / (px * py))
```

상호 정보량은 pointwise dependence를 joint distribution에 대해 평균낸 값으로 볼 수 있다.

## 복잡도 (Complexity)

이산 작은 변수의 plug-in 추정은 표본 수에 선형이지만, 고차원 연속 변수에서는 밀도 추정 자체가 어렵다. 추정량의 bias와 variance가 커질 수 있어 정보량 기반 해석은 신중해야 한다.

## 응용 (Applications)

- 표현 학습과 information bottleneck
- contrastive learning 목적 해석
- 일반화 경계와 알고리즘 안정성 분석
- feature selection과 dependency 측정

## 흔한 오해 (Common Misunderstandings)

- 상호 정보량이 크다고 항상 좋은 표현은 아니다. 불필요한 잡음도 정보다.
- 연속 변수의 상호 정보량 추정은 단순하지 않다.
- 정보량 기반 경계가 실제 성능을 날카롭게 예측한다고 보장되지는 않는다.
- correlation이 0이어도 비선형 의존으로 상호 정보량은 양수일 수 있다.

## TMI

- InfoNCE는 contrastive learning에서 상호 정보량 하한과 연결되어 자주 설명된다.
- 데이터 처리 부등식은 후처리로 정보가 증가하지 않는다는 핵심 원리다.
- 딥러닝에서 information bottleneck 해석은 흥미롭지만 측정과 가정에 민감하다.

## 연습 / 확인 문제 (Exercises)

- 독립 변수의 상호 정보량이 0이 되는 이유를 정의로 보이라.
- information bottleneck 목적의 두 항이 각각 무엇을 선호하는지 설명하라.
- 고차원 연속 표현의 상호 정보량 추정이 어려운 이유를 말하라.

## 이어서 읽기 (Reading Path)

- 이전: [MDL](MDL.md)
- 다음: [AI/PGMs/](../PGMs/)

## 참조 (References)

- [Math/Probability-Statistics/Information-Theory.md](../../Math/Probability-Statistics/Information-Theory.md)
- [MDL.md](MDL.md)
- [Generalization-Bounds.md](Generalization-Bounds.md)
- [Reference/Books.md](../../Reference/Books.md)
