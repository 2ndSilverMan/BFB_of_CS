# RLHF (Reinforcement Learning from Human Feedback)

- Level: Advanced
- Prerequisites: [AI/LLMs/Instruction-Tuning.md](Instruction-Tuning.md), [AI/Reinforcement-Learning/PPO.md](../Reinforcement-Learning/PPO.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

RLHF는 사람의 선호 비교나 평가를 보상 모델로 학습하고, 언어 모델 정책을 그 보상에 맞춰 최적화하는 정렬 방법이다. 보통 SFT 이후 응답 품질, 유용성, 안전성을 조정하는 데 사용한다.

## 직관 (Intuition)

정답이 하나로 정해지지 않은 질문에서는 "어느 답이 더 좋은가"를 사람이 비교하는 편이 쉽다. RLHF는 그 비교 감각을 reward model로 근사하고, 모델이 더 선호되는 답을 내도록 훈련한다.

## 이론 (Theory)

전형적 파이프라인은 SFT model → preference data 수집 → reward model 학습 → PPO 등으로 policy optimization이다. 정책이 원래 모델에서 과도하게 멀어지지 않도록 KL penalty를 둔다.

Reward model은 사람 선호의 proxy이며 진짜 목표가 아니다. 따라서 reward hacking, overoptimization, labeler bias, policy drift가 주요 위험이다.

## 구현 (Implementation)

```python
objective = {
    "maximize": "reward_model(prompt, response)",
    "regularize": "KL(policy || reference_policy)",
}
```

운영에서는 data quality, label guideline, rejection sampling, safety evaluation을 함께 관리한다.

## 복잡도 (Complexity)

SFT보다 파이프라인이 복잡하다. Reward model 학습, policy sampling, KL-controlled RL update, 평가가 반복되며 안정성 튜닝이 어렵다.

## 응용 (Applications)

- 대화형 assistant 정렬
- 선호 기반 요약·코딩 응답 개선
- 안전 정책 준수 강화
- 도메인별 응답 스타일 조정

## 흔한 오해 (Common Misunderstandings)

- RLHF가 진실성을 직접 보장하지 않는다. 선호를 최적화할 뿐이다.
- 사람 피드백은 편향과 불일치를 가진다.
- Reward가 높아질수록 무조건 좋은 모델이 되는 것은 아니다.
- RLHF 없이도 SFT나 DPO로 유사한 행동 개선이 가능할 수 있다.

## TMI

- KL penalty는 모델이 보상 모델의 허점을 과도하게 파고드는 것을 완화한다.
- Preference data는 prompt distribution에 매우 민감하다.
- Constitutional AI류 방법은 일부 피드백 생성을 규칙이나 모델 critique로 보조한다.

## 연습 / 확인 문제 (Exercises)

- RLHF 파이프라인의 네 단계를 설명하라.
- Reward hacking 사례를 하나 만들어라.
- KL penalty가 커지거나 작아질 때 모델 행동을 예측하라.

## 이어서 읽기 (Reading Path)

- 이전: [Instruction Tuning](Instruction-Tuning.md)
- 다음: [DPO](DPO.md), [AI Safety의 RLHF](../AI-Safety/RLHF-Constitutional-AI.md)

## 참조 (References)

- [AI/Reinforcement-Learning/PPO.md](../Reinforcement-Learning/PPO.md)
- [AI/AI-Safety/RLHF-Constitutional-AI.md](../AI-Safety/RLHF-Constitutional-AI.md)
- [Reference/Papers.md](../../Reference/Papers.md)
