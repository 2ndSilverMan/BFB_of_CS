# 샘플 복잡도 하한과 No-Free-Lunch 정리

- Level: Advanced
- Prerequisites: [PAC-Learning.md](PAC-Learning.md), [Shattering.md](Shattering.md), [Generalization-Bounds.md](Generalization-Bounds.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

No-Free-Lunch 정리는 아무런 가정 없이 모든 문제와 모든 분포에서 잘 작동하는 보편 학습 알고리즘은 없다는 사실을 말한다. 학습이 가능하려면 데이터 분포, 가설 클래스, 손실, inductive bias 중 어딘가에 구조적 가정이 필요하다.

## 직관 (Intuition)

본 적 없는 입력의 정답을 맞히려면 “비슷한 입력은 비슷한 라벨을 가진다” 같은 믿음이 필요하다. 그런 믿음이 전혀 없으면, 훈련셋 밖의 라벨은 어떤 방식으로든 뒤집힐 수 있다. 그래서 학습 알고리즘은 공짜로 일반화하지 못한다.

## 이론 (Theory)

유한 입력 공간 $X$에서 표본이 일부 점만 덮고 있다고 하자. 관측되지 않은 점들의 라벨은 훈련 데이터와 모순 없이 여러 방식으로 정의될 수 있다. 어떤 알고리즘이 하나의 라벨링을 예측하면, 그와 반대되는 목표 함수도 동일한 훈련 데이터와 양립할 수 있다.

따라서 충분한 구조가 없으면 모든 가능한 목표 함수에 대해 작은 일반화 오차를 보장할 수 없다. PAC 학습에서는 이를 피하기 위해 가설 클래스 $H$를 제한하거나, VC 차원 같은 capacity가 유한하다는 조건을 둔다.

샘플 복잡도 하한은 특정 문제를 학습하려면 최소한 어느 정도 표본이 필요하다는 결과다. 상한이 “이만큼이면 충분하다”를 말한다면, 하한은 “이보다 적으면 어떤 알고리즘도 보장하기 어렵다”를 말한다.

### Inductive bias의 필연성

No-Free-Lunch의 핵심 메시지는 좋은 학습기가 특정 문제군에 맞는 inductive bias를 가져야 한다는 것이다. 선형 모델은 선형 분리 가능성을, CNN은 지역성과 translation equivariance를, Transformer는 sequence token 간 attention 구조를 가정한다.

이 bias가 현실 구조와 맞으면 적은 데이터로 일반화할 수 있고, 맞지 않으면 큰 모델도 엉뚱한 방향으로 일반화할 수 있다.

### 상한과 하한의 짝

학습 이론에서 상한은 특정 알고리즘이나 가설 클래스가 충분한 표본에서 잘된다는 보장이다. 하한은 어떤 알고리즘도 그보다 적은 정보로는 보장할 수 없다는 한계다. 둘이 비슷하면 이론이 문제의 난이도를 잘 포착했다고 볼 수 있다.

PAC 학습에서 VC 차원 기반 상한과 하한이 같은 차수로 맞는 경우, VC 차원이 분포 독립 학습 가능성의 핵심량임을 알 수 있다.

### 실제 문제에서의 의미

현실 문제는 모든 가능한 라벨링이 똑같이 그럴듯하지 않다. 이미지, 언어, 물리, 사회 데이터에는 구조가 있다. 딥러닝이 성공하는 이유는 NFL을 무시해서가 아니라, architecture, pretraining, data augmentation, optimization bias가 현실 구조에 맞는 가정을 제공하기 때문이다.

### OOD와 NFL

훈련 분포 밖 영역의 라벨은 데이터가 직접 말해주지 않는다. OOD 일반화 주장은 causal mechanism, invariance, smoothness, domain relation 같은 추가 가정이 있어야 한다. NFL은 이 추가 가정 없이 OOD 성능을 약속할 수 없다는 경고로 읽을 수 있다.

## 구현 (Implementation)

관측되지 않은 점의 라벨을 뒤집는 두 목표 함수를 생각하면 no-free-lunch 직관을 볼 수 있다.

```python
def make_targets(train_labels, unseen_x):
    def target_a(x):
        if x in train_labels:
            return train_labels[x]
        return 0

    def target_b(x):
        if x in train_labels:
            return train_labels[x]
        return 1 if x == unseen_x else 0

    return target_a, target_b


train = {"a": 1, "b": 0}
fa, fb = make_targets(train, "c")
print(fa("c"), fb("c"))
```

두 목표 함수는 훈련 데이터에서는 같지만 unseen point에서는 다르다.

```python
def agrees_on_training(f, g, train_points):
    return all(f(x) == g(x) for x in train_points)
```

훈련 데이터에서 구분되지 않는 목표들이 테스트 영역에서 다를 수 있다는 점이 하한 논증의 출발점이다.

## 복잡도 (Complexity)

No-Free-Lunch는 특정 알고리즘의 시간복잡도보다 정보량의 한계를 말한다. 계산을 무한히 해도 표본과 가정이 부족하면 일반화 보장은 나오지 않는다.

## 응용 (Applications)

- 모델 선택에서 inductive bias의 필요성 설명
- 표본 복잡도 하한 이해
- 데이터 없는 일반화 주장 비판
- 분포 이동과 out-of-distribution 평가의 중요성 강조

## 흔한 오해 (Common Misunderstandings)

- No-Free-Lunch가 “학습은 불가능하다”는 뜻은 아니다. 구조 가정이 필요하다는 뜻이다.
- 모든 알고리즘이 실제 문제에서 똑같다는 뜻도 아니다. 실제 문제는 강한 구조를 가진다.
- 더 큰 모델이 항상 하한을 무시할 수 있는 것은 아니다.
- 하한은 최악 경우 결과이므로 실제 분포에서는 더 적은 데이터로도 잘 될 수 있다.

## TMI

- NFL 관점에서 좋은 모델이란 현실 문제의 구조에 잘 맞는 inductive bias를 가진 모델이다.
- 데이터 증강, convolution, attention, causal prior는 모두 특정 구조 가정을 모델에 넣는 방식으로 볼 수 있다.
- OOD 일반화가 어려운 이유도 훈련 분포가 말해주지 않는 영역에 대한 가정이 필요하기 때문이다.

## 연습 / 확인 문제 (Exercises)

- 훈련셋에서 동일하지만 테스트 점 하나에서 다른 두 목표 함수를 구성하라.
- inductive bias가 없는 학습기가 왜 unseen input을 예측할 수 없는지 설명하라.
- 상한과 하한의 차이를 PAC 표본 복잡도 관점에서 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [Shattering](Shattering.md)
- 다음: [편향-분산 이론](Bias-Variance-Theory.md)

## 참조 (References)

- [PAC-Learning.md](PAC-Learning.md)
- [Shattering.md](Shattering.md)
- [Generalization-Bounds.md](Generalization-Bounds.md)
- [Reference/Books.md](../../Reference/Books.md)
