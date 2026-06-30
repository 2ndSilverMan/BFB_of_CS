# 정규 표현식 (Regular Expressions)

- Level: Intermediate
- Prerequisites: [CS-Theory/Computation-Theory/Regular-Languages.md](Regular-Languages.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

정규 표현식(정규식)은 **정규 언어를 기술하는 대수적 표기법**이다. 문자, 연결, 선택(`|`), 반복(`*`)을 조합해 문자열의 패턴을 표현한다. 이론적으로 정규식이 표현하는 언어의 집합은 [유한 오토마타](Regular-Languages.md)가 인식하는 언어의 집합과 **정확히 일치**한다.

## 직관 (Intuition)

"숫자 한 개 이상으로 이뤄진 문자열" 같은 패턴을 매번 코드로 짜는 대신, `[0-9]+`라는 짧은 식 하나로 기술한다. 정규식은 패턴을 선언적으로 적으면, 엔진이 그것을 오토마타로 바꿔 매칭을 수행해 준다. "패턴의 언어"인 셈이다.

## 이론 (Theory)

형식적으로 정규식은 세 가지 기본 연산으로 정의된다(클레이니 정리, Kleene's theorem가 정규식 ↔ 유한 오토마타 동치를 보장).

| 연산 | 표기 | 의미 |
|---|---|---|
| 연결(concatenation) | `ab` | `a` 다음 `b` |
| 선택(union) | `a\|b` | `a` 또는 `b` |
| 반복(Kleene star) | `a*` | `a`를 0번 이상 |

이 세 연산의 닫힘(closure)으로 만들 수 있는 언어가 곧 정규 언어다. 자주 쓰는 `+`(1번 이상), `?`(0 또는 1번), `[...]`(문자 클래스)는 위 세 연산의 축약이다.

정규식의 표현력에는 한계가 있다 — **중첩된 괄호 짝맞춤**이나 `aⁿbⁿ` 같은 "개수 세기"는 정규 언어가 아니라서 (순수) 정규식으로 표현할 수 없다. 이는 [펌핑 보조정리](Regular-Languages.md)로 증명된다.

> 주의: 많은 프로그래밍 언어의 "정규식"은 역참조(backreference) 같은 비정규 기능을 포함해, 이론적 정규 언어보다 강하지만 최악의 경우 지수 시간이 걸릴 수 있다.

## 구현 (Implementation)

파이썬 표준 라이브러리 `re`로 패턴을 매칭한다.

```python
import re

pattern = r"^[a-z]+@[a-z]+\.[a-z]+$"     # 아주 단순화한 이메일 패턴
print(bool(re.match(pattern, "a@b.com")))    # True
print(bool(re.match(pattern, "a@@b")))       # False

# 숫자 추출
print(re.findall(r"\d+", "order 12 has 3 items"))   # ['12', '3']
```

`*`, `+`의 기본 동작은 **탐욕적(greedy)** 으로 가능한 한 길게 매칭한다. `*?`, `+?`는 최소 매칭(lazy)이다.

## 복잡도 (Complexity)

`n`은 입력 길이, `m`은 패턴 길이다.

| 엔진 방식 | 시간 |
|---|---|
| DFA/NFA 기반(Thompson NFA) | `O(n·m)` 보장 |
| 백트래킹 기반(역참조 지원) | 최악 `O(2^n)` 가능(파국적 백트래킹) |

순수 정규 언어용 엔진은 입력 길이에 선형이지만, 역참조 등 확장 기능을 쓰는 백트래킹 엔진은 특정 패턴에서 폭발적으로 느려질 수 있다.

## 응용 (Applications)

- 입력 검증(이메일·전화번호 형식 등 — 단, 완벽한 이메일 검증은 정규식만으로 어렵다)
- 로그·텍스트에서 패턴 추출(`grep`, `sed`)
- 컴파일러의 어휘 분석(토큰 정의)
- 찾기/바꾸기, 구문 강조

## 흔한 오해 (Common Misunderstandings)

- 정규식으로 모든 패턴을 표현할 수 있는 것은 아니다. 괄호 짝맞춤·HTML 중첩 구조는 정규 언어가 아니다(유명한 "정규식으로 HTML 파싱하지 마라").
- 프로그래밍 언어의 "정규식"은 이론적 정규식과 다르다. 역참조 같은 기능 때문에 더 강하지만 느려질 수 있다.
- 탐욕적 매칭을 모르면 `.*`가 의도보다 너무 많이 잡아먹는 버그가 흔하다.
- 정규식이 짧다고 빠른 게 아니다. 패턴 구조에 따라 백트래킹이 폭발(ReDoS)할 수 있다.

## TMI

- 정규식의 이론적 토대인 정규 언어와 `*` 연산은 1951년 스티븐 클레이니(Kleene)가 정립했다. 그래서 `*`를 "클레이니 스타"라 부른다.
- ReDoS(정규식 서비스 거부)는 `(a+)+$` 같은 패턴에 악의적 입력을 넣어 서버를 마비시키는 실제 공격이다. 입력 검증 정규식의 보안 취약점으로 다뤄진다.
- 켄 톰슨이 1968년 제안한 NFA 시뮬레이션 방식은 백트래킹 없이 선형 시간을 보장하며, 현대의 RE2·Rust regex 같은 엔진이 이 계열이다.

## 연습 / 확인 문제 (Exercises)

- "0과 1로 이뤄지고 1로 끝나는 문자열"을 정규식으로 작성하라.
- `aⁿbⁿ`이 정규식으로 표현 불가능한 이유를 펌핑 보조정리로 설명하라.
- 탐욕적 `.*`와 게으른 `.*?`가 같은 입력에서 다르게 매칭되는 예를 만들어라.

## 이어서 읽기 (Reading Path)

- 이전: [정규 언어와 유한 오토마타](Regular-Languages.md)
- 다음: [문맥 자유 문법](Context-Free.md)
- 관련: [어휘 분석기](../Compilers/Lexer.md)

## 참조 (References)

- [CS-Theory/Computation-Theory/Regular-Languages.md](Regular-Languages.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
