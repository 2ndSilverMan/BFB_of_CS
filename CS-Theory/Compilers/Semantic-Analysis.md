# 의미 분석과 타입 검사 (Semantic Analysis and Type Checking)

- Level: Advanced
- Prerequisites: [Parser.md](Parser.md), [AST.md](AST.md), [CS-Theory/Programming-Languages/Type-Systems.md](../Programming-Languages/Type-Systems.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

의미 분석은 파싱된 [AST](AST.md)가 **언어의 의미 규칙**을 만족하는지 검사한다 — 이름 해석, 스코프, 선언 전 사용, 타입 검사, 인자 검사. 문법(파서)이 "형태"를 본다면, 의미 분석은 "**말이 되는가**"를 본다.

## 직관 (Intuition)

파서는 `사과 + 자동차` 가 *문법적으로* 맞는지만 본다. 의미 분석은 그게 *말이 되는지*(타입이 맞는지, 이름이 선언됐는지)를 본다. 핵심 자료구조는 **심볼 테이블**(스코프별 이름→정보), 핵심 절차는 **타이핑 규칙을 AST에 재귀 적용**하는 것이다.

## 이론 (Theory)

### 1. 주요 작업

- **심볼 테이블**: 변수·함수·타입을 스코프별 기록(스택).
- **이름 해석(name resolution)**: 식별자가 어느 선언을 가리키는지(shadowing 처리).
- **타입 검사**: 표현식·문장의 타입 규칙.
- **제어 흐름 검사**: return 누락, unreachable, break/continue 위치.

### 2. 타이핑 규칙(judgment)

"환경 $\Gamma$ 에서 식 $e$ 의 타입은 $\tau$" 를 $\Gamma \vdash e : \tau$ 로 쓴다. 정수 덧셈 규칙:

$$\frac{\Gamma \vdash e_1 : \text{int} \qquad \Gamma \vdash e_2 : \text{int}}{\Gamma \vdash e_1 + e_2 : \text{int}}$$

변수 규칙: $\dfrac{(x:\tau)\in\Gamma}{\Gamma\vdash x:\tau}$. 타입 검사는 이 규칙들을 AST 잎에서 위로 재귀 적용하는 것.

### 3. 전방 참조와 2-pass

함수가 *뒤에* 선언된 것을 부를 수 있으면 **2-pass**(1차: 선언 수집, 2차: 본문 검사)가 필요하다. 좋은 컴파일러는 첫 오류에서 멈추지 않고 **error recovery** 로 여러 오류를 모아 보고한다.

## 구현 (Implementation)

```python
class Scope:
    def __init__(self): self.stack = [{}]
    def enter(self): self.stack.append({})
    def exit(self):  self.stack.pop()
    def define(self, name, typ): self.stack[-1][name] = typ
    def lookup(self, name):
        for s in reversed(self.stack):           # 안쪽 스코프 우선(shadowing)
            if name in s: return s[name]
        raise NameError(name)

def type_of(node, scope):                        # 타이핑 규칙을 재귀 적용
    if node[0] == "int":  return "int"
    if node[0] == "var":  return scope.lookup(node[1])
    if node[0] == "add":
        lt, rt = type_of(node[1], scope), type_of(node[2], scope)
        if lt == rt == "int": return "int"
        raise TypeError(f"add expects int, got {lt}+{rt}")   # 타입 오류
```

**워크드 예제.** `x:int` 환경에서 `("add", ("var","x"), ("int",3))`: `var x`→int(룩업), `int 3`→int, 둘 다 int → `add`→int ✅. 만약 `x:str` 이면 `int + str` 에서 TypeError.

## 복잡도 (Complexity)

| 항목 | 특성 |
|---|---|
| 기본 의미 분석 | AST 크기에 준선형 |
| overload/trait 해소 | 후보 탐색으로 증가 |
| generic constraint·타입 추론 | 제약 풀이로 크게 복잡(최악 지수도) |

## 응용 (Applications)

- 컴파일 오류 진단, IDE 자동완성·jump-to-definition.
- 최적화 전 타입/스코프 정보 제공, 안전한 [IR](Intermediate-Representation.md) 생성.

## 흔한 오해 (Common Misunderstandings)

- **파싱 성공 ≠ 의미적으로 올바름** — `1 + "a"` 는 파싱되나 타입 오류.
- **타입 검사는 런타임 테스트를 대체하지 않는다** — 표현 가능한 성질만 보장.
- **동적 타입 언어도 이름 해석·스코프 검사는 필요**하다.
- **에러 메시지 품질은 의미 분석 설계의 일부** — source span + recovery.

## TMI

- Rust의 borrow checker는 의미 분석 + 타입 시스템이 메모리/동시성 안전을 강하게 보장하는 사례다.
- IDE의 language server(LSP)는 컴파일러 프런트엔드를 계속 돌려 실시간 진단을 준다.
- C의 "typedef 이름이 타입인지 식별자인지"는 lexer·parser·심볼 테이블이 얽히는 유명한 모호성(lexer hack)이다.

## 연습 / 확인 문제 (Exercises)

- 파싱 오류와 타입 오류의 차이를 예로 설명하라.
- 중첩 스코프의 shadowing을 심볼 테이블 룩업으로 추적하라.
- `Γ ⊢ e : τ` 규칙으로 `(x + 3) * 2`(x:int)를 타입 검사하라.
- 전방 참조(뒤에 선언된 함수 호출)에 2-pass가 왜 필요한지 보여라.

## 이어서 읽기 (Reading Path)

- 이전: [AST](AST.md)
- 다음: [중간 표현](Intermediate-Representation.md)
- 관련: [타입 시스템](../Programming-Languages/Type-Systems.md)

## 참조 (References)

- [Parser.md](Parser.md)
- [AST.md](AST.md)
- [CS-Theory/Programming-Languages/Type-Systems.md](../Programming-Languages/Type-Systems.md)
- [Reference/Books.md](../../Reference/Books.md)
