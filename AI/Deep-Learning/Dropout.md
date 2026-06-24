# 드롭아웃 (Dropout)

- Level: Intermediate
- Prerequisites: [AI/Deep-Learning/MLP.md](MLP.md), [AI/Machine-Learning/Regularization.md](../Machine-Learning/Regularization.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

드롭아웃은 훈련 중 activation 일부를 무작위로 0으로 만들어 co-adaptation을 줄이는 신경망 규제 방법이다. 추론 때는 모든 unit을 사용하며 일반적으로 inverted dropout이 훈련 중 scale을 보정한다.

## 직관 (Intuition)

매번 일부 팀원이 빠진 상태에서도 문제를 풀게 하면 한 경로에만 의존하기 어렵다. 다양한 부분 네트워크를 공유 파라미터로 학습하고 추론 때 결합하는 효과를 낸다.

## 이론 (Theory)

keep probability $q=1-p$와 mask $m_i\sim Bernoulli(q)$에 대해 inverted dropout은

$$\tilde h_i=\frac{m_i}{q}h_i$$

로 훈련한다. 그러면 $E[\tilde h_i]=h_i$여서 추론 때 추가 scale 변경이 필요 없다. dropout rate가 너무 크면 정보와 gradient가 과도하게 사라져 underfitting할 수 있다.

## 구현 (Implementation)

```python
import numpy as np


def dropout(x, rate, training, rng):
    if not training or rate == 0:
        return x
    keep = 1.0 - rate
    mask = rng.random(x.shape) < keep
    return x * mask / keep
```

## 복잡도 (Complexity)

원소 수 $N$에 대해 mask 생성과 곱은 `O(N)`, mask 저장은 backward를 위해 `O(N)`이다. 추론에서는 보통 추가 비용이 없다.

## 응용 (Applications)

- MLP와 classification head 규제
- attention weight·residual branch dropout
- Monte Carlo dropout 기반 불확실성 근사
- 작은 데이터의 과적합 완화

## 흔한 오해 (Common Misunderstandings)

- 추론 때 dropout을 켜 두면 보통 예측이 무작위가 된다.
- dropout이 데이터 누출이나 잘못된 평가를 해결하지 않는다.
- 모든 아키텍처와 데이터 규모에서 필수는 아니다.
- rate는 버리는 비율인지 유지 비율인지 API 문서를 확인해야 한다.

## TMI

- dropout은 많은 부분 네트워크의 근사 ensemble로 해석할 수 있다.
- BatchNorm과 함께 쓸 때 noise 상호작용과 위치를 고려해야 한다.
- stochastic depth는 unit 대신 residual block 전체를 무작위로 건너뛴다.

## 연습 / 확인 문제 (Exercises)

- inverted scaling이 기댓값을 보존함을 보이라.
- train/eval 모드에서 같은 입력의 출력을 비교하라.
- dropout rate를 바꾸며 train/validation gap을 관찰하라.

## 이어서 읽기 (Reading Path)

- 이전: [정규화 층](Normalization-Layers.md)
- 다음: [CNN](CNN.md)

## 참조 (References)

- [AI/Machine-Learning/Regularization.md](../Machine-Learning/Regularization.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Papers.md](../../Reference/Papers.md)
