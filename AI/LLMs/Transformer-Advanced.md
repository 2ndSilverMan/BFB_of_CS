# Transformer 심화 (위치 인코딩, KV 캐시)

- Level: Advanced
- Prerequisites: [AI/Deep-Learning/Transformer.md](../Deep-Learning/Transformer.md), [AI/NLP/Transformer-NLP.md](../NLP/Transformer-NLP.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

대규모 언어 모델 규모에서 Transformer를 실용적으로 만드는 핵심 요소들이다. 위치 정보를 어떻게 넣는지(positional encoding), 생성 시 과거 계산을 어떻게 재사용하는지(KV cache), 긴 context에서 attention 비용을 어떻게 줄이는지를 다룬다.

## 직관 (Intuition)

기본 self-attention은 순서를 모르고, 생성할 때마다 전체 sequence를 다시 계산하면 막대한 낭비가 생긴다. 위치 인코딩은 "몇 번째 토큰인지"를 알려 주고, KV cache는 이미 계산한 key·value를 저장해 새 토큰만 추가로 처리하게 한다. 둘 다 정확도보다 "어떻게 효율적으로 같은 계산을 하느냐"의 문제다.

## 이론 (Theory)

**위치 인코딩.** 절대 위치(sinusoidal/learned)는 임베딩에 위치 벡터를 더한다. 상대 위치 방식이 길이 일반화에 유리하다.

- **RoPE(rotary)**: query·key를 위치각만큼 회전시켜, 내적이 상대 위치 $m-n$에만 의존하게 만든다.
- **ALiBi**: attention score에 거리 비례 음의 bias를 더해 먼 토큰을 덜 보게 한다.

**KV 캐시.** autoregressive 생성에서 step $t$의 attention은 과거 모든 key $K_{1:t}$, value $V_{1:t}$를 필요로 한다. 이를 캐싱하면 각 step은 새 토큰의 $q_t,k_t,v_t$만 계산하면 된다.

**효율적 attention.** 전체 $QK^\top$의 `O(n^2)` 비용을 줄이려 sparse·sliding-window·linear attention을 쓰거나, FlashAttention처럼 메모리 IO를 줄이는 정확 계산을 쓴다.

## 구현 (Implementation)

```python
def generate(model, prompt, max_new):
    kv_cache = None
    tokens = prompt
    for _ in range(max_new):
        # 캐시가 있으면 마지막 토큰만 forward
        logits, kv_cache = model.step(tokens[-1:], kv_cache)
        next_token = sample(logits[-1])
        tokens.append(next_token)
    return tokens
```

## 복잡도 (Complexity)

길이 $n$ sequence를 한 번에 처리하는 full attention은 대략 `O(n^2 d)`다. Autoregressive 생성에서 KV cache가 없으면 매 step마다 prefix 전체를 다시 계산하므로, $n$개 토큰 생성의 누적 attention 비용이 `O(n^3 d)`까지 커질 수 있다. KV cache를 쓰면 과거 key/value를 재사용해 step $t$의 attention을 새 query가 과거 $t$개 key/value를 보는 `O(td)` 수준으로 줄이고, 전체 decode attention 비용은 `O(n^2 d)`가 된다. 대신 cache 메모리는 layer·head·길이·head dimension에 비례해 `O(n)`으로 커지며, 긴 context에서는 이 메모리가 병목이 된다. 효율적 attention은 full attention의 길이 비용이나 메모리 IO를 줄이려는 시도다.

## 응용 (Applications)

- 모든 LLM 추론 엔진의 표준 최적화(KV cache)
- 긴 문서·코드·대화의 long-context 모델
- 실시간 스트리밍 생성에서의 지연 단축
- 메모리 제약 환경의 양자화된 KV cache

## 흔한 오해 (Common Misunderstandings)

- KV cache는 정확도를 바꾸지 않는다. 같은 결과를 더 싸게 계산할 뿐이다.
- context window를 늘리면 메모리·계산이 따라 늘어, 단순히 숫자만 키운다고 공짜가 아니다.
- 상대 위치 인코딩이 무한 길이 일반화를 보장하지는 않는다.
- linear attention이 모든 경우에 정확 attention만큼 성능을 내지는 않는다.

## TMI

- RoPE는 회전 행렬의 성질을 이용해 절대·상대 위치의 장점을 결합한 방식으로 많은 오픈 LLM이 채택했다.
- FlashAttention은 알고리즘 변경이 아니라 GPU 메모리 계층(SRAM/HBM) IO 최적화로 속도를 크게 올렸다.
- KV cache 메모리를 줄이려는 GQA(grouped-query)·MQA(multi-query)는 key/value 헤드를 공유한다.

## 연습 / 확인 문제 (Exercises)

- KV cache가 있을 때와 없을 때 길이 $n$ 생성의 총 attention 계산량을 비교하라.
- 절대 위치 인코딩과 RoPE가 길이 외삽(extrapolation)에서 보이는 차이를 설명하라.
- MQA가 KV cache 메모리를 어떻게 줄이는지 헤드 수 관점에서 논하라.

## 이어서 읽기 (Reading Path)

- 이전: [AI/NLP/Transformer-NLP.md](../NLP/Transformer-NLP.md)
- 다음: [사전학습](Pretraining.md), [어텐션 효율화](Efficient-Attention.md)

## 참조 (References)

- [AI/Deep-Learning/Transformer.md](../Deep-Learning/Transformer.md)
- [AI/LLMs/Pretraining.md](Pretraining.md)
- [Reference/Papers.md](../../Reference/Papers.md)
