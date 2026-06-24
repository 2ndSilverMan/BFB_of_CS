# 데이터 오염 공격 (Poisoning Attacks)

- Level: Advanced
- Prerequisites: [Engineering/Security/Web-Security.md](../../Engineering/Security/Web-Security.md), [AI/MLOps/Data-Validation.md](../MLOps/Data-Validation.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

데이터 오염 공격은 학습 데이터, fine-tuning data, feedback data, retrieval index에 악의적 샘플을 주입해 모델 행동을 바꾸는 공격이다. Backdoor, targeted misclassification, data extraction 유도 등이 포함된다.

## 직관 (Intuition)

요리 재료 창고에 몰래 이상한 재료를 섞으면 완성된 음식 맛이 바뀐다. 모델도 학습 데이터 공급망이 오염되면 배포 후 특정 조건에서 의도치 않은 행동을 할 수 있다.

## 이론 (Theory)

Poisoning은 availability attack과 integrity attack으로 나눌 수 있다. Backdoor attack은 특정 trigger가 있을 때만 목표 행동이 나오도록 학습시킨다. LLM에서는 instruction data poisoning, preference data poisoning, RAG corpus poisoning, prompt injection과 결합된 retrieval poisoning이 중요하다.

방어는 data provenance, deduplication, anomaly detection, robust training, holdout evaluation, canary, access control을 조합한다.

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
