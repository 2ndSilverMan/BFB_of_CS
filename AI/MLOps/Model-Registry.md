# 모델 레지스트리 (Model Registry)

- Level: Intermediate
- Prerequisites: [AI/MLOps/Experiment-Tracking.md](Experiment-Tracking.md), [AI/MLOps/ML-Pipeline.md](ML-Pipeline.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

모델 레지스트리는 model artifact와 version, lineage, evaluation, approval, deployment status를 관리하는 system of record다. Artifact store와 metadata catalog, promotion workflow를 연결한다.

## 직관 (Intuition)

공유 폴더의 `best_model.pkl` 대신 immutable version과 검증 성적표를 등록하고 `staging`, `production` alias가 어떤 version을 가리키는지 감사 가능하게 바꾼다.

## 이론 (Theory)

Entry에는 artifact digest, model signature, framework/runtime, training run, data version, metrics, owner, approval가 필요하다. Version은 immutable하고 stage/alias만 원자적으로 이동한다. Promotion gate는 quality, latency, security scan, compatibility를 확인한다.

Rollback은 이전 artifact뿐 아니라 preprocessing·feature·schema compatibility를 함께 복원해야 한다.

## 구현 (Implementation)

```yaml
model: churn-risk
version: 12
artifact_digest: sha256:example
training_run: run-9482
data_version: customer-churn-v7
signature: {input: feature-schema-v4, output: probability}
status: validated
```

## 복잡도 (Complexity)

Metadata query는 작지만 artifact storage는 model 수·size·retention에 비례한다. Replication과 scan, download cache가 운영 비용을 만든다.

## 응용 (Applications)

- model promotion·rollback
- lineage·audit
- deployment automation
- 여러 team의 model discovery

## 흔한 오해 (Common Misunderstandings)

- registry 등록이 production readiness를 자동 보장하지 않는다.
- mutable file overwrite는 version registry가 아니다.
- model만 rollback하고 feature pipeline을 남기면 incompatibility가 생긴다.
- registry에 secret·raw training data를 넣으면 안 된다.

## TMI

- alias는 human-friendly pointer, digest는 immutable identity 역할을 한다.
- model card를 registry metadata와 연결하면 limitation을 배포자가 확인할 수 있다.
- garbage collection은 lineage·legal retention을 고려해야 한다.

## 연습 / 확인 문제 (Exercises)

- registry metadata schema를 설계하라.
- promotion gate와 rollback 절차를 작성하라.
- model signature 호환성 test를 정의하라.

## 이어서 읽기 (Reading Path)

- 이전: [ML 파이프라인](ML-Pipeline.md)
- 다음: [모델 모니터링](Model-Monitoring.md)

## 참조 (References)

- [AI/MLOps/Experiment-Tracking.md](Experiment-Tracking.md)
- [AI/MLOps/ML-Pipeline.md](ML-Pipeline.md)
- [Reference/Books.md](../../Reference/Books.md)
