# 변분 추론 (Variational Inference)

- Level: Advanced
- Prerequisites: [MCMC.md](MCMC.md), [Factorization.md](Factorization.md), [Math/Probability-Statistics/MLE.md](../../Math/Probability-Statistics/MLE.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

변분 추론은 계산하기 어려운 posterior $p(z\mid x)$를 다루기 쉬운 분포 $q_\phi(z)$로 근사하는 방법이다. 샘플링으로 posterior를 탐색하는 MCMC와 달리, 변분 추론은 근사 분포를 최적화 문제로 맞춘다.

## 직관 (Intuition)

복잡한 산의 정확한 모양을 모두 따라 그리기 어렵다면, 특정 모양의 고무막을 골라 최대한 비슷하게 맞춘다고 생각할 수 있다. 고무막의 형태를 단순하게 제한하면 계산은 쉬워지지만, 실제 posterior와 차이가 생길 수 있다.

## 이론 (Theory)

잠재변수 모델에서 로그 주변우도는 다음처럼 ELBO로 하한을 만들 수 있다.

$$
\log p(x)\ge
E_{q_\phi(z)}[\log p_\theta(x,z)-\log q_\phi(z)]
=\mathcal{L}(\theta,\phi)
$$

ELBO를 최대화하는 것은

$$
KL(q_\phi(z)\|p_\theta(z\mid x))
$$

를 줄이는 것과 연결된다. mean-field variational inference는 $q(z)=\prod_i q_i(z_i)$처럼 독립적인 factor로 posterior를 근사한다. 이 가정은 계산을 쉽게 하지만 posterior correlation을 놓칠 수 있다.

## 구현 (Implementation)

ELBO는 reconstruction 항과 KL 항의 조합으로 자주 구현된다.

```python
def elbo(log_px_given_z, log_pz, log_qz):
    return log_px_given_z + log_pz - log_qz


samples = [
    {"log_px_given_z": -1.2, "log_pz": -0.7, "log_qz": -0.5},
    {"log_px_given_z": -1.0, "log_pz": -0.8, "log_qz": -0.6},
]

estimate = sum(elbo(**s) for s in samples) / len(samples)
print(round(estimate, 3))
```

VAE는 neural encoder가 $q_\phi(z\mid x)$를 만들고 reparameterization trick으로 ELBO를 최적화하는 대표 사례다.

## 복잡도 (Complexity)

변분 추론은 MCMC보다 빠르고 대규모 데이터에 적합할 수 있지만, 근사 family 선택에 따른 bias가 생긴다. stochastic variational inference는 mini-batch로 확장 가능하지만 gradient variance와 수렴 진단이 중요하다.

## 응용 (Applications)

- 베이지안 posterior 근사
- 토픽 모델과 혼합 모델
- VAE와 deep latent variable model
- 대규모 확률 모델의 빠른 근사 추론

## 흔한 오해 (Common Misunderstandings)

- 변분 추론은 정확한 추론이 아니라 근사 추론이다.
- ELBO가 높아졌다고 posterior의 모든 측면이 잘 맞는 것은 아니다.
- mean-field 가정은 posterior 상관을 과소평가할 수 있다.
- MCMC보다 항상 좋은 것은 아니다. 정확성/속도 trade-off가 있다.

## TMI

- KL 방향 $KL(q\|p)$는 mode-seeking 성향을 가져 posterior 불확실성을 과소평가할 수 있다.
- black-box variational inference는 모델별 수식 유도 부담을 줄인다.
- amortized inference는 각 데이터마다 최적화하지 않고 neural network로 variational parameter를 예측한다.

## 연습 / 확인 문제 (Exercises)

- Jensen 부등식을 사용해 ELBO를 유도하라.
- mean-field 가정의 장점과 한계를 설명하라.
- MCMC와 변분 추론을 속도와 정확성 관점에서 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [신뢰 전파](Belief-Propagation.md), [MCMC](MCMC.md)
- 다음: [EM 알고리즘](EM-Algorithm.md)

## 참조 (References)

- [MCMC.md](MCMC.md)
- [Factorization.md](Factorization.md)
- [Math/Probability-Statistics/MLE.md](../../Math/Probability-Statistics/MLE.md)
- [AI/Generative-Models/VAE.md](../Generative-Models/VAE.md)
