# 매개 분석 (Mediation Analysis)

- Level: Advanced
- Prerequisites: [AI/Causal-Inference/Causal-DAG.md](Causal-DAG.md), [AI/Causal-Inference/Intervention.md](Intervention.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

매개 분석은 treatment가 outcome에 영향을 주는 경로 중 mediator를 통과하는 간접 효과와 직접 효과를 분해하려는 방법이다. "효과가 왜, 어떤 경로로 생겼는가"를 묻는다.

## 직관 (Intuition)

교육 프로그램이 소득을 올렸다면, 그것이 기술 향상 때문인지 네트워크 확장 때문인지 궁금할 수 있다. mediator는 treatment와 outcome 사이의 중간 메커니즘 후보이다.

## 이론 (Theory)

간단한 DAG는 $X\to M\to Y$와 $X\to Y$를 포함한다. Total effect는 mediator를 포함한 전체 효과이고, direct effect는 mediator 경로를 고정하거나 차단했을 때의 효과, indirect effect는 mediator를 통해 전달되는 부분이다.

Natural direct/indirect effect는 cross-world counterfactual을 포함하므로 강한 식별 가정이 필요하다. Treatment-mediator confounding, mediator-outcome confounding, treatment 이후 confounder가 핵심 위험이다.

### 효과 분해의 언어

Treatment를 $X$, mediator를 $M$, outcome을 $Y$라고 하자. Total effect는 $X$를 바꿨을 때 $Y$가 전체 경로를 통해 얼마나 바뀌는지 묻는다. Direct effect는 $M$을 고정하거나 특정 방식으로 통제했을 때 $X\to Y$ 경로에 남는 효과를 묻는다. Indirect effect는 $X\to M\to Y$ 경로를 통해 전달되는 부분을 묻는다.

Controlled direct effect(CDE)는 mediator를 특정 값 $m$으로 개입해 고정한다.

$$
CDE(m) = E[Y(1, m) - Y(0, m)]
$$

Natural direct effect와 natural indirect effect는 "treatment가 바뀌었을 때 mediator가 자연스럽게 가졌을 값"을 섞어 비교한다. 그래서 서로 다른 세계의 반사실을 한 식에 넣는 cross-world 가정이 필요하다.

### Sequential ignorability

전형적인 식별 논리는 두 단계의 무교란성을 요구한다.

- 관측 covariate를 조정하면 treatment 배정이 잠재 결과와 mediator에 대해 as-if random이어야 한다.
- Treatment와 covariate를 조정하면 mediator가 outcome의 잠재 결과에 대해 as-if random이어야 한다.

두 번째 조건이 특히 강하다. Mediator와 outcome을 함께 일으키는 숨은 요인이 있으면 indirect/direct effect 분해가 깨진다.

### Treatment 이후 confounder

Treatment가 어떤 변수 $L$을 바꾸고, $L$이 mediator와 outcome을 모두 바꾸는 경우가 어렵다. $L$을 조정하면 treatment 효과의 일부 경로를 막을 수 있고, 조정하지 않으면 mediator-outcome confounding이 남는다. 이 경우 단순 회귀 계수 분해보다 g-method, sequential g-formula, structural nested model 같은 도구가 필요할 수 있다.

### 해석상의 안전장치

매개 분석은 "효과가 있다"보다 더 섬세한 메커니즘 주장을 한다. 따라서 분석 전에 DAG로 mediator가 treatment 이후 변수인지, mediator 이전 confounder와 이후 confounder가 무엇인지, direct effect가 controlled인지 natural인지 명시해야 한다.

## 구현 (Implementation)

```python
def linear_mediation(total_effect, direct_effect):
    indirect_effect = total_effect - direct_effect
    return {
        "total": total_effect,
        "direct": direct_effect,
        "indirect": indirect_effect,
    }
```

이 함수는 선형·가산적 설정의 계산 직관만 보여 준다. 실제 분석에서는 효과 정의, 조정 집합, mediator-outcome confounding 가능성을 먼저 DAG로 고정해야 한다.

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
