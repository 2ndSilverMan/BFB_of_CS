# 임베디드 실시간 설계 (Embedded Real-Time Design)

- Level: Intermediate
- Prerequisites: [MCU와 인터페이스](Microcontrollers-and-Interfaces.md), [스케줄링](../Systems/Operating-Systems/Scheduling.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (핵심 원리와 제한된 검증 모형)

---

## 개념 (Concept)

실시간 시스템은 계산 결과뿐 아니라 결과가 나온 시각도 요구사항에 포함한다. 빨리 끝나는 평균값과 deadline을 보장하는 것은 다르다. hard/soft real-time의 구분은 deadline 위반이 시스템에 어떤 의미를 갖는지에 관한 것이다. 여기서는 단일 CPU·고정 우선순위·선점 가능한 주기 태스크의 제한된 모형을 다룬다.

## 직관 (Intuition)

낮은 우선순위 태스크가 실행되는 동안 더 급한 작업이 들어오면 처리 시간이 늘어난다. 평균 CPU 사용률에 여유가 있어도 동시에 도착하는 작업 때문에 마감시간을 놓칠 수 있다. 따라서 간섭이 가장 불리한 상황에서 완료까지 걸리는 응답시간을 계산한다.

## 이론 (Theory)

태스크 $i$의 최악 실행시간을 $C_i$, 최소 도착 간격을 $T_i$, 상대 deadline을 $D_i$라 두자. 독립 태스크, 단일 CPU, 고정 우선순위, 완전 선점, 도착 jitter 없음, blocking 없음, $D_i\le T_i$를 가정한다. 스케줄러·인터럽트 오버헤드는 없다고 이상화하거나 실행시간 경계에 이미 반영해야 한다.

우선순위가 높은 집합 $hp(i)$에 대해 다음 고정점 반복을 사용한다.

$$R_i^{(0)}=C_i,\qquad R_i^{(k+1)}=C_i+\sum_{j\in hp(i)}\left\lceil\frac{R_i^{(k)}}{T_j}\right\rceil C_j$$

높은 우선순위 작업이 응답 구간에 몇 번 도착할 수 있는지 올림으로 세는 식이다. $R_i$가 수렴하고 $R_i\le D_i$이면 이 모형에서 deadline을 만족한다. 실제 공유 자원, 캐시 관련 선점 비용, 멀티코어에서는 분석을 확장해야 한다. [York의 응답시간 분석 논문](https://www-users.york.ac.uk/~rd17/papers/ImpCRPD.pdf)은 기본 분석과 캐시 관련 선점 지연의 차이를 다룬다.

## 구현 (Implementation)

가상 태스크 A=(C=1,T=4,D=4), B=(C=2,T=5,D=5)를 두고 A의 우선순위를 높게 한다. B는 $2\to3\to3$으로 수렴한다. 사용률은 $1/4+2/5=0.65$다. B의 C가 4라면 $4\to5\to6$이므로 D=5를 넘는다.

```python
from math import ceil

def response_time(c, deadline, higher):
    # positive integer times; higher is [(C, T), ...]
    if c <= 0 or deadline <= 0 or any(cj <= 0 or tj <= 0 for cj, tj in higher):
        raise ValueError("positive times required")
    r = c
    while r <= deadline:
        nxt = c + sum(ceil(r / tj) * cj for cj, tj in higher)
        if nxt == r:
            return r
        r = nxt
    return None  # misses deadline under the stated model

assert response_time(1, 4, []) == 1
assert response_time(2, 5, [(1, 4)]) == 3
assert response_time(4, 5, [(1, 4)]) is None
assert response_time(2, 1, []) is None
```

엔드투엔드 요구는 CPU 태스크만의 deadline과 별도로 쓴다. 센서 대기 3ms, 계산 응답 상한 3ms, 출력 버스 2ms라는 독립 상한을 가정하면 총 8ms다. 10ms 요구에 2ms 여유가 있지만, 이 합에 빠진 필터 지연·통신 재시도가 있으면 보장이 깨진다.

## 복잡도 (Complexity)

반복마다 높은 우선순위 태스크 수만큼 계산한다. 정수 시간의 단순 구현은 응답 상한까지의 증가 횟수에 의존하므로 입력 비트 길이에 대한 강한 다항 시간 알고리즘으로 해석하지 않는다. WCET가 평균 측정값이면 계산 결과는 보장이 아니다. 측정 최대값도 관측하지 않은 경로를 포함한다는 증거가 필요하다.

## 응용 (Applications)

주기 센서 수집, 통신 제어, 미디어 처리의 deadline 예산에 적용한다. deadline 위반 시 오래된 출력 폐기·안전한 출력 유지·상태 알림을 요구사항으로 정한다. 이 문서의 작은 모형은 안전필수 시스템 인증을 대신하지 않는다.

## 흔한 오해 (Common Misunderstandings)

- CPU 사용률이 100% 미만이면 충분하다: 우선순위·deadline·blocking에 따라 실패한다.
- 실시간이면 가능한 한 빠르게 실행해야 한다: 중요한 것은 요구 시간 안의 예측 가능성이다.
- watchdog이 있으면 deadline을 보장한다: watchdog은 일부 실패를 감지할 뿐 스케줄 가능성을 증명하지 않는다.

## TMI

- priority inversion은 단순히 낮은 우선순위가 실행되는 현상이 아니라 공유 자원 때문에 높은 우선순위가 지연되는 문제다.
- 제어 루프는 최악 지연뿐 아니라 샘플링 jitter에도 민감할 수 있다.

## 연습 / 확인 문제 (Exercises)

1. B의 C를 3으로 바꾸면? **답:** $3\to4\to4$, D=5를 만족한다.
2. 센서 대기가 최대 6ms로 늘면 총 예산은? **답:** 11ms로 10ms 요구를 넘는다. CPU만 최적화하기 전에 지연 구성을 확인한다.
3. 공유 mutex가 생기면 기존 식을 그대로 사용해도 되는가? **답:** 안 된다. blocking과 프로토콜 가정을 분석해야 한다.

## 이어서 읽기 (Reading Path)

- 관련: [동기화](../Systems/Operating-Systems/Synchronization.md), [HDL과 FPGA](HDL-and-FPGA.md).
- 다음: 실제 RTOS의 우선순위·타이머·드라이버를 위 모형에 대응하는 실험.

## 참조 (References)

- [Altmeyer, Davis, Maiza — Improved Cache Related Pre-emption Delay Aware Response Time Analysis](https://www-users.york.ac.uk/~rd17/papers/ImpCRPD.pdf) — 기본 고정 우선순위 응답시간 분석과 캐시 선점 비용 확장. 여기서는 그 확장을 구현하지 않는다.

## 재작성 메모 (Rewrite Notes)

- 재사용할 재료: 명시적 모형 가정, 두 태스크 고정점 계산, 엔드투엔드 지연 예산.
- 보충할 내용: blocking·jitter·EDF·멀티코어 분석, WCET 측정과 정적 분석 비교, 실제 RTOS 실험.
- 확인 상태: 2026-09-18 논문 원문을 열어 기본 응답시간 분석 절의 위치 확인. 논문 전체 증명은 미확인. Python 계산 모델 외 실제 deadline 보장은 검증하지 않았다. Python 3.12/Windows에서 본문의 Python 1개 블록과 assert를 독립 실행해 통과했다. 재실행 검사는 test_new_domain_examples.py에서 관리한다.
