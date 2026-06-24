# k-최근접 이웃 (k-Nearest Neighbors)

- Level: Intermediate
- Prerequisites: [Math/Linear-Algebra/Vectors.md](../../Math/Linear-Algebra/Vectors.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

k-NN은 새 입력과 가장 가까운 훈련 표본 $k$개를 찾아 다수결이나 평균으로 예측하는 비모수 지도학습 방법이다. 명시적인 파라미터 학습 대신 데이터 자체를 저장하는 lazy learning이다.

## 직관 (Intuition)

새 동네의 성격을 알고 싶다면 가장 가까운 이웃 몇 곳을 살펴본다. 가까움이 의미 있는 특징 공간이라면 주변 표본의 레이블이 좋은 단서가 된다.

## 이론 (Theory)

Euclidean distance는

$$d(x,z)=\sqrt{\sum_{j=1}^{d}(x_j-z_j)^2}$$

이다. 분류는 이웃의 최빈 레이블, 회귀는 평균을 사용한다. 거리의 역수로 가중할 수도 있다. 작은 $k$는 복잡한 경계를 만들어 분산이 크고, 큰 $k$는 부드럽지만 편향이 커진다.

특징 단위가 다르면 큰 스케일 특징이 거리를 지배하므로 표준화가 중요하다. 고차원에서는 거리들이 비슷해지는 차원의 저주로 성능이 악화될 수 있다.

## 구현 (Implementation)

```python
import math
from collections import Counter


def distance(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def predict_knn(train_x, train_y, query, k=3):
    neighbors = sorted(zip(train_x, train_y), key=lambda p: distance(p[0], query))[:k]
    return Counter(label for _, label in neighbors).most_common(1)[0][0]


print(predict_knn([[0], [1], [5], [6]], [0, 0, 1, 1], [4.5]))
```

## 복잡도 (Complexity)

학습은 저장만 하면 `O(nd)` 공간이다. brute-force 예측은 질의 하나에 거리 계산 `O(nd)`와 선택 비용이 든다. KD-tree·ball tree·근사 최근접 탐색은 데이터와 차원에 따라 질의를 가속한다.

## 응용 (Applications)

- 작은 데이터의 분류·회귀 기준선
- 유사 이미지·문서 검색
- 추천과 이상치 탐지
- 결측값 대치

## 흔한 오해 (Common Misunderstandings)

- 학습이 빠른 대신 예측이 비싸고 메모리를 많이 쓴다.
- $k$가 홀수면 모든 다중 클래스 tie가 사라지는 것은 아니다.
- 거리 metric과 스케일 선택은 모델의 핵심 가정이다.
- 고차원에서 더 많은 특징이 반드시 도움이 되지는 않는다.

## TMI

- $k=1$이면 훈련 오차가 거의 0이어도 일반화는 불안정할 수 있다.
- cosine distance는 텍스트·임베딩처럼 방향이 중요한 데이터에 자주 쓰인다.
- approximate nearest neighbor는 정확한 최근접을 일부 포기하고 대규모 검색 속도를 얻는다.

## 연습 / 확인 문제 (Exercises)

- $k=1,3,5$에서 같은 질의의 예측을 비교하라.
- 특징 하나의 단위를 1000배 키웠을 때 거리와 예측이 어떻게 변하는지 확인하라.
- 거리 가중 회귀 k-NN을 구현하라.

## 이어서 읽기 (Reading Path)

- 이전: [로지스틱 회귀](Logistic-Regression.md)
- 다음: [k-평균 클러스터링](K-Means.md)

## 참조 (References)

- [Math/Linear-Algebra/Vectors.md](../../Math/Linear-Algebra/Vectors.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
