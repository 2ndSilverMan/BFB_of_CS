# 가설 검정 (Hypothesis Testing)

- Level: Intermediate
- Prerequisites: [Math/Probability-Statistics/CLT.md](CLT.md), [Math/Probability-Statistics/Expectation.md](Expectation.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

가설 검정은 데이터가 귀무가설 $H_0$과 얼마나 양립하기 어려운지 통계량으로 평가하는 절차다. 대립가설 $H_1$, 유의수준 $\alpha$, 검정통계량을 미리 정하고, 관측 결과가 $H_0$ 아래 지나치게 극단적이면 귀무가설을 기각한다.

## 직관 (Intuition)

공정한 동전이라는 가정 아래 100번 중 앞면이 90번 나오기는 매우 어렵다. 이런 결과를 보면 "공정하다"는 가정을 의심한다. 다만 드문 사건도 일어날 수 있으므로 검정은 확정 판결이 아니라 오류율을 관리하는 의사결정 규칙이다.

## 이론 (Theory)

p-value는 $H_0$이 참이라고 가정했을 때 관측 통계량 이상으로 극단적인 결과가 나올 확률이다. p-value가 $\alpha$보다 작으면 $H_0$을 기각한다.

| 실제 상태 / 결정 | 기각 | 기각하지 않음 |
|---|---|---|
| $H_0$ 참 | 제1종 오류, 확률 $\alpha$ | 올바른 결정 |
| $H_1$ 참 | 검정력 $1-\beta$ | 제2종 오류, 확률 $\beta$ |

평균 검정의 한 예로, 알려진 표준편차 $\sigma$ 아래

$$
z=\frac{\bar x-\mu_0}{\sigma/\sqrt n}
$$

를 사용한다. 실제 검정 선택은 자료형, 표본 크기, 독립성·등분산·분포 가정에 달려 있다. 신뢰 구간, 효과 크기, 검정력도 p-value와 함께 보고해야 한다.

## 구현 (Implementation)

표준정규 근사를 사용한 양측 평균 z 검정의 작은 예다.

```python
import math


def two_sided_z_test(sample_mean, null_mean, std, n):
    z = (sample_mean - null_mean) / (std / math.sqrt(n))
    p_value = math.erfc(abs(z) / math.sqrt(2))
    return z, p_value


z, p = two_sided_z_test(10.6, 10.0, 2.0, 100)
print(round(z, 3), round(p, 4))
```

실무에서는 검증된 통계 라이브러리를 사용하고 분석 전에 단측/양측, 제외 기준, 지표를 정한다.

## 복잡도 (Complexity)

표본평균과 분산 계산은 표본 수 $n$에 대해 `O(n)`이며 요약 통계가 있으면 검정통계량 계산은 `O(1)`이다. permutation test는 반복 횟수 $R$과 표본 크기에 따라 보통 `O(Rn)`이다.

## 응용 (Applications)

- A/B 테스트와 제품 실험
- 임상·과학 연구의 효과 검정
- 제조 공정과 이상 탐지
- 모델 성능 차이의 불확실성 평가

## 흔한 오해 (Common Misunderstandings)

- p-value는 귀무가설이 참일 확률이 아니다.
- 기각하지 못했다는 것이 귀무가설을 증명한 것은 아니다.
- 통계적으로 유의하다고 실무적으로 큰 효과인 것은 아니다.
- 여러 가설을 동시에 검사하면 거짓 양성이 늘어나므로 보정이 필요하다.

## TMI

- 표본 수가 매우 크면 실질적으로 사소한 차이도 매우 작은 p-value를 만들 수 있다.
- 분석을 보고 가설이나 중단 시점을 바꾸면 명목상 오류율이 유지되지 않는다.
- 사전등록과 재현 가능한 분석은 선택적 보고와 p-hacking을 줄이는 장치다.

## 연습 / 확인 문제 (Exercises)

- 제1종 오류와 제2종 오류를 스팸 필터 예로 설명하라.
- 같은 효과 크기에서 표본 수가 증가하면 검정력이 어떻게 변하는지 설명하라.
- p-value, 신뢰 구간, 효과 크기를 함께 보고하는 예시 문장을 작성하라.

## 이어서 읽기 (Reading Path)

- 이전: [중심 극한 정리](CLT.md)
- 다음: [정보 이론](Information-Theory.md)

## 참조 (References)

- [Math/Probability-Statistics/CLT.md](CLT.md)
- [Math/Probability-Statistics/Expectation.md](Expectation.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
