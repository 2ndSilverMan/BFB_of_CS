# 마르코프 체인 (Markov Chains)

- Level: Intermediate
- Prerequisites: [Math/Probability-Statistics/Probability-Basics.md](Probability-Basics.md), [Math/Linear-Algebra/Matrices.md](../Linear-Algebra/Matrices.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

마르코프 체인은 "다음 상태가 현재 상태에만 의존하고 과거 이력과는 무관한"(마르코프 성질) 확률 과정이다. 상태 전이를 전이 행렬로 표현하고, 장기 거동을 정상 분포로 분석한다.

## 직관 (Intuition)

날씨가 "오늘이 맑으면 내일 맑을 확률 0.8"처럼 바로 직전 상태만으로 결정된다면, 전체 역사를 기억할 필요가 없다. 이 "기억 없음"이 마르코프 성질이다. 많은 스텝을 거치면 시작점을 잊고 일정한 분포로 수렴하는 경우가 많은데, 그 안정 상태가 정상 분포다.

## 이론 (Theory)

상태 집합 위 전이 행렬 $P$, $P_{ij}=\Pr(X_{t+1}=j\mid X_t=i)$, 각 행의 합은 1(확률 행렬). $n$스텝 전이는 $P^n$이다. 분포 $\pi$가

$$\pi P=\pi,\qquad \sum_i \pi_i=1$$

를 만족하면 **정상 분포**다. 체인이 기약적(irreducible)이고 비주기적(aperiodic)이면 유일한 정상 분포로 수렴한다(에르고딕 정리). 정상 분포는 전이 행렬의 고윳값 1에 대응하는 좌고유벡터다. 가역(detailed balance) 체인은 $\pi_i P_{ij}=\pi_j P_{ji}$를 만족한다.

## 구현 (Implementation)

```python
import numpy as np

def stationary(P, iters=1000):
    n = P.shape[0]
    pi = np.ones(n) / n
    for _ in range(iters):
        pi = pi @ P            # 분포를 반복 전이 → 정상 분포로 수렴
    return pi

P = np.array([[0.8, 0.2],
              [0.4, 0.6]])
print(stationary(P))           # πP = π 만족하는 분포
```

## 복잡도 (Complexity)

한 스텝 전이(분포 × 행렬)는 상태 수 $n$에 대해 `O(n^2)`이다. 정상 분포는 반복 곱(거듭제곱법)으로 수렴할 때까지, 또는 $\pi P=\pi$ 선형 시스템을 `O(n^3)`에 직접 풀어 구한다. 희소 전이(대부분 상태가 연결 안 됨)면 반복당 비용이 0이 아닌 원소 수로 줄어든다.

## 응용 (Applications)

- PageRank(웹 그래프의 정상 분포)
- 자연어의 N-gram·텍스트 생성
- 큐잉 이론, 신뢰성·대기열 모델
- MCMC 표본화(원하는 분포를 정상 분포로 설계)

## 흔한 오해 (Common Misunderstandings)

- 마르코프 성질은 "과거 무관"이지 "독립"이 아니다. 상태들은 시간에 걸쳐 상관된다.
- 정상 분포가 항상 유일하거나 존재하는 것은 아니다(기약·비주기 조건 필요).
- 주기적 체인은 분포가 진동해 수렴하지 않을 수 있다.
- 정상 분포는 시작 분포와 무관하지만, 수렴 속도는 영향을 받는다.

## TMI

- 마르코프는 1900년대 초 푸시킨 시의 모음·자음 전이를 분석하며 이 이론을 만들었다.
- 구글 PageRank는 웹을 거대한 마르코프 체인으로 보고 정상 분포를 페이지 중요도로 해석한다.
- MCMC는 "샘플하기 어려운 분포를 정상 분포로 갖는 체인을 일부러 만들어" 표본을 얻는 역발상이다.

## 연습 / 확인 문제 (Exercises)

- 2상태 전이 행렬의 정상 분포를 $\pi P=\pi$로 직접 풀어라.
- 주기적 체인의 예를 만들고 수렴하지 않음을 보여라.
- detailed balance를 만족하는 체인이 그 $\pi$를 정상 분포로 가짐을 확인하라.

## 이어서 읽기 (Reading Path)

- 이전: [확률 기초](Probability-Basics.md)
- 다음: [AI/Reinforcement-Learning/MDP.md](../../AI/Reinforcement-Learning/MDP.md), [마르코프 연쇄 몬테카를로](../../AI/PGMs/MCMC.md)

## 참조 (References)

- [Math/Probability-Statistics/Probability-Basics.md](Probability-Basics.md)
- [AI/Reinforcement-Learning/MDP.md](../../AI/Reinforcement-Learning/MDP.md)
- [Reference/Books.md](../../Reference/Books.md)
