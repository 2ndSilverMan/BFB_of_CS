# 디지털 논리 (Digital Logic)

- Level: Beginner
- Prerequisites: [Systems/Computer-Architecture/Data-Representation.md](Data-Representation.md), [Math/Discrete/Logic.md](../../Math/Discrete/Logic.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

디지털 논리는 0과 1로 표현되는 신호를 논리 게이트로 처리하는 회로의 기초다. 불 대수, 조합 회로(게이트 조합), 순차 회로(상태를 가진 플립플롭)로 컴퓨터의 하드웨어가 만들어진다.

## 직관 (Intuition)

컴퓨터는 결국 스위치(트랜지스터)의 켜짐/꺼짐이다. 이 두 상태를 0/1로 보고, AND·OR·NOT 같은 규칙으로 조합하면 덧셈기, 비교기, 메모리까지 만들 수 있다. 복잡한 연산도 단순한 게이트의 층층이 쌓임이라는 점이 핵심 통찰이다.

## 이론 (Theory)

**불 대수**: 변수는 0/1, 연산은 AND($\cdot$), OR($+$), NOT($\overline{x}$). 드모르간 $\overline{x\cdot y}=\overline x+\overline y$. 진리표로 함수를 정의하고, 카르노 맵으로 식을 간소화한다.

**조합 회로**: 출력이 현재 입력만으로 결정(가산기, 멀티플렉서, 디코더). 반가산기·전가산기를 이어 다비트 덧셈을 만든다.

**순차 회로**: 출력이 과거 상태에도 의존. 래치·플립플롭(D, JK)이 1비트를 저장하고, 클록으로 동기화한다. 레지스터·카운터·유한 상태 기계(FSM)가 여기서 나온다.

## 구현 (Implementation)

```python
def half_adder(a, b):
    return (a ^ b, a & b)              # (합, 자리올림)

def full_adder(a, b, cin):
    s1, c1 = half_adder(a, b)
    s2, c2 = half_adder(s1, cin)
    return (s2, c1 | c2)               # 캐리 전파

def ripple_add(A, B):                  # 비트 리스트(LSB first)
    carry = 0; out = []
    for a, b in zip(A, B):
        s, carry = full_adder(a, b, carry)
        out.append(s)
    out.append(carry)
    return out
```

## 복잡도 (Complexity)

리플 캐리 가산기는 비트 수 $n$에 대해 지연이 `O(n)`(캐리 전파)이다. 캐리 예측(carry-lookahead) 가산기는 `O(log n)` 지연으로 줄인다. 회로 성능은 게이트 지연·임계 경로·전력으로 측정되며, 게이트 수가 면적·비용을 정한다.

## 응용 (Applications)

- CPU의 ALU·레지스터·제어 장치
- 메모리·캐시의 디코더·셀
- FPGA·ASIC 설계
- 임베디드·디지털 신호 처리

## 흔한 오해 (Common Misunderstandings)

- 조합 회로는 기억이 없다. 상태를 가지려면 순차 회로(플립플롭)가 필요하다.
- NAND/NOR는 단독으로 모든 논리를 만들 수 있는 보편 게이트다.
- 클록이 빠를수록 항상 좋지 않다 — 임계 경로 지연·전력·발열 제약이 있다.
- 불 식 간소화는 정확성이 아니라 게이트 수·지연을 줄이는 일이다.

## TMI

- 클로드 섀넌의 1937년 석사논문이 불 대수를 스위칭 회로에 연결해 디지털 시대를 열었다.
- NAND만으로 컴퓨터 전체를 만드는 "Nand2Tetris" 교육과정이 유명하다.
- 캐리-룩어헤드는 덧셈 지연을 줄이려 자리올림을 미리 병렬 계산하는 영리한 기법이다.

## 연습 / 확인 문제 (Exercises)

- 진리표로 XOR를 AND/OR/NOT으로 표현하라.
- 전가산기를 반가산기 두 개로 구성함을 보여라.
- NAND만으로 NOT, AND, OR를 만들어라.

## 이어서 읽기 (Reading Path)

- 이전: [데이터 표현](Data-Representation.md)
- 다음: [CPU와 ISA](CPU-and-ISA.md), [파이프라이닝](Pipelining.md)

## 참조 (References)

- [Systems/Computer-Architecture/CPU-and-ISA.md](CPU-and-ISA.md)
- [Math/Discrete/Logic.md](../../Math/Discrete/Logic.md)
- [Reference/Books.md](../../Reference/Books.md)
