# 활성화 함수 (Activation Functions)

- Level: Intermediate
- Prerequisites: [AI/Deep-Learning/MLP.md](MLP.md), [Math/Calculus/Differentiation.md](../../Math/Calculus/Differentiation.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

활성화 함수는 신경망 층의 선형 출력에 비선형성을 더한다. ReLU, sigmoid, tanh, GELU 등이 있으며 hidden layer와 output layer에서 목적이 다르다.

## 직관 (Intuition)

선형 변환만 여러 번 쌓으면 결국 한 번의 선형 변환이다. 활성화 함수가 입력 공간을 꺾고 눌러 여러 층이 복잡한 패턴을 표현하게 한다.

## 이론 (Theory)

$$\operatorname{ReLU}(x)=\max(0,x),\quad
\sigma(x)=\frac{1}{1+e^{-x}},\quad
\tanh(x)=\frac{e^x-e^{-x}}{e^x+e^{-x}}$$

ReLU는 양수에서 gradient가 일정해 학습이 쉽지만 음수 영역에서 dead unit이 생길 수 있다. sigmoid와 tanh는 큰 절댓값에서 포화되어 gradient가 작아진다. GELU는 입력 크기에 따라 부드럽게 gating하며 Transformer에서 흔하다.

출력층은 binary classification의 sigmoid, mutually exclusive multiclass의 softmax, 회귀의 identity처럼 손실과 확률모형에 맞춰 선택한다.

## 구현 (Implementation)

```python
import math


def relu(x):
    return max(0.0, x)


def sigmoid(x):
    if x >= 0:
        return 1 / (1 + math.exp(-x))
    e = math.exp(x)
    return e / (1 + e)
```

## 복잡도 (Complexity)

activation 원소 수를 $N$이라 하면 forward와 backward는 `O(N)`, 출력 저장도 `O(N)`이다. 실제 비용은 주변 matrix multiplication보다 작지만 kernel fusion과 메모리 이동이 중요하다.

## 응용 (Applications)

- MLP·CNN·Transformer hidden layer
- 확률 출력과 gating
- sparse activation과 conditional computation
- 신경망 표현력 부여

## 흔한 오해 (Common Misunderstandings)

- 모든 층에 sigmoid를 쓰는 것이 확률적이라는 뜻은 아니다.
- ReLU는 0에서 미분 불가능하지만 subgradient 관례로 학습한다.
- softmax 값은 합이 1이어도 calibration된 확률을 보장하지 않는다.
- 활성화 선택만으로 vanishing gradient가 완전히 해결되지는 않는다.

## TMI

- Leaky ReLU는 음수 구간에 작은 기울기를 남긴다.
- Swish/SiLU와 GELU는 매끄럽고 비단조인 구간을 가진다.
- activation 분포는 초기화와 normalization 설계에 직접 영향을 준다.

## 연습 / 확인 문제 (Exercises)

- sigmoid derivative가 $\sigma(x)(1-\sigma(x))$임을 유도하라.
- 큰 양수·음수에서 각 activation과 derivative를 비교하라.
- ReLU dead unit이 생기는 update 예를 만들어라.

## 이어서 읽기 (Reading Path)

- 이전: [MLP](MLP.md)
- 다음: [손실 함수](Loss-Functions.md), [정규화 층](Normalization-Layers.md)

## 참조 (References)

- [Math/Calculus/Differentiation.md](../../Math/Calculus/Differentiation.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Papers.md](../../Reference/Papers.md)
