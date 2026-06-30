# 사후 분석 (Postmortem)

- Level: Intermediate
- Prerequisites: [Engineering/Debugging/Error-Tracking.md](Error-Tracking.md), [Engineering/Debugging/Scientific-Debugging.md](Scientific-Debugging.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

사후 분석은 장애나 중대한 버그가 끝난 뒤 타임라인, 영향, 원인, 대응, 재발 방지 액션을 기록하는 학습 문서다. 목적은 비난이 아니라 시스템 개선이다.

## 직관 (Intuition)

불이 꺼진 뒤 "누가 잘못했나"만 보면 다음 불을 막지 못한다. 왜 불이 커졌고, 어떤 감지·대응·설계가 부족했는지 기록해야 한다.

## 이론 (Theory)

좋은 postmortem은 impact, detection, timeline, root/contributing factors, what went well, what went poorly, action items를 포함한다. Action item은 owner와 due date가 있어야 한다.

### Blameless와 accountability

Blameless postmortem은 책임을 없애자는 뜻이 아니라 개인 비난 대신 시스템 개선에 집중하자는 뜻이다. 누가 실수했는가보다 어떤 조건이 그 실수를 가능하게 했고, 탐지와 복구가 왜 늦었는지를 묻는다.

좋은 action item은 구체적 owner, deadline, 검증 방법이 있다. "주의하기"는 action item이 아니라 희망사항이다. Runbook, alert, test, guardrail, 자동화로 바뀌어야 재발 방지 효과가 있다.

## 구현 (Implementation)

```text
Impact:
Timeline:
Detection:
Root cause:
Contributing factors:
Action items:
Lessons:
```

## 복잡도 (Complexity)

Postmortem 작성 비용은 incident 기간, 관련 system 수, timeline 근거의 품질에 좌우된다. 분석 자체보다 action item을 추적하고 완료를 검증하는 비용이 재발 방지 효과를 결정한다.

## 응용 (Applications)

- 장애 학습과 공유
- 재발 방지 추적
- 운영 프로세스 개선
- 신뢰성 문화 형성

## 흔한 오해 (Common Misunderstandings)

- Postmortem은 책임자 색출 문서가 아니다.
- Root cause 하나만 찾으면 끝나는 것이 아니다. 기여 요인을 봐야 한다.
- 액션 아이템이 추적되지 않으면 문서만 남는다.
- 작은 장애도 반복되면 분석 가치가 있다.

## TMI

- Blameless postmortem은 개인 비난보다 시스템 조건을 본다.
- Near miss도 기록하면 큰 사고를 예방할 수 있다.
- 타임라인은 채팅 로그와 모니터링 이벤트를 근거로 재구성한다.

## 연습 / 확인 문제 (Exercises)

- 최근 버그를 postmortem 템플릿으로 작성하라.
- 좋은 action item과 나쁜 action item을 비교하라.
- Blameless 문장으로 원인을 다시 써라.

## 이어서 읽기 (Reading Path)

- 이전: [에러 트래킹](Error-Tracking.md), [카나리와 기능 플래그](Canary-Feature-Flags.md)
- 다음: [DevOps](../DevOps/), [Metrics and Alerts](../DevOps/Metrics-Alerts.md)

## 참조 (References)

- [Engineering/Debugging/Scientific-Debugging.md](Scientific-Debugging.md)
- [Reference/Books.md](../../Reference/Books.md)
