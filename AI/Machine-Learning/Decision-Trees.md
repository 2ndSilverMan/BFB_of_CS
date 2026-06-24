# 결정 트리 (Decision Trees)

- Level: Intermediate
- Prerequisites: [Math/Probability-Statistics/Information-Theory.md](../../Math/Probability-Statistics/Information-Theory.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

결정 트리는 특징에 대한 질문을 순서대로 나눠 예측하는 지도학습 모델이다. 내부 노드는 분할 조건, 가지는 결과, 잎은 클래스 확률이나 회귀값을 담는다.

## 직관 (Intuition)

스무고개처럼 가장 잘 구분되는 질문부터 던져 데이터를 작은 그룹으로 나눈다. "나이 < 30?", "방문 횟수 < 3?" 같은 규칙이 이어지므로 예측 경로를 사람이 읽기 쉽다.

## 이론 (Theory)

분류에서는 불순도 감소가 큰 분할을 고른다. Gini impurity와 entropy는

$$G=1-\sum_k p_k^2,\qquad H=-\sum_k p_k\log_2p_k$$

이고, 부모 불순도에서 자식 불순도의 가중평균을 뺀 값이 gain이다. 회귀 트리는 보통 평균제곱오차 감소를 사용한다. 모든 후보 분할에서 현재 가장 좋은 greedy 선택을 하므로 전역 최적 트리를 보장하지 않는다.

깊이, 잎의 최소 표본 수, 가지치기는 과적합을 제어한다. 연속 특징은 임계값, 범주 특징은 집합 분할로 처리한다.

## 구현 (Implementation)

```python
def predict_tree(row, node):
    if "value" in node:
        return node["value"]
    branch = "left" if row[node["feature"]] < node["threshold"] else "right"
    return predict_tree(row, node[branch])


tree = {"feature": "age", "threshold": 30,
        "left": {"value": "low-risk"}, "right": {"value": "high-risk"}}
print(predict_tree({"age": 25}, tree))
```

실제 학습은 검증된 라이브러리로 수행하고 결측값·범주형 처리 정책을 확인한다.

## 복잡도 (Complexity)

균형 트리의 예측은 깊이 $h$에 대해 `O(h)`, 최악 `O(n)`이다. 정렬을 재사용하는 전형적 학습은 표본 $n$, 특징 $d$에 대해 대략 `O(dn log n)`이나 구현과 트리 깊이에 따라 달라진다.

## 응용 (Applications)

- 해석 가능한 분류·회귀 기준선
- 신용, 이탈, 진단 규칙
- 랜덤 포레스트와 boosting의 기본 학습기
- 비선형 특징 상호작용 탐색

## 흔한 오해 (Common Misunderstandings)

- 트리가 해석 가능해도 깊은 트리 전체가 쉽게 이해되는 것은 아니다.
- feature importance가 인과 효과를 뜻하지 않는다.
- 정규화가 거의 필요 없지만 과적합 제어는 필요하다.
- 작은 데이터 변화로 트리 구조가 크게 바뀔 수 있다.

## TMI

- CART는 이진 분할로 분류와 회귀를 모두 다룬다.
- 축에 평행한 분할을 조합하므로 대각선 경계는 계단 모양이 된다.
- 잎의 클래스 비율은 확률처럼 보이지만 별도 calibration이 필요할 수 있다.

## 연습 / 확인 문제 (Exercises)

- 세 클래스 분포의 Gini impurity를 계산하라.
- 깊이 제한을 바꾸며 훈련·검증 성능을 비교하라.
- 한 예측이 루트에서 잎까지 거치는 규칙을 문장으로 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [로지스틱 회귀](Logistic-Regression.md)
- 다음: [앙상블](Ensemble.md)

## 참조 (References)

- [Math/Probability-Statistics/Information-Theory.md](../../Math/Probability-Statistics/Information-Theory.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
