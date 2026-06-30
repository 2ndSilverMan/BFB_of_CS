# 마르코프 랜덤 필드 (Markov Random Field)

- Level: Advanced
- Prerequisites: [Factorization.md](Factorization.md), [Graph-Review.md](Graph-Review.md), [Math/Probability-Statistics/Distributions.md](../../Math/Probability-Statistics/Distributions.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

마르코프 랜덤 필드(MRF)는 무방향 그래프로 확률 변수 사이의 국소 상호작용을 표현하는 모델이다. 각 노드는 변수이고, 간선은 직접적인 compatibility나 의존 관계를 나타낸다.

## 직관 (Intuition)

이미지의 한 픽셀 라벨은 주변 픽셀 라벨과 비슷할 가능성이 높다. 이 관계는 원인 방향보다는 “서로 잘 맞는가”에 가깝다. MRF는 이런 대칭적 국소 관계를 potential function의 곱으로 표현한다.

## 이론 (Theory)

양수 분포와 무방향 그래프 $G$에 대해, Hammersley-Clifford 정리는 Markov property와 clique factorization 사이의 연결을 제공한다. MRF는 보통 다음 형태다.

$$
P(X)=\frac{1}{Z}\prod_{C\in\mathcal{C}}\phi_C(X_C)
$$

여기서 $\phi_C$는 clique potential이고 $Z=\sum_X\prod_C\phi_C(X_C)$는 partition function이다. 에너지 기반 표현으로는

$$
P(X)=\frac{1}{Z}\exp(-E(X))
$$

라고 쓴다. 낮은 에너지는 더 그럴듯한 할당을 뜻한다.

```mermaid
flowchart LR
    Graph["undirected graph"] --> Potentials["clique potentials"]
    Potentials --> Energy["energy / unnormalized score"]
    Energy --> Inference["marginal or MAP inference"]
```

### Markov property

MRF의 국소 Markov property는 한 노드가 이웃 노드가 주어지면 나머지와 조건부 독립이라는 뜻이다. 이미지 grid에서는 한 픽셀 label이 주변 픽셀 label과 직접 상호작용하고, 먼 픽셀의 영향은 이웃을 통해 전달된다고 가정한다.

### MAP와 marginal의 차이

가장 가능성 높은 전체 할당을 찾는 MAP 문제와 각 변수의 주변확률을 구하는 marginal inference는 다르다. graph cut, belief propagation, MCMC, variational inference 중 어떤 방법이 맞는지는 에너지 형태와 필요한 출력에 따라 달라진다.

### Smoothness prior의 위험

pairwise smoothness는 segmentation에서 노이즈를 줄이지만, 실제 경계까지 지나치게 부드럽게 만들 수 있다. edge-aware potential이나 contrast-sensitive term을 사용해 강한 이미지 경계에서는 label 변화가 허용되도록 한다.

## 구현 (Implementation)

두 이진 변수의 pairwise potential을 곱해 비정규화 점수를 계산할 수 있다.

```python
def same_label_potential(a, b):
    return 2.0 if a == b else 0.5


def unnormalized_score(labels):
    score = 1.0
    edges = [("A", "B"), ("B", "C")]
    for u, v in edges:
        score *= same_label_potential(labels[u], labels[v])
    return score


print(unnormalized_score({"A": 1, "B": 1, "C": 0}))
```

정규화된 확률을 얻으려면 모든 할당에 대한 partition function이 필요하다.

```python
def energy_from_score(score):
    import math
    return -math.log(score)
```

## 복잡도 (Complexity)

partition function 계산과 정확 marginal 추론은 일반적으로 어렵다. 그래프 treewidth가 크면 정확 추론 비용이 지수적으로 증가하며, 큰 MRF에서는 MCMC, loopy belief propagation, variational inference 같은 근사가 필요하다.

## 응용 (Applications)

- 이미지 segmentation과 denoising
- 공간 통계와 격자 모델
- 자연어 시퀀스 labeling의 기반 개념
- 에너지 기반 모델 이해

## 흔한 오해 (Common Misunderstandings)

- potential은 확률일 필요가 없다. 양수 점수로 보면 된다.
- 무방향 간선은 인과 방향을 말하지 않는다.
- partition function이 작게 보이는 표기와 달리 계산의 핵심 병목일 수 있다.
- MRF의 국소 Markov property가 모든 복잡한 장거리 의존을 쉽게 해결한다는 뜻은 아니다.

## TMI

- Ising model은 MRF의 고전적 예다.
- CRF는 관측 변수에 조건화한 조건부 MRF로 볼 수 있다.
- 에너지 기반 모델은 deep generative modeling에서도 다시 등장한다.

## 연습 / 확인 문제 (Exercises)

- MRF와 베이지안 네트워크의 그래프 방향성 차이를 설명하라.
- partition function이 왜 필요한지 말하라.
- pairwise MRF에서 edge potential이 라벨 smoothness를 어떻게 유도하는지 예를 들어라.

## 이어서 읽기 (Reading Path)

- 이전: [HMM](HMM.md)
- 다음: [클리크와 포텐셜 함수](Cliques.md)

## 참조 (References)

- [Factorization.md](Factorization.md)
- [Graph-Review.md](Graph-Review.md)
- [Math/Probability-Statistics/Distributions.md](../../Math/Probability-Statistics/Distributions.md)
- [Reference/Books.md](../../Reference/Books.md)
