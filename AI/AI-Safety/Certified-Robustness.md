# 인증된 강건성 (Certified Robustness)

- Level: Advanced
- Prerequisites: [AI/AI-Safety/Adversarial-Examples.md](Adversarial-Examples.md), [Math/Optimization/Convex-Optimization.md](../../Math/Optimization/Convex-Optimization.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

인증된 강건성은 특정 반경의 입력 perturbation 안에서는 모델 예측이 변하지 않는다는 보증을 수학적으로 제공하려는 분야다. 경험적 공격 방어보다 더 강한 안전 보증을 목표로 한다.

## 직관 (Intuition)

모델이 작은 잡음에 안 속는다고 말하려면 공격 몇 개를 막아본 것만으로 부족하다. 가능한 모든 작은 변화에 대해 답이 바뀌지 않는다는 보증이 필요하다.

## 이론 (Theory)

대표 접근은 randomized smoothing, convex relaxation, interval bound propagation, Lipschitz bound 등이다. Randomized smoothing은 입력에 Gaussian noise를 더한 smoothed classifier의 반경 보증을 제공한다.

보증 반경, 정확도, 계산 비용 사이에는 tradeoff가 있다. 큰 모델과 고차원 입력에서는 tight한 certificate를 얻기 어렵다.

## 구현 (Implementation)

```python
certificate = {
    "norm": "L2",
    "radius": 0.5,
    "guarantee": "prediction unchanged within radius",
}
```

인증 결과는 threat model과 norm을 명확히 함께 보고해야 한다.

## 복잡도 (Complexity)

정확한 verification은 매우 어려울 수 있다. Relaxation은 계산 가능하게 만들지만 보증이 느슨해질 수 있고, smoothing은 많은 샘플이 필요하다.

## 응용 (Applications)

- 안전 중요 비전 모델 검증
- adversarial defense 평가
- 작은 입력 변화에 대한 보증
- robustness benchmark

## 흔한 오해 (Common Misunderstandings)

- 특정 norm 반경 보증이 모든 현실 공격을 막는 것은 아니다.
- 경험적 공격에 강하다고 certified robust인 것은 아니다.
- 보증 반경이 크면 clean accuracy가 떨어질 수 있다.
- Certificate는 threat model 밖에서는 의미가 약하다.

## TMI

- Certified robustness는 "공격자가 못 찾았다"와 "공격이 없다"를 구분하려는 시도다.
- L0, L2, L∞ threat model은 서로 다른 공격 공간을 의미한다.
- Robust training은 일반 정확도와 강건성 사이 tradeoff를 만들 수 있다.

## 연습 / 확인 문제 (Exercises)

- Empirical robustness와 certified robustness의 차이를 설명하라.
- Threat model을 명시하지 않은 강건성 주장이 왜 약한지 말하라.
- Randomized smoothing의 직관을 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [Adversarial Examples](Adversarial-Examples.md)
- 다음: [Poisoning Attacks](Poisoning-Attacks.md), [OOD Generalization](OOD-Generalization.md)

## 참조 (References)

- [AI/AI-Safety/Adversarial-Examples.md](Adversarial-Examples.md)
- [Math/Optimization/Convex-Optimization.md](../../Math/Optimization/Convex-Optimization.md)
- [Reference/Papers.md](../../Reference/Papers.md)
