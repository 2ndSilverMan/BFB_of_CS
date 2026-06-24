# 위험 역량 평가 (Dangerous Capability Evaluation)

- Level: Advanced
- Prerequisites: [AI/AI-Safety/Capability-Evaluation.md](Capability-Evaluation.md), [AI/AI-Safety/Red-Teaming.md](Red-Teaming.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

위험 역량 평가는 모델이 사이버 공격, 생물학적 위해, 사기 자동화, 자율 에이전트 행동, 설득·조작처럼 오용될 수 있는 능력을 어느 정도 갖는지 측정하는 과정이다.

## 직관 (Intuition)

모델이 일반 지식 시험을 잘 보는 것과 위험한 일을 실제로 도울 수 있는 것은 다르다. 위험 역량 평가는 "무엇을 할 수 있나"와 "어떤 조건에서 피해로 이어질 수 있나"를 분리해 본다.

## 이론 (Theory)

평가는 capability, elicitation, safeguards, deployment context를 구분해야 한다. 모델이 latent capability를 갖고 있어도 prompt, tool, scaffolding, fine-tuning 없이는 드러나지 않을 수 있다.

위험 평가는 안전한 sandbox, access control, expert review, dual-use handling을 요구한다. 결과는 release gate, mitigation priority, monitoring plan에 연결되어야 한다.

## 구현 (Implementation)

```python
risk_eval = {
    "domain": "cyber",
    "capability": "vulnerability discovery assistance",
    "tools_allowed": False,
    "human_expert_review": True,
}
```

평가 프롬프트와 결과물은 민감할 수 있으므로 접근 권한과 공개 범위를 제한한다.

## 복잡도 (Complexity)

위험 역량은 domain expert, 안전한 환경, 반복 elicitation이 필요해 비용이 크다. 너무 약한 평가도, 위험 정보를 과도하게 확산하는 평가도 모두 문제가 된다.

## 응용 (Applications)

- frontier model release 평가
- red-team 시나리오 설계
- tool-enabled agent 안전성 검토
- 정책·거버넌스 risk tiering

## 흔한 오해 (Common Misunderstandings)

- 모델이 거절한다고 capability가 없다는 뜻은 아니다.
- Benchmark 점수만으로 실제 오용 가능성을 판단하기 어렵다.
- 안전장치 평가와 base capability 평가는 구분해야 한다.
- 위험 평가는 공개 재현성과 정보 보안 사이 균형이 필요하다.

## TMI

- Elicitation은 모델의 숨은 능력을 끌어내는 평가 절차다.
- Tool access는 위험 역량을 크게 증폭할 수 있다.
- Capability threshold는 배포 단계별 요구 통제를 정하는 데 쓰인다.

## 연습 / 확인 문제 (Exercises)

- 위험 역량 평가에서 tool access를 통제해야 하는 이유를 설명하라.
- Capability와 propensity의 차이를 말하라.
- 공개해도 되는 평가 요약과 제한해야 할 세부 정보를 구분하라.

## 이어서 읽기 (Reading Path)

- 이전: [Capability Evaluation](Capability-Evaluation.md), [Red-Teaming](Red-Teaming.md)
- 다음: [AI Risk Classification](AI-Risk-Classification.md), [AI Regulation](AI-Regulation.md)

## 참조 (References)

- [AI/AI-Safety/Capability-Evaluation.md](Capability-Evaluation.md)
- [Reference/Papers.md](../../Reference/Papers.md)
