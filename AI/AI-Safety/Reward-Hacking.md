# 보상 해킹과 목표 오명세 (Reward Hacking and Goal Misgeneralization)

- Level: Advanced
- Prerequisites: [Alignment-Overview.md](Alignment-Overview.md), [AI/Reinforcement-Learning/MDP.md](../Reinforcement-Learning/MDP.md), [AI/Machine-Learning/Overfitting.md](../Machine-Learning/Overfitting.md)
- Status: Draft
- Reviewed-by: -

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
