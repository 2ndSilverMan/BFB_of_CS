# 암묵적 규제 (Implicit Regularization)

- Level: Advanced
- Prerequisites: [GD-Convergence.md](GD-Convergence.md), [Non-Convex-Convergence.md](Non-Convex-Convergence.md), [AI/Machine-Learning/Regularization.md](../Machine-Learning/Regularization.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

암묵적 규제는 명시적 정규화 항을 넣지 않았는데도 최적화 알고리즘, 초기화, 모델 구조, 학습 절차가 특정한 종류의 해를 선호하는 현상이다. 딥러닝 일반화에서 “훈련 오차 0인데 왜 테스트가 잘 되는가”를 설명하는 중요한 관점이다.

## 직관 (Intuition)

방정식의 해가 무수히 많을 때, 풀이 방법이 어떤 해를 고르는지가 중요하다. 같은 훈련 데이터를 완벽히 맞추는 모델이 많아도 gradient descent는 그중 더 낮은 norm, 더 큰 margin, 더 매끄러운 함수 같은 특정 성질을 가진 해 쪽으로 갈 수 있다.

## 이론 (Theory)

선형 회귀에서 underdetermined 시스템 $Xw=y$는 해가 많다. 작은 초기값에서 gradient descent를 쓰면 명시적으로 L2 정규화를 넣지 않아도 minimum-norm solution에 도달한다. 이는 알고리즘의 경로가 해 선택에 영향을 준다는 단순하고 강력한 예다.

분류 문제에서는 separable data에 logistic loss를 gradient descent로 최적화할 때 가중치 norm은 계속 커질 수 있지만 방향은 max-margin classifier 쪽으로 수렴하는 결과가 알려져 있다. 딥러닝에서는 이 현상이 더 복잡하지만, optimizer와 architecture가 일반화 성질에 영향을 준다는 점은 핵심이다.

### Minimum-norm bias

Underdetermined linear regression에서 $Xw=y$를 만족하는 해가 무한히 많을 때, 0 초기화의 gradient descent는 row space 안에서만 움직인다. 따라서 null space 성분이 생기지 않고 minimum Euclidean norm 해로 수렴한다.

이 예시는 명시적 L2 penalty가 없어도 optimization path가 해 선택을 제한할 수 있음을 보여 준다.

### Max-margin bias

선형 분류에서 데이터가 separable이면 logistic loss의 infimum은 0이지만 finite minimizer는 없다. Gradient descent는 weight norm을 계속 키우면서도 방향은 max-margin separator로 수렴할 수 있다. 일반화와 margin이 연결되므로, 이 방향 선택은 중요한 implicit bias다.

### SGD noise와 batch size

SGD의 stochastic noise는 단순한 계산 오차가 아니라 어떤 basin이나 해를 선택하는지에 영향을 줄 수 있다. 작은 batch는 noise가 커서 sharp한 해에서 빠져나올 가능성이 있고, 큰 batch는 더 deterministic하게 움직인다. 다만 "flat minimum이 항상 일반화가 좋다"는 식의 단순화는 조심해야 한다.

### Architecture bias

암묵적 규제는 optimizer만이 아니라 architecture에서도 온다. CNN은 locality와 weight sharing을, Transformer는 attention 기반 token interaction을, normalization layer는 scale 동역학을 통해 특정 함수 family를 더 쉽게 학습하게 만든다.

## 구현 (Implementation)

명시적 penalty가 없어도 업데이트 규칙이 해를 제한할 수 있다.

```python
def gradient_step(w, grad, eta):
    return [wi - eta * gi for wi, gi in zip(w, grad)]


# 같은 훈련 오차를 갖는 해가 많더라도
# 초기값과 gradient update 경로가 최종 해를 제한한다.
w = [0.0, 0.0, 0.0]
grad = [-1.0, 0.0, -1.0]
print(gradient_step(w, grad, eta=0.1))
```

실험적으로는 optimizer, batch size, initialization, learning rate schedule을 바꿔 일반화 차이를 비교한다.

```python
experiment_grid = {
    "optimizer": ["sgd", "adam"],
    "batch_size": [32, 256],
    "initialization_scale": [0.01, 0.1],
    "explicit_weight_decay": [0.0],
}
```

명시적 regularization을 고정하고 학습 절차만 바꾸면 implicit bias를 관찰하기 쉽다.

## 복잡도 (Complexity)

암묵적 규제는 별도 알고리즘 비용이라기보다 학습 절차의 성질이다. 분석 비용은 크며, 같은 모델도 optimizer와 데이터에 따라 다른 bias를 가질 수 있다.

## 응용 (Applications)

- 과매개변수 모델의 일반화 설명
- optimizer 선택과 batch size 효과 분석
- max-margin behavior 연구
- double descent와 benign overfitting 해석

## 흔한 오해 (Common Misunderstandings)

- 암묵적 규제가 있으므로 명시적 정규화가 필요 없다는 뜻은 아니다.
- 훈련 알고리즘의 bias가 항상 좋은 방향이라는 보장은 없다.
- 작은 norm이 모든 문제에서 좋은 일반화의 충분조건은 아니다.
- 암묵적 규제는 하나의 원리가 아니라 여러 현상의 묶음이다.

## TMI

- SGD의 noise는 단순한 계산 부산물이 아니라 해 선택에 영향을 줄 수 있다.
- early stopping도 암묵적 정규화로 해석할 수 있다.
- 딥러닝에서 sharpness와 flatness 논의는 암묵적 규제와 자주 연결된다.

## 연습 / 확인 문제 (Exercises)

- underdetermined 선형 회귀에서 minimum-norm 해가 왜 특별한지 설명하라.
- logistic regression에서 separable data의 weight norm이 커질 수 있는 이유를 말하라.
- explicit regularization과 implicit regularization을 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [비볼록 수렴](Non-Convex-Convergence.md)
- 다음: [후회 최소화](Regret-Minimization.md)

## 참조 (References)

- [GD-Convergence.md](GD-Convergence.md)
- [Non-Convex-Convergence.md](Non-Convex-Convergence.md)
- [AI/Machine-Learning/Regularization.md](../Machine-Learning/Regularization.md)
- [Reference/Books.md](../../Reference/Books.md)
