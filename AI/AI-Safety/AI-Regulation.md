# AI 규제 프레임워크 (AI Regulation Frameworks)

- Level: Advanced
- Prerequisites: [AI/AI-Safety/AI-Risk-Classification.md](AI-Risk-Classification.md), [AI/AI-Safety/Fairness-Bias.md](Fairness-Bias.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

AI 규제 프레임워크는 AI 시스템의 위험을 줄이고 책임, 투명성, 안전, 인권 보호를 확보하기 위한 법·표준·가이드라인의 조합이다. 이 문서는 법률 자문이 아니라 기술자가 규제 문서를 읽고 내부 안전 프로세스와 연결하는 법을 설명한다.

## 직관 (Intuition)

규제는 "모델을 쓰지 말라"가 아니라 "위험한 용도일수록 더 강한 증거, 문서, 감독, 책임을 요구하라"는 운영 체계에 가깝다. 같은 모델도 채팅 장난감인지 채용·의료·금융 의사결정인지에 따라 요구가 달라진다.

## 이론 (Theory)

2026-06-23에 확인한 공식 자료 기준, EU AI Act는 위험 기반 접근을 사용하며 unacceptable, high, transparency/limited, minimal/no risk 같은 층위를 둔다. EU 집행위 설명에 따르면 AI Act는 2024-08-01 발효되었고, 금지 관행과 AI literacy 의무는 2025-02-02부터, 거버넌스 규칙과 GPAI 모델 의무는 2025-08-02부터 적용되었다. 전체 적용 기준일은 2026-08-02이지만, high-risk 시스템 중 일부는 전환 기간이 더 길다. 2026-06 기준 집행위 안내는 특정 high-risk 영역은 2027-12-02, 제품에 통합된 high-risk 시스템은 2028-08-02 적용을 안내한다.

NIST AI RMF는 자발적 프레임워크로 AI 위험을 조직의 설계, 개발, 사용, 평가 과정에 통합하도록 돕는다. OECD AI Principles는 인권, 민주적 가치, 투명성, 강건성, 책임성을 trustworthy AI의 핵심 원칙으로 둔다.

## 구현 (Implementation)

```python
compliance_map = {
    "system_purpose": "employment screening",
    "risk_tier": "high",
    "required_controls": ["risk_management", "data_governance", "logging", "human_oversight"],
    "evidence": ["model_card", "eval_report", "incident_process"],
}
```

실제 적용은 관할권, 산업, 제품 책임, 개인정보, 고용·의료·금융 등 분야별 법과 함께 검토해야 한다.

## 복잡도 (Complexity)

규제 준수는 모델 평가만이 아니라 데이터 거버넌스, 문서화, human oversight, incident reporting, vendor management, post-market monitoring을 포함한다. 국가와 지역별 요구가 달라 cross-jurisdiction mapping이 필요하다.

## 응용 (Applications)

- AI product release checklist
- high-risk use case 검토
- model card·system card 작성
- 내부 감사와 incident response

## 흔한 오해 (Common Misunderstandings)

- 오픈소스 모델을 쓴다고 규제 책임이 자동으로 사라지지 않는다.
- 기술 benchmark 점수는 규제 준수 증거의 일부일 뿐이다.
- "Human-in-the-loop"는 이름만 붙인다고 충분하지 않고 실제 권한과 역량이 필요하다.
- 규제는 빠르게 변하므로 문서 작성 시점과 출처를 남겨야 한다.

## TMI

- Risk-based regulation은 시스템의 용도와 영향받는 사람을 함께 본다.
- GPAI처럼 범용 모델은 downstream use가 다양해 transparency와 systemic risk 관리가 중요해진다.
- 표준과 code of practice는 법적 요구를 실무 절차로 번역하는 다리 역할을 한다.

## 연습 / 확인 문제 (Exercises)

- AI 시스템 하나를 골라 risk tier와 필요한 evidence를 작성하라.
- Human oversight가 실질적이려면 어떤 권한과 로그가 필요한지 설명하라.
- 규제 요구를 MLOps release gate로 바꾸는 체크리스트를 설계하라.

## 이어서 읽기 (Reading Path)

- 이전: [AI Risk Classification](AI-Risk-Classification.md)
- 다음: [Fairness & Bias](Fairness-Bias.md), [Model Monitoring](../MLOps/Model-Monitoring.md)

## 참조 (References)

- [European Commission — AI Act](https://digital-strategy.ec.europa.eu/en/policies/regulatory-framework-ai)
- [NIST — AI Risk Management Framework](https://www.nist.gov/itl/ai-risk-management-framework)
- [OECD — AI Principles](https://oecd.ai/en/ai-principles)
