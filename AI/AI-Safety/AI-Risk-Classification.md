# AI 위험 분류 체계 (AI Risk Classification)

- Level: Advanced
- Prerequisites: [AI/AI-Safety/Alignment-Overview.md](Alignment-Overview.md), [AI/AI-Safety/Dangerous-Capability-Evaluation.md](Dangerous-Capability-Evaluation.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

AI 위험 분류 체계는 AI 시스템의 위해 가능성을 risk tier로 나누고, 각 tier에 필요한 평가·통제·문서화·승인 절차를 정하는 방법이다. 기술적 위험과 사회적 영향, 배포 맥락을 함께 본다.

## 직관 (Intuition)

스팸 필터와 의료 진단 보조 시스템에 같은 안전 절차를 요구하면 비효율적이고 위험하다. 위험 분류는 "어떤 시스템에 어느 정도의 안전장치가 필요한가"를 결정하는 지도다.

## 이론 (Theory)

위험은 보통 severity, likelihood, exposure, controllability, reversibility로 평가한다. 모델 자체 능력뿐 아니라 사용 목적, 사용자, tool access, autonomy, affected population, failure recoverability가 risk tier를 바꾼다.

분류 체계는 금지/제한, 고위험, 제한적 위험, 낮은 위험처럼 구간화할 수 있다. 단, 같은 모델도 배포 맥락에 따라 위험 등급이 달라질 수 있다.

### 위험은 capability와 context의 함수다

동일한 모델도 어디에 연결되는지에 따라 risk tier가 달라진다. 텍스트 요약 모델이 개인 메모를 정리하는 경우와 의료 기록을 요약해 진료 결정을 보조하는 경우는 영향 범위가 다르다. 따라서 risk classification은 모델 카드만 보지 않고 deployment card를 함께 봐야 한다.

중요 입력은 다음과 같다.

- Domain: 의료, 금융, 고용, 교육, 법률, 인프라 등 권리·안전 영향 영역인가
- Autonomy: 사람이 승인하는가, 모델이 직접 행동하는가
- Tool access: 코드 실행, 외부 메시지, 결제, 데이터 수정 권한이 있는가
- Exposure: 영향을 받는 사용자 수와 취약 집단 여부
- Reversibility: 잘못된 결정이 복구 가능한가
- Evidence: 평가·모니터링·감사 로그가 충분한가

### Tier와 control mapping

Risk tier는 이름표가 아니라 control set을 선택하는 입력이다. 낮은 tier는 기본 문서화와 모니터링이면 충분할 수 있지만, 높은 tier는 독립 평가, adversarial testing, human oversight, incident reporting, post-market monitoring이 필요하다.

예시 mapping은 다음과 같다.

- Low: 기본 모델 카드, 일반 품질 테스트, 사용자 피드백 채널
- Moderate: domain-specific eval, abuse monitoring, release review
- High: 독립 red team, human-in-the-loop, logging, rollback plan, formal approval
- Prohibited or restricted: 출시 금지, 기능 제거, 권한 차단, 법무·윤리 검토

### 규제 프레임워크와 내부 분류

EU AI Act는 위험 기반 접근을 사용하고, unacceptable/high/transparency/minimal risk 같은 구간과 고위험 시스템 의무를 둔다. NIST AI RMF는 자발적 위험관리 프레임워크로, 조직이 AI 위험을 식별·측정·관리하는 절차를 세우는 데 초점을 둔다.

법적 분류와 내부 안전 분류는 일치하지 않을 수 있다. 어떤 시스템이 특정 관할권에서 법적으로 low risk처럼 보이더라도, 조직 내부 threat model에서는 high operational risk일 수 있다. 반대로 법적 의무가 강한 영역은 성능이 좋아도 문서화와 감사를 생략할 수 없다.

규제 문서는 계속 변하므로 운영 문서에는 관할권, 기준일, 제품 버전, 판단 근거를 함께 남긴다.

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

```python
def tier_requires_independent_review(record):
    return (
        record["tier"] in {"high_risk", "restricted"}
        or record["domain"] in {"employment", "healthcare", "law_enforcement"}
        or record["autonomy"] == "fully_autonomous"
    )
```

자동 점수는 triage에 쓰고, 경계 사례는 사람이 판단 근거를 기록해야 한다.

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
