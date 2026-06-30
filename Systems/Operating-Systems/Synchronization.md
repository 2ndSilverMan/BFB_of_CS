# 동기화 (Synchronization)

- Level: Intermediate
- Prerequisites: [Systems/Operating-Systems/Processes-and-Threads.md](Processes-and-Threads.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

동기화는 여러 스레드/프로세스가 **공유 자원에 동시에 접근할 때 생기는 충돌을 막아** 결과의 일관성을 보장하는 기법이다. 핵심은 **임계 구역(critical section)**, 즉 한 번에 한 실행 흐름만 들어가야 하는 코드 영역을 보호하는 것이다.

## 직관 (Intuition)

화장실 한 칸을 여러 사람이 쓴다면 문에 잠금이 필요하다. 잠금이 없으면 두 사람이 동시에 들어가는(경쟁 조건) 사고가 난다. 뮤텍스는 이 "문 잠금"이고, 세마포어는 "빈 칸 수를 세는 표지판"이다. 동기화는 공유 자원 앞에 이런 교통 정리를 두는 일이다.

## 이론 (Theory)

**경쟁 조건(race condition)** 은 결과가 실행 순서(스케줄링)에 따라 달라지는 버그다. `counter += 1`조차 읽기→증가→쓰기 세 단계라, 중간에 끼어들면 갱신이 사라진다. 이를 막으려면 그 연산이 **원자적(atomic)** 이거나 임계 구역으로 보호돼야 한다.

올바른 임계 구역 해법은 세 조건을 만족해야 한다.

| 조건 | 의미 |
|---|---|
| 상호 배제(mutual exclusion) | 한 번에 하나만 임계 구역에 진입 |
| 진행(progress) | 비어 있으면 들어가려는 쪽이 무한정 막히지 않음 |
| 한정 대기(bounded waiting) | 진입을 기다리는 횟수에 상한이 있음 |

대표 도구는 다음과 같다.

- **뮤텍스(mutex)**: 잠금/해제 한 쌍. 소유자만 해제할 수 있는 이진 잠금.
- **세마포어(semaphore)**: 정수 카운터. `wait`(P)로 감소, `signal`(V)로 증가. 자원 `N`개를 동시에 허용.
- **조건 변수(condition variable)**: 특정 조건이 될 때까지 대기/통지(생산자-소비자).

바쁜 대기(busy-waiting)로 도는 락을 **스핀락(spinlock)** 이라 하며, 짧은 임계 구역에 유리하다.

## 구현 (Implementation)

세마포어로 동시 접근 수를 제한한다.

```python
import threading

semaphore = threading.Semaphore(2)   # 동시에 최대 2개 허용
result = []

def access(i):
    with semaphore:                  # wait(P) ... signal(V)
        result.append(f"{i} 진입")

threads = [threading.Thread(target=access, args=(i,)) for i in range(5)]
for t in threads: t.start()
for t in threads: t.join()
# 어느 순간에도 임계 구역 안의 스레드는 최대 2개
```

뮤텍스(`Lock`)는 동시 1개만 허용하는 세마포어의 특수 경우로 볼 수 있다.

```python
lock = threading.Lock()
with lock:
    pass   # 임계 구역: 한 번에 한 스레드
```

## 복잡도 (Complexity)

성능은 **경합(contention)** 정도가 좌우한다.

| 상황 | 영향 |
|---|---|
| 임계 구역이 김 | 다른 스레드 대기 증가, 병렬성 저하 |
| 락 경합이 심함 | 컨텍스트 스위치·캐시 무효화 비용 |
| 스핀락 + 긴 임계 구역 | CPU를 헛돌며 낭비 |
| 락 세분화(fine-grained) | 병렬성↑, 그러나 교착 위험·복잡도↑ |

## 응용 (Applications)

- 공유 카운터·자료구조의 안전한 갱신
- 생산자-소비자 큐(조건 변수)
- 커넥션 풀·자원 풀의 개수 제한(세마포어)
- 데이터베이스 락, 커널 자료구조 보호

## 흔한 오해 (Common Misunderstandings)

- 뮤텍스와 세마포어는 같지 않다. 뮤텍스는 소유 개념이 있어 잠근 스레드만 풀 수 있고, 세마포어는 카운팅 신호라 다른 스레드가 `signal`할 수 있다.
- 락을 더 많이 건다고 안전한 게 아니다. 잘못된 순서로 여러 락을 잡으면 **교착 상태**가 생긴다.
- `volatile`이나 단순 플래그로 동기화가 끝나지 않는다. 가시성(visibility)과 원자성(atomicity)은 다른 문제다.
- CPython의 GIL이 있어도 동기화는 필요하다. `+=` 같은 복합 연산은 여전히 원자적이지 않다.

## TMI

- 데이크스트라가 1965년 세마포어를 제안하며 쓴 `P`(probeer, 시도)와 `V`(verhoog, 증가)는 네덜란드어에서 왔다.
- 식사하는 철학자 문제(dining philosophers)는 동기화와 교착을 가르치는 고전 예제로, 자원 획득 순서가 왜 중요한지 보여 준다.
- 락-프리(lock-free) 자료구조는 락 대신 `compare-and-swap`(CAS) 같은 원자적 명령으로 동기화해, 교착 없이 높은 병렬성을 노린다. 대신 구현이 매우 까다롭다.

## 연습 / 확인 문제 (Exercises)

- 락 없이 두 스레드가 공유 카운터를 증가시켜 값이 손실되는 경쟁 조건을 재현하라.
- 세마포어로 크기 `N`인 버퍼의 생산자-소비자 문제를 구현하라.
- 두 스레드가 락 두 개를 반대 순서로 잡을 때 교착이 생기는 시나리오를 작성하라.

## 이어서 읽기 (Reading Path)

- 이전: [CPU 스케줄링](Scheduling.md)
- 다음: [교착 상태](Deadlock.md)
- 관련: [프로세스와 스레드](Processes-and-Threads.md)

## 참조 (References)

- [Systems/Operating-Systems/Processes-and-Threads.md](Processes-and-Threads.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Courses.md](../../Reference/Courses.md)
