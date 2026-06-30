# 스택 트레이스 읽기 (Reading Stack Traces)

- Level: Intermediate
- Prerequisites: [Programming/Functions-and-Recursion.md](../../Programming/Functions-and-Recursion.md), [Engineering/Debugging/Scientific-Debugging.md](Scientific-Debugging.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

스택 트레이스는 예외·오류 시점의 call stack frame을 함수, 파일, 줄과 함께 보여 준다. 실패 지점에서 어떤 호출 경로로 도달했는지 추적하는 핵심 증거다.

## 직관 (Intuition)

함수 호출을 쌓아 둔 접시 더미라 보면 맨 위가 현재 실행 위치다. Trace는 위·아래 방향 표기가 runtime마다 다르므로 exception message와 첫 application frame을 기준으로 읽는다.

## 이론 (Theory)

먼저 exception type·message·cause chain을 읽고, framework 내부 frame을 건너 application code의 가장 가까운 frame으로 간다. 이후 caller 방향으로 input과 invariant가 어디서 깨졌는지 추적한다.

Async task, callback, distributed request에서는 한 stack만으로 전체 경로가 연결되지 않아 trace ID와 async stack support가 필요하다. Optimized build·source map·symbol이 없으면 frame 해석이 제한된다.

### Trace를 읽는 순서

스택 트레이스는 위에서부터 무작정 읽기보다 실패 지점, 최초 애플리케이션 프레임, 경계 호출, 원인 예외를 분리해 본다. Wrapper exception이 많으면 가장 바깥 증상과 가장 안쪽 cause가 다를 수 있다.

비동기/분산 환경에서는 logical stack이 물리적 call stack과 다르다. async task, queue consumer, RPC boundary에서는 trace ID와 causality metadata가 없으면 원인 흐름이 끊긴다.

## 구현 (Implementation)

```python
import traceback


try:
    int("not-a-number")
except ValueError:
    traceback.print_exc()
```

Production log에는 stack과 correlation context를 남기되 token·개인정보를 redaction한다.

## 복잡도 (Complexity)

Stack capture는 depth $d$에 대략 `O(d)`이며 symbolization·source map lookup 비용이 추가된다. 빈번한 exception을 정상 control flow로 쓰면 비용이 커질 수 있다.

## 응용 (Applications)

- exception root cause 탐색
- crash·error grouping
- async failure 조사
- regression 위치 추적

## 흔한 오해 (Common Misunderstandings)

- trace의 마지막 줄만 고치면 원인이 해결되는 것은 아니다.
- framework frame가 많아도 첫 application frame를 놓치면 안 된다.
- exception wrapping에서 original cause를 버리면 진단이 어려워진다.
- line number는 배포 source version과 맞아야 한다.

## TMI

- "Caused by" chain은 low-level error가 domain error로 번역된 경로를 보여 준다.
- minified JavaScript는 source map이 있어야 원본 위치를 복원한다.
- native crash는 debug symbol과 core dump가 필요할 수 있다.

## 연습 / 확인 문제 (Exercises)

- nested exception trace에서 최초 원인을 찾아라.
- application frame과 library frame을 구분하라.
- context를 보존하는 exception wrapping을 작성하라.

## 이어서 읽기 (Reading Path)

- 이전: [과학적 디버깅](Scientific-Debugging.md)
- 다음: [구조화 로깅](Structured-Logging.md)

## 참조 (References)

- [Programming/Functions-and-Recursion.md](../../Programming/Functions-and-Recursion.md)
- [Reference/Books.md](../../Reference/Books.md)
