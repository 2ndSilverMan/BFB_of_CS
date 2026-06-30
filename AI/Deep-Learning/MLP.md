# 퍼셉트론과 다층 신경망 (MLP)

- Level: Intermediate
- Prerequisites: [AI/Machine-Learning/Logistic-Regression.md](../Machine-Learning/Logistic-Regression.md), [Math/Linear-Algebra/Matrices.md](../../Math/Linear-Algebra/Matrices.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

다층 퍼셉트론(MLP)은 affine transformation과 비선형 활성화 함수를 여러 층 쌓은 feedforward neural network다. 입력에서 출력으로만 정보가 흐르며 hidden layer가 데이터의 중간 표현을 학습한다.

## 직관 (Intuition)

한 개의 선형 경계로 나눌 수 없는 문제도 여러 층이 단순한 변환을 조합하면 복잡한 경계를 만들 수 있다. 각 층은 이전 표현을 다시 섞고 꺾어 다음 층이 다루기 쉬운 특징으로 바꾼다.

## 이론 (Theory)

층 $l$의 계산은

$$z^{(l)}=W^{(l)}h^{(l-1)}+b^{(l)},\qquad h^{(l)}=\phi(z^{(l)})$$

다. 활성화가 없으면 여러 선형층의 합성도 하나의 선형변환이므로 깊이의 표현력이 생기지 않는다. 충분한 폭의 MLP는 적절한 조건에서 연속함수를 근사할 수 있지만, 효율적인 학습과 일반화까지 자동 보장하는 정리는 아니다.

```mermaid
flowchart LR
    X["입력 x"] --> A1["Affine: xW1 + b1"]
    A1 --> H1["Activation"]
    H1 --> A2["Affine: hW2 + b2"]
    A2 --> Y["logit 또는 예측값"]
```

### Shape와 파라미터 해석

입력 배치가 $X\in\mathbb{R}^{B\times d_{in}}$이고 hidden width가 $h$이면 첫 층은 $W_1\in\mathbb{R}^{d_{in}\times h}$, $b_1\in\mathbb{R}^{h}$를 가진다. 출력 차원이 $c$이면 둘째 층은 $W_2\in\mathbb{R}^{h\times c}$, $b_2\in\mathbb{R}^{c}$다. 이때 전체 파라미터 수는

$$d_{in}h+h+hc+c$$

다. tabular 모델에서 입력 feature 수가 크거나 hidden width를 크게 잡으면 파라미터가 빠르게 늘어나므로, 데이터 수와 regularization을 함께 보아야 한다.

### 초기화, 대칭, 활성화 분포

모든 hidden unit을 같은 값으로 초기화하면 각 unit이 같은 gradient를 받아 끝까지 같은 역할을 한다. 그래서 무작위 초기화는 단순한 관례가 아니라 대칭을 깨기 위한 필수 장치다. ReLU 계열에는 He 초기화, tanh 계열에는 Xavier/Glorot 초기화가 흔히 쓰이며, 목적은 층을 지나도 activation과 gradient scale이 급격히 사라지거나 폭주하지 않게 하는 것이다.

### 표현력, 최적화, 일반화의 분리

MLP가 충분한 함수를 표현할 수 있다는 말은 세 가지를 보장하지 않는다.

| 질문 | 확인해야 할 것 |
| --- | --- |
| 표현할 수 있는가 | depth, width, activation, 입력 feature |
| 학습할 수 있는가 | 초기화, optimizer, learning rate, normalization |
| 일반화하는가 | 데이터 수, regularization, 검증 성능, 분포 차이 |

따라서 "모델이 작아서 못 맞춘다"와 "모델은 충분하지만 학습이 불안정하다"와 "훈련은 맞추지만 검증에서 무너진다"를 분리해 진단해야 한다.

## 구현 (Implementation)

```python
import numpy as np


def relu(x):
    return np.maximum(x, 0)


def forward(x, w1, b1, w2, b2):
    hidden = relu(x @ w1 + b1)
    return hidden @ w2 + b2
```

가중치는 대칭을 깨도록 무작위 초기화하고, 출력층 활성화와 손실은 과제에 맞춘다.

```python
def mlp_param_count(d_in, hidden, d_out):
    return d_in * hidden + hidden + hidden * d_out + d_out
```

## 복잡도 (Complexity)

배치 크기 $B$, 층 너비 $d_{l-1},d_l$일 때 한 층의 주된 비용은 `O(B·d_{l-1}·d_l)`이다. 파라미터와 activation 저장량은 각 층 행렬 크기와 배치에 비례한다.

## 응용 (Applications)

- tabular 데이터와 고정 길이 특징 분류·회귀
- 다른 아키텍처의 projection·classification head
- 복잡한 비선형 함수 근사
- 신경망 기본 구조 학습

## 흔한 오해 (Common Misunderstandings)

- 층을 늘리기만 하면 항상 성능이 좋아지지 않는다.
- 퍼셉트론 하나와 다층 신경망의 표현력은 다르다.
- universal approximation은 작은 데이터에서 잘 일반화한다는 뜻이 아니다.
- 출력 logit은 정규화된 확률이 아니다.

## TMI

- XOR은 단일 선형 퍼셉트론의 한계를 보여 주는 고전적 예다.
- MLP 블록은 Transformer에서도 attention 뒤의 핵심 구성 요소다.
- residual connection 없이 매우 깊은 MLP를 안정적으로 학습하기는 어렵다.

## 연습 / 확인 문제 (Exercises)

- 활성화를 제거한 두 선형층이 하나의 선형층과 같음을 보여라.
- XOR을 표현하는 작은 MLP 구조를 설계하라.
- 층별 파라미터 수를 계산하라.

## 이어서 읽기 (Reading Path)

- 이전: [로지스틱 회귀](../Machine-Learning/Logistic-Regression.md)
- 다음: [역전파](Backpropagation.md), [활성화 함수](Activation-Functions.md)

## 참조 (References)

- [Math/Linear-Algebra/Matrices.md](../../Math/Linear-Algebra/Matrices.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
