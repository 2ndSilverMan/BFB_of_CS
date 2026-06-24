# 러버 덕 디버깅과 코드 리뷰 활용

- Level: Beginner
- Prerequisites: [Engineering/Debugging/Scientific-Debugging.md](Scientific-Debugging.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

러버 덕 디버깅은 문제를 다른 사람이나 물건에게 단계적으로 설명하며 자신의 가정과 빈틈을 발견하는 방법이다. 코드 리뷰는 다른 시각으로 가정과 변경 영향을 검토하게 해 준다.

## 직관 (Intuition)

머릿속에서는 당연해 보이는 흐름도 입 밖으로 설명하면 빈칸이 드러난다. 오리가 대답하지 않아도 설명 과정 자체가 디버거가 된다.

## 이론 (Theory)

설명은 기대 동작, 실제 동작, 이미 확인한 사실, 아직 추측인 것, 가장 작은 재현 절차로 나눠야 한다. 리뷰 요청은 "어딘가 틀린 것 같아요"보다 구체적 가설과 증거를 포함할수록 효과적이다.

## 구현 (Implementation)

```text
1. 이 함수의 목적은 ...
2. 입력은 ...
3. 여기서 상태가 바뀌어야 하는데 ...
4. 실제로는 ...
5. 내가 의심하는 지점은 ...
```

## 복잡도 (Complexity)

Rubber duck debugging의 비용은 설명에 쓰는 시간 정도로 작지만, 효과는 얼마나 구체적으로 가정·관찰·기대 결과를 말하느냐에 달려 있다. 말로 설명해도 모호한 부분은 재현 케이스나 로그로 다시 고정해야 한다.

## 응용 (Applications)

- 막힌 디버깅 세션 전환
- PR 리뷰 품질 개선
- 페어 프로그래밍
- 장애 대응 handoff

## 흔한 오해 (Common Misunderstandings)

- 러버 덕은 초보자만 쓰는 기법이 아니다.
- 코드 리뷰는 스타일 지적만 하는 시간이 아니다.
- 설명 없이 스크린샷만 던지면 협업 비용이 커진다.
- 리뷰어가 원인을 대신 찾아줘야만 성공한 것이 아니다.

## TMI

- Debugging journal을 함께 쓰면 설명이 더 빨라진다.
- Pair debugging은 지식 공유 효과가 크다.
- "내가 아는 사실"과 "내 추측"을 분리하는 습관이 핵심이다.

## 연습 / 확인 문제 (Exercises)

- 현재 버그를 5문장으로 설명하라.
- 리뷰어에게 보낼 디버깅 요청 템플릿을 작성하라.
- 사실과 추측을 나눠 기록하라.

## 이어서 읽기 (Reading Path)

- 이전: [과학적 디버깅](Scientific-Debugging.md)
- 다음: [스택 트레이스](Stack-Traces.md)

## 참조 (References)

- [Engineering/Software-Design/Clean-Code.md](../Software-Design/Clean-Code.md)
- [Reference/Books.md](../../Reference/Books.md)
