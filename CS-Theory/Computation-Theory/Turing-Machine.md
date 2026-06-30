# 튜링 머신 (Turing Machine)

- Level: Advanced
- Prerequisites: [CS-Theory/Computation-Theory/Context-Free.md](Context-Free.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

튜링 머신은 **무한히 긴 테이프**와 그 위를 좌우로 움직이며 읽고 쓰는 **헤드**, 그리고 유한한 상태 제어부로 이뤄진 추상 계산 모델이다. 1936년 앨런 튜링이 "계산이란 무엇인가"를 형식화하려고 고안했으며, 오늘날 "알고리즘으로 계산 가능한 것"의 표준 정의로 쓰인다.

## 직관 (Intuition)

유한 오토마타는 기억이 상태뿐, 푸시다운 오토마타는 스택 하나뿐이라 한계가 있었다. 튜링 머신은 **읽고 쓸 수 있는 무한 테이프**를 줘서 이 제약을 없앤다. 종이 위에서 규칙에 따라 기호를 읽고, 지우고, 다시 쓰고, 좌우로 옮겨 가며 연필로 계산하는 사람을 극한까지 추상화한 것이다.

```mermaid
graph LR
    T["... | 1 | 0 | 1 | _ | ..."] 
    H["헤드 (현재 칸 읽기/쓰기)"] --> T
    C["상태 제어부 (전이 규칙)"] --> H
```

## 이론 (Theory)

튜링 머신은 7-튜플 $(Q, \Sigma, \Gamma, \delta, q_0, q_{accept}, q_{reject})$로 정의된다. 핵심은 전이 함수다.

$$\delta: Q \times \Gamma \rightarrow Q \times \Gamma \times \{L, R\}$$

"현재 상태와 읽은 기호를 보고 → 새 상태로 가고, 기호를 쓰고, 헤드를 좌(L)/우(R)로 옮긴다." 머신은 받아들임/거부 상태에 도달하면 멈추고, 영원히 멈추지 않을 수도 있다.

**처치-튜링 논제(Church-Turing thesis)**: "직관적으로 계산 가능한 모든 함수는 튜링 머신으로 계산 가능하다." 이는 증명된 정리가 아니라, 계산 가능성에 대한 정의로 받아들여지는 명제다. 람다 대수, 재귀 함수, 모든 범용 프로그래밍 언어가 튜링 머신과 **동일한 계산 능력**(튜링 완전, Turing-complete)을 가진다.

언어 인식 능력으로 보면 튜링 머신은 정규·문맥 자유를 포함하는 가장 강력한 모델이며, **결정 가능(decidable, 항상 멈춤)** 언어와 **인식 가능(recognizable, 받아들이면 멈추지만 아니면 영원히 돌 수 있음)** 언어를 구분한다.

## 구현 (Implementation)

`a`를 `b`로 바꾸는 단순 튜링 머신을 시뮬레이션한다.

```python
def run_tm(tape, transitions, start, accept):
    tape = list(tape)
    pos, state = 0, start
    while state != accept:
        sym = tape[pos] if 0 <= pos < len(tape) else "_"
        if (state, sym) not in transitions:
            break
        new_state, write, move = transitions[(state, sym)]
        if 0 <= pos < len(tape):
            tape[pos] = write
        state = new_state
        pos += 1 if move == "R" else -1
    return "".join(tape)

# 모든 a를 b로 바꾸고 끝(_)에서 멈춤
transitions = {
    ("q0", "a"): ("q0", "b", "R"),
    ("q0", "b"): ("q0", "b", "R"),
    ("q0", "_"): ("accept", "_", "R"),
}
print(run_tm("aab", transitions, "q0", "accept"))   # bbb
```

## 복잡도 (Complexity)

튜링 머신은 **계산 가능성과 복잡도 이론의 기준 모델**이다.

| 측면 | 의미 |
|---|---|
| 시간 복잡도 | 멈출 때까지의 전이 횟수 |
| 공간 복잡도 | 사용한 테이프 칸 수 |
| 변형(다중 테이프 등) | 능력은 동일, 효율(다항식 인자)만 차이 |

단일 테이프와 다중 테이프 튜링 머신은 **같은 언어를 인식**하며, 시간 복잡도는 다항식 차이 안에서 서로 시뮬레이션된다. 이 견고함(robustness)이 튜링 머신을 복잡도 클래스 정의의 기준으로 만든다.

## 응용 (Applications)

- 계산 가능성의 형식적 정의(무엇이 알고리즘으로 풀리는가)
- 복잡도 클래스 P, NP, PSPACE 정의의 기준 모델
- 결정 불가능성 증명의 도구([정지 문제](Undecidability.md))
- 튜링 완전성 판정(프로그래밍 언어, 셀룰러 오토마타 등)

## 흔한 오해 (Common Misunderstandings)

- 튜링 머신은 실제로 만드는 기계가 아니라 **사고 모델**이다. 무한 테이프는 물리적 무한이 아니라 "필요한 만큼 늘어나는" 추상이다.
- 처치-튜링 논제는 정리가 아니라 논제(thesis)다. 증명 대상이 아니라 계산 가능성의 정의로 채택된 것이다.
- "튜링 완전"이 "강력하고 빠르다"는 뜻은 아니다. 단지 "모든 계산 가능한 함수를 표현할 수 있다"는 능력의 한계를 뜻한다.
- 튜링 머신이 모든 문제를 푸는 것은 아니다. 정지 문제처럼 결정 불가능한 문제가 존재한다.

## TMI

- 튜링은 이 모델을 1936년, 컴퓨터가 존재하기도 전에 순수 수학 문제(힐베르트의 결정 문제)를 풀기 위해 고안했다.
- 엑셀의 수식, 매직 더 개더링 카드 게임, 심지어 콘웨이의 라이프 게임도 튜링 완전임이 증명됐다. 튜링 완전성은 의외로 단순한 시스템에서도 나타난다.
- "범용 튜링 머신(universal TM)"은 다른 튜링 머신의 설명을 입력으로 받아 그것을 흉내 내는 머신으로, 오늘날 "프로그램을 실행하는 컴퓨터"의 이론적 원형이다.

## 연습 / 확인 문제 (Exercises)

- 입력 이진수에 1을 더하는 튜링 머신의 전이 규칙을 설계하라.
- 결정 가능 언어와 인식 가능 언어의 차이를 정지 여부로 설명하라.
- 다중 테이프 튜링 머신이 단일 테이프보다 "더 강력하지 않은" 이유를 시뮬레이션 관점에서 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [문맥 자유 문법과 푸시다운 오토마타](Context-Free.md)
- 다음: [결정 불가능성](Undecidability.md)
- 관련: [복잡도 클래스](Complexity-Classes.md)

## 참조 (References)

- [CS-Theory/Computation-Theory/Context-Free.md](Context-Free.md)
- [Reference/Books.md](../../Reference/Books.md)
- [Reference/Papers.md](../../Reference/Papers.md)
