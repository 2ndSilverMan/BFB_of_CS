# 테스트 피라미드 (Testing Pyramid)

- Level: Intermediate
- Prerequisites: [Programming/Functions-and-Recursion.md](../../Programming/Functions-and-Recursion.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

테스트 피라미드는 빠르고 고립된 단위 테스트를 넓은 기반으로, 경계 통합 테스트를 그 위에, 느리고 취약한 E2E 테스트를 적게 두는 test portfolio 원칙이다.

## 직관 (Intuition)

모든 결함을 browser E2E로 확인하면 느리고 실패 원인이 불분명하다. 작은 규칙은 작은 test, component 연결은 integration, 핵심 user journey는 E2E로 가장 가까운 층에서 검증한다.

## 이론 (Theory)

| 층 | 범위 | 장점 | 한계 |
|---|---|---|---|
| Unit | 함수·class | 빠름, 원인 명확 | 경계 오류 놓침 |
| Integration | DB·queue·service 경계 | 실제 contract 검증 | setup·속도 비용 |
| E2E | 전체 user flow | 높은 현실성 | 느림, flaky, 진단 어려움 |

비율은 제품과 architecture에 따라 달라진다. 핵심은 feedback speed, confidence, maintenance cost의 균형이며 모든 test가 독립적이고 deterministic하도록 노력한다.

### 포트폴리오 설계 기준

테스트 피라미드는 단순 비율표가 아니라 결함을 가장 싼 층에서 잡기 위한 투자 원칙이다. 작은 domain rule은 unit에서, 외부 경계 contract는 integration에서, 사용자 신뢰에 직결되는 핵심 journey는 E2E에서 검증한다. 같은 버그를 재현할 수 있다면 더 낮은 층의 deterministic regression test로 내리는 것이 장기 유지비를 줄인다.

CI에서는 층별 실행 주기를 다르게 둘 수 있다. Unit은 모든 push, integration은 PR gate, E2E와 장기 성능 테스트는 merge 전 또는 nightly로 운영하되, release-blocking 기준과 flaky 처리 정책을 명확히 둔다.

## 구현 (Implementation)

```python
def total(prices):
    return sum(prices)


def test_total_empty_cart():
    assert total([]) == 0


def test_total_multiple_items():
    assert total([100, 250]) == 350
```

## 복잡도 (Complexity)

Suite 시간은 test별 setup과 실행 비용의 합이며 병렬화는 shared resource 격리에 제한된다. E2E 수가 늘면 조합·환경 비용이 빠르게 커진다.

## 응용 (Applications)

- CI feedback 설계
- test 투자 우선순위
- regression·release gate
- service architecture 검증

## 흔한 오해 (Common Misunderstandings)

- 정해진 비율을 맞추는 것이 목적은 아니다.
- unit test만 많아도 integration contract는 보장되지 않는다.
- E2E를 0개로 만드는 원칙도 아니다.
- flaky test를 retry로만 숨기면 신뢰가 무너진다.

## TMI

- test trophy는 integration test에 더 무게를 두는 대안적 비유다.
- 가장 싼 층에서 bug를 재현한 regression test를 두면 suite가 안정적이다.
- hermetic test는 외부 시간·network·state 의존을 통제한다.

## 연습 / 확인 문제 (Exercises)

- 결제 service의 test portfolio를 층별로 설계하라.
- E2E test 하나를 unit·integration으로 분해하라.
- flaky 원인을 환경·시간·순서로 분류하라.

## 이어서 읽기 (Reading Path)

- 이전: 없음
- 다음: [단위 테스트 원칙](Unit-Test-Principles.md), [통합 테스트 전략](Integration-Test-Strategy.md)

## 참조 (References)

- [Engineering/Software-Design/README.md](../Software-Design/README.md)
- [Reference/Books.md](../../Reference/Books.md)
