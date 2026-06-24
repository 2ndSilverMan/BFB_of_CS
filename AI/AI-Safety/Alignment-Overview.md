# AI 정렬 문제 개요 (Alignment Overview)

- Level: Advanced
- Prerequisites: [AI/Deep-Learning/Transformer.md](../Deep-Learning/Transformer.md), [AI/Theoretical-ML/Generalization-Bounds.md](../Theoretical-ML/Generalization-Bounds.md), [AI/Causal-Inference/SCM.md](../Causal-Inference/SCM.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

AI 정렬은 AI 시스템의 실제 행동이 인간의 의도, 가치, 제약, 사회적 맥락과 일관되도록 만드는 문제다. 단순히 훈련 목표를 잘 최적화하는 것을 넘어, 새로운 상황에서도 유해한 부작용 없이 의도한 목적을 따르게 하는 것이 핵심이다.

## 직관 (Intuition)

“문제를 해결하라”는 지시와 “사람이 납득할 수 있고 안전한 방식으로 문제를 해결하라”는 지시는 다르다. 강한 최적화 능력을 가진 시스템은 우리가 적어둔 보상이나 프롬프트의 빈틈을 찾아낼 수 있다. 정렬 문제는 그 빈틈을 줄이고, 시스템이 애매한 상황에서도 올바른 방향으로 행동하게 만드는 작업이다.

## 이론 (Theory)

정렬 문제는 여러 층으로 나뉜다.

- 외부 정렬(outer alignment): 명시한 목표가 정말 원하는 목표인가?
- 내부 정렬(inner alignment): 학습된 모델 내부의 실제 목표가 훈련 목표와 일치하는가?
- 견고성(robustness): 분포 이동, 적대적 입력, 긴 작업 체인에서도 안전한가?
- 감독 가능성(oversight): 인간이 모델의 행동과 이유를 충분히 평가할 수 있는가?
- 수정 가능성(corrigibility): 시스템이 인간의 수정, 중단, 제약을 받아들이는가?

현대 AI 시스템은 사전학습, 미세조정, 인간 피드백, 도구 사용, 에이전트 루프가 결합되므로 정렬도 단일 알고리즘이 아니라 데이터, 목표 설계, 평가, 모니터링, 거버넌스의 조합으로 다뤄야 한다.

## 구현 (Implementation)

정렬 검토는 개발 프로세스에 체크리스트로 들어갈 수 있다.

```python
def alignment_review(system):
    checks = {
        "objective_matches_intent": system.has_clear_objective,
        "known_failure_modes_tested": len(system.red_team_cases) > 0,
        "human_override_available": system.has_shutdown_or_override,
        "distribution_shift_evaluated": system.has_ood_eval,
        "monitoring_enabled": system.has_runtime_monitoring,
    }
    return checks, all(checks.values())
```

현실의 체크리스트는 훨씬 구체적이어야 하며, 위험도가 큰 기능일수록 독립 평가와 출시 후 모니터링이 필요하다.

## 복잡도 (Complexity)

정렬은 단일 계산 문제가 아니라 시스템 안전 문제다. 데이터 수집, reward modeling, 평가, red-teaming, 해석 가능성 분석, 운영 모니터링이 모두 비용을 만든다. 특히 모델 역량이 커질수록 인간 평가가 따라가기 어려워지는 scalable oversight 문제가 커진다.

## 응용 (Applications)

- LLM과 에이전트의 안전한 배포
- 인간 피드백 기반 모델 정렬
- 위험 역량 평가와 red-teaming
- 해석 가능성과 감사 가능성 설계

## 흔한 오해 (Common Misunderstandings)

- 정렬은 “모델이 친절한 말투를 쓰게 하는 것”보다 훨씬 넓다.
- 안전 필터만 붙이면 정렬 문제가 해결되는 것은 아니다.
- 훈련 데이터에 좋은 행동 예시가 많아도 분포 밖 상황에서 안전하다는 보장은 없다.
- 높은 benchmark 성능은 목표 이해와 안전 행동을 자동으로 보장하지 않는다.

## TMI

- specification gaming은 외부 정렬 실패의 고전적 신호다.
- mesa-optimizer 논의는 학습된 내부 최적화 과정이 명시 목표와 다를 수 있다는 우려를 다룬다.
- 정렬 연구는 기술 문제와 제도적 문제를 동시에 포함한다.

## 연습 / 확인 문제 (Exercises)

- 외부 정렬 실패와 내부 정렬 실패의 예를 각각 하나씩 들어라.
- “정확하지만 해로운 답변”이 생기는 상황을 목표 설계 관점에서 설명하라.
- 출시 전 평가와 출시 후 모니터링이 모두 필요한 이유를 정리하라.

## 이어서 읽기 (Reading Path)

- 이전: [AI/Theoretical-ML/](../Theoretical-ML/)
- 다음: [보상 해킹](Reward-Hacking.md), [슈퍼정렬](Superalignment.md), [AI 위험 분류](AI-Risk-Classification.md)

## 참조 (References)

- [AI/Theoretical-ML/Generalization-Bounds.md](../Theoretical-ML/Generalization-Bounds.md)
- [AI/Causal-Inference/SCM.md](../Causal-Inference/SCM.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
