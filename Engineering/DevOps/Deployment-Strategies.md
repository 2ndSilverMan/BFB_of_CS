# 배포 전략 (Deployment Strategies)

- Level: Intermediate
- Prerequisites: [Engineering/DevOps/CICD-Principles.md](CICD-Principles.md), [Engineering/Debugging/Canary-Feature-Flags.md](../Debugging/Canary-Feature-Flags.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

배포 전략은 새 버전을 사용자에게 노출하는 순서와 실패 시 되돌리는 방식을 정하는 운영 설계다.

## 직관 (Intuition)

한 번에 모든 문을 열지, 옆 건물로 바꿔 탈지, 일부 손님에게만 먼저 보여 줄지 결정하는 일이다.

## 이론 (Theory)

Rolling 배포는 instance를 조금씩 교체한다. Blue-green은 구버전과 신버전 환경을 나란히 두고 traffic switch로 전환한다. Canary는 작은 사용자·traffic 비율부터 시작해 metric을 보며 확대한다. Feature flag는 배포와 기능 노출을 분리한다. 모든 전략은 health check, rollback, database migration 호환성을 함께 고려해야 한다.

## 구현 (Implementation)

```text
canary rollout:
1% traffic -> error rate 확인 -> 10% -> 50% -> 100%
```

각 단계에는 자동 중단 조건과 담당자 승인 조건을 둔다.

## 복잡도 (Complexity)

안전한 전략일수록 infrastructure와 observability 요구가 커진다. Blue-green은 비용이 늘고, canary는 traffic routing과 metric 해석이 필요하다.

## 응용 (Applications)

- web service release
- mobile backend compatibility rollout
- database migration 배포
- ML model serving rollout

## 흔한 오해 (Common Misunderstandings)

- Blue-green은 database schema 변경을 자동 해결하지 않는다.
- Canary는 metric이 좋아야 의미가 있다.
- Rollback은 deploy 버튼보다 먼저 설계해야 한다.
- Feature flag를 방치하면 코드 복잡도가 쌓인다.

## TMI

- Expand-contract migration은 구버전과 신버전이 모두 동작하도록 schema를 단계적으로 바꾼다.
- Dark launch는 기능을 노출하지 않고 backend 경로만 미리 태운다.
- 배포 실패의 상당수는 코드보다 config와 dependency 차이에서 온다.

## 연습 / 확인 문제 (Exercises)

- 특정 API 변경을 rolling 배포하려면 어떤 호환성이 필요한지 정리하라.
- Canary 중단 기준을 error rate와 latency로 정의하라.
- Feature flag 제거 시점을 release checklist에 넣어라.

## 이어서 읽기 (Reading Path)

- 이전: [Jenkins / GitLab CI](Jenkins-GitLab-CI.md)
- 다음: [Docker 기초](Docker-Basics.md)

## 참조 (References)

- [Engineering/Debugging/Canary-Feature-Flags.md](../Debugging/Canary-Feature-Flags.md)
- [Engineering/DevOps/Metrics-Alerts.md](Metrics-Alerts.md)

