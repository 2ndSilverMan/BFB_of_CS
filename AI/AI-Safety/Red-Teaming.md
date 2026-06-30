# Red-Teaming 방법론 (Red-Teaming)

- Level: Advanced
- Prerequisites: [Capability-Evaluation.md](Capability-Evaluation.md), [Reward-Hacking.md](Reward-Hacking.md), [Engineering/Security/Web-Security.md](../../Engineering/Security/Web-Security.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

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

### 범위와 규칙

Red team은 시작 전에 scope를 명확히 해야 한다. 모델 단독인지, 제품 UI와 tool integration까지 포함하는지, 허용된 테스트 강도와 금지된 데이터 접근이 무엇인지 정한다. 범위가 없으면 위험을 놓치거나 불필요한 피해를 만들 수 있다.

좋은 scope 문서는 다음을 포함한다.

- 평가 대상 모델·버전·system prompt·tool 권한
- 허용되는 테스트 유형과 금지되는 행위
- 민감 데이터 처리와 기록 보존 정책
- severity rubric과 escalation path
- 테스트 종료 조건과 재검증 절차

### Severity와 reproducibility

실패 사례는 흥미로움이 아니라 위험 기준으로 우선순위를 매긴다. Severity는 피해 크기, 악용 가능성, affected population, 권한 수준, 완화 가능성으로 평가한다. Reproducibility는 같은 조건에서 실패가 다시 나타나는지를 본다.

재현이 어려운 단발 사례도 버리지 않는다. 고영향 위험이면 prompt family, decoding 설정, 모델 버전, 주변 맥락을 기록해 cluster로 추적한다.

### 자동 red team과 인간 red team

자동화는 coverage와 regression test에 강하다. 인간 red team은 새로운 시나리오, 모호한 정책 경계, 사회적 맥락을 더 잘 탐색한다. 두 접근은 대체재가 아니라 보완재다.

자동 red team 결과는 false positive와 false negative가 있으므로, 고위험 finding은 사람이 triage하고, 사람이 발견한 대표 실패는 regression suite에 편입한다.

### 완화 후 재검증

Red team finding은 보고서에서 끝나지 않는다. 정책 수정, 데이터 보강, guardrail 변경, tool permission 조정, UI 경고, 모니터링 rule 추가 중 어떤 완화가 적용됐는지 기록하고, 같은 실패와 주변 변형을 다시 평가한다.

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

```python
def prioritize_finding(finding):
    severity_rank = {"low": 1, "medium": 2, "high": 3, "critical": 4}
    base = severity_rank[finding["severity"]]
    if finding["reproducible"]:
        base += 1
    if finding.get("tool_access_required"):
        base += 1
    return base
```

우선순위 점수는 triage 보조일 뿐이고, critical finding은 점수와 무관하게 즉시 escalation한다.

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
