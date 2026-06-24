# AWS 핵심 서비스 (AWS Core Services)

- Level: Beginner
- Prerequisites: [Engineering/DevOps/Cloud-Computing.md](Cloud-Computing.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

AWS 핵심 서비스는 EC2, S3, RDS, VPC, IAM처럼 compute, storage, database, network, identity의 기본 빌딩 블록이다.

## 직관 (Intuition)

EC2는 빌린 서버, S3는 객체 창고, RDS는 관리형 데이터베이스, VPC는 사설 네트워크, IAM은 출입증과 권한표에 가깝다.

## 이론 (Theory)

EC2는 instance type, AMI, security group, EBS volume으로 구성된다. S3는 bucket과 object, versioning, lifecycle, policy를 제공한다. RDS는 backup, replication, patching을 관리형으로 제공하지만 schema와 query 책임은 사용자에게 남는다. VPC는 subnet, route table, internet gateway, NAT gateway, security group으로 network 경계를 만든다. IAM은 user, role, policy로 권한을 제어한다.

## 구현 (Implementation)

```text
minimal web stack:
VPC -> public load balancer -> private EC2/ECS
    -> RDS private subnet
    -> S3 for static assets/backups
    -> IAM roles for workload permissions
```

## 복잡도 (Complexity)

서비스 조합이 많아질수록 IAM, network routing, cost allocation, quota 관리가 중요해진다. Managed service는 운영을 줄이지만 장애 모드와 제한을 이해해야 한다.

## 응용 (Applications)

- 웹 애플리케이션 인프라
- object storage와 backup
- relational database 운영
- private network segmentation

## 흔한 오해 (Common Misunderstandings)

- Security group과 network ACL은 같은 계층의 같은 도구가 아니다.
- S3 bucket 이름은 전역 namespace 특성을 고려해야 한다.
- IAM `*` 권한은 빠르지만 사고 반경을 키운다.
- RDS가 query 최적화까지 대신해 주지는 않는다.

## TMI

- IAM role은 장기 access key보다 workload 권한 부여에 안전한 기본값이다.
- Cost Explorer와 budget alert는 실험 계정에도 필요하다.
- Public subnet은 route가 public일 뿐, 모든 resource가 자동 공개되는 것은 아니다.

## 연습 / 확인 문제 (Exercises)

- EC2, S3, RDS, VPC, IAM을 한 문장씩 설명하라.
- Public/private subnet이 필요한 이유를 정리하라.
- 최소 권한 IAM policy를 설계할 때 확인할 질문을 작성하라.

## 이어서 읽기 (Reading Path)

- 이전: [클라우드 컴퓨팅](Cloud-Computing.md)
- 다음: [GCP / Azure 개요](GCP-Azure-Overview.md)

## 참조 (References)

- [Engineering/DevOps/Cloud-Computing.md](Cloud-Computing.md)
- [Engineering/Security/Auth.md](../Security/Auth.md)

