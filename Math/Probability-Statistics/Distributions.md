# 확률 변수와 분포 (Random Variables and Distributions)

- Level: Intermediate
- Prerequisites: [Math/Probability-Statistics/Probability-Basics.md](Probability-Basics.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

확률 변수는 표본 공간의 결과를 수로 대응시키는 함수이고, 확률 분포는 그 값들이 얼마나 자주 나타나는지 기술한다. 이산 변수는 확률질량함수(PMF), 연속 변수는 확률밀도함수(PDF), 둘 모두 누적분포함수(CDF)로 표현할 수 있다.

## 직관 (Intuition)

동전을 열 번 던졌을 때 앞면의 개수는 0부터 10까지인 이산 확률 변수다. 사람의 키는 구간 안의 연속적인 값을 갖는 연속 확률 변수로 모델링할 수 있다. 분포는 가능한 값의 목록뿐 아니라 값마다 확률이 어떻게 퍼져 있는지를 함께 말한다.

## 이론 (Theory)

이산 변수 $X$의 PMF는 $p(x)=P(X=x)$이고 $\sum_x p(x)=1$이다. 연속 변수의 PDF $f(x)$는 구간 확률을 적분으로 준다.

$$
P(a\le X\le b)=\int_a^b f(x)\,dx,\qquad F(x)=P(X\le x)
$$

| 분포 | 주요 매개변수 | 대표 용도 |
|---|---|---|
| Bernoulli | 성공확률 $p$ | 한 번의 성공/실패 |
| Binomial | 시행 수 $n$, 확률 $p$ | 독립 시행의 성공 횟수 |
| Poisson | 발생률 $\lambda$ | 구간 내 사건 횟수 |
| Uniform | 구간 $[a,b]$ | 구간에서 동일한 밀도 |
| Normal | 평균 $\mu$, 분산 $\sigma^2$ | 합성 오차와 자연 변동 |
| Exponential | 발생률 $\lambda$ | Poisson 사건 사이 대기시간 |

PDF 값은 확률 자체가 아니며 1보다 클 수도 있다. 연속 변수에서 한 점의 확률은 0이고, 구간 아래 면적이 확률이다.

## 구현 (Implementation)

```python
import math
import random


def normal_pdf(x, mean=0.0, std=1.0):
    z = (x - mean) / std
    return math.exp(-0.5 * z * z) / (std * math.sqrt(2 * math.pi))


samples = [sum(random.random() < 0.3 for _ in range(10)) for _ in range(10_000)]
print(sum(samples) / len(samples))  # Binomial(10, 0.3)의 평균 약 3
print(normal_pdf(0.0))
```

## 복잡도 (Complexity)

닫힌 형태의 PMF/PDF 한 점 평가는 보통 `O(1)`이다. 표본 $N$개 생성과 통계량 계산은 `O(N)`이다. 고차원 결합분포는 가능한 조합 수나 적분 비용이 차원에 따라 급격히 커질 수 있다.

## 응용 (Applications)

- 분류 출력, 사건 횟수, 대기시간의 확률 모델링
- 시뮬레이션과 불확실성 전파
- 우도 함수와 베이즈 추론의 모델 정의
- 이상치 탐지와 신뢰 구간 계산

## 흔한 오해 (Common Misunderstandings)

- PDF의 높이는 확률이 아니다. 구간 적분이 확률이다.
- 데이터가 종 모양이라고 자동으로 정규분포인 것은 아니다.
- 같은 평균과 분산을 가진 분포도 꼬리와 모양은 다를 수 있다.
- 독립이고 같은 분포를 따른다는 i.i.d. 가정은 편리하지만 실제 데이터에서는 확인이 필요하다.

## TMI

- 지수분포는 이미 기다린 시간과 무관하게 남은 대기시간 분포가 같은 memoryless 성질을 가진다.
- 정규분포의 선형결합은 다시 정규분포가 되지만, 일반 분포에는 이런 닫힘이 없다.
- 두 변수의 주변분포만으로 결합분포가 완전히 정해지지는 않는다.

## 연습 / 확인 문제 (Exercises)

- Bernoulli와 Binomial 분포의 차이를 예로 설명하라.
- 표준정규 PDF 아래 전체 면적이 1인 이유를 조사하라.
- 평균이 같은 Poisson 표본과 Normal 표본을 생성해 히스토그램 모양을 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [확률 공리와 조건부 확률](Probability-Basics.md)
- 다음: [기댓값, 분산, 공분산](Expectation.md), [베이즈 정리](Bayes-Theorem.md)

## 참조 (References)

- [Math/Probability-Statistics/Probability-Basics.md](Probability-Basics.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
