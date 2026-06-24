# 극한과 연속 (Limits and Continuity)

- Level: Beginner
- Prerequisites: 없음
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

극한은 입력이 어떤 값에 한없이 가까워질 때 함수값이 다가가는 값이다. 연속은 함수가 그 점에서 "끊김 없이" 이어지는 성질로, 극한값과 함수값이 일치함을 뜻한다. 미적분 전체의 출발점이다.

## 직관 (Intuition)

"$x$가 2에 가까워지면 $f(x)$는 무엇에 가까워지는가?"라는 질문이 극한이다. 실제로 2를 대입할 수 없거나(0/0 꼴) 정의되지 않아도, 주변의 거동으로 값을 추론한다. 미분(순간 변화율)과 적분(넓이의 극한)은 모두 이 "한없이 가까이"라는 아이디어 위에 세워진다.

## 이론 (Theory)

$\varepsilon$-$\delta$ 정의: $\lim_{x\to a}f(x)=L$이란, 모든 $\varepsilon>0$에 대해 어떤 $\delta>0$가 존재해

$$0<|x-a|<\delta \implies |f(x)-L|<\varepsilon$$

좌극한·우극한이 같아야 극한이 존재한다. 연속은 $\lim_{x\to a}f(x)=f(a)$. 연속 함수는 합·곱·합성에 닫혀 있다.

핵심 정리:
- **중간값 정리**: $[a,b]$에서 연속이고 $f(a)<y<f(b)$이면 $f(c)=y$인 $c$가 존재.
- **최대·최소 정리**: 닫힌 구간의 연속 함수는 최댓값·최솟값을 가진다.

부정형 $0/0,\ \infty/\infty$는 인수분해, 유리화, 또는 로피탈 정리로 푼다.

## 구현 (Implementation)

```python
def limit_estimate(f, a, side="both", h=1e-6):
    if side == "right":
        return f(a + h)
    if side == "left":
        return f(a - h)
    left, right = f(a - h), f(a + h)   # 좌/우 극한 비교
    return (left + right) / 2 if abs(left - right) < 1e-4 else None
```

수치적 추정은 직관용이며, 엄밀한 극한은 대수적/해석적으로 구한다.

## 복잡도 (Complexity)

극한·연속은 해석적 성질이라 알고리즘 복잡도와 직접 관계는 없다. 다만 수치적 추정은 작은 $h$에서 부동소수점 반올림 오차에 민감해, 너무 작은 $h$는 오히려 정확도를 해친다(상쇄 오차).

## 응용 (Applications)

- 미분·적분의 정의 기반
- 알고리즘의 점근 분석(연속적 근사)
- 수치해석의 수렴 판정
- 최적화에서 함수의 거동 분석

## 흔한 오해 (Common Misunderstandings)

- 극한이 존재해도 그 점에서 함수가 정의되거나 연속일 필요는 없다.
- $0/0$은 "값이 없다"가 아니라 "더 따져 봐야 한다"는 부정형이다.
- 연속이라고 미분 가능한 것은 아니다(예: $|x|$는 0에서 연속이나 미분 불가).
- 수치적으로 $h$를 0에 가깝게 둘수록 항상 정확해지지는 않는다.

## TMI

- $\varepsilon$-$\delta$ 정의는 19세기 코시·바이어슈트라스가 미적분을 엄밀화하며 정립했다.
- 바이어슈트라스 함수는 "모든 점에서 연속이지만 어디서도 미분 불가능"한 충격적 예다.
- 로피탈 정리는 실은 그의 스승 베르누이의 결과로 알려져 있다.

## 연습 / 확인 문제 (Exercises)

- $\lim_{x\to 2}\frac{x^2-4}{x-2}$를 인수분해로 구하라.
- 좌극한과 우극한이 다른 함수의 예를 들고 극한이 없는 이유를 설명하라.
- 중간값 정리로 $x^3-x-1=0$이 $[1,2]$에 근을 가짐을 보여라.

## 이어서 읽기 (Reading Path)

- 이전: [Math/Calculus/](README.md)
- 다음: [미분](Differentiation.md), [편미분과 그래디언트](Partial-Derivatives.md)

## 참조 (References)

- [Math/Calculus/Differentiation.md](Differentiation.md)
- [Math/Real-Analysis/Continuity.md](../Real-Analysis/Continuity.md)
- [Reference/Books.md](../../Reference/Books.md)
