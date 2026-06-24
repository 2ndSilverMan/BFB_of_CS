# 문맥 자유 문법과 푸시다운 오토마타 (Context-Free Grammars & PDA)

- Level: Intermediate
- Prerequisites: [CS-Theory/Computation-Theory/Regular-Languages.md](Regular-Languages.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

문맥 자유 문법(CFG)은 **재귀적 생성 규칙**으로 언어를 정의하는 형식 문법이다. 정규 언어보다 표현력이 강해, 괄호 짝맞춤이나 중첩 구조 같은 "개수 세기"를 표현할 수 있다. CFG가 생성하는 언어를 **문맥 자유 언어(CFL)** 라 하며, 이를 인식하는 기계가 **푸시다운 오토마타(PDA)** — 유한 오토마타에 스택을 더한 것이다.

## 직관 (Intuition)

유한 오토마타는 기억이 "현재 상태" 하나뿐이라 깊이를 셀 수 없다. 그래서 `(()())` 같은 괄호 짝맞춤을 못 한다. 여기에 **스택**이라는 무제한 기억을 붙이면, 여는 괄호를 넣고 닫는 괄호에 꺼내며 짝을 셀 수 있다. PDA는 바로 이 "스택 달린 오토마타"다. 프로그래밍 언어 문법이 대부분 CFG로 기술되는 이유다.

## 이론 (Theory)

CFG는 네 요소 $(V, \Sigma, R, S)$로 정의된다 — 변수(비단말) $V$, 단말 $\Sigma$, 생성 규칙 $R$, 시작 기호 $S$. 규칙은 $A \rightarrow \alpha$ 꼴로, 좌변이 **단일 비단말**이라는 점이 "문맥 자유"의 핵심이다.

예: $a^n b^n$ 언어의 문법.

$$S \rightarrow aSb \mid \varepsilon$$

언어 계층(촘스키 위계, Chomsky hierarchy)에서 정규 언어 ⊊ 문맥 자유 언어 ⊊ 결정 가능 언어다.

| 언어 | 인식 기계 | 표현 가능 예 |
|---|---|---|
| 정규 | 유한 오토마타 | `a*b*` |
| 문맥 자유 | 푸시다운 오토마타 | `aⁿbⁿ`, 괄호 짝맞춤 |

CFL에도 한계가 있다 — `aⁿbⁿcⁿ`(세 종류를 동시에 세기)은 문맥 자유가 아니며, **CFL용 펌핑 보조정리**로 증명된다. 또 같은 문자열이 두 가지 파스 트리를 갖는 **모호성(ambiguity)** 이 생길 수 있어, 문법 설계 시 주의해야 한다.

## 구현 (Implementation)

괄호 짝맞춤을 스택(=PDA의 핵심)으로 검사한다.

```python
def balanced(s):
    stack = []
    pairs = {")": "(", "]": "[", "}": "{"}
    for ch in s:
        if ch in "([{":
            stack.append(ch)            # 여는 괄호 push
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False            # 닫는 괄호와 짝이 안 맞음
    return not stack                    # 남은 게 없어야 균형

print(balanced("(()())"))   # True
print(balanced("(()"))      # False
```

## 복잡도 (Complexity)

| 작업 | 시간 |
|---|---|
| 괄호/단순 CFL 인식(스택) | `O(n)` |
| 일반 CFG 파싱(CYK 알고리즘) | `O(n^3)` |
| 결정적 CFL(LR 파서) | `O(n)` |

프로그래밍 언어는 보통 결정적 문맥 자유 문법의 부분집합으로 설계해, 선형 시간 파싱이 가능하게 한다.

## 응용 (Applications)

- 프로그래밍 언어 구문 정의(BNF/EBNF)
- 컴파일러·인터프리터의 구문 분석(파서)
- 마크업·설정 언어(JSON, XML) 문법
- 자연어 처리의 구문 구조 모델

## 흔한 오해 (Common Misunderstandings)

- CFG가 모든 언어를 표현하는 것은 아니다. `aⁿbⁿcⁿ`이나 문맥 의존적 규칙(변수 선언 후 사용 검사 등)은 문맥 자유를 벗어난다.
- 그래서 실제 컴파일러는 구문(CFG)과 의미(타입·선언 검사)를 분리한다. "변수가 선언됐는지"는 파서가 아니라 의미 분석 단계가 본다.
- 모호한 문법은 같은 코드를 다르게 해석할 수 있다(고전적 dangling-else). 문법을 다듬거나 우선순위 규칙으로 해소한다.
- "정규식으로 충분하다"는 착각이 흔하다. 중첩 구조가 있으면 정규 언어로는 불가능하고 CFG가 필요하다.

## TMI

- BNF(배커스-나우어 표기법)는 1959년 ALGOL 60 명세를 위해 만들어졌고, 지금도 언어 명세의 표준 표기법이다.
- "정규식으로 HTML을 파싱하려는" 시도를 막는 유명한 Stack Overflow 답변은, HTML이 정규 언어가 아니라 (대략) 문맥 자유 언어라는 사실에 기반한다.
- CYK 알고리즘의 `O(n^3)`은 동적 프로그래밍으로 모든 부분 문자열의 생성 가능 비단말을 채워 나가는 방식이다.

## 연습 / 확인 문제 (Exercises)

- $a^n b^n$을 생성하는 CFG를 쓰고, 왜 정규 언어가 아닌지 설명하라.
- 모호한 문법의 예를 만들고, 같은 문자열의 두 파스 트리를 그려라.
- 괄호 짝맞춤 검사기를 확장해 세 종류 괄호의 중첩까지 검증하라.

## 이어서 읽기 (Reading Path)

- 이전: [정규 표현식](Regular-Expressions.md)
- 다음: [튜링 머신](Turing-Machine.md)
- 관련: [구문 분석기](../Compilers/Parser.md)

## 참조 (References)

- [CS-Theory/Computation-Theory/Regular-Languages.md](Regular-Languages.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
