# 카나리 배포와 기능 플래그 활용

- Level: Intermediate
- Prerequisites: [Engineering/Debugging/Structured-Logging.md](Structured-Logging.md), [Engineering/System-Design/Load-Balancing.md](../System-Design/Load-Balancing.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

카나리 배포는 새 버전을 일부 트래픽에만 먼저 노출해 이상을 확인하는 방식이고, 기능 플래그는 코드를 배포한 뒤 기능 활성화 여부를 설정으로 제어하는 방법이다.

## 직관 (Intuition)

모든 사용자를 한 번에 새 다리로 보내지 않고 일부만 먼저 지나가게 해 안전성을 확인한다. 문제가 있으면 플래그를 끄거나 트래픽을 되돌린다.

## 이론 (Theory)

카나리는 error rate, latency, business metric, log anomaly를 비교해야 한다. 기능 플래그는 release flag, experiment flag, ops kill switch 등 목적별 수명이 다르며 오래된 플래그는 기술 부채가 된다.

## 구현 (Implementation)

```python
if flags.enabled("new_checkout", user):
    return new_checkout(user)
return old_checkout(user)
```

## 복잡도 (Complexity)

Canary 비용은 rollout 단계 수, 각 단계의 관찰 시간, 필요한 traffic 양에 좌우된다. 단계를 잘게 쪼갤수록 blast radius는 줄지만 배포 시간이 길어지고, metric 지연이 크면 잘못된 버전을 오래 노출할 수 있다.

## 응용 (Applications)

- 위험한 변경의 점진 출시
- A/B 테스트
- 즉시 rollback 대신 kill switch
- 특정 고객 대상 기능 공개

## 흔한 오해 (Common Misunderstandings)

- 카나리 비율만 낮추면 안전한 것은 아니다. 관측 metric이 필요하다.
- 기능 플래그는 제거하지 않으면 복잡도를 늘린다.
- DB schema 변경은 플래그만으로 안전해지지 않는다.
- 카나리 대상이 전체 사용자를 대표하지 않을 수 있다.

## TMI

- Dark launch는 사용자에게 보이지 않게 새 경로를 미리 실행해 보는 방식이다.
- Ring deployment는 내부→소규모→전체처럼 단계적 범위를 둔다.
- Flag ownership과 만료일을 기록하면 부채를 줄인다.

## 연습 / 확인 문제 (Exercises)

- 결제 기능 카나리 배포 metric을 정의하라.
- 기능 플래그 제거 절차를 작성하라.
- 카나리와 A/B 테스트의 목적 차이를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [로드 밸런싱](../System-Design/Load-Balancing.md)
- 다음: [에러 트래킹](Error-Tracking.md), [Postmortem](Postmortem.md)

## 참조 (References)

- [Engineering/System-Design/Load-Balancing.md](../System-Design/Load-Balancing.md)
- [Engineering/DevOps/Metrics-Alerts.md](../DevOps/Metrics-Alerts.md)
