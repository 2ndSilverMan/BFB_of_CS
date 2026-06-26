# 과학적 디버깅 (Scientific Debugging)

- Level: Intermediate
- Prerequisites: [Engineering/Testing/Unit-Test-Principles.md](../Testing/Unit-Test-Principles.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

과학적 디버깅은 증상을 관찰하고 재현 가능한 사실에서 가설을 세운 뒤 한 변수를 바꾸는 실험으로 원인을 좁히고 수정 후 반증 test로 검증하는 방법이다.

## 직관 (Intuition)

무작정 code를 바꾸는 대신 탐정처럼 증거와 추측을 분리한다. 각 실험은 가능한 원인 집합을 줄여야 한다.

## 이론 (Theory)

1. Expected/actual behavior와 최초 실패 시점을 기록
2. Minimal reproduction과 환경 고정
3. Data flow·control flow에서 가설 우선순위화
4. 한 변수만 바꾸는 실험
5. 원인에 가까운 작은 regression test
6. Fix, negative test, adjacent impact 검증

Observation, inference, action log를 분리하면 같은 실패를 반복하지 않는다. Binary search는 commit, input, pipeline stage를 절반씩 줄이는 강력한 실험이다.

## 구현 (Implementation)

```text
관찰: 특정 timezone에서 자정 주문만 하루 전으로 저장됨
가설: local date를 UTC timestamp로 변환하는 경계 오류
실험: UTC와 +09:00 입력을 같은 instant로 고정해 비교
결과: timezone offset을 두 번 적용함
검증: DST·월말·자정 regression cases 추가
```

## 복잡도 (Complexity)

후보 $n$개를 순차 확인하면 `O(n)`, 균등하게 나눌 수 있는 탐색은 `O(log n)` 실험으로 줄일 수 있다. 좋은 observability는 각 실험 비용을 낮춘다.

## 응용 (Applications)

- code·data·configuration bug
- intermittent production incident
- performance regression
- distributed failure investigation

## 흔한 오해 (Common Misunderstandings)

- 증상을 없앤 것이 root cause 수정은 아니다.
- 동시에 여러 변경을 하면 어떤 것이 효과였는지 모른다.
- log가 많다고 evidence가 좋은 것은 아니다.
- 재현 실패가 bug 부재를 증명하지 않는다.

## TMI

- debugging journal은 pair·handoff에서 중복 실험을 줄인다.
- minimal reproducer 작성 중 원인이 드러나는 경우가 많다.
- 가장 최근 변경은 좋은 후보지만 확정 원인은 아니다.

## 연습 / 확인 문제 (Exercises)

- flaky test의 가설 tree를 작성하라.
- input을 delta debugging으로 줄여라.
- fix를 반증할 regression test를 설계하라.

## 이어서 읽기 (Reading Path)

- 이전: [단위 테스트 원칙](../Testing/Unit-Test-Principles.md)
- 다음: [스택 트레이스](Stack-Traces.md), [구조화 로깅](Structured-Logging.md)
- 관련: [최소 재현 케이스](Minimal-Reproducible-Example.md), [러버 덕 디버깅과 코드 리뷰 활용](Rubber-Duck-Debugging.md)

## 참조 (References)

- [Engineering/Testing/Unit-Test-Principles.md](../Testing/Unit-Test-Principles.md)
- [Reference/Books.md](../../Reference/Books.md)
