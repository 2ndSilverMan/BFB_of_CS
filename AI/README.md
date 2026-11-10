# 인공지능 (Artificial Intelligence)

> 탐색·지식표현·추론·계획·학습을 통해 지능적 과제를 해결하는 방법. 현재 자료는 ML·딥러닝 중심이다.

**선수지식**: [Programming/](../Programming/), [Math/Linear-Algebra/](../Math/Linear-Algebra/), [Math/Probability-Statistics/](../Math/Probability-Statistics/), [Math/Calculus/](../Math/Calculus/), [Math/Optimization/](../Math/Optimization/)

---

## 현재 가용성

등록된 주제는 `Draft` 이상 본문이 있으며 각 하위 README에서 찾을 수 있다. 다만 고전 탐색·지식표현·계획·CSP·로보틱스 등의 체계적인 본문이 부족하므로 AI 전체 범위가 확보된 것은 아니다. 공백은 [전체 지식 범위](../Maintainers/Curriculum-Coverage.md), 직접 출처와 재작성 메모는 [전체 자료 목록](../Maintainers/Preparation-Inventory.md)에서 확인한다.

---

## 서브섹션

### 핵심

| 서브섹션 | 내용 | 선수지식 |
|---|---|---|
| [Machine-Learning/](Machine-Learning/) | 지도학습, 비지도학습, 모델 평가, 정규화 | [Programming/](../Programming/), [Math/Linear-Algebra/](../Math/Linear-Algebra/), [Math/Probability-Statistics/](../Math/Probability-Statistics/) |
| [Deep-Learning/](Deep-Learning/) | 신경망, 역전파, CNN, RNN, Transformer 기초 | [AI/Machine-Learning/](Machine-Learning/), [Math/Calculus/](../Math/Calculus/), [Math/Optimization/](../Math/Optimization/) |

### 응용 분야

| 서브섹션 | 내용 | 선수지식 |
|---|---|---|
| [NLP/](NLP/) | 텍스트 처리, 임베딩, 언어 모델 | [AI/Deep-Learning/](Deep-Learning/) |
| [Computer-Vision/](Computer-Vision/) | 이미지 분류, 객체 탐지, 세그멘테이션 | [AI/Deep-Learning/](Deep-Learning/) |
| [Reinforcement-Learning/](Reinforcement-Learning/) | MDP, Q-러닝, Policy Gradient | [AI/Machine-Learning/](Machine-Learning/), [Math/Probability-Statistics/](../Math/Probability-Statistics/) |
| [Generative-Models/](Generative-Models/) | VAE, GAN, Diffusion Model | [AI/Deep-Learning/](Deep-Learning/) |
| [LLMs/](LLMs/) | GPT 계열, BERT, 프롬프트 엔지니어링, RLHF | [AI/NLP/](NLP/), [AI/Deep-Learning/](Deep-Learning/) |

### 심화 이론

| 서브섹션 | 내용 | 선수지식 |
|---|---|---|
| [Theoretical-ML/](Theoretical-ML/) | PAC 학습, VC 차원, 일반화 이론 | [AI/Machine-Learning/](Machine-Learning/), [Math/Real-Analysis/](../Math/Real-Analysis/) |
| [PGMs/](PGMs/) | 베이지안 네트워크, 마르코프 랜덤 필드 | [Math/Probability-Statistics/](../Math/Probability-Statistics/), [Math/Discrete/](../Math/Discrete/) (그래프 이론) |
| [Causal-Inference/](Causal-Inference/) | 인과 그래프, 개입, 반사실 | [Math/Probability-Statistics/](../Math/Probability-Statistics/), [AI/PGMs/](PGMs/) |
| [AI-Safety/](AI-Safety/) | 정렬 문제, 해석 가능성, 강건성 | [AI/Deep-Learning/](Deep-Learning/), [AI/Theoretical-ML/](Theoretical-ML/) |

### 엔지니어링

| 서브섹션 | 내용 | 선수지식 |
|---|---|---|
| [MLOps/](MLOps/) | 실험 관리, 모델 서빙, 모니터링, 파이프라인 | [AI/Machine-Learning/](Machine-Learning/), [Systems/](../Systems/), [Engineering/DevOps/](../Engineering/DevOps/) |

---

## 학습 순서

```text
프로그래밍 + 선형대수 + 확률/통계 + 미적분 + 최적화
                  ↓
        Machine-Learning
            ↓         ↘
      Deep-Learning   Reinforcement-Learning
      ↙   ↓   ↘                ↓
    NLP   CV   Generative-Models
     ↓     ↘   ↙
    LLMs ← (RLHF: RL을 LLM 정렬에 적용)
     ↓
    MLOps (배포 단계)

확률/통계 + 이산수학 → PGMs → Causal-Inference
실해석학 + ML → Theoretical-ML → AI-Safety
```

- **RLHF**는 강화학습 전체를 선수로 요구하지 않는다. Policy Gradient / PPO 정도의 핵심만 알면 LLM 정렬에 적용 가능.
- **Generative-Models**는 이미지 생성(GAN/Diffusion)과 텍스트 생성(LLM)의 공통 기반이라 LLMs로도 연결된다.

---

## 연관 섹션

- [Math/](../Math/) — 선수 수학 전체
- [Systems/](../Systems/) — MLOps 인프라 기반
- [Engineering/](../Engineering/) — 모델 서빙, 시스템 설계
