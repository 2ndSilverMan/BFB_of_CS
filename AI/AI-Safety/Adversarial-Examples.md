# 적대적 예제 (Adversarial Examples)

- Level: Advanced
- Prerequisites: [AI/Deep-Learning/Loss-Functions.md](../Deep-Learning/Loss-Functions.md), [AI/Deep-Learning/Backpropagation.md](../Deep-Learning/Backpropagation.md), [Sparse-Autoencoder.md](Sparse-Autoencoder.md)
- Status: Draft
- Reviewed-by: -

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
