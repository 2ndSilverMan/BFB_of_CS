# 데이터 버전 관리 (Data Versioning)

- Level: Intermediate
- Prerequisites: [AI/MLOps/Reproducibility.md](Reproducibility.md), [Engineering/DevOps/Git/README.md](../../Engineering/DevOps/Git/README.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

데이터 버전 관리는 dataset snapshot, schema, lineage, transformation과 접근 정책을 식별해 어떤 데이터가 model을 만들었는지 추적하는 실천이다.

## 직관 (Intuition)

파일 이름 `final_v2.csv` 대신 immutable ID와 생성 recipe를 남긴다. 원본이 같아도 filter·join·label correction이 다르면 다른 dataset version이다.

## 이론 (Theory)

Snapshot 방식은 재현이 쉽지만 저장이 크고, recipe+source 방식은 공간을 아끼지만 source immutability와 deterministic transform이 필요하다. Content hash, manifest, object storage URI, schema, partition, label policy를 함께 관리한다. 개인 삭제 요청과 retention은 immutability 정책에 예외 workflow가 필요하다.

## 구현 (Implementation)

```yaml
dataset_id: customer-churn-v7
sources:
  - uri: object://raw/events/2026-06/
transform_commit: abc123
schema_version: 4
row_count: 1250031
split_manifest: splits-v7.json
```

## 복잡도 (Complexity)

Full copy는 version마다 `O(data size)` 공간, content-addressed chunking은 변경분 중심으로 저장할 수 있다. Hash 계산과 validation은 data size에 선형이다.

## 응용 (Applications)

- model lineage·rollback
- label correction audit
- train/serve consistency
- reproducible feature pipeline

## 흔한 오해 (Common Misunderstandings)

- Git에 대용량·민감 data를 직접 commit하면 안 된다.
- schema만 같다고 의미가 같은 dataset은 아니다.
- latest pointer만 저장하면 과거 재현이 어렵다.
- data versioning은 access control·privacy를 대체하지 않는다.

## TMI

- data diff는 row count뿐 아니라 distribution·label transition도 보여 줄 수 있다.
- time-travel table과 object manifest는 서로 다른 versioning 구현이다.
- feature definition version도 raw data version만큼 중요하다.

## 연습 / 확인 문제 (Exercises)

- dataset manifest schema를 설계하라.
- 삭제 요청과 재현성 요구를 함께 만족하는 정책을 논의하라.
- 두 version의 의미적 diff 항목을 정의하라.

## 이어서 읽기 (Reading Path)

- 이전: [재현 가능성](Reproducibility.md)
- 다음: [ML 파이프라인](ML-Pipeline.md)

## 참조 (References)

- [Engineering/DevOps/Git/README.md](../../Engineering/DevOps/Git/README.md)
- [Reference/Books.md](../../Reference/Books.md)
