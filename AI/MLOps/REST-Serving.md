# REST 모델 서빙 (REST Model Serving)

- Level: Intermediate
- Prerequisites: [Engineering/DevOps/Docker-Basics.md](../../Engineering/DevOps/Docker-Basics.md), [Engineering/Security/Auth.md](../../Engineering/Security/Auth.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

REST 모델 서빙은 HTTP API로 validation, preprocessing, inference, postprocessing을 제공한다. Model code뿐 아니라 schema, version, timeout, batching, security와 observability가 하나의 serving contract를 이룬다.

## 직관 (Intuition)

모델 파일을 server에 올리는 것으로 끝나지 않는다. 입력을 안전하게 받고 훈련 때와 같은 변환을 적용하며 느린 요청과 오류를 제어해 안정적인 service로 감싼다.

## 이론 (Theory)

API는 explicit schema와 model version을 두고 idempotency, error semantics, size limit를 정의한다. CPU-bound inference는 async만으로 빨라지지 않으며 worker·batch·accelerator를 조절한다. Readiness는 model load 완료 후 성공해야 한다.

## 구현 (Implementation)

```python
def predict_endpoint(payload, model, transformer):
    validated = validate_schema(payload)
    features = transformer.transform(validated)
    prediction = model.predict(features)
    return {"model_version": model.version, "prediction": prediction}
```

실제 endpoint는 auth, timeout, request ID, logging redaction을 추가한다.

## 복잡도 (Complexity)

Latency는 queue+preprocess+inference+postprocess+network 합이다. Throughput은 worker, batch size, memory와 accelerator utilization에 제한된다.

## 응용 (Applications)

- real-time scoring
- internal model microservice
- synchronous feature API
- online experimentation

## 흔한 오해 (Common Misunderstandings)

- async framework가 CPU inference를 자동 병렬화하지 않는다.
- request 전체를 log하면 민감정보가 노출될 수 있다.
- health check가 model correctness를 완전히 검증하지 않는다.
- preprocessing version mismatch는 silent prediction bug를 만든다.

## TMI

- dynamic batching은 짧게 기다려 여러 request를 한 tensor로 묶는다.
- cold start에는 image pull, runtime, model load, warmup이 포함된다.
- shadow traffic은 응답에 영향 없이 새 모델을 관찰한다.

## 연습 / 확인 문제 (Exercises)

- prediction request/response schema를 정의하라.
- timeout·overload 응답 정책을 설계하라.
- train/serve preprocessing 일치 test를 작성하라.

## 이어서 읽기 (Reading Path)

- 이전: [온라인/배치 서빙](Online-vs-Batch-Serving.md)
- 다음: [모델 최적화](Model-Optimization.md), [A/B 테스트](AB-Testing.md)

## 참조 (References)

- [Engineering/Security/Auth.md](../../Engineering/Security/Auth.md)
- [Reference/Books.md](../../Reference/Books.md)
