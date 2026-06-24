# 인수 분해와 조건부 독립 (Factorization and Conditional Independence)

- Level: Advanced
- Prerequisites: [Graph-Review.md](Graph-Review.md), [Math/Probability-Statistics/Probability-Basics.md](../../Math/Probability-Statistics/Probability-Basics.md), [Math/Probability-Statistics/Bayes-Theorem.md](../../Math/Probability-Statistics/Bayes-Theorem.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

인수 분해는 큰 결합분포를 작은 factor들의 곱으로 표현하는 방법이다. 조건부 독립은 어떤 변수를 알고 나면 다른 변수에 대한 정보가 추가로 필요 없다는 성질이며, PGM이 결합분포를 작게 표현할 수 있게 하는 핵심이다.

## 직관 (Intuition)

모든 변수의 조합을 하나의 거대한 표로 만들면 금방 폭발한다. 하지만 “날씨를 알면 우산 사용과 잔디 젖음은 각각 간단히 설명된다”처럼 구조를 알면 큰 표를 작은 표 여러 개로 쪼갤 수 있다.

## 이론 (Theory)

조건부 독립은 다음처럼 쓴다.

$$
X \perp Y \mid Z
$$

이는

$$
P(X,Y\mid Z)=P(X\mid Z)P(Y\mid Z)
$$

와 동치인 경우가 많다. 방향 그래프 모델에서는 결합분포가

$$
P(X_1,\dots,X_n)=\prod_i P(X_i\mid Pa(X_i))
$$

로 인수분해된다. 무방향 그래프 모델에서는 clique 또는 factor 집합 $\mathcal{C}$에 대해

$$
P(X)=\frac{1}{Z}\prod_{C\in\mathcal{C}}\phi_C(X_C)
$$

형태로 쓴다. 여기서 $Z$는 정규화 상수(partition function)다.

## 구현 (Implementation)

두 factor의 곱은 공통 변수 할당이 일치할 때 값을 곱해 새 factor를 만든다.

```python
def compatible(a, b):
    return all(b.get(k, v) == v for k, v in a.items())


def merge_assignment(a, b):
    out = dict(a)
    out.update(b)
    return out


f1 = [({"A": 0}, 0.4), ({"A": 1}, 0.6)]
f2 = [({"A": 0, "B": 0}, 0.7), ({"A": 1, "B": 0}, 0.2)]

product = []
for a, va in f1:
    for b, vb in f2:
        if compatible(a, b):
            product.append((merge_assignment(a, b), va * vb))

print(product)
```

실제 inference engine은 factor 곱과 주변화를 효율적으로 조합한다.

## 복잡도 (Complexity)

factor 크기는 포함하는 변수 수에 지수적으로 증가한다. 독립성 구조가 factor scope를 작게 유지하면 표현과 추론 비용이 줄어든다. 반대로 큰 clique가 생기면 계산이 어려워진다.

## 응용 (Applications)

- 베이지안 네트워크의 CPD 분해
- MRF와 factor graph 모델링
- 변수 소거와 belief propagation의 계산 단위
- 조건부 독립성 기반 구조 학습

## 흔한 오해 (Common Misunderstandings)

- 인수분해는 단순한 표기법이 아니라 독립성 가정을 포함한다.
- factor는 항상 확률분포일 필요는 없다. 양수 compatibility 함수일 수 있다.
- 조건부 독립은 주변 독립과 다르다.
- 관측 변수를 추가로 조건화하면 독립성이 생기기도 하지만 깨지기도 한다.

## TMI

- partition function $Z$ 계산이 MRF에서 큰 병목이 되는 경우가 많다.
- factor graph는 같은 인수분해를 더 세밀하게 보여주는 bipartite graph다.
- 조건부 독립성은 확률 추론뿐 아니라 인과 추론의 조정 변수 선택에도 중요하다.

## 연습 / 확인 문제 (Exercises)

- $X\perp Y\mid Z$의 의미를 확률식으로 써라.
- $P(A,B,C)=P(A)P(B\mid A)P(C\mid B)$가 어떤 조건부 독립을 암시하는지 설명하라.
- factor scope가 커질수록 계산 비용이 왜 지수적으로 늘어나는지 예로 보이라.

## 이어서 읽기 (Reading Path)

- 이전: [그래프 복습](Graph-Review.md)
- 다음: [베이지안 네트워크](Bayesian-Networks.md)

## 참조 (References)

- [Graph-Review.md](Graph-Review.md)
- [Math/Probability-Statistics/Probability-Basics.md](../../Math/Probability-Statistics/Probability-Basics.md)
- [Math/Probability-Statistics/Bayes-Theorem.md](../../Math/Probability-Statistics/Bayes-Theorem.md)
- [Reference/Books.md](../../Reference/Books.md)
