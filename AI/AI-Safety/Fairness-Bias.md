# 공정성과 편향 (Fairness and Bias)

- Level: Advanced
- Prerequisites: [AI/Causal-Inference/Confounding.md](../Causal-Inference/Confounding.md), [Math/Probability-Statistics/Hypothesis-Testing.md](../../Math/Probability-Statistics/Hypothesis-Testing.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

AI 공정성은 모델의 예측과 의사결정이 특정 개인이나 집단에 부당한 피해를 주지 않도록 평가하고 개선하는 문제다. 편향은 데이터, 라벨, 목표, 배포 맥락, 사회 구조에서 생길 수 있다.

## 직관 (Intuition)

모델은 과거 데이터를 배운다. 과거 데이터에 차별적 관행이나 측정 편향이 들어 있으면, 모델은 그것을 효율적으로 반복할 수 있다.

## 이론 (Theory)

대표 metric은 demographic parity, equalized odds, equal opportunity, calibration, predictive parity 등이다. 이 metric들은 서로 충돌할 수 있으며, 어떤 metric이 적절한지는 도메인과 피해 유형에 따라 달라진다.

인과적 공정성은 민감 속성 자체보다 proxy, mediator, confounder, counterfactual dependence를 분석한다. 단순히 민감 속성을 제거해도 proxy variable이 남으면 bias가 사라지지 않는다.

## 구현 (Implementation)

```python
fairness_report = {
    "groups": ["A", "B"],
    "metrics": ["false_positive_rate", "false_negative_rate", "calibration"],
    "slices": ["overall", "high_risk_segment"],
}
```

평가는 전체 평균이 아니라 집단별·교차집단별 slice로 본다.

## 복잡도 (Complexity)

공정성 개선은 정확도, calibration, group parity 사이 tradeoff를 만들 수 있다. 작은 subgroup은 통계적 불확실성이 커서 confidence interval과 qualitative review가 필요하다.

## 응용 (Applications)

- 채용·대출·보험 모델 검토
- content moderation bias 분석
- 의료 AI subgroup 성능 평가
- 추천 시스템 exposure fairness

## 흔한 오해 (Common Misunderstandings)

- 민감 속성을 제거하면 공정해진다는 보장은 없다.
- 공정성 metric 하나로 모든 윤리적 문제를 해결할 수 없다.
- 집단 평균이 비슷해도 개인 수준 피해가 남을 수 있다.
- 데이터가 "현실을 반영"한다고 해서 공정한 것은 아니다.

## TMI

- Intersectional fairness는 성별×인종처럼 여러 속성의 교차집단을 본다.
- Counterfactual fairness는 민감 속성을 바꾼 대체 세계에서 예측이 유지되는지 묻는다.
- Fairness review는 기술팀만이 아니라 법무, 정책, 도메인 전문가, affected stakeholder와 연결된다.

## 연습 / 확인 문제 (Exercises)

- Demographic parity와 equalized odds가 충돌하는 예를 들어라.
- 민감 속성 제거가 실패하는 proxy bias 사례를 설명하라.
- 공정성 평가 리포트의 필수 표와 그래프를 설계하라.

## 이어서 읽기 (Reading Path)

- 이전: [AI Risk Classification](AI-Risk-Classification.md), [Confounding](../Causal-Inference/Confounding.md)
- 다음: [AI Regulation](AI-Regulation.md), [Model Monitoring](../MLOps/Model-Monitoring.md)

## 참조 (References)

- [AI/Causal-Inference/Counterfactual.md](../Causal-Inference/Counterfactual.md)
- [Math/Probability-Statistics/Hypothesis-Testing.md](../../Math/Probability-Statistics/Hypothesis-Testing.md)
- [Reference/Books.md](../../Reference/Books.md)
