# do-calculus

- Level: Advanced
- Prerequisites: [SCM.md](SCM.md), [AI/PGMs/d-Separation.md](../PGMs/d-Separation.md), [Math/Probability-Statistics/Bayes-Theorem.md](../../Math/Probability-Statistics/Bayes-Theorem.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

do-calculus는 개입분포 $P(Y\mid do(X=x))$를 관측분포로 바꿀 수 있는지 판단하고 변형하는 규칙 체계다. 그래프의 d-분리 조건을 이용해 관측, 개입, 조건화를 서로 삽입·삭제·교환한다.

## 직관 (Intuition)

우리는 보통 관측 데이터만 가진다. 하지만 궁금한 것은 “X를 강제로 바꾸면 Y가 어떻게 변하는가”다. do-calculus는 인과 그래프가 충분한 구조를 줄 때, 개입이라는 보이지 않는 실험을 관측 데이터의 조합으로 계산하는 대수적 도구다.

## 이론 (Theory)

조건화와 개입은 다르다.

$$
P(Y\mid X=x) \neq P(Y\mid do(X=x))
$$

일 수 있다. 예를 들어 공통 원인 $Z$가 $X$와 $Y$를 모두 만들면 관측 조건화에는 confounding이 섞인다. 이때 backdoor 조정이 가능하면

$$
P(Y\mid do(X=x))=\sum_z P(Y\mid X=x,Z=z)P(Z=z)
$$

로 표현된다.

do-calculus의 세 규칙은 그래프에서 특정 d-분리 조건이 성립할 때 다음 조작을 허용한다.

- 관측의 삽입/삭제: 어떤 관측 변수가 결과와 독립이면 조건식에서 넣거나 뺄 수 있다.
- 개입과 관측의 교환: 어떤 개입을 관측 조건으로 바꿔도 되는 경우를 판정한다.
- 개입의 삽입/삭제: 어떤 개입이 결과 분포에 영향을 주지 않으면 제거할 수 있다.

정확한 판정은 간선을 제거한 mutilated graph에서의 d-분리로 한다. 따라서 do-calculus는 단순한 공식 암기가 아니라 그래프 조작과 독립성 판정의 조합이다.

## 구현 (Implementation)

backdoor 조정이 가능한 경우의 이산 ATE 계산은 다음처럼 쓸 수 있다.

```python
def backdoor_mean(p_z, mean_y_given_xz, x):
    total = 0.0
    for z, p in p_z.items():
        total += mean_y_given_xz[(x, z)] * p
    return total


p_z = {"low": 0.4, "high": 0.6}
mean_y_given_xz = {
    (0, "low"): 1.0,
    (1, "low"): 2.0,
    (0, "high"): 3.0,
    (1, "high"): 3.5,
}

ate = backdoor_mean(p_z, mean_y_given_xz, 1) - backdoor_mean(p_z, mean_y_given_xz, 0)
print(round(ate, 3))
```

do-calculus는 backdoor보다 넓은 상황을 다루지만, 실무에서는 먼저 backdoor/frontdoor 같은 알려진 패턴을 확인하는 경우가 많다.

## 복잡도 (Complexity)

단일 조정 공식 계산은 변수 수와 도메인 크기에 따라 합산 비용이 든다. 일반적인 식별 알고리즘은 그래프 구조를 분석하며, 계산된 estimand는 고차원 합이나 적분을 포함할 수 있다. 이론적으로 어려운 부분은 가능한 변형을 찾는 식별 단계다.

## 응용 (Applications)

- 관측 데이터에서 개입 효과 식별
- backdoor/frontdoor adjustment 정당화
- 인과 그래프 기반 실험 설계
- 정책 시뮬레이션과 counterfactual 분석의 기반

## 흔한 오해 (Common Misunderstandings)

- do-calculus는 그래프 가정이 맞을 때만 유효하다.
- 모든 개입 효과를 관측 데이터로 식별할 수 있는 것은 아니다.
- 공변량을 전부 조정하는 것이 do-calculus의 결론은 아니다.
- 공식 하나를 적용하기보다 어떤 그래프에서 어떤 d-분리가 성립하는지 확인해야 한다.

## TMI

- do-calculus는 완전성 결과를 갖는다. 식별 가능한 효과라면 적절한 규칙 적용으로 도출할 수 있다.
- frontdoor criterion은 직접 confounding이 있어도 매개 변수를 통해 효과를 식별할 수 있는 유명한 예다.
- 실제 데이터 분석에서는 식별 이후에도 추정량의 편향, 분산, positivity 문제가 남는다.

## 연습 / 확인 문제 (Exercises)

- backdoor criterion이 성립하는 작은 그래프를 그리고 조정 공식을 써라.
- $P(Y\mid X=x)$가 $P(Y\mid do(X=x))$와 같아지는 조건을 설명하라.
- collider를 조정하면 backdoor path가 어떻게 열릴 수 있는지 예를 들어라.

## 이어서 읽기 (Reading Path)

- 이전: [구조적 인과 모델](SCM.md)
- 다음: [식별가능성](Identifiability.md)

## 참조 (References)

- [SCM.md](SCM.md)
- [AI/PGMs/d-Separation.md](../PGMs/d-Separation.md)
- [Math/Probability-Statistics/Bayes-Theorem.md](../../Math/Probability-Statistics/Bayes-Theorem.md)
- [Reference/Books.md](../../Reference/Books.md)
