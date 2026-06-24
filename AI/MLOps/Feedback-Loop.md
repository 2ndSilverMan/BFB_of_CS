# 피드백 루프와 재학습 트리거 (Feedback Loop)

- Level: Advanced
- Prerequisites: [AI/MLOps/Model-Monitoring.md](Model-Monitoring.md), [AI/MLOps/Data-Drift.md](Data-Drift.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

피드백 루프는 운영 예측, 사용자 행동, delayed label, 모니터링 신호를 다시 데이터와 모델 개선으로 연결하는 구조다. 재학습 트리거는 언제 새 데이터로 모델을 다시 만들지 결정하는 정책이다.

## 직관 (Intuition)

모델은 배포 순간 끝나는 물건이 아니라 현장에서 반응을 받는 생물에 가깝다. 다만 반응을 무작정 먹이면 자기 예측이 세상을 바꾸고, 바뀐 세상을 다시 정답처럼 배우는 순환 오류가 생긴다.

## 이론 (Theory)

재학습 트리거는 time-based, volume-based, drift-based, performance-based, event-based로 나눌 수 있다. Trigger는 후보일 뿐이며 label quality, data coverage, regression risk, business calendar를 함께 확인해야 한다.

Feedback data에는 selection bias가 자주 들어간다. 모델이 보여 준 item에 대해서만 click label을 얻는 추천 시스템이 대표적이다. Exploration, randomized holdout, counterfactual logging이 bias 추정에 도움을 준다.

## 구현 (Implementation)

```python
trigger = {
    "min_new_labels": 10000,
    "max_model_age_days": 30,
    "drift_alert": "warning_or_higher",
    "regression_gate": "must_pass",
}

if should_retrain(metrics, trigger):
    start_pipeline("training")
```

재학습 후에는 offline evaluation, shadow/canary, rollback plan을 통과해야 production alias로 승격한다.

## 복잡도 (Complexity)

피드백 루프 비용은 label 지연, 재학습 주기, pipeline 비용, evaluation 범위, 배포 검증 단계에 좌우된다. 너무 자주 학습하면 비용과 운영 위험이 커지고, 너무 늦으면 모델이 현실을 따라가지 못한다.

## 응용 (Applications)

- fraud·abuse pattern 변화 대응
- 추천 시스템 click feedback 반영
- LLM preference data 개선 루프
- drift alert 기반 retraining workflow

## 흔한 오해 (Common Misunderstandings)

- drift alert 하나만으로 자동 재배포까지 가면 위험하다.
- 운영 로그는 모델 행동에 의해 편향될 수 있다.
- 최신 데이터만 쓰면 장기 패턴과 rare case를 잃을 수 있다.
- 재학습은 성능 저하 원인을 고치는 유일한 방법이 아니다.

## TMI

- Champion/challenger 구조는 새 모델을 기존 모델과 계속 비교하게 해 준다.
- Frozen holdout은 데이터 분포가 변해도 장기 회귀 확인용으로 유용하다.
- Human review feedback은 policy 변화와 annotator drift도 함께 기록해야 한다.

## 연습 / 확인 문제 (Exercises)

- 서비스별 재학습 트리거 3종을 설계하라.
- 모델이 만든 selection bias를 줄이는 로그 전략을 설명하라.
- 자동 재학습 pipeline의 stop condition을 정의하라.

## 이어서 읽기 (Reading Path)

- 이전: [모델 모니터링](Model-Monitoring.md), [데이터 드리프트](Data-Drift.md)
- 다음: [ML 파이프라인](ML-Pipeline.md), [A/B 테스트](AB-Testing.md)

## 참조 (References)

- [AI/MLOps/Model-Monitoring.md](Model-Monitoring.md)
- [Reference/Books.md](../../Reference/Books.md)
