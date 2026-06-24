# 조합론 (Combinatorics)

- Level: Beginner
- Prerequisites: [Math/Discrete/Set-Theory.md](Set-Theory.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

조합론은 "몇 가지 방법이 있는가"를 세는 수학이다. 합·곱의 법칙, 순열과 조합, 이항계수, 포함-배제, 비둘기집 원리, 생성 함수 같은 도구로 경우의 수를 체계적으로 센다.

## 직관 (Intuition)

모든 경우를 일일이 나열하면 금세 폭발한다. 조합론은 "선택을 단계로 쪼개 곱한다", "겹치는 것은 빼 준다"처럼 구조를 이용해 세는 방법이다. 알고리즘의 경우의 수, 확률의 분모, 해시 충돌 분석이 모두 여기에 기댄다.

## 이론 (Theory)

기본 법칙: 독립 선택은 곱($m\cdot n$), 배타적 선택은 합($m+n$).

순열과 조합:

$$P(n,k)=\frac{n!}{(n-k)!},\qquad \binom{n}{k}=\frac{n!}{k!\,(n-k)!}$$

이항정리 $(x+y)^n=\sum_{k=0}^n \binom{n}{k}x^k y^{n-k}$, 파스칼 항등식 $\binom{n}{k}=\binom{n-1}{k-1}+\binom{n-1}{k}$.

**포함-배제**: $|A\cup B|=|A|+|B|-|A\cap B|$를 일반화. **비둘기집 원리**: $n$개 항목을 $m<n$개 상자에 넣으면 한 상자에 둘 이상이 들어간다. **생성 함수**는 수열을 멱급수의 계수로 인코딩해 점화식·합을 대수적으로 푼다.

## 구현 (Implementation)

```python
from math import comb, perm

print(perm(5, 2))     # 순열 P(5,2) = 20
print(comb(5, 2))     # 조합 C(5,2) = 10

def pascal_row(n):    # 파스칼 항등식으로 이항계수 한 행 생성
    row = [1]
    for k in range(1, n + 1):
        row.append(row[-1] * (n - k + 1) // k)
    return row
```

## 복잡도 (Complexity)

이항계수 한 줄은 `O(n)`, 표 전체(파스칼 삼각형)는 `O(n^2)`에 만든다. 팩토리얼은 매우 빠르게 커져 큰 수에서는 모듈러 산술·로그가 필요하다. 모든 경우를 실제로 생성(순열 나열)하면 `O(n!)`로 폭발하므로, 세는 것과 생성하는 것을 구분해야 한다.

## 응용 (Applications)

- 확률 계산의 경우의 수(분자/분모)
- 알고리즘 분석(상태 수, 부분집합 수)
- 해시·생일 역설, 충돌 확률
- 동적 계획법의 경우의 수 카운팅

## 흔한 오해 (Common Misunderstandings)

- 순열과 조합의 차이는 "순서를 구분하는가"다.
- 포함-배제에서 부호를 빠뜨리면 중복을 잘못 센다.
- 비둘기집 원리는 "존재"만 보장하지, 어느 상자인지는 말하지 않는다.
- "경우의 수를 센다"와 "모든 경우를 나열한다"는 비용이 전혀 다르다.

## TMI

- 생일 역설: 23명만 모여도 생일이 같은 쌍이 있을 확률이 50%를 넘는다.
- 파스칼 삼각형은 동아시아(양휘 삼각형) 등 여러 문명에서 독립적으로 발견됐다.
- 생성 함수는 "수열을 다루는 대수 기계"로, 점화식 풀이의 강력한 도구다.

## 연습 / 확인 문제 (Exercises)

- 10명 중 3명을 뽑아 일렬로 세우는 경우의 수와, 단순히 3명을 고르는 경우의 수를 비교하라.
- 1부터 100까지에서 2 또는 3의 배수의 개수를 포함-배제로 구하라.
- 비둘기집 원리로 "임의의 6명 중 서로 아는/모르는 3인조가 있다"를 직관적으로 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [관계와 함수](Relations-and-Functions.md)
- 다음: [재귀와 점화식](Recurrences.md), [Math/Probability-Statistics/Probability-Basics.md](../Probability-Statistics/Probability-Basics.md)

## 참조 (References)

- [Math/Discrete/Set-Theory.md](Set-Theory.md)
- [Math/Probability-Statistics/Probability-Basics.md](../Probability-Statistics/Probability-Basics.md)
- [Reference/Books.md](../../Reference/Books.md)
