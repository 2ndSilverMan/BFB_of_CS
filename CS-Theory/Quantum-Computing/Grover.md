# Grover 탐색 알고리즘 (Grover Search)

- Level: Advanced
- Prerequisites: [Quantum-Circuits.md](Quantum-Circuits.md), [Quantum-Gates.md](Quantum-Gates.md), [Algorithms/Randomized-Algorithms.md](../../Algorithms/Randomized-Algorithms.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

Grover는 정렬되지 않은 $N$ 개 후보 중 marked item을 찾는다. 고전 black-box 탐색이 $O(N)$ 질의인데, Grover는 **$O(\sqrt N)$** — quadratic speedup. 일반 비구조 탐색에서 이게 최적(증명됨)이다.

## 직관 (Intuition)

모든 후보를 균등 중첩으로 놓고, **정답의 진폭은 키우고 나머지는 줄이는** 과정을 반복한다. 정답을 직접 읽는 게 아니라 **간섭**으로 측정 시 정답 확률을 높인다. 기하적으로는 2차원 평면에서 상태 벡터를 정답 쪽으로 조금씩 회전시키는 것이다.

## 이론 (Theory)

### 1. Grover iteration = 두 반사

균등 중첩에서 각 진폭은 $1/\sqrt N$. 한 iteration:

1. **Oracle**: marked state의 위상을 뒤집음($|x^*\rangle \to -|x^*\rangle$).
2. **Diffusion**: 평균에 대한 반사 → marked 진폭 증폭.

두 반사의 합성은 **회전**이다. 초기각 $\theta\approx 1/\sqrt N$ 에서 매 iteration마다 $2\theta$ 씩 정답 축으로 회전 → 약 $\frac{\pi}{4}\sqrt N$ 회에서 진폭이 최대.

### 2. 과회전 주의

$$\text{최적 반복} \approx \left\lfloor\frac{\pi}{4}\sqrt N\right\rfloor$$

**너무 많이 반복하면 진폭이 다시 줄어든다**(회전이 정답 축을 지나침). marked item이 $M$ 개면 $\frac{\pi}{4}\sqrt{N/M}$.

## 구현 (Implementation)

```text
initialize uniform superposition (각 진폭 1/√N)
repeat ~ (π/4)·√N 회:
    oracle: marked state 위상 플립
    diffusion: 평균에 대한 반사(증폭)
measure → 높은 확률로 marked item
```

**워크드 예제.** $N=10^6$: 고전은 평균 $5\times10^5$ 질의, Grover는 $\frac{\pi}{4}\sqrt{10^6}\approx 785$ 회. **약 600배 적은** 질의(단 지수 아님). oracle 비용까지 더해야 전체 비용이 평가된다.

## 복잡도 (Complexity)

| | 질의 수 |
|---|---|
| 고전 | $O(N)$ |
| Grover | $O(\sqrt N)$ |

speedup은 **quadratic**(지수 아님). oracle 구현 비용·회로 depth가 실제 비용을 좌우한다.

## 응용 (Applications)

- 비구조 탐색, amplitude amplification(일반화).
- 일부 조합 문제의 search subroutine, 대칭키 exhaustive search 비용 평가.

## 흔한 오해 (Common Misunderstandings)

- **모든 검색을 즉시 빠르게 하지 않는다** — oracle 구성 비용이 결정적.
- **speedup은 지수가 아니라 제곱근**.
- **한 번 측정으로 모든 후보를 읽는 게 아니다** — 확률을 높일 뿐.
- **반복을 많이 할수록 좋아지지 않는다** — 과회전으로 확률 감소.

## TMI

- Grover 때문에 **대칭키 보안 비트가 대략 절반**으로 평가된다(AES-128 ≈ 양자 64비트 안전) → AES-256 권장.
- amplitude amplification은 Grover를 임의 초기 분포로 일반화한 틀이다.
- marked item 수 $M$ 을 모르면 반복 횟수를 모르는 문제가 생겨, exponential search류로 추정한다.

## 연습 / 확인 문제 (Exercises)

- Grover의 두 반사(oracle·diffusion)가 무엇인지 설명하라.
- $N=10^6$ 의 최적 반복 횟수 $\frac{\pi}{4}\sqrt N$ 를 계산하라(≈785).
- 과회전이 왜 성공 확률을 떨어뜨리는지 회전 그림으로 설명하라.
- oracle 비용을 무시하면 안 되는 이유를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [양자 회로](Quantum-Circuits.md)
- 다음: [Shor 알고리즘](Shor.md)
- 관련: [랜덤 알고리즘](../../Algorithms/Randomized-Algorithms.md)

## 참조 (References)

- [Quantum-Circuits.md](Quantum-Circuits.md)
- [Algorithms/Randomized-Algorithms.md](../../Algorithms/Randomized-Algorithms.md)
- [Reference/Books.md](../../Reference/Books.md)
