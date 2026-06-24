# Shattering과 성장 함수 (Shattering and Growth Function)

- Level: Advanced
- Prerequisites: [VC-Dimension.md](VC-Dimension.md), [PAC-Learning.md](PAC-Learning.md), [Math/Discrete/Combinatorics.md](../../Math/Discrete/Combinatorics.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

Shattering은 가설 클래스가 어떤 점 집합에 대해 가능한 모든 이진 라벨링을 구현할 수 있는 성질이다. 성장 함수(growth function)는 점 $m$개에 대해 가설 클래스가 만들 수 있는 최대 라벨 패턴 수를 나타낸다.

## 직관 (Intuition)

모델이 점 3개에 대해 8가지 라벨 조합을 전부 만들 수 있다면 그 점 3개를 완전히 마음대로 분류할 수 있다. 하지만 점이 늘어나면 언젠가 만들 수 없는 라벨 패턴이 생긴다. 그 한계가 VC 차원으로 이어진다.

## 이론 (Theory)

가설 클래스 $H$와 점 집합 $S=\{x_1,\dots,x_m\}$에 대해 가능한 dichotomy 수는

$$
|\{(h(x_1),\dots,h(x_m)):h\in H\}|
$$

이다. 성장 함수는 이를 모든 $m$개 점 집합에 대해 최대로 만든 값이다.

$$
\Pi_H(m)=\max_{|S|=m}|\{(h(x_1),\dots,h(x_m)):h\in H\}|
$$

$\Pi_H(m)=2^m$이면 어떤 $m$개 점 집합을 shatter할 수 있다. VC 차원은 $\Pi_H(m)=2^m$가 가능한 가장 큰 $m$이다.

Sauer-Shelah lemma는 VC 차원이 $d$인 클래스에 대해 $m>d$이면 성장 함수가 지수 $2^m$이 아니라 대략 $O(m^d)$로 제한됨을 보여준다. 이것이 무한 가설 클래스에도 일반화 경계를 줄 수 있는 이유다.

## 구현 (Implementation)

유한한 가설 집합과 점 집합에서는 가능한 라벨 패턴 수를 직접 셀 수 있다.

```python
def label_patterns(hypotheses, points):
    return {tuple(h(x) for x in points) for h in hypotheses}


thresholds = [-1.0, 0.3, 0.8, 2.0]
hypotheses = [lambda x, t=t: int(x >= t) for t in thresholds]
points = [0.2, 0.5]

patterns = label_patterns(hypotheses, points)
print(patterns)
print("shattered?", len(patterns) == 2 ** len(points))
```

연속 가설 클래스에서는 직접 열거가 아니라 증명으로 shattering 가능성과 불가능성을 보인다.

## 복잡도 (Complexity)

점 $m$개에 대한 모든 라벨 패턴은 $2^m$개라서 직접 검사는 지수적으로 커진다. 이론에서는 조합적 상계와 기하학적 논증으로 이를 피한다.

## 응용 (Applications)

- VC 차원 증명
- PAC 학습의 표본 복잡도 분석
- 모델 표현력의 조합적 해석
- 구조적 위험 최소화의 이론적 기반

## 흔한 오해 (Common Misunderstandings)

- 한 데이터셋을 잘 맞춘다고 그 크기의 모든 점 집합을 shatter한다는 뜻은 아니다.
- 성장 함수는 특정 점 집합이 아니라 최악 또는 최대 경우를 본다.
- VC 차원이 낮아도 특정 분포에서는 좋은 성능을 낼 수 있다.
- shattering은 라벨이 이진일 때 가장 표준적으로 정의된다.

## TMI

- 선형 분류기의 VC 차원 증명은 affine independence와 Radon's theorem 같은 기하학과 연결된다.
- 성장 함수는 empirical process theory의 covering number와 비슷하게 capacity를 제한하는 역할을 한다.
- “모든 라벨링을 구현한다”는 말은 잡음까지 외울 수 있는 능력을 포함한다.

## 연습 / 확인 문제 (Exercises)

- 1차원 threshold가 두 점을 shatter하지 못하는 라벨 패턴을 쓰라.
- 성장 함수와 VC 차원의 관계를 정의로 설명하라.
- Sauer-Shelah lemma가 일반화 경계에 왜 중요한지 직관적으로 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [VC 차원](VC-Dimension.md)
- 다음: [No-Free-Lunch](No-Free-Lunch.md)

## 참조 (References)

- [VC-Dimension.md](VC-Dimension.md)
- [PAC-Learning.md](PAC-Learning.md)
- [Math/Discrete/Combinatorics.md](../../Math/Discrete/Combinatorics.md)
- [Reference/Books.md](../../Reference/Books.md)
