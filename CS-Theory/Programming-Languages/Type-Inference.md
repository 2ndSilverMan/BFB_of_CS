# 타입 추론 (Type Inference)

- Level: Advanced
- Prerequisites: [Type-Systems.md](Type-Systems.md), [Lambda-Calculus.md](Lambda-Calculus.md), [CS-Theory/Compilers/Semantic-Analysis.md](../Compilers/Semantic-Analysis.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

타입 추론은 프로그래머가 모든 타입을 명시하지 않아도 컴파일러가 표현식과 변수의 타입을 자동으로 계산하는 과정이다. 정적 타입의 안전성과 코드 간결성을 함께 얻기 위한 핵심 기술이다.

## 직관 (Intuition)

`x = 1 + 2`라고 쓰면 `x`가 정수라는 것은 사람이 봐도 명확하다. 타입 추론은 이런 단서를 프로그램 전체의 제약식으로 모아, 가능한 타입을 계산한다.

## 이론 (Theory)

Hindley-Milner 스타일 타입 추론은 다음 흐름으로 설명할 수 있다.

1. 표현식에서 타입 변수를 생성한다.
2. 연산과 함수 적용에서 타입 제약을 만든다.
3. 제약을 unification으로 푼다.
4. 일반화 가능한 타입 변수를 polymorphic type으로 만든다.

예를 들어 identity 함수 `fun x -> x`는 입력 타입과 출력 타입이 같다는 제약만 있으므로 `'a -> 'a`로 추론된다.

## 구현 (Implementation)

unification의 핵심은 타입 변수와 타입 구조를 일관되게 맞추는 것이다.

```python
def bind(var, typ, subst):
    if var == typ:
        return subst
    subst[var] = typ
    return subst


subst = {}
bind("T", "Int", subst)
print(subst)
```

실제 구현은 occurs check, type constructor, polymorphic generalization을 포함한다.

## 복잡도 (Complexity)

기본 Hindley-Milner 추론은 실용적으로 효율적이지만, 서브타이핑, typeclass, higher-rank polymorphism, dependent type이 들어가면 복잡도가 크게 증가한다. 오류 메시지도 어려워진다.

## 응용 (Applications)

- ML, OCaml, Haskell류 언어
- Rust, Swift, TypeScript의 지역 타입 추론
- IDE type hint와 정적 분석
- generic 함수 타입 계산

## 흔한 오해 (Common Misunderstandings)

- 타입 추론은 동적 타입과 다르다. 타입은 컴파일 시간에 결정될 수 있다.
- 모든 타입을 생략해도 항상 좋은 것은 아니다. API 경계에는 명시 타입이 문서가 된다.
- 타입 추론이 강할수록 오류 메시지가 어려워질 수 있다.
- 타입 추론은 타입 검사를 대체하는 것이 아니라 타입 검사의 일부다.

## TMI

- principal type은 표현식에 부여할 수 있는 가장 일반적인 타입이다.
- occurs check는 무한 타입을 막기 위해 필요하다.
- TypeScript는 구조적 타입과 복잡한 조건부 타입 때문에 추론이 매우 실용적이지만 복잡하다.

## 연습 / 확인 문제 (Exercises)

- identity 함수의 타입이 왜 `'a -> 'a`인지 설명하라.
- unification이 실패하는 예를 하나 들어라.
- 타입 추론과 타입 명시의 trade-off를 API 설계 관점에서 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [타입 시스템](Type-Systems.md)
- 다음: [패러다임 비교](Paradigms.md)

## 참조 (References)

- [Type-Systems.md](Type-Systems.md)
- [Lambda-Calculus.md](Lambda-Calculus.md)
- [CS-Theory/Compilers/Semantic-Analysis.md](../Compilers/Semantic-Analysis.md)
- [Reference/Books.md](../../Reference/Books.md)
