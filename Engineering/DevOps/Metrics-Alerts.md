# 메트릭과 알람 (Metrics and Alerts)

- Level: Intermediate
- Prerequisites: [Engineering/DevOps/Kubernetes-Basics.md](Kubernetes-Basics.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

메트릭은 시간에 따른 system 상태를 수치 series로 기록하고, 알람은 사용자 영향이나 임박한 위험을 action 가능한 signal로 전달한다. Counter, gauge, histogram이 기본 metric type이다.

## 직관 (Intuition)

계기판 숫자를 모두 울리는 경보로 만들면 소음만 남는다. 사용자가 실제로 실패하는지, error budget이 빠르게 소진되는지처럼 대응할 수 있는 조건을 경보로 만든다.

## 이론 (Theory)

Counter는 누적 event, gauge는 현재값, histogram은 관측 분포 bucket을 기록한다. Rate는 counter 증가율을 계산한다. Label은 차원을 만들지만 user ID 같은 high-cardinality label은 저장·query 비용을 폭발시킨다.

좋은 alert에는 증상, severity, owner, runbook, dashboard link가 있다. For-duration, grouping, inhibition으로 flapping·중복을 줄이고 warning과 paging을 구분한다.

### Alert 품질

좋은 알람은 사용자가 겪는 문제나 곧 문제로 이어질 포화 상태에 연결된다. CPU 80% 같은 증상 metric만으로는 noise가 많을 수 있다. Error budget burn, latency percentile, saturation, queue age처럼 행동 가능한 신호를 우선한다.

알람에는 owner, severity, runbook, silence policy가 필요하다. 응답하지 않을 알람은 시스템을 더 안전하게 만들지 않는다.

## 구현 (Implementation)

```yaml
groups:
  - name: api
    rules:
      - alert: HighErrorRate
        expr: rate(http_requests_total{status=~"5.."}[5m])
              / rate(http_requests_total[5m]) > 0.05
        for: 10m
        labels: {severity: page}
```

실제 rule은 traffic이 0인 경우, label matching, SLO를 고려해 테스트한다.

## 복잡도 (Complexity)

Metric storage는 series 수와 sample rate에 비례한다. Label cardinality 곱이 series 수를 결정하며 query range와 aggregation이 CPU·memory 비용을 좌우한다.

## 응용 (Applications)

- service health dashboard
- SLO burn-rate alert
- capacity·resource monitoring
- deployment regression detection

## 흔한 오해 (Common Misunderstandings)

- 모든 metric threshold를 page로 만들면 alert fatigue가 생긴다.
- 평균 latency는 tail latency를 숨긴다.
- dashboard가 있다는 것과 alert가 action 가능하다는 것은 다르다.
- high-cardinality label은 나중에 쉽게 고칠 수 있는 사소한 문제가 아니다.

## TMI

- RED는 Rate·Errors·Duration, USE는 Utilization·Saturation·Errors를 본다.
- multi-window burn-rate alert는 빠르고 느린 SLO 소진을 함께 잡는다.
- histogram bucket은 나중에 원하는 quantile 정확도에 영향을 준다.

## 연습 / 확인 문제 (Exercises)

- counter와 gauge를 잘못 선택한 예를 고쳐라.
- user ID label이 series를 얼마나 늘리는지 계산하라.
- 한 alert에 runbook과 owner를 작성하라.

## 이어서 읽기 (Reading Path)

- 이전: [Kubernetes 기초](Kubernetes-Basics.md)
- 다음: [SLI/SLO/SLA](SLI-SLO-SLA.md)

## 참조 (References)

- [Prometheus Alerting Practices](https://prometheus.io/docs/practices/alerting/)
- [Reference/Books.md](../../Reference/Books.md)
