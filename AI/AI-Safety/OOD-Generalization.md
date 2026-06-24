# 분포 외 일반화 (OOD Generalization)

- Level: Advanced
- Prerequisites: [AI/Theoretical-ML/Generalization-Bounds.md](../Theoretical-ML/Generalization-Bounds.md), [AI/Causal-Inference/Causal-Representation.md](../Causal-Inference/Causal-Representation.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

분포 외 일반화(OOD generalization)는 학습 데이터와 다른 분포의 입력에서도 모델이 안정적으로 작동하는 능력이다. AI 안전성에서는 배포 환경 변화와 rare case에서 실패를 줄이는 핵심 문제다.

## 직관 (Intuition)

눈 오는 날을 본 적 없는 자율주행 모델이 맑은 날 성능만으로 안전하다고 할 수 없다. OOD 문제는 모델이 진짜 원리를 배웠는지, 아니면 학습 분포의 shortcut을 외웠는지 드러낸다.

## 이론 (Theory)

Distribution shift는 covariate shift, label shift, concept shift, domain shift로 나눌 수 있다. Robust generalization은 invariant feature, causal mechanism, uncertainty estimation, domain adaptation과 연결된다.

OOD 성능은 training IID validation만으로 예측하기 어렵다. Stress test, subgroup evaluation, synthetic shift, temporal split, adversarial evaluation이 필요하다.

## 구현 (Implementation)

```python
eval_splits = {
    "iid": "same distribution validation",
    "ood": "new domain or time period",
    "stress": "rare or adversarial conditions",
}
```

평가는 평균 성능뿐 아니라 worst-group performance와 calibration을 함께 본다.

## 복잡도 (Complexity)

OOD 평가셋 구축이 어렵고 비용이 크다. 가능한 shift가 무한하므로 실제 위험 시나리오를 우선순위화해야 한다.

## 응용 (Applications)

- 안전한 모델 배포 평가
- 의료·자율주행·금융 rare case 분석
- LLM jailbreak·prompt distribution shift 평가
- 데이터 수집 계획 수립

## 흔한 오해 (Common Misunderstandings)

- IID test 성능이 높다고 OOD 성능이 보장되지 않는다.
- 데이터 증강이 모든 shift를 커버하지 않는다.
- OOD detection과 OOD generalization은 다른 문제다.
- 불확실성 점수가 항상 실패를 잘 예측하는 것은 아니다.

## TMI

- Shortcut learning은 배경, 스타일, 포맷 같은 비인과 단서를 쓰는 현상이다.
- Invariant risk minimization은 환경이 바뀌어도 유지되는 예측 관계를 찾으려는 접근이다.
- Model monitoring의 drift metric은 OOD 위험 신호지만 성능 하락과 일대일 대응하지 않는다.

## 연습 / 확인 문제 (Exercises)

- 세 가지 distribution shift 예시를 들고 위험도를 비교하라.
- Worst-group accuracy를 보고해야 하는 상황을 설명하라.
- OOD evaluation set을 설계할 때 피해야 할 leakage를 말하라.

## 이어서 읽기 (Reading Path)

- 이전: [일반화 경계](../Theoretical-ML/Generalization-Bounds.md)
- 다음: [Certified Robustness](Certified-Robustness.md), [Poisoning Attacks](Poisoning-Attacks.md)

## 참조 (References)

- [AI/Causal-Inference/Causal-Representation.md](../Causal-Inference/Causal-Representation.md)
- [Reference/Papers.md](../../Reference/Papers.md)
