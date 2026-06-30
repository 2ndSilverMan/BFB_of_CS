# Probing Classifiers

- Level: Advanced
- Prerequisites: [AI/AI-Safety/Mechanistic-Interpretability.md](Mechanistic-Interpretability.md), [AI/Machine-Learning/Logistic-Regression.md](../Machine-Learning/Logistic-Regression.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

Probing classifier는 모델 내부 representation에 간단한 분류기를 학습시켜 특정 정보가 표현 안에 존재하는지 조사하는 방법이다. 예를 들어 layer activation에 품사, 위치, 사실, 독성 여부가 선형적으로 읽히는지 본다.

## 직관 (Intuition)

모델 내부에 어떤 정보가 숨어 있는지 직접 볼 수 없으니, 작은 탐침을 꽂아 "이 정보가 쉽게 읽히는가"를 묻는다. 쉽게 읽히면 표현 어딘가에 그 정보가 담겼을 가능성이 있다.

## 이론 (Theory)

Probe 성능이 높다는 것은 representation에서 label을 예측할 수 있다는 뜻이다. 하지만 모델이 실제로 그 정보를 사용한다는 뜻은 아니다. 그래서 probe complexity, control task, selectivity, intervention 실험이 중요하다.

Linear probe는 선형적으로 접근 가능한 정보를 보고, nonlinear probe는 더 많은 정보를 뽑아낼 수 있지만 과해석 위험이 커진다.

### Accessibility와 usage의 차이

Probe는 정보가 representation에서 읽힐 수 있는지를 측정한다. 그러나 모델의 forward pass가 그 정보를 실제로 사용한다는 뜻은 아니다. 예를 들어 hidden state에서 성별 정보를 예측할 수 있어도, 특정 decision head가 그 정보를 사용하지 않을 수 있다.

따라서 probe 결과는 "정보 존재 가능성"의 증거이고, "인과적 사용"의 증거가 되려면 ablation, activation patching, counterfactual input, causal mediation 분석이 필요하다.

### Probe capacity 통제

강한 nonlinear probe는 representation에 없는 구조까지 데이터셋 shortcut으로 학습할 수 있다. 그래서 probe capacity를 제한하거나, linear probe와 nonlinear probe를 함께 비교한다. Probe가 너무 약하면 실제 정보를 못 읽고, 너무 강하면 원 모델이 아니라 probe가 문제를 푸는 셈이 된다.

좋은 보고서는 probe architecture, parameter 수, regularization, training data size, control task 성능을 함께 적는다.

### Control task와 selectivity

Control task는 label을 무작위로 섞거나, 표면적 shortcut만 남긴 task로 probe가 얼마나 쉽게 가짜 패턴을 배우는지 확인한다. Selectivity는 실제 task 성능과 control task 성능의 차이로 볼 수 있다.

Probe accuracy가 높아도 selectivity가 낮으면 representation에 의미 있는 정보가 있다기보다 probe가 dataset artifact를 이용했을 가능성이 크다.

### Layer-wise 해석

Layer별 probe를 학습하면 정보가 어느 층에서 나타나고 사라지는지 볼 수 있다. 낮은 층은 표면적·지역적 정보, 중간 층은 syntactic/semantic feature, 높은 층은 task-specific 정보가 강할 수 있지만 이는 모델과 task에 따라 달라진다.

Layer curve는 가설 생성 도구다. 특정 층에서 probe 성능이 높다면 그 층을 대상으로 patching이나 ablation을 설계한다.

## 구현 (Implementation)

```python
probe = {
    "input": "hidden_state_at_layer_k",
    "target": "attribute_label",
    "model": "linear_classifier",
}
```

Train/test split은 원 모델 학습 데이터와 독립적으로 구성하고 leakage를 피한다.

```python
def selectivity(real_accuracy, control_accuracy):
    return real_accuracy - control_accuracy
```

높은 probe 성능은 높은 selectivity와 함께 보고해야 해석 가치가 커진다.

## 복잡도 (Complexity)

Activation 추출 비용은 데이터 수와 모델 forward 비용에 비례한다. Probe 자체는 작지만 layer별·position별 probe를 많이 학습하면 비용이 커진다.

## 응용 (Applications)

- 언어 정보가 어느 층에 있는지 분석
- 안전 관련 속성 탐지
- representation 비교
- fine-tuning 전후 내부 변화 측정

## 흔한 오해 (Common Misunderstandings)

- Probe가 정보를 읽는다고 모델이 그 정보를 사용한다는 뜻은 아니다.
- 강한 probe는 데이터셋 shortcut을 배울 수 있다.
- Probe 성능 비교는 probe capacity를 통제해야 한다.
- Label 품질이 낮으면 해석도 흐려진다.

## TMI

- Diagnostic classifier라는 이름도 쓰인다.
- Selectivity는 실제 task와 control task 성능 차이로 probe 의미를 점검한다.
- Causal probing은 단순 예측을 넘어 intervention과 연결하려는 시도다.

## 연습 / 확인 문제 (Exercises)

- Linear probe와 nonlinear probe의 장단점을 비교하라.
- Probe control task를 설계하라.
- Probe 결과와 activation patching 결과를 함께 해석하는 방법을 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [Mechanistic Interpretability](Mechanistic-Interpretability.md)
- 다음: [Activation Patching](Activation-Patching.md), [Attention Visualization](Attention-Visualization.md)

## 참조 (References)

- [AI/Machine-Learning/Logistic-Regression.md](../Machine-Learning/Logistic-Regression.md)
- [Reference/Papers.md](../../Reference/Papers.md)
