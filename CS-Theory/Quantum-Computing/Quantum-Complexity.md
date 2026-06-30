# 양자 복잡도 클래스 BQP (Quantum Complexity)

- Level: Advanced
- Prerequisites: [Quantum-Circuits.md](Quantum-Circuits.md), [Grover.md](Grover.md), [Shor.md](Shor.md), [CS-Theory/Computation-Theory/Complexity-Classes.md](../Computation-Theory/Complexity-Classes.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

양자 복잡도 이론은 양자 컴퓨터가 어떤 문제를 얼마나 효율적으로 푸는지 연구한다. **BQP**(bounded-error quantum polynomial time)는 다항 크기 양자 회로가 **높은 확률(예: ≥2/3)** 로 답하는 결정 문제의 클래스다.

## 직관 (Intuition)

양자 컴퓨터는 모든 문제를 마법처럼 빠르게 풀지 않는다. 어떤 문제엔 큰 speedup([Shor](Shor.md), 지수), 어떤 문제엔 작은 이점([Grover](Grover.md), 제곱근), 어떤 문제엔 알려진 이점이 없다. BQP는 "양자로 효율적으로 풀 수 있는 문제"의 경계를 형식화한다.

## 이론 (Theory)

### 1. 정의와 오류 증폭

다항 크기 uniform 회로 family $\{C_n\}$ 가, yes면 확률 ≥2/3 수락, no면 ≤1/3 수락. **2/3 은 임의** — $k$ 번 독립 실행 후 다수결로 오류를 $2^{-\Omega(k)}$ 로 낮춘다(Chernoff). 그래서 상수 2/3과 0.99는 같은 클래스를 정의.

### 2. 알려진 포함 관계

$$\text{P} \subseteq \text{BPP} \subseteq \text{BQP} \subseteq \text{PSPACE}$$

(BQP ⊆ PSPACE: 진폭을 다항 공간에서 합산 시뮬레이션). **BQP와 NP의 관계는 미해결** — 한쪽이 다른쪽을 포함한다고 안 알려짐.

### 3. factoring의 위치

Shor로 factoring ∈ BQP. 하지만 **factoring은 NP-완전으로 알려져 있지 않다**(NP ∩ co-NP에 가깝다고 여겨짐). 그래서 "양자가 NP-완전을 푼다"는 결론은 *나오지 않는다*. Grover의 제곱근 speedup도 NP-완전을 다항으로 만들지 못한다($2^{n/2}$ 는 여전히 지수).

## 구현 (Implementation)

```text
BQP 판정(개념):
for 입력 길이 n:
    poly(n) 크기 양자 회로 C_n 구성 (uniform: 고전적으로 효율 생성 가능)
    C_n을 입력 x에 실행
    yes 사례: 수락 확률 >= 2/3
    no  사례: 수락 확률 <= 1/3
# k번 반복 + 다수결 → 오류 2^{-Ω(k)}
```

하드웨어 세부가 아니라 **계산 가능성과 자원 scaling**(큐비트·게이트·depth)에 초점.

## 복잡도 (Complexity)

| 자원 | 측정 대상 |
|---|---|
| 큐비트 수 / 게이트 수 / depth | 회로 비용 |
| oracle query 수 | 질의 복잡도(Grover 등) |
| 오류정정 overhead | fault-tolerant 실현 비용 |

이론적 BQP 알고리즘이 **실용적이라는 뜻은 아니다** — fault-tolerant 구현 비용은 별도.

## 응용 (Applications)

- 양자 알고리즘의 한계 이해, 고전/확률/양자 모델 비교.
- 암호 가정의 장기 안전성 평가, 양자 우위·시뮬레이션 난이도 분석.

## 흔한 오해 (Common Misunderstandings)

- **BQP ⊇ NP 인지 미해결** — 양자가 NP-완전을 푼다고 단정 불가.
- **Shor가 있다고 NP-완전이 다 풀리지 않는다** — factoring은 NP-완전이 아니라고 여겨짐.
- **양자 컴퓨터 ≠ 비결정론 컴퓨터(NP)** — 진폭 간섭이지 "모든 경로를 동시에 수락"이 아니다.
- **이론적 speedup ≠ 실용적 speedup**(상수·overhead).

## TMI

- **QMA**는 양자판 NP(증거가 양자 상태) — 세부는 NP와 다르다.
- 양자 우위(advantage) 실험은 random circuit sampling 같은, 고전 시뮬이 어려운 작업을 노린다(결정 문제가 아닌 샘플링).
- Gottesman-Knill: Clifford 회로는 양자적이지만 고전 효율 시뮬 가능 — "얽힘만으론 양자 우위가 안 난다"는 교훈.

## 연습 / 확인 문제 (Exercises)

- BQP의 bounded-error(2/3) 조건과 다수결 증폭을 설명하라.
- $\text{P}\subseteq\text{BPP}\subseteq\text{BQP}\subseteq\text{PSPACE}$ 의 각 포함 직관을 적어라.
- "BQP = NP"라고 말할 수 없는 이유를 factoring의 위치로 정리하라.
- Grover의 $2^{n/2}$ 가 왜 NP-완전을 다항으로 못 만드는지 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [양자 오류 수정](Quantum-Error-Correction.md)
- 다음: [복잡도 클래스](../Computation-Theory/Complexity-Classes.md)
- 관련: [Shor](Shor.md), [Grover](Grover.md)

## 참조 (References)

- [Quantum-Circuits.md](Quantum-Circuits.md)
- [Grover.md](Grover.md)
- [Shor.md](Shor.md)
- [CS-Theory/Computation-Theory/Complexity-Classes.md](../Computation-Theory/Complexity-Classes.md)
- [Reference/Books.md](../../Reference/Books.md)
