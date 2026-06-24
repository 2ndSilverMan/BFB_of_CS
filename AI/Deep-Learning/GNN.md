# 그래프 신경망 (Graph Neural Networks, GNN)

- Level: Advanced
- Prerequisites: [AI/Deep-Learning/MLP.md](MLP.md), [Math/Discrete/Graph-Theory.md](../../Math/Discrete/Graph-Theory.md), [Math/Linear-Algebra/Matrices.md](../../Math/Linear-Algebra/Matrices.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

그래프 신경망은 노드와 간선으로 표현되는 데이터에서 학습하는 신경망이다. 각 노드는 이웃 노드의 정보를 모아 자신의 표현을 갱신하고, 이를 여러 층 반복해 그래프 구조를 반영한 embedding을 만든다.

## 직관 (Intuition)

소셜 네트워크에서 한 사람의 성향은 그 사람의 속성뿐 아니라 주변 친구들의 속성과 관계에도 영향을 받는다. GNN은 “내 이웃들이 어떤 정보를 가지고 있는가”를 반복적으로 모아 노드, 간선, 전체 그래프를 예측한다.

## 이론 (Theory)

많은 GNN은 message passing neural network 형태로 쓸 수 있다.

$$
m_v^{(k)} = \operatorname{AGG}^{(k)}(\{h_u^{(k-1)}:u\in N(v)\})
$$

$$
h_v^{(k)} = \operatorname{UPDATE}^{(k)}(h_v^{(k-1)},m_v^{(k)})
$$

AGG는 sum, mean, max, attention 등이 될 수 있다. GCN은 정규화된 adjacency matrix로 이웃 feature를 평균화하고, GAT는 attention으로 이웃별 가중치를 학습한다.

층이 깊어질수록 더 먼 이웃 정보가 들어오지만, 너무 깊으면 노드 표현이 비슷해지는 over-smoothing 문제가 생길 수 있다. 또한 message passing GNN의 표현력은 Weisfeiler-Lehman graph isomorphism test와 관련해 분석된다.

## 구현 (Implementation)

가장 단순한 mean aggregation은 이웃 feature 평균을 구해 갱신한다.

```python
def mean_aggregate(node, neighbors, features):
    vals = [features[n] for n in neighbors[node]]
    return [sum(col) / len(vals) for col in zip(*vals)]


features = {
    "A": [1.0, 0.0],
    "B": [0.0, 1.0],
    "C": [1.0, 1.0],
}
neighbors = {"A": ["B", "C"], "B": ["A"], "C": ["A"]}

print(mean_aggregate("A", neighbors, features))
```

실제 GNN은 aggregation 결과에 선형층, 비선형성, residual connection, normalization을 결합한다.

## 복잡도 (Complexity)

한 message passing layer의 비용은 대체로 간선 수 $|E|$와 hidden dimension에 비례한다. 큰 그래프에서는 전체 이웃을 다 보지 않고 neighbor sampling, subgraph batching, graph partitioning을 사용한다.

## 응용 (Applications)

- 노드 분류와 링크 예측
- 추천 시스템과 지식 그래프
- 분자 property prediction
- 프로그램, 회로, 교통망 같은 구조 데이터 분석

## 흔한 오해 (Common Misunderstandings)

- 그래프가 있으면 항상 GNN이 최선은 아니다. feature 품질과 graph construction이 중요하다.
- 간선이 많을수록 항상 좋은 정보가 되는 것은 아니다. noisy edge는 성능을 해칠 수 있다.
- 깊은 GNN이 무조건 더 먼 정보를 잘 쓰는 것은 아니다. over-smoothing과 over-squashing이 있다.
- node order에 의존하지 않는 permutation invariance/equivariance가 중요하다.

## TMI

- graph-level prediction에서는 node embedding을 readout pooling으로 합친다.
- heterophily graph에서는 이웃이 비슷하다는 homophily 가정이 약해져 일반 GNN이 어려워질 수 있다.
- over-squashing은 먼 노드의 많은 정보가 좁은 embedding으로 압축되며 손실되는 문제다.

## 연습 / 확인 문제 (Exercises)

- GCN과 GAT의 aggregation 차이를 설명하라.
- node classification과 graph classification의 readout 차이를 말하라.
- over-smoothing이 생기는 직관을 message passing 반복 관점에서 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [Transformer](Transformer.md)
- 다음: [자기 지도 학습](Self-Supervised.md)

## 참조 (References)

- [AI/Deep-Learning/MLP.md](MLP.md)
- [Math/Discrete/Graph-Theory.md](../../Math/Discrete/Graph-Theory.md)
- [Math/Linear-Algebra/Matrices.md](../../Math/Linear-Algebra/Matrices.md)
- [Reference/Books.md](../../Reference/Books.md)
