# Scalable Oversight

- Level: Advanced
- Prerequisites: [AI/AI-Safety/Feedback-Limitations.md](Feedback-Limitations.md), [AI/AI-Safety/Alignment-Overview.md](Alignment-Overview.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

Scalable oversight는 인간이 직접 평가하기 어려운 모델 행동을 더 강한 절차, 도구, 모델 보조, 분해된 검증으로 감독하려는 연구 방향이다.

## 직관 (Intuition)

어려운 증명을 혼자 읽기 어렵다면 여러 검토자에게 부분을 나눠 맡기거나, 다른 AI에게 반례를 찾게 하거나, 형식 검증 도구를 쓸 수 있다. 감독 능력을 확장하는 것이다.

## 이론 (Theory)

대표 접근은 debate, recursive reward modeling, iterated amplification, critique model, process supervision, tool-assisted verification이다. 목표는 인간 판단의 병목을 줄이면서도 모델이 감독 절차를 속이지 못하게 하는 것이다.

핵심 위험은 보조 모델도 같은 오류와 편향을 가질 수 있고, 복잡한 절차가 오히려 검증하기 어려워질 수 있다는 점이다.

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
