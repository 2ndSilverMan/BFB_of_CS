# 하이퍼파라미터 튜닝 (Hyperparameter Tuning)

- Level: Intermediate
- Prerequisites: [AI/Machine-Learning/Cross-Validation.md](../Machine-Learning/Cross-Validation.md), [AI/MLOps/Experiment-Tracking.md](Experiment-Tracking.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

하이퍼파라미터 튜닝은 학습으로 직접 추정되지 않는 설정값을 검증 성능과 운영 제약에 맞게 탐색하는 과정이다. Learning rate, regularization, tree depth, batch size, architecture width, preprocessing choice 등이 대표적이다.

## 직관 (Intuition)

모델은 같은 알고리즘이어도 조리법이 달라지면 완전히 다른 결과가 나온다. 튜닝은 가능한 조리법을 무작정 다 먹어 보는 일이 아니라, 비용이 큰 실험을 근거 있게 줄여 가는 탐색이다.

## 이론 (Theory)

탐색 공간, 목적 함수, 예산, 평가 방식이 튜닝 문제를 정의한다. Grid search는 조합을 규칙적으로 훑고, random search는 중요한 축이 적을 때 효율적일 수 있다. Bayesian optimization은 과거 실험으로 surrogate model을 만들고 acquisition function으로 다음 후보를 고른다.

Multi-fidelity 방법은 작은 data, 적은 epoch, 낮은 resolution 같은 저비용 proxy로 후보를 걸러낸다. 하지만 proxy와 최종 성능의 상관이 약하면 좋은 후보를 조기에 버릴 수 있다.

검증 점수는 noise가 있으므로 seed, split, metric variance를 같이 기록해야 한다. Test set은 최종 확인용이고 반복 튜닝의 목적 함수가 되면 leakage가 생긴다.

## 구현 (Implementation)

```python
search_space = {
    "learning_rate": [1e-4, 3e-4, 1e-3],
    "weight_decay": [0.0, 1e-4, 1e-2],
    "batch_size": [32, 64],
}

for config in sample_configs(search_space, budget=20):
    run = train_and_evaluate(config)
    log_run(config=config, metric=run["val_loss"], artifact=run["model"])
```

각 run은 [Experiment-Tracking.md](Experiment-Tracking.md)에 남기고 code, data, seed, environment를 함께 고정한다.

## 복잡도 (Complexity)

Grid search 비용은 각 축 후보 수의 곱으로 증가한다. Random search는 예산 `B`개 실험으로 제한되지만, 넓은 공간에서는 좋은 영역을 놓칠 수 있다. 병렬 실행은 wall time을 줄이지만 GPU, storage, queue, data loader가 병목이 된다.

## 응용 (Applications)

- baseline model 개선
- architecture·optimizer 선택
- serving latency 제약을 포함한 model selection
- AutoML·pipeline search의 기초

## 흔한 오해 (Common Misunderstandings)

- validation 성능만 높이면 운영 모델이 좋아진다는 보장은 없다.
- search space가 엉망이면 좋은 optimizer도 좋은 결과를 만들기 어렵다.
- tuning run을 많이 돌리면 test set에 간접적으로 과적합될 수 있다.
- 단일 seed 최고 점수는 안정적인 개선의 증거가 아니다.

## TMI

- log scale이 자연스러운 값은 선형 grid보다 log-uniform sampling이 낫다.
- early stopping은 튜닝 자체의 hyperparameter가 되기도 한다.
- 실패한 run도 탐색 공간의 위험 신호라서 기록할 가치가 있다.

## 연습 / 확인 문제 (Exercises)

- 특정 모델의 search space와 예산을 설계하라.
- validation variance가 큰 상황에서 후보를 비교하는 기준을 정하라.
- latency 제한이 있는 모델의 tuning objective를 정의하라.

## 이어서 읽기 (Reading Path)

- 이전: [교차 검증](../Machine-Learning/Cross-Validation.md), [실험 추적](Experiment-Tracking.md)
- 다음: [재현 가능성](Reproducibility.md), [모델 레지스트리](Model-Registry.md)

## 참조 (References)

- [AI/Machine-Learning/Cross-Validation.md](../Machine-Learning/Cross-Validation.md)
- [Reference/Books.md](../../Reference/Books.md)
