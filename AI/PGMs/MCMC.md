# MCMC 샘플링 (Markov Chain Monte Carlo)

- Level: Advanced
- Prerequisites: [Belief-Propagation.md](Belief-Propagation.md), [Math/Probability-Statistics/Distributions.md](../../Math/Probability-Statistics/Distributions.md), [Math/Probability-Statistics/Expectation.md](../../Math/Probability-Statistics/Expectation.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

MCMC는 직접 샘플링하기 어려운 분포에서, 그 분포를 정상분포(stationary distribution)로 갖는 마르코프 체인을 만들어 샘플을 얻는 방법이다. 대표 알고리즘으로 Metropolis-Hastings와 Gibbs sampling이 있다.

## 직관 (Intuition)

높은 산맥의 지형을 정확한 지도 없이 탐색한다고 하자. 현재 위치 주변을 조금씩 제안하고, 더 그럴듯한 곳은 잘 받아들이고 덜 그럴듯한 곳도 가끔 받아들이면 긴 시간 뒤에는 자주 방문한 곳이 목표 분포의 밀도를 반영한다.

## 이론 (Theory)

목표 분포를 $\pi(x)$라고 하자. Metropolis-Hastings는 현재 상태 $x$에서 제안분포 $q(x'\mid x)$로 후보 $x'$를 뽑고, 다음 확률로 수락한다.

$$
\alpha=\min\left(1,
\frac{\pi(x')q(x\mid x')}{\pi(x)q(x'\mid x)}
\right)
$$

이 전이 규칙이 detailed balance를 만족하면 $\pi$가 체인의 정상분포가 된다. Gibbs sampling은 각 변수의 조건부분포 $P(X_i\mid X_{-i})$에서 차례로 샘플링하는 특수한 MCMC다.

실제 사용에서는 burn-in, mixing time, autocorrelation, effective sample size가 중요하다. 샘플이 많아도 서로 강하게 상관되어 있으면 독립 표본 수는 적다.

## 구현 (Implementation)

대칭 proposal을 쓰는 random-walk Metropolis로 표준정규분포를 샘플링할 수 있다.

```python
import math
import random


def log_target(x):
    return -0.5 * x * x


def metropolis(steps, proposal_std=1.0):
    x = 0.0
    samples = []
    for _ in range(steps):
        candidate = x + random.gauss(0.0, proposal_std)
        log_accept = log_target(candidate) - log_target(x)
        if math.log(random.random()) < min(0.0, log_accept):
            x = candidate
        samples.append(x)
    return samples


samples = metropolis(10_000)
print(round(sum(samples[1000:]) / len(samples[1000:]), 3))
```

고차원 모델에서는 proposal 설계가 성능을 좌우한다. 너무 작은 proposal은 천천히 움직이고, 너무 큰 proposal은 거절이 많아진다.

## 복잡도 (Complexity)

한 스텝 비용은 목표 밀도 또는 조건부분포 계산 비용이다. 총 비용은 필요한 effective sample size와 mixing 속도에 좌우된다. 차원이 높거나 posterior가 여러 mode를 가지면 mixing이 매우 느릴 수 있다.

## 응용 (Applications)

- 베이지안 posterior 추론
- PGM의 근사 marginal 계산
- 물리 시뮬레이션과 통계역학
- 잠재 변수 모델의 불확실성 추정

## 흔한 오해 (Common Misunderstandings)

- MCMC 샘플은 일반적으로 독립 표본이 아니다.
- burn-in을 버린다고 항상 mixing 문제가 해결되는 것은 아니다.
- acceptance rate가 높을수록 항상 좋은 것은 아니다. 거의 움직이지 않아도 acceptance는 높을 수 있다.
- 정규화 상수를 몰라도 비례 밀도만으로 동작할 수 있지만, proposal과 진단은 여전히 어렵다.

## TMI

- Hamiltonian Monte Carlo는 gradient를 사용해 고차원 연속분포에서 더 긴 이동을 효율적으로 제안한다.
- collapsed Gibbs sampling은 일부 변수를 적분해 mixing을 개선할 수 있다.
- 여러 체인을 돌려 수렴 진단을 하는 것은 실무에서 거의 필수에 가깝다.

## 연습 / 확인 문제 (Exercises)

- Metropolis-Hastings의 수락확률에서 proposal 비율이 왜 필요한지 설명하라.
- Gibbs sampling이 항상 수락되는 이유를 조건부분포 관점에서 설명하라.
- autocorrelation이 effective sample size를 줄이는 이유를 말하라.

## 이어서 읽기 (Reading Path)

- 이전: [신뢰 전파](Belief-Propagation.md)
- 다음: [AI/Causal-Inference/](../Causal-Inference/)

## 참조 (References)

- [Belief-Propagation.md](Belief-Propagation.md)
- [Math/Probability-Statistics/Distributions.md](../../Math/Probability-Statistics/Distributions.md)
- [Math/Probability-Statistics/Expectation.md](../../Math/Probability-Statistics/Expectation.md)
- [Reference/Books.md](../../Reference/Books.md)
