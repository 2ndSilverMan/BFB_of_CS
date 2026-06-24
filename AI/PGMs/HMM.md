# Hidden Markov Model (HMM)

- Level: Advanced
- Prerequisites: [Bayesian-Networks.md](Bayesian-Networks.md), [Math/Probability-Statistics/Markov-Chains.md](../../Math/Probability-Statistics/Markov-Chains.md), [Belief-Propagation.md](Belief-Propagation.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

Hidden Markov Model은 시간에 따라 변하는 숨은 상태 $Z_t$와 그 상태에서 생성되는 관측 $X_t$를 모델링하는 순차 확률 모델이다. 상태는 직접 보이지 않고, 관측 시퀀스를 통해 추론한다.

## 직관 (Intuition)

밖의 날씨는 직접 못 보고 사람이 우산을 들었는지만 본다고 하자. 날씨는 전날 날씨에 영향을 받고, 우산 관측은 오늘 날씨에 영향을 받는다. HMM은 이런 “숨은 상태 + 관측” 구조를 시간축으로 펼친 베이지안 네트워크다.

## 이론 (Theory)

HMM은 보통 세 요소를 갖는다.

- 초기분포: $P(Z_1)$
- 전이확률: $P(Z_t\mid Z_{t-1})$
- 방출확률: $P(X_t\mid Z_t)$

결합분포는

$$
P(z_{1:T},x_{1:T})=P(z_1)P(x_1\mid z_1)\prod_{t=2}^{T}P(z_t\mid z_{t-1})P(x_t\mid z_t)
$$

로 쓸 수 있다. 주요 추론 문제는 filtering $P(Z_t\mid x_{1:t})$, smoothing $P(Z_t\mid x_{1:T})$, decoding $\arg\max z_{1:T}P(z_{1:T}\mid x_{1:T})$이다. Viterbi 알고리즘은 가장 가능성 높은 상태열을 동적 계획법으로 찾는다.

## 구현 (Implementation)

Viterbi의 핵심은 이전 최적 점수에서 현재 전이와 방출 확률을 곱해 갱신하는 것이다.

```python
def viterbi_step(prev_scores, transition, emission_obs):
    next_scores = {}
    for z in emission_obs:
        best = max(
            prev_scores[p] * transition[p][z] * emission_obs[z]
            for p in prev_scores
        )
        next_scores[z] = best
    return next_scores


prev = {"sunny": 0.3, "rainy": 0.7}
transition = {
    "sunny": {"sunny": 0.8, "rainy": 0.2},
    "rainy": {"sunny": 0.3, "rainy": 0.7},
}
emission = {"sunny": 0.1, "rainy": 0.9}
print(viterbi_step(prev, transition, emission))
```

실제 구현은 underflow 방지를 위해 로그 확률을 사용한다.

## 복잡도 (Complexity)

상태 수를 $K$, 시퀀스 길이를 $T$라 하면 forward, backward, Viterbi는 보통 $O(TK^2)$ 시간이 든다. sparse transition이면 더 줄일 수 있다. 메모리는 전체 경로 복원이 필요하면 $O(TK)$가 든다.

## 응용 (Applications)

- 품사 태깅과 음성 인식의 고전 모델
- 생물정보학 시퀀스 분석
- 센서 상태 추정
- 이상 탐지와 regime switching 모델

## 흔한 오해 (Common Misunderstandings)

- HMM은 관측이 Markov라는 뜻이 아니라 숨은 상태가 Markov라는 가정이다.
- 현재 관측은 현재 숨은 상태에만 의존한다고 가정한다.
- Viterbi 경로와 각 시점별 최빈 상태를 따로 고른 결과는 다를 수 있다.
- 딥러닝 시퀀스 모델이 등장했다고 HMM의 추론 아이디어가 사라진 것은 아니다.

## TMI

- forward-backward 알고리즘은 chain 구조에서의 sum-product belief propagation이다.
- Baum-Welch 알고리즘은 HMM 파라미터 학습을 위한 EM 알고리즘이다.
- CRF는 HMM과 달리 관측 전체를 조건으로 라벨 시퀀스를 직접 모델링한다.

## 연습 / 확인 문제 (Exercises)

- HMM의 결합분포 인수분해식을 써라.
- filtering과 smoothing의 차이를 설명하라.
- Viterbi와 forward 알고리즘의 목적 차이를 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [나이브 베이즈](Naive-Bayes.md)
- 다음: [MRF](MRF.md), [CRF](CRF.md)

## 참조 (References)

- [Bayesian-Networks.md](Bayesian-Networks.md)
- [Math/Probability-Statistics/Markov-Chains.md](../../Math/Probability-Statistics/Markov-Chains.md)
- [Belief-Propagation.md](Belief-Propagation.md)
- [Reference/Books.md](../../Reference/Books.md)
