# RLHF와 Constitutional AI

- Level: Advanced
- Prerequisites: [Reward-Hacking.md](Reward-Hacking.md), [AI/NLP/GPT.md](../NLP/GPT.md), [AI/Reinforcement-Learning/Policy.md](../Reinforcement-Learning/Policy.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

RLHF(Reinforcement Learning from Human Feedback)는 인간 선호 데이터를 사용해 모델의 응답을 더 유용하고 안전하게 조정하는 방법론이다. Constitutional AI는 명시적 원칙 집합을 사용해 모델이 스스로 비판·수정하거나 선호 데이터를 생성하도록 돕는 접근이다.

## 직관 (Intuition)

언어 모델은 다음 토큰 예측만으로도 많은 지식을 배우지만, “사람이 원하는 답변 방식”은 별도의 신호가 필요하다. RLHF는 사람이 더 나은 답변을 고르는 비교 데이터를 주고, 모델이 그 선호를 따르도록 훈련한다. Constitutional AI는 매번 인간이 판단하기 어려운 부분을 원칙 기반 피드백으로 보완하려는 시도다.

## 이론 (Theory)

전형적인 RLHF 파이프라인은 다음 단계로 설명된다.

1. 사전학습 모델을 instruction data로 supervised fine-tuning한다.
2. 같은 prompt에 대한 여러 응답을 만들고 인간 선호 비교를 수집한다.
3. 선호 데이터를 이용해 reward model $r_\phi(x,y)$을 학습한다.
4. 정책 모델이 reward model 점수를 높이도록 최적화한다.
5. 안전 평가와 red-teaming으로 부작용을 점검한다.

Constitutional AI는 인간 피드백 일부를 원칙 기반 critique와 revision으로 대체하거나 보강한다. 핵심은 “어떤 원칙을 쓰는가”, “원칙이 충돌할 때 어떻게 판단하는가”, “모델이 원칙을 피상적으로만 따르지 않는가”를 계속 평가하는 것이다.

### Preference model의 의미

선호 모델은 "정답"을 학습하는 모델이 아니라 특정 지침과 라벨러 집단이 더 선호한 응답의 패턴을 학습한다. 따라서 reward model score는 사실성, 안전성, 친절함, 간결함, 문체 선호가 뒤섞인 proxy다.

선호 데이터 품질은 다음 요소에 크게 좌우된다.

- Prompt 분포가 실제 사용과 고위험 사례를 포함하는가
- Chosen/rejected 차이가 명확하고 지침과 일관되는가
- 라벨러가 필요한 전문성을 갖고 있는가
- 안전 거절과 유용한 대안 제시가 함께 평가되는가
- Reward model holdout이 policy optimization에 오염되지 않았는가

### Policy optimization과 KL 제약

RLHF에서 정책을 reward model에 맞춰 너무 강하게 최적화하면 reward model의 취약점을 파고들 수 있다. 그래서 기준 모델(reference model)에서 너무 멀어지지 않도록 KL penalty를 둔다.

$$
\max_\pi E[r_\phi(x,y)] - \beta KL(\pi(\cdot\mid x)\|\pi_{ref}(\cdot\mid x))
$$

KL 제약은 완전한 안전장치가 아니다. Reference model 자체의 결함도 남고, reward model이 선호하는 피상적 패턴으로 drift할 수 있다. 하지만 과격한 policy shift를 줄이는 실용적 제어 장치다.

### Constitutional AI의 평가 포인트

Constitutional AI에서 원칙은 라벨러를 대체하는 자동 진리표가 아니다. 원칙 간 충돌, 문화·도메인 차이, 애매한 요청에서의 우선순위가 필요하다. 좋은 constitution은 다음 속성을 가져야 한다.

- 적용 범위와 예외가 명확하다.
- 원칙 충돌 시 tie-break rule이 있다.
- 모델 자기비판이 실제 오류 수정으로 이어지는지 측정한다.
- 원칙을 말로만 언급하고 행동은 바뀌지 않는지 red team한다.

### PPO, DPO, RLAIF의 위치

PPO 기반 RLHF는 reward model을 학습한 뒤 정책을 강화학습으로 최적화한다. DPO류 방법은 preference pair에서 직접 정책을 업데이트해 파이프라인을 단순화한다. RLAIF는 인간 대신 AI 피드백을 사용해 비용을 줄일 수 있지만, 평가자의 편향과 오류가 증폭될 수 있다.

방법이 달라도 공통 위험은 같다. 선호 데이터가 무엇을 대표하는지, reward/proxy를 얼마나 최적화했는지, holdout human evaluation이 유지되는지 봐야 한다.

## 구현 (Implementation)

선호 데이터는 보통 쌍대 비교 형태로 저장한다.

```python
preference_example = {
    "prompt": "복잡한 개념을 간단히 설명해 줘.",
    "chosen": "핵심 직관을 먼저 말하고 예시를 붙인 답변",
    "rejected": "정의만 길게 나열한 답변",
    "reason": "chosen이 더 명확하고 사용자의 요청에 맞음",
}


def preference_loss(chosen_score, rejected_score):
    # Bradley-Terry 스타일 로지스틱 손실의 형태
    import math
    return math.log(1 + math.exp(-(chosen_score - rejected_score)))
```

실제 학습은 대규모 데이터, 품질 관리, policy optimization, safety evaluation이 결합된 파이프라인이다.

```python
def preference_record_ok(example):
    return all([
        example.get("prompt"),
        example.get("chosen"),
        example.get("rejected"),
        example.get("rubric_id"),
        example["chosen"] != example["rejected"],
    ])
```

데이터 스키마에 `rubric_id`, `risk_domain`, `annotator_expertise`, `disagreement_reason`을 남기면 나중에 reward model 실패를 추적하기 쉽다.

## 복잡도 (Complexity)

RLHF의 비용은 인간 라벨링, reward model 학습, 정책 최적화, 반복 평가에서 발생한다. 선호 데이터 품질이 낮거나 라벨러 지침이 불명확하면 모델이 모순된 신호를 학습할 수 있다. Constitutional AI는 인간 라벨 비용을 줄일 수 있지만, 원칙 설계와 검증 비용이 생긴다.

## 응용 (Applications)

- 대화형 LLM의 지시 따르기와 안전성 개선
- 요약, 코딩, 질의응답의 선호 최적화
- 유해 요청 거절과 안전한 대안 제시
- 원칙 기반 모델 자기비판과 답변 수정

## 흔한 오해 (Common Misunderstandings)

- RLHF는 모델을 완전히 안전하게 만드는 마법 버튼이 아니다.
- reward model은 인간 선호의 근사치일 뿐이며, 자체적으로 보상 해킹 대상이 될 수 있다.
- Constitutional AI에서 “헌법”은 보편적으로 정해진 하나의 문서가 아니라 설계된 원칙 집합이다.
- 선호 최적화는 사실성, 최신성, 논리성을 자동으로 보장하지 않는다.

## TMI

- PPO 외에도 DPO류 직접 선호 최적화 방법들이 널리 연구된다.
- 선호 데이터는 답변 스타일을 크게 바꿀 수 있어 모델의 주관적 품질 체감에 큰 영향을 준다.
- 안전한 거절은 단순 거부가 아니라, 가능한 경우 사용자의 합법적·안전한 목표를 돕는 방향을 포함해야 한다.

## 연습 / 확인 문제 (Exercises)

- RLHF 파이프라인에서 reward hacking이 생길 수 있는 지점을 두 곳 찾으라.
- Constitutional AI의 원칙이 서로 충돌하는 예를 만들어라.
- “도움됨”과 “안전함” 사이 trade-off를 평가 데이터로 어떻게 포착할지 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [보상 해킹](Reward-Hacking.md)
- 다음: [인간 피드백의 한계](Feedback-Limitations.md), [기계적 해석 가능성](Mechanistic-Interpretability.md)

## 참조 (References)

- [Reward-Hacking.md](Reward-Hacking.md)
- [AI/NLP/GPT.md](../NLP/GPT.md)
- [AI/Reinforcement-Learning/Policy.md](../Reinforcement-Learning/Policy.md)
- [Reference/Books.md](../../Reference/Books.md)
