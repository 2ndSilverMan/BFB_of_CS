# 활성화 패치 (Activation Patching)

- Level: Advanced
- Prerequisites: [AI/AI-Safety/Mechanistic-Interpretability.md](Mechanistic-Interpretability.md), [AI/Causal-Inference/Intervention.md](../Causal-Inference/Intervention.md)
- Status: Draft
- Reviewed-by: -
- Depth: Deep-dive (자기완결)

---

## 개념 (Concept)

Activation patching은 신경망 내부 activation을 다른 입력에서 나온 값으로 바꿔 넣어 특정 layer, head, neuron, feature가 출력에 인과적으로 기여하는지 확인하는 해석 가능성 기법이다.

## 직관 (Intuition)

모델 내부의 특정 부품이 답을 바꾸는지 보려면 그 부품만 교체해 보면 된다. 고장난 회로에서 칩 하나를 정상 칩으로 바꿔 동작이 돌아오는지 보는 식이다.

## 이론 (Theory)

보통 clean input과 corrupted input을 준비한다. Corrupted run의 특정 activation 위치를 clean run activation으로 대체했을 때 정답 logit이나 metric이 회복되면, 그 위치가 관련 계산에 인과적으로 중요하다는 신호다.

Patch granularity는 layer, attention head, MLP neuron, residual stream position 등으로 나뉜다. 단, activation 간 상호작용과 distribution shift 때문에 결과를 과해석하면 안 된다.

### Clean/corrupted pair 설계

좋은 patching 실험은 clean input과 corrupted input이 목표 feature만 다르도록 설계한다. 예를 들어 factual recall에서 clean prompt는 정답을 요구하고, corrupted prompt는 핵심 subject만 바꿔 다른 답을 요구하게 만들 수 있다.

나쁜 pair는 여러 요소가 동시에 바뀐다. 문장 길이, 토큰화, 위치, 문법, 주제 난이도가 함께 바뀌면 patch 효과가 무엇을 의미하는지 모호해진다.

### Metric 선택

Patching 결과는 보통 logit difference로 측정한다.

$$
\Delta = logit(y_{correct}) - logit(y_{distractor})
$$

Patch 후 $\Delta$가 corrupted run보다 clean run에 가까워지면 해당 activation이 목표 계산에 기여한다는 신호다. Classification accuracy처럼 이산 metric만 보면 작은 logit 변화가 가려질 수 있다.

### Patch, ablation, path patching

Activation patching은 clean activation을 넣어 기능을 복원하는 실험이다. Ablation은 component를 제거하거나 평균값으로 바꿔 기능이 사라지는지 본다. Path patching은 특정 sender component에서 receiver component로 가는 경로만 바꿔 회로 연결을 더 좁힌다.

세 방법은 서로 보완적이다. 복원 실험만으로는 충분하지 않고, 제거 실험과 control patch를 함께 봐야 한다.

### Control 실험

과해석을 막기 위해 다음 control이 필요하다.

- 무작위 layer/position patch
- 같은 layer의 무관 token position patch
- 의미는 같지만 표면 형태가 다른 prompt pair
- Patch 값의 norm이나 분포가 비정상적으로 바뀌지 않는지 확인

## 구현 (Implementation)

```python
def patch_activation(corrupted_cache, clean_cache, layer, position):
    corrupted_cache[layer][position] = clean_cache[layer][position]
    return corrupted_cache
```

실제 실험은 patch 전후 logit difference나 task metric 변화를 기록한다.

```python
def patch_effect(clean_metric, corrupted_metric, patched_metric):
    denominator = clean_metric - corrupted_metric
    if abs(denominator) < 1e-12:
        return 0.0
    return (patched_metric - corrupted_metric) / denominator
```

`1.0`에 가까우면 clean performance를 많이 복원한 것이고, `0.0`에 가까우면 patch가 거의 영향을 주지 않은 것이다.

## 복잡도 (Complexity)

Layer×position×component 조합을 모두 탐색하면 비용이 크다. 모델 크기와 sequence length가 커질수록 cache memory도 병목이 된다.

## 응용 (Applications)

- 회로(circuit) 후보 찾기
- 특정 factual recall 경로 분석
- attention head 기능 검증
- safety-relevant feature 추적

## 흔한 오해 (Common Misunderstandings)

- Patch 효과가 있다고 그 component만으로 전체 기능을 설명할 수 있는 것은 아니다.
- Corrupted input 설계가 나쁘면 실험 결론도 흔들린다.
- Activation patching은 상관 분석보다 강하지만 완전한 인과 증명은 아니다.
- Layer 이름과 인간 개념이 일대일로 대응한다고 보면 안 된다.

## TMI

- Path patching은 여러 component 사이 연결 경로를 더 세밀하게 조사한다.
- Logit lens와 patching을 함께 쓰면 어느 층에서 정보가 생기는지 볼 수 있다.
- Activation steering과 patching은 모두 내부 표현 개입이라는 점에서 연결된다.

## 연습 / 확인 문제 (Exercises)

- Clean/corrupted prompt 쌍을 설계하라.
- Patch metric으로 logit difference를 쓰는 이유를 설명하라.
- Patch 결과를 과해석하지 않기 위한 control 실험을 제안하라.

## 이어서 읽기 (Reading Path)

- 이전: [기계적 해석 가능성](Mechanistic-Interpretability.md)
- 다음: [Probing Classifiers](Probing-Classifiers.md), [Sparse Autoencoder](Sparse-Autoencoder.md)

## 참조 (References)

- [AI/AI-Safety/Mechanistic-Interpretability.md](Mechanistic-Interpretability.md)
- [AI/Causal-Inference/Intervention.md](../Causal-Inference/Intervention.md)
- [Reference/Papers.md](../../Reference/Papers.md)
