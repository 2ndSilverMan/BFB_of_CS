# k-평균 클러스터링 (k-Means Clustering)

- Level: Intermediate
- Prerequisites: [Math/Linear-Algebra/Vectors.md](../../Math/Linear-Algebra/Vectors.md), [Math/Probability-Statistics/Expectation.md](../../Math/Probability-Statistics/Expectation.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

k-means는 레이블 없는 데이터를 $k$개 군집으로 나누고 각 군집 중심과 표본 사이 제곱거리 합을 최소화하는 비지도학습 알고리즘이다.

## 직관 (Intuition)

임시 중심을 놓고 각 점을 가장 가까운 중심에 배정한 뒤, 각 그룹의 평균으로 중심을 옮긴다. 배정과 이동을 반복하면 중심이 안정된다.

## 이론 (Theory)

군집 배정 $c_i$와 중심 $\mu_j$에 대한 목적은

$$J=\sum_{i=1}^n\|x_i-\mu_{c_i}\|_2^2$$

다. Lloyd 알고리즘은 assignment step과 update step을 번갈아 수행하며 각 단계에서 목적값을 증가시키지 않는다. 유한 단계에서 지역 최적점에 도달하지만 전역 최적은 보장하지 않는다. k-means++ 초기화와 여러 번의 restart가 나쁜 초기화를 줄인다.

## 구현 (Implementation)

```python
import random


def squared_distance(a, b):
    return sum((x - y) ** 2 for x, y in zip(a, b))


def mean(points):
    return [sum(values) / len(points) for values in zip(*points)]


def kmeans(points, k, steps=30):
    centers = random.sample(points, k)
    for _ in range(steps):
        labels = [min(range(k), key=lambda j: squared_distance(p, centers[j])) for p in points]
        centers = [mean([p for p, label in zip(points, labels) if label == j])
                   for j in range(k)]
    return labels, centers
```

빈 군집 처리는 생략했으며 실제 구현은 해당 중심을 재초기화해야 한다.

## 복잡도 (Complexity)

표본 $n$, 차원 $d$, 군집 $k$, 반복 $T$에 대해 시간 `O(Tnkd)`, 중심과 배정 외 데이터 공간 `O(kd+n)`이다.

## 응용 (Applications)

- 고객·문서·이미지 임베딩 군집화
- 색상 양자화와 압축
- prototype 생성과 데이터 요약
- 이상치 탐색의 전처리

## 흔한 오해 (Common Misunderstandings)

- $k$는 알고리즘이 자동으로 정해 주지 않는다.
- 구형이고 비슷한 크기의 군집 가정이 강하다.
- 범주형 특징에 Euclidean mean을 그대로 적용할 수 없다.
- cluster 번호 0과 1에는 순서 의미가 없다.

## TMI

- 중심 업데이트가 평균인 이유는 제곱거리 합을 최소화하는 점이 평균이기 때문이다.
- scale이 큰 특징이 거리를 지배하므로 표준화가 중요하다.
- elbow와 silhouette는 $k$ 선택의 보조 지표이지 정답 생성기는 아니다.

## 연습 / 확인 문제 (Exercises)

- 서로 다른 초기화로 목적값이 달라지는 예를 찾아라.
- 표준화 전후 군집 결과를 비교하라.
- 빈 군집 재초기화 정책을 구현하라.

## 이어서 읽기 (Reading Path)

- 이전: [k-최근접 이웃](KNN.md)
- 다음: [차원 축소](Dimensionality-Reduction.md)
- 관련: [계층적 클러스터링](Hierarchical-Clustering.md)

## 참조 (References)

- [Math/Linear-Algebra/Vectors.md](../../Math/Linear-Algebra/Vectors.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
