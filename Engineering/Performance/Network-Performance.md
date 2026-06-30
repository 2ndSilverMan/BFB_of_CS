# 네트워크 성능 (Network Performance)

- Level: Intermediate
- Prerequisites: [Systems/Networks/TCP-UDP.md](../../Systems/Networks/TCP-UDP.md), [Systems/Networks/HTTP.md](../../Systems/Networks/HTTP.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

네트워크 성능 최적화는 latency, throughput, connection reuse, serialization, packet loss, retry를 조정해 원격 통신 비용을 줄이는 작업이다.

## 직관 (Intuition)

원격 호출은 함수 호출처럼 보여도 거리와 대기열이 있다. 요청 수를 줄이고, 연결을 재사용하고, 실패를 제어해야 한다.

## 이론 (Theory)

End-to-end latency는 DNS, TCP/TLS handshake, request queueing, server processing, response transfer로 나뉜다. Keep-alive와 connection pool은 handshake를 줄이고, HTTP/2 multiplexing은 connection당 concurrency를 늘린다. Payload 크기, compression, serialization format, timeout, retry budget이 tail latency에 영향을 준다.

### Latency budget

네트워크 성능은 RTT, DNS, TLS handshake, payload size, serialization, server processing, queueing이 합쳐진 결과다. End-to-end latency budget을 나눠 각 구간의 p95/p99를 추적해야 한다.

Connection reuse, HTTP/2 multiplexing, compression, regional routing은 도움이 되지만 head-of-line blocking, retry storm, payload bloat 같은 부작용을 함께 본다.

## 구현 (Implementation)

```text
good client defaults:
- connect timeout
- request timeout
- bounded connection pool
- exponential backoff with jitter
- idempotent retry only
```

## 복잡도 (Complexity)

요청 수가 많으면 RTT 비용이 누적된다. Batch는 RTT를 줄이지만 payload와 tail latency를 키울 수 있어 균형이 필요하다.

## 응용 (Applications)

- API gateway tuning
- service-to-service RPC
- mobile network optimization
- bulk data transfer

## 흔한 오해 (Common Misunderstandings)

- 대역폭이 충분해도 RTT가 크면 작은 요청이 느리다.
- 무제한 retry는 장애를 증폭한다.
- Compression은 CPU 비용과 latency를 함께 본다.
- Connection pool을 너무 크게 잡으면 서버와 NAT 자원을 고갈시킬 수 있다.

## TMI

- Tail latency는 fan-out 구조에서 쉽게 증폭된다.
- Jitter 없는 retry는 여러 client가 동시에 재시도하는 thundering herd를 만든다.
- Binary protocol은 크기를 줄일 수 있지만 디버깅과 호환성 비용이 있다.

## 연습 / 확인 문제 (Exercises)

- keep-alive 유무에 따른 요청 latency를 비교하라.
- timeout 없이 느린 downstream을 호출하는 문제를 재현하라.
- batch size별 latency와 throughput trade-off를 측정하라.

## 이어서 읽기 (Reading Path)

- 이전: [데이터베이스 쿼리 최적화](Database-Query-Optimization.md)
- 다음: [CDN 캐싱](CDN-Caching.md)

## 참조 (References)

- [Systems/Networks/TCP-UDP.md](../../Systems/Networks/TCP-UDP.md)
- [Systems/Networks/HTTP.md](../../Systems/Networks/HTTP.md)
