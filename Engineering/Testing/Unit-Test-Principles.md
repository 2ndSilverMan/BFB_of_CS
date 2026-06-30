# 단위 테스트 작성 원칙 (Unit Test Principles)

- Level: Intermediate
- Prerequisites: [Engineering/Testing/Testing-Pyramid.md](Testing-Pyramid.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

단위 테스트는 작은 behavior 단위를 빠르고 결정적으로 검증한다. 좋은 test는 실패 이유가 분명하고 구현 세부보다 observable contract를 검증하며 유지보수 비용이 낮다.

## 직관 (Intuition)

Test는 code를 비추는 작은 실험이다. 준비, 행동, 검증이 한눈에 보이고 한 이유로 실패해야 debugging signal이 선명하다.

## 이론 (Theory)

AAA는 Arrange-Act-Assert 구조다. FIRST는 Fast, Independent, Repeatable, Self-validating, Timely를 강조한다. Boundary와 representative equivalence class를 고르고 happy path뿐 아니라 error contract를 검증한다.

Mock은 interaction이 contract인 경계에서 제한적으로 쓰고 내부 호출 순서를 과도하게 고정하지 않는다. Time, random, network는 injectable dependency로 제어한다.

### Contract 중심 테스트

좋은 단위 테스트는 내부 구현 순서가 아니라 외부에서 관찰 가능한 contract를 고정한다. 입력, 출력, 예외, 상태 변화, side effect 경계를 명확히 하고, refactor 중 바뀌어도 되는 내부 호출 순서는 가능한 한 고정하지 않는다.

Mock은 네트워크, 시간, 파일 시스템, 결제 API처럼 process 밖 경계에 유용하다. 같은 process 내부 협력 객체를 과도하게 mock하면 설계가 취약해지고 테스트가 구현 복제본이 된다.

## 구현 (Implementation)

```python
def divide(a, b):
    if b == 0:
        raise ValueError("divisor must be non-zero")
    return a / b


def test_divide_rejects_zero():
    try:
        divide(1, 0)
        assert False
    except ValueError as error:
        assert "non-zero" in str(error)
```

## 복잡도 (Complexity)

Test 실행 비용은 대상+fixture setup이다. Shared fixture가 크면 개별 test는 빨라도 suite coupling과 병렬화 문제가 생긴다.

## 응용 (Applications)

- domain rule regression
- refactoring safety net
- edge/error behavior documentation
- fast CI feedback

## 흔한 오해 (Common Misunderstandings)

- 함수마다 test 하나가 충분하다는 규칙은 없다.
- private method를 직접 test해야 하는 것은 아니다.
- coverage 100%가 assertion 품질을 보장하지 않는다.
- mock 호출 수만 확인하면 실제 output contract를 놓칠 수 있다.

## TMI

- property-based testing은 example 대신 invariant와 generator를 정의한다.
- mutation testing은 code를 일부 바꿔 test가 실패하는지 본다.
- test 이름을 behavior 문장으로 쓰면 실패 report가 문서가 된다.

## 연습 / 확인 문제 (Exercises)

- boundary value를 포함한 divide test를 작성하라.
- brittle interaction test를 state/output test로 바꿔라.
- random dependency를 주입 가능하게 refactor하라.

## 이어서 읽기 (Reading Path)

- 이전: [테스트 피라미드](Testing-Pyramid.md)
- 다음: [통합 테스트 전략](Integration-Test-Strategy.md)
- 관련: [과학적 디버깅](../Debugging/Scientific-Debugging.md), [경계값 분석과 동등 분할](Boundary-Value-Analysis.md), [테스트 더블](Test-Doubles.md)

## 참조 (References)

- [Engineering/Testing/Testing-Pyramid.md](Testing-Pyramid.md)
- [Reference/Books.md](../../Reference/Books.md)
