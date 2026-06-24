# 적응형 최적화 방법 (Adaptive Optimization Methods)

- Level: Intermediate
- Prerequisites: [Math/Optimization/SGD.md](SGD.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

적응형 최적화 방법은 파라미터별 gradient의 과거 크기와 방향을 이용해 유효 학습률을 자동 조절한다. AdaGrad, RMSProp, Adam이 대표적이며, 서로 다른 스케일과 희소한 gradient를 가진 문제에서 빠른 초기 학습을 돕는다.

## 직관 (Intuition)

자주 크고 거친 gradient가 나타나는 방향에는 작은 걸음을, 드물고 작은 gradient가 나타나는 방향에는 상대적으로 큰 걸음을 준다. Adam은 여기에 momentum처럼 gradient의 평균 방향까지 추적해 속도와 스케일을 함께 보정한다.

## 이론 (Theory)

Adam은 gradient $g_t$의 1차·2차 모멘트 이동 평균을 계산한다.

$$
m_t=\beta_1m_{t-1}+(1-\beta_1)g_t,
\qquad v_t=\beta_2v_{t-1}+(1-\beta_2)g_t^2
$$

초기값 0의 편향을 보정해

$$
\hat m_t=\frac{m_t}{1-\beta_1^t},\quad
\hat v_t=\frac{v_t}{1-\beta_2^t},\quad
\theta_{t+1}=\theta_t-\eta\frac{\hat m_t}{\sqrt{\hat v_t}+\varepsilon}
$$

로 갱신한다. 모든 연산은 성분별이다. RMSProp은 주로 제곱 gradient 평균을, AdaGrad는 누적 제곱합을 사용한다. AdamW는 weight decay를 gradient 기반 update와 분리해 L2 규제와의 혼동을 줄인다.

## 구현 (Implementation)

```python
import math


def adam_1d(grad, x=0.0, lr=0.1, steps=100,
            beta1=0.9, beta2=0.999, eps=1e-8):
    m = v = 0.0
    for t in range(1, steps + 1):
        g = grad(x)
        m = beta1 * m + (1 - beta1) * g
        v = beta2 * v + (1 - beta2) * g * g
        m_hat = m / (1 - beta1 ** t)
        v_hat = v / (1 - beta2 ** t)
        x -= lr * m_hat / (math.sqrt(v_hat) + eps)
    return x


print(adam_1d(lambda x: 2 * (x - 3)))
```

## 복잡도 (Complexity)

파라미터 수가 $d$면 한 스텝의 gradient 외 update 비용은 `O(d)`이고, 1차·2차 모멘트를 저장해 추가 공간 `O(d)`가 필요하다. SGD보다 optimizer state 메모리가 약 두 배 더 든다.

## 응용 (Applications)

- Transformer와 대규모 신경망 학습
- 희소 임베딩과 불균일한 특징 스케일
- 빠른 baseline과 hyperparameter 탐색
- 비정상적·noisy gradient가 있는 온라인 학습

## 흔한 오해 (Common Misunderstandings)

- Adam이 모든 문제에서 SGD보다 좋은 최종 일반화를 보장하지 않는다.
- 적응형이라는 말이 학습률 선택이 불필요하다는 뜻은 아니다.
- Adam의 `epsilon`은 단순 반올림 장식이 아니라 수치 안정성과 update 크기에 영향을 줄 수 있다.
- L2 penalty를 Adam에 더하는 것과 decoupled weight decay는 일반적으로 같은 update가 아니다.

## TMI

- AdaGrad는 누적 제곱합이 계속 커져 학습률이 지나치게 작아질 수 있고, RMSProp은 지수 이동 평균으로 이를 완화한다.
- optimizer state는 mixed precision 대규모 모델에서 모델 가중치보다 더 많은 메모리를 차지할 수 있다.
- AMSGrad는 Adam의 수렴 반례를 보완하려고 2차 모멘트 상한을 단조롭게 유지한다.

## 연습 / 확인 문제 (Exercises)

- 편향 보정을 제거했을 때 초기 update가 어떻게 달라지는지 비교하라.
- SGD와 Adam으로 같은 이차함수를 최적화해 경로를 비교하라.
- AdamW와 L2 penalty update의 차이를 식으로 정리하라.

## 이어서 읽기 (Reading Path)

- 이전: [확률적 경사 하강법](SGD.md)
- 다음: [라그랑주 승수법](Lagrangian.md)

## 참조 (References)

- [Math/Optimization/SGD.md](SGD.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Papers.md](../../Reference/Papers.md)
- [Reference/Courses.md](../../Reference/Courses.md)
