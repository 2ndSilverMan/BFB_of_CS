# 연구자 로드맵 (Researcher Roadmap)

> 분야별 연구 접근을 고르고 문헌·주장·증거·한계를 연결하는 안내서.

---

## 대상

- 어느 CS/컴퓨터공학 분야에서든 연구를 시작하려는 학습자.
- **전제**: 선택 분야의 핵심 개념. AI·딥러닝은 모든 연구자의 선수지식이 아니다.

## 현재 가용성

아래 분야별 시작 자료와 기존 AI 이론 분기에는 `Draft` 이상 본문이 있다. [공통 연구 방법](../Research-Practice/), HCI·하드웨어 등의 새 전용 주제는 `Planned`다. 분야별 연구 교육이 완성됐다는 뜻은 아니며, [전체 지식 범위](../Maintainers/Curriculum-Coverage.md)와 [자료 목록](../Maintainers/Preparation-Inventory.md)에서 공백을 확인한다.

## 순서

1. [분야별 경로](Domain-Paths.md)에서 문제와 필요한 선수지식을 고른다.
2. [연구 실무](../Research-Practice/)의 목표에 따라 문헌 비교표에 질문·가정·방법·증거·한계를 기록한다. 공통 방법의 전용 본문은 아직 Planned다.
3. 아래에서 문제에 적합한 방법을 고른다. 모든 연구를 통계 실험으로 환원하지 않는다.
4. 작은 증명 검산·재현·설계 평가를 수행하고 확인한 범위와 실패를 남긴다.

| 분야 | 현재 시작 자료 | 연구에서 확인할 것 | 추가 확보할 것 |
|---|---|---|---|
| 이론·알고리즘 | [계산 이론](../CS-Theory/Computation-Theory/), [알고리즘](../Algorithms/) | 정의·가정·증명·반례·환원의 방향 | 논문 증명 읽기와 하한 분석 사례 |
| 시스템·데이터 | [분산](../Systems/Distributed-Systems/), [DB](../Systems/Databases/), [성능](../Engineering/Performance/) | 워크로드·비교군·측정 오차·실패 모델 | 재현 가능한 실험과 타당성 분석 |
| 언어·보안·공학 | [언어론](../CS-Theory/Programming-Languages/), [보안](../Engineering/Security/), [테스트](../Engineering/Testing/) | 의미 보존·위협 모델·관측 범위 | 검증·분석 도구와 실증 연구 방법 |
| 하드웨어·그래픽스 | [구조](../Systems/Computer-Architecture/), [선형대수](../Math/Linear-Algebra/) | 타이밍·물리 가정·영상 오차·자원 비용 | [하드웨어](../Hardware-and-Embedded/)와 [그래픽스](../Graphics-and-Interaction/Graphics/) 전용 본문 |
| HCI·교육·사회 | [통계](../Math/Probability-Statistics/), [사회 계획](../Computing-and-Society/) | 참여자 권리·표집·질적/양적 근거·해석 | [HCI](../Graphics-and-Interaction/HCI/)와 [교육](../Teaching-and-Academia/) 전용 본문 |
| AI | 아래 기존 AI 이론 분기, [AI](../AI/) | 데이터·기준선·학습/평가 분리·가정 | 비ML AI와 문제별 연구 방법 |

## 공통 확인 목표

- 논문 기여와 선행 연구를 구분하고 주장마다 근거와 한계를 표시한다.
- 문제에 맞게 증명·실험·관찰·설계 평가를 선택하고 타당성 위협을 설명한다.
- 자신의 기록으로 무엇을 재현·검산했는지, 무엇은 확인하지 못했는지 구분한다.
- 연구 산출물의 출처·권리·기여를 기록한다. 실제 사람 검토나 참여자 연구를 했다고 허위 표시하지 않는다.

## 선택 분기: AI 이론

아래는 기존 AI 중심 순서를 보존한 선택 경로다. 이 분기만 [AI-Core](AI-Core.md)의 ML·딥러닝 지식을 전제로 한다.

### 수학 기반

1. [실해석학](../Math/Real-Analysis/)
   - 수렴, 연속성, 측도론 — 이론 ML의 수학적 언어
2. [확률과 통계](../Math/Probability-Statistics/)
   - 확률 측도, 분포, 정보 이론
3. [최적화](../Math/Optimization/)
   - 볼록 최적화, 쌍대 이론

### CS 이론

4. [계산 이론](../CS-Theory/Computation-Theory/)
   - 복잡도 클래스, 환원, 하한 증명

### AI 이론

5. [이론적 머신러닝](../AI/Theoretical-ML/)
   - PAC 학습, VC 차원, 일반화 경계
6. [확률 그래프 모델](../AI/PGMs/)
   - 베이지안 네트워크, 추론 알고리즘
7. [인과 추론](../AI/Causal-Inference/)
   - 인과 그래프, do-calculus, 반사실
8. [AI 안전성](../AI/AI-Safety/)
   - 정렬 문제, 해석 가능성, 강건성

---

## AI 이론 분기의 완료 기준

- 최근 5년 내 분야 대표 논문을 읽고 핵심 기여, 가정, 한계를 자기 말로 요약할 수 있다.
- 측도론적 확률, 수렴, 함수 공간의 언어로 학습 이론 페이퍼를 따라 읽을 수 있다.
- PAC 학습, VC 차원, Rademacher 복잡도를 이용해 일반화 경계를 해석할 수 있다.
- 베이지안 네트워크와 MRF의 인수 분해, 추론 알고리즘(VE, BP, MCMC, VI)을 비교할 수 있다.
- do-calculus와 잠재 결과 프레임워크로 관찰 데이터로부터 인과 효과를 식별할 수 있는지 판단할 수 있다.
- 정렬 문제, 보상 해킹, 해석 가능성, 강건성 연구 흐름을 구분해서 설명할 수 있다.
- 새로운 가설을 작은 실험으로 설계하고, 결과를 통계적으로 검증할 수 있다.
- 자신의 연구 주제와 관련된 최소 한 편의 노트 또는 재현 실험을 공개할 수 있다.

---

## 관련 자료

- [추천 논문 목록](../Reference/Papers.md)
