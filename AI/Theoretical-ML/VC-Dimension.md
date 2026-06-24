# VC 차원 (VC Dimension)

- Level: Advanced
- Prerequisites: [PAC-Learning.md](PAC-Learning.md), [Math/Discrete/Set-Theory.md](../../Math/Discrete/Set-Theory.md), [Math/Probability-Statistics/Probability-Basics.md](../../Math/Probability-Statistics/Probability-Basics.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

VC 차원은 가설 클래스가 얼마나 다양한 라벨 패턴을 표현할 수 있는지 재는 척도다. 어떤 $n$개 점 집합에 대해 가능한 모든 $2^n$가지 이진 라벨링을 가설 클래스가 구현할 수 있으면 그 집합을 shatter한다고 한다. VC 차원은 shatter할 수 있는 가장 큰 점 집합의 크기다.

## 직관 (Intuition)

모델이 데이터 몇 개에 대해 어떤 정답 패턴이 오더라도 모두 맞출 수 있다면 표현력이 크다. 하지만 표현력이 클수록 훈련셋에 우연히 맞는 규칙도 더 많이 만들 수 있다. VC 차원은 이 “마음대로 맞추는 능력”을 데이터 점 개수 단위로 센다.

## 이론 (Theory)

가설 클래스 $H$의 VC 차원을 $d_{VC}$라고 쓰자. 예를 들어 1차원 threshold 분류기 $h_t(x)=1[x\ge t]$는 한 점은 shatter할 수 있지만 두 점의 라벨 패턴 `1,0`은 만들 수 없으므로 VC 차원이 1이다. 반면 실수 직선 위의 구간 분류기는 VC 차원이 2이다. $\mathbb{R}^p$의 선형 분류기는 일반 위치 조건에서 VC 차원이 $p+1$이다.

VC 차원의 중요성은 무한한 가설 클래스에도 표본 복잡도 경계를 줄 수 있다는 점이다. 대략적으로 이진 분류에서 realizable 설정의 표본 복잡도는

$$
O\left(\frac{d_{VC}\log(1/\epsilon)+\log(1/\delta)}{\epsilon}\right)
$$

이고, agnostic 설정에서는 보통 $\epsilon^{-2}$ 의존성이 나타난다. 정확한 상수보다 중요한 메시지는 `가설 개수` 대신 `표현 가능한 라벨 패턴의 성장률`이 일반화를 좌우한다는 것이다.

## 구현 (Implementation)

유한한 입력 집합과 유한한 가설 집합에서는 shattering 여부를 직접 확인할 수 있다.

```python
from itertools import product


def labels_of(h, points):
    return tuple(h(x) for x in points)


def shatters(hypotheses, points):
    observed = {labels_of(h, points) for h in hypotheses}
    all_patterns = set(product([0, 1], repeat=len(points)))
    return observed == all_patterns


points = [0.2, 0.7]
thresholds = [-1.0, 0.5, 1.0]
hypotheses = [lambda x, t=t: int(x >= t) for t in thresholds]

print(shatters(hypotheses, points))  # False: 패턴 (1, 0)을 만들 수 없음
```

연속 공간의 실제 VC 차원 증명은 조합론과 기하학을 사용한다. 코드는 개념 확인용이다.

## 복잡도 (Complexity)

직접 shattering을 검사하면 점 $n$개에 대해 $2^n$개 라벨 패턴을 다뤄야 하므로 빠르게 폭발한다. 이론 분석에서는 성장 함수, Sauer-Shelah lemma, 기하학적 성질을 사용해 직접 열거를 피한다.

## 응용 (Applications)

- 선형 모델, 결정 트리, 신경망의 표현력 분석
- PAC 학습 가능성 판단
- 표본 수와 모델 복잡도 사이의 정성적 관계 설명
- 구조적 위험 최소화(structural risk minimization)

## 흔한 오해 (Common Misunderstandings)

- VC 차원이 크다고 항상 성능이 나쁜 것은 아니다. 데이터 분포, 최적화, 규제, inductive bias가 함께 작동한다.
- 파라미터 수와 VC 차원은 관련이 있지만 항상 같지 않다.
- VC 차원은 특정 데이터셋의 라벨 난이도가 아니라 가설 클래스의 최악 경우 표현력이다.
- 현대 딥러닝 일반화를 VC 차원만으로 설명하기에는 부족한 경우가 많다.

## TMI

- Sauer-Shelah lemma는 VC 차원이 유한하면 가능한 라벨 패턴 수가 지수적으로 계속 늘지 않고 다항식으로 제한됨을 보여준다.
- 신경망의 VC 차원은 파라미터 수와 활성화 함수에 따라 상계가 알려져 있지만, 실제 일반화 성능을 날카롭게 예측하지는 못하는 경우가 많다.
- VC 이론은 통계학의 uniform convergence와 계산 학습 이론을 잇는 고전적 다리다.

## 연습 / 확인 문제 (Exercises)

- 1차원 threshold의 VC 차원이 1임을 보이라.
- 1차원 구간 분류기의 VC 차원이 2임을 보이고, 3이 아님을 설명하라.
- 2차원 선형 분류기가 세 점을 shatter할 수 있는 예와 네 점을 항상 shatter할 수 없는 이유를 찾아보라.

## 이어서 읽기 (Reading Path)

- 이전: [PAC 학습](PAC-Learning.md)
- 다음: [Rademacher 복잡도](Rademacher-Complexity.md)

## 참조 (References)

- [PAC-Learning.md](PAC-Learning.md)
- [Math/Discrete/Set-Theory.md](../../Math/Discrete/Set-Theory.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
