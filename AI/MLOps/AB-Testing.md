# A/B 테스트와 섀도우 배포 (A/B Testing and Shadow Deployment)

- Level: Intermediate
- Prerequisites: [Math/Probability-Statistics/Hypothesis-Testing.md](../../Math/Probability-Statistics/Hypothesis-Testing.md), [AI/MLOps/Experiment-Tracking.md](Experiment-Tracking.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

A/B 테스트는 traffic을 무작위로 control과 treatment에 배정해 model·product 변경의 인과 효과를 추정한다. Shadow deployment는 새 모델에 복제 traffic을 보내지만 사용자 응답에는 사용하지 않는다.

## 직관 (Intuition)

Offline metric이 좋아도 실제 사용자 행동·latency·failure가 나빠질 수 있다. A/B는 실제 영향, shadow는 사용자 위험 없이 runtime behavior를 본다.

## 이론 (Theory)

Randomization unit은 user·session·request 중 interference와 carryover를 고려해 정한다. Primary metric, guardrail, sample size, duration, stopping rule을 사전에 정한다. SRM(sample ratio mismatch), novelty, seasonality를 점검한다.

## 구현 (Implementation)

```python
import hashlib


def assign(user_id, experiment):
    key = f"{experiment}:{user_id}".encode()
    bucket = int(hashlib.sha256(key).hexdigest()[:8], 16) % 100
    return "treatment" if bucket < 50 else "control"
```

## 복잡도 (Complexity)

Assignment는 `O(1)`이지만 필요한 sample은 effect size가 작을수록 대략 역제곱으로 증가한다. Shadow는 inference compute를 추가 사용한다.

## 응용 (Applications)

- ranking·recommendation 변경
- model rollout·rollback 결정
- latency·error guardrail
- production data 검증

## 흔한 오해 (Common Misunderstandings)

- p-value만으로 practical significance를 판단하지 않는다.
- request randomization은 같은 user가 두 경험을 오가게 할 수 있다.
- 매일 결과를 보고 임의 중단하면 오류율이 변한다.
- shadow에서 label 기반 user impact를 직접 측정할 수는 없다.

## TMI

- canary는 일부 사용자의 실제 응답에 적용되고 shadow는 응답에 영향이 없다.
- CUPED 같은 variance reduction은 사전 정보를 사용한다.
- interference가 있으면 한 사용자의 treatment가 control 사용자에게 영향을 줄 수 있다.

## 연습 / 확인 문제 (Exercises)

- randomization unit을 선택하고 이유를 설명하라.
- primary·guardrail metric을 정의하라.
- SRM 탐지 시 조사 순서를 작성하라.

## 이어서 읽기 (Reading Path)

- 이전: [실험 추적](Experiment-Tracking.md)
- 다음: [데이터 드리프트](Data-Drift.md)

## 참조 (References)

- [Math/Probability-Statistics/Hypothesis-Testing.md](../../Math/Probability-Statistics/Hypothesis-Testing.md)
- [Reference/Books.md](../../Reference/Books.md)
