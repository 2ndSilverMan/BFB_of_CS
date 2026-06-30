# 기계적 해석 가능성 (Mechanistic Interpretability)

- Level: Advanced
- Prerequisites: [AI/Deep-Learning/Transformer.md](../Deep-Learning/Transformer.md), [AI/Deep-Learning/Attention.md](../Deep-Learning/Attention.md), [AI/Causal-Inference/SCM.md](../Causal-Inference/SCM.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

기계적 해석 가능성은 신경망 내부의 회로, feature, attention head, MLP neuron 등이 어떤 계산을 수행하는지 구체적으로 밝히려는 분야다. 목표는 “모델이 왜 이런 출력을 냈는가”를 단순 상관 설명이 아니라 내부 계산 메커니즘 수준에서 이해하는 것이다.

## 직관 (Intuition)

모델을 거대한 블랙박스로 보지 않고, 회로판처럼 들여다본다고 생각하면 된다. 어떤 부품이 특정 패턴을 감지하고, 어떤 경로가 그 정보를 다음 층으로 보내며, 최종 logit에 어떤 영향을 주는지 추적한다.

## 이론 (Theory)

해석 가능성 연구는 대체로 세 질문을 다룬다.

- 표현: activation space에 어떤 feature가 저장되는가?
- 회로: 여러 component가 어떻게 연결되어 계산을 만드는가?
- 인과성: 특정 activation이나 head를 바꾸면 출력이 실제로 바뀌는가?

대표 도구로 activation patching, logit lens, attribution patching, feature visualization, sparse autoencoder 기반 feature 분해가 있다. 단순히 attention weight가 높다고 중요한 원인이라는 뜻은 아니므로, 인과적 개입과 ablation이 중요하다.

### 설명의 수준

기계적 해석 가능성은 여러 수준의 설명을 구분한다.

- Behavioral: 특정 입력에서 모델이 어떤 출력을 내는가
- Representational: 내부 activation에 어떤 정보가 담겨 있는가
- Circuit-level: component들이 어떤 경로로 계산을 만드는가
- Causal: component를 바꾸면 출력과 metric이 실제로 바뀌는가

안전 연구에서 중요한 것은 마지막 두 수준이다. 단순 probe나 attention heatmap은 가설 생성에는 좋지만, 내부 계산이 그 정보를 사용했다는 증거로는 부족하다.

### 회로 가설의 구성

회로 가설은 "어떤 component가 어떤 정보를 언제 읽고, 어디로 전달하며, 최종 logit에 어떻게 영향을 준다"를 명시해야 한다. 좋은 가설은 다음을 포함한다.

- 입력 조건: 어떤 prompt family에서 작동하는가
- 위치: layer, head, neuron, token position
- 중간 표현: 어떤 feature가 저장되거나 이동하는가
- 출력 metric: logit difference, accuracy, refusal rate 등
- 반례: 어떤 입력에서는 회로가 작동하지 않아야 하는가

이 구조가 없으면 해석 가능성 분석은 흥미로운 시각화 모음에 머물기 쉽다.

### Superposition과 feature

대형 모델은 제한된 차원에 많은 feature를 겹쳐 표현할 수 있다. 그래서 neuron 하나를 사람 언어의 단일 개념으로 해석하면 위험하다. 같은 neuron이 여러 문맥에서 다른 feature 조합의 일부로 쓰일 수 있고, 하나의 feature가 여러 neuron이나 residual direction에 분산될 수도 있다.

SAE, dictionary learning, activation steering은 이 superposition을 풀어 보려는 도구다. 하지만 feature 이름은 항상 가설이며, activation patching이나 causal intervention으로 검증해야 한다.

### 안전 분석에서의 역할

Mechanistic interpretability는 위험 행동을 직접 제거하는 완성된 제품이라기보다, 실패 모드의 원인 후보를 찾는 현미경에 가깝다. 예를 들어 refusal feature, deception 관련 feature, tool-use planning circuit 후보를 찾고, 이를 red-team prompt와 연결해 평가할 수 있다.

## 구현 (Implementation)

개념적으로 activation patching은 깨끗한 입력의 중간 activation을 손상된 입력 실행에 끼워 넣고 출력 복원을 보는 방식이다.

```python
def patch_activation(run_corrupted, clean_cache, layer_name):
    def hook(activation, name):
        if name == layer_name:
            return clean_cache[name]
        return activation

    return run_corrupted(hook=hook)
```

실제 구현은 모델 프레임워크의 hook API, 토큰 위치, layer/component 이름, 평가 metric을 명확히 정해야 한다.

```python
experiment_spec = {
    "hypothesis": "head 7.3 copies the previous matching token",
    "intervention": "patch head output at target position",
    "metric": "logit_difference(correct, distractor)",
    "controls": ["random_patch", "unrelated_position_patch"],
}
```

해석 실험은 가설, 개입, metric, control을 기록해야 재현 가능한 과학 실험이 된다.

## 복잡도 (Complexity)

큰 모델의 모든 component를 실험하면 비용이 매우 크다. 입력 쌍, layer, head, token position을 조합하면 실험 수가 폭발한다. 따라서 작은 모델, 특정 task, 자동화된 attribution, sparse feature 도구를 조합해 탐색한다.

## 응용 (Applications)

- 모델 내부 지식과 회로 분석
- hallucination, refusal, bias 관련 내부 feature 탐색
- 안전 관련 행동의 원인 component 후보 찾기
- 모델 디버깅과 평가 보조

## 흔한 오해 (Common Misunderstandings)

- attention map은 곧 설명이 아니다.
- neuron 하나가 항상 사람 언어의 한 개념에 대응하지는 않는다.
- 해석 가능성 결과는 선택한 입력과 metric에 민감하다.
- 내부 회로를 찾았다고 해서 즉시 안전 제어가 가능해지는 것은 아니다.

## TMI

- superposition은 하나의 neuron 또는 차원이 여러 feature를 겹쳐 표현할 수 있다는 관점이다.
- induction head는 transformer 해석 가능성에서 자주 언급되는 회로 예시다.
- mechanistic interpretability는 과학 실험에 가깝다. 가설, 개입, 재현, 반례 확인이 모두 필요하다.

## 연습 / 확인 문제 (Exercises)

- attention weight 기반 설명과 activation patching 기반 설명의 차이를 설명하라.
- 특정 layer를 ablation했을 때 성능이 떨어지는 것이 충분한 인과 증거인지 논하라.
- 한 task에 대한 회로 가설을 세우고 검증 실험을 설계하라.

## 이어서 읽기 (Reading Path)

- 이전: [RLHF와 Constitutional AI](RLHF-Constitutional-AI.md)
- 다음: [Sparse Autoencoder](Sparse-Autoencoder.md)

## 참조 (References)

- [AI/Deep-Learning/Transformer.md](../Deep-Learning/Transformer.md)
- [AI/Deep-Learning/Attention.md](../Deep-Learning/Attention.md)
- [AI/Causal-Inference/SCM.md](../Causal-Inference/SCM.md)
- [Reference/Books.md](../../Reference/Books.md)
