# 어텐션 효율화 (Efficient Attention)

- Level: Advanced
- Prerequisites: [AI/LLMs/Transformer-Advanced.md](Transformer-Advanced.md), [Engineering/Performance/Benchmarking-Basics.md](../../Engineering/Performance/Benchmarking-Basics.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

어텐션 효율화는 self-attention의 계산·메모리 비용을 줄여 긴 context와 빠른 추론을 가능하게 하는 기법이다. Flash Attention, sparse/sliding attention, MQA/GQA, linear attention 등이 있다.

## 직관 (Intuition)

기본 attention은 모든 토큰이 모든 토큰을 보게 해서 길이가 길어질수록 표가 제곱으로 커진다. 효율화는 표를 더 똑똑하게 계산하거나, 꼭 봐야 할 칸만 보거나, 저장할 내용을 줄이는 방식이다.

## 이론 (Theory)

정확 attention은 $QK^\top$와 softmax, $V$ 가중합을 계산한다. Flash Attention은 수학적으로 같은 결과를 유지하면서 GPU memory IO를 줄인다. Sparse attention은 local window, block pattern, global token으로 attention graph를 제한한다.

MQA/GQA는 query head는 여러 개 유지하되 key/value head를 공유해 KV cache memory를 줄인다.

## 구현 (Implementation)

```python
costs = {
    "full_attention": "O(n^2)",
    "sliding_window": "O(n * window)",
    "kv_cache_memory": "layers * length * kv_heads * head_dim",
}
```

효율화는 throughput, latency, memory, 품질을 함께 측정해야 한다.

## 복잡도 (Complexity)

Full attention은 sequence length $n$에 대해 메모리와 연산이 대체로 `O(n^2)`다. Sparse/window 방식은 pattern에 따라 `O(nw)`로 줄일 수 있지만 장거리 의존성 손실이 생길 수 있다.

## 응용 (Applications)

- long-context LLM
- 실시간 serving
- 긴 코드·문서 처리
- edge device 추론 최적화

## 흔한 오해 (Common Misunderstandings)

- Flash Attention은 approximate attention이 아니라 정확 계산의 IO 최적화다.
- Sparse attention은 모든 task에서 품질을 보장하지 않는다.
- KV cache를 줄이면 memory는 줄지만 모델 구조와 품질 tradeoff가 생길 수 있다.
- Benchmark는 batch size와 sequence length를 고정해야 비교가 된다.

## TMI

- Attention 최적화는 FLOPs보다 HBM↔SRAM memory movement가 병목인 경우가 많다.
- Long-context 모델은 위치 인코딩과 학습 데이터 길이도 함께 고려해야 한다.
- Paged attention은 serving에서 KV cache memory fragmentation을 줄이는 아이디어다.

## 연습 / 확인 문제 (Exercises)

- Full attention과 sliding-window attention의 계산량을 비교하라.
- Flash Attention이 빠른 이유를 메모리 IO 관점에서 설명하라.
- MQA/GQA가 KV cache를 줄이는 방식을 헤드 수로 계산하라.

## 이어서 읽기 (Reading Path)

- 이전: [Transformer Advanced](Transformer-Advanced.md)
- 다음: [Quantization](Quantization.md), [Inference Optimization](Inference-Optimization.md)

## 참조 (References)

- [AI/LLMs/Transformer-Advanced.md](Transformer-Advanced.md)
- [Engineering/Performance/Benchmarking-Basics.md](../../Engineering/Performance/Benchmarking-Basics.md)
- [Reference/Papers.md](../../Reference/Papers.md)
