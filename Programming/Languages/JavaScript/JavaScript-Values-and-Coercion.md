# JavaScript 값과 타입 변환 (Values and Coercion)

- Level: Beginner
- Prerequisites: [JavaScript 기본 문법](JavaScript-Setup-and-Syntax.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

JavaScript 값은 **7가지 원시값**(string, number, bigint, boolean, undefined, symbol, null)과 **객체**로 나뉜다. 연산 중 **암묵적 타입 변환(coercion)** 이 일어나는데, 그 규칙(ToPrimitive→ToNumber/ToString)을 알아야 `==`·`+`·truthy의 함정을 피한다.

## 직관 (Intuition)

JavaScript는 편의를 위해 값을 자동으로 바꿔 준다. 그 친절함이 곧 버그의 원천이다. 해법은 "언제 어떤 규칙으로 변환되는가"를 알고 **명시적 변환 + `===`** 를 쓰는 것.

## 핵심 문법 (Core Syntax)

```javascript
Boolean("");          // false   (falsy)
Boolean("hello");     // true
Number("42");         // 42
Number("x");          // NaN
value == null;        // value가 null 또는 undefined일 때만 true
```

falsy: `false, 0, -0, 0n, "", null, undefined, NaN`. 그 외는 모두 truthy(빈 배열·빈 객체 포함).

## 이론 (Theory)

### 1. `==` 의 추상 동등 알고리즘

`==` 는 타입이 다르면 한쪽을 변환해 비교한다(대략: 불리언→숫자, 문자열↔숫자는 숫자로, 객체→원시값). 그래서 `0 == ""`(둘 다 0), `0 == "0"`, `"" == "0"` 가 `false` 인 **비추이성**이 생긴다. `===` 는 변환 없이 타입+값 비교 → **항상 `===`**.

### 2. null vs undefined vs NaN

`undefined` = 값이 안 주어짐, `null` = 의도적 비움. `NaN` 은 숫자 특수값이며 **자기 자신과도 같지 않다**(`NaN === NaN` 은 false) → `Number.isNaN`. `typeof null === "object"` 는 언어 초기의 유명한 버그.

### 3. `||` vs `??`

`||` 는 falsy면 오른쪽(그래서 `0`·`""` 도 대체) — 기본값 버그의 원천. `??`(nullish)는 **null/undefined일 때만** 오른쪽 → 0이나 빈 문자열을 보존.

## 구현 (Implementation)

```javascript
0 == "";    // true   ← 추상 동등의 함정(둘 다 ToNumber 0)
0 === "";   // false  ← 권장
[] == ![];  // true   ← ![]=false→0, []→""→0  (악명 높은 예)

function toInt(value) {
  const n = Number(value);
  return Number.isNaN(n) ? 0 : n;           // 명시적 변환 + NaN 가드
}
const count = config.retries ?? 3;          // 0이면 0 유지(|| 였으면 3)
```

## 복잡도 (Complexity)

| 항목 | 특성 |
|---|---|
| number/boolean 변환 | $O(1)$ |
| 문자열 파싱 | 입력 길이에 비례 |
| 객체/배열 | 참조 전달 — 복사 여부가 메모리·mutation 비용 결정 |

암묵 변환의 비용은 성능보다 **correctness**다.

## 응용 (Applications)

- 사용자 입력·폼 값 파싱, API 응답 검증, 조건문 안전성.

## 흔한 오해 (Common Misunderstandings)

- **`typeof null === "object"`** — 객체처럼 다루면 안 됨.
- **`NaN === NaN` 은 false** — `Number.isNaN` 사용.
- **빈 배열 `[]` 은 truthy** (하지만 `[] == false` 는 true — 다른 경로).
- **`||` 기본값은 0/""도 대체** — 필요하면 `??`.
- **`==` 는 추이적이지 않다** — `===` 만 안전.

## TMI

- `??` 와 `||` 를 괄호 없이 섞으면 문법 에러다(우선순위 모호성을 막으려는 설계).
- 옵셔널 체이닝 `?.` 은 `null/undefined` 면 단락(`a?.b?.c`)해 `TypeError` 를 막는다.
- TypeScript는 이런 값 흐름을 정적으로 잡아 coercion 버그를 컴파일 타임에 드러낸다.

## 연습 / 확인 문제 (Exercises)

- falsy 값 목록을 조건문으로 직접 확인하라.
- `||` 와 `??` 가 `0` 입력에서 다르게 동작하는 예를 작성하라.
- `[] == ![]` 가 왜 true인지 변환 단계를 추적하라.
- `0 == "0"`, `0 == ""`, `"" == "0"` 의 결과로 `==` 의 비추이성을 보여라.

## 이어서 읽기 (Reading Path)

- 이전: [JavaScript 기본 문법](JavaScript-Setup-and-Syntax.md)
- 다음: [함수와 스코프](JavaScript-Functions-and-Scope.md)
- 관련: [변수와 타입](../../Variables-and-Types.md)

## 참조 (References)

- [Programming/Variables-and-Types.md](../../Variables-and-Types.md)
- [Reference/Books.md](../../../Reference/Books.md)
