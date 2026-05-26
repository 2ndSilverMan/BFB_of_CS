# 엔지니어링 (Engineering)

> 소프트웨어를 올바르게 짓고, 운영하고, 지키는 방법.

**선수지식**: [Programming/](../Programming/), [Data-Structures/](../Data-Structures/)

---

## 현재 가용성

현재 이 섹션은 소프트웨어 설계, 운영, 품질, 보안, 성능의 학습 범위를 보여주는 주제 지도다. 개별 본문은 대부분 `Planned` 상태이므로, 각 하위 README에서 `Draft` 이상으로 열린 항목부터 읽는다.

---

## 서브섹션

| 서브섹션 | 내용 | 선수지식 |
|---|---|---|
| [Software-Design/](Software-Design/) | 디자인 패턴, 클린 코드, SOLID, 리팩토링 | [Programming/](../Programming/) |
| [Testing/](Testing/) | 단위 테스트, 통합 테스트, TDD, 테스트 전략 | [Programming/](../Programming/), [Engineering/Software-Design/](Software-Design/) |
| [Debugging/](Debugging/) | 디버깅 전략, 로깅, 트레이싱, 오류 분석 | [Programming/](../Programming/), [Engineering/Testing/](Testing/) |
| [System-Design/](System-Design/) | 대규모 시스템 아키텍처, 로드 밸런싱, 캐싱, 확장성 | [Systems/Networks/](../Systems/Networks/), [Systems/Databases/](../Systems/Databases/) |
| [DevOps/](DevOps/) | Git, CI/CD, Docker, Kubernetes, 클라우드 (AWS/GCP/Azure) | [Systems/Operating-Systems/](../Systems/Operating-Systems/), [Systems/Networks/](../Systems/Networks/) |
| [Performance/](Performance/) | 프로파일링, 벤치마킹, 병목 분석, 메모리 최적화 | [Systems/Computer-Architecture/](../Systems/Computer-Architecture/), [Systems/Operating-Systems/](../Systems/Operating-Systems/) |
| [Security/](Security/) | 실무 보안, 실용 암호학, 인증/인가, 웹 보안 | [Math/Discrete/](../Math/Discrete/), [Systems/Networks/](../Systems/Networks/) |

---

## 학습 순서

```text
Programming → Software-Design → Testing → Debugging

Systems/Networks + Systems/Databases → System-Design
Systems/Operating-Systems + Systems/Networks → DevOps
Systems/Computer-Architecture + Systems/Operating-Systems → Performance

Math/Discrete + Systems/Networks → Security
```

---

## 연관 섹션

- [Systems/](../Systems/) — OS, 네트워크, DB 지식이 Engineering 실무의 기반
- [CS-Theory/Computation-Theory/](../CS-Theory/Computation-Theory/) — 보안의 이론적 기반 (암호학)
- [AI/MLOps/](../AI/MLOps/) — ML 시스템 엔지니어링
