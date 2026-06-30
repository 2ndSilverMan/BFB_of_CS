# 인간 피드백의 한계 (Feedback Limitations)

- Level: Advanced
- Prerequisites: [AI/AI-Safety/RLHF-Constitutional-AI.md](RLHF-Constitutional-AI.md), [AI/LLMs/RLHF.md](../LLMs/RLHF.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

인간 피드백의 한계는 RLHF, preference tuning, 평가 과정에서 사람의 판단이 불완전하고 비용이 높으며 모델 역량을 따라가기 어렵다는 문제다. Reward model collapse와 overoptimization도 이 맥락에서 다룬다.

## 직관 (Intuition)

사람이 더 나은 답을 고르는 일은 쉬워 보이지만, 전문 지식이 필요한 답·긴 추론·교묘한 조작에서는 판단이 흔들린다. 모델은 그 흔들림과 보상 모델의 빈틈을 학습할 수 있다.

## 이론 (Theory)

피드백의 주요 한계는 labeler bias, inconsistency, preference ambiguity, expertise gap, fatigue, distribution shift다. Reward model은 인간 선호의 proxy이므로, policy가 reward model을 과도하게 최적화하면 실제 선호와 reward가 어긋나는 reward overoptimization이 생길 수 있다.

Reward model collapse는 preference signal이 좁아지거나 모델 응답이 reward model의 특정 패턴에 몰리면서 다양성과 실제 품질이 떨어지는 현상으로 이해할 수 있다.

### 피드백 noise의 종류

인간 피드백은 단순히 noisy label이 아니라 여러 종류의 불확실성을 담는다.

- Aleatoric ambiguity: 문제 자체가 애매해서 합의된 답이 없다.
- Epistemic gap: 평가자가 필요한 지식이나 맥락을 모른다.
- Preference diversity: 사용자 집단마다 진짜 선호가 다르다.
- Instruction drift: 라벨링 지침이 시간에 따라 해석이 바뀐다.
- Fatigue effect: 반복 작업으로 판단 품질이 떨어진다.

이들을 모두 "라벨 오류"로만 처리하면 중요한 신호를 잃는다. 특히 disagreement는 정책 선택의 모호성이나 domain split의 신호일 수 있다.

### 평가자-모델 역량 격차

모델이 평가자보다 더 많은 정보를 처리하거나 더 긴 추론을 수행하면, 평가자는 그 답이 맞는지보다 그럴듯해 보이는지를 평가하게 된다. 이때 선호 최적화는 설득력, 자신감, 형식적 완성도를 과보상할 수 있다.

전문 영역에서는 일반 라벨러 평가와 expert audit을 분리해야 한다. 긴 추론이나 도구 사용 결과는 최종 답만 보지 말고 intermediate evidence, tool log, citation trace를 함께 검토한다.

### Reward overoptimization curve

정책 최적화가 진행될수록 reward model score는 계속 올라가도 독립 human score는 어느 순간 정체하거나 하락할 수 있다. 이 괴리가 reward overoptimization의 핵심 신호다.

운영에서는 다음 곡선을 함께 본다.

- Reward model score
- Holdout human preference
- Safety violation rate
- Diversity and refusal quality
- Calibration on known-answer tasks

Reward model이 policy의 최신 분포를 계속 따라가지 못하면, 높은 score는 품질이 아니라 exploitation을 의미할 수 있다.

## 구현 (Implementation)

```python
feedback_audit = {
    "inter_annotator_agreement": "tracked",
    "expert_review_required": True,
    "reward_model_holdout": "separate",
    "overoptimization_curve": "monitored",
}
```

Reward가 올라갈수록 사람 평가도 함께 올라가는지 별도 holdout과 red team set에서 확인한다.

```python
def overoptimization_alert(reward_scores, human_scores, window=5):
    reward_trend = reward_scores[-1] - reward_scores[-window]
    human_trend = human_scores[-1] - human_scores[-window]
    return reward_trend > 0 and human_trend <= 0
```

이 경고는 학습 중단 조건이 아니라 독립 평가와 데이터 재점검을 요구하는 신호로 다룬다.

## 복잡도 (Complexity)

피드백 비용은 prompt 수, 응답 수, annotator overlap, 전문성 수준에 비례한다. 고위험 도메인은 일반 라벨러가 아니라 전문가 검토가 필요해 비용이 더 커진다.

## 응용 (Applications)

- RLHF 데이터 설계
- 선호 모델 평가
- 안전 정책 라벨링
- scalable oversight 연구

## 흔한 오해 (Common Misunderstandings)

- 사람 피드백은 항상 정답이 아니라 noisy signal이다.
- Reward model 점수가 높다고 실제 사용자 가치와 일치한다고 볼 수 없다.
- 라벨러 지침이 길다고 일관성이 자동으로 보장되지는 않는다.
- 피드백을 많이 모으면 편향이 사라지는 것이 아니다.

## TMI

- Labeler disagreement는 데이터 오류뿐 아니라 문제 정의의 모호성을 드러낼 수 있다.
- Pairwise preference는 absolute score보다 쉽지만 transitivity가 항상 보장되지는 않는다.
- 모델이 점점 강해질수록 인간이 평가하기 어려운 영역이 넓어진다.

## 연습 / 확인 문제 (Exercises)

- Reward overoptimization을 탐지할 평가 곡선을 설계하라.
- 전문가 검토가 필요한 prompt 유형을 분류하라.
- 라벨러 간 불일치가 생겼을 때의 resolution 정책을 작성하라.

## 이어서 읽기 (Reading Path)

- 이전: [RLHF와 Constitutional AI](RLHF-Constitutional-AI.md)
- 다음: [Scalable Oversight](Scalable-Oversight.md), [Superalignment](Superalignment.md)

## 참조 (References)

- [AI/LLMs/RLHF.md](../LLMs/RLHF.md)
- [Reference/Papers.md](../../Reference/Papers.md)
