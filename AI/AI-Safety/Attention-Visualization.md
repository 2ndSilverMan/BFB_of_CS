# Attention 시각화의 한계 (Limits of Attention Visualization)

- Level: Advanced
- Prerequisites: [AI/Deep-Learning/Attention.md](../Deep-Learning/Attention.md), [AI/AI-Safety/Mechanistic-Interpretability.md](Mechanistic-Interpretability.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

Attention 시각화는 attention weight를 heatmap으로 보여 주어 모델이 어떤 토큰을 참조했는지 직관화하는 방법이다. 하지만 attention weight가 곧 설명이나 인과적 중요도를 의미하지는 않는다.

## 직관 (Intuition)

어떤 사람이 책을 볼 때 시선이 머문 위치가 생각의 전부는 아니다. Attention도 모델 계산의 한 부분일 뿐이며, 높은 weight가 항상 답을 만든 원인이라는 뜻은 아니다.

## 이론 (Theory)

Transformer block은 attention, value vector, MLP, residual stream, layer norm이 결합된다. Attention weight는 value를 섞는 계수지만, value 내용과 후속 layer가 최종 출력에 미치는 영향까지 포함하지 않는다.

따라서 attention heatmap은 탐색 도구로는 유용하지만 explanation으로 쓰려면 ablation, activation patching, gradient, causal mediation 같은 보조 분석이 필요하다.

## 구현 (Implementation)

```python
attention_view = {
    "layer": 10,
    "head": 3,
    "weights": "token_to_token_matrix",
}
```

Head별 기능이 다를 수 있으므로 평균 heatmap만 보는 것은 많은 정보를 잃는다.

## 복잡도 (Complexity)

Attention matrix는 sequence length의 제곱 크기다. 긴 context에서는 시각화 자체가 무거워지고 해석 가능성도 떨어진다.

## 응용 (Applications)

- 모델 내부 탐색
- head 패턴 비교
- 데이터 오류 분석 보조
- 해석 가능성 가설 생성

## 흔한 오해 (Common Misunderstandings)

- Attention이 높은 토큰이 항상 중요한 토큰은 아니다.
- Attention heatmap만으로 편향이나 안전성을 증명할 수 없다.
- Layer/head 평균은 세부 회로를 가릴 수 있다.
- Attention이 낮아도 정보가 residual stream이나 MLP를 통해 전달될 수 있다.

## TMI

- Attention rollout은 여러 layer attention을 합성하려는 방법이지만 여전히 한계가 있다.
- Induction head처럼 attention pattern이 비교적 해석 가능한 사례도 있다.
- Value vector 분석 없이 attention만 보면 "어디를 봤는가"와 "무엇을 가져왔는가"를 분리하지 못한다.

## 연습 / 확인 문제 (Exercises)

- Attention weight와 feature importance의 차이를 설명하라.
- Attention heatmap 해석을 검증할 ablation 실험을 설계하라.
- 긴 context에서 attention visualization이 어려운 이유를 말하라.

## 이어서 읽기 (Reading Path)

- 이전: [Attention](../Deep-Learning/Attention.md)
- 다음: [Activation Patching](Activation-Patching.md)

## 참조 (References)

- [AI/Deep-Learning/Attention.md](../Deep-Learning/Attention.md)
- [Reference/Papers.md](../../Reference/Papers.md)
