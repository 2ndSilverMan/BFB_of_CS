# 클라우드 컴퓨팅 (Cloud Computing)

- Level: Beginner
- Prerequisites: [Systems/Operating-Systems/Processes-and-Threads.md](../../Systems/Operating-Systems/Processes-and-Threads.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

클라우드 컴퓨팅은 compute, storage, database, network 같은 IT 자원을 필요할 때 API로 생성하고 사용량 기반으로 운영하는 모델이다.

## 직관 (Intuition)

서버를 직접 사서 꽂는 대신, 전기처럼 필요한 만큼 빌리고 줄인다. 대신 비용·권한·네트워크 경계를 계속 설계해야 한다.

## 이론 (Theory)

IaaS는 VM·network·disk 같은 기반 자원을 제공하고, PaaS는 application 실행 플랫폼을 제공하며, SaaS는 완성된 software를 제공한다. Region과 availability zone은 장애 격리 단위다. Shared responsibility model은 cloud provider와 사용자 책임을 나눈다. Elasticity, managed service, IAM, encryption, billing visibility가 핵심 운영 요소다.

### 책임 공유 모델

클라우드는 운영 책임을 없애는 것이 아니라 경계를 바꾼다. Provider는 물리 인프라와 managed service 일부를 책임지고, 사용자는 identity, network policy, data classification, configuration, cost, application security를 책임진다. 서비스마다 책임 경계가 다르므로 아키텍처 문서에 명시한다.

클라우드 설계는 region, availability zone, quota, IAM, backup, observability, cost allocation을 함께 다뤄야 한다.

## 구현 (Implementation)

```text
basic cloud design:
- region / availability zone 선택
- network boundary 설계
- identity and access policy
- compute and database 선택
- backup, monitoring, cost alert
```

## 복잡도 (Complexity)

자원 생성은 쉬워지지만 분산 시스템, 비용, 보안, vendor-specific 설정의 복잡도가 생긴다. Managed service는 운영 부담을 줄이는 대신 제약과 비용 모델을 갖는다.

## 응용 (Applications)

- web service hosting
- data pipeline
- disaster recovery
- globally distributed application

## 흔한 오해 (Common Misunderstandings)

- 클라우드는 자동으로 싸지지 않는다.
- Managed service도 schema, access, backup 책임이 남는다.
- Multi-AZ 배치가 application-level resilience를 자동 보장하지 않는다.
- Public cloud와 public access는 다르다.

## TMI

- Region 선택은 latency, compliance, 서비스 가용성, 비용을 함께 본다.
- Tagging 전략은 비용 분석과 소유권 관리에 큰 도움이 된다.
- Cloud 장애 대응은 provider status보다 내부 dependency map이 먼저 필요하다.

## 연습 / 확인 문제 (Exercises)

- 간단한 웹 서비스의 cloud 구성 요소를 그려라.
- IaaS, PaaS, SaaS 예시를 각각 하나씩 설명하라.
- Shared responsibility model에서 사용자가 맡는 보안 책임을 정리하라.

## 이어서 읽기 (Reading Path)

- 이전: [Helm](Helm.md)
- 다음: [AWS 핵심 서비스](AWS-Core-Services.md)
- 관련: [IP 주소와 라우팅](../../Systems/Networks/IP-and-Routing.md), [분산 시스템 모델](../../Systems/Distributed-Systems/System-Models.md)

## 참조 (References)

- [Systems/Networks/IP-and-Routing.md](../../Systems/Networks/IP-and-Routing.md)
- [Systems/Distributed-Systems/System-Models.md](../../Systems/Distributed-Systems/System-Models.md)
