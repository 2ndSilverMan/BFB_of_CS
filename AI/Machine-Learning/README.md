# 머신러닝 (Machine Learning)

> 데이터에서 규칙을 자동으로 학습하는 방법.

**선수지식**: [Math/Linear-Algebra/](../../Math/Linear-Algebra/), [Math/Probability-Statistics/](../../Math/Probability-Statistics/), [Math/Optimization/](../../Math/Optimization/)

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

### 지도학습 (Supervised Learning)

| 주제 | 파일 | Status |
|---|---|---|
| 선형 회귀 | [Linear-Regression.md](Linear-Regression.md) | Draft |
| 로지스틱 회귀 | [Logistic-Regression.md](Logistic-Regression.md) | Draft |
| 결정 트리 | Decision-Trees.md | Planned |
| 앙상블 (Random Forest, Boosting) | Ensemble.md | Planned |
| SVM | SVM.md | Planned |
| k-NN | KNN.md | Planned |

### 비지도학습 (Unsupervised Learning)

| 주제 | 파일 | Status |
|---|---|---|
| k-평균 클러스터링 | K-Means.md | Planned |
| 계층적 클러스터링 | Hierarchical-Clustering.md | Planned |
| 차원 축소 (PCA, t-SNE, UMAP) | Dimensionality-Reduction.md | Planned |

### 모델 평가 및 일반화

| 주제 | 파일 | Status |
|---|---|---|
| 편향-분산 트레이드오프 | Bias-Variance.md | Planned |
| 교차 검증 | Cross-Validation.md | Planned |
| 정규화 (L1, L2, Dropout) | Regularization.md | Planned |
| 과적합과 과소적합 | Overfitting.md | Planned |

---

## 학습 순서

```text
Linear-Regression → Logistic-Regression
        ↓
Decision-Trees / KNN / SVM → Ensemble
        ↓
K-Means / Hierarchical-Clustering / Dimensionality-Reduction
        ↓
Bias-Variance → Cross-Validation → Regularization → Overfitting
```

---

## 연관 섹션

- [AI/Deep-Learning/](../Deep-Learning/) — ML의 확장
- [Math/Optimization/](../../Math/Optimization/) — 모델 학습 = 최적화
