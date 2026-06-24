# 데이터 검증 (Data Validation)

- Level: Intermediate
- Prerequisites: [AI/MLOps/Data-Versioning.md](Data-Versioning.md), [Math/Probability-Statistics/Distributions.md](../../Math/Probability-Statistics/Distributions.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

데이터 검증은 학습·추론에 들어가는 데이터가 schema, range, completeness, distribution, business rule을 만족하는지 확인하는 절차다. 모델 품질 문제를 학습 이후가 아니라 데이터 유입 지점에서 잡는 것이 목표다.

## 직관 (Intuition)

모델은 쓰레기통이 아니라 확대경에 가깝다. 잘못된 값, 빠진 컬럼, 달라진 단위가 들어가면 모델은 그 오류를 조용히 증폭해 예측으로 내보낸다.

## 이론 (Theory)

검증은 schema validation, semantic validation, statistical validation으로 나눌 수 있다. Schema는 column, type, nullability, allowed value를 검사한다. Semantic rule은 `start_time <= end_time` 같은 도메인 제약을 본다. Statistical validation은 분포, quantile, missing rate, cardinality, correlation 변화를 추적한다.

검증 기준은 data version과 함께 관리해야 한다. 새 feature나 source 변경이 있을 때 threshold를 code review 없이 임의로 낮추면 guardrail이 사라진다.

## 구현 (Implementation)

```python
rules = {
    "age": {"type": "int", "min": 0, "max": 120, "nullable": False},
    "country": {"type": "category", "max_unknown_rate": 0.02},
    "label": {"allowed": [0, 1], "nullable": False},
}

report = validate_batch(dataset, rules)
if report.has_blocking_errors():
    raise RuntimeError(report.summary())
```

Blocking rule과 warning rule을 구분해 pipeline 중단 조건을 명확히 둔다.

## 복잡도 (Complexity)

단순 schema 검사는 행 수 `n`, column 수 `d`에 대해 대략 `O(nd)`다. Heavy distribution check와 segment별 검증은 feature×segment×window 수만큼 metric을 만든다.

## 응용 (Applications)

- training dataset quality gate
- online request validation
- upstream pipeline regression 탐지
- feature store publish gate

## 흔한 오해 (Common Misunderstandings)

- null check만으로 데이터 품질을 검증했다고 볼 수 없다.
- training data가 valid해도 serving data가 valid하다는 보장은 없다.
- threshold를 너무 엄격하게 잡으면 정상적인 계절성에도 pipeline이 멈춘다.
- alert를 만들었다고 owner와 대응 절차가 생기는 것은 아니다.

## TMI

- "unknown" 범주는 missing과 다른 의미일 수 있어 별도로 추적한다.
- 검증 실패 샘플을 안전하게 샘플링해 저장하면 debugging이 빨라진다.
- 데이터 계약은 producer와 consumer 사이의 API 문서처럼 다루는 편이 좋다.

## 연습 / 확인 문제 (Exercises)

- 학습 데이터셋에 필요한 blocking rule 5개를 설계하라.
- 경고로만 처리할 rule과 즉시 중단할 rule을 구분하라.
- distribution shift와 schema break를 구분하는 runbook을 작성하라.

## 이어서 읽기 (Reading Path)

- 이전: [데이터 버전 관리](Data-Versioning.md), [Feature Store](Feature-Store.md)
- 다음: [스트리밍 vs 배치](Streaming-vs-Batch.md), [데이터 드리프트](Data-Drift.md)

## 참조 (References)

- [Math/Probability-Statistics/Distributions.md](../../Math/Probability-Statistics/Distributions.md)
- [Reference/Books.md](../../Reference/Books.md)
