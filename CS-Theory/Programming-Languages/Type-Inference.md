# 타입 추론 (Type Inference)

- Level: Advanced
- Prerequisites: [Type-Systems.md](Type-Systems.md), [Lambda-Calculus.md](Lambda-Calculus.md), [CS-Theory/Compilers/Semantic-Analysis.md](../Compilers/Semantic-Analysis.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

타입 추론은 프로그래머가 타입을 명시하지 않아도 컴파일러가 표현식·변수의 타입을 **자동 계산**하는 것이다. 정적 타입의 안전성과 동적 타입의 간결성을 함께 얻는 핵심 기술로, **Hindley-Milner(HM)** 가 ML·OCaml·Haskell의 토대다.

## 직관 (Intuition)

`x = 1 + 2` 면 사람도 `x:int` 임을 안다. 타입 추론은 이런 단서를 **프로그램 전체의 제약식**으로 모아 **unification(통일)** 으로 푼다. identity 함수 `fun x -> x` 는 "입력 타입 = 출력 타입"이라는 제약만 있어 가장 일반적인 타입 `'a -> 'a` 로 추론된다.

## 이론 (Theory)

### 1. Algorithm W의 4단계

1. 각 부분식에 **새 타입 변수** 부여.
2. 연산·적용에서 **제약** 생성(예: `f a` → `f : τ_a → β`).
3. 제약을 **unification** 으로 풀어 대입(substitution) 도출.
4. let-바인딩에서 자유 타입 변수를 **일반화(generalize)** → 다형 타입.

### 2. unification과 occurs check

두 타입을 맞춘다: 변수는 타입에 바인딩, 생성자는 인자끼리 재귀 통일. **occurs check** — 변수 `α` 를 `α → β` 같이 자기를 포함한 타입에 바인딩하면 **무한 타입**이라 실패(이게 `fun x -> x x` 가 HM에서 거부되는 이유).

### 3. principal type와 let-다형성

HM은 표현식마다 **가장 일반적인 타입(principal type)** 이 유일하게 존재함을 보장한다. `let id = fun x -> x` 는 `∀a. a→a` 로 일반화되어 `id 3` 과 `id "s"` 가 모두 통과(let-polymorphism).

## 구현 (Implementation)

```python
def unify(t1, t2, subst):
    t1, t2 = resolve(t1, subst), resolve(t2, subst)
    if t1 == t2: return subst
    if is_var(t1): 
        if occurs(t1, t2, subst): raise TypeError("infinite type")  # occurs check
        subst[t1] = t2; return subst
    if is_var(t2): return unify(t2, t1, subst)
    if t1[0] == t2[0] == "->":                       # 함수: 인자·결과 재귀 통일
        unify(t1[1], t2[1], subst); return unify(t1[2], t2[2], subst)
    raise TypeError(f"cannot unify {t1} and {t2}")
```

**워크드 예제(`map`).** `map : (a→b) → [a] → [b]`. `map (fun x -> x+1) [1,2]`: `x+1` 의 `+` 가 `x:int` 강제 → `a=int`, 결과 `int` → `b=int` → 전체 `[int]`. unification이 `a,b` 를 int로 풀어낸다.

## 복잡도 (Complexity)

| 항목 | 특성 |
|---|---|
| 기본 HM | 실용적으로 거의 선형(이론상 최악 지수 — 중첩 let) |
| 서브타이핑·typeclass·higher-rank | 크게 증가 |
| dependent type | 일반적으로 결정 불가능에 근접 |

서브타이핑·조건부 타입이 들어가면 **오류 메시지가 어려워진다**(추론된 타입이 사람 직관과 멀어짐).

## 응용 (Applications)

- ML·OCaml·Haskell(전역 추론), Rust·Swift·TypeScript(지역 추론).
- IDE 타입 힌트·정적 분석, generic 함수 타입 계산.

## 흔한 오해 (Common Misunderstandings)

- **타입 추론 ≠ 동적 타입** — 타입은 컴파일 시간에 결정된다.
- **모든 타입 생략이 좋지 않다** — API 경계의 명시 타입은 문서·오류 국소화에 유리.
- **추론이 강할수록 오류 메시지가 어려워질 수 있다**(원인이 먼 곳에서 드러남).
- **타입 추론은 타입 검사의 일부**지 대체가 아니다.

## TMI

- **principal type** 정리(Hindley·Milner·Damas)는 "가장 일반적인 타입이 유일하게 존재"를 보장 — 그래서 주석 없이도 일관된 추론이 가능하다.
- occurs check가 무한 타입을 막는데, 일부 언어(OCaml `-rectypes`)는 이를 풀어 재귀 타입을 허용한다.
- TypeScript의 구조적 타입 + 조건부 타입은 실용적이지만 추론이 비결정적으로 느려질 수 있다.

## 연습 / 확인 문제 (Exercises)

- `fun x -> x` 의 타입이 왜 `'a -> 'a` 인지 제약·통일로 보여라.
- unification이 실패하는 예(`int` vs `bool`)와 occurs check 실패(`fun x -> x x`)를 각각 들어라.
- `let id = fun x -> x in (id 3, id "a")` 가 왜 통과하는지 let-다형성으로 설명하라.
- 타입 추론 vs 명시의 trade-off를 API 설계 관점에서 논하라.

## 이어서 읽기 (Reading Path)

- 이전: [타입 시스템](Type-Systems.md)
- 다음: [패러다임 비교](Paradigms.md)
- 관련: [람다 대수](Lambda-Calculus.md), [의미 분석](../Compilers/Semantic-Analysis.md)

## 참조 (References)

- [Type-Systems.md](Type-Systems.md)
- [Lambda-Calculus.md](Lambda-Calculus.md)
- [CS-Theory/Compilers/Semantic-Analysis.md](../Compilers/Semantic-Analysis.md)
- [Reference/Books.md](../../Reference/Books.md)
