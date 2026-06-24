# 레이스 컨디션 디버깅 (Race Condition Debugging)

- Level: Advanced
- Prerequisites: [Systems/Operating-Systems/Synchronization.md](../../Systems/Operating-Systems/Synchronization.md), [Engineering/Debugging/Scientific-Debugging.md](Scientific-Debugging.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

레이스 컨디션은 여러 실행 흐름이 공유 상태에 접근하는 순서에 따라 결과가 달라지는 버그다. 재현이 어렵고 로그나 디버거가 timing을 바꿔 숨길 수 있다.

## 직관 (Intuition)

두 사람이 동시에 같은 문서를 수정하는데 순서와 잠금 규칙이 없다면 마지막 저장자가 앞 사람 변경을 덮어쓸 수 있다.

## 이론 (Theory)

Data race는 동기화 없이 같은 메모리에 하나 이상 쓰기가 포함된 동시 접근이다. Atomicity, visibility, ordering 문제가 함께 나타난다. ThreadSanitizer 같은 도구가 도움을 줄 수 있다.

## 구현 (Implementation)

```python
# 개념 예시: 공유 counter를 lock 없이 증가
counter = counter + 1
```

읽기-수정-쓰기 세 단계가 원자적이지 않으면 업데이트가 사라질 수 있다.

## 복잡도 (Complexity)

가능한 thread interleaving 수는 매우 커서 순수 재현 반복만으로는 비용이 폭발한다. Deterministic scheduler, stress test, lock tracing, sanitizer는 탐색 공간을 줄이지만 실행 overhead와 false positive를 함께 고려해야 한다.

## 응용 (Applications)

- 멀티스레드 서버
- 캐시와 공유 map
- 비동기 작업 queue
- 테스트 flakiness 조사

## 흔한 오해 (Common Misunderstandings)

- 재현 빈도가 낮아도 위험도가 낮은 것은 아니다.
- 로그를 추가하면 timing이 바뀌어 버그가 사라질 수 있다.
- 단일 머신에서 괜찮아도 코어 수와 부하가 바뀌면 터질 수 있다.
- Lock만 추가하면 deadlock이나 성능 문제가 생길 수 있다.

## TMI

- Heisenbug는 관찰하면 사라지는 버그를 농담처럼 부르는 말이다.
- Deterministic scheduler는 concurrency test를 안정화하는 연구/도구 방향이다.
- Immutable data와 message passing은 공유 상태를 줄인다.

## 연습 / 확인 문제 (Exercises)

- 공유 counter race를 재현하고 lock으로 고쳐라.
- 레이스 디버깅에서 로그가 위험한 이유를 설명하라.
- ThreadSanitizer가 찾을 수 있는 버그 유형을 조사하라.

## 이어서 읽기 (Reading Path)

- 이전: [동기화](../../Systems/Operating-Systems/Synchronization.md)
- 다음: [데드락 탐지](Deadlock-Detection.md)

## 참조 (References)

- [Systems/Operating-Systems/Synchronization.md](../../Systems/Operating-Systems/Synchronization.md)
- [Reference/Books.md](../../Reference/Books.md)
