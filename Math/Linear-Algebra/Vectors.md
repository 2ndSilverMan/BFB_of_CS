# 벡터와 벡터 공간 (Vectors and Vector Spaces)

- Level: Intermediate
- Prerequisites: 고등학교 수학
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

벡터는 수들을 순서대로 묶은 것이다. 기하적으로는 크기와 방향을 가진 화살표, 대수적으로는 $n$개 성분의 순서쌍 $\mathbf{v} = (v_1, v_2, \dots, v_n)$이다. 머신러닝에서 하나의 데이터(특징, embedding)는 보통 하나의 벡터다.

## 직관 (Intuition)

키와 몸무게로 한 사람을 $(170, 65)$처럼 나타내면, 사람은 2차원 공간의 한 점(벡터)이 된다. 특징이 많아지면 차원이 늘어날 뿐 원리는 같다. 벡터 연산은 "여러 수를 한꺼번에 다루는" 방법이다.

```mermaid
flowchart LR
    RAW["현실의 대상<br/>사람, 문서, 이미지"] --> FEAT["특징 추출<br/>수치화"]
    FEAT --> VEC["벡터 v<br/>(v1, v2, ..., vn)"]
    VEC --> OPS["내적, 거리, 투영"]
    OPS --> USE["유사도 검색<br/>분류, 회귀, 추천"]
```

## 이론 (Theory)

벡터는 덧셈과 스칼라 곱을 가진다.

$$\mathbf{a} + \mathbf{b} = (a_1+b_1, \dots, a_n+b_n), \qquad c\,\mathbf{a} = (c a_1, \dots, c a_n)$$

**내적(dot product)** 과 **노름(norm)**:

$$\mathbf{a} \cdot \mathbf{b} = \sum_{i=1}^{n} a_i b_i, \qquad \|\mathbf{a}\| = \sqrt{\mathbf{a} \cdot \mathbf{a}}$$

두 벡터의 사이각 $\theta$는 내적으로 구한다. 이를 정규화한 **코사인 유사도**는 방향이 얼마나 비슷한지를 잰다.

$$\cos\theta = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\|\,\|\mathbf{b}\|}$$

벡터 공간은 이런 덧셈·스칼라 곱에 대해 닫힌 집합이며, 공간을 생성하는 최소 벡터 집합이 기저(basis), 그 개수가 차원이다.

### 선형결합, span, 독립성

벡터 $\mathbf{v}_1,\dots,\mathbf{v}_k$와 스칼라 $c_1,\dots,c_k$가 있을 때

$$
c_1\mathbf{v}_1+\cdots+c_k\mathbf{v}_k
$$

를 선형결합이라 한다. 가능한 모든 선형결합의 집합이 이 벡터들이 생성하는 공간(span)이다. 어떤 벡터가 다른 벡터들의 선형결합으로 표현되면 정보가 중복된 것이고, 그런 중복이 없으면 선형독립이다.

예를 들어 $\mathbf{e}_1=(1,0)$, $\mathbf{e}_2=(0,1)$는 2차원 평면 전체를 생성한다. $(2,3)=2\mathbf{e}_1+3\mathbf{e}_2$처럼 모든 2차원 벡터를 만들 수 있기 때문이다. 반면 $(1,1)$과 $(2,2)$는 같은 직선만 생성하므로 2차원 전체의 기저가 될 수 없다.

### 좌표는 기저에 의존한다

벡터 자체와 그 벡터의 좌표 표현은 구분해야 한다. 표준기저에서는 $(3,4)$로 보이는 벡터가, 다른 기저에서는 전혀 다른 계수쌍으로 표현될 수 있다. 선형대수의 많은 연산은 "공간의 대상은 그대로 두고, 보기 좋은 기저로 좌표계를 바꾸는 일"로 해석할 수 있다.

### 투영과 성분 분해

단위벡터 $\mathbf{u}$ 방향으로 $\mathbf{x}$를 투영하면

$$
\operatorname{proj}_{\mathbf{u}}(\mathbf{x})=(\mathbf{x}\cdot\mathbf{u})\mathbf{u}
$$

이다. $\mathbf{u}$가 단위벡터가 아니라면 $\operatorname{proj}_{\mathbf{u}}(\mathbf{x})=\frac{\mathbf{x}\cdot\mathbf{u}}{\mathbf{u}\cdot\mathbf{u}}\mathbf{u}$를 쓴다. 투영은 뒤의 최소제곱, PCA, attention score를 이해하는 기본 조각이다.

## 구현 (Implementation)

```python
import math

def dot(a, b):
    return sum(x * y for x, y in zip(a, b))

def norm(a):
    return math.sqrt(dot(a, a))

def cosine_similarity(a, b):
    return dot(a, b) / (norm(a) * norm(b))

print(dot([1, 2, 3], [4, 5, 6]))            # 32
print(round(cosine_similarity([1, 0], [1, 1]), 3))  # 0.707
```

워크드 예제: $\mathbf{a}=(3,4)$, $\mathbf{b}=(4,3)$이면

$$
\mathbf{a}\cdot\mathbf{b}=3\cdot4+4\cdot3=24,
\quad \|\mathbf{a}\|=\|\mathbf{b}\|=5,
\quad \cos\theta=\frac{24}{25}=0.96
$$

두 벡터는 길이가 같고 방향도 매우 비슷하다. 반대로 $(1,0)$과 $(0,1)$은 내적이 0이라 직교하고 코사인 유사도도 0이다.

## 복잡도 (Complexity)

`n`은 벡터 차원이다.

| 연산 | 시간 |
|---|---|
| 덧셈, 스칼라 곱 | `O(n)` |
| 내적, 노름 | `O(n)` |

벡터 하나를 저장하는 공간은 `O(n)`이다. 대규모 임베딩 검색에서는 한 번의 내적은 단순해도 후보가 수백만 개가 되므로, 정규화·인덱싱·근사 최근접 탐색이 전체 성능을 좌우한다.

## 응용 (Applications)

- 머신러닝의 특징 벡터와 파라미터 표현
- 단어·문서·이미지 임베딩과 유사도 검색
- 그래픽스의 위치·방향·조명 계산
- 추천 시스템(사용자·아이템 벡터)

## 흔한 오해 (Common Misunderstandings)

- 벡터는 화살표"만"이 아니다. 방향·크기 해석은 기하적 관점이고, 데이터에서는 단지 수의 묶음으로 본다.
- 내적과 성분별 곱(element-wise)은 다르다. 내적은 하나의 스칼라를 낸다.
- 코사인 유사도는 크기(노름)를 무시하고 방향만 본다. 길이가 중요한 문제에는 적합하지 않을 수 있다.
- 0벡터는 방향이 없으므로 코사인 유사도를 정의할 수 없다. 구현에서는 0노름 예외 처리가 필요하다.
- 차원이 크다고 항상 정보가 많은 것은 아니다. 서로 강하게 상관된 특징은 실제 자유도를 거의 늘리지 않을 수 있다.

## TMI

- 고차원에서는 무작위로 뽑은 두 벡터가 거의 직교(내적 ≈ 0)하는 경향이 있다("차원의 저주"의 한 단면).
- 임베딩 공간에서 "왕 - 남자 + 여자 ≈ 여왕" 같은 벡터 산술이 의미를 갖는 현상은 단어 임베딩 연구에서 유명해졌다.

## 연습 / 확인 문제 (Exercises)

- 두 벡터 $(3,4)$와 $(4,3)$의 내적·노름·코사인 유사도를 구하라.
- 코사인 유사도가 1, 0, -1이 되는 두 벡터의 예를 각각 들어라.
- `n`차원 벡터의 내적이 왜 `O(n)`인지 설명하라.
- $(2,1)$을 $(1,1)$ 방향으로 투영하고, 남은 잔차가 $(1,1)$과 직교하는지 확인하라.
- $(1,1)$과 $(2,2)$가 선형독립이 아닌 이유를 span 관점에서 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: 없음
- 다음: [행렬 연산](Matrices.md)
- 관련: [큐비트와 중첩](../../CS-Theory/Quantum-Computing/Qubits.md)

## 참조 (References)

- [AI/Machine-Learning/](../../AI/Machine-Learning/)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
