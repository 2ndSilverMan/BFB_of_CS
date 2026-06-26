# CDN과 캐싱 계층 (CDN Caching)

- Level: Intermediate
- Prerequisites: [Systems/Networks/CDN-and-Load-Balancing.md](../../Systems/Networks/CDN-and-Load-Balancing.md), [Engineering/System-Design/Caching.md](../System-Design/Caching.md)
- Status: Draft
- Reviewed-by: -

---

> 📍 **초점**: HTTP 캐시 헤더·TTL·무효화 등 **엣지 캐시의 동작 메커니즘**에 집중한다.

## 개념 (Concept)

CDN 캐싱은 사용자와 가까운 edge server에 static 또는 cache 가능한 response를 저장해 origin 부하와 latency를 줄이는 설계다.

## 직관 (Intuition)

모든 사용자가 본사 창고까지 가지 않고 동네 창고에서 물건을 받는다. 대신 어떤 물건을 언제 새로 채울지 규칙이 필요하다.

## 이론 (Theory)

Cache-Control, ETag, Last-Modified, Vary, surrogate key가 cache behavior를 결정한다. TTL이 길면 hit rate는 높지만 stale risk가 커지고, TTL이 짧으면 origin 부하가 늘어난다. Purge, versioned URL, stale-while-revalidate, request collapsing으로 freshness와 availability를 조정한다.

## 구현 (Implementation)

```http
Cache-Control: public, max-age=31536000, immutable
```

위 설정은 content hash가 포함된 정적 asset에 적합하다. 사용자별 response에는 `private` 또는 `no-store`가 필요할 수 있다.

## 복잡도 (Complexity)

Hit request는 edge에서 끝나 origin 비용이 줄지만, miss와 purge 전파는 network·metadata 비용이 든다. Key cardinality가 높으면 hit rate가 낮아진다.

## 응용 (Applications)

- static asset delivery
- image·video distribution
- API edge cache
- DDoS 흡수와 origin 보호

## 흔한 오해 (Common Misunderstandings)

- CDN은 모든 동적 API를 자동으로 빠르게 만들지 않는다.
- `Vary: Authorization` 같은 header는 cache key를 폭발시킬 수 있다.
- 개인정보 response를 public cache에 저장하면 보안 사고가 된다.
- Purge는 즉시 전 세계에 반영된다고 가정하면 위험하다.

## TMI

- Versioned filename은 purge보다 단순하고 안전한 cache busting이다.
- Negative caching은 404 같은 결과도 짧게 저장해 origin을 보호한다.
- Edge computing은 cache 근처에서 간단한 routing·rewrite를 수행한다.

## 연습 / 확인 문제 (Exercises)

- 정적 asset에 content hash와 immutable cache header를 적용하라.
- API response의 cache key에 포함할 요소를 설계하라.
- stale-while-revalidate가 사용자 경험에 주는 이점을 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [네트워크 성능](Network-Performance.md)
- 다음: [JIT 최적화](JIT-Optimization.md)
- 같은 주제 다른 관점: [CDN (시스템 설계 관점)](../System-Design/CDN.md), [CDN과 로드 밸런싱 (네트워크 관점)](../../Systems/Networks/CDN-and-Load-Balancing.md), [메모이제이션과 캐싱 (성능 관점)](Memoization-Caching.md), [캐싱 전략 (시스템 설계 관점)](../System-Design/Caching.md)

## 참조 (References)

- [Systems/Networks/CDN-and-Load-Balancing.md](../../Systems/Networks/CDN-and-Load-Balancing.md)
- [Engineering/System-Design/Caching.md](../System-Design/Caching.md)

