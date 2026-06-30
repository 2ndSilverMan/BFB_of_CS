# 일반화 경계 (Generalization Bounds)

- Level: Advanced
- Prerequisites: [PAC-Learning.md](PAC-Learning.md), [Rademacher-Complexity.md](Rademacher-Complexity.md), [AI/Machine-Learning/Cross-Validation.md](../Machine-Learning/Cross-Validation.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

일반화 경계는 훈련 데이터에서 측정한 경험 위험 $\hat R(h)$와 미지의 분포에서의 실제 위험 $R(h)$ 사이 차이를 상한으로 묶는 부등식이다. 목표는 “훈련에서 잘했다”를 “새 데이터에서도 어느 정도 잘한다”로 바꾸는 정량적 근거를 만드는 것이다.

## 직관 (Intuition)

훈련셋은 전체 세계의 작은 표본이다. 표본 평균이 모집단 평균과 가까우려면 표본 수가 충분해야 하고, 동시에 우리가 고르는 후보 모델 수나 복잡도도 통제되어야 한다. 일반화 경계는 이 표본 오차와 선택 편향을 함께 다룬다.

## 이론 (Theory)

가장 단순한 유한 가설 집합에서는 Hoeffding 부등식과 union bound로 다음 형태의 경계를 얻는다.

$$
R(h) \le \hat R_S(h)
+\sqrt{\frac{\log |H|+\log(1/\delta)}{2n}}
$$

이는 모든 $h\in H$에 대해 동시에 성립하는 uniform convergence 경계다. 가설 클래스가 무한하면 $|H|$ 대신 VC 차원, covering number, Rademacher 복잡도, algorithmic stability, PAC-Bayes bound 같은 도구가 쓰인다.

일반화 경계의 기본 구조는 대체로 다음과 같다.

```text
true risk ≤ empirical risk + complexity penalty + confidence penalty
```

여기서 complexity penalty는 가설 공간이나 알고리즘이 데이터를 얼마나 유연하게 맞출 수 있는지를 나타내고, confidence penalty는 실패 확률 $\delta$를 낮출수록 커진다.

### Uniform convergence와 algorithm-dependent bound

Uniform convergence 경계는 모든 $h\in H$에 대해 동시에 경험 위험과 실제 위험이 가깝다고 보장한다. 이는 ERM 분석에 강력하지만, 현대 딥러닝에서는 매우 느슨할 수 있다.

Algorithm-dependent bound는 실제 학습 알고리즘이 어떤 해를 선택하는지 반영한다. Stability, compression, PAC-Bayes, margin/norm bound는 단순한 hypothesis class 크기보다 학습 과정과 선택된 해의 성질을 더 많이 본다.

### Confidence parameter 해석

$\delta$는 모델이 틀릴 확률이 아니라 경계 자체가 실패할 확률이다. 예를 들어 $1-\delta$ 확률로 모든 $h$에 대해 부등식이 성립한다는 뜻이다. $\delta$를 작게 만들수록 confidence penalty가 커진다.

실무에서 이론 bound의 $\delta$를 테스트셋 p-value처럼 해석하면 안 된다. 역할은 보장 수준을 조절하는 수학적 매개변수다.

### Bound가 느슨해도 유용한 이유

딥러닝 bound는 수치적으로 실제 test error보다 훨씬 클 수 있다. 그래도 어떤 항이 표본 수, norm, margin, stability, compression과 연결되는지 보여 주면 연구적으로 의미가 있다. Bound의 목적은 항상 정확한 예측이 아니라 일반화 메커니즘을 분해하는 것이다.

### 분포 이동의 한계

대부분의 기본 일반화 경계는 train/test가 같은 분포에서 i.i.d.로 온다고 가정한다. 배포 환경이 바뀌면 경험 위험과 실제 위험의 연결 자체가 약해진다. 이 경우 domain adaptation, robust optimization, causal invariance, OOD evaluation이 별도로 필요하다.

## 구현 (Implementation)

유한 가설 집합 경계는 간단히 계산할 수 있다.

```python
import math


def finite_class_bound(empirical_risk, num_hypotheses, n, delta):
    penalty = math.sqrt(
        (math.log(num_hypotheses) + math.log(1 / delta)) / (2 * n)
    )
    return min(1.0, empirical_risk + penalty)


print(round(finite_class_bound(0.08, num_hypotheses=100, n=1000, delta=0.05), 3))
```

이 값은 보통 실제 검증 오차보다 보수적이다. 경계는 모델 선택의 정확한 대체재라기보다 일반화가 가능하려면 무엇을 제어해야 하는지 알려주는 분석 도구다.

```python
def generic_bound(empirical_risk, complexity, confidence):
    return empirical_risk + complexity + confidence
```

대부분의 경계는 이 구조를 갖지만, 어떤 complexity를 쓰는지와 어떤 가정에서 성립하는지가 핵심이다.

## 복잡도 (Complexity)

경계를 계산하는 비용은 선택한 복잡도 척도에 따라 다르다. 유한 클래스 bound는 $O(1)$로 계산되지만, Rademacher 복잡도 근사나 stability 분석은 학습 알고리즘 반복 실행이 필요할 수 있다. 실제 병목은 수치 계산보다 타당한 가정 설정이다.

## 응용 (Applications)

- 표본 수가 얼마나 필요한지 추정
- 모델 클래스 선택의 이론적 근거 제공
- regularization penalty 설계
- 논문에서 알고리즘의 안전한 성능 보장 제시

## 흔한 오해 (Common Misunderstandings)

- 일반화 경계가 작다고 실제 성능이 반드시 최고라는 뜻은 아니다.
- 느슨한 경계도 개념적으로 유용할 수 있다. 어떤 항을 줄여야 하는지 알려준다.
- 테스트셋 평가와 이론적 경계는 역할이 다르다. 하나는 경험적 추정, 하나는 수학적 보장이다.
- 경계의 가정이 깨지면 수식은 예뻐도 결론은 약해진다.

## TMI

- 딥러닝에서는 고전적 worst-case bound가 실제 성능보다 훨씬 비관적인 경우가 많아 sharpness, margin, norm, compression, PAC-Bayes 등 다양한 설명이 연구된다.
- validation set에 반복적으로 맞추면 validation 성능도 선택 편향을 갖는다. 이론적으로는 validation을 통한 모델 선택도 일반화 분석 대상이다.
- 분포 이동이 있으면 i.i.d. 일반화 경계만으로는 충분하지 않다.

## 연습 / 확인 문제 (Exercises)

- 유한 가설 집합 경계를 Hoeffding 부등식과 union bound로 유도하라.
- $n$이 4배가 되면 confidence penalty가 어떻게 변하는지 계산하라.
- 경험 위험이 0인 모델 두 개가 있을 때 복잡도 항이 모델 선택에 어떤 영향을 주는지 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [Rademacher 복잡도](Rademacher-Complexity.md)
- 다음: [이중 강하](Double-Descent.md)

## 참조 (References)

- [PAC-Learning.md](PAC-Learning.md)
- [Rademacher-Complexity.md](Rademacher-Complexity.md)
- [AI/Machine-Learning/Cross-Validation.md](../Machine-Learning/Cross-Validation.md)
- [Reference/Books.md](../../Reference/Books.md)
