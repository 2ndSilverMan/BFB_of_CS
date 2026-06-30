# Terraform 기초 (Terraform Basics)

- Level: Intermediate
- Prerequisites: [Engineering/DevOps/Cloud-Computing.md](Cloud-Computing.md), [Engineering/DevOps/Git/Git-Basics.md](Git/Git-Basics.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

Terraform은 provider API를 통해 cloud와 infrastructure resource를 선언형 코드로 관리하는 Infrastructure as Code 도구다.

## 직관 (Intuition)

콘솔에서 손으로 클릭한 결과를 기억하려 하지 않고, 원하는 인프라 상태를 코드로 써서 변경 전 차이를 확인한다.

## 이론 (Theory)

Terraform configuration은 provider, resource, data source, variable, output, module로 구성된다. State는 실제 resource와 configuration의 매핑을 저장하므로 안전하게 관리해야 한다. `plan`은 변경 예측, `apply`는 적용, `destroy`는 제거다. Remote state와 locking은 팀 작업에서 중요하다.

### State와 drift

Terraform의 핵심 자산은 state다. Remote backend, state locking, 접근 제어, secret 노출 방지, 백업이 필수다. 실제 인프라가 수동 변경되면 drift가 생기므로 plan 결과를 정기적으로 확인하고 예외 변경을 코드로 되돌린다.

Module은 재사용을 돕지만 추상화가 과하면 provider의 중요한 의미를 숨긴다. 입력/출력, version constraint, lifecycle rule을 명확히 한다.

## 구현 (Implementation)

```hcl
resource "aws_s3_bucket" "logs" {
  bucket = "example-app-logs"
}
```

```bash
terraform init
terraform plan
terraform apply
```

## 복잡도 (Complexity)

Resource 수와 provider API dependency가 늘수록 plan 시간이 길어지고 drift 가능성이 커진다. Module은 재사용성을 높이지만 추상화 비용을 만든다.

## 응용 (Applications)

- cloud resource provisioning
- network·IAM 정책 관리
- environment 복제
- infrastructure review workflow

## 흔한 오해 (Common Misunderstandings)

- Terraform state에는 민감 정보가 들어갈 수 있다.
- `plan`이 모든 runtime 실패를 보장해 잡지는 못한다.
- 콘솔에서 수동 변경하면 drift가 생긴다.
- `destroy`는 실제 resource 삭제이므로 보호 장치가 필요하다.

## TMI

- Remote backend locking은 동시에 apply하는 사고를 줄인다.
- Import는 기존 resource를 state에 연결하지만 configuration을 자동으로 완성해 주지는 않는다.
- 작은 module부터 시작하고 과한 범용 module을 피하는 편이 유지보수에 좋다.

## 연습 / 확인 문제 (Exercises)

- 간단한 resource를 만들고 plan output을 설명하라.
- State file을 안전하게 보관해야 하는 이유를 적어라.
- Drift가 생겼을 때 대응 절차를 설계하라.

## 이어서 읽기 (Reading Path)

- 이전: [서버리스](Serverless.md)
- 다음: [Ansible](Ansible.md)

## 참조 (References)

- [Engineering/DevOps/Cloud-Computing.md](Cloud-Computing.md)
- [Engineering/DevOps/GitHub/GitHub-Code-Review.md](GitHub/GitHub-Code-Review.md)
