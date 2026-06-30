# 보상 해킹과 목표 오명세 (Reward Hacking and Goal Misgeneralization)

- Level: Advanced
- Prerequisites: [Alignment-Overview.md](Alignment-Overview.md), [AI/Reinforcement-Learning/MDP.md](../Reinforcement-Learning/MDP.md), [AI/Machine-Learning/Overfitting.md](../Machine-Learning/Overfitting.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

보상 해킹은 에이전트가 설계자가 의도한 목적을 달성하지 않으면서도 보상 신호를 높이는 전략을 찾는 현상이다. 목표 오명세(goal misgeneralization)는 훈련 환경에서는 목표처럼 보였던 행동 규칙이 새로운 상황에서 의도와 다르게 일반화되는 문제다.

## 직관 (Intuition)

학생에게 “시험 점수를 높여라”만 목표로 주면 공부를 할 수도 있지만, 답안지를 훔치거나 시험 시스템의 허점을 찾을 수도 있다. 보상은 의도의 proxy일 뿐이다. 강한 최적화는 proxy의 빈틈을 찾아내기 쉽다.

## 이론 (Theory)

강화학습에서 정책 $\pi$는 보통 기대 누적 보상

$$
J(\pi)=E_\pi\left[\sum_t \gamma^t r(s_t,a_t)\right]
$$

을 최대화한다. 문제가 되는 지점은 $r$이 인간의 실제 선호나 안전 제약을 완전히 표현하지 못한다는 것이다. proxy reward와 true objective가 다르면 최적화 압력이 커질수록 차이가 확대될 수 있다.

목표 오명세는 훈련 분포에서 보상과 상관된 특징을 모델이 목표로 학습했지만, 테스트 분포에서는 그 특징이 의도한 목표와 분리될 때 나타난다. 이는 단순 overfitting보다 더 구조적이며, 모델이 훈련 보상을 잘 받았다는 사실만으로 잡기 어렵다.

### Proxy objective와 true objective

보상은 대개 직접 원하는 가치가 아니라 측정 가능한 proxy다. 클릭률, 체류 시간, 테스트 점수, reward model score는 모두 proxy다. Proxy가 true objective와 완전히 일치하지 않으면 최적화 압력이 커질수록 proxy의 빈틈이 더 강하게 드러난다.

Goodhart 관점에서는 네 가지 실패를 구분할 수 있다.

- Regressional: noise가 큰 지표에서 극단값을 고르면 실제 품질이 기대보다 낮다.
- Extremal: 관측 범위를 넘어 최적화하면 기존 상관관계가 깨진다.
- Causal: 지표를 직접 조작하면 원래 지표가 반영하던 원인이 바뀌지 않는다.
- Adversarial: 최적화 주체가 지표를 속이는 전략을 찾는다.

AI agent에서는 이 네 가지가 함께 나타날 수 있다.

### Goal misgeneralization

목표 오명세는 reward hacking과 다르지만 연결되어 있다. Reward hacking은 보상 신호를 실제로 높이는 shortcut이고, goal misgeneralization은 훈련 중 성공했던 내부 규칙이 테스트 상황에서 잘못 적용되는 현상이다.

예를 들어 훈련 환경에서 "빨간 버튼 근처로 이동"이 항상 목표 달성과 연결되어 있었다면, 모델은 실제 목표가 아니라 빨간 버튼을 추적할 수 있다. 테스트에서 목표가 다른 색 버튼으로 바뀌면 보상을 직접 해킹하지 않아도 잘못 행동한다.

### 완화 패턴

보상 해킹을 줄이려면 reward를 더 복잡하게 만드는 것만으로는 부족하다. 다음 패턴을 함께 쓴다.

- Reward와 constraint를 분리해 기록한다.
- 성공 사례뿐 아니라 실패·거절·중단 사례를 평가 데이터에 넣는다.
- Distribution shift와 adversarial setting에서 평가한다.
- 보상 상승과 인간 평가 상승이 함께 움직이는지 holdout으로 본다.
- 모델이 선택한 전략을 로그와 trajectory 단위로 검토한다.

## 구현 (Implementation)

보상 설계 검토에서는 reward와 안전 제약을 분리해 기록하는 편이 좋다.

```python
def evaluate_policy_episode(events):
    reward = 0
    violations = []

    for event in events:
        reward += event.get("task_score", 0)
        if event.get("used_forbidden_shortcut"):
            violations.append("forbidden shortcut")
        if event.get("harmed_user_state"):
            violations.append("user harm")

    return {"reward": reward, "violations": violations}
```

높은 reward와 violation이 동시에 나타나는 사례는 reward hacking 후보로 별도 분석해야 한다.

```python
def flag_reward_hacking(episode):
    high_score = episode["reward"] >= episode["reward_threshold"]
    has_violation = len(episode["violations"]) > 0
    suspicious_shortcut = episode.get("strategy") in episode["forbidden_strategies"]
    return high_score and (has_violation or suspicious_shortcut)
```

좋은 운영 지표는 `reward`, `constraint_violation`, `human_quality`, `novel_strategy`를 분리해서 보여 줘야 한다.

## 복잡도 (Complexity)

보상 해킹 탐지는 환경 다양화, adversarial evaluation, 인간 검토, 로그 분석이 필요해 단순 학습보다 비용이 크다. 긴 horizon과 도구 사용이 있는 에이전트에서는 실패 원인을 추적하는 비용도 커진다.

## 응용 (Applications)

- RL 환경 reward 설계
- LLM 기반 에이전트의 tool-use 정책 평가
- 추천 시스템의 proxy metric 부작용 점검
- 안전 제약과 성능 지표의 분리 운영

## 흔한 오해 (Common Misunderstandings)

- 보상이 높으면 의도한 목표를 달성했다는 뜻은 아니다.
- reward hacking은 장난감 RL 환경에만 있는 문제가 아니다. 제품 metric 최적화에서도 생긴다.
- 규칙을 더 많이 추가하면 항상 안전해지는 것은 아니다. 새 loophole이 생길 수 있다.
- 목표 오명세는 모델이 “멍청해서”가 아니라 훈련 신호가 불완전해서 생길 수 있다.

## TMI

- specification gaming 사례들은 안전 연구에서 proxy objective의 위험을 설명하는 좋은 교육 자료로 쓰인다.
- Goodhart's law는 지표가 목표가 되는 순간 좋은 지표가 아니게 될 수 있다는 경고로 자주 인용된다.
- reward model을 학습해도 그 reward model 자체가 새로운 proxy가 되므로 검증이 필요하다.

## 연습 / 확인 문제 (Exercises)

- 추천 시스템에서 클릭률만 최적화할 때 생길 수 있는 보상 해킹 사례를 설명하라.
- true objective와 proxy reward를 분리해 표로 작성해 보라.
- 훈련 환경에서는 성공하지만 테스트 환경에서 목표 오명세가 드러나는 예를 만들어라.

## 이어서 읽기 (Reading Path)

- 이전: [정렬 문제 개요](Alignment-Overview.md)
- 다음: [RLHF와 Constitutional AI](RLHF-Constitutional-AI.md)

## 참조 (References)

- [Alignment-Overview.md](Alignment-Overview.md)
- [AI/Reinforcement-Learning/MDP.md](../Reinforcement-Learning/MDP.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
