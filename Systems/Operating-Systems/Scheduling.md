# CPU 스케줄링 (CPU Scheduling)

- Level: Intermediate
- Prerequisites: [Systems/Operating-Systems/Processes-and-Threads.md](Processes-and-Threads.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

CPU 스케줄링은 **준비 상태(ready)의 여러 프로세스/스레드 중 어느 것을 다음에 CPU에 올릴지** 결정하는 운영체제의 정책이다. CPU는 한 번에 하나의 작업만 실행할 수 있으므로(코어당), 스케줄러는 응답 시간·처리량·공정성 같은 목표 사이에서 균형을 잡으며 실행 순서를 정한다.

## 직관 (Intuition)

은행 창구가 하나뿐인데 손님이 여럿이라면, 누구를 먼저 받을지 규칙이 필요하다. 온 순서대로(FCFS)? 일이 빨리 끝나는 사람 먼저(SJF)? 모두에게 짧게 돌아가며(라운드 로빈)? 각 규칙은 평균 대기 시간과 공정성에서 다른 결과를 낳는다. CPU 스케줄링은 바로 이 "창구 정책"을 정하는 일이다.

## 이론 (Theory)

스케줄링은 실행 중인 작업을 강제로 멈출 수 있는지에 따라 나뉜다.

- **비선점(non-preemptive)**: 작업이 스스로 CPU를 놓을 때까지 기다림(FCFS, 비선점 SJF).
- **선점(preemptive)**: 더 급한 작업이 오면 실행 중인 작업을 멈추고 교체(라운드 로빈, 선점 우선순위).

| 알고리즘 | 기준 | 특징 |
|---|---|---|
| FCFS | 도착 순서 | 단순, 호위 효과(convoy effect) 발생 |
| SJF / SRTF | 실행 시간 최소 | 평균 대기 최소(이론적 최적), 기아 가능 |
| 라운드 로빈 | 시간 할당량(quantum) | 공정, 응답성 좋음, 할당량 크기에 민감 |
| 우선순위 | 우선순위 값 | 중요 작업 우대, 낮은 우선순위 기아 |
| 다단계 피드백 큐 | 동적 우선순위 | 실측 동작 기반, 범용 OS가 사용 |

주요 지표는 대기 시간(waiting), 반환 시간(turnaround), 응답 시간(response), 처리량(throughput)이다. SJF는 평균 대기 시간을 최소화하지만, 미래 실행 시간을 알아야 하므로 실제로는 과거 기록으로 **추정**한다.

## 구현 (Implementation)

선점형 라운드 로빈을 시뮬레이션한다.

```python
from collections import deque


def round_robin(jobs, quantum):
    # jobs: {이름: 남은 실행 시간}
    q = deque(jobs.items())
    time, log = 0, []
    while q:
        name, remaining = q.popleft()
        run = min(quantum, remaining)
        time += run
        remaining -= run
        log.append((name, time))
        if remaining > 0:
            q.append((name, remaining))   # 아직 안 끝났으면 뒤로
    return log


print(round_robin({"A": 5, "B": 3, "C": 1}, quantum=2))
# [('A', 2), ('B', 4), ('C', 5), ('A', 7), ('B', 8), ('A', 9)]
```

## 복잡도 (Complexity)

알고리즘 비용보다 **정책이 만드는 성능 특성**이 핵심이다.

| 항목 | 영향 |
|---|---|
| 할당량(quantum)이 너무 큼 | 라운드 로빈이 FCFS처럼 동작, 응답성 저하 |
| 할당량이 너무 작음 | 컨텍스트 스위치 오버헤드 증가 |
| 우선순위 고정 | 낮은 우선순위 작업 기아(starvation) |
| 에이징(aging) 적용 | 오래 기다린 작업의 우선순위를 올려 기아 완화 |

## 응용 (Applications)

- 범용 OS(Linux CFS, Windows 스케줄러)의 작업 분배
- 실시간 시스템의 마감 시간 보장(EDF, RM 스케줄링)
- 컨테이너·VM의 CPU 시간 분배(cgroup)
- 배치 처리 시스템의 작업 큐 관리

## 흔한 오해 (Common Misunderstandings)

- SJF가 "최적"이라고 항상 쓸 수 있는 것은 아니다. 실행 시간을 미리 알 수 없어 추정에 의존한다.
- 우선순위가 높다고 항상 먼저 끝나는 것은 아니다. 선점·기아·우선순위 역전 같은 현상이 끼어든다.
- 라운드 로빈의 할당량은 작을수록 좋은 게 아니다. 너무 작으면 전환 비용이 실행 시간을 잡아먹는다.
- 처리량과 응답 시간은 같이 좋아지지 않는다. 둘은 흔히 상충하는 목표다.

## TMI

- 우선순위 역전(priority inversion)은 1997년 화성 탐사선 패스파인더를 멈추게 한 유명한 버그다. 낮은 우선순위 작업이 잡은 락을 높은 우선순위 작업이 기다리며 시스템이 리셋을 반복했고, 원인은 우선순위 상속(priority inheritance) 누락이었다.
- 리눅스의 CFS(Completely Fair Scheduler)는 "가상 실행 시간(vruntime)"이 가장 적은 작업을 고르는 방식으로 공정성을 근사한다.
- 비선점 FCFS의 "호위 효과"는, 긴 작업 하나가 앞에 서면 뒤의 짧은 작업들이 줄줄이 기다리는 현상이다(마트에서 카트 가득한 손님 뒤에 선 느낌).

## 연습 / 확인 문제 (Exercises)

- FCFS와 SJF로 같은 작업 집합의 평균 대기 시간을 계산해 비교하라.
- 라운드 로빈에서 할당량을 1, 4, 100으로 바꿔 가며 컨텍스트 스위치 횟수가 어떻게 변하는지 시뮬레이션하라.
- 우선순위 스케줄링에 에이징을 추가해 기아를 막는 의사코드를 작성하라.

## 이어서 읽기 (Reading Path)

- 이전: [프로세스와 스레드](Processes-and-Threads.md)
- 다음: [동기화](Synchronization.md)
- 관련: [메모리 관리](Memory-Management.md)

## 참조 (References)

- [Systems/Operating-Systems/Processes-and-Threads.md](Processes-and-Threads.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
