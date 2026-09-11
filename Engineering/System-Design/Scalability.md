# 확장성 (Scalability)

- Level: Intermediate
- Prerequisites: [Engineering/System-Design/Approach.md](Approach.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

확장성은 load가 증가할 때 resource를 추가해 목표 성능·신뢰성을 유지하는 능력이다. Scale up은 한 node를 크게, scale out은 node 수를 늘린다.

## 직관 (Intuition)

한 계산대를 빠르게 만드는 것과 계산대를 여러 개 여는 차이다. 여러 계산대는 더 확장되지만 queue 분배, shared inventory, failure 조정이 필요하다.

## 이론 (Theory)

Stateless service는 load balancer 뒤 replica를 늘리기 쉽다. Stateful tier는 partitioning, replication, consistency가 필요하다. Amdahl 법칙은 고정된 작업에서 직렬 비율 $s$가 일정하고 병렬화 오버헤드를 무시할 때 speedup을 제한한다. 웹 서비스의 replica 수에 이 식을 그대로 대입해 처리량을 예측하는 것은 적절하지 않다.

$$S(p)=\frac{1}{s+(1-s)/p}$$

Throughput·latency·queue length·saturation을 함께 보고 load test로 knee point를 찾는다. Autoscaling은 관측 지연과 startup time 때문에 reactive lag가 있다. 예를 들어 [Kubernetes HPA](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/)는 지표를 주기적으로 읽는 제어 루프이며, 새 Pod의 readiness와 누락된 지표도 고려한다. replica 목표가 늘었다고 즉시 요청을 처리할 수 있는 것은 아니다.

## 구현 (Implementation)

### API를 늘린 뒤 DB가 병목이 되는 계산

아래 수치는 실측값이나 특정 제품의 성능이 아닌 가상 워크로드다. CPU 시간이 요청마다 일정하고 요청이 균등 분배되며, DB 쿼리는 같은 비용이라고 가정한다.

- API replica당 2 CPU, 요청당 CPU 사용 시간 5ms, 계획 사용률 상한 70%: replica당 예산은 $2\times0.7/0.005=280$요청/초다.
- DB의 지연 목표를 만족하는 쿼리 예산을 1,800쿼리/초, 요청당 쿼리를 2개로 가정한다: DB 기준 예산은 $1800/2=900$요청/초다.
- 전체 계획 처리량은 두 예산의 최솟값이다. 네트워크·메모리·락 등 다른 병목은 제외했으므로 실제 지연 목표 달성은 부하 시험으로 확인해야 한다.

| API replica 수 | API 예산 (요청/초) | DB 예산 (요청/초) | 전체 예산 (요청/초) | API 비용 지수 (단위/시간) |
|---|---|---|---|---|
| 2 | 560 | 900 | 560 | 4 |
| 4 | 1,120 | 900 | 900 | 8 |
| 6 | 1,680 | 900 | 900 | 12 |

비용은 replica당 시간당 2단위라는 가상 값이며 DB·네트워크 비용은 제외했다. 4개에서 6개로 늘리면 API 비용만 50% 증가하고 전체 예산은 같다. DB 호출을 줄이거나 DB 용량을 바꾸는 것이 다음 조사 대상이다. 요청당 쿼리를 평균 1.5개로 줄일 수 있다면 DB 예산은 1,200요청/초가 되고, replica 4개의 API 예산 1,120요청/초가 다시 한계가 된다. 캐시를 쓴다면 평균 적중률뿐 아니라 원본 조회가 몰리는 시점과 허용 가능한 오래된 데이터도 평가해야 한다.

다음 코드는 표와 장애 여유분을 계산한다. Python 3 표준 라이브러리만 사용한다.

```python
from math import ceil, isclose


def amdahl_speedup(serial_fraction, workers):
    return 1 / (serial_fraction + (1 - serial_fraction) / workers)


def planned_rps(replicas, queries_per_request=2):
    api_rps = replicas * 2 * 0.70 / 0.005
    db_rps = 1800 / queries_per_request
    return min(api_rps, db_rps)


assert isclose(amdahl_speedup(0.1, 16), 6.4)
assert [planned_rps(n) for n in (2, 4, 6)] == [560, 900, 900]
assert planned_rps(4, queries_per_request=1.5) == 1120
target_rps = 800
required_api = ceil(target_rps / 280)
assert required_api == 3
assert planned_rps(required_api) >= target_rps
assert planned_rps(required_api - 1) < target_rps
assert planned_rps(required_api + 1 - 1) >= target_rps
print([int(planned_rps(n)) for n in (2, 4, 6)])
print("normal replicas:", required_api, "one-failure replicas:", required_api + 1)
```

예상 출력:

```text
[560, 900, 900]
normal replicas: 3 one-failure replicas: 4
```

800요청/초를 처리하는 데 API 3개면 계산상 충분하지만, 하나가 멈추면 예산이 560으로 줄어든다. 4개를 확보하면 하나의 장애 후에도 840을 남긴다. 이것은 API replica 하나의 장애에 대한 여유분이며 DB 장애나 한 가용 영역의 여러 replica 동시 장애를 보장하지 않는다.

자동 확장 지연도 따로 계산한다. replica 2개인 상태에서 유입이 800요청/초로 증가하고 추가 replica가 준비되기까지 60초가 걸린다고 가정하자. 처리량이 계속 560이고 거절·재시도가 없다면 그동안 $\left(800-560\right)\times60=14400$요청이 쌓인다. replica 4개가 준비된 후에도 순 배출 속도는 $900-800=100$요청/초여서 큐를 비우는 데 144초가 더 든다. 유한 큐·요청 기한·유입 제한이 없으면 확장이 완료된 뒤에도 대기열이 오래 남을 수 있다. [Google SRE의 Handling Overload](https://sre.google/sre-book/handling-overload/)는 과부하 시 요청 거절과 재시도 제한을 함께 다룬다.

## 복잡도 (Complexity)

Scale out은 capacity를 늘리지만 coordination·network·replication overhead도 증가한다. 변동이 있는 유입과 처리 시간을 가진 큐에서는 utilization이 100%에 가까워질수록 대기 시간이 크게 늘어날 수 있다. 위 용량 계산만으로 p95/p99 지연을 구할 수는 없다. 부하 시험에서는 유입률·성공 처리량·지연 분위수·큐 길이·DB 포화도를 같은 시간축으로 기록하고, 확장 전후 및 replica 장애 시점을 비교한다.

## 응용 (Applications)

- web service replica·autoscaling
- database sharding·read replica
- batch·stream parallelism
- regional deployment

## 흔한 오해 (Common Misunderstandings)

- horizontal scaling이 state를 자동 분산하지 않는다.
- CPU utilization 하나만으로 autoscaling하면 queue·I/O 병목을 놓칠 수 있다.
- replica 증가가 downstream capacity도 늘리지는 않는다.
- scalability와 availability는 동일 개념이 아니다.

## TMI

- Little's Law $L=\lambda W$는 안정된 시스템의 장기 평균 체류 요청 수, 시스템을 통과하는 요청률, 평균 체류 시간을 연결한다. 대기 시간이 포함되면 $L$에도 대기 요청을 포함해야 하며, 증가 중인 대기열에 정상 상태 평균을 그대로 적용하면 안 된다.
- hot partition은 전체 평균 capacity가 남아도 병목을 만든다.
- load shedding은 overload에서 일부 요청을 빠르게 거부해 전체 붕괴를 막는다.

## 연습 / 확인 문제 (Exercises)

- serial fraction 5%의 최대 speedup을 계산하라.
- stateless API와 database 확장 전략을 비교하라.
- overload 보호 정책을 설계하라.
- 위 예제에서 1,000요청/초 목표를 API 증설만으로 달성할 수 있는가? 힌트: DB 예산 900이 먼저 제한한다.
- 자동 확장 중 큐를 최대 1,000요청으로 제한하면 나머지 유입에 어떤 정책이 필요한가? 재시도가 유입률에 미치는 영향까지 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [시스템 설계 접근](Approach.md)
- 다음: [캐싱](Caching.md)
- 관련: [데이터베이스 선택과 샤딩](Database-Design.md)

## 참조 (References)

- [Kubernetes: Horizontal Pod Autoscaling](https://kubernetes.io/docs/concepts/workloads/autoscaling/horizontal-pod-autoscale/) — 이론 절의 주기적 제어 루프, Algorithm details의 replica 계산 및 준비되지 않은 Pod 처리.
- [Google SRE: Handling Overload](https://sre.google/sre-book/handling-overload/) — 구현 절의 과부하 대응, Deciding to Retry의 요청별·클라이언트별 재시도 예산. 이 문서의 가상 용량 수치를 제공하는 출처는 아니다.
- [Systems/Distributed-Systems/Partitioning.md](../../Systems/Distributed-Systems/Partitioning.md)
- [Reference/Papers.md](../../Reference/Papers.md)
- [Reference/Books.md](../../Reference/Books.md)

## 재작성 메모 (Rewrite Notes)

- 재사용할 재료: CPU·DB 예산 비교 표, 용량 계산 코드, replica 하나의 장애 여유분, 확장 지연 중 대기열 증가 계산.
- 보충할 내용: 실제 부하 생성기와 지연 목표, 요청별 DB 비용 분포·락 경합, 캐시 미스 폭증 실험, API/DB/네트워크를 포함한 비용. Amdahl과 Little의 법칙은 원문 및 가정을 더 조사할 필요가 있다.
- 확인 상태: 2026-09-11에 Kubernetes HPA와 Google SRE 공식 문서의 대응 절에 접근. Python 3 계산 예제의 assert와 예상 출력을 로컬에서 확인; 서비스 부하 시험은 수행하지 않음. 사람 검토는 수행하지 않음.
