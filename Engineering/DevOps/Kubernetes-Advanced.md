# Kubernetes 고급 (Kubernetes Advanced)

- Level: Advanced
- Prerequisites: [Engineering/DevOps/Kubernetes-Basics.md](Kubernetes-Basics.md), [Systems/Distributed-Systems/System-Models.md](../../Systems/Distributed-Systems/System-Models.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

Kubernetes 고급 주제는 Ingress, HPA, StatefulSet, ConfigMap/Secret, RBAC, rollout 전략처럼 실제 운영에 필요한 controller와 policy를 다룬다.

## 직관 (Intuition)

Pod를 띄우는 것이 시작이라면, 운영은 트래픽을 들이고, 늘리고, 상태를 보존하고, 누가 무엇을 할 수 있는지 정하는 일이다.

## 이론 (Theory)

Ingress는 HTTP routing을 cluster 외부에 노출하고, HPA는 metric에 따라 replica 수를 조정한다. StatefulSet은 stable network identity와 persistent volume claim을 제공해 상태ful workload에 맞다. ConfigMap과 Secret은 image와 설정을 분리한다. RBAC은 service account 권한을 최소화한다. Readiness/liveness probe는 traffic 수신과 재시작 판단을 분리한다.

### 운영 안정성 축

Kubernetes 고급 운영은 object를 더 많이 아는 것보다 failure mode를 제어하는 일이다. Request/limit, readiness/liveness/startup probe, PDB, HPA, rollout strategy, network policy, RBAC, admission control이 서로 맞아야 한다.

Cluster 변경은 workload 변경만큼 위험하다. CRD, controller, CNI, storage class, ingress controller 업그레이드는 staging cluster와 rollback 계획이 필요하다.

## 구현 (Implementation)

```yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: api
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: api
  minReplicas: 2
  maxReplicas: 10
```

## 복잡도 (Complexity)

Controller가 많아질수록 desired state 상호작용을 이해해야 한다. Autoscaling은 metric 지연, startup time, downstream capacity와 함께 조정한다.

## 응용 (Applications)

- production traffic ingress
- stateless service autoscaling
- database·queue 같은 stateful workload
- multi-tenant cluster 권한 관리

## 흔한 오해 (Common Misunderstandings)

- HPA는 resource 부족을 자동으로 모두 해결하지 않는다.
- Secret은 기본적으로 편의 기능이지 완전한 비밀 관리 솔루션이 아니다.
- Liveness probe를 readiness처럼 쓰면 정상 Pod도 재시작될 수 있다.
- StatefulSet이 database 운영을 자동으로 쉽게 만들어 주지는 않는다.

## TMI

- PodDisruptionBudget은 voluntary disruption 중 최소 가용성을 지키는 데 도움을 준다.
- NetworkPolicy는 cluster 내부 통신 경계를 줄인다.
- Operator pattern은 domain-specific controller로 운영 지식을 자동화한다.

## 연습 / 확인 문제 (Exercises)

- readiness와 liveness probe를 서로 다른 조건으로 설계하라.
- HPA metric과 max replica를 정하는 기준을 적어라.
- StatefulSet이 Deployment와 다른 점을 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [Kubernetes 기초](Kubernetes-Basics.md)
- 다음: [Helm](Helm.md)

## 참조 (References)

- [Engineering/DevOps/Kubernetes-Basics.md](Kubernetes-Basics.md)
- [Systems/Distributed-Systems/Replication.md](../../Systems/Distributed-Systems/Replication.md)
