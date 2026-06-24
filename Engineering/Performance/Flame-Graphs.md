# 플레임 그래프 (Flame Graphs)

- Level: Intermediate
- Prerequisites: [Engineering/Performance/CPU-Profiling.md](CPU-Profiling.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

플레임 그래프는 stack sample을 접어 같은 call stack을 합치고, 폭으로 sample 비중을 표현하는 성능 시각화다.

## 직관 (Intuition)

가로로 넓은 박스는 많은 표본에서 등장한 stack이다. 높이는 call depth이고, 왼쪽에서 오른쪽 순서는 시간 순서가 아니다.

## 이론 (Theory)

프로파일러는 일정 주기로 thread stack을 수집한다. 동일한 stack trace를 aggregate한 뒤 root에서 leaf까지 쌓아 그린다. On-CPU flame graph는 CPU 소비를, off-CPU flame graph는 block·sleep 시간을, allocation flame graph는 allocation source를 보여 준다. Symbol과 stack unwinding 품질이 나쁘면 그래프가 깨진다.

## 구현 (Implementation)

```text
main;handle_request;parse_json 42
main;handle_request;query_db 180
main;handle_request;render 25
```

위 folded stack 형식에서 숫자는 sample 수다. 넓은 `query_db` 박스는 CPU인지 대기인지 profile 종류와 함께 해석해야 한다.

## 복잡도 (Complexity)

수집 비용은 sample frequency와 thread 수에 비례한다. 렌더링은 unique stack 수에 좌우되며, stack cardinality가 높으면 grouping이 어려워진다.

## 응용 (Applications)

- hotspot 탐색
- lock wait·I/O wait 분석
- allocation source 파악
- 성능 회귀 비교

## 흔한 오해 (Common Misunderstandings)

- 색은 보통 의미가 없고 구분을 돕는 장식이다.
- x축은 timeline이 아니다.
- 가장 위 leaf만 고치면 된다는 뜻이 아니다.
- sample이 적으면 넓은 박스도 우연일 수 있다.

## TMI

- Differential flame graph는 두 profile의 차이를 색으로 보여 준다.
- CPU profile에서 사라진 병목이 off-CPU profile에 나타나는 경우가 많다.
- Inlining 때문에 source 함수와 stack 함수가 다르게 보일 수 있다.

## 연습 / 확인 문제 (Exercises)

- CPU-bound workload와 I/O-bound workload의 flame graph 차이를 설명하라.
- 넓은 stack 하나를 골라 self time과 inclusive time을 구분하라.
- 최적화 전후 profile을 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [I/O 프로파일링](IO-Profiling.md)
- 다음: [분기 예측](Branch-Prediction.md)

## 참조 (References)

- [Engineering/Performance/CPU-Profiling.md](CPU-Profiling.md)
- [Engineering/Debugging/Stack-Traces.md](../Debugging/Stack-Traces.md)

