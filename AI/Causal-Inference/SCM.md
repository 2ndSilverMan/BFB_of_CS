# 구조적 인과 모델 (Structural Causal Model)

- Level: Advanced
- Prerequisites: [Potential-Outcomes.md](Potential-Outcomes.md), [AI/PGMs/Bayesian-Networks.md](../PGMs/Bayesian-Networks.md), [AI/PGMs/d-Separation.md](../PGMs/d-Separation.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

구조적 인과 모델(SCM)은 각 변수가 부모 변수와 외생 잡음의 함수로 생성된다고 보는 인과 모델이다. 그래프는 변수 간 직접 인과 관계를 나타내고, 구조 방정식은 개입과 반사실을 계산할 수 있게 한다.

## 직관 (Intuition)

상관관계 모델은 “함께 어떻게 움직이는가”를 말한다. SCM은 한 걸음 더 나아가 “어떤 손잡이를 강제로 돌리면 나머지가 어떻게 바뀌는가”를 묻는다. 방정식이 있기 때문에 관측뿐 아니라 개입, 그리고 다른 세계의 결과까지 이야기할 수 있다.

## 이론 (Theory)

SCM은 보통 세 요소로 구성된다.

- 내생 변수 $V$: 모델 안에서 설명할 변수
- 외생 변수 $U$: 모델 밖의 잡음과 배경 요인
- 구조 방정식 $F$: 각 $V_i=f_i(Pa_i, U_i)$

예를 들어

$$
X=f_X(U_X),\quad Y=f_Y(X,U_Y)
$$

라면 $X$는 $Y$의 직접 원인이다. 개입 $do(X=x)$는 $X$의 원래 방정식을 제거하고 $X=x$로 고정하는 graph surgery로 표현한다. 이때 관측 조건화 $P(Y\mid X=x)$와 개입분포 $P(Y\mid do(X=x))$는 일반적으로 다르다.

반사실 추론은 보통 세 단계로 설명된다.

1. Abduction: 관측된 사실로 외생 변수에 대한 믿음을 갱신한다.
2. Action: 관심 개입으로 구조 방정식을 바꾼다.
3. Prediction: 수정된 모델에서 결과를 계산한다.

## 구현 (Implementation)

간단한 선형 SCM에서 관측 조건화와 개입을 분리해 볼 수 있다.

```python
def scm(u_x, u_y):
    x = u_x
    y = 2 * x + u_y
    return x, y


def intervene_y(do_x, u_y):
    # do(X=do_x): X 생성 방정식을 끊고 직접 고정
    x = do_x
    y = 2 * x + u_y
    return y


print(scm(u_x=1.0, u_y=0.5))
print(intervene_y(do_x=3.0, u_y=0.5))
```

실제 문제에서는 어떤 구조 방정식과 그래프를 가정할지, 어떤 변수들이 관측되는지가 핵심이다.

## 복잡도 (Complexity)

SCM 자체의 계산 비용은 방정식 형태에 따라 달라진다. 선형 Gaussian SCM은 닫힌형 계산이 가능하지만, 비선형·고차원 SCM은 sampling이나 optimization이 필요할 수 있다. 더 어려운 문제는 계산보다 식별가능성이다.

## 응용 (Applications)

- 개입 효과 추정
- 반사실 설명과 정책 시뮬레이션
- 인과 그래프 기반 feature selection
- AI 시스템의 인과적 해석 가능성 연구

## 흔한 오해 (Common Misunderstandings)

- SCM 그래프의 간선은 단순 상관이 아니라 구조적 개입 의미를 갖는다.
- 좋은 예측 모델이 곧 좋은 인과 모델은 아니다.
- $do(X=x)$와 $X=x$로 조건화하는 것은 다르다.
- SCM은 강한 가정을 요구한다. 그래프와 누락 변수 가정이 틀리면 결론도 흔들린다.

## TMI

- Pearl의 ladder of causation은 association, intervention, counterfactual을 구분한다.
- 같은 관측분포를 만드는 여러 SCM이 서로 다른 인과 효과를 가질 수 있다.
- SCM은 잠재 결과의 $Y(x)$를 구조 방정식에서의 개입 결과로 해석하게 해준다.

## 연습 / 확인 문제 (Exercises)

- $Z\to X\to Y$와 $Z\to Y$가 있는 SCM에서 confounding path를 찾아라.
- $P(Y\mid X=x)$와 $P(Y\mid do(X=x))$가 다른 예를 설명하라.
- graph surgery가 어떤 방정식을 제거하는지 작은 예로 써라.

## 이어서 읽기 (Reading Path)

- 이전: [잠재 결과](Potential-Outcomes.md)
- 다음: [do-calculus](Do-Calculus.md)

## 참조 (References)

- [Potential-Outcomes.md](Potential-Outcomes.md)
- [AI/PGMs/Bayesian-Networks.md](../PGMs/Bayesian-Networks.md)
- [AI/PGMs/d-Separation.md](../PGMs/d-Separation.md)
- [Reference/Books.md](../../Reference/Books.md)
