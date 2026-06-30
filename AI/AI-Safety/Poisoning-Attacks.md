# 데이터 오염 공격 (Poisoning Attacks)

- Level: Advanced
- Prerequisites: [Engineering/Security/Web-Security.md](../../Engineering/Security/Web-Security.md), [AI/MLOps/Data-Validation.md](../MLOps/Data-Validation.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

데이터 오염 공격은 학습 데이터, fine-tuning data, feedback data, retrieval index에 악의적 샘플을 주입해 모델 행동을 바꾸는 공격이다. Backdoor, targeted misclassification, data extraction 유도 등이 포함된다.

## 직관 (Intuition)

요리 재료 창고에 몰래 이상한 재료를 섞으면 완성된 음식 맛이 바뀐다. 모델도 학습 데이터 공급망이 오염되면 배포 후 특정 조건에서 의도치 않은 행동을 할 수 있다.

## 이론 (Theory)

Poisoning은 availability attack과 integrity attack으로 나눌 수 있다. Backdoor attack은 특정 trigger가 있을 때만 목표 행동이 나오도록 학습시킨다. LLM에서는 instruction data poisoning, preference data poisoning, RAG corpus poisoning, prompt injection과 결합된 retrieval poisoning이 중요하다.

방어는 data provenance, deduplication, anomaly detection, robust training, holdout evaluation, canary, access control을 조합한다.

### 공격 표면

Poisoning은 학습 데이터에만 국한되지 않는다. 현대 AI 시스템에는 여러 데이터 공급망이 있다.

- Pretraining corpus
- Instruction tuning dataset
- Preference/RLHF dataset
- Evaluation benchmark와 holdout set
- RAG index와 external knowledge base
- User feedback log와 자동 재학습 파이프라인

특히 evaluation set이 오염되면 모델이 실제로 좋아진 것이 아니라 평가에 맞춰진 것일 수 있다. 데이터 무결성은 학습과 평가 모두에 필요하다.

### Backdoor와 trigger

Backdoor는 평소에는 정상적으로 작동하다가 특정 trigger가 있을 때 목표 행동을 내도록 만드는 공격이다. Trigger는 이미지 패턴, 특정 문구, metadata, retrieval 문서 조합처럼 다양한 형태를 가질 수 있다.

Backdoor의 어려움은 clean test 성능이 높아도 숨어 있을 수 있다는 점이다. 따라서 일반 성능 평가와 별도로 trigger search, suspicious cluster 분석, targeted regression test가 필요하다.

### RAG poisoning

RAG 시스템은 모델을 재학습하지 않아도 knowledge base나 검색 순위가 오염되면 잘못된 답을 낼 수 있다. 문서 신뢰도, freshness, source authority, chunk boundary, retrieval score가 모두 공격 표면이다.

운영에서는 ingestion pipeline에 provenance, source allowlist, review queue, hash-based change tracking, rollback을 넣고, 검색 결과가 민감 행동으로 이어질 때는 출처 기반 confidence를 함께 본다.

### 공급망 방어

데이터는 코드처럼 버전 관리되어야 한다. 누가 추가했는지, 어떤 필터를 통과했는지, 어떤 모델 버전에 들어갔는지 추적해야 한다. 원본 데이터, 정제 데이터, 학습 shard, 평가 결과 사이 lineage가 없으면 사고 후 원인 추적이 어렵다.

## 구현 (Implementation)

```python
data_guard = {
    "source_allowlist": True,
    "hash_and_lineage": True,
    "outlier_review": True,
    "poison_trigger_tests": "scheduled",
}
```

데이터셋 변경은 code 변경처럼 review와 rollback이 가능해야 한다.

```python
def dataset_change_requires_review(change):
    return (
        change["source"] not in change["trusted_sources"]
        or change["rows_added"] > change["large_change_threshold"]
        or change["affects_eval_set"]
        or change["contains_user_generated_content"]
    )
```

자동 필터가 통과시킨 데이터도 고영향 source 변경이나 evaluation set 변경이면 별도 리뷰가 필요하다.

## 복잡도 (Complexity)

대규모 데이터에서는 모든 샘플 수동 검토가 불가능하다. 자동 필터는 false positive/negative가 있으며, 공격자는 필터를 우회하려고 적응한다.

## 응용 (Applications)

- 학습 데이터 공급망 보안
- RAG knowledge base 보호
- fine-tuning dataset 검수
- 모델 release 전 backdoor scan

## 흔한 오해 (Common Misunderstandings)

- 공개 데이터만 쓰면 안전한 것이 아니다.
- 데이터 검증은 schema뿐 아니라 semantic·security 검토도 필요하다.
- Backdoor는 일반 test 성능이 높아도 숨어 있을 수 있다.
- RAG는 모델 재학습을 안 하므로 poisoning과 무관하다는 생각은 틀리다.

## TMI

- Clean-label poisoning은 label이 정상처럼 보여 더 찾기 어렵다.
- Web-scale data에서는 중복 샘플이 poison 영향력을 키울 수 있다.
- Retrieval poisoning은 검색 순위와 문서 신뢰도 평가가 함께 필요하다.

## 연습 / 확인 문제 (Exercises)

- Backdoor trigger 평가셋을 설계하라.
- RAG corpus poisoning 방어 절차를 작성하라.
- 데이터 provenance가 없는 dataset의 위험을 평가하라.

## 이어서 읽기 (Reading Path)

- 이전: [Data Validation](../MLOps/Data-Validation.md)
- 다음: [Red-Teaming](Red-Teaming.md), [AI Risk Classification](AI-Risk-Classification.md)

## 참조 (References)

- [AI/MLOps/Data-Validation.md](../MLOps/Data-Validation.md)
- [Engineering/Security/Web-Security.md](../../Engineering/Security/Web-Security.md)
- [Reference/Papers.md](../../Reference/Papers.md)
