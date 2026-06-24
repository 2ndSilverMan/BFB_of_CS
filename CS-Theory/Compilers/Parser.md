# 구문 분석기 (Parser)

- Level: Intermediate
- Prerequisites: [CS-Theory/Compilers/Lexer.md](Lexer.md), [CS-Theory/Computation-Theory/Context-Free.md](../Computation-Theory/Context-Free.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

구문 분석기(parser)는 렉서가 만든 토큰 스트림이 문법에 맞는지 검사하고, 토큰 사이의 계층 구조를 파스 트리나 **추상 구문 트리(AST)** 로 만든다. 연산자 우선순위와 결합 방향, 문장 중첩, 함수 호출 구조를 결정하는 단계다.

## 직관 (Intuition)

`1 + 2 * 3`은 토큰을 왼쪽부터 단순 나열한 것만으로 뜻이 정해지지 않는다. 곱셈이 덧셈보다 먼저라는 문법 규칙에 따라 `1 + (2 * 3)` 구조를 만들어야 결과가 `7`이 된다. 파서는 평평한 토큰 열을 의미 있는 나무로 접는다.

## 이론 (Theory)

문법은 재귀적인 비단말 기호로 표현한다. 다음 문법은 곱셈의 우선순위를 덧셈보다 높게 만든다.

$$
\begin{aligned}
E &\rightarrow T\ ((+ \mid -)\ T)^* \\
T &\rightarrow F\ ((* \mid /)\ F)^* \\
F &\rightarrow \text{INT} \mid (E)
\end{aligned}
$$

대표적인 파서 계열은 다음과 같다.

| 계열 | 방향 | 특징 |
|---|---|---|
| 재귀 하강 / LL | 위에서 아래 | 손으로 구현하기 쉽고 오류 메시지 제어가 편함 |
| LR / LALR | 아래에서 위 | 더 넓은 문법을 다루며 생성기에서 흔함 |
| Pratt parser | 표현식 중심 | 연산자 우선순위와 결합성을 간결하게 처리 |
| Earley / CYK | 일반 CFG | 폭넓은 문법을 처리하지만 비용이 큼 |

LL(1) 파서는 한 토큰 미리보기로 적용할 생성 규칙을 결정해야 한다. 직접 왼쪽 재귀가 있는 $E \rightarrow E + T \mid T$는 재귀 하강 파서가 무한 재귀하므로 반복 형태나 오른쪽 재귀로 변환한다. 모호한 문법은 같은 입력에 여러 파스 트리를 허용하므로 우선순위와 결합 규칙을 문법에 반영해야 한다.

## 구현 (Implementation)

정수와 덧셈을 처리하는 재귀 하강 파서의 핵심이다. 토큰은 `(종류, 값)` 튜플이라고 가정한다.

```python
class Parser:
    def __init__(self, tokens):
        self.tokens = tokens + [("EOF", None)]
        self.pos = 0

    def take(self, expected):
        kind, value = self.tokens[self.pos]
        if kind != expected:
            raise SyntaxError(f"expected {expected}, got {kind}")
        self.pos += 1
        return value

    def expression(self):
        node = ("integer", self.take("INT"))
        while self.tokens[self.pos][0] == "PLUS":
            self.take("PLUS")
            right = ("integer", self.take("INT"))
            node = ("add", node, right)
        return node

    def parse(self):
        node = self.expression()
        self.take("EOF")
        return node


print(Parser([("INT", 1), ("PLUS", "+"), ("INT", 2)]).parse())
```

실전 파서는 예상 토큰 집합과 원본 위치를 활용해 오류를 보고하고, 세미콜론이나 닫는 괄호 같은 동기화 지점까지 건너뛰어 여러 오류를 한 번에 찾기도 한다.

## 복잡도 (Complexity)

결정적인 LL/LR 문법의 파서는 토큰 수 $n$에 대해 보통 시간 `O(n)`이다. 재귀 하강 파서의 호출 스택은 중첩 깊이 $h$에 대해 `O(h)`, AST 저장은 `O(n)`이다. 일반 CFG 파싱은 Earley의 경우 보통 `O(n^3)` 최악 시간이며 문법 특성에 따라 더 빨라질 수 있다.

## 응용 (Applications)

- 프로그래밍 언어와 DSL의 구문 트리 생성
- IDE의 실시간 오류 진단과 코드 구조 탐색
- 포매터, 린터, 리팩터링 도구의 구조적 입력 제공
- SQL, 정규식, 명령행 표현식 같은 작은 언어 해석

## 흔한 오해 (Common Misunderstandings)

- 파서는 변수 선언 여부나 타입 호환성을 보통 검사하지 않는다. 이는 의미 분석 단계의 책임이다.
- 문법이 CFG라고 아무 파서 알고리즘으로나 처리되는 것은 아니다. LL, LR 등은 서로 다른 문법 부분집합과 변환 조건을 가진다.
- 왼쪽 재귀는 모든 파서에서 나쁜 것이 아니다. 재귀 하강에는 문제지만 LR 파서는 자연스럽게 다룬다.
- 첫 오류에서 무조건 중단하는 것이 항상 좋은 전략은 아니다. 편집기용 파서는 불완전한 코드에서도 부분 트리를 만들어야 한다.

## TMI

- "dangling else"는 `else`가 어느 `if`에 붙는지 모호해지는 고전적인 문법 문제다. 많은 언어는 가장 가까운 아직 짝 없는 `if`에 붙인다.
- Pratt parsing은 작은 코드로 전위·중위·후위 연산자와 우선순위를 다룰 수 있어 수작업 언어 구현에서 인기가 높다.
- 산업용 IDE 파서는 입력이 늘 깨져 있다는 전제에서 동작한다. 사용자가 타이핑하는 순간 대부분의 파일은 잠시 문법적으로 불완전하기 때문이다.

## 연습 / 확인 문제 (Exercises)

- 구현 예시에 곱셈을 추가하고 `1 + 2 * 3`이 올바른 트리를 만들게 하라.
- 왼쪽 재귀 문법 $E \rightarrow E + T \mid T$를 반복 가능한 형태로 바꿔라.
- 닫는 괄호가 빠진 입력에서 유용한 위치와 예상 토큰을 출력하도록 오류를 개선하라.

## 이어서 읽기 (Reading Path)

- 이전: [어휘 분석기](Lexer.md)
- 다음: [추상 구문 트리](AST.md)
- 관련: [문맥 자유 문법과 푸시다운 오토마타](../Computation-Theory/Context-Free.md)

## 참조 (References)

- [CS-Theory/Compilers/Lexer.md](Lexer.md)
- [CS-Theory/Computation-Theory/Context-Free.md](../Computation-Theory/Context-Free.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
