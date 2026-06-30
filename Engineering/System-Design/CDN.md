# CDN (Content Delivery Network)

- Level: Intermediate
- Prerequisites: [Engineering/System-Design/Caching.md](Caching.md), [Systems/Networks/CDN-and-Load-Balancing.md](../../Systems/Networks/CDN-and-Load-Balancing.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

> 📍 **초점**: CDN을 **아키텍처 구성요소**로 보고 배치·오리진 오프로드·동적 콘텐츠 캐싱 전략을 다룬다.

## 개념 (Concept)

CDN은 사용자 가까운 edge location에 정적·동적 콘텐츠를 캐싱해 latency를 줄이고 origin 부하를 낮추는 네트워크 계층이다. 이미지, JS/CSS, 동영상, 다운로드 파일, 일부 API 응답에 쓰인다.

## 직관 (Intuition)

전 세계 사용자가 한 창고로 물건을 받으러 오게 하지 않고, 지역 물류센터에 자주 찾는 물건을 미리 쌓아 둔다. 가까운 곳에서 받으니 빠르고 중앙 창고도 덜 바쁘다.

## 이론 (Theory)

CDN 캐시는 cache key, TTL, invalidation, cache-control header, compression, TLS termination에 영향을 받는다. Hit ratio가 높을수록 origin offload 효과가 커진다.

동적 콘텐츠는 personalization과 freshness 때문에 캐싱이 어렵다. Query string, cookie, authorization header가 cache key에 섞이면 hit ratio가 급격히 낮아질 수 있다.

## 구현 (Implementation)

```http
Cache-Control: public, max-age=3600, stale-while-revalidate=60
```

정적 asset은 content hash를 파일명에 넣어 긴 TTL을 주는 전략이 흔하다.

## 복잡도 (Complexity)

CDN은 latency를 줄이지만 캐시 무효화와 일관성 문제를 만든다. 잘못된 캐시 설정은 오래된 데이터나 개인화 데이터 노출 사고로 이어질 수 있다.

## 응용 (Applications)

- 이미지·영상·정적 파일 전송
- 글로벌 웹사이트 latency 개선
- DDoS 흡수와 edge protection
- API response cache

## 흔한 오해 (Common Misunderstandings)

- CDN이 모든 API를 자동으로 빠르게 만들지는 않는다.
- 캐시 무효화는 어렵고 비용이 있을 수 있다.
- 인증된 사용자 응답을 public cache하면 보안 사고가 난다.
- Hit ratio 없이 CDN 효과를 판단하기 어렵다.

## TMI

- Origin shield는 여러 edge miss를 한 중간 계층으로 모아 origin 부하를 줄인다.
- Edge function은 요청을 가까운 위치에서 변형할 수 있게 해 준다.
- 이미지 resizing을 edge에서 하면 origin과 client 모두 비용을 줄일 수 있다.

## 연습 / 확인 문제 (Exercises)

- 정적 asset에 content hash를 붙이는 이유를 설명하라.
- 캐시 key에 cookie가 들어갈 때 생기는 문제를 말하라.
- CDN 도입 전후 측정할 metric을 설계하라.

## 이어서 읽기 (Reading Path)

- 이전: [캐싱](Caching.md)
- 다음: [로드 밸런싱](Load-Balancing.md), [성능 공학](../Performance/)
- 같은 주제 다른 관점: [CDN과 캐싱 계층 (성능 관점)](../Performance/CDN-Caching.md), [CDN과 로드 밸런싱 (네트워크 관점)](../../Systems/Networks/CDN-and-Load-Balancing.md)

## 참조 (References)

- [Systems/Networks/CDN-and-Load-Balancing.md](../../Systems/Networks/CDN-and-Load-Balancing.md)
- [Reference/Books.md](../../Reference/Books.md)
