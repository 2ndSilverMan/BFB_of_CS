# 데드락 탐지 (Deadlock Detection)

- Level: Advanced
- Prerequisites: [Systems/Operating-Systems/Deadlock.md](../../Systems/Operating-Systems/Deadlock.md), [Engineering/Debugging/Race-Condition-Debugging.md](Race-Condition-Debugging.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

데드락은 여러 작업이 서로가 가진 자원을 기다리며 영원히 진행하지 못하는 상태다. 탐지는 thread dump, lock graph, timeout, wait-for graph를 통해 수행한다.

## 직관 (Intuition)

두 사람이 각각 열쇠 하나를 들고 상대 열쇠가 있어야 문을 열 수 있다면 둘 다 움직이지 못한다. 프로그램에서도 lock 순서가 꼬이면 같은 일이 생긴다.

## 이론 (Theory)

데드락의 Coffman 조건은 mutual exclusion, hold and wait, no preemption, circular wait이다. 해결은 timeout, lock ordering, try-lock, finer-grained lock, actor/message passing 등으로 접근한다.

### Wait-for graph

데드락은 자원 대기 관계의 cycle로 볼 수 있다. Thread A가 lock X를 잡고 Y를 기다리고, Thread B가 Y를 잡고 X를 기다리면 wait-for graph에 cycle이 생긴다. Thread dump, lock order log, database lock table은 이 graph를 복원하는 증거다.

예방은 모든 코드가 같은 lock acquisition order를 따르게 하거나, timeout과 try-lock으로 무한 대기를 피하고, 긴 I/O 중 lock을 잡지 않는 방식으로 설계한다.

## 구현 (Implementation)

```text
Thread A: holds Lock1, waits Lock2
Thread B: holds Lock2, waits Lock1
```

## 복잡도 (Complexity)

Wait-for graph가 있으면 deadlock cycle 탐지는 노드와 간선 수에 대해 대략 `O(V+E)`로 볼 수 있다. 실제 비용은 thread dump를 얻는 시점, lock 이름의 식별 가능성, 재현 빈도에 더 크게 좌우된다.

## 응용 (Applications)

- 멀티스레드 서버 hang 분석
- DB transaction lock 문제
- 배포 후 요청 정지 원인 추적
- thread dump 분석

## 흔한 오해 (Common Misunderstandings)

- CPU 사용률이 낮아도 데드락으로 서비스가 멈출 수 있다.
- Timeout은 데드락을 숨길 뿐 근본 설계를 고치지 못할 수 있다.
- Lock 순서 규칙이 문서화되지 않으면 재발한다.
- DB deadlock도 애플리케이션 재시도 정책이 필요하다.

## TMI

- Thread dump를 여러 번 떠서 같은 wait 상태가 지속되는지 본다.
- Lock hierarchy는 circular wait를 줄이는 단순한 규칙이다.
- Livelock은 계속 움직이지만 진전이 없는 상태다.

## 연습 / 확인 문제 (Exercises)

- 두 lock으로 데드락이 생기는 순서를 그려라.
- Coffman 조건 중 하나를 깨는 해결책을 제안하라.
- Thread dump에서 waiting thread를 찾는 절차를 작성하라.

## 이어서 읽기 (Reading Path)

- 이전: [운영체제 데드락](../../Systems/Operating-Systems/Deadlock.md)
- 다음: [프로덕션 디버깅](Canary-Feature-Flags.md)

## 참조 (References)

- [Systems/Operating-Systems/Deadlock.md](../../Systems/Operating-Systems/Deadlock.md)
- [Reference/Books.md](../../Reference/Books.md)
