# 슈퍼정렬 (Superalignment)

- Level: Advanced
- Prerequisites: [AI/AI-Safety/Alignment-Overview.md](Alignment-Overview.md), [AI/AI-Safety/Scalable-Oversight.md](Scalable-Oversight.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

슈퍼정렬은 인간보다 훨씬 강한 AI 시스템이 인간 의도와 제약을 따르도록 만드는 정렬 문제를 가리킨다. 핵심 난점은 인간이 직접 평가하기 어려운 능력과 전략을 가진 시스템을 어떻게 감독할지다.

## 직관 (Intuition)

초등학생이 계산기 답을 검산할 수는 있지만, 자신보다 훨씬 뛰어난 수학자의 증명을 매번 검증하기는 어렵다. 슈퍼정렬은 이 감독 격차가 AI 전반으로 커지는 상황을 다룬다.

## 이론 (Theory)

주요 연구 방향은 scalable oversight, weak-to-strong generalization, interpretability, adversarial evaluation, debate, recursive reward modeling, eliciting latent knowledge 등이다. 공통 질문은 "약한 감독 신호로 강한 모델의 행동을 충분히 제어할 수 있는가"다.

슈퍼정렬은 단일 알고리즘보다 평가, 해석, 훈련, 배포 제한, 거버넌스가 결합된 시스템 문제다.

## 구현 (Implementation)

```python
research_program = [
    "train strong model with weak labels",
    "measure where supervision fails",
    "add oversight aids",
    "stress-test under distribution shift",
]
```

현실의 연구는 toy setting에서 실패 모드를 분리해 측정하는 것부터 시작한다.

## 복잡도 (Complexity)

모델 역량이 커질수록 평가 데이터 생성, red-teaming, interpretability 분석, 안전한 실험 환경 비용이 커진다. 가장 어려운 부분은 실패가 드물고 고영향일 수 있다는 점이다.

## 응용 (Applications)

- frontier model 안전성 연구
- 고위험 agent 배포 검토
- 강한 모델의 자기평가·상호검증 설계
- 해석 가능성 기반 감시

## 흔한 오해 (Common Misunderstandings)

- 슈퍼정렬은 단지 더 친절한 챗봇을 만드는 문제가 아니다.
- 인간보다 강한 모델이 항상 인간에게 설명 가능한 답을 주는 것은 아니다.
- 평가 benchmark 점수가 높아도 deceptive behavior 가능성을 배제하지 못한다.
- 감독 자동화는 감독 실패도 자동화할 수 있다.

## TMI

- Weak-to-strong 실험은 약한 모델이 만든 라벨로 강한 모델을 통제할 수 있는지 보는 축소판이다.
- Debate와 amplification은 인간 판단을 보조하는 절차 설계에 가깝다.
- 슈퍼정렬 논의는 기술 연구와 배포 거버넌스를 분리하기 어렵다.

## 연습 / 확인 문제 (Exercises)

- 인간이 직접 평가하기 어려운 AI output 예시를 들어라.
- Weak-to-strong generalization 실험을 작은 분류 문제로 설계하라.
- 슈퍼정렬에서 interpretability가 필요한 이유를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [AI 정렬 개요](Alignment-Overview.md)
- 다음: [Scalable Oversight](Scalable-Oversight.md), [위험 역량 평가](Dangerous-Capability-Evaluation.md)

## 참조 (References)

- [AI/AI-Safety/Alignment-Overview.md](Alignment-Overview.md)
- [Reference/Papers.md](../../Reference/Papers.md)
