# 시스템 설계 사례 (System Design Case Studies)

- Level: Intermediate
- Prerequisites: [Engineering/System-Design/Approach.md](Approach.md), [Engineering/System-Design/Microservices.md](Microservices.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

시스템 설계 사례는 URL 단축기, 피드 시스템, 채팅, 파일 저장소 같은 구체 문제를 요구사항→API→데이터 모델→확장→장애 대응 순서로 풀어 보는 연습이다.

## 직관 (Intuition)

개념을 따로 배우면 각 도구가 좋아 보인다. 사례 풀이는 제한된 시간과 요구사항 안에서 어떤 도구를 왜 선택하는지 설명하는 훈련이다.

## 이론 (Theory)

좋은 설계 답변은 다음 흐름을 가진다.

1. 기능/비기능 요구사항 명확화
2. 규모 추정과 병목 후보
3. API와 데이터 모델
4. 핵심 flow
5. 확장성, 일관성, 장애 대응
6. tradeoff와 대안

URL 단축기는 key generation, redirect latency, analytics, abuse prevention이 핵심이다. 피드 시스템은 fan-out on write/read, ranking, cache invalidation이 핵심이다.

## 구현 (Implementation)

```text
URL Shortener:
Client -> API -> DB(short_code, long_url)
Redirect path -> cache lookup -> DB fallback -> 301/302 response
```

다이어그램은 간단해도 데이터 흐름과 장애 지점을 드러내야 한다.

## 복잡도 (Complexity)

사례의 난이도는 요구사항이 추가될수록 증가한다. 실시간성, global deployment, personalization, strong consistency가 붙으면 설계가 크게 달라진다.

## 응용 (Applications)

- 시스템 설계 면접 준비
- 아키텍처 리뷰 연습
- 팀 설계 문서 초안
- tradeoff 설명 훈련

## 흔한 오해 (Common Misunderstandings)

- 유명한 정답 구조를 외우는 것보다 요구사항에서 끌어내는 과정이 중요하다.
- 처음부터 모든 컴포넌트를 넣으면 과설계가 된다.
- 데이터 모델 없이 캐시와 큐만 말하면 설계가 비어 보인다.
- 장애와 운영 metric을 빼면 실제 시스템 설계가 아니다.

## TMI

- Back-of-the-envelope estimation은 완벽한 숫자보다 병목 감각을 얻는 도구다.
- 설계 사례는 대부분 "읽기 최적화냐 쓰기 최적화냐" 질문으로 좁혀진다.
- Abuse prevention은 URL 단축기처럼 단순해 보이는 시스템에서도 중요하다.

## 연습 / 확인 문제 (Exercises)

- URL 단축기의 API와 DB schema를 설계하라.
- 팔로워 1억 명 계정의 피드 fan-out 전략을 비교하라.
- 채팅 시스템에서 메시지 순서와 재전송 정책을 설계하라.

## 이어서 읽기 (Reading Path)

- 이전: [마이크로서비스](Microservices.md), [메시지 큐](Message-Queues.md)
- 다음: [DevOps](../DevOps/), [Performance](../Performance/)

## 참조 (References)

- [Engineering/System-Design/Approach.md](Approach.md)
- [Reference/Books.md](../../Reference/Books.md)
