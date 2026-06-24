# 중심 극한 정리 (Central Limit Theorem)

- Level: Intermediate
- Prerequisites: [Math/Probability-Statistics/Expectation.md](Expectation.md), [Math/Probability-Statistics/Distributions.md](Distributions.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

중심 극한 정리(CLT)는 적절한 조건에서 독립이고 같은 분포를 따르는 확률 변수의 합이나 평균을 표준화하면, 원래 분포의 모양과 무관하게 표본 수가 커질수록 표준정규분포에 가까워진다는 정리다.

## 직관 (Intuition)

한 번의 주사위 결과는 평평한 이산 분포지만, 여러 주사위의 평균을 반복해서 기록하면 가운데가 높고 양끝이 낮은 종 모양이 나타난다. 서로 독립인 작은 변동들이 더해질 때 정규분포가 자주 등장하는 이유다.

## 이론 (Theory)

$X_1,\dots,X_n$이 평균 $\mu$, 유한한 양의 분산 $\sigma^2$을 가진 i.i.d. 변수라면

$$
\frac{\sum_{i=1}^{n}X_i-n\mu}{\sigma\sqrt{n}}
=\frac{\sqrt n(\bar X_n-\mu)}{\sigma}
\xrightarrow{d}\mathcal N(0,1)
$$

이다. 따라서 큰 $n$에서 표본평균은 근사적으로 $\mathcal N(\mu,\sigma^2/n)$을 따른다. 평균의 표준편차 $\sigma/\sqrt n$을 표준오차라 한다.

CLT는 표본 자체가 정규분포가 된다는 말이 아니라 **표본평균의 반복 표집 분포**에 대한 말이다. 심한 꼬리, 의존성, 무한 분산에서는 수렴이 느리거나 기본 형태의 정리가 적용되지 않을 수 있다.

## 구현 (Implementation)

```python
import random
import statistics


def sample_mean(sample_size):
    return statistics.mean(random.randint(1, 6) for _ in range(sample_size))


means = [sample_mean(30) for _ in range(20_000)]
print(round(statistics.mean(means), 3))
print(round(statistics.pstdev(means), 3))  # 이론값 sqrt(35/12/30) 근처
```

## 복잡도 (Complexity)

$R$번 반복해 크기 $n$의 표본평균을 시뮬레이션하면 시간 `O(Rn)`, 평균만 스트리밍하면 추가 공간 `O(R)` 또는 요약 통계만 저장할 때 `O(1)`이다.

## 응용 (Applications)

- 표본평균의 신뢰 구간과 가설 검정
- Monte Carlo 추정 오차 분석
- 측정 오차와 집계 지표의 정규 근사
- 대규모 A/B 테스트 통계량 근사

## 흔한 오해 (Common Misunderstandings)

- 표본 수 30이면 언제나 충분하다는 보편 법칙은 없다.
- CLT와 대수의 법칙은 다르다. 대수의 법칙은 평균의 수렴, CLT는 오차의 분포를 설명한다.
- 원자료가 정규분포여야만 CLT가 적용되는 것은 아니다.
- 관측값이 강하게 의존하면 i.i.d. 버전을 그대로 사용할 수 없다.

## TMI

- Berry–Esseen 정리는 정규 근사의 오차가 얼마나 빨리 줄어드는지 상한을 준다.
- Cauchy 분포는 평균과 분산이 정의되지 않아 표본평균이 일반적인 CLT처럼 안정되지 않는다.
- 합의 분산은 $n$배 늘지만 평균의 분산은 $1/n$로 줄어든다.

## 연습 / 확인 문제 (Exercises)

- 표본 크기 1, 5, 30에서 주사위 평균 분포를 비교하라.
- 표본 크기를 4배로 늘리면 표준오차가 어떻게 변하는지 설명하라.
- CLT와 대수의 법칙의 결론을 각각 한 문장으로 구분하라.

## 이어서 읽기 (Reading Path)

- 이전: [최대 우도 추정](MLE.md)
- 다음: [가설 검정](Hypothesis-Testing.md)

## 참조 (References)

- [Math/Probability-Statistics/Expectation.md](Expectation.md)
- [Math/Probability-Statistics/Distributions.md](Distributions.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
