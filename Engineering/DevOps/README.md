# 데브옵스 (DevOps)

> 개발과 운영을 연결하는 자동화, 컨테이너, 클라우드, 협업 도구.

**선수지식**: [Programming/](../../Programming/), [Systems/Operating-Systems/](../../Systems/Operating-Systems/), [Systems/Networks/](../../Systems/Networks/)

---

## 읽는 법

- 링크가 걸린 `Draft` 이상 문서는 지금 읽을 수 있는 본문이다.
- `Planned` 파일명은 앞으로 채울 예정 주제이며 아직 본문 파일은 없다.

---

## 주제 목록

### 버전 관리와 협업

| 주제 | 파일 | 설명 | Status |
|---|---|---|---|
| Git 학습 트랙 | [Git/](Git/) | 커밋, 브랜치, 원격 저장소, 충돌 해결 | Planned |
| GitHub 학습 트랙 | [GitHub/](GitHub/) | 저장소, 이슈, Pull Request, 코드 리뷰, Actions | Planned |
| Git 내부 구조 | Git-Internals.md | 오브젝트 모델, 팩파일 | Planned |

### CI/CD

| 주제 | 파일 | Status |
|---|---|---|
| CI/CD 개념 — 지속적 통합과 배포의 원칙 | CICD-Principles.md | Planned |
| Jenkins / GitLab CI | Jenkins-GitLab-CI.md | Planned |
| 배포 전략 — Blue-Green, Canary, Rolling | Deployment-Strategies.md | Planned |

### 컨테이너화

| 주제 | 파일 | Status |
|---|---|---|
| Docker 기초 — 이미지, 컨테이너, Dockerfile | Docker-Basics.md | Planned |
| Docker Compose — 멀티 컨테이너 구성 | Docker-Compose.md | Planned |
| 컨테이너 네트워킹과 볼륨 | Container-Networking-Volumes.md | Planned |
| Kubernetes 기초 — Pod, Deployment, Service | Kubernetes-Basics.md | Planned |
| Kubernetes 고급 — Ingress, HPA, StatefulSet | Kubernetes-Advanced.md | Planned |
| Helm — 패키지 관리 | Helm.md | Planned |

### 클라우드

| 주제 | 파일 | Status |
|---|---|---|
| 클라우드 컴퓨팅 개념 — IaaS/PaaS/SaaS | Cloud-Computing.md | Planned |
| AWS 핵심 서비스 — EC2, S3, RDS, VPC | AWS-Core-Services.md | Planned |
| GCP / Azure 개요 | GCP-Azure-Overview.md | Planned |
| 서버리스 — Lambda, Cloud Functions | Serverless.md | Planned |

### Infrastructure as Code

| 주제 | 파일 | Status |
|---|---|---|
| Terraform 기초 — 선언형 인프라 관리 | Terraform-Basics.md | Planned |
| Ansible — 구성 관리 자동화 | Ansible.md | Planned |

### 모니터링 & 관찰 가능성

| 주제 | 파일 | Status |
|---|---|---|
| 로깅 시스템 — ELK Stack, Loki | Logging-Systems.md | Planned |
| 메트릭 & 알람 — Prometheus, Grafana | Metrics-Alerts.md | Planned |
| 분산 트레이싱 — OpenTelemetry, Jaeger | Distributed-Tracing.md | Planned |
| SLI / SLO / SLA 정의 | SLI-SLO-SLA.md | Planned |

---

## 학습 순서

```text
Git → GitHub → CI/CD
         ↓
      Docker → Kubernetes
         ↓
      Cloud (AWS/GCP)
         ↓
      Terraform / Ansible
         ↓
      모니터링 & 관찰 가능성
```

---

## 연관 섹션

- [Systems/Operating-Systems/](../../Systems/Operating-Systems/) — 프로세스, 파일 시스템 (컨테이너 기반)
- [Systems/Operating-Systems/Linux/](../../Systems/Operating-Systems/Linux/) — Linux 셸과 서버 운영 실습
- [Systems/Networks/](../../Systems/Networks/) — 컨테이너 네트워킹, 클라우드 VPC
- [Systems/Distributed-Systems/](../../Systems/Distributed-Systems/) — Kubernetes 이론적 기반
- [Engineering/Performance/](../Performance/) — 배포 후 성능 모니터링
- [AI/MLOps/](../../AI/MLOps/) — ML 파이프라인 운영에서 DevOps 기술 재활용
