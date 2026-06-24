# Ansible

- Level: Intermediate
- Prerequisites: [Engineering/DevOps/Terraform-Basics.md](Terraform-Basics.md), [Systems/Operating-Systems/Linux/Linux-Shell-Basics.md](../../Systems/Operating-Systems/Linux/Linux-Shell-Basics.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

Ansible은 inventory에 있는 host에 SSH 등으로 접속해 playbook에 정의된 task를 실행하는 구성 관리 자동화 도구다.

## 직관 (Intuition)

서버마다 손으로 같은 명령을 치지 않고, “이 서버들은 이런 상태여야 한다”는 절차를 재사용 가능한 문서로 실행한다.

## 이론 (Theory)

Inventory는 대상 host와 group을 정의하고, playbook은 play와 task 목록을 담는다. Module은 package 설치, file 배치, service 재시작 같은 작업을 idempotent하게 수행한다. Variable, role, handler로 재사용성과 구조를 높인다. Terraform이 resource provisioning에 강하다면 Ansible은 OS와 application configuration에 강하다.

## 구현 (Implementation)

```yaml
- hosts: web
  become: true
  tasks:
    - name: install nginx
      ansible.builtin.package:
        name: nginx
        state: present
```

## 복잡도 (Complexity)

Host 수가 늘수록 병렬 실행, SSH 연결, inventory 관리, secret 배포가 중요해진다. Playbook이 imperative script처럼 변하면 idempotency를 잃는다.

## 응용 (Applications)

- package와 service 구성
- config file 배포
- one-off maintenance task
- immutable image 전환 전 기존 서버 관리

## 흔한 오해 (Common Misunderstandings)

- Ansible task가 모두 자동으로 idempotent한 것은 아니다. 사용하는 module과 command 설계가 중요하다.
- Secret을 plain YAML에 두면 안 된다.
- Terraform과 Ansible은 경쟁보다 역할 분리가 자연스러운 경우가 많다.
- 수동 hotfix를 계속 허용하면 playbook과 실제 서버가 어긋난다.

## TMI

- Handler는 변경이 발생했을 때만 service restart 같은 작업을 실행한다.
- Ansible Vault는 secret 암호화에 쓰인다.
- Dynamic inventory는 cloud resource를 inventory로 자동 가져오는 데 유용하다.

## 연습 / 확인 문제 (Exercises)

- Nginx 설치와 설정 파일 배포 playbook을 작성하라.
- Handler가 필요한 상황을 설명하라.
- Terraform과 Ansible의 책임 경계를 나눠라.

## 이어서 읽기 (Reading Path)

- 이전: [Terraform 기초](Terraform-Basics.md)
- 다음: [로깅 시스템](Logging-Systems.md)

## 참조 (References)

- [Systems/Operating-Systems/Linux/Linux-Shell-Basics.md](../../Systems/Operating-Systems/Linux/Linux-Shell-Basics.md)
- [Engineering/DevOps/Terraform-Basics.md](Terraform-Basics.md)

