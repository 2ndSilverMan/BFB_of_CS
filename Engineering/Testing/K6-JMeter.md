# k6 / JMeter

- Level: Intermediate
- Prerequisites: [Engineering/Testing/Load-Stress-Soak-Testing.md](Load-Stress-Soak-Testing.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

k6와 JMeter는 HTTP/API 부하 테스트 시나리오를 작성하고 실행하는 대표 도구다. 도구보다 중요한 것은 현실적인 workload와 해석 가능한 metric이다.

## 직관 (Intuition)

도구는 가상의 사용자들을 보내는 펌프다. 펌프가 강해도 어떤 행동을 얼마나 자주 하게 할지 잘못 정하면 실제 서비스 부하와 다른 결과가 나온다.

## 이론 (Theory)

부하 테스트 도구는 virtual user, arrival rate, ramp-up, duration, assertion, threshold를 정의한다. 테스트 스크립트는 인증, 데이터 준비, think time, correlation ID, cleanup을 포함할 수 있다.

### 스크립트 모델의 차이

k6는 코드 중심 스크립팅과 CI 친화성이 강하고, JMeter는 GUI 기반 시나리오 구성과 다양한 프로토콜 플러그인이 강점이다. 선택 기준은 팀의 자동화 방식, protocol mix, 결과 분석 도구, 운영 환경과의 통합이다.

부하 도구는 트래픽을 만드는 장치일 뿐이다. 의미 있는 테스트가 되려면 workload model, think time, 데이터 분포, 인증 토큰 처리, ramp-up, 실패 기준, 관측 지표가 함께 정의되어야 한다.

## 구현 (Implementation)

```javascript
// k6 style sketch
export default function () {
  http.get("https://example.com/api/products");
}
```

실제 테스트에는 threshold와 scenario를 명확히 둔다.

## 복잡도 (Complexity)

도구가 만드는 부하가 충분하지 않으면 시스템 한계가 아니라 generator 한계를 측정한다. 분산 부하 생성과 네트워크 위치도 고려해야 한다.

## 응용 (Applications)

- HTTP API 부하 테스트
- CI 성능 smoke test
- capacity planning
- regression latency 감시

## 흔한 오해 (Common Misunderstandings)

- 도구 기본 설정이 현실적 workload라는 뜻은 아니다.
- 성공률이 높아도 p95/p99가 나쁘면 사용자 경험이 나쁠 수 있다.
- 로컬 노트북에서 production 규모 부하를 만들기는 어렵다.
- 테스트 데이터가 고정되면 캐시 효과만 측정할 수 있다.

## TMI

- k6는 스크립트를 코드처럼 버전 관리하기 쉽다.
- JMeter는 오래된 생태계와 GUI 기반 시나리오 작성으로 널리 쓰였다.
- Threshold를 CI gate로 쓰면 성능 회귀를 빨리 잡을 수 있다.

## 연습 / 확인 문제 (Exercises)

- 로그인 후 상품 조회 시나리오를 작성하라.
- p95 latency threshold를 정의하라.
- 부하 생성기 병목을 확인할 metric을 나열하라.

## 이어서 읽기 (Reading Path)

- 이전: [부하/스트레스/소크 테스트](Load-Stress-Soak-Testing.md)
- 다음: [성능 공학](../Performance/)

## 참조 (References)

- [Engineering/Performance/Benchmarking-Basics.md](../Performance/Benchmarking-Basics.md)
- [Reference/Books.md](../../Reference/Books.md)
