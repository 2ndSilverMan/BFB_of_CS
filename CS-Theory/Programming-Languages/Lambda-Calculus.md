# 람다 대수 (Lambda Calculus)

- Level: Intermediate
- Prerequisites: [CS-Theory/Programming-Languages/Syntax-and-Semantics.md](Syntax-and-Semantics.md), [Programming/Functions-and-Recursion.md](../../Programming/Functions-and-Recursion.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

람다 대수는 **함수 정의와 함수 적용만으로 계산을 표현하는 최소 형식 체계**다. 변수 $x$, 함수 $\lambda x.e$, 적용 $e_1\ e_2$ 세 구문만으로 이뤄지며 함수형 프로그래밍, 타입 이론, 언어 의미론의 공통 토대가 된다.

## 직관 (Intuition)

람다 대수에서는 이름 붙은 함수, 반복문, 숫자조차 필수 기능이 아니다. 값을 받는 익명 함수와 그 함수를 적용하는 규칙만 있으면 다른 계산을 인코딩할 수 있다. 핵심 계산은 함수 호출 시 매개변수를 인자로 **치환**하는 것이다.

예를 들어 항등 함수 $(\lambda x.x)$에 $y$를 적용하면 한 단계 뒤에 $y$가 된다.

$$
(\lambda x.x)\ y \rightarrow_\beta y
$$

## 이론 (Theory)

람다 항의 문법은 다음과 같다.

$$
e ::= x \mid \lambda x.e \mid e\ e
$$

세 가지 변환이 중심이다.

| 변환 | 예 | 의미 |
|---|---|---|
| $\alpha$ 변환 | $\lambda x.x \equiv_\alpha \lambda z.z$ | 묶인 변수 이름 변경 |
| $\beta$ 축약 | $(\lambda x.e)\ v \rightarrow e[x := v]$ | 함수 적용과 치환 |
| $\eta$ 변환 | $\lambda x.f\ x \equiv_\eta f$ | 같은 외연을 가진 함수 단순화 |

치환은 **변수 포획(variable capture)** 을 피해야 한다. 예를 들어 $(\lambda x.\lambda y.x)\ y$에서 안쪽 $y$의 이름을 먼저 바꾸지 않고 치환하면 자유 변수였던 $y$가 잘못 묶인다.

평가 전략도 결과와 종료 여부에 영향을 준다.

- 호출값(call by value): 인자를 먼저 값으로 평가한 뒤 함수 본문에 넣는다.
- 호출이름(call by name): 필요할 때까지 인자를 평가하지 않는다.
- 호출필요(call by need): 지연 평가 결과를 저장해 다시 계산하지 않는다.

타입 없는 람다 대수는 튜링 완전하다. 반면 단순 타입 람다 대수는 모든 잘 형성된 항의 평가가 종료하지만, 그만큼 표현 가능한 계산이 제한된다.

## 구현 (Implementation)

다음은 이름 충돌이 없는 입력만 가정한 작은 람다 항 평가 예시다. 실제 구현은 자유 변수 집합과 알파 변환을 함께 처리해야 한다.

```python
def substitute(expr, name, value):
    tag = expr[0]
    if tag == "var":
        return value if expr[1] == name else expr
    if tag == "lambda":
        param, body = expr[1], expr[2]
        return expr if param == name else ("lambda", param, substitute(body, name, value))
    if tag == "apply":
        return ("apply", substitute(expr[1], name, value),
                substitute(expr[2], name, value))
    raise ValueError(tag)


identity = ("lambda", "x", ("var", "x"))
argument = ("var", "answer")
print(substitute(identity[2], identity[1], argument))  # ('var', 'answer')
```

실제 인터프리터는 이름 대신 De Bruijn index를 사용하거나, 환경(environment)에 변수와 값을 저장해 안전한 치환을 구현하기도 한다.

## 복잡도 (Complexity)

한 번의 단순 치환은 항 크기를 $n$이라 할 때 `O(n)`이지만, 인자를 여러 위치에 복제하면 항의 크기가 급격히 늘 수 있다. 전체 정규화 시간에는 일반적인 상한이 없다. 타입 없는 람다 대수에는 끝나지 않는 항 $(\lambda x.x\ x)(\lambda x.x\ x)$가 존재하기 때문이다.

## 응용 (Applications)

- 함수형 언어의 일급 함수, 클로저, 고차 함수의 이론적 모델
- 컴파일러의 중간 언어와 함수 인라이닝·베타 축약
- 타입 시스템과 Curry–Howard 대응의 기반
- Church encoding을 통한 불리언, 자연수, 자료구조 표현

## 흔한 오해 (Common Misunderstandings)

- 람다 대수의 `lambda`는 파이썬의 익명 함수 문법 하나만을 뜻하지 않는다.
- 변수 이름은 본질이 아니다. 묶인 변수만 일관되게 바꾼 알파 동치 항은 같은 구조다.
- 모든 람다 항이 종료하는 것은 아니다. 재귀 이름이 없어도 자기 적용으로 무한 계산을 만들 수 있다.
- 호출값과 지연 평가는 단순 성능 옵션이 아니다. 어떤 프로그램이 종료하고 언제 부수 효과가 일어나는지 바꿀 수 있다.

## TMI

- 람다 대수의 $\lambda$ 표기는 오늘날 Python, Java, C#, Kotlin 등 여러 언어에서 익명 함수를 나타내는 이름과 문법으로 이어졌다.
- Church numeral에서 자연수 $n$은 함수를 $n$번 적용하는 고차 함수다. 예를 들어 2는 $\lambda f.\lambda x.f(f(x))$다.
- De Bruijn index는 변수 이름 대신 자신을 묶는 람다까지의 거리를 써 알파 동치 처리를 기계적으로 단순화한다.

## 연습 / 확인 문제 (Exercises)

- $(\lambda x.\lambda y.x)\ a\ b$를 베타 축약해 결과를 구하라.
- 변수 포획이 일어나는 치환 예를 만들고 알파 변환으로 고쳐라.
- Church boolean `true`, `false`와 조건 선택 함수를 람다 항으로 표현하라.

## 이어서 읽기 (Reading Path)

- 이전: [구문과 의미론](Syntax-and-Semantics.md)
- 다음: [타입 시스템](Type-Systems.md)
- 관련: [함수와 재귀](../../Programming/Functions-and-Recursion.md)

## 참조 (References)

- [CS-Theory/Programming-Languages/Syntax-and-Semantics.md](Syntax-and-Semantics.md)
- [Programming/Functions-and-Recursion.md](../../Programming/Functions-and-Recursion.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
