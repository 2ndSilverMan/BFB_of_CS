# 오프라인 강화학습 (Offline Reinforcement Learning)

- Level: Advanced
- Prerequisites: [DQN.md](DQN.md), [Policy-Gradient.md](Policy-Gradient.md), [AI/MLOps/Data-Versioning.md](../MLOps/Data-Versioning.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

오프라인 RL은 환경과 새로 상호작용하지 않고, 이미 수집된 고정 데이터셋만으로 정책을 학습하는 문제다. 의료, 로봇, 추천처럼 온라인 탐험이 비싸거나 위험한 영역에서 중요하다.

## 직관 (Intuition)

운전 기록만 보고 새로운 운전 정책을 배우려 한다고 하자. 데이터에 없는 위험한 행동을 실제로 시도해볼 수 없고, 기록에 없는 상태-행동 조합의 결과를 모델이 과신하면 큰 문제가 생긴다. 오프라인 RL은 이런 분포 밖 행동을 조심해야 한다.

## 이론 (Theory)

핵심 난점은 distributional shift다. 학습 정책 $\pi$가 데이터 수집 정책 $\beta$가 거의 시도하지 않은 행동을 선택하면 Q 함수가 그 행동 가치를 부정확하게 과대평가할 수 있다.

대표 접근은 다음과 같다.

- Behavior cloning: 데이터의 행동을 모방한다.
- Conservative Q-learning: 데이터 밖 행동의 Q값을 보수적으로 낮춘다.
- Policy constraint: 학습 정책이 behavior policy에서 너무 멀어지지 않게 한다.
- Offline evaluation: 새 정책을 배포 전 안전하게 평가한다.

## 구현 (Implementation)

데이터셋에 없는 행동을 패널티 주는 보수적 아이디어는 다음처럼 표현할 수 있다.

```python
def conservative_score(q_value, action_in_dataset, penalty=1.0):
    if action_in_dataset:
        return q_value
    return q_value - penalty


print(conservative_score(5.0, action_in_dataset=False))
```

실제 알고리즘은 Q distribution, policy divergence, uncertainty estimation을 더 정교하게 사용한다.

## 복잡도 (Complexity)

오프라인 RL은 환경 interaction 비용은 없지만, 데이터 품질 검증과 off-policy evaluation이 어렵다. 데이터 커버리지가 부족하면 어떤 알고리즘도 안전한 개선을 보장하기 어렵다.

## 응용 (Applications)

- 로봇 로그 기반 정책 학습
- 의료 처치 정책 연구
- 추천/광고 로그 기반 개선
- 시뮬레이터 구축 전 초기 정책 학습

## 흔한 오해 (Common Misunderstandings)

- 고정 데이터가 많으면 오프라인 RL이 자동으로 안전한 것은 아니다.
- Supervised learning처럼 단순히 state-action을 맞추는 것만으로 장기 보상 최적화가 되지는 않는다.
- Off-policy evaluation 없이 배포하면 위험하다.
- 데이터 수집 정책의 coverage가 성능 한계를 강하게 정한다.

## TMI

- Offline RL은 causal inference의 off-policy evaluation 문제와 만나는 지점이 많다.
- D4RL은 오프라인 RL benchmark로 널리 알려져 있다.
- 실제 제품에서는 보수적 offline learning 후 작은 규모 online A/B test로 넘어가는 staged rollout이 안전하다.

## 연습 / 확인 문제 (Exercises)

- Offline RL에서 distributional shift가 위험한 이유를 설명하라.
- Behavior cloning과 offline RL의 목표 차이를 말하라.
- 데이터 커버리지가 부족한 정책 학습 사례를 하나 만들어라.

## 이어서 읽기 (Reading Path)

- 이전: [계층적 RL](Hierarchical-RL.md)
- 다음: [AI/MLOps/](../MLOps/)

## 참조 (References)

- [DQN.md](DQN.md)
- [Policy-Gradient.md](Policy-Gradient.md)
- [AI/MLOps/Data-Versioning.md](../MLOps/Data-Versioning.md)
- [Reference/Books.md](../../Reference/Books.md)
