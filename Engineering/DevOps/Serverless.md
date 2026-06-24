# 서버리스 (Serverless)

- Level: Intermediate
- Prerequisites: [Engineering/DevOps/Cloud-Computing.md](Cloud-Computing.md), [Systems/Distributed-Systems/Message-Queues-Event-Streaming.md](../../Systems/Distributed-Systems/Message-Queues-Event-Streaming.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

서버리스는 서버 운영 단위를 직접 관리하지 않고, 함수·event·managed backend 중심으로 application을 실행하는 cloud 모델이다.

## 직관 (Intuition)

항상 켜 둔 주방을 관리하기보다 주문이 들어올 때만 조리대를 빌린다. 사용량이 적거나 event 기반이면 효율적이다.

## 이론 (Theory)

FaaS는 HTTP request, queue message, object upload, schedule 같은 event로 함수를 실행한다. 장점은 자동 scaling, 사용량 기반 과금, 운영 부담 감소다. 단점은 cold start, 실행 시간 제한, local debugging 난도, vendor lock-in, distributed tracing 필요성이다. Stateless function과 external state store 조합이 기본이다.

## 구현 (Implementation)

```text
object uploaded -> function validates metadata
                -> message queue
                -> worker function processes file
                -> result stored in database
```

## 복잡도 (Complexity)

함수 하나는 단순하지만 event chain 전체는 분산 시스템이다. Retry, idempotency, timeout, poison message 처리가 중요하다.

## 응용 (Applications)

- image thumbnail 생성
- scheduled cleanup job
- webhook handler
- event-driven data pipeline

## 흔한 오해 (Common Misunderstandings)

- 서버리스에도 서버는 있다. 사용자가 직접 관리하지 않을 뿐이다.
- Cold start는 모든 workload에서 무시할 수 있는 문제가 아니다.
- 함수가 작아도 전체 workflow 관찰이 어렵다.
- 무제한 scaling은 downstream database를 과부하시킬 수 있다.

## TMI

- Idempotency key는 retry가 있는 event 처리에서 거의 필수다.
- Provisioned concurrency 같은 기능은 cold start와 비용을 교환한다.
- 서버리스는 cron 대체재로도 많이 쓰인다.

## 연습 / 확인 문제 (Exercises)

- 이미지 업로드 처리 pipeline을 서버리스로 설계하라.
- 중복 event가 와도 안전한 handler 조건을 적어라.
- Cold start가 사용자 경험에 영향을 주는 경우를 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [GCP / Azure 개요](GCP-Azure-Overview.md)
- 다음: [Terraform 기초](Terraform-Basics.md)

## 참조 (References)

- [Systems/Distributed-Systems/Message-Queues-Event-Streaming.md](../../Systems/Distributed-Systems/Message-Queues-Event-Streaming.md)
- [Engineering/DevOps/Distributed-Tracing.md](Distributed-Tracing.md)

