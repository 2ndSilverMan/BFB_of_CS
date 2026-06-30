# 적대적 예제 (Adversarial Examples)

- Level: Advanced
- Prerequisites: [AI/Deep-Learning/Loss-Functions.md](../Deep-Learning/Loss-Functions.md), [AI/Deep-Learning/Backpropagation.md](../Deep-Learning/Backpropagation.md), [Sparse-Autoencoder.md](Sparse-Autoencoder.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

적대적 예제는 사람에게는 거의 같아 보이지만 모델의 예측을 크게 바꾸도록 설계된 입력이다. 이미지, 텍스트, 음성, 코드 모델 모두에서 입력 공간의 작은 변화가 취약한 의사결정을 유도할 수 있다.

## 직관 (Intuition)

사람은 사진의 전체 구조를 보지만, 모델은 고차원 공간의 결정 경계 근처에서 매우 민감하게 반응할 수 있다. 입력을 눈에 잘 띄지 않는 방향으로 조금만 밀어도 결정 경계를 넘어 다른 클래스로 분류될 수 있다.

## 이론 (Theory)

분류 모델 $f_\theta$와 손실 $L(\theta,x,y)$가 있을 때, FGSM류 공격의 기본 형태는

$$
x_{adv}=x+\epsilon\operatorname{sign}(\nabla_x L(\theta,x,y))
$$

이다. 이는 입력 방향 gradient를 사용해 손실을 증가시키는 작은 perturbation을 만든다. threat model은 어떤 norm 제한($L_\infty$, $L_2$ 등), 공격자가 아는 정보, 허용되는 입력 변환 범위를 명시한다.

방어 연구에서는 adversarial training, certified robustness, 입력 전처리, detection 등이 사용되지만, adaptive attack에 대해 검증하지 않은 방어는 쉽게 과대평가될 수 있다.

### Threat model의 구성

적대적 강건성 주장은 threat model 없이는 의미가 약하다. 최소한 다음을 명시해야 한다.

- 공격자가 모델 구조와 파라미터를 아는지
- 입력을 어느 norm과 반경 안에서 바꿀 수 있는지
- 의미 보존이나 물리적 실현 가능성 제약이 있는지
- 공격 성공 기준이 misclassification인지 targeted class인지
- 방어가 공격자에게 공개되어 adaptive attack이 가능한지

같은 방어도 white-box, black-box, physical-world threat model에서 전혀 다르게 평가될 수 있다.

### Gradient masking

방어가 gradient를 불안정하게 만들면 gradient 기반 공격이 실패해 강건해 보일 수 있다. 그러나 이는 실제 decision boundary가 안전하다는 뜻이 아니다. 더 강한 optimizer, expectation over transformation, black-box transfer attack, gradient-free attack을 쓰면 쉽게 깨질 수 있다.

Gradient masking 의심 신호는 다음과 같다.

- 반복 공격보다 단일 공격이 더 강하게 보인다.
- 공격 step 수를 늘려도 성공률이 늘지 않는다.
- Black-box attack이 white-box attack보다 강하다.
- 방어 전처리를 제거하면 성능 패턴이 크게 달라진다.

### Adversarial training

Adversarial training은 학습 중 적대적 예제를 만들어 모델이 그 주변에서도 정답을 유지하도록 훈련한다. 직관적으로는 각 샘플 주변의 worst-case loss를 낮추는 min-max 문제다.

$$
\min_\theta E_{(x,y)}\left[\max_{\|\delta\|\le \epsilon} L(\theta, x+\delta, y)\right]
$$

이 방식은 계산 비용이 크고, 특정 norm과 epsilon에 맞춘 강건성만 주는 경우가 많다. Clean accuracy와 robust accuracy 사이 tradeoff도 고려해야 한다.

### 텍스트와 LLM의 특수성

텍스트에서는 작은 perturbation이 연속 공간의 작은 변화가 아니라 토큰·문장·의미 변화로 나타난다. 철자 변경, paraphrase, instruction conflict, jailbreak prompt는 모두 "작은 변화"의 정의가 다르다. 따라서 이미지식 norm만으로 LLM robustness를 설명하기 어렵고, 정책 위반률·instruction hierarchy 준수·semantic equivalence를 함께 평가해야 한다.

## 구현 (Implementation)

아래는 실제 공격 절차가 아니라 gradient 기반 perturbation의 수학적 형태를 보여주는 장난감 코드다.

```python
def fgsm_like_step(x, grad_x, epsilon, lo=0.0, hi=1.0):
    adv = []
    for value, grad in zip(x, grad_x):
        direction = 1 if grad >= 0 else -1
        adv.append(min(hi, max(lo, value + epsilon * direction)))
    return adv


x = [0.2, 0.7, 0.4]
grad_x = [0.5, -0.1, 2.0]
print(fgsm_like_step(x, grad_x, epsilon=0.03))
```

실제 보안 평가는 허가된 모델과 데이터에서, 명확한 threat model과 방어 검증 목적 아래 수행해야 한다.

```python
robust_eval = {
    "attack": "iterative_gradient",
    "norm": "linf",
    "epsilon": 0.03,
    "adaptive_to_defense": True,
    "reported_metrics": ["clean_accuracy", "robust_accuracy"],
}
```

강건성 보고서는 공격 이름보다 threat model과 attack strength를 더 중요하게 기록해야 한다.

## 복잡도 (Complexity)

단일 gradient step은 backpropagation 한 번 정도의 비용이다. 반복 공격은 step 수만큼 비용이 늘어난다. 강건성 평가는 여러 norm, epsilon, attack strength를 sweep해야 해서 일반 평가보다 훨씬 비싸다.

## 응용 (Applications)

- 모델 강건성 평가
- 안전-critical perception 시스템 검증
- prompt/input robustness 점검
- adversarial training 데이터 생성

## 흔한 오해 (Common Misunderstandings)

- 적대적 예제는 이미지 모델에만 있는 현상이 아니다.
- 단순 노이즈와 적대적 perturbation은 다르다. 후자는 모델 손실을 의도적으로 키운다.
- 방어가 한 공격에 강하다고 모든 공격에 강한 것은 아니다.
- threat model을 명시하지 않은 강건성 주장은 비교하기 어렵다.

## TMI

- gradient masking은 방어가 강한 것처럼 보이지만 실제로는 gradient 기반 공격만 어렵게 만드는 실패 모드다.
- certified robustness는 특정 반경 안에서 예측이 변하지 않음을 수학적으로 보장하려 한다.
- 텍스트에서는 의미 보존 제약과 이산 토큰 구조 때문에 이미지와 다른 평가 난점이 있다.

## 연습 / 확인 문제 (Exercises)

- $L_\infty$ 제한과 $L_2$ 제한의 차이를 설명하라.
- adversarial training이 왜 계산 비용을 크게 늘리는지 말하라.
- threat model 없이 “강건하다”고 말하면 안 되는 이유를 정리하라.

## 이어서 읽기 (Reading Path)

- 이전: [Sparse Autoencoder](Sparse-Autoencoder.md)
- 다음: [AI 역량 평가](Capability-Evaluation.md)

## 참조 (References)

- [AI/Deep-Learning/Loss-Functions.md](../Deep-Learning/Loss-Functions.md)
- [AI/Deep-Learning/Backpropagation.md](../Deep-Learning/Backpropagation.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
