# AI 역량 평가 (Capability Evaluation)

- Level: Advanced
- Prerequisites: [Alignment-Overview.md](Alignment-Overview.md), [AI/MLOps/Model-Monitoring.md](../MLOps/Model-Monitoring.md), [AI/Machine-Learning/Cross-Validation.md](../Machine-Learning/Cross-Validation.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

AI 역량 평가는 모델이 어떤 작업을 얼마나 안정적으로 수행할 수 있는지 측정하는 과정이다. 지식, 추론, 코딩, 도구 사용, 장기 계획, 안전 관련 행동을 benchmark와 시나리오 테스트로 평가한다.

## 직관 (Intuition)

모델을 배포하기 전에는 “똑똑해 보인다”가 아니라 “어떤 조건에서 무엇을 할 수 있고, 무엇을 못 하며, 실패할 때 어떤 방식으로 실패하는가”를 알아야 한다. 역량 평가는 성적표이면서 동시에 위험 지도다.

## 이론 (Theory)

평가 설계에서 중요한 요소는 다음과 같다.

- construct validity: benchmark가 정말 측정하려는 능력을 측정하는가?
- contamination control: 훈련 데이터에 평가 문제가 섞이지 않았는가?
- calibration: 모델 confidence와 실제 정답률이 맞는가?
- robustness: prompt, seed, format 변화에도 결과가 안정적인가?
- ceiling/floor effect: 너무 쉽거나 어려워 모델 차이를 구분하지 못하지 않는가?

MMLU, BIG-Bench 같은 benchmark는 역사적으로 널리 쓰인 평가 모음이지만, 단일 점수로 모델의 전체 역량이나 안전성을 요약할 수는 없다. 특히 에이전트형 시스템은 tool access, memory, time budget, scaffolding에 따라 결과가 크게 달라진다.

### 평가 대상의 분해

역량 평가는 먼저 측정하려는 construct를 분해해야 한다. "추론 능력" 같은 넓은 단어는 너무 모호하다. 수학 증명 검증, 다단계 계획, 코드 수정, 정보 검색, 도구 사용, 지시 충돌 처리처럼 관찰 가능한 task family로 나눈다.

각 task family에는 다음을 정한다.

- 성공 기준과 실패 기준
- 허용되는 도구와 시간 예산
- 채점 방식과 사람 검토 필요 여부
- 예상되는 contamination 위험
- 실제 제품 사용과의 관련성

이 과정을 거치지 않으면 benchmark 점수는 높지만 제품 위험을 설명하지 못하는 평가가 된다.

### Contamination과 memorization

평가 문제가 학습 데이터나 prompt tuning 데이터에 포함되어 있으면 점수가 과대평가된다. 특히 공개 benchmark는 시간이 지날수록 contamination 위험이 커진다. Contamination check는 exact match뿐 아니라 paraphrase, solution trace, answer-only leakage까지 고려해야 한다.

Dynamic benchmark, private holdout, temporal split, canary item은 contamination 위험을 줄인다. 하지만 private 평가도 반복 사용하면 모델 개발 과정에 간접적으로 새어 들어갈 수 있으므로 access control과 usage log가 필요하다.

### Agent evaluation

에이전트 평가에서는 모델 자체와 scaffolding을 분리해야 한다. 같은 base model도 planner, memory, retrieval, tool permission, retry budget, reflection loop가 바뀌면 성능과 위험이 크게 달라진다.

따라서 agent eval report에는 model version뿐 아니라 system prompt, tool list, tool permission, environment seed, time budget, human intervention rule을 함께 기록한다.

### 통계적 보고

평가 점수는 표본 추정치다. 작은 benchmark에서 1~2문제 차이는 실제 성능 차이가 아닐 수 있다. Bootstrap confidence interval, paired comparison, McNemar test 같은 도구로 버전 차이의 불확실성을 함께 보고한다.

## 구현 (Implementation)

객관식 평가의 최소 scoring loop는 다음처럼 생겼다.

```python
def accuracy(examples, predict):
    correct = 0
    for ex in examples:
        pred = predict(ex["question"], ex["choices"])
        correct += int(pred == ex["answer"])
    return correct / len(examples)


examples = [
    {"question": "2+2?", "choices": ["3", "4"], "answer": "4"},
]

print(accuracy(examples, lambda q, choices: "4"))
```

실제 평가 harness는 prompt template, decoding setting, refusal handling, logging, bootstrap confidence interval, contamination check를 함께 관리한다.

```python
def eval_record(model, benchmark, score, ci_low, ci_high):
    return {
        "model": model,
        "benchmark": benchmark,
        "score": score,
        "confidence_interval": [ci_low, ci_high],
        "prompt_template_version": "p1",
        "contamination_checked": True,
    }
```

점수만 저장하지 말고 평가 조건을 함께 저장해야 regression과 재현이 가능하다.

## 복잡도 (Complexity)

평가 비용은 문제 수, 모델 호출 비용, 반복 횟수, 사람 채점 필요성에 비례한다. 에이전트 평가는 환경 실행과 tool call 비용까지 포함한다. 신뢰구간을 좁히려면 더 많은 샘플과 반복이 필요하다.

## 응용 (Applications)

- 모델 출시 전 역량과 한계 측정
- 모델 버전 비교와 regression test
- 위험 역량의 조기 신호 탐지
- 제품 요구사항에 맞는 모델 선택

## 흔한 오해 (Common Misunderstandings)

- benchmark 점수 하나가 모델의 실제 유용성을 대표하지 않는다.
- 높은 역량 점수는 안전성을 보장하지 않는다.
- 평가 문제가 훈련 데이터에 노출되면 점수 해석이 어려워진다.
- 사람이 만든 평가도 편향과 blind spot을 가진다.

## TMI

- pass@k, exact match, preference win-rate, calibration error는 서로 다른 품질 측면을 본다.
- benchmark saturation이 오면 더 어려운 평가나 동적 평가가 필요해진다.
- 안전 평가에서는 평균 성능보다 tail risk와 worst-case behavior가 더 중요할 때가 많다.

## 연습 / 확인 문제 (Exercises)

- 객관식 benchmark와 에이전트 task benchmark의 차이를 설명하라.
- contamination이 평가 점수를 왜 부풀릴 수 있는지 예를 들어라.
- 모델 역량 평가와 안전 평가를 별도 축으로 나눠 설계해 보라.

## 이어서 읽기 (Reading Path)

- 이전: [적대적 예제](Adversarial-Examples.md)
- 다음: [Red-Teaming](Red-Teaming.md)

## 참조 (References)

- [Alignment-Overview.md](Alignment-Overview.md)
- [AI/MLOps/Model-Monitoring.md](../MLOps/Model-Monitoring.md)
- [AI/Machine-Learning/Cross-Validation.md](../Machine-Learning/Cross-Validation.md)
- [Reference/Books.md](../../Reference/Books.md)
