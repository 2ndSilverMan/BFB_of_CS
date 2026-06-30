# 경계값 분석과 동등 분할

- Level: Intermediate
- Prerequisites: [Engineering/Testing/Unit-Test-Principles.md](Unit-Test-Principles.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

경계값 분석은 입력 범위의 경계 주변에서 버그가 자주 난다는 점을 이용해 테스트 값을 고르는 기법이다. 동등 분할은 같은 방식으로 처리될 입력을 그룹으로 나눠 대표값을 고른다.

## 직관 (Intuition)

나이 제한이 18세라면 0, 10, 50보다 17, 18, 19가 더 중요하다. 조건이 바뀌는 문턱에서 실수가 자주 발생한다.

## 이론 (Theory)

입력 domain을 valid/invalid partition으로 나누고 각 partition의 대표값을 고른다. 경계에서는 `min`, `min+1`, `max-1`, `max`, `max+1` 같은 값을 확인한다.

### 경계의 종류

경계값은 숫자 범위만 의미하지 않는다. 빈 문자열, 최대 길이, timezone 전환, leap day, 권한 없음, 중복 요청, 정렬 동률, pagination 마지막 페이지도 모두 경계다. 결함은 보통 normal case 내부보다 비교 연산이 바뀌는 지점에서 많이 나온다.

동등 분할은 입력 공간을 같은 규칙으로 처리되는 그룹으로 나누는 기법이다. 각 partition에서 대표값을 고르고, partition 사이 경계에서 바로 안쪽/바깥쪽 값을 추가하면 적은 테스트로 많은 위험을 덮을 수 있다.

## 구현 (Implementation)

```python
def is_valid_age(age):
    return 0 <= age <= 120


def test_age_boundaries():
    assert not is_valid_age(-1)
    assert is_valid_age(0)
    assert is_valid_age(120)
    assert not is_valid_age(121)
```

## 복잡도 (Complexity)

모든 입력을 테스트할 수 없기 때문에 partition을 잘 나눠 테스트 수를 줄인다. 여러 입력이 조합되면 pairwise testing 같은 방법을 고려한다.

## 응용 (Applications)

- 폼 validation
- 가격·수량 제한
- 날짜 범위 검사
- API parameter validation

## 흔한 오해 (Common Misunderstandings)

- 임의 값 몇 개보다 경계값이 더 가치 있는 경우가 많다.
- 경계는 숫자뿐 아니라 문자열 길이, 날짜, 상태 전이에도 있다.
- 동등 분할은 구현이 아니라 요구사항 기준으로 나눠야 한다.
- Invalid partition도 반드시 테스트해야 한다.

## TMI

- Off-by-one bug는 경계값 테스트의 단골 손님이다.
- Empty, one, many는 컬렉션 테스트의 기본 경계다.
- Timezone과 daylight saving은 날짜 경계의 함정이다.

## 연습 / 확인 문제 (Exercises)

- 비밀번호 길이 8~64 조건의 테스트 값을 고르라.
- 가격 할인 규칙을 partition으로 나눠라.
- 날짜 범위 API의 경계값을 설계하라.

## 이어서 읽기 (Reading Path)

- 이전: [단위 테스트 원칙](Unit-Test-Principles.md)
- 다음: [TDD](TDD.md)

## 참조 (References)

- [Engineering/Testing/Unit-Test-Principles.md](Unit-Test-Principles.md)
- [Reference/Books.md](../../Reference/Books.md)
