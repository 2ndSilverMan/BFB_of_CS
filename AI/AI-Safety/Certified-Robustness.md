# 인증된 강건성 (Certified Robustness)

- Level: Advanced
- Prerequisites: [AI/AI-Safety/Adversarial-Examples.md](Adversarial-Examples.md), [Math/Optimization/Convex-Optimization.md](../../Math/Optimization/Convex-Optimization.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

인증된 강건성은 특정 반경의 입력 perturbation 안에서는 모델 예측이 변하지 않는다는 보증을 수학적으로 제공하려는 분야다. 경험적 공격 방어보다 더 강한 안전 보증을 목표로 한다.

## 직관 (Intuition)

모델이 작은 잡음에 안 속는다고 말하려면 공격 몇 개를 막아본 것만으로 부족하다. 가능한 모든 작은 변화에 대해 답이 바뀌지 않는다는 보증이 필요하다.

## 이론 (Theory)

대표 접근은 randomized smoothing, convex relaxation, interval bound propagation, Lipschitz bound 등이다. Randomized smoothing은 입력에 Gaussian noise를 더한 smoothed classifier의 반경 보증을 제공한다.

보증 반경, 정확도, 계산 비용 사이에는 tradeoff가 있다. 큰 모델과 고차원 입력에서는 tight한 certificate를 얻기 어렵다.

### Empirical defense와 certificate

경험적 방어는 "우리가 시도한 공격이 실패했다"를 말한다. Certified robustness는 "명시한 반경 안의 모든 perturbation에 대해 예측이 변하지 않는다"를 말하려 한다. 둘 사이에는 큰 차이가 있다.

Certificate는 보통 보수적이다. 보증을 얻지 못했다고 반드시 취약하다는 뜻은 아니고, 보증을 얻었다고 threat model 밖 공격까지 막는 것도 아니다. 따라서 certified accuracy와 clean accuracy를 함께 보고한다.

### Randomized smoothing

Randomized smoothing은 기본 분류기 위에 noise를 평균내는 smoothed classifier를 만든다. 직관적으로 입력 주변의 noisy sample들이 같은 class로 많이 분류되면, 그 주변 반경 안에서 class가 유지된다는 확률적 보증을 준다.

장점은 비교적 큰 모델에도 적용할 수 있다는 점이고, 단점은 많은 sampling 비용과 norm/threat model 제한이다.

### Bound propagation과 relaxation

Interval bound propagation, linear relaxation, convex relaxation은 입력 perturbation이 각 layer를 통과하며 만들 수 있는 activation 범위를 계산한다. 정확한 범위를 계산하기 어렵기 때문에 relaxation을 쓰며, relaxation이 느슨하면 실제로는 강건해도 certificate를 못 받을 수 있다.

인증 방법을 비교할 때는 보증 반경, certified accuracy, 계산 시간, clean accuracy, 적용 가능한 모델 구조를 함께 본다.

### 보고 기준

강건성 certificate는 다음 항목을 같이 기록한다.

- Norm과 radius
- Certified accuracy와 clean accuracy
- Verification method
- 실패한 sample 비율과 원인
- Threat model 밖에서의 한계

## 구현 (Implementation)

```python
certificate = {
    "norm": "L2",
    "radius": 0.5,
    "guarantee": "prediction unchanged within radius",
}
```

인증 결과는 threat model과 norm을 명확히 함께 보고해야 한다.

```python
def certified_accuracy(results, radius):
    certified = [r for r in results if r["correct"] and r["radius"] >= radius]
    return len(certified) / len(results)
```

`radius`를 바꿔가며 curve를 그리면 어느 강도까지 보증이 유지되는지 볼 수 있다.

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
