# 인스트럭션 파인튜닝 (Instruction Tuning)

- Level: Advanced
- Prerequisites: [AI/LLMs/Pretraining.md](Pretraining.md), [AI/Deep-Learning/Fine-Tuning.md](../Deep-Learning/Fine-Tuning.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

instruction tuning은 사전학습된 언어 모델을 "지시(instruction)–응답" 형식의 데이터로 추가 학습해, 자연어 지시를 따르도록 만드는 단계다. 흔히 지도 학습(SFT) 후, 사람 선호를 반영하는 선호 최적화(RLHF, DPO)로 이어진다.

## 직관 (Intuition)

사전학습 모델은 "다음 단어"를 잘 맞히지만, 사용자가 원하는 것은 보통 "이 질문에 답해 줘", "이걸 요약해 줘" 같은 지시 수행이다. 다양한 지시–응답 예시를 보여 주면, 모델은 단순 이어쓰기 대신 "지시를 받아 수행한다"는 행동 양식을 학습한다. 이어 사람 선호 신호로 더 도움이 되고 안전한 응답 쪽으로 미세 조정한다.

## 이론 (Theory)

**SFT(supervised fine-tuning).** 지시 $x$에 대한 바람직한 응답 $y$의 토큰을 그대로 예측하도록 cross-entropy로 학습한다. 핵심은 과제 다양성과 데이터 품질이다.

**RLHF.** 사람이 매긴 응답 비교로 reward model $r_\phi(x,y)$를 학습하고, 정책 $\pi_\theta$를 그 보상에 맞춰 강화학습(보통 PPO)으로 최적화한다. 사전학습 정책에서 멀어지지 않도록 KL 패널티를 둔다.

$$\max_\theta\ \mathbb{E}_{x,\,y\sim\pi_\theta}\big[r_\phi(x,y)\big]-\beta\,\mathrm{KL}\!\big(\pi_\theta(\cdot\mid x)\,\|\,\pi_{\text{ref}}(\cdot\mid x)\big)$$

**DPO(direct preference optimization).** 별도 reward model과 RL 루프 없이, 선호쌍 $(y^+,y^-)$에서 직접 정책을 최적화하는 분류 형태의 손실을 쓴다. 구현이 단순하고 안정적이라 널리 쓰인다.

## 구현 (Implementation)

```python
# SFT: 지시-응답 쌍의 응답 토큰에 대한 손실 (개념)
def sft_loss(model, instruction, response):
    ids = tokenize(instruction + response)
    logits = model(ids[:-1])
    targets = ids[1:]
    mask = response_token_mask(instruction, response)  # 응답 부분만 학습
    return masked_cross_entropy(logits, targets, mask)
```

## 복잡도 (Complexity)

SFT는 사전학습보다 훨씬 적은 데이터·계산으로 끝난다(전체 또는 PEFT로). RLHF는 reward model 학습 + 온라인 샘플링 + RL 업데이트로 파이프라인이 복잡하고 불안정할 수 있다. DPO는 RL 루프가 없어 SFT에 가까운 비용·안정성을 가진다.

## 응용 (Applications)

- 대화형 어시스턴트의 지시 수행 능력 부여
- 도메인 특화(코드, 의료, 고객 응대) 지시 적응
- 안전성·정책 준수 응답 정렬(alignment)
- 평가·심사 등 특정 출력 형식 강제

## 흔한 오해 (Common Misunderstandings)

- instruction tuning이 새 지식을 크게 주입하지는 않는다. 주로 "행동·형식"을 바꾼다.
- RLHF가 모델을 "진실하게" 만든다고 단정할 수 없다. 사람 선호를 근사할 뿐이다.
- 데이터 양보다 다양성·품질이 중요하며, 소량의 고품질 데이터가 효과적인 경우가 많다.
- DPO가 RLHF를 항상 대체하지는 않지만, 많은 경우 더 간단히 비슷한 효과를 낸다.

## TMI

- "alignment tax"라는 표현은 정렬 과정에서 일부 능력(예: 특정 벤치마크 점수)이 다소 떨어질 수 있음을 가리킨다.
- 소량 고품질 SFT만으로도 상당한 지시 수행이 가능하다는 관찰(이른바 LIMA류)이 데이터 품질론에 힘을 실었다.
- reward hacking은 모델이 진짜 의도 대신 보상 신호의 허점을 노리는 현상으로 RLHF의 대표적 위험이다.

## 연습 / 확인 문제 (Exercises)

- SFT와 RLHF가 각각 모델의 무엇을 바꾸는지 구분해 설명하라.
- RLHF 목적식의 KL 패널티가 빠지면 어떤 문제가 생길지 논하라.
- DPO가 reward model을 명시적으로 두지 않고도 선호를 반영할 수 있는 직관을 설명하라.

## 이어서 읽기 (Reading Path)

- 이전: [사전학습](Pretraining.md)
- 다음: [RLHF](RLHF.md), [DPO](DPO.md), [프롬프트 엔지니어링](Prompt-Engineering.md)

## 참조 (References)

- [AI/LLMs/Pretraining.md](Pretraining.md)
- [AI/Deep-Learning/Fine-Tuning.md](../Deep-Learning/Fine-Tuning.md)
- [Reference/Papers.md](../../Reference/Papers.md)
