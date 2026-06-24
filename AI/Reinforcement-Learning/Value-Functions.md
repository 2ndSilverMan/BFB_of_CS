# 가치 함수와 벨만 방정식 (Value Functions and Bellman Equations)

- Level: Intermediate
- Prerequisites: [AI/Reinforcement-Learning/MDP.md](MDP.md), [Math/Probability-Statistics/Expectation.md](../../Math/Probability-Statistics/Expectation.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

value function은 특정 상태(또는 상태-행동)에서 시작해 정책 $\pi$를 따랐을 때 기대되는 누적 보상이다. 상태 가치 $V^\pi(s)$와 행동 가치 $Q^\pi(s,a)$로 나뉘며, 벨만 방정식은 이 값들이 만족하는 재귀 관계다.

## 직관 (Intuition)

강화학습의 목표는 "지금 보상"이 아니라 "앞으로 받을 보상의 총합"을 키우는 것이다. 가치 함수는 각 상황이 장기적으로 얼마나 좋은지를 한 숫자로 요약한다. 핵심 통찰은 "어떤 상태의 가치 = 즉시 보상 + 다음 상태의 가치"라는 재귀 구조이며, 이 덕분에 전체를 한꺼번에 풀지 않고 단계적으로 계산할 수 있다.

## 이론 (Theory)

할인율 $\gamma\in[0,1)$에서 return은 $G_t=\sum_{k\ge 0}\gamma^k R_{t+k+1}$이고,

$$V^\pi(s)=\mathbb{E}_\pi[G_t\mid S_t=s],\qquad Q^\pi(s,a)=\mathbb{E}_\pi[G_t\mid S_t=s,A_t=a]$$

**벨만 기대 방정식**:

$$V^\pi(s)=\sum_a \pi(a\mid s)\sum_{s',r}p(s',r\mid s,a)\big[r+\gamma V^\pi(s')\big]$$

**벨만 최적 방정식**(최적 가치 $V^\*,Q^\*$):

$$Q^\*(s,a)=\sum_{s',r}p(s',r\mid s,a)\big[r+\gamma \max_{a'}Q^\*(s',a')\big]$$

벨만 연산자는 $\gamma$-수축(contraction)이라, 반복 적용하면 유일한 고정점으로 수렴한다. 이것이 value iteration·TD 학습의 이론적 근거다.

## 구현 (Implementation)

```python
def value_iteration(states, actions, P, R, gamma, tol=1e-6):
    V = {s: 0.0 for s in states}
    while True:
        delta = 0
        for s in states:
            v_old = V[s]
            V[s] = max(sum(P[s][a][s2] * (R[s][a][s2] + gamma * V[s2])
                           for s2 in states) for a in actions)
            delta = max(delta, abs(v_old - V[s]))
        if delta < tol:                 # 수축이라 수렴 보장
            return V
```

## 복잡도 (Complexity)

상태 $|S|$, 행동 $|A|$에서 한 번의 벨만 갱신(sweep)은 `O(|S|^2|A|)`(전이 합 포함)다. 수렴까지 반복 횟수는 $\gamma$에 따라 늘어난다($\gamma$가 1에 가까울수록 느림). 상태 공간이 크면 표 기반 계산이 불가능해 함수 근사가 필요하다.

## 응용 (Applications)

- 동적 프로그래밍(value/policy iteration)의 핵심량
- TD·Q-learning 등 모델 프리 학습의 학습 대상
- 게임·로봇·제어의 평가 함수
- DQN 등 딥 RL의 가치 추정

## 흔한 오해 (Common Misunderstandings)

- $V$와 $Q$는 다르다. 행동 선택에는 보통 $Q$가 더 직접적으로 쓰인다.
- 할인율 $\gamma$는 단순 하이퍼파라미터가 아니라 "얼마나 미래를 보는가"를 정해 최적 정책 자체를 바꾼다.
- 벨만 방정식은 정책 평가식이지, 그 자체가 최적 정책을 주지는 않는다(최적 방정식은 별개).
- 가치가 높은 상태가 곧 도달하기 쉬운 상태라는 뜻은 아니다.

## TMI

- 벨만 방정식은 1950년대 Richard Bellman의 동적 프로그래밍에서 나왔고, "curse of dimensionality"라는 표현도 그가 만들었다.
- $\gamma<1$ 조건은 무한 지평에서 return이 발산하지 않게 하는 수학적 장치이기도 하다.
- 수축 사상과 고정점 정리(바나흐)는 가치 반복 수렴 증명의 핵심 도구다.

## 연습 / 확인 문제 (Exercises)

- 2상태 MDP에서 주어진 정책의 $V^\pi$를 벨만 기대 방정식으로 직접 풀어라.
- $\gamma$를 0에 가깝게/1에 가깝게 둘 때 최적 정책이 어떻게 달라지는지 예로 보여라.
- 벨만 최적 연산자가 수축임을 이용해 value iteration의 수렴을 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [MDP](MDP.md)
- 다음: [정책 (Policy)](Policy.md), [시간 차분 학습](TD-Learning.md)

## 참조 (References)

- [AI/Reinforcement-Learning/MDP.md](MDP.md)
- [AI/Reinforcement-Learning/TD-Learning.md](TD-Learning.md)
- [Reference/Books.md](../../Reference/Books.md)
