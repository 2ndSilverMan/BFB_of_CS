# 캐싱 전략 (Caching Strategies)

- Level: Intermediate
- Prerequisites: [Engineering/System-Design/Scalability.md](Scalability.md), [Systems/Distributed-Systems/Replication.md](../../Systems/Distributed-Systems/Replication.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

Cache는 비싼 원본 계산·저장소보다 가까운 곳에 재사용 가능한 결과를 임시 보관해 latency와 backend load를 줄인다. 핵심은 key, placement, eviction, invalidation, consistency 정책이다.

## 직관 (Intuition)

자주 쓰는 책을 창고가 아닌 책상에 둔다. 빠르지만 책상 사본이 원본과 달라질 수 있고 공간이 차면 무엇을 치울지 정해야 한다.

## 이론 (Theory)

Cache-aside는 miss 시 application이 원본을 읽어 cache에 넣는다. Read-through/write-through는 cache layer가 원본 접근을 감싼다. Write-back은 빠르지만 durability·flush 복잡성이 크다.

Hit ratio만 보지 않고 hit/miss latency를 포함한 평균과 tail을 본다. TTL은 stale 기간과 origin load를 교환한다. Cache stampede는 인기 key 만료 시 동시 miss가 backend를 덮치는 현상으로 request coalescing, jitter, stale-while-revalidate로 완화한다.

## 구현 (Implementation)

```python
def get_with_cache(cache, store, key, ttl):
    value = cache.get(key)
    if value is not None:
        return value
    value = store.get(key)
    cache.set(key, value, ttl=ttl)
    return value
```

Negative caching과 `None` value 구분, concurrency control은 실제 구현에서 추가한다.

## 복잡도 (Complexity)

Hash cache lookup은 평균 `O(1)`이지만 network cache는 round trip이 있다. 공간은 entry 수·object size·replication에 비례하며 eviction 유지 비용이 추가된다.

## 응용 (Applications)

- browser·CDN·reverse proxy
- application object·query cache
- DNS와 metadata
- computed feature·model result cache

## 흔한 오해 (Common Misunderstandings)

- cache는 원본 consistency 문제를 없애지 않는다.
- hit ratio가 높아도 큰 object miss가 tail을 지배할 수 있다.
- 모든 응답을 cache하면 privacy·authorization leak이 생길 수 있다.
- cache 장애 시 backend가 전체 traffic을 감당할 수 있어야 한다.

## TMI

- TTL jitter는 많은 key의 동시 만료를 피한다.
- LRU는 recency, LFU는 frequency를 근사한다.
- versioned key는 복잡한 delete 대신 새 namespace로 invalidation할 수 있다.

## 연습 / 확인 문제 (Exercises)

- cache-aside read/write sequence를 그려라.
- stampede를 재현하고 single-flight를 설계하라.
- 사용자별 응답의 안전한 cache key를 정의하라.

## 이어서 읽기 (Reading Path)

- 이전: [확장성](Scalability.md)
- 다음: [CDN](CDN.md)

## 참조 (References)

- [Systems/Distributed-Systems/Replication.md](../../Systems/Distributed-Systems/Replication.md)
- [Reference/Books.md](../../Reference/Books.md)
