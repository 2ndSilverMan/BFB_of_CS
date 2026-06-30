# 결정 불가능성과 정지 문제 (Undecidability & the Halting Problem)

- Level: Advanced
- Prerequisites: [CS-Theory/Computation-Theory/Turing-Machine.md](Turing-Machine.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

결정 불가능성은 **어떤 문제는 그 어떤 알고리즘으로도 항상 올바른 답을 내며 멈출 수 없다**는 사실이다. 가장 유명한 예가 **정지 문제(halting problem)** — "임의의 프로그램과 입력이 주어졌을 때, 그 프로그램이 멈추는지(halt) 아니면 영원히 도는지를 판정하라"는 문제다. 튜링은 1936년 이 문제가 결정 불가능함을 증명했다.

## 직관 (Intuition)

"모든 프로그램의 무한 루프를 미리 잡아내는 완벽한 검사기"가 있으면 좋겠지만, 그런 검사기는 **원리적으로 불가능**하다. 만약 있다고 가정하면, 그 검사기를 거꾸로 이용해 "자기 자신에 대해 모순되는 행동을 하는 프로그램"을 만들 수 있어 논리적 모순이 생긴다. 이 자기 참조 모순이 핵심이다.

## 이론 (Theory)

정지 문제의 결정 불가능성은 **대각선 논법(diagonalization)** 과 자기 참조로 증명된다.

정지 판정기 $H(P, x)$가 "프로그램 $P$가 입력 $x$에서 멈추면 yes, 아니면 no"를 항상 정확히 답한다고 **가정**하자. 그러면 다음 프로그램 $D$를 만들 수 있다.

$$D(P): \quad \text{if } H(P, P) = \text{yes} \text{ then 무한 루프, else 멈춤}$$

이제 $D(D)$를 생각하면 모순이 생긴다.

- $D(D)$가 멈춘다면 → $H(D,D)=\text{yes}$ → 정의상 $D$는 무한 루프 → 안 멈춤. 모순.
- $D(D)$가 안 멈춘다면 → $H(D,D)=\text{no}$ → 정의상 $D$는 멈춤. 모순.

따라서 그런 $H$는 존재할 수 없다. 정지 문제는 **인식 가능(recognizable)하지만 결정 불가능(undecidable)** 하다 — 멈추는 경우는 실행해서 확인할 수 있지만, 안 멈추는 경우를 유한 시간에 단정할 방법이 없다.

**라이스 정리(Rice's theorem)** 는 이를 일반화한다 — 프로그램이 계산하는 함수의 **자명하지 않은 의미적 성질**은 모두 결정 불가능하다. "이 프로그램이 항상 0을 출력하는가?" 같은 질문도 일반적으로 풀 수 없다.

## 구현 (Implementation)

정지 문제는 풀 수 없으므로, "푸는 코드"가 아니라 **모순을 드러내는 구조**를 보인다.

```python
# 가정: 아래 halts(f, x)가 항상 정확히 답한다고 치자 (실제로는 불가능)
def halts(func, arg):
    ...   # 멈추면 True, 아니면 False 를 반환한다고 가정

def diagonal(func):
    if halts(func, func):
        while True:        # 멈춘다고 했으니 일부러 무한 루프
            pass
    else:
        return             # 안 멈춘다고 했으니 멈춤

# diagonal(diagonal) 은 멈춰도 모순, 안 멈춰도 모순
# → halts 같은 함수는 존재할 수 없다
```

## 복잡도 (Complexity)

결정 불가능성은 복잡도(빠르다/느리다)를 넘어선 **계산 가능성**의 한계다.

| 구분 | 의미 |
|---|---|
| 결정 가능(decidable) | 항상 멈추며 yes/no를 답하는 알고리즘 존재 |
| 인식 가능(recognizable) | yes는 멈춰서 확인, no는 영원히 돌 수 있음 |
| 결정 불가능(undecidable) | 항상 멈추는 판정 알고리즘이 존재하지 않음 |

정지 문제는 "아무리 빠른 컴퓨터로도" 풀리지 않는다. 자원의 문제가 아니라 원리의 문제다.

## 응용 (Applications)

- 정적 분석의 근본 한계(완벽한 무한 루프·도달성 검사 불가)
- 컴파일러·검증 도구가 근사·보수적 분석을 쓰는 이유
- 다른 문제의 결정 불가능성 증명(정지 문제로 환원)
- 바이러스 완전 탐지·완벽한 데드코드 제거의 불가능성

## 흔한 오해 (Common Misunderstandings)

- "특정 프로그램의 정지 여부"는 종종 알 수 있다. 결정 불가능한 것은 **모든** 프로그램에 대해 항상 답하는 일반 알고리즘이다.
- 결정 불가능 ≠ "매우 어렵다". NP-난해 문제와 달리, 더 빠른 컴퓨터나 양자 컴퓨터로도 풀 수 없다.
- 결정 불가능성은 인간의 무능이 아니라 **수학적 한계**다. 더 똑똑한 알고리즘으로 극복되는 문제가 아니다.
- 실무 정적 분석기가 무한 루프를 "잡는" 것은 모든 경우가 아니라 일부 패턴에 한한 근사다.

## TMI

- 정지 문제 증명의 대각선 논법은 칸토어가 "실수가 자연수보다 많다"를 보인 기법, 괴델의 불완전성 정리와 같은 뿌리의 자기 참조 논증이다.
- 튜링의 1936년 논문은 사실 힐베르트의 "결정 문제(Entscheidungsproblem)"가 풀 수 없음을 보이는 것이 목적이었고, 튜링 머신은 그 도구로 등장했다.
- "비버 챔피언(Busy Beaver)" 함수는 계산 가능하지 않을 만큼 빨리 커지는 함수로, 정지 문제의 결정 불가능성과 깊이 연결돼 있다.

## 연습 / 확인 문제 (Exercises)

- 정지 문제의 대각선 논법을 자신의 말로 다시 서술하라.
- "이 프로그램이 출력으로 42를 내는가?"가 왜 일반적으로 결정 불가능한지 라이스 정리로 설명하라.
- 결정 불가능 문제와 NP-완전 문제의 차이를 "더 빠른 컴퓨터로 풀리는가" 관점에서 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [튜링 머신](Turing-Machine.md)
- 다음: [복잡도 클래스](Complexity-Classes.md)
- 관련: [NP-완전성과 환원](NP-Completeness.md)

## 참조 (References)

- [CS-Theory/Computation-Theory/Turing-Machine.md](Turing-Machine.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Papers.md](../../Reference/Papers.md)
