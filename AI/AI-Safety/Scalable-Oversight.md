# Scalable Oversight

- Level: Advanced
- Prerequisites: [AI/AI-Safety/Feedback-Limitations.md](Feedback-Limitations.md), [AI/AI-Safety/Alignment-Overview.md](Alignment-Overview.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

Scalable oversight는 인간이 직접 평가하기 어려운 모델 행동을 더 강한 절차, 도구, 모델 보조, 분해된 검증으로 감독하려는 연구 방향이다.

## 직관 (Intuition)

어려운 증명을 혼자 읽기 어렵다면 여러 검토자에게 부분을 나눠 맡기거나, 다른 AI에게 반례를 찾게 하거나, 형식 검증 도구를 쓸 수 있다. 감독 능력을 확장하는 것이다.

## 이론 (Theory)

대표 접근은 debate, recursive reward modeling, iterated amplification, critique model, process supervision, tool-assisted verification이다. 목표는 인간 판단의 병목을 줄이면서도 모델이 감독 절차를 속이지 못하게 하는 것이다.

핵심 위험은 보조 모델도 같은 오류와 편향을 가질 수 있고, 복잡한 절차가 오히려 검증하기 어려워질 수 있다는 점이다.

### Task decomposition

Scalable oversight의 첫 단계는 어려운 작업을 사람이 검증 가능한 단위로 나누는 것이다. 좋은 분해는 각 하위 주장에 evidence, verifier, failure mode를 붙인다. 나쁜 분해는 하위 작업도 원래 작업만큼 모호하거나, 하위 결과를 합치는 과정에서 오류가 숨어든다.

예를 들어 장문 리서치 답변은 claim extraction, source verification, numerical check, counterargument search, final synthesis로 나눌 수 있다.

### Process supervision

Outcome supervision은 최종 답만 평가한다. Process supervision은 중간 단계가 타당한지 평가한다. 수학, 코드, 도구 사용, 장기 계획처럼 최종 답만 보고는 오류 원인을 알기 어려운 task에서 특히 유용하다.

하지만 process label도 비용이 크고, 모델이 "그럴듯한 과정"을 쓰는 법을 배울 수 있다. 중간 단계 검증은 실제 evidence와 tool log에 연결되어야 한다.

### Debate와 critique의 한계

Debate는 두 모델 또는 두 agent가 서로의 오류를 드러내고 인간이 판정하게 하는 접근이다. Critique model은 답변의 결함을 찾는 보조 모델이다. 둘 다 인간 판정을 돕지만, 다음 실패가 가능하다.

- 두 모델이 같은 blind spot을 공유한다.
- 더 설득력 있는 쪽이 진실한 쪽을 이긴다.
- 인간이 논쟁의 핵심 기술 내용을 이해하지 못한다.
- 절차가 길어져 감사 자체가 어려워진다.

따라서 critique는 독립 evidence, tool verification, adversarial prompt set과 결합해야 한다.

### Oversight의 audit trail

감독 절차가 복잡해질수록 결과뿐 아니라 판단 경로를 남겨야 한다. 어떤 하위 작업이 자동 검증됐고, 어떤 부분이 사람이 판정했으며, 어떤 불확실성이 남았는지 기록해야 사후 분석과 개선이 가능하다.

## 구현 (Implementation)

```python
oversight_pipeline = [
    "decompose task",
    "generate answer",
    "generate critique",
    "verify key claims",
    "human adjudication",
]
```

중요한 주장은 external tool이나 독립 모델로 검증하도록 설계한다.

```python
def oversight_step(claim, verifier, evidence_required):
    return {
        "claim": claim,
        "verifier": verifier,
        "evidence_required": evidence_required,
        "status": "pending",
    }
```

각 claim을 검증 단위로 쪼개면 사람이 최종 답 전체를 한 번에 믿어야 하는 부담이 줄어든다.

## 복잡도 (Complexity)

감독 절차가 늘수록 latency와 비용이 커진다. 여러 모델과 도구가 결합되면 failure mode도 조합적으로 늘어난다.

## 응용 (Applications)

- 장문 답변 검증
- 코드·수학 증명 보조 평가
- 위험 역량 평가
- agent 작업의 중간 단계 감사

## 흔한 오해 (Common Misunderstandings)

- 모델에게 스스로 평가하게 하면 감독 문제가 자동 해결되는 것은 아니다.
- 절차가 복잡할수록 안전한 것은 아니다.
- Critique가 그럴듯해도 실제 오류를 놓칠 수 있다.
- Scalable oversight는 인간 책임을 없애는 것이 아니라 보조한다.

## TMI

- Process supervision은 최종 답뿐 아니라 중간 과정에 피드백을 준다.
- Debate는 두 모델이 서로의 오류를 드러내 인간이 판정하도록 하는 아이디어다.
- Formal verification 가능한 하위문제로 작업을 변환하면 감독이 쉬워질 수 있다.

## 연습 / 확인 문제 (Exercises)

- 복잡한 리서치 답변을 검증 가능한 하위 작업으로 분해하라.
- Debate 방식의 실패 모드를 3개 들어라.
- Process supervision과 outcome supervision을 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [Feedback Limitations](Feedback-Limitations.md)
- 다음: [Superalignment](Superalignment.md), [Dangerous Capability Evaluation](Dangerous-Capability-Evaluation.md)

## 참조 (References)

- [AI/AI-Safety/Feedback-Limitations.md](Feedback-Limitations.md)
- [Reference/Papers.md](../../Reference/Papers.md)
