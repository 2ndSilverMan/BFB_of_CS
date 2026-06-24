# 로드 밸런싱 (Load Balancing)

- Level: Intermediate
- Prerequisites: [Engineering/System-Design/Scalability.md](Scalability.md), [Systems/Networks/CDN-and-Load-Balancing.md](../../Systems/Networks/CDN-and-Load-Balancing.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

로드 밸런싱은 여러 서버나 인스턴스에 요청을 분산해 throughput, availability, fault tolerance를 높이는 설계 기법이다. L4는 전송 계층 정보, L7은 HTTP 같은 애플리케이션 정보를 기준으로 라우팅한다.

## 직관 (Intuition)

계산대가 여러 개 있을 때 손님을 적절히 나누는 안내원이다. 단순히 줄만 나누는 것이 아니라 고장난 계산대는 피하고, 특정 요청은 맞는 담당자에게 보내야 한다.

## 이론 (Theory)

대표 알고리즘은 round-robin, least connections, weighted routing, consistent hashing이다. Stateless service는 분산이 쉽지만 session state가 서버에 묶이면 sticky session이나 외부 session store가 필요하다.

Health check는 instance를 pool에서 넣고 빼는 기준이다. 너무 민감하면 flapping이 생기고, 너무 느리면 장애 instance로 요청이 계속 간다.

## 구현 (Implementation)

```python
def round_robin(servers, counter):
    return servers[counter % len(servers)]
```

실제 시스템은 health, weight, region, overload, retry budget을 함께 고려한다.

## 복잡도 (Complexity)

Load balancer 자체가 병목이나 단일 장애점이 될 수 있다. 계층화, anycast, active-active 구성으로 확장한다. Retry가 잘못 설계되면 장애 시 부하를 증폭한다.

## 응용 (Applications)

- 웹 API replica 분산
- region별 트래픽 라우팅
- canary·blue-green 배포
- TCP/HTTP ingress

## 흔한 오해 (Common Misunderstandings)

- 로드 밸런서가 downstream DB 병목을 해결하지는 않는다.
- Sticky session은 편하지만 확장성과 장애 복구를 어렵게 한다.
- Health check endpoint가 살아 있어도 실제 기능이 정상이라는 보장은 없다.
- Retry는 반드시 timeout과 budget을 함께 둬야 한다.

## TMI

- Consistent hashing은 cache node 추가·제거 시 key 이동을 줄인다.
- L7 load balancer는 path, header, cookie 기반 routing이 가능하다.
- Connection draining은 배포 시 기존 요청을 안전하게 마무리하게 한다.

## 연습 / 확인 문제 (Exercises)

- Stateless API의 load balancing 구성을 그려라.
- Sticky session이 필요한 상황과 피해야 할 상황을 비교하라.
- Health check와 readiness check를 설계하라.

## 이어서 읽기 (Reading Path)

- 이전: [확장성](Scalability.md)
- 다음: [캐싱](Caching.md), [CDN](CDN.md)

## 참조 (References)

- [Systems/Networks/CDN-and-Load-Balancing.md](../../Systems/Networks/CDN-and-Load-Balancing.md)
- [Reference/Books.md](../../Reference/Books.md)
