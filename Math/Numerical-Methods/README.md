# 수치 해석 (Numerical Methods)

> 수학적 문제를 컴퓨터로 근사 계산하는 방법.

**선수지식**: [Math/Calculus/](../Calculus/), [Math/Linear-Algebra/](../Linear-Algebra/)

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

| 주제 | 파일 | Status |
|---|---|---|
| 부동소수점 표현과 오차 | [Floating-Point.md](Floating-Point.md) | Draft |
| 방정식의 수치 해법 (이분법, Newton-Raphson) | [Root-Finding.md](Root-Finding.md) | Draft |
| 선형 방정식 수치 풀이 (LU 분해, Gaussian 소거) | [Numerical-Linear-Systems.md](Numerical-Linear-Systems.md) | Draft |
| 보간법 (Interpolation) | [Interpolation.md](Interpolation.md) | Draft |
| 수치 미분과 적분 | [Differentiation-Integration.md](Differentiation-Integration.md) | Draft |
| 상미분 방정식 수치 해법 (Euler, Runge-Kutta) | [ODE-Solvers.md](ODE-Solvers.md) | Draft |

---

## 학습 순서

```text
Floating-Point → Root-Finding
        ↓
Numerical-Linear-Systems → Interpolation
        ↓
Differentiation-Integration → ODE-Solvers
```

---

## 연관 섹션

- [AI/Deep-Learning/](../../AI/Deep-Learning/) — 부동소수점 연산, 수치 안정성
- [Math/Optimization/](../Optimization/) — 수치 최적화
