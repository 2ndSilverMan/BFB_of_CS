# PAC 학습 프레임워크 (PAC Learning)

- Level: Advanced
- Prerequisites: [AI/Machine-Learning/Overfitting.md](../Machine-Learning/Overfitting.md), [Math/Probability-Statistics/Probability-Basics.md](../../Math/Probability-Statistics/Probability-Basics.md), [Math/Real-Analysis/Real-Numbers.md](../../Math/Real-Analysis/Real-Numbers.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

PAC 학습은 학습 알고리즘이 “충분히 많은 표본을 받으면 높은 확률로 거의 맞는 가설을 반환하는가?”를 묻는 이론적 틀이다. PAC는 Probably Approximately Correct의 약자로, `probably`는 실패 확률 $\delta$가 작다는 뜻이고 `approximately correct`는 실제 위험 $R(h)$가 목표 오차 $\epsilon$ 이하라는 뜻이다.

## 직관 (Intuition)

시험 문제 몇 개를 보고 전체 과목을 이해했다고 말하려면 두 가지가 필요하다. 첫째, 표본 시험이 과목 전체를 어느 정도 대표해야 한다. 둘째, 답안을 맞힌 방식이 우연한 암기가 아니라 문제군 전체에 통하는 규칙이어야 한다. PAC 학습은 이 두 조건을 $\epsilon$, $\delta$, 표본 수 $m$의 관계로 표현한다.

## 이론 (Theory)

입력 공간을 $X$, 라벨을 $Y$, 가설 집합을 $H$, 데이터 분포를 $D$라고 하자. 손실 $\ell(h(x), y)$에 대해 실제 위험은

$$
R(h)=E_{(x,y)\sim D}[\ell(h(x),y)]
$$

이고 경험 위험은

$$
\hat R_S(h)=\frac{1}{m}\sum_{i=1}^{m}\ell(h(x_i),y_i)
$$

이다. 실현 가능(realizable) PAC 설정에서는 어떤 목표 개념 $c \in H$가 데이터 라벨을 완벽히 생성한다고 가정한다. 이때 일관된 가설을 찾는 학습기가 표본 수

$$
m \gtrsim \frac{1}{\epsilon}\left(\log |H|+\log\frac{1}{\delta}\right)
$$

을 받으면, 유한한 $H$에 대해 $R(h)\le\epsilon$을 확률 $1-\delta$ 이상으로 보장할 수 있다. 잡음이 있거나 목표가 $H$ 안에 없을 수 있는 agnostic 설정에서는 일반적으로 $\epsilon^{-2}$ 의존성이 등장한다.

핵심은 훈련 오차가 작다는 사실만으로는 부족하고, 가설 공간의 크기나 복잡도를 함께 제어해야 한다는 점이다. 무한 가설 공간에서는 단순한 $|H|$ 대신 [VC 차원](VC-Dimension.md), Rademacher 복잡도 같은 도구를 사용한다.

## 구현 (Implementation)

아주 작은 유한 가설 집합에서는 경험 위험 최소화(ERM)를 그대로 구현할 수 있다.

```python
def empirical_risk(h, sample):
    return sum(h(x) != y for x, y in sample) / len(sample)


def erm(hypotheses, sample):
    return min(hypotheses, key=lambda h: empirical_risk(h, sample))


# 1차원 threshold 가설: x >= t 이면 1
thresholds = [0.2, 0.5, 0.8]
hypotheses = [lambda x, t=t: int(x >= t) for t in thresholds]
sample = [(0.1, 0), (0.4, 0), (0.7, 1), (0.9, 1)]

best = erm(hypotheses, sample)
print([best(x) for x, _ in sample])
```

실제 연구에서는 ERM 구현 자체보다 “이 ERM이 어떤 표본 수에서 일반화되는가”를 분석하는 쪽이 PAC 프레임워크의 역할이다.

## 복잡도 (Complexity)

PAC 학습에는 두 종류의 복잡도가 있다.

- 표본 복잡도: 원하는 $\epsilon,\delta$를 달성하는 데 필요한 데이터 수
- 계산 복잡도: 그런 가설을 실제로 찾는 데 드는 시간

표본 복잡도가 낮아도 최적 가설을 찾는 문제가 NP-hard일 수 있다. 반대로 계산은 쉬워도 표본이 부족하면 일반화 보장은 약하다.

## 응용 (Applications)

- 모델 클래스가 학습 가능한지 판단
- 데이터 수와 일반화 오차의 관계 추정
- 유한 가설 집합, 선형 분류기, 결정 트리 등의 이론적 분석
- agnostic learning, online learning, bandit 이론의 출발점

## 흔한 오해 (Common Misunderstandings)

- PAC 보장은 특정 테스트셋 점수가 아니라 미지의 분포에 대한 확률적 보장이다.
- $\delta$는 오차 크기가 아니라 보장이 실패할 확률이다.
- 표본 복잡도 보장이 있다고 해서 효율적인 알고리즘이 자동으로 존재하는 것은 아니다.
- PAC 설정은 데이터가 독립 동일분포(i.i.d.)라는 강한 가정을 자주 사용한다.

## TMI

- “학습 가능하다”는 말은 보통 모든 분포에 대해 다항 표본 수로 $\epsilon,\delta$ 보장이 가능하다는 뜻으로 쓰인다.
- No-Free-Lunch 류 결과는 분포나 가설 공간에 아무 구조도 두지 않으면 일반화 보장을 할 수 없다는 사실을 보여준다.
- VC 차원은 PAC 학습 가능성과 깊게 연결되어, 이진 분류에서 유한 VC 차원은 분포 독립 학습 가능성의 핵심 조건이 된다.

## 연습 / 확인 문제 (Exercises)

- 유한한 $|H|$에 대해 일관된 가설의 실패 확률을 union bound로 유도하라.
- $\epsilon=0.05$, $\delta=0.01$, $|H|=1000$일 때 realizable PAC 표본 수의 대략적인 크기를 계산하라.
- “훈련 오차 0”과 “PAC 일반화 보장”의 차이를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [과적합과 일반화](../Machine-Learning/Overfitting.md)
- 다음: [VC 차원](VC-Dimension.md)

## 참조 (References)

- [AI/Machine-Learning/Overfitting.md](../Machine-Learning/Overfitting.md)
- [Math/Probability-Statistics/Probability-Basics.md](../../Math/Probability-Statistics/Probability-Basics.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
