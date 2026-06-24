# 매개 분석 (Mediation Analysis)

- Level: Advanced
- Prerequisites: [AI/Causal-Inference/Causal-DAG.md](Causal-DAG.md), [AI/Causal-Inference/Intervention.md](Intervention.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

매개 분석은 treatment가 outcome에 영향을 주는 경로 중 mediator를 통과하는 간접 효과와 직접 효과를 분해하려는 방법이다. "효과가 왜, 어떤 경로로 생겼는가"를 묻는다.

## 직관 (Intuition)

교육 프로그램이 소득을 올렸다면, 그것이 기술 향상 때문인지 네트워크 확장 때문인지 궁금할 수 있다. mediator는 treatment와 outcome 사이의 중간 메커니즘 후보이다.

## 이론 (Theory)

간단한 DAG는 $X\to M\to Y$와 $X\to Y$를 포함한다. Total effect는 mediator를 포함한 전체 효과이고, direct effect는 mediator 경로를 고정하거나 차단했을 때의 효과, indirect effect는 mediator를 통해 전달되는 부분이다.

Natural direct/indirect effect는 cross-world counterfactual을 포함하므로 강한 식별 가정이 필요하다. Treatment-mediator confounding, mediator-outcome confounding, treatment 이후 confounder가 핵심 위험이다.

## 구현 (Implementation)

```python
effects = {
    "total": "X changes Y through all paths",
    "direct": "X changes Y not through M",
    "indirect": "X changes M, then M changes Y",
}
```

실제 분석은 DAG로 어떤 confounder를 조정할지 먼저 명시해야 한다.

## 복잡도 (Complexity)

선형 모델에서는 계수 곱으로 단순히 보일 수 있지만, 비선형 모델·상호작용·시간 의존 mediator에서는 효과 분해가 복잡해진다.

## 응용 (Applications)

- 정책 효과의 작동 메커니즘 분석
- 의료 처치가 biomarker를 통해 작동하는지 평가
- 제품 변경이 engagement를 통해 retention에 주는 영향
- 공정성에서 proxy 경로 분석

## 흔한 오해 (Common Misunderstandings)

- Mediator를 회귀에 넣으면 항상 직접 효과가 추정되는 것은 아니다.
- Treatment 이후 변수를 조정하면 효과 일부를 차단하거나 bias를 만들 수 있다.
- 매개 분석은 인과 효과가 있다는 사실보다 더 강한 메커니즘 가정을 요구한다.
- Indirect effect의 비율 해석은 불안정할 수 있다.

## TMI

- Controlled direct effect는 mediator를 특정 값으로 고정하는 개입 효과다.
- Multiple mediator가 있으면 경로별 분해가 훨씬 어려워진다.
- Mediation과 moderation은 다르다. Moderation은 효과가 subgroup마다 달라지는 문제다.

## 연습 / 확인 문제 (Exercises)

- Total, direct, indirect effect를 DAG로 설명하라.
- Mediator-outcome confounder가 있을 때 필요한 조정을 말하라.
- 제품 변경→클릭→구매 사례의 매개 분석 가정을 작성하라.

## 이어서 읽기 (Reading Path)

- 이전: [인과 DAG](Causal-DAG.md), [반사실](Counterfactual.md)
- 다음: [인과적 머신러닝](Causal-ML.md)

## 참조 (References)

- [AI/Causal-Inference/Causal-DAG.md](Causal-DAG.md)
- [Reference/Books.md](../../Reference/Books.md)
