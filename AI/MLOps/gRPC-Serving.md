# gRPC 모델 서빙 (gRPC Model Serving)

- Level: Intermediate
- Prerequisites: [AI/MLOps/REST-Serving.md](REST-Serving.md), [Systems/Networks/TCP-UDP.md](../../Systems/Networks/TCP-UDP.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

gRPC 모델 서빙은 schema-first RPC 인터페이스로 inference service를 제공하는 방식이다. 명시적 message contract, binary serialization, deadline, streaming, 내부 서비스 간 통신에 강점이 있다.

## 직관 (Intuition)

REST가 사람이 읽기 쉬운 주문서라면 gRPC는 주방 내부의 정확한 작업 지시서에 가깝다. 어떤 필드가 오고 가는지 미리 정하고, 클라이언트와 서버가 같은 계약에서 코드를 생성한다.

## 이론 (Theory)

Protocol schema는 request·response type, optional field, versioning 규칙을 정의한다. Model serving에서는 tensor shape, dtype, model version, request ID, error code, deadline이 contract에 들어간다.

Unary RPC는 일반 요청/응답에 쓰고, streaming RPC는 긴 입력, incremental output, bidirectional interaction에 쓴다. Deadline과 cancellation은 overload와 stale request를 줄이는 핵심이다.

## 구현 (Implementation)

```proto
service Predictor {
  rpc Predict(PredictRequest) returns (PredictResponse);
}

message PredictRequest {
  string model_version = 1;
  repeated float features = 2;
}
```

서버 구현은 validation, preprocessing, batching, auth, observability를 REST 서빙과 동일하게 고려한다.

## 복잡도 (Complexity)

Serialization overhead는 payload 구조와 크기에 좌우된다. Throughput은 worker, batching, model runtime, network, client connection reuse에 영향을 받는다. Schema evolution을 잘못하면 구버전 client가 깨진다.

## 응용 (Applications)

- 내부 microservice 간 inference
- low-latency feature·prediction service
- streaming inference
- polyglot client가 많은 플랫폼

## 흔한 오해 (Common Misunderstandings)

- gRPC를 쓰면 모델 latency가 자동으로 줄어드는 것은 아니다.
- schema가 있어도 semantic validation은 별도로 필요하다.
- field 삭제·재사용은 backward compatibility를 깨뜨릴 수 있다.
- 내부 API라도 auth, quota, timeout을 생략하면 장애가 커진다.

## TMI

- Deadline propagation은 downstream service가 쓸모없는 일을 계속하지 않게 한다.
- Protobuf field number는 API의 오래 가는 흔적이라 신중히 정한다.
- REST gateway를 함께 두면 외부 client와 내부 service를 나눠 운영할 수 있다.

## 연습 / 확인 문제 (Exercises)

- prediction RPC의 request/response schema를 설계하라.
- backward-compatible schema 변경 예시를 작성하라.
- deadline, retry, idempotency 정책을 정의하라.

## 이어서 읽기 (Reading Path)

- 이전: [REST 모델 서빙](REST-Serving.md)
- 다음: [모델 최적화](Model-Optimization.md), [A/B 테스트](AB-Testing.md)

## 참조 (References)

- [Systems/Networks/TCP-UDP.md](../../Systems/Networks/TCP-UDP.md)
- [Reference/Books.md](../../Reference/Books.md)
