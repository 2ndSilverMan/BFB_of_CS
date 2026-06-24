# 관계와 함수 (Relations and Functions)

- Level: Beginner
- Prerequisites: [Math/Discrete/Set-Theory.md](Set-Theory.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

관계는 두 집합의 원소 사이 연관을 곱집합의 부분집합으로 형식화한 것이다. 함수는 각 입력에 정확히 하나의 출력을 대응시키는 특별한 관계다. 동치 관계, 순서 관계, 단사·전사·전단사 같은 성질이 핵심이다.

## 직관 (Intuition)

"~보다 작다", "~와 친구다", "~의 부모다"처럼 세상의 많은 개념이 두 대상 사이의 관계다. 이를 순서쌍의 집합으로 보면 수학적으로 다룰 수 있다. 함수는 그중 "입력 하나에 답 하나"라는 제약을 가진 관계로, 계산·매핑·변환의 기본 모형이다.

## 이론 (Theory)

$A$ 위의 관계 $R\subseteq A\times A$의 주요 성질:

- **반사적**: 모든 $a$에 대해 $aRa$.
- **대칭적**: $aRb \Rightarrow bRa$.
- **추이적**: $aRb \wedge bRc \Rightarrow aRc$.

세 성질을 모두 가지면 **동치 관계**이며, 집합을 동치류로 분할한다. 반사·반대칭·추이적이면 **부분 순서**다.

함수 $f:A\to B$는 모든 $a\in A$에 유일한 $f(a)$를 준다.

- **단사(injective)**: $f(a)=f(a')\Rightarrow a=a'$.
- **전사(surjective)**: 모든 $b\in B$에 대해 $f(a)=b$인 $a$ 존재.
- **전단사(bijective)**: 단사이며 전사 → 역함수 존재.

합성 $g\circ f$와 역함수가 정의되며, 전단사는 두 집합의 크기가 같음을 보이는 도구다.

## 구현 (Implementation)

```python
# 관계를 순서쌍 집합으로 표현
R = {(1, 1), (2, 2), (1, 2), (2, 1)}

def is_symmetric(R):
    return all((b, a) in R for (a, b) in R)

def is_transitive(R):
    return all((a, c) in R
               for (a, b) in R for (b2, c) in R if b == b2)
```

## 복잡도 (Complexity)

$n$개 원소 위 관계는 순서쌍이 최대 $n^2$개라 성질 검사는 보통 `O(n^2)`~`O(n^3)`(추이성)이다. 동치류 분할은 union-find로 거의 선형에 처리할 수 있다. 함수의 단사/전사 검사는 정의역 크기에 선형이다.

## 응용 (Applications)

- 데이터베이스의 관계 모델과 동치/순서 질의
- 타입 변환·매핑, 해시 함수
- union-find로 연결 요소·동치류 관리
- 위상 정렬의 기반인 부분 순서

## 흔한 오해 (Common Misunderstandings)

- 모든 관계가 함수는 아니다. 한 입력에 여러 출력이면 함수가 아니다.
- 대칭과 반대칭은 반대가 아니다. 둘 다 만족하는 관계도 있다.
- 전사와 단사는 독립적 성질이다(둘 다, 하나만, 둘 다 아님 가능).
- 역함수는 전단사일 때만 (전역적으로) 존재한다.

## TMI

- 동치 관계와 분할이 일대일 대응한다는 사실은 "같다고 볼 것"을 정의하는 수학의 핵심 도구다.
- 함수의 현대적 정의(순서쌍 집합)는 19세기 이후 정착됐고, 그 전에는 "공식"으로 좁게 여겨졌다.
- 관계형 데이터베이스의 "relation"이라는 이름이 바로 이 수학적 관계에서 왔다.

## 연습 / 확인 문제 (Exercises)

- "모드 $n$ 합동" 관계가 동치 관계임을 세 성질로 보여라.
- 단사이지만 전사가 아닌 함수, 전사이지만 단사가 아닌 함수를 각각 들어라.
- 부분 순서와 전순서의 차이를 예로 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [집합론](Set-Theory.md)
- 다음: [조합론](Combinatorics.md), [그래프 이론](Graph-Theory.md)

## 참조 (References)

- [Math/Discrete/Set-Theory.md](Set-Theory.md)
- [Data-Structures/Union-Find.md](../../Data-Structures/Union-Find.md)
- [Reference/Books.md](../../Reference/Books.md)
