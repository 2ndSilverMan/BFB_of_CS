# GPT 계열 (GPT Family)

- Level: Advanced
- Prerequisites: [AI/LLMs/Pretraining.md](Pretraining.md), [AI/NLP/GPT.md](../NLP/GPT.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

GPT 계열은 decoder-only Transformer를 causal language modeling 목표로 사전학습한 autoregressive 언어 모델 계열이다. 이전 토큰을 조건으로 다음 토큰을 예측하며, 생성·요약·코딩·대화 등으로 확장된다.

## 직관 (Intuition)

GPT는 문장을 왼쪽에서 오른쪽으로 이어 쓰는 거대한 자동완성기에서 출발한다. 하지만 충분한 규모와 데이터, 후속 튜닝을 거치면 단순 자동완성을 넘어 지시 수행과 추론처럼 보이는 행동을 보인다.

## 이론 (Theory)

핵심 목표는 다음 토큰 likelihood 최대화다.

$$\max_\theta \sum_t \log p_\theta(x_t\mid x_{<t})$$

Decoder-only 구조는 causal mask로 미래 토큰을 보지 못하게 한다. 규모가 커질수록 in-context learning, tool use, multi-step reasoning 같은 능력이 나타날 수 있지만, 이는 학습 목표·데이터·스케일·튜닝의 상호작용 결과다.

Instruction tuning과 preference optimization은 base GPT를 assistant-like model로 바꾼다.

## 구현 (Implementation)

```python
def causal_mask(seq_len):
    return [[j <= i for j in range(seq_len)] for i in range(seq_len)]
```

생성에서는 temperature, top-p, repetition penalty, stop sequence 같은 decoding 설정이 출력 품질을 크게 바꾼다.

## 복잡도 (Complexity)

학습 비용은 모델 파라미터 수와 토큰 수에 비례해 커진다. 추론은 context 길이, batch, KV cache, decoding step 수에 좌우된다.

## 응용 (Applications)

- 대화형 어시스턴트
- 코드 생성·리팩터링
- 문서 요약·질의응답
- agent와 tool-use 기반 workflow

## 흔한 오해 (Common Misunderstandings)

- GPT 계열이 항상 사실을 알고 말하는 것은 아니다. 다음 토큰 생성과 사실성은 다르다.
- 모델 크기만 키우면 모든 문제가 해결되지는 않는다. 데이터, 튜닝, 평가가 함께 중요하다.
- Base model과 instruction-tuned model은 행동 양식이 다르다.
- Context에 넣었다고 모든 정보를 균등하게 활용하는 것은 아니다.

## TMI

- Decoder-only 구조는 생성과 KV cache에 잘 맞아 LLM 추론에서 널리 쓰인다.
- System/developer/user 같은 역할 구분은 모델 자체 구조보다 사용 인터페이스의 대화 포맷에 가깝다.
- 같은 base model도 SFT와 preference tuning에 따라 성격이 크게 바뀐다.

## 연습 / 확인 문제 (Exercises)

- Causal mask가 필요한 이유를 설명하라.
- Base GPT와 instruction-tuned GPT의 차이를 정리하라.
- Temperature를 높이거나 낮출 때 출력이 어떻게 변하는지 예측하라.

## 이어서 읽기 (Reading Path)

- 이전: [사전학습](Pretraining.md), [GPT](../NLP/GPT.md)
- 다음: [인스트럭션 파인튜닝](Instruction-Tuning.md), [RLHF](RLHF.md)

## 참조 (References)

- [AI/LLMs/Pretraining.md](Pretraining.md)
- [AI/NLP/GPT.md](../NLP/GPT.md)
- [Reference/Papers.md](../../Reference/Papers.md)
