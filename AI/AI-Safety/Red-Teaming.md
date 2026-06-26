# Red-Teaming 방법론 (Red-Teaming)

- Level: Advanced
- Prerequisites: [Capability-Evaluation.md](Capability-Evaluation.md), [Reward-Hacking.md](Reward-Hacking.md), [Engineering/Security/Web-Security.md](../../Engineering/Security/Web-Security.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

AI red-teaming은 모델이나 AI 시스템이 안전 요구사항을 위반하는 방식으로 행동할 수 있는지 체계적으로 탐색하는 평가 방법이다. 목적은 피해를 만들기 위한 것이 아니라, 배포 전에 실패 모드를 발견하고 완화하는 것이다.

## 직관 (Intuition)

일반 테스트가 “정상 사용자가 잘 쓸 수 있는가”를 본다면, red-teaming은 “영리하고 끈질긴 사용자가 빈틈을 찾으면 어떻게 되는가”를 본다. 좋은 red team은 단순히 모델을 괴롭히는 팀이 아니라, 실패를 재현 가능한 증거로 남기고 방어 개선까지 연결하는 팀이다.

## 이론 (Theory)

AI red-teaming은 다음 요소를 포함한다.

- 범위 정의: 평가할 모델, 도구, 정책, 금지 영역, 허용된 테스트 방식
- 위험 분류: 유해 조언, 프라이버시, 보안, 차별, 허위정보, 과도한 자율성 등
- 시나리오 설계: 실제 사용자 맥락과 악용 가능성을 반영한 테스트
- 증거 기록: prompt, response, 환경, 모델 버전, severity, 재현성
- 완화와 재검증: 정책, 데이터, 모델, product guardrail 수정 후 재평가

Red-teaming은 benchmark와 다르게 열린 탐색을 포함한다. 따라서 정량 점수와 정성 사례 분석을 함께 다룬다.

## 구현 (Implementation)

테스트 케이스는 구조화된 형태로 남겨야 재현과 수정이 가능하다.

```python
red_team_case = {
    "risk_area": "privacy",
    "scenario": "사용자가 타인의 민감 정보를 추론하려는 상황",
    "prompt": "<test prompt redacted or summarized>",
    "expected_policy": "민감 정보 추론을 돕지 않고 안전한 대안을 제시",
    "observed_behavior": "model response summary",
    "severity": "medium",
    "reproducible": True,
}
```

민감한 공격 세부사항은 접근 권한과 기록 정책을 분리하고, 외부 공유 시 요약·비식별화한다.

## 복잡도 (Complexity)

Red-teaming은 사람 시간과 반복 비용이 크다. 모델 버전, decoding 설정, system prompt, tool 권한이 바뀌면 결과도 달라질 수 있어 회귀 테스트가 필요하다. 고위험 시스템은 독립 팀과 staged rollout이 바람직하다.

## 응용 (Applications)

- LLM 안전 정책 검증
- 도구 사용 에이전트의 권한 남용 테스트
- 출시 전 위험 사례 발견
- 사고 대응 후 재발 방지 테스트

## 흔한 오해 (Common Misunderstandings)

- Red-teaming은 일회성 이벤트가 아니라 반복 프로세스다.
- 실패 사례를 많이 찾는 것만으로 충분하지 않다. severity와 완화 우선순위가 필요하다.
- 자동 평가만으로 창의적인 악용 시나리오를 모두 포착하기 어렵다.
- 안전 정책을 우회하는 구체적 방법을 널리 공유하면 오히려 위험을 키울 수 있다.

## TMI

- 좋은 red team 보고서는 “어떻게 실패했는가”뿐 아니라 “어떤 완화가 효과 있었는가”를 포함한다.
- 모델 단독 평가와 제품 전체 평가를 분리해야 한다. UI, memory, retrieval, tools가 위험을 바꾼다.
- 익명화된 실패 사례 taxonomy는 장기적으로 평가 세트를 성장시키는 씨앗이 된다.

## 연습 / 확인 문제 (Exercises)

- AI red-teaming의 범위 문서에 들어가야 할 항목을 5개 쓰라.
- severity와 likelihood를 분리해 위험 우선순위를 매기는 이유를 설명하라.
- red-team 실패 사례를 regression test로 바꾸는 절차를 설계하라.

## 이어서 읽기 (Reading Path)

- 이전: [AI 역량 평가](Capability-Evaluation.md)
- 다음: [Scalable Oversight](Scalable-Oversight.md), [AI 규제 프레임워크](AI-Regulation.md)

## 참조 (References)

- [Capability-Evaluation.md](Capability-Evaluation.md)
- [Reward-Hacking.md](Reward-Hacking.md)
- [Engineering/Security/Web-Security.md](../../Engineering/Security/Web-Security.md)
- [Reference/Books.md](../../Reference/Books.md)
