# 지식 증류 (Knowledge Distillation)

- Level: Advanced
- Prerequisites: [AI/Deep-Learning/Transfer-Learning.md](../Deep-Learning/Transfer-Learning.md), [AI/LLMs/Instruction-Tuning.md](Instruction-Tuning.md)
- Status: Draft
- Reviewed-by: -

---

## 개념 (Concept)

지식 증류는 큰 teacher model의 출력, 분포, reasoning pattern, preference behavior를 작은 student model이 모방하도록 학습하는 방법이다. 목표는 비용을 줄이면서 성능과 행동 양식을 보존하는 것이다.

## 직관 (Intuition)

큰 선생님이 직접 문제를 풀어 보여 주고, 작은 학생 모델이 그 답안 스타일과 판단 기준을 배운다. 정답 label만 보는 것보다 teacher의 확률 분포와 예시가 더 풍부한 신호를 준다.

## 이론 (Theory)

고전 distillation은 teacher soft target을 temperature로 부드럽게 만들어 student가 class 간 상대적 유사성을 학습하게 한다. LLM에서는 response distillation, chain distillation, preference distillation, logits distillation이 사용된다.

Teacher가 틀리거나 편향되면 student도 이를 배운다. 또한 teacher output을 training data로 사용할 때 license, privacy, contamination을 검토해야 한다.

## 구현 (Implementation)

```python
distill_sample = {
    "prompt": "질문",
    "teacher_response": "고품질 응답",
    "student_target": "teacher_response",
}
```

Logits 접근이 가능하면 token distribution KL을, 없으면 generated response SFT를 사용할 수 있다.

## 복잡도 (Complexity)

Teacher inference 비용이 데이터 생성 단계에 든다. Student training은 모델 크기에 따라 싸지만, teacher output 품질 필터링과 다양성 확보가 필요하다.

## 응용 (Applications)

- 작은 assistant 모델 학습
- 도메인 스타일 이전
- reasoning trace 학습
- serving 비용 절감

## 흔한 오해 (Common Misunderstandings)

- Teacher가 크면 항상 좋은 student가 나오는 것은 아니다.
- Distillation은 teacher의 오류와 bias도 복사할 수 있다.
- Synthetic data만으로 다양성이 충분하다고 가정하면 위험하다.
- Student가 teacher보다 특정 분포에서 더 좋아질 수도 있지만 보장되지는 않는다.

## TMI

- Self-distillation은 같은 계열 모델이나 이전 checkpoint를 teacher로 쓰는 방식이다.
- Rejection sampling은 teacher 후보 중 좋은 응답만 골라 SFT data로 만든다.
- Distillation은 quantization, PEFT와 함께 경량화 stack을 이룬다.

## 연습 / 확인 문제 (Exercises)

- Hard label과 soft target distillation의 차이를 설명하라.
- Teacher output data의 품질 필터를 설계하라.
- Distillation과 instruction tuning의 관계를 정리하라.

## 이어서 읽기 (Reading Path)

- 이전: [Instruction Tuning](Instruction-Tuning.md)
- 다음: [Quantization](Quantization.md), [Inference Optimization](Inference-Optimization.md)

## 참조 (References)

- [AI/Deep-Learning/Transfer-Learning.md](../Deep-Learning/Transfer-Learning.md)
- [Reference/Papers.md](../../Reference/Papers.md)
