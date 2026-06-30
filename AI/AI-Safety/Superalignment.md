# 슈퍼정렬 (Superalignment)

- Level: Advanced
- Prerequisites: [AI/AI-Safety/Alignment-Overview.md](Alignment-Overview.md), [AI/AI-Safety/Scalable-Oversight.md](Scalable-Oversight.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

슈퍼정렬은 인간보다 훨씬 강한 AI 시스템이 인간 의도와 제약을 따르도록 만드는 정렬 문제를 가리킨다. 핵심 난점은 인간이 직접 평가하기 어려운 능력과 전략을 가진 시스템을 어떻게 감독할지다.

## 직관 (Intuition)

초등학생이 계산기 답을 검산할 수는 있지만, 자신보다 훨씬 뛰어난 수학자의 증명을 매번 검증하기는 어렵다. 슈퍼정렬은 이 감독 격차가 AI 전반으로 커지는 상황을 다룬다.

## 이론 (Theory)

주요 연구 방향은 scalable oversight, weak-to-strong generalization, interpretability, adversarial evaluation, debate, recursive reward modeling, eliciting latent knowledge 등이다. 공통 질문은 "약한 감독 신호로 강한 모델의 행동을 충분히 제어할 수 있는가"다.

슈퍼정렬은 단일 알고리즘보다 평가, 해석, 훈련, 배포 제한, 거버넌스가 결합된 시스템 문제다.

### 감독 격차의 구조

슈퍼정렬의 어려움은 모델이 단순히 더 빠르거나 더 많은 지식을 갖는다는 데서 끝나지 않는다. 강한 모델은 사람이 직접 확인하기 어려운 계획, 코드, 과학적 주장, 사회적 영향 경로를 만들 수 있다. 이때 인간 피드백은 세 가지 병목에 걸린다.

- 평가자가 정답을 모른다.
- 평가자가 전체 추론 과정을 볼 시간이 없다.
- 평가자가 모델의 숨은 의도나 장기 전략을 알 수 없다.

따라서 supervision은 "사람이 최종 답을 고른다"에서 "사람이 보조 도구와 절차를 사용해 평가 가능성을 높인다"로 확장된다.

### Weak-to-strong generalization

Weak-to-strong 실험은 약한 감독자가 강한 모델의 좋은 일반화를 유도할 수 있는지 보는 축소판이다. 예를 들어 작은 모델이 만든 noisy label로 큰 모델을 학습시킨 뒤, 큰 모델이 약한 라벨의 오류를 넘어서는지 측정한다.

핵심 질문은 다음과 같다.

- 강한 모델이 약한 라벨의 패턴만 모방하는가?
- 약한 감독 신호에서 latent truth를 끌어낼 수 있는가?
- 어느 task family에서 실패가 먼저 나타나는가?
- 강한 모델이 자신의 오류를 드러내는 방향으로 훈련되는가?

### Eliciting latent knowledge

모델이 내부적으로는 사실을 알고 있지만 외부 행동에서는 숨기거나 왜곡할 수 있다는 우려가 있다. Eliciting latent knowledge는 모델 내부 표현이나 보조 질의 절차를 통해 실제로 알고 있는 정보를 끌어낼 수 있는지 묻는다.

이 문제는 해석 가능성과 연결된다. Activation probing, mechanistic interpretability, consistency check, adversarial questioning은 모두 "모델이 무엇을 알고 있고 무엇을 말하고 있는가"의 차이를 줄이는 도구가 될 수 있다.

### 배포 제한과 연구 윤리

슈퍼정렬 연구는 강한 capability를 실험 대상으로 삼기 때문에, 연구 자체도 위험 관리가 필요하다. 고위험 도구 접근, autonomous replication, cyber/biology misuse 가능성이 있는 실험은 sandbox, approval, logging, staged release가 필요하다.

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

```python
def weak_to_strong_eval(weak_score, strong_score, oracle_score):
    imitation_gap = strong_score - weak_score
    remaining_gap = oracle_score - strong_score
    return {
        "improves_over_weak": imitation_gap > 0,
        "distance_to_oracle": remaining_gap,
    }
```

축소 실험은 실제 슈퍼정렬의 충분한 증거가 아니지만, 감독 격차를 분해해 측정하는 출발점이 된다.

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
