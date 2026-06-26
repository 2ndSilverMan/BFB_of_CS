# 벡터와 벡터 공간 (Vectors and Vector Spaces)

- Level: Intermediate
- Prerequisites: 고등학교 수학
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

벡터는 수들을 순서대로 묶은 것이다. 기하적으로는 크기와 방향을 가진 화살표, 대수적으로는 $n$개 성분의 순서쌍 $\mathbf{v} = (v_1, v_2, \dots, v_n)$이다. 머신러닝에서 하나의 데이터(특징, embedding)는 보통 하나의 벡터다.

## 직관 (Intuition)

키와 몸무게로 한 사람을 $(170, 65)$처럼 나타내면, 사람은 2차원 공간의 한 점(벡터)이 된다. 특징이 많아지면 차원이 늘어날 뿐 원리는 같다. 벡터 연산은 "여러 수를 한꺼번에 다루는" 방법이다.

## 이론 (Theory)

벡터는 덧셈과 스칼라 곱을 가진다.

$$\mathbf{a} + \mathbf{b} = (a_1+b_1, \dots, a_n+b_n), \qquad c\,\mathbf{a} = (c a_1, \dots, c a_n)$$

**내적(dot product)** 과 **노름(norm)**:

$$\mathbf{a} \cdot \mathbf{b} = \sum_{i=1}^{n} a_i b_i, \qquad \|\mathbf{a}\| = \sqrt{\mathbf{a} \cdot \mathbf{a}}$$

두 벡터의 사이각 $\theta$는 내적으로 구한다. 이를 정규화한 **코사인 유사도**는 방향이 얼마나 비슷한지를 잰다.

$$\cos\theta = \frac{\mathbf{a} \cdot \mathbf{b}}{\|\mathbf{a}\|\,\|\mathbf{b}\|}$$

벡터 공간은 이런 덧셈·스칼라 곱에 대해 닫힌 집합이며, 공간을 생성하는 최소 벡터 집합이 기저(basis), 그 개수가 차원이다.

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

## 복잡도 (Complexity)

`n`은 벡터 차원이다.

| 연산 | 시간 |
|---|---|
| 덧셈, 스칼라 곱 | `O(n)` |
| 내적, 노름 | `O(n)` |

## 응용 (Applications)

- 머신러닝의 특징 벡터와 파라미터 표현
- 단어·문서·이미지 임베딩과 유사도 검색
- 그래픽스의 위치·방향·조명 계산
- 추천 시스템(사용자·아이템 벡터)

## 흔한 오해 (Common Misunderstandings)

- 벡터는 화살표"만"이 아니다. 방향·크기 해석은 기하적 관점이고, 데이터에서는 단지 수의 묶음으로 본다.
- 내적과 성분별 곱(element-wise)은 다르다. 내적은 하나의 스칼라를 낸다.
- 코사인 유사도는 크기(노름)를 무시하고 방향만 본다. 길이가 중요한 문제에는 적합하지 않을 수 있다.

## TMI

- 고차원에서는 무작위로 뽑은 두 벡터가 거의 직교(내적 ≈ 0)하는 경향이 있다("차원의 저주"의 한 단면).
- 임베딩 공간에서 "왕 - 남자 + 여자 ≈ 여왕" 같은 벡터 산술이 의미를 갖는 현상은 단어 임베딩 연구에서 유명해졌다.

## 연습 / 확인 문제 (Exercises)

- 두 벡터 $(3,4)$와 $(4,3)$의 내적·노름·코사인 유사도를 구하라.
- 코사인 유사도가 1, 0, -1이 되는 두 벡터의 예를 각각 들어라.
- `n`차원 벡터의 내적이 왜 `O(n)`인지 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: 없음
- 다음: [행렬 연산](Matrices.md)
- 관련: [큐비트와 중첩](../../CS-Theory/Quantum-Computing/Qubits.md)

## 참조 (References)

- [AI/Machine-Learning/](../../AI/Machine-Learning/)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
