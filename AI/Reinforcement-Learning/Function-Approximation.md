# 함수 근사 (Function Approximation in RL)

- Level: Advanced
- Prerequisites: [TD-Learning.md](TD-Learning.md), [AI/Machine-Learning/Linear-Regression.md](../Machine-Learning/Linear-Regression.md), [AI/Deep-Learning/MLP.md](../Deep-Learning/MLP.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

함수 근사는 상태나 행동 공간이 너무 커서 tabular value를 저장할 수 없을 때, 파라미터화된 함수 $V_\theta(s)$, $Q_\theta(s,a)$, $\pi_\theta(a\mid s)$로 가치나 정책을 표현하는 방법이다. 선형 모델부터 신경망까지 사용할 수 있다.

## 직관 (Intuition)

모든 칸의 가치를 표로 외울 수 없는 큰 게임에서는 비슷한 상태들이 비슷한 가치를 갖는다는 패턴을 배워야 한다. 함수 근사는 본 적 없는 상태에서도 feature와 파라미터를 통해 값을 예측한다.

## 이론 (Theory)

선형 가치 근사는

$$
V_\theta(s)=\theta^\top \phi(s)
$$

처럼 feature vector $\phi(s)$와 파라미터 $\theta$를 사용한다. TD 학습과 결합하면 TD error

$$
\delta_t=R_{t+1}+\gamma V_\theta(S_{t+1})-V_\theta(S_t)
$$

를 줄이도록 파라미터를 업데이트한다.

비선형 신경망 근사는 표현력이 크지만 안정성이 어려워진다. bootstrapping, off-policy learning, function approximation이 함께 있을 때 발산할 수 있는 “deadly triad”가 유명하다.

## 구현 (Implementation)

선형 TD(0) 업데이트는 다음처럼 쓸 수 있다.

```python
def dot(a, b):
    return sum(x * y for x, y in zip(a, b))


def td_linear_update(theta, phi_s, reward, phi_next, gamma, alpha):
    delta = reward + gamma * dot(theta, phi_next) - dot(theta, phi_s)
    return [w + alpha * delta * x for w, x in zip(theta, phi_s)]


print(td_linear_update([0.1, 0.2], [1, 0], 1.0, [0, 1], 0.9, 0.01))
```

신경망을 쓰면 loss를 만들고 backpropagation으로 파라미터를 갱신한다.

## 복잡도 (Complexity)

테이블 방식은 상태-행동 수에 비례해 저장하지만, 함수 근사는 파라미터 수에 비례한다. 대신 학습은 최적화 문제가 되며, 모델 평가와 gradient 계산 비용이 추가된다.

## 응용 (Applications)

- 대규모/연속 상태 공간 RL
- DQN과 policy gradient의 신경망 기반
- 선형 feature 기반 제어
- representation learning과 RL 결합

## 흔한 오해 (Common Misunderstandings)

- 함수 근사를 쓰면 자동으로 일반화가 좋아지는 것은 아니다.
- 신경망 근사는 강력하지만 안정화 장치가 필요하다.
- tabular 알고리즘의 수렴 보장이 그대로 유지되지 않을 수 있다.
- feature 설계나 representation 품질이 성능에 크게 영향을 준다.

## TMI

- Tile coding과 radial basis function은 고전적 RL feature 표현이다.
- Target network와 replay buffer는 딥 RL에서 function approximation 불안정을 줄이는 대표 장치다.
- Distributional RL은 가치의 평균뿐 아니라 return distribution을 근사한다.

## 연습 / 확인 문제 (Exercises)

- Tabular value function과 함수 근사의 차이를 설명하라.
- Deadly triad의 세 요소를 나열하라.
- 선형 가치 근사에서 feature scaling이 중요한 이유를 말하라.

## 이어서 읽기 (Reading Path)

- 이전: [TD 학습](TD-Learning.md)
- 다음: [DQN](DQN.md)

## 참조 (References)

- [TD-Learning.md](TD-Learning.md)
- [AI/Machine-Learning/Linear-Regression.md](../Machine-Learning/Linear-Regression.md)
- [AI/Deep-Learning/MLP.md](../Deep-Learning/MLP.md)
- [Reference/Books.md](../../Reference/Books.md)
