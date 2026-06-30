# 메모이제이션과 캐싱 (Memoization and Caching)

- Level: Intermediate
- Prerequisites: [Data-Structures/Hash-Table.md](../../Data-Structures/Hash-Table.md), [Engineering/System-Design/Caching.md](../System-Design/Caching.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

> 📍 **초점**: 함수 메모이제이션 등 **코드·계산 수준의 캐싱**에 집중한다.

## 개념 (Concept)

메모이제이션은 함수 입력과 결과를 저장해 같은 계산을 재사용하는 기법이고, 캐싱은 비싼 데이터 접근·계산 결과를 가까운 계층에 보관하는 전략이다.

## 직관 (Intuition)

같은 질문에 매번 처음부터 답하지 않는다. 대신 답이 언제 틀릴 수 있는지와 얼마나 오래 보관할지를 정해야 한다.

## 이론 (Theory)

Cache key는 identity와 dependency를 정확히 표현해야 한다. Eviction은 LRU, LFU, TTL, size cap 등으로 관리한다. Cache hit가 늘면 latency는 줄지만 stale data, memory pressure, stampede, invalidation 복잡도가 생긴다. Memoization은 pure function에 가장 안전하다.

### 캐시의 정확성 조건

캐시는 빠른 정답을 위한 도구이지 오래된 답을 허용하는 변명이 아니다. Key 설계, TTL, invalidation, consistency level, negative caching, stampede 방지가 함께 필요하다. 캐시 키에는 사용자, 권한, locale, feature flag처럼 결과에 영향을 주는 문맥을 포함한다.

Hit rate만 보면 안 된다. 캐시 miss penalty, stale data risk, memory pressure, eviction churn, warmup behavior를 함께 봐야 한다.

## 구현 (Implementation)

```python
from functools import lru_cache

@lru_cache(maxsize=2048)
def fib(n: int) -> int:
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)
```

외부 상태에 의존하는 함수는 key에 version·tenant·permission 같은 조건을 포함해야 한다.

## 복잡도 (Complexity)

반복 subproblem이 많은 경우 exponential 계산을 polynomial로 줄일 수 있다. 대신 storage는 unique key 수에 비례한다.

## 응용 (Applications)

- dynamic programming
- API response cache
- database query cache
- feature computation reuse

## 흔한 오해 (Common Misunderstandings)

- 캐시는 correctness 문제를 숨길 수 있다.
- hit rate만 높아도 tail latency가 나쁠 수 있다.
- 무제한 memoization은 memory leak처럼 동작한다.
- invalidation 전략 없는 캐시는 빚이 된다.

## TMI

- Cache stampede는 인기 key가 동시에 만료될 때 backend를 폭주시킨다.
- Negative cache는 실패 결과도 잠깐 저장해 반복 실패를 줄인다.
- Distributed cache는 network hop과 serialization 비용을 포함해 평가해야 한다.

## 연습 / 확인 문제 (Exercises)

- LRU cache의 max size에 따른 hit rate와 memory 사용량을 측정하라.
- TTL cache에서 stale data 허용 범위를 정의하라.
- cache stampede를 singleflight나 jitter로 완화하라.

## 이어서 읽기 (Reading Path)

- 이전: [실전 복잡도](Practical-Complexity.md)
- 다음: [지연 계산](Lazy-Evaluation.md)
- 같은 주제 다른 관점: [CDN과 캐싱 계층 (성능 관점)](CDN-Caching.md), [캐싱 전략 (시스템 설계 관점)](../System-Design/Caching.md)

## 참조 (References)

- [Engineering/System-Design/Caching.md](../System-Design/Caching.md)
- [Data-Structures/Hash-Table.md](../../Data-Structures/Hash-Table.md)
