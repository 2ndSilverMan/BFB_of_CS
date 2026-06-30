# SLI, SLO, SLA

- Level: Intermediate
- Prerequisites: [Engineering/DevOps/Metrics-Alerts.md](Metrics-Alerts.md), [Engineering/DevOps/Distributed-Tracing.md](Distributed-Tracing.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

SLI는 서비스 수준을 재는 지표, SLO는 목표, SLA는 사용자나 고객과 약속한 계약적 보장이다.

## 직관 (Intuition)

SLI는 체온계 숫자, SLO는 정상 체온 범위, SLA는 그 범위를 지키지 못했을 때의 공식 약속에 가깝다.

## 이론 (Theory)

좋은 SLI는 사용자 경험과 직접 연결된다. 예를 들어 availability, successful request ratio, p95 latency, freshness가 있다. SLO는 일정 기간 동안 SLI가 만족해야 하는 목표다. Error budget은 100%에서 SLO를 뺀 허용 실패량이며, release velocity와 reliability trade-off를 조정하는 도구다. SLA는 법적·상업적 책임을 동반하므로 SLO보다 보수적으로 잡는 경우가 많다.

### Error budget 운영

SLO는 목표 숫자가 아니라 의사결정 장치다. Error budget을 빠르게 쓰고 있으면 release 속도를 줄이고 reliability work를 우선한다. Budget이 충분하면 개선 실험과 기능 배포를 진행할 여지가 있다.

SLI는 사용자가 느끼는 경험과 가까워야 한다. 내부 CPU나 pod restart보다 request success rate, p95 latency, freshness, durability 같은 user-facing metric이 더 좋은 출발점이다.

## 구현 (Implementation)

```text
SLI: 5xx가 아닌 HTTP 요청 비율
SLO: 28일 rolling window에서 99.9% 이상
SLA: 월간 99.5% 미만이면 credit 제공
```

Alert는 순간 CPU보다 error budget burn rate처럼 사용자 영향에 가까운 신호에 연결하는 편이 좋다.

## 복잡도 (Complexity)

SLO window, traffic volume, low-traffic service, dependency failure attribution이 해석을 어렵게 만든다. 너무 많은 SLO는 운영 집중도를 낮춘다.

## 응용 (Applications)

- reliability 목표 설정
- alert threshold 설계
- release freeze 판단
- 고객 계약 기준 정의

## 흔한 오해 (Common Misunderstandings)

- 100% availability 목표는 현실적이지 않고 속도를 마비시킬 수 있다.
- SLA와 SLO는 같은 말이 아니다.
- CPU나 memory 사용률은 보조 지표이지 사용자 SLI가 아닐 수 있다.
- SLO를 정해도 측정과 alert가 없으면 운영 도구가 되지 않는다.

## TMI

- Multi-window multi-burn-rate alert는 빠른 장애와 느린 소모를 함께 잡는 데 쓰인다.
- Error budget이 남아 있으면 실험과 배포를 더 허용하고, 소진되면 안정화에 집중한다.
- SLO는 팀과 제품이 감당할 수 있는 운영 약속이어야 한다.

## 연습 / 확인 문제 (Exercises)

- 로그인 API의 SLI와 SLO를 정의하라.
- Error budget이 30일에 0.1%일 때 허용 실패 시간을 계산하라.
- CPU alert를 사용자 영향 기반 alert로 바꾸는 방법을 제안하라.

## 이어서 읽기 (Reading Path)

- 이전: [분산 트레이싱](Distributed-Tracing.md)
- 다음: [성능 공학](../Performance/)

## 참조 (References)

- [Engineering/DevOps/Metrics-Alerts.md](Metrics-Alerts.md)
- [Engineering/Performance/Benchmarking-Basics.md](../Performance/Benchmarking-Basics.md)
