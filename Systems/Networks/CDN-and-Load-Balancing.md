# CDN과 로드 밸런싱 (CDN and Load Balancing)

- Level: Intermediate
- Prerequisites: [Systems/Networks/DNS.md](DNS.md), [Systems/Networks/HTTP.md](HTTP.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

> 📍 **초점**: **네트워크 관점**에서 CDN과 로드 밸런싱(L4/L7·분배 알고리즘·헬스 체크)을 함께 다룬다.

## 개념 (Concept)

CDN(콘텐츠 전송 네트워크)은 콘텐츠를 사용자 가까운 엣지 서버에 복제해 지연과 원본 부하를 줄인다. 로드 밸런싱은 여러 서버에 요청을 분산해 처리량과 가용성을 높인다.

## 직관 (Intuition)

한 서버가 전 세계 요청을 다 받으면 멀리 있는 사용자는 느리고 서버는 과부하다. CDN은 "사본을 곳곳에 미리 둬서" 가까운 곳에서 받게 한다. 로드 밸런서는 "여러 일꾼에게 일을 고르게 나눠" 한 명이 쓰러져도 서비스가 유지되게 한다.

## 이론 (Theory)

**로드 밸런싱 계층**:
- **L4(전송 계층)**: IP/포트 기반, 빠름.
- **L7(응용 계층)**: HTTP 경로·헤더 기반 라우팅, 유연.

**분배 알고리즘**: 라운드 로빈, 최소 연결, 가중치, 해시(세션 고정/sticky). **헬스 체크**로 죽은 서버를 빼고, 장애 조치(failover)로 가용성을 지킨다.

**CDN**: 정적·동적 콘텐츠를 엣지에 캐싱. 사용자를 가까운 엣지로 보내는 데 **애니캐스트**나 **DNS 기반 지리 라우팅**을 쓴다. 캐시 무효화(purge)와 TTL로 신선도를 관리한다.

## 구현 (Implementation)

```python
# 가중 라운드 로빈 로드 밸런서(개념)
class WeightedRR:
    def __init__(self, servers):       # servers: [(name, weight)]
        self.pool = []
        for name, w in servers:
            self.pool += [name] * w     # 가중치만큼 복제
        self.i = -1
    def next(self):
        self.i = (self.i + 1) % len(self.pool)
        return self.pool[self.i]        # 순환 분배
```

## 복잡도 (Complexity)

분배 결정은 보통 `O(1)`~`O(log n)`이다. 핵심 이득은 알고리즘이 아니라 분산: CDN은 지연(RTT)을 수백 ms에서 수십 ms로, 로드 밸런서는 단일 서버 한계를 수평 확장으로 넘는다. 일관성 해시는 서버 추가/제거 시 재배치를 최소화한다.

## 응용 (Applications)

- 정적 자산(이미지·JS·동영상) 가속
- 글로벌 웹 서비스의 지연 최소화
- 트래픽 급증·DDoS 흡수
- 무중단 배포(서버를 풀에서 빼고 교체)

## 흔한 오해 (Common Misunderstandings)

- CDN은 정적 콘텐츠만이 아니라 동적 콘텐츠·API도 가속할 수 있다(엣지 컴퓨팅).
- sticky 세션은 편하지만 부하 불균형·확장성 저하를 부른다(가능하면 무상태 설계).
- 로드 밸런서 자체가 단일 장애점이 될 수 있다(이중화 필요).
- 캐시 무효화는 "컴퓨터 과학의 어려운 문제"로, 신선도와 효율의 균형이 까다롭다.

## TMI

- "캐시 무효화와 이름 짓기가 컴퓨터 과학에서 가장 어려운 두 가지"라는 농담이 유명하다.
- 일관성 해시(consistent hashing)는 CDN·분산 캐시·분산 DB의 공통 핵심 기법이다.
- 애니캐스트는 같은 IP를 여러 위치에서 광고해 라우팅이 가장 가까운 곳으로 보내게 한다.

## 연습 / 확인 문제 (Exercises)

- 라운드 로빈과 최소 연결 분배의 차이를 상황별로 비교하라.
- 일관성 해시가 서버 추가 시 재배치를 줄이는 원리를 설명하라.
- L4와 L7 로드 밸런싱의 장단점을 들어라.

## 이어서 읽기 (Reading Path)

- 이전: [네트워크 보안 기초](Network-Security-Basics.md)
- 다음: [Engineering/System-Design/Scalability.md](../../Engineering/System-Design/Scalability.md), [Engineering/System-Design/Caching.md](../../Engineering/System-Design/Caching.md)
- 같은 주제 다른 관점: [CDN과 캐싱 계층 (성능 관점)](../../Engineering/Performance/CDN-Caching.md), [CDN (시스템 설계 관점)](../../Engineering/System-Design/CDN.md)

## 참조 (References)

- [Systems/Networks/DNS.md](DNS.md)
- [Engineering/System-Design/Scalability.md](../../Engineering/System-Design/Scalability.md)
- [Reference/Books.md](../../Reference/Books.md)
