# Helm

- Level: Intermediate
- Prerequisites: [Engineering/DevOps/Kubernetes-Basics.md](Kubernetes-Basics.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

Helm은 Kubernetes manifest를 chart라는 패키지로 묶고, values로 환경별 설정을 주입하며, release 단위로 설치·업그레이드·롤백하는 도구다.

## 직관 (Intuition)

반복해서 붙여 넣는 YAML 묶음을 설치 가능한 앱 패키지로 만든다. 같은 chart에 개발·스테이징·운영 values만 다르게 넣는다.

## 이론 (Theory)

Chart는 templates, values.yaml, Chart.yaml로 구성된다. Template은 Go template 문법으로 rendering되고, release는 cluster에 설치된 chart instance다. `helm upgrade --install`은 없으면 설치하고 있으면 갱신한다. Chart version과 app version을 구분하고, values schema와 lint로 실수를 줄인다.

## 구현 (Implementation)

```bash
helm create api
helm lint api
helm template api -f values-dev.yaml
helm upgrade --install api ./api -f values-prod.yaml
```

배포 전 `helm template` 결과를 확인하면 실제 적용될 manifest를 검토할 수 있다.

## 복잡도 (Complexity)

Template가 복잡해질수록 재사용성은 늘지만 읽기 어려워진다. 환경별 values가 많으면 drift와 secret 관리 문제가 생긴다.

## 응용 (Applications)

- Kubernetes application packaging
- 환경별 manifest 재사용
- dependency chart 설치
- release rollback

## 흔한 오해 (Common Misunderstandings)

- Helm chart는 나쁜 Kubernetes 설계를 자동으로 좋게 만들지 않는다.
- Template에 로직을 과도하게 넣으면 디버깅이 어려워진다.
- Secret values를 평문 repository에 두면 안 된다.
- Chart version과 container image tag를 혼동하면 release 추적이 어려워진다.

## TMI

- Helm hooks는 migration job 등에 쓰이지만 실패 처리와 재실행 정책이 중요하다.
- OCI registry에 chart를 저장할 수 있다.
- Kustomize는 template보다 patch와 overlay에 초점을 둔 다른 접근이다.

## 연습 / 확인 문제 (Exercises)

- Deployment와 Service를 chart로 만들고 values로 image tag를 바꾸라.
- `helm template` 출력과 실제 manifest를 비교하라.
- rollback이 안전하려면 database migration이 어떻게 설계되어야 하는지 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [Kubernetes 고급](Kubernetes-Advanced.md)
- 다음: [클라우드 컴퓨팅](Cloud-Computing.md)

## 참조 (References)

- [Engineering/DevOps/Kubernetes-Advanced.md](Kubernetes-Advanced.md)
- [Engineering/DevOps/Deployment-Strategies.md](Deployment-Strategies.md)

