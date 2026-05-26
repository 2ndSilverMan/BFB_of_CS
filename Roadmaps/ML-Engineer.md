# ML 엔지니어 로드맵 (ML Engineer Roadmap)

> 모델 학습부터 배포까지 다루려는 학습자를 위한 순서.

---

## 대상

- 모델 학습, 실험 관리, 서빙, 배포까지 다루려는 학습자

## 현재 가용성

현재 이 로드맵은 ML 엔지니어링 학습 범위와 완료 기준을 제공한다. AI와 운영 인프라 본문은 대부분 `Planned` 상태이므로, 지금은 범위를 파악하고 각 섹션 README에서 `Draft` 이상 문서가 열린 항목부터 읽는다.

## 시작 전 확인

- [AI 핵심 로드맵](AI-Core.md)의 머신러닝과 딥러닝 기본 개념을 알고 있다.
- Python으로 데이터 전처리, 학습, 평가 코드를 실행해 본 적이 있다.
- Docker, API, 모니터링이 낯설다면 MLOps와 함께 [Engineering/DevOps/](../Engineering/DevOps/)를 병행한다.

## 순서

### 기초 도구

1. [프로그래밍 기초](../Programming/)
2. [미적분](../Math/Calculus/)
3. [선형대수](../Math/Linear-Algebra/)
4. [확률과 통계](../Math/Probability-Statistics/)
5. [최적화](../Math/Optimization/)

### AI 핵심

6. [머신러닝](../AI/Machine-Learning/)
7. [딥러닝](../AI/Deep-Learning/)
8. [생성 모델](../AI/Generative-Models/)
9. [대규모 언어 모델 (LLMs)](../AI/LLMs/)

### 모델 운영

10. [MLOps](../AI/MLOps/)
11. [DevOps (Docker, Kubernetes, Cloud)](../Engineering/DevOps/)

### 시스템 설계

12. [시스템 설계](../Engineering/System-Design/)

---

## 완료 기준

- 데이터 수집, 전처리, 학습, 평가, 서빙으로 이어지는 ML 라이프사이클 전체를 코드로 재현할 수 있다.
- 실험 추적, 데이터 버전 관리, 시드 고정으로 결과의 재현 가능성을 확보할 수 있다.
- 모델을 REST/gRPC API로 서빙하고, 온라인/배치 추론의 트레이드오프를 설명할 수 있다.
- 양자화, 프루닝, 지식 증류 중 적절한 기법으로 모델 추론 비용을 줄일 수 있다.
- 데이터 드리프트와 모델 성능 저하를 모니터링하고, 재학습 트리거를 설계할 수 있다.
- Docker/Kubernetes로 학습·서빙 파이프라인을 컨테이너화하고 클라우드에 배포할 수 있다.
- A/B 테스트와 섀도우 배포로 모델 변경을 안전하게 검증할 수 있다.
- 분산 학습(데이터 병렬화/모델 병렬화)이 필요한 시점과 그 비용을 설명할 수 있다.

---

## 다음 단계

- [연구자 로드맵](Researcher.md)

## 관련 로드맵

- [시스템 엔지니어 로드맵](Systems-Engineer.md)
