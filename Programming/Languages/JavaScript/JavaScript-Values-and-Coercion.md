# JavaScript 값과 타입 변환 (Values and Coercion)

- Level: Beginner
- Prerequisites: [JavaScript 기본 문법](JavaScript-Setup-and-Syntax.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

JavaScript 값은 원시값과 객체로 나뉘며, 연산 중 암묵적 타입 변환(coercion)이 일어날 수 있다. `null`, `undefined`, truthy/falsy, `NaN`은 반드시 익숙해져야 하는 기본 개념이다.

## 직관 (Intuition)

JavaScript는 편의를 위해 값을 자동으로 바꿔 주려 하지만, 그 친절함이 버그가 되기도 한다. 그래서 "언제 변환되는가"를 알고 명시적으로 다루는 습관이 중요하다.

## 핵심 문법 (Core Syntax)

```javascript
console.log(Boolean(""));
console.log(Boolean("hello"));
console.log(Number("42"));
console.log(Number("not a number"));

const value = null;
if (value == null) {
  console.log("null 또는 undefined");
}
```

Falsy 값에는 `false`, `0`, `""`, `null`, `undefined`, `NaN` 등이 있다.

## 이론 (Theory)

`undefined`는 값이 아직 주어지지 않았음을, `null`은 의도적으로 비어 있음을 표현하는 경우가 많다. `NaN`은 숫자 타입의 특수값이며 자기 자신과도 같지 않다.

## 구현 (Implementation)

값 비교는 기본적으로 `===`를 사용하고, 필요한 변환은 `Number()`, `String()`, `Boolean()`처럼 명시한다. `null`, `undefined`, `NaN`, truthy/falsy 값을 표로 만들어 직접 평가해 보면 coercion 함정을 줄일 수 있다.

## 복잡도 (Complexity)

숫자와 boolean 변환은 대체로 작지만 문자열 parsing은 입력 길이에 비례한다. 객체와 배열은 reference로 전달되므로 복사 여부가 memory와 mutation 비용을 결정하고, 암묵 변환은 성능보다 correctness 비용이 더 크다.

## 응용 (Applications)

- 사용자 입력 파싱
- API 응답 검증
- 조건문 안전성 개선
- 폼 값 처리

## 흔한 오해 (Common Misunderstandings)

- `typeof null`은 `"object"`로 나오지만 실제 객체처럼 다루면 안 된다.
- `NaN === NaN`은 `false`다. 확인에는 `Number.isNaN`을 쓴다.
- 빈 배열 `[]`은 truthy다.
- `||`로 기본값을 주면 `0`이나 빈 문자열도 대체될 수 있다. 필요하면 `??`를 쓴다.

## TMI

- `??`는 nullish coalescing operator로 `null` 또는 `undefined`일 때만 오른쪽 값을 사용한다.
- Optional chaining `?.`은 중첩 속성 접근에서 오류를 줄인다.
- TypeScript는 이런 값 흐름을 정적으로 더 잘 잡게 도와준다.

## 연습 / 확인 문제 (Exercises)

- Falsy 값 목록을 직접 조건문으로 확인하라.
- `||`와 `??`가 다르게 동작하는 예를 작성하라.
- `Number.isNaN(NaN)`과 `NaN === NaN` 결과를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [JavaScript 기본 문법](JavaScript-Setup-and-Syntax.md)
- 다음: [함수와 스코프](JavaScript-Functions-and-Scope.md)

## 참조 (References)

- [Programming/Variables-and-Types.md](../../Variables-and-Types.md)
- [Reference/Books.md](../../../Reference/Books.md)
