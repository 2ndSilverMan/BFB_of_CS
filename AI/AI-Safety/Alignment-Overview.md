# AI 정렬 문제 개요 (Alignment Overview)

- Level: Advanced
- Prerequisites: [AI/Deep-Learning/Transformer.md](../Deep-Learning/Transformer.md), [AI/Theoretical-ML/Generalization-Bounds.md](../Theoretical-ML/Generalization-Bounds.md), [AI/Causal-Inference/SCM.md](../Causal-Inference/SCM.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

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

### 정렬 실패의 층위

정렬 실패는 "모델이 나쁜 답을 했다"로만 묶으면 원인 분석이 어렵다. 보통 다음 층위를 분리해 본다.

- Specification failure: 목표·정책·보상·프롬프트가 의도를 제대로 표현하지 못한다.
- Generalization failure: 훈련 분포에서는 안전했지만 새로운 상황에서 목표가 다르게 일반화된다.
- Oversight failure: 인간 또는 평가 시스템이 모델 행동의 품질과 위험을 제대로 판정하지 못한다.
- Control failure: 문제가 발견되어도 중단, 수정, 권한 축소, 롤백이 어렵다.
- Governance failure: 누가 어떤 기준으로 출시·감사·사후 대응을 결정하는지 불명확하다.

이 구분은 대응책을 다르게 만든다. 보상 설계 문제에는 reward audit가 필요하고, 감독 실패에는 scalable oversight가 필요하며, 통제 실패에는 권한 경계와 kill switch가 필요하다.

### 시스템 경계와 threat model

정렬은 모델 가중치만의 문제가 아니라 시스템 경계의 문제다. 같은 LLM도 검색만 하는 도구인지, 코드 실행 권한이 있는 에이전트인지, 결제·배포·메시징 권한을 가진 운영 시스템인지에 따라 위험이 달라진다.

Threat model에는 최소한 다음을 적는다.

- 모델이 접근할 수 있는 도구와 데이터
- 사용자가 유도할 수 있는 목표와 입력 분포
- 실패했을 때 영향을 받는 사람과 자산
- 사람이 개입할 수 있는 지점과 지연 시간
- 로그, 감사, 롤백, 권한 회수 절차

정렬 평가는 이 경계 안에서 수행해야 한다. sandbox 없는 tool-use agent를 단순 질의응답 benchmark로만 평가하면 실제 위험을 놓친다.

### Defense in depth

안전한 시스템은 하나의 필터에 의존하지 않는다. 사전학습 데이터 정제, instruction tuning, preference optimization, 정책 필터, tool permission, runtime monitor, incident response가 겹겹이 작동해야 한다. 각 방어층은 서로 다른 실패를 잡도록 설계한다.

중요한 원칙은 "성능 metric과 안전 metric을 분리해 추적한다"는 것이다. 모델이 더 유용해지는 과정에서 권한·자율성·사용자 신뢰도도 함께 커지므로, 유용성 상승은 안전 검증의 대체물이 아니라 추가 검증의 신호다.

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

```python
def release_gate(report):
    required = [
        report.objective_spec_reviewed,
        report.red_team_regressions_passed,
        report.high_risk_tools_scoped,
        report.human_override_tested,
        report.incident_owner_assigned,
    ]
    return all(required) and report.residual_risk in {"low", "accepted"}
```

출시 gate는 "모든 위험이 0"이라는 뜻이 아니라 남은 위험이 문서화되고 책임자가 승인했다는 뜻이어야 한다.

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
