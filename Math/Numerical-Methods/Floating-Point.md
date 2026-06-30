# 부동소수점 표현과 오차 (Floating-Point and Error)

- Level: Intermediate
- Prerequisites: [Systems/Computer-Architecture/Data-Representation.md](../../Systems/Computer-Architecture/Data-Representation.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

부동소수점은 실수를 유한한 비트로 근사하는 표준 표현이다. IEEE 754는 부호·지수·가수로 수를 나타내며, 유한 정밀도에서 비롯되는 반올림 오차와 그 누적이 수치 계산의 핵심 주제다.

## 직관 (Intuition)

실수는 무한히 많지만 비트는 유한하다. 그래서 컴퓨터는 대부분의 실수를 "가장 가까운 표현 가능한 값"으로 반올림한다. 0.1조차 이진으로는 무한소수라 정확히 담기지 않는다. 이 작은 오차들이 반복 계산에서 쌓이면 결과를 크게 망칠 수 있어, 수치 알고리즘은 이를 의식해 설계한다.

```mermaid
flowchart LR
    REAL["실수 값"] --> ROUND["표현 가능한 값으로 반올림"]
    ROUND --> OP["연산 수행"]
    OP --> ERR["반올림 오차 누적"]
    ERR --> STABLE["안정적 알고리즘 필요"]
```

## 이론 (Theory)

IEEE 754 배정밀도(double)는 64비트 = 부호 1 + 지수 11 + 가수 52로

$$x=(-1)^s\times 1.m \times 2^{e-1023}$$

표현한다. 표현 가능한 수 간 간격은 기계 엡실론 $\varepsilon\approx 2.22\times10^{-16}$(double)로 측정된다. 핵심 오차 현상:

- **반올림 오차**: 한 연산당 상대 오차 $\le \varepsilon$.
- **상쇄(catastrophic cancellation)**: 비슷한 두 수의 뺄셈에서 유효숫자가 소실.
- **흡수(absorption)**: 큰 수에 아주 작은 수를 더하면 작은 수가 사라짐.

특수값으로 $\pm\infty$, `NaN`, 비정규수(subnormal)가 있다. 안정적 알고리즘은 조건수(condition number)가 큰 연산을 피하도록 식을 재배열한다.

### 절대 오차와 상대 오차

근사값 $\hat{x}$에 대해

$$
\text{절대 오차}=|\hat{x}-x|,\qquad
\text{상대 오차}=\frac{|\hat{x}-x|}{|x|}
$$

다. 큰 값에서는 절대 오차가 커도 상대 오차가 작을 수 있고, 0 근처에서는 상대 오차가 폭발할 수 있다. 수치 계산 보고서에서는 어떤 오차 기준을 쓰는지 명확히 해야 한다.

### 안정성, 조건수, 알고리즘 오차

조건수는 문제 자체가 입력 오차에 얼마나 민감한지 나타내고, 안정성은 알고리즘이 추가 오차를 얼마나 키우는지 나타낸다.

| 개념 | 질문 |
|---|---|
| conditioning | 입력을 조금 바꾸면 정답이 얼마나 바뀌나? |
| stability | 알고리즘이 반올림 오차를 얼마나 증폭하나? |
| backward stability | 계산 결과가 약간 변형된 입력의 정확한 해로 볼 수 있나? |

좋은 수치 알고리즘은 보통 backward stable한 알고리즘이다. 다만 문제 자체가 ill-conditioned이면 안정적 알고리즘도 정확한 해를 보장하기 어렵다.

### 안전한 비교와 합산

부동소수점 비교는 절대/상대 허용오차를 함께 쓰는 편이 안전하다.

$$
|a-b|\le \text{atol}+\text{rtol}\cdot\max(|a|,|b|)
$$

많은 작은 수를 더할 때는 순서가 결과에 영향을 준다. 큰 수부터 더하면 작은 항이 흡수될 수 있으므로, pairwise sum이나 Kahan summation으로 오차를 줄인다.

## 구현 (Implementation)

```python
print(0.1 + 0.2 == 0.3)        # False — 반올림 오차
print(0.1 + 0.2)               # 0.30000000000000004

# 상쇄를 피한 안정적 이차방정식 근 (b>0일 때)
import math
def stable_root(a, b, c):
    q = -(b + math.copysign(math.sqrt(b*b - 4*a*c), b)) / 2
    return q / a, c / q          # 두 근을 상쇄 없이
```

허용오차 비교와 Kahan summation 예:

```python
import math

print(math.isclose(0.1 + 0.2, 0.3, rel_tol=1e-12, abs_tol=1e-12))

def kahan_sum(values):
    total = 0.0
    c = 0.0
    for x in values:
        y = x - c
        t = total + y
        c = (t - total) - y
        total = t
    return total
```

## 복잡도 (Complexity)

부동소수점 연산 자체는 상수 시간이지만, 정확도는 알고리즘 구조에 달렸다. 오차는 보통 연산 수에 따라 누적되며, 조건수가 큰 문제는 입력의 작은 오차가 출력에서 크게 증폭된다. 그래서 "빠른" 알고리즘이 "정확한" 알고리즘과 다를 수 있다.

보상 합산은 단순 합보다 상수 비용이 조금 더 들지만 여전히 `O(n)`이다. 큰 배열에서는 pairwise sum이 병렬화와 정확도 사이의 좋은 균형을 제공한다.

## 응용 (Applications)

- 과학 계산·시뮬레이션의 정확도 관리
- 머신러닝의 수치 안정성(로그-합-지수, 정규화)
- 금융 계산(정확성이 필요하면 십진/정수 사용)
- 그래픽스·물리 엔진의 누적 오차 제어

## 흔한 오해 (Common Misunderstandings)

- 부동소수점 동치 비교(`==`)는 위험하다. 허용 오차(epsilon) 비교를 쓴다.
- 결합법칙이 성립하지 않는다: `(a+b)+c ≠ a+(b+c)`일 수 있다.
- 정밀도를 늘려도(오차를 줄일 뿐) 근본적으로 없애지는 못한다.
- `NaN`은 자기 자신과도 같지 않다(`NaN != NaN`).
- `float`가 "대략 실수"라는 말은 모든 계산이 임의로 부정확하다는 뜻이 아니다. IEEE 754는 엄격한 반올림 규칙을 제공한다.
- decimal이 항상 더 좋은 선택은 아니다. 금융처럼 십진 정확도가 필요한 경우에는 좋지만, 과학 계산 성능은 보통 binary float가 낫다.

## TMI

- 1996년 아리안 5 로켓 폭발은 부동소수점→정수 변환 오버플로가 원인이었다.
- `0.1 + 0.2 != 0.3`은 거의 모든 언어에서 재현되는 부동소수점 입문의 상징적 예다.
- log-sum-exp 트릭은 소프트맥스의 오버플로/언더플로를 막는 표준 수치 안정화 기법이다.

## 연습 / 확인 문제 (Exercises)

- `0.1`을 이진 부동소수점으로 정확히 표현할 수 없는 이유를 설명하라.
- 상쇄가 발생하는 식을 만들고 재배열로 개선하라.
- 기계 엡실론을 코드로 추정하라(1에 더해도 변하지 않는 가장 작은 수).
- 큰 수 하나와 작은 수 여러 개를 더하는 예제를 만들고, 합산 순서에 따라 결과가 달라지는지 관찰하라.
- `math.isclose`의 `rel_tol`과 `abs_tol`이 각각 필요한 상황을 예로 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [Systems/Computer-Architecture/Data-Representation.md](../../Systems/Computer-Architecture/Data-Representation.md)
- 다음: [방정식의 수치 해법](Root-Finding.md), [선형 방정식 수치 풀이](Numerical-Linear-Systems.md)

## 참조 (References)

- [Systems/Computer-Architecture/Data-Representation.md](../../Systems/Computer-Architecture/Data-Representation.md)
- [Reference/Books.md](../../Reference/Books.md)
