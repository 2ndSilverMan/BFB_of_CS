# AI 위험 분류 체계 (AI Risk Classification)

- Level: Advanced
- Prerequisites: [AI/AI-Safety/Alignment-Overview.md](Alignment-Overview.md), [AI/AI-Safety/Dangerous-Capability-Evaluation.md](Dangerous-Capability-Evaluation.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

AI 위험 분류 체계는 AI 시스템의 위해 가능성을 risk tier로 나누고, 각 tier에 필요한 평가·통제·문서화·승인 절차를 정하는 방법이다. 기술적 위험과 사회적 영향, 배포 맥락을 함께 본다.

## 직관 (Intuition)

스팸 필터와 의료 진단 보조 시스템에 같은 안전 절차를 요구하면 비효율적이고 위험하다. 위험 분류는 "어떤 시스템에 어느 정도의 안전장치가 필요한가"를 결정하는 지도다.

## 이론 (Theory)

위험은 보통 severity, likelihood, exposure, controllability, reversibility로 평가한다. 모델 자체 능력뿐 아니라 사용 목적, 사용자, tool access, autonomy, affected population, failure recoverability가 risk tier를 바꾼다.

분류 체계는 금지/제한, 고위험, 제한적 위험, 낮은 위험처럼 구간화할 수 있다. 단, 같은 모델도 배포 맥락에 따라 위험 등급이 달라질 수 있다.

## 구현 (Implementation)

```python
risk_record = {
    "capability": "high",
    "domain": "employment",
    "autonomy": "human-in-the-loop",
    "impact": "rights_affecting",
    "tier": "high_risk",
}
```

Risk tier는 평가 깊이, release approval, monitoring 강도를 결정한다.

## 복잡도 (Complexity)

정량 점수화는 비교를 쉽게 하지만 false precision을 만들 수 있다. 경계 사례는 전문가 검토와 문서화가 필요하다.

## 응용 (Applications)

- 모델 출시 gate
- 위험 역량 평가 우선순위
- 규제 준수 mapping
- 내부 AI governance process

## 흔한 오해 (Common Misunderstandings)

- 모델 크기만으로 위험 등급을 정할 수 없다.
- 낮은 위험 등급이 무위험을 뜻하지 않는다.
- 분류는 한 번 하고 끝나는 것이 아니라 배포 후 갱신해야 한다.
- Risk tier는 법률 분류와 내부 안전 분류가 다를 수 있다.

## TMI

- EU AI Act도 위험 기반 접근을 사용한다.
- NIST AI RMF 같은 프레임워크는 조직의 risk management 과정에 AI 특성을 통합하려 한다.
- Incident database는 risk taxonomy를 현실 사례로 업데이트하는 데 도움을 준다.

## 연습 / 확인 문제 (Exercises)

- 같은 LLM을 검색 보조와 의료 triage에 쓸 때 risk tier를 비교하라.
- Risk scoring rubric을 설계하라.
- Tier 변경을 유발하는 배포 조건을 정리하라.

## 이어서 읽기 (Reading Path)

- 이전: [Dangerous Capability Evaluation](Dangerous-Capability-Evaluation.md)
- 다음: [AI Regulation](AI-Regulation.md), [Fairness & Bias](Fairness-Bias.md)

## 참조 (References)

- [AI/AI-Safety/Dangerous-Capability-Evaluation.md](Dangerous-Capability-Evaluation.md)
- [Reference/Books.md](../../Reference/Books.md)
