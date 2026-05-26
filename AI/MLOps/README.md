# 머신러닝 운영 (MLOps)

> ML 모델을 실험에서 프로덕션까지 안정적으로 운영하는 엔지니어링 실천.

**선수지식**: [AI/Machine-Learning/](../Machine-Learning/), [Engineering/DevOps/](../../Engineering/DevOps/)

**Last reviewed**: 2026-05-26

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

### 실험 관리

| 주제 | 파일 | Status |
|---|---|---|
| 실험 추적 — MLflow, Weights & Biases | Experiment-Tracking.md | Planned |
| 하이퍼파라미터 튜닝 — Grid Search, Bayesian 최적화 | Hyperparameter-Tuning.md | Planned |
| 재현 가능성 — 시드 고정, 환경 고정 | Reproducibility.md | Planned |
| 데이터 버전 관리 — DVC | Data-Versioning.md | Planned |

### 데이터 파이프라인

| 주제 | 파일 | Status |
|---|---|---|
| Feature Store — 특성 재사용과 일관성 | Feature-Store.md | Planned |
| 데이터 검증 — Great Expectations, Evidently | Data-Validation.md | Planned |
| 스트리밍 vs 배치 파이프라인 | Streaming-vs-Batch.md | Planned |
| 데이터 레이블링과 품질 관리 | Data-Labeling.md | Planned |

### 모델 서빙

| 주제 | 파일 | Status |
|---|---|---|
| 온라인 서빙 vs 배치 추론 | Online-vs-Batch-Serving.md | Planned |
| REST API 서빙 — FastAPI, TorchServe | REST-Serving.md | Planned |
| gRPC 서빙 — TensorFlow Serving | gRPC-Serving.md | Planned |
| 모델 최적화 — 양자화, 프루닝, ONNX | Model-Optimization.md | Planned |
| A/B 테스트와 섀도우 배포 | AB-Testing.md | Planned |

### 모델 모니터링

| 주제 | 파일 | Status |
|---|---|---|
| 데이터 드리프트 탐지 | Data-Drift.md | Planned |
| 모델 성능 저하 모니터링 | Model-Monitoring.md | Planned |
| 피드백 루프와 재학습 트리거 | Feedback-Loop.md | Planned |

### ML 인프라

| 주제 | 파일 | Status |
|---|---|---|
| ML 파이프라인 — Kubeflow, Airflow, Prefect | ML-Pipeline.md | Planned |
| 분산 학습 — 데이터 병렬화, 모델 병렬화 | Distributed-Training.md | Planned |
| GPU 클러스터 관리 | GPU-Cluster.md | Planned |
| 모델 레지스트리 | Model-Registry.md | Planned |

---

## 학습 순서

```text
실험 추적 & 재현 가능성
           ↓
   데이터 파이프라인 & Feature Store
           ↓
     모델 서빙 기초
           ↓
  모델 모니터링 & 드리프트 탐지
           ↓
  분산 학습 & ML 파이프라인 자동화
```

---

## 연관 섹션

- [AI/Machine-Learning/](../Machine-Learning/) — 서빙 대상 모델의 이론
- [AI/Deep-Learning/](../Deep-Learning/) — 분산 학습의 기반
- [Engineering/DevOps/](../../Engineering/DevOps/) — CI/CD, 컨테이너, 클라우드 인프라 재활용
- [Systems/Distributed-Systems/](../../Systems/Distributed-Systems/) — 분산 학습 이론적 기반
- [Engineering/Performance/](../../Engineering/Performance/) — 모델 추론 최적화
