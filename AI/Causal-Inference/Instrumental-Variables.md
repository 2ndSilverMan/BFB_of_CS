# 도구 변수 (Instrumental Variables)

- Level: Advanced
- Prerequisites: [AI/Causal-Inference/Confounding.md](Confounding.md), [AI/Causal-Inference/Intervention.md](Intervention.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

도구 변수(IV)는 treatment에는 영향을 주지만 outcome에는 treatment를 통해서만 영향을 주는 변수를 이용해 unobserved confounding이 있는 상황에서 인과 효과를 식별하려는 방법이다.

## 직관 (Intuition)

사람이 스스로 치료를 선택하면 건강 상태 같은 숨은 요인이 섞인다. 그런데 병원과의 거리처럼 치료 선택에는 영향을 주지만 결과에는 직접 영향이 없다고 믿을 수 있는 변수가 있다면, 그 외생적 흔들림만 이용해 효과를 본다.

## 이론 (Theory)

좋은 IV $Z$는 보통 세 조건이 필요하다.

- Relevance: $Z$가 treatment $X$에 영향을 준다.
- Exclusion: $Z$는 $X$를 통해서만 $Y$에 영향을 준다.
- Independence: $Z$는 outcome의 unobserved cause와 독립이다.

선형 설정에서는 2SLS가 대표적이다. 먼저 $X$를 $Z$로 예측하고, 예측된 treatment variation으로 $Y$를 설명한다. 해석은 종종 complier에 대한 LATE가 된다.

## 구현 (Implementation)

```python
wald_estimate = (mean_y_z1 - mean_y_z0) / (mean_x_z1 - mean_x_z0)
```

Binary instrument의 단순 Wald estimator는 reduced form 효과를 first stage 효과로 나눈다.

## 복잡도 (Complexity)

계산은 회귀 두 단계로 단순할 수 있지만, 약한 도구 변수는 variance와 bias를 크게 만든다. 표준오차는 2단계 구조를 반영해야 한다.

## 응용 (Applications)

- 정책 배정 규칙을 이용한 효과 추정
- 의료 접근성·거리 기반 treatment variation
- 자연 실험 분석
- encouragement design

## 흔한 오해 (Common Misunderstandings)

- Treatment와 상관된 변수라고 모두 좋은 도구 변수가 아니다.
- Exclusion restriction은 데이터만으로 완전히 검증하기 어렵다.
- Weak instrument는 결과를 불안정하게 만든다.
- IV 추정치는 전체 ATE가 아니라 특정 집단 LATE일 수 있다.

## TMI

- First-stage F-statistic은 weak instrument 진단에 자주 쓰인다.
- Monotonicity는 defier가 없다는 LATE 해석의 핵심 가정이다.
- Overidentification test는 도움은 되지만 IV validity를 증명하지는 않는다.

## 연습 / 확인 문제 (Exercises)

- IV 세 조건을 실제 예시로 검토하라.
- Weak instrument가 왜 위험한지 설명하라.
- Wald estimator를 작은 표로 계산하라.

## 이어서 읽기 (Reading Path)

- 이전: [교란 변수](Confounding.md), [RCT](RCT.md)
- 다음: [이중 차분법](DiD.md), [RDD](RDD.md)

## 참조 (References)

- [AI/Causal-Inference/Confounding.md](Confounding.md)
- [Reference/Books.md](../../Reference/Books.md)
