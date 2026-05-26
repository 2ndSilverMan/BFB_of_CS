# 수학 (Math)

> CS와 AI를 이해하는 데 필요한 수학적 토대.

**선수지식**: 없음 (고등학교 수학 수준에서 시작 가능)

---

## 현재 가용성

현재 바로 읽을 수 있는 본문은 [명제 논리와 술어 논리](Discrete/Logic.md)다. 나머지 수학 주제는 섹션 README와 로드맵으로 준비되어 있으며, 각 하위 README에서 `Draft` 이상으로 열린 항목부터 읽는다.

---

## 서브섹션

| 서브섹션 | 내용 | 선수지식 |
|---|---|---|
| [이산수학 (Discrete Mathematics)](Discrete/) | 알고리즘, 논리, 집합론, 그래프 이론의 기반 | 고등학교 수학 |
| [미적분 (Calculus)](Calculus/) | 변화율, 적분, 역전파와 최적화 알고리즘의 기반 | 고등학교 수학 |
| [선형대수 (Linear Algebra)](Linear-Algebra/) | 벡터, 행렬, 고유값, 머신러닝과 그래픽스의 핵심 | [Math/Calculus/](Calculus/) (기초 권장) |
| [확률과 통계 (Probability & Statistics)](Probability-Statistics/) | 확률분포, 추정, 검정, 통계적 학습 | [Math/Calculus/](Calculus/), [Math/Linear-Algebra/](Linear-Algebra/) (기초) |
| [최적화 (Optimization)](Optimization/) | 경사 하강법, 볼록 최적화, ML 학습 | [Math/Calculus/](Calculus/), [Math/Linear-Algebra/](Linear-Algebra/) |
| [실해석학 (Real Analysis)](Real-Analysis/) | 수렴, 연속성, 함수 이론의 엄밀한 기반 | [Math/Calculus/](Calculus/) |
| [수치 해석 (Numerical Methods)](Numerical-Methods/) | 수치 적분, 선형 시스템, 부동소수점 | [Math/Calculus/](Calculus/), [Math/Linear-Algebra/](Linear-Algebra/) |

---

## 학습 순서

Math는 하나의 선형 과정이라기보다 목적에 따라 갈라지는 허브다. 대표적인 경로는 다음 두 가지다.

```text
[CS / 알고리즘 경로]          [AI / ML 경로]
이산수학                       미적분
    ↓                             ↓
자료구조/알고리즘/CS-Theory    선형대수 + 확률/통계
                                  ↓
                              최적화 → AI/ML
                                  ↓
                      실해석학 / 수치 해석 (심화)
```

두 경로는 **독립적**으로 시작할 수 있다. ML을 목표로 한다면 이산수학 전에 미적분부터 시작해도 된다.

---

## 연관 섹션

- [Programming/](../Programming/) — 수학적 개념을 코드로 구현하는 연습
- [Algorithms/](../Algorithms/) — 이산수학과 복잡도 이론 적용
- [AI/Machine-Learning/](../AI/Machine-Learning/) — 선형대수, 확률, 최적화 직접 사용
