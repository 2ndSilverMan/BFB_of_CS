# 시스템 모델과 장애 유형 (System Models & Failure Types)

- Level: Intermediate
- Prerequisites: [Systems/Networks/Network-Models.md](../Networks/Network-Models.md), [Systems/Operating-Systems/Processes-and-Threads.md](../Operating-Systems/Processes-and-Threads.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

분산 시스템의 **시스템 모델**은 "노드와 네트워크가 어떻게 동작하고 어떻게 고장 나는지"에 대한 가정의 집합이다. 알고리즘의 정당성은 항상 이 가정 위에서만 성립하므로, 어떤 모델을 전제하는지가 분산 알고리즘 설계의 출발점이다.

## 직관 (Intuition)

한 컴퓨터 안에서는 "메모리는 항상 응답하고, 시계는 같고, 고장 나면 다 같이 멈춘다"고 믿어도 된다. 하지만 여러 컴퓨터가 네트워크로 연결되면 이 가정이 모두 깨진다 — 메시지는 늦거나 사라지고, 노드는 일부만 죽고, 시계는 제각각이다. 시스템 모델은 "무엇을 믿고 무엇을 의심할지"를 명문화해, 현실의 불확실성을 다룰 수 있는 형태로 좁힌다.

## 이론 (Theory)

**타이밍 모델** — 메시지 지연과 처리 시간에 대한 가정이다.

| 모델 | 가정 |
|---|---|
| 동기(synchronous) | 메시지 지연·처리 시간에 알려진 상한이 있음 |
| 비동기(asynchronous) | 지연에 상한이 없음(언제 올지 보장 못 함) |
| 부분 동기(partially synchronous) | 평소엔 동기지만 가끔 상한이 깨짐 — 현실에 가장 가까움 |

**장애 모델** — 노드가 어떻게 고장 나는지에 대한 가정이다.

| 장애 유형 | 설명 |
|---|---|
| 중단(crash-stop) | 멈추면 영영 멈춤 |
| 중단-복구(crash-recovery) | 멈췄다 다시 살아남(상태 복구 필요) |
| 생략(omission) | 일부 메시지를 빠뜨림 |
| 비잔틴(Byzantine) | 임의로(악의적·버그 포함) 잘못된 동작 |

핵심 난제는 비동기 네트워크에서 "느린 노드"와 "죽은 노드"를 **구별할 수 없다**는 점이다. 이 근본적 한계가 [FLP 불가능성 정리](Consensus.md)("비동기 + 한 노드 장애 가능 시 결정적 합의는 불가능")로 이어진다. 그래서 실제 시스템은 타임아웃으로 장애를 **추정**하는 장애 감지기(failure detector)를 쓴다.

## 구현 (Implementation)

하트비트 기반 장애 감지의 단순 모델이다.

```python
import time

class FailureDetector:
    def __init__(self, timeout=3.0):
        self.last_seen = {}
        self.timeout = timeout

    def heartbeat(self, node):
        self.last_seen[node] = time.monotonic()

    def suspected(self, node):
        # 타임아웃 내 하트비트가 없으면 "장애 의심"(확정 아님)
        return time.monotonic() - self.last_seen.get(node, 0) > self.timeout
```

`suspected`는 "확정된 죽음"이 아니라 **의심**이다 — 느린 노드를 죽은 것으로 오판할 수 있다.

## 복잡도 (Complexity)

알고리즘 비용보다 **가정의 강도와 보장 가능성**이 핵심이다.

| 가정이 강할수록 | 결과 |
|---|---|
| 동기 모델 가정 | 알고리즘이 단순해짐, 그러나 현실에서 깨지면 오동작 |
| 비동기 모델 가정 | 견고하지만 합의 등 일부 문제는 결정적 해법 불가 |
| 비잔틴 내성 요구 | 더 많은 노드(3f+1)와 통신 비용 필요 |

## 응용 (Applications)

- 합의·복제 알고리즘이 전제하는 모델 명시
- 장애 감지기·타임아웃 설계
- 비잔틴 내성: 블록체인, 항공·우주 같은 고신뢰 시스템
- SLA·가용성 목표 설정의 근거

## 흔한 오해 (Common Misunderstandings)

- "노드가 응답이 없다 = 죽었다"가 아니다. 비동기 네트워크에서는 느린 것과 죽은 것을 확실히 구분할 수 없다.
- 동기 모델이 "빠르다"는 뜻이 아니다. 지연에 **상한이 있다**는 가정일 뿐이다.
- 비잔틴 장애는 악의적 공격만이 아니다. 메모리 손상·소프트웨어 버그로 인한 임의 동작도 포함한다.
- 모델 가정을 어기면 알고리즘 보장도 깨진다. "이론상 안전"은 가정이 성립할 때만 유효하다.

## TMI

- "비잔틴 장군 문제"라는 이름은 램포트가 1982년 논문에서, 일부 장군이 배신할 수 있는 상황에 빗대 붙였다. 임의 장애의 대명사가 됐다.
- 분산 컴퓨팅의 "여덟 가지 오류(fallacies of distributed computing)" 중 첫 번째가 "네트워크는 신뢰할 수 있다"이다. 거의 모든 분산 버그가 이 잘못된 가정에서 나온다.
- 부분 동기 모델은 1988년 Dwork·Lynch·Stockmeyer가 도입했다. "대부분의 시간은 정상이지만 가끔 느려진다"는 현실을 포착해, 실용적 합의 알고리즘(Raft, Paxos)의 이론적 토대가 됐다.

## 연습 / 확인 문제 (Exercises)

- 동기·비동기·부분 동기 모델 각각에서 장애 감지가 얼마나 신뢰할 수 있는지 비교하라.
- 하트비트 타임아웃을 너무 짧게/길게 잡았을 때의 트레이드오프를 설명하라.
- 비잔틴 장애를 견디려면 왜 더 많은 노드가 필요한지 직관적으로 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [네트워크 모델](../Networks/Network-Models.md)
- 다음: [CAP 정리](CAP-Theorem.md), [분산 합의](Consensus.md)
- 관련: [프로세스와 스레드](../Operating-Systems/Processes-and-Threads.md)

## 참조 (References)

- [Systems/Networks/Network-Models.md](../Networks/Network-Models.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Papers.md](../../Reference/Papers.md)
