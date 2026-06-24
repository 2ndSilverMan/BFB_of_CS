# Rademacher 복잡도 (Rademacher Complexity)

- Level: Advanced
- Prerequisites: [VC-Dimension.md](VC-Dimension.md), [Math/Probability-Statistics/Expectation.md](../../Math/Probability-Statistics/Expectation.md), [AI/Machine-Learning/Overfitting.md](../Machine-Learning/Overfitting.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

Rademacher 복잡도는 함수 클래스가 무작위 라벨을 얼마나 잘 맞출 수 있는지 측정하는 데이터 의존 복잡도다. 무작위 부호 $\sigma_i \in \{-1,+1\}$를 붙였을 때 함수 클래스가 그 부호들과 크게 상관될 수 있다면 복잡도가 크다.

## 직관 (Intuition)

진짜 패턴이 없는 동전 던지기 라벨에도 모델이 잘 맞춘다면 그 모델은 우연한 잡음까지 흡수할 힘이 있다. Rademacher 복잡도는 “랜덤 잡음을 외울 수 있는 능력”을 수치화한다. 작을수록 경험 위험과 실제 위험의 간격을 더 잘 제어할 수 있다.

## 이론 (Theory)

표본 $S=(x_1,\dots,x_n)$과 함수 클래스 $F$에 대해 경험적 Rademacher 복잡도는

$$
\hat{\mathfrak R}_S(F)
=E_\sigma\left[\sup_{f\in F}\frac{1}{n}\sum_{i=1}^{n}\sigma_i f(x_i)\right]
$$

로 정의한다. 여기서 $\sigma_i$는 독립 Rademacher 변수다. 손실 함수 클래스에 대한 Rademacher 복잡도가 작으면 높은 확률로 모든 $f\in F$에 대해

$$
R(f) \le \hat R_S(f) + 2\hat{\mathfrak R}_S(\ell\circ F)
 + O\left(\sqrt{\frac{\log(1/\delta)}{n}}\right)
$$

형태의 일반화 경계를 얻는다.

VC 차원이 최악 경우 조합적 표현력을 보는 반면, Rademacher 복잡도는 실제 표본 위치와 함수 값 스케일을 반영한다. 그래서 margin, norm constraint, kernel, 신경망 norm bound 같은 분석에서 자주 등장한다.

## 구현 (Implementation)

유한한 함수 클래스에서는 무작위 부호를 여러 번 샘플링해 경험적 Rademacher 복잡도를 근사할 수 있다.

```python
import random


def empirical_rademacher(functions, xs, trials=1000):
    n = len(xs)
    total = 0.0
    for _ in range(trials):
        sigmas = [random.choice([-1, 1]) for _ in xs]
        best = max(
            sum(s * f(x) for s, x in zip(sigmas, xs)) / n
            for f in functions
        )
        total += best
    return total / trials


functions = [
    lambda x: 1 if x >= 0.3 else -1,
    lambda x: 1 if x >= 0.6 else -1,
    lambda x: -1,
    lambda x: 1,
]

print(round(empirical_rademacher(functions, [0.1, 0.4, 0.9]), 3))
```

큰 모델에서는 함수 클래스 전체를 열거할 수 없으므로 norm bound나 Lipschitz 성질을 이용해 상계를 구한다.

## 복잡도 (Complexity)

유한 함수 $|F|$개, 표본 $n$개, Monte Carlo 반복 $B$번이면 단순 근사는 $O(B|F|n)$이다. 무한 함수 클래스의 정확한 복잡도 계산은 일반적으로 어렵고, 분석 가능한 상계를 사용한다.

## 응용 (Applications)

- 일반화 경계 도출
- margin classifier와 boosting 분석
- kernel method, norm-constrained linear model 분석
- 딥러닝에서 norm 기반 capacity bound 연구

## 흔한 오해 (Common Misunderstandings)

- Rademacher 복잡도는 모델의 테스트 성능을 직접 예측하는 점수가 아니다.
- 훈련 라벨과 무작위 부호를 헷갈리면 안 된다. 핵심은 “진짜 구조가 없는 라벨”을 얼마나 맞추는가다.
- 데이터 의존 복잡도라고 해서 모든 분포 이동 문제를 해결하지는 않는다.
- 작은 Rademacher 복잡도는 충분조건에 가깝고, 필요한 모든 설명은 아니다.

## TMI

- symmetrization은 Rademacher 복잡도 경계를 유도하는 핵심 테크닉이다.
- contraction lemma는 Lipschitz 손실을 합성해도 복잡도가 통제됨을 보여준다.
- 실제 딥러닝 일반화에서는 Rademacher bound가 너무 느슨한 경우가 많지만, “잡음 적합 능력”이라는 직관은 여전히 유용하다.

## 연습 / 확인 문제 (Exercises)

- 상수 함수 두 개만 있는 클래스의 경험적 Rademacher 복잡도를 손으로 계산하라.
- 함수 클래스가 커질수록 $\sup$ 값이 왜 줄어들 수 없는지 설명하라.
- VC 차원과 Rademacher 복잡도가 각각 어떤 정보를 반영하는지 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [VC 차원](VC-Dimension.md)
- 다음: [일반화 경계](Generalization-Bounds.md)

## 참조 (References)

- [VC-Dimension.md](VC-Dimension.md)
- [Math/Probability-Statistics/Expectation.md](../../Math/Probability-Statistics/Expectation.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
