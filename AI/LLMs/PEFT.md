# 효율적 파인튜닝 (PEFT: LoRA, QLoRA, Adapter)

- Level: Advanced
- Prerequisites: [AI/Deep-Learning/Fine-Tuning.md](../Deep-Learning/Fine-Tuning.md), [AI/LLMs/Instruction-Tuning.md](Instruction-Tuning.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

PEFT(Parameter-Efficient Fine-Tuning)는 거대한 모델 전체를 업데이트하지 않고 작은 추가 파라미터나 저랭크 업데이트만 학습해 비용을 줄이는 방법이다. LoRA, Adapter, prefix tuning, QLoRA 등이 대표적이다.

## 직관 (Intuition)

두꺼운 교과서 전체를 다시 쓰는 대신, 중요한 페이지에 포스트잇과 수정 테이프를 붙여 특정 과제에 맞춘다. 원본 모델 대부분은 고정하고 작은 변화만 학습한다.

## 이론 (Theory)

LoRA는 가중치 업데이트 $\Delta W$를 저랭크 행렬 $BA$로 근사한다. Rank가 작으면 학습 파라미터와 메모리가 크게 줄어든다. Adapter는 layer 사이에 작은 bottleneck module을 삽입한다.

QLoRA는 base model을 양자화해 메모리를 줄이고 LoRA adapter만 학습한다. PEFT는 여러 task adapter를 교체하기 쉬운 장점도 있다.

## 구현 (Implementation)

```python
config = {
    "method": "LoRA",
    "rank": 8,
    "target_modules": ["q_proj", "v_proj"],
    "train_base_model": False,
}
```

Target module, rank, alpha, dropout 선택이 품질과 비용을 좌우한다.

## 복잡도 (Complexity)

Full fine-tuning보다 trainable parameter, optimizer state, GPU memory가 훨씬 작다. 하지만 inference 때 adapter merge 여부와 여러 adapter serving 전략을 고려해야 한다.

## 응용 (Applications)

- 도메인 특화 instruction tuning
- 개인화·조직별 adapter
- 저자원 GPU fine-tuning
- 빠른 실험과 ablation

## 흔한 오해 (Common Misunderstandings)

- PEFT가 항상 full fine-tuning과 같은 성능을 내는 것은 아니다.
- 작은 adapter도 데이터가 나쁘면 overfitting한다.
- QLoRA의 양자화 설정은 품질에 영향을 줄 수 있다.
- Adapter가 많아지면 운영 버전 관리가 복잡해진다.

## TMI

- LoRA adapter는 merge해 단일 가중치처럼 배포할 수 있다.
- Rank를 높이면 표현력은 늘지만 메모리와 overfitting 위험도 늘어난다.
- PEFT는 multi-tenant 모델 운영에서 base model 공유 전략과 잘 맞는다.

## 연습 / 확인 문제 (Exercises)

- LoRA가 파라미터 수를 줄이는 원리를 설명하라.
- Full fine-tuning과 PEFT의 메모리 구성을 비교하라.
- 여러 고객별 adapter를 서빙하는 버전 관리 방식을 설계하라.

## 이어서 읽기 (Reading Path)

- 이전: [Instruction Tuning](Instruction-Tuning.md), [DPO](DPO.md)
- 다음: [Quantization](Quantization.md), [Inference Optimization](Inference-Optimization.md)

## 참조 (References)

- [AI/Deep-Learning/Fine-Tuning.md](../Deep-Learning/Fine-Tuning.md)
- [Reference/Papers.md](../../Reference/Papers.md)
