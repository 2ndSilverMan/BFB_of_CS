# 신뢰 전파 (Belief Propagation)

- Level: Advanced
- Prerequisites: [Variable-Elimination.md](Variable-Elimination.md), [Bayesian-Networks.md](Bayesian-Networks.md), [Math/Probability-Statistics/Probability-Basics.md](../../Math/Probability-Statistics/Probability-Basics.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

신뢰 전파는 그래프의 노드들이 메시지를 주고받아 주변확률이나 최빈 상태를 계산하는 추론 알고리즘이다. 트리 구조에서는 sum-product belief propagation이 정확한 marginal을 계산하고, max-product는 가장 가능성 높은 할당을 찾는 데 쓰인다.

## 직관 (Intuition)

큰 조직에서 전체 정보를 한 사람이 다 모으지 않고, 각 부서가 자기 하위 부서의 요약만 전달한다고 하자. 트리라면 중복 없이 모든 정보가 한 번씩 모인다. belief propagation은 factor들이 지역 정보를 메시지로 압축해 이웃에게 보내는 방식이다.

## 이론 (Theory)

factor graph에서 변수 노드 $x$와 factor 노드 $f$가 번갈아 연결되어 있다고 하자. sum-product 메시지는 대략 다음 구조를 가진다.

$$
m_{x\to f}(x)=\prod_{g\in N(x)\setminus f}m_{g\to x}(x)
$$

$$
m_{f\to x}(x)=
\sum_{\mathbf{x}_{N(f)\setminus x}}
f(\mathbf{x}_{N(f)})
\prod_{y\in N(f)\setminus x}m_{y\to f}(y)
$$

트리에서는 잎에서 루트로, 다시 루트에서 잎으로 메시지를 보내면 정확한 belief를 얻는다. 그래프에 cycle이 있으면 loopy belief propagation으로 반복 적용할 수 있지만, 수렴과 정확성은 보장되지 않을 수 있다.

```mermaid
flowchart LR
    Leaf["leaf messages"] --> Root["collect to root"]
    Root --> Down["distribute back"]
    Down --> Belief["node beliefs"]
```

### 변수 소거와의 관계

트리에서 BP는 여러 질의를 효율적으로 재사용하는 변수 소거로 볼 수 있다. 한 노드의 marginal을 구할 때 필요한 하위 factor 계산을 메시지로 저장하고, 모든 노드에 대해 같은 계산을 반복하지 않는다.

### 메시지 정규화

메시지는 scale이 계속 커지거나 작아질 수 있어 보통 정규화한다. 정규화는 belief를 안정적으로 계산하기 위한 수치적 장치이며, 최종 marginal은 다시 normalize한다.

### Loopy BP 사용 시 점검

cycle이 있는 그래프에서는 damping, update schedule, convergence criterion이 중요하다. 수렴해도 정확 marginal이 아닐 수 있으므로 작은 문제의 exact inference나 샘플링 결과와 비교해 sanity check를 한다.

## 구현 (Implementation)

두 이진 변수 $A,B$와 factor $\phi(A,B)$가 있을 때 $B$에서 $A$로 보내는 메시지는 $B$를 합산한 값이다.

```python
phi = {
    (0, 0): 0.9,
    (0, 1): 0.1,
    (1, 0): 0.2,
    (1, 1): 0.8,
}
msg_b_to_phi = {0: 0.6, 1: 0.4}


def factor_to_a(a):
    return sum(phi[(a, b)] * msg_b_to_phi[b] for b in [0, 1])


raw = {a: factor_to_a(a) for a in [0, 1]}
z = sum(raw.values())
belief_a = {a: v / z for a, v in raw.items()}
print(belief_a)
```

큰 factor graph에서는 모든 간선 방향 메시지를 저장하고 수렴할 때까지 반복한다.

## 복잡도 (Complexity)

트리에서 메시지 수는 간선 수에 선형이지만, 각 factor 메시지 계산은 factor scope의 도메인 크기에 지수적으로 의존할 수 있다. loopy belief propagation은 반복 횟수까지 곱해지며, 수렴하지 않을 가능성도 있다.

## 응용 (Applications)

- HMM, Kalman filter, LDPC code decoding
- 이미지/그래프 labeling 문제
- factor graph 기반 확률 추론
- approximate inference와 variational method의 연결점

## 흔한 오해 (Common Misunderstandings)

- belief propagation이 모든 그래프에서 정확한 것은 아니다.
- loopy BP가 수렴했다고 해서 참 marginal이라는 보장은 없다.
- 메시지는 확률분포처럼 정규화할 수 있지만, 중간 메시지 자체가 항상 독립적인 확률 모델은 아니다.
- max-product와 sum-product는 목적이 다르다.

## TMI

- HMM의 forward-backward 알고리즘은 chain factor graph에서의 belief propagation으로 볼 수 있다.
- loopy BP는 이론적으로는 불완전하지만 coding theory와 computer vision에서 강력하게 작동한 사례가 많다.
- Bethe free energy의 stationary point와 loopy BP fixed point는 연결된다.

## 연습 / 확인 문제 (Exercises)

- chain graph에서 한 노드의 marginal을 메시지 두 방향의 곱으로 표현하라.
- sum-product와 max-product의 메시지 식 차이를 써라.
- cycle이 있는 그래프에서 BP가 왜 중복 정보를 셀 수 있는지 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [변수 소거](Variable-Elimination.md)
- 다음: [MCMC](MCMC.md)
- 관련: [변분 추론](Variational-Inference.md)

## 참조 (References)

- [Variable-Elimination.md](Variable-Elimination.md)
- [Bayesian-Networks.md](Bayesian-Networks.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
