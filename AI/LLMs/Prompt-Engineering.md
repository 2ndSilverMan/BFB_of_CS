# 프롬프트 엔지니어링 (Prompt Engineering)

- Level: Intermediate
- Prerequisites: [AI/NLP/GPT.md](../NLP/GPT.md), [AI/NLP/Language-Model-Basics.md](../NLP/Language-Model-Basics.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

prompt engineering은 모델 가중치를 바꾸지 않고, 입력 텍스트(prompt)의 구성만으로 LLM의 출력을 원하는 방향으로 유도하는 방법이다. 지시 방식, 예시 제공(few-shot), 추론 유도(chain-of-thought) 등이 포함된다.

## 직관 (Intuition)

사전학습·정렬된 LLM은 이미 많은 능력을 품고 있지만, 어떻게 묻느냐에 따라 그 능력이 발현되는 정도가 달라진다. 좋은 프롬프트는 모델에게 "맥락, 역할, 출력 형식, 풀이 과정"을 분명히 알려 주어 잠재된 능력을 끌어낸다. 학습이 필요 없어 가장 빠르고 싼 적응 수단이다.

## 이론 (Theory)

- **zero-shot**: 지시만 제공. $p_\theta(y \mid \text{instruction}, x)$.
- **few-shot / in-context learning**: 프롬프트에 입력–출력 예시 $k$개를 넣어 패턴을 보여 준다. 가중치 갱신 없이 문맥만으로 과제를 학습하는 것처럼 동작한다.
- **chain-of-thought(CoT)**: "단계별로 생각하자"처럼 중간 추론을 쓰게 유도하면, 다단계 추론 과제 정확도가 오른다.
- **구조화 기법**: 역할 지정, 출력 스키마(JSON) 강제, 구분자 사용, 자기검증(self-consistency: 여러 추론을 샘플링해 다수결).

이 방법들은 모델의 조건부 분포를 좋은 영역으로 옮기는 "조건화"로 볼 수 있다. 능력 자체를 늘리지는 못하지만, 같은 모델에서 더 나은 출력을 끌어낸다.

## 구현 (Implementation)

```text
역할: 너는 꼼꼼한 수학 조교다.
지시: 다음 문제를 단계별로 풀고, 마지막 줄에 "정답:" 뒤에 답만 적어라.

[예시]
문제: 3 + 4 × 2 = ?
풀이: 곱셈 먼저 → 4 × 2 = 8 → 3 + 8 = 11
정답: 11

[실제]
문제: (5 + 1) × 3 = ?
풀이:
```

## 복잡도 (Complexity)

추가 학습 비용이 없다는 것이 최대 장점이다. 비용은 추론 시 토큰 수에 비례하며, few-shot 예시와 CoT는 프롬프트·출력 길이를 늘려 지연·비용을 키운다. self-consistency처럼 여러 번 샘플링하는 기법은 호출 수만큼 비용이 곱해진다.

## 응용 (Applications)

- 빠른 프로토타이핑과 과제 적응(학습 불필요)
- 데이터·추출·분류·요약의 형식 제어
- 복잡 추론(수학·코딩)의 정확도 향상
- 도구 호출·에이전트 워크플로의 행동 지시

## 흔한 오해 (Common Misunderstandings)

- 프롬프트가 모델의 지식·능력 한계를 넘게 해 주지는 않는다. 발현을 도울 뿐이다.
- CoT가 항상 도움이 되지는 않으며, 작은 모델·단순 과제에선 효과가 작거나 역효과일 수 있다.
- few-shot 예시는 형식뿐 아니라 순서·분포에도 민감하다.
- 프롬프트는 모델·버전이 바뀌면 깨지기 쉬워, 안정 운영에는 평가가 필요하다.

## TMI

- "Let's think step by step" 한 줄이 추론 정확도를 끌어올린다는 보고가 CoT 연구를 촉발했다.
- few-shot은 가중치를 바꾸지 않는데도 "학습"처럼 보여 in-context learning이라 불리며, 그 메커니즘은 활발한 연구 주제다.
- prompt injection은 외부 입력이 시스템 지시를 덮어쓰는 보안 문제로, 에이전트 시대에 특히 중요하다.

## 연습 / 확인 문제 (Exercises)

- 같은 과제를 zero-shot과 few-shot으로 작성해 출력 차이를 비교하라.
- CoT가 도움이 되는 과제와 거의 도움이 안 되는 과제를 각각 들어라.
- 출력 형식을 JSON으로 강제하는 프롬프트를 설계하고 실패 사례를 예측하라.

## 이어서 읽기 (Reading Path)

- 이전: [인스트럭션 파인튜닝](Instruction-Tuning.md)
- 다음: [RAG](RAG.md), [In-context Learning](In-Context-Learning.md)

## 참조 (References)

- [AI/NLP/GPT.md](../NLP/GPT.md)
- [AI/LLMs/RAG.md](RAG.md)
- [Reference/Papers.md](../../Reference/Papers.md)
