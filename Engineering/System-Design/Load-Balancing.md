# 로드 밸런싱 (Load Balancing)

- Level: Intermediate
- Prerequisites: [Engineering/System-Design/Scalability.md](Scalability.md), [Systems/Networks/CDN-and-Load-Balancing.md](../../Systems/Networks/CDN-and-Load-Balancing.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

로드 밸런싱은 여러 서버나 인스턴스에 요청을 분산해 throughput, availability, fault tolerance를 높이는 설계 기법이다. L4는 전송 계층 정보, L7은 HTTP 같은 애플리케이션 정보를 기준으로 라우팅한다.

## 직관 (Intuition)

계산대가 여러 개 있을 때 손님을 적절히 나누는 안내원이다. 단순히 줄만 나누는 것이 아니라 고장난 계산대는 피하고, 특정 요청은 맞는 담당자에게 보내야 한다.

## 이론 (Theory)

대표 알고리즘은 round-robin, least connections, weighted routing, consistent hashing이다. Stateless service는 분산이 쉽지만 session state가 서버에 묶이면 sticky session이나 외부 session store가 필요하다.

Health check는 instance를 pool에서 넣고 빼는 기준이다. 너무 민감하면 flapping이 생기고, 너무 느리면 장애 instance로 요청이 계속 간다.

능동 검사는 별도의 probe를 보내고, 수동 검사는 실제 요청의 실패로 건강 상태를 추정한다. [NGINX 문서](https://nginx.org/en/docs/http/load_balancing.html)는 round-robin·가중치와 수동 검사 동작을 설명한다. 건강 상태를 갱신하는 정책과 그 결과를 이용해 다음 서버를 고르는 정책은 구분해서 설계한다.

## 구현 (Implementation)

### 건강 상태를 반영한 round-robin

다음 Python 3 예제는 호출 시점의 건강한 서버 목록을 순회한다. probe, HTTP 전달, 공유 카운터의 동시성 제어는 포함하지 않는다. 건강한 서버가 없으면 명시적으로 실패시키는 정책을 선택했다.

```python
from collections import Counter


def round_robin(servers, health, counter):
    eligible = [server for server in servers if health.get(server, False)]
    if not eligible:
        raise RuntimeError("no healthy upstream")
    return eligible[counter % len(eligible)]


servers = ("api-a", "api-b", "api-c")
health = {server: True for server in servers}
before = [round_robin(servers, health, i) for i in range(6)]
assert Counter(before) == {"api-a": 2, "api-b": 2, "api-c": 2}

health["api-b"] = False
after = [round_robin(servers, health, i) for i in range(6, 12)]
assert Counter(after) == {"api-a": 3, "api-c": 3}
assert "api-b" not in after

for server in servers:
    health[server] = False
try:
    round_robin(servers, health, 12)
except RuntimeError as error:
    assert str(error) == "no healthy upstream"
else:
    raise AssertionError("an empty healthy pool must be rejected")

print(before)
print(after)
```

예상 출력:

```text
['api-a', 'api-b', 'api-c', 'api-a', 'api-b', 'api-c']
['api-a', 'api-c', 'api-a', 'api-c', 'api-a', 'api-c']
```

동일 개수의 요청이 같은 부하를 뜻하지는 않는다. CPU 2배인 `api-a`에 동일 비용 요청을 2배 배정하려면 `2:1:1` 가중치를 검토할 수 있다. 그러나 장기 요청·연결 재사용·hot key가 있으면 연결 수와 처리 시간도 봐야 한다. 위 코드는 목록 갱신 전후의 균등 분배만 확인한다.

### 장애 감지와 재분배의 시간차

가상 상황으로 각 서버의 지속 가능한 예산을 120요청/초, 전체 유입을 300요청/초로 둔다. 처음에는 서버당 100요청/초다. `api-b`가 멈추고 능동 검사가 5초 간격, 연속 실패 2회로 제외한다고 가정한다. 각 검사가 1초 후 timeout되고 probe 간격은 시작 시각 기준이며 추가 전파 지연이 없다면, 장애 직후 다음 검사까지 0~5초, 두 번째 검사 시작까지 추가 5초, 결과까지 1초가 필요하다. 제외까지 약 6~11초이며, 계속 균등 분배하면 대략 600~1,100개의 최초 시도가 죽은 서버에 배정될 수 있다.

제외 이후 살아 있는 두 서버에는 각 150요청/초가 배정되어 각자의 예산 120을 넘는다. 장애 서버를 제외하는 것만으로 복구되지 않으며, 60요청/초를 제한하거나 여유 replica가 필요하다. 재시도까지 무제한 허용하면 실제 시도율은 300보다 커진다. [Google SRE](https://sre.google/sre-book/handling-overload/)가 설명하는 요청별·클라이언트별 예산은 이런 증폭을 제한하는 근거가 된다. 재시도 여부에는 멱등성, 남은 기한, 다른 계층의 재시도 여부도 포함한다.

빈 healthy pool의 정책은 제품마다 다르다. 위 예제는 거절하지만, [AWS ALB](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html)는 모든 활성 가용 영역에서 등록된 대상 전체가 unhealthy이면 해당 대상들로 라우팅하는 fail-open 동작을 문서화한다. 따라서 공통 DB 장애를 모든 서버의 readiness 실패로 연결할 때는 전체 제외 이후 동작까지 확인해야 한다. 이 예제의 검사 주기와 장애 시간 계산은 ALB 기본값이나 보장 시간이 아니다.

배포 실습에서는 새 요청 제외와 기존 요청 종료를 따로 관찰한다. draining 중 처리 중인 요청을 기다리되 종료 기한을 정하고, 복구된 서버를 다시 편입할 때 연속 성공 조건을 두어 반복 편입·제외를 줄인다.

## 복잡도 (Complexity)

위 실습은 매 요청마다 서버 $n$개를 필터링하므로 $O(n)$ 시간과 $O(n)$ 추가 공간을 쓴다. 건강한 목록을 상태 변경 시 별도로 갱신하면 선택 연산 자체는 $O(1)$로 구현할 수 있지만, 동시 접근과 갱신 비용은 남는다. Load balancer 자체가 병목이나 단일 장애점이 될 수 있어 계층화, anycast, active-active 구성 등을 검토한다. Retry가 잘못 설계되면 장애 시 부하를 증폭한다.

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
- 가상 장애 예제에서 replica 하나의 장애 후에도 300요청/초를 받으려면 최초 replica가 최소 몇 개 필요한가? 힌트: $(n-1)\times120\ge300$이므로 4개다.
- 요청별 최대 3회 시도를 허용하는 계층이 3개 중첩되어 모두 실패하면 최하위 호출은 최대 몇 번인가? 힌트: 최초 호출을 포함해 $3^3=27$회다.

## 이어서 읽기 (Reading Path)

- 이전: [확장성](Scalability.md)
- 다음: [캐싱](Caching.md), [CDN](CDN.md)

## 참조 (References)

- [NGINX: Using nginx as HTTP load balancer](https://nginx.org/en/docs/http/load_balancing.html) — 이론 절의 round-robin, Weighted load balancing의 가중치 배분, Health checks의 수동 검사.
- [AWS: Health checks for Application Load Balancer target groups](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-health-checks.html) — 구현 절의 연속 실패·성공 조건 및 전체 unhealthy 대상에 대한 fail-open 예외.
- [Google SRE: Handling Overload](https://sre.google/sre-book/handling-overload/) — 장애 예제의 재시도 증폭 대응; Deciding to Retry의 요청별·클라이언트별 예산 및 여러 계층에서의 재시도 폭증.
- [Systems/Networks/CDN-and-Load-Balancing.md](../../Systems/Networks/CDN-and-Load-Balancing.md)
- [Reference/Books.md](../../Reference/Books.md)

## 재작성 메모 (Rewrite Notes)

- 재사용할 재료: 건강 상태 전후의 round-robin 실행 예제, 6~11초 감지 지연 계산, 서버 제외 뒤의 과부하 계산, 전체 unhealthy 정책 비교.
- 보충할 내용: 실제 프록시에서 probe·timeout·draining을 관찰하는 실험, 긴 요청을 섞은 알고리즘 비교, 공유 DB 장애 시 readiness 기준, 제품 버전별 재시도·연결 처리 설정.
- 확인 상태: 2026-09-11에 위 공식 문서 3개의 대응 절에 접근. Python 3 예제의 assert와 예상 출력을 로컬에서 확인; 실제 네트워크 장애·프록시 설정은 시험하지 않음. 사람 검토는 수행하지 않음.
