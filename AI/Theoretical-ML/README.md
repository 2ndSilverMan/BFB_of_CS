# 이론적 머신러닝 (Theoretical Machine Learning)

> 학습 알고리즘의 능력과 한계를 수학적으로 분석하는 분야.

**선수지식**: [AI/Machine-Learning/](../Machine-Learning/), [Math/Real-Analysis/](../../Math/Real-Analysis/), [Math/Probability-Statistics/](../../Math/Probability-Statistics/)

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

### 계산 학습 이론

| 주제 | 파일 | Status |
|---|---|---|
| PAC 학습 프레임워크 | PAC-Learning.md | Planned |
| VC 차원 | VC-Dimension.md | Planned |
| Shattering과 성장 함수 | Shattering.md | Planned |
| 샘플 복잡도 하한 (NFL 정리) | No-Free-Lunch.md | Planned |

### 일반화 이론

| 주제 | 파일 | Status |
|---|---|---|
| 편향-분산 트레이드오프 (이론적) | Bias-Variance-Theory.md | Planned |
| Rademacher 복잡도 | Rademacher-Complexity.md | Planned |
| 일반화 경계 (Generalization Bounds) | Generalization-Bounds.md | Planned |
| 이중 강하 현상 (Double Descent) | Double-Descent.md | Planned |

### 최적화 이론과 학습

| 주제 | 파일 | Status |
|---|---|---|
| 볼록 최적화와 학습 | Convex-Learning.md | Planned |
| 비볼록 최적화에서의 수렴 | Non-Convex-Convergence.md | Planned |
| 경사 하강법 수렴 분석 | GD-Convergence.md | Planned |
| 암묵적 규제 (Implicit Regularization) | Implicit-Regularization.md | Planned |

### 온라인 학습

| 주제 | 파일 | Status |
|---|---|---|
| 후회 최소화 (Regret Minimization) | Regret-Minimization.md | Planned |
| 전문가 알고리즘 | Expert-Algorithms.md | Planned |
| 멀티암드 밴딧 | Multi-Armed-Bandit.md | Planned |

### 정보 이론과 학습

| 주제 | 파일 | Status |
|---|---|---|
| MDL (최소 기술 길이) | MDL.md | Planned |
| 상호 정보량과 학습 | Mutual-Information.md | Planned |

---

## 학습 순서

```text
PAC-Learning → VC-Dimension → Shattering → No-Free-Lunch
        ↓
Bias-Variance-Theory → Rademacher-Complexity → Generalization-Bounds → Double-Descent
        ↓
Convex-Learning → Non-Convex-Convergence → GD-Convergence → Implicit-Regularization
        ↓
Regret-Minimization → Expert-Algorithms → Multi-Armed-Bandit
        ↓
MDL → Mutual-Information
```

---

## 연관 섹션

- [Math/Real-Analysis/](../../Math/Real-Analysis/) — 선수지식
- [AI/Machine-Learning/](../Machine-Learning/) — 이론을 적용하는 실제 ML
- [CS-Theory/Computation-Theory/](../../CS-Theory/Computation-Theory/) — 계산 복잡도
