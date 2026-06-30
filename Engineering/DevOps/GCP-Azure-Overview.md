# GCP와 Azure 개요 (GCP / Azure Overview)

- Level: Beginner
- Prerequisites: [Engineering/DevOps/Cloud-Computing.md](Cloud-Computing.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

GCP와 Azure는 AWS와 마찬가지로 compute, storage, database, network, identity, observability를 제공하는 public cloud platform이다.

## 직관 (Intuition)

브랜드와 서비스 이름은 달라도 기본 질문은 비슷하다. 어디에 배치하고, 누가 접근하며, 어떻게 저장하고, 어떻게 관찰하고, 얼마가 드는가다.

## 이론 (Theory)

GCP는 project 중심 자원 경계, VPC, Compute Engine, GKE, Cloud Storage, Cloud SQL, IAM을 제공한다. Azure는 subscription/resource group, VNet, Virtual Machines, AKS, Blob Storage, Azure SQL, Entra ID를 중심으로 설계한다. Cloud마다 IAM 계층, network 기본값, managed Kubernetes 통합, billing 단위가 다르므로 이름 매핑보다 운영 모델 비교가 중요하다.

### Provider 비교의 함정

GCP와 Azure를 비교할 때 서비스 이름을 1:1로 대응시키면 중요한 차이를 놓칠 수 있다. Identity 모델, project/subscription 구조, network boundary, managed Kubernetes 통합, logging/monitoring 기본값, quota 정책이 운영 경험을 바꾼다.

멀티클라우드는 이식성을 높일 수 있지만 가장 낮은 공통분모 설계, 관측 복잡도, IAM 중복, 비용 추적 문제를 만든다. 명확한 실패 시나리오가 있을 때만 선택한다.

## 구현 (Implementation)

```text
concept mapping:
VM: EC2 / Compute Engine / Azure Virtual Machines
Object storage: S3 / Cloud Storage / Blob Storage
Kubernetes: EKS / GKE / AKS
Network: VPC / VPC / VNet
```

## 복잡도 (Complexity)

Multi-cloud는 vendor risk를 줄일 수 있지만 IAM, network, observability, compliance, cost tooling을 중복 운영해야 한다.

## 응용 (Applications)

- managed Kubernetes 선택
- cloud migration 비교
- multi-cloud architecture 검토
- provider-specific managed service 평가

## 흔한 오해 (Common Misunderstandings)

- 서비스 이름이 비슷해도 동작과 제한이 같지는 않다.
- Multi-cloud가 자동으로 고가용성을 보장하지 않는다.
- 추상화 도구만으로 provider 차이가 사라지지 않는다.
- Identity 체계 차이를 뒤늦게 보면 migration 비용이 커진다.

## TMI

- GCP project와 Azure resource group은 비용·권한·수명주기 관리의 핵심 단위다.
- Managed Kubernetes도 node upgrade, workload security, network policy 책임이 남는다.
- Cloud 선택에는 기술뿐 아니라 조직 경험과 지원 체계가 크게 작용한다.

## 연습 / 확인 문제 (Exercises)

- AWS 서비스 5개를 GCP/Azure 대응 서비스와 매핑하라.
- Multi-cloud를 선택할 만한 이유와 피해야 할 이유를 각각 적어라.
- Cloud provider별 identity 경계를 비교하라.

## 이어서 읽기 (Reading Path)

- 이전: [AWS 핵심 서비스](AWS-Core-Services.md)
- 다음: [서버리스](Serverless.md)

## 참조 (References)

- [Engineering/DevOps/Cloud-Computing.md](Cloud-Computing.md)
- [Engineering/DevOps/Kubernetes-Advanced.md](Kubernetes-Advanced.md)
